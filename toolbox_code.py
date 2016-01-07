# -*- coding: utf-8 -*-
#COPYRIGHT 2012 ESRI
#
#TRADE SECRETS: ESRI PROPRIETARY AND CONFIDENTIAL
#Unpublished material - all rights reserved under the
#Copyright Laws of the United States.
#
#For additional information, contact:
#Environmental Systems Research Institute, Inc.
#Attn: Contracts Dept
#380 New York Street
#Redlands, California, USA 92373
#
#email: contracts@esri.com
"""Routines for generating python code from a toolbox."""

import codecs
import collections
import glob
import imp
import itertools
import keyword
import locale
import os
import re
import sys
import textwrap
import types
import xml.dom.minidom

from arcpy import gp

from os.path import relpath

HTML_RE = re.compile('(</?[A-Z]+( [A-Za-z]+="[^"]*")*/?>)')
def text_for_node(somenode):
    """Returns a safe representation of all the text in a dom.minidom node"""
    if isinstance(somenode, list):
        return " ".join(text_for_node(node) for node in somenode)
    elif somenode is None:
        return ""
    elif somenode.nodeType == somenode.ELEMENT_NODE:
        if somenode.tagName.lower() == "bullet_item":
            return "\n\n* " + " ".join(text_for_node(node) for node in somenode.childNodes) + "\n"
        elif somenode.tagName.lower() == "link":
            return ""
        lines = ["\n".join(textwrap.wrap(line.replace(ur'           \u2014',ur'\u2014'), 80))
                 for line in
                     ("".join(text_for_node(node) for node in somenode.childNodes).split("\n"))]
        return "\n".join(lines)
    elif somenode.nodeType in (somenode.TEXT_NODE, somenode.ENTITY_NODE):
        if somenode.data.strip():
            data = somenode.data
            # Strip out HTML and HTML-like data in the text nodes
            for replace_data in set(x[0] for x in HTML_RE.findall(somenode.data)):
                data = data.replace(replace_data, ' ')
            return data.replace("\n", " ").replace("  ", " ")
    return ""

def indent_text(astring, indentation=4):
    return '\n'.join((" " * (indentation if line else 0)) + line
                      for linenum, line in enumerate(astring if isinstance(astring, list)
                                                             else astring.split('\n'))).strip()

def indent_unicode_text(astring, indentation=4):
    itext = '\n'.join((u" " * (indentation if line else 0)) + line
                      for linenum, line in enumerate(astring if isinstance(astring, list)
                                                             else astring.split(u'\n'))).strip()
    return itext

def safe_name(*names, **kw):
    """Creates a python-safe identifier name from a set of provided strings"""
    appropriate_name_re = re.compile("^[_A-Za-z][_A-Za-z0-9]*$")
    front, back, bad = (kw.get('front', None),
                        kw.get('back',  None),
                        kw.get('bad',   None))
    def good(name):
        if not name:
            return False
        if bad:
            if name in bad:
                return False
        return name not in keyword.kwlist and appropriate_name_re.match(name)
    for name in names:
        if not name:
            continue
        if good(name):
            return name
        if front:
            if good(front + name):
                return front + name
        if back:
            if good(name + back):
                return name + back
    if kw.get('no_raise', None):
        return None
    raise ValueError(gp.getIDMessage(89008) % #"Cannot create good identifier from options: %s" %
                      repr(names))

def arglist_for_tool(tool, long_mode=False):
    """Builds a list of names for arguments in the tool's calling function"""
    seen_names = set()
    arglist = []

    try:
        md_string = tool.metadata.encode("utf-8")
        md = xml.dom.minidom.parseString(md_string)
        params = md.getElementsByTagName("param")
    except:
        md_string, md, params, param_names = None, None, None, None
    try:
        if params is not None:
            param_names = [paramnode.attrib.get('expression', '').strip()
                           for paramnode in params]
        else:
            param_names = [paramitem.name for paramitem in tool.parameters]
    except:
        param_names = []
    param_names += ([None] * len(tool.parameters))
    try:
        for index, parameter in enumerate(t for t in tool.parameters if t.parametertype != "Derived"):
            name = safe_name(parameter.name,
                             parameter.displayname.replace(' ', '_').replace('-', '_'),
                             'parameter_%i' % (index+1), # fallback
                             front='_',
                             bad=seen_names)
            seen_names.add(name)
            if long_mode:
                try:
                    if parameter.multivalue or (isinstance(parameter.datatype, basestring)
                                                    and 'value table' in
                                                        parameter.datatype.lower()):
                        name = "%s;%s..." % (name, name)
                except (RuntimeError, AttributeError):
                    pass
            arglist.append(param_names[index] if param_names[index] else name)
    except:
        arglist = ['*a']
    return arglist

def docstring_for_tool(tool):
    """Builds the documentation string for an individual tool"""
    def sstr(string):
        return string # ''.join(x for x in string if 32 <= ord(x) < 128)
    fn_name = "%s%s" % (tool.name, "_%s" % tool.toolbox.alias
                                           if safe_name(tool.toolbox.alias, no_raise=True)
                                           else '')
    arglist = arglist_for_tool(tool, True)
    arg_string = "argument, argument, argument, ..."
    if isinstance(arglist, list):
        arg_string_list = []
        try:
            params = tool.parameters
        except:
            params = []
        for param, argname in zip([p for p in params if (p.parametertype != "Derived") ], arglist):
            if param.parametertype != "Required":
                arg_string_list.append("{%s}" % argname)
            else:
                arg_string_list.append(argname)
        arg_string = ", ".join(arg_string_list)
    # First line (usage)
    yield "%s(%s)" % (fn_name, arg_string)
    inputs, outputs = [], []
    # Now attempt to fetch XML metadata and make more documentation with that
    md = None
    try:
        param_info_types = [[param.displayname
                if isinstance(param.displayname, unicode)
                    else param.displayname.decode("utf-8")]
                             for param in tool.parameters]
    except:
        param_info_types = [[x if isinstance(x, unicode) else x.decode("utf-8")] for x in arglist]
    try:
        md_string = tool.metadata.encode("utf-8")
        md = xml.dom.minidom.parseString(md_string)
        params = md.getElementsByTagName("param")
        if params:
            param_info_types = [[text_for_node(y).replace('\n\n\n', '\n\n').strip()
                                     for y in ((p.getElementsByTagName('pythonReference') or
                                                p.getElementsByTagName('dialogReference')))
                                ] for p in params]
            if len(param_info_types) < len(tool.parameters):
                param_info_types += [[param.displayname]
                                     for param in
                                     tool.parameters[len(param_info_types):]]
        summarynodes = (md.getElementsByTagName('summary') or md.getElementsByTagName('idAbs'))
        if summarynodes:
            description = summarynodes[-1]
            description_text = text_for_node(description).strip()
            if description_text:
                yield ""
                yield "        " + indent_text(description_text.split('\n'), 8)
    except Exception, e: # Just sort of pretend the whole thing never happened
        yield ""
        #import traceback
        #yield traceback.format_exc()

    # Inputs/outputs
    try:
        tool.parameters
    except:
        return # Give up if params aren't gettable.
    for index, parameter in enumerate([p for p in tool.parameters if (p.parametertype != "Derived")]):
        ltb, rtb = ('(', ')') if parameter.parametertype == "Required" else ('{', '}')
        param_string = (u"      %s %s%s%s" % ((parameter.name or ''),
                                              ltb,
                                              parameter.datatype if isinstance(parameter.datatype, basestring)
                                                                    else u' / '.join(parameter.datatype)
                                                  if not (parameter.filter and
                                                          parameter.filter.list and
                                                          parameter.filter.type != "ValueList")
                                                  else u"|".join(unicode(pl) for pl in
                                                                parameter.filter.list),
                                              rtb))
        to_append = None
        if parameter.direction == "Input":
            to_append = inputs
        else:
            to_append = outputs
        tabbing = len(param_string)

        indented_text = (indent_unicode_text(u'\n'.join(param_info_types[index]), 10)
                         if param_info_types[index] else u'')
        try:
            if indented_text:
                param_string += u":\n          " + indented_text
        except Exception, e:
            pass

        to_append.append(param_string)
    if inputs or outputs:
        yield ''
    if inputs:
        yield "     INPUTS:"
        for line in inputs:
            yield line
        if outputs:
            yield ''
    if outputs:
        yield "     OUTPUTS:"
        for line in outputs:
            yield line

def function_name_for_tool(tool, alt_alias=None, use_alt_alias=True):
    alias = (use_alt_alias and alt_alias) or tool.toolbox.alias
    fn_name = "%s%s" % (tool.name, "_%s" % alias
                                           if alias
                                              and ' ' not in alias
                                           else '')
    return str(fn_name)

def code_for_tool(tool, include_add_toolbox=False, alt_alias=None, use_alt_alias=True):
    """Builds a code snippet for an individual tool"""
    arglist = arglist_for_tool(tool)
    fn_name = function_name_for_tool(tool, alt_alias)
    gp_fn_name = function_name_for_tool(tool, alt_alias, use_alt_alias)

    yield "@gptooldoc(%r, None)" % str(fn_name)
    yield "def %s(%s):" % (tool.name,
                                                ', '.join("%s=None" % arg
                                                if '*' not in arg else arg
                                                for arg in arglist))

    fn_doc = u"\n".join(line if isinstance(line, unicode)
                            else line.decode("utf-8")
                            for line in docstring_for_tool(tool))
    yield u'    """%s"""' % (fn_doc.replace('"""',"'''"))
    argstring = ("(%s%s)" % (', '.join(arglist)
                            if all('*' not in arg for arg in arglist)
                            else ','.join(a.lstrip('*') for a in arglist),
                            ',' if len(arglist) == 1
                                and not arglist[0].startswith('*')
                                else ''))
    yield "    from arcpy.geoprocessing._base import gp, gp_fixargs"
    yield "    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject"
    yield "    try:"
    yield "        retval = convertArcObjectToPythonObject(gp.%s(*gp_fixargs(%s, True)))" % (gp_fn_name, argstring)
    try:
        mod = __import__('arcpy._%s' % getattr(tool.toolbox, 'alias', ''))
        if (tool.name + "Result") in mod.__dict__:
            yield "        from arcpy._%s import %sResult" % (tool.toolbox.alias, tool.name)
            yield "        retval.__class__ = %sResult" % (tool.name)
    except ImportError:
        pass
    yield "        return retval"
    yield "    except Exception, e:"
    yield "        raise e"

def docstring_for_toolbox(toolbox):
    """Returns a documentation string for a toolbox"""
    try:
        md_string = toolbox.metadata.encode("utf-8")
        md = xml.dom.minidom.parseString(md_string)
        abstract = (md.getElementsByTagName('idAbs') or [None]).pop()
        return text_for_node(abstract).strip()
    except:
        return "Toolbox %s" % toolbox.displayname

def code_for_toolbox(toolbox, include_add_toolbox, relative_to=None, system_toolbox=False, alt_alias=None, use_alt_alias=True):
    def toolset(tool):
        return os.path.dirname(tool.pathname)[len(tool.toolbox.pathname)+1:]
    toolsets = collections.defaultdict(list)
    for tool in toolbox.tools:
        tool.parameters # This is necessary to rehydrate some tools.
        toolsets[toolset(tool)].append(tool)
    yield '# -*- coding: utf-8 -*-'
    yield u'"""%s"""' % docstring_for_toolbox(toolbox).replace('"""', "'''")
    yield "__all__ = %r" % ([str(tool.name) for tool in toolbox.tools],)
    yield "__alias__ = %r" % (alt_alias if alt_alias else toolbox.alias)
    if not system_toolbox:
        yield "__pathname__ = %r" % (toolbox.pathname if not relative_to
                                     else os.path.relpath(toolbox.pathname,
                                                          os.path.dirname(relative_to)))
    yield "from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs"
    yield "from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject"
    if system_toolbox:
        alias = getattr(toolbox, 'alias', '').strip().lower()
        if alias:
            try:
                __import__('arcpy._%s' % alias)
                yield "import _%s" % alias
                yield "from _%s import *" % alias
                yield "__all__ += _%s.__all__" % alias
            except ImportError:
                pass # No special hidden _alias module found
    alt_alias_string = ", {}".format(repr(alt_alias)) if (alt_alias and use_alt_alias) else ''
    # Add the boilerplate gp.addToolbox() stanza
    if include_add_toolbox or relative_to:
        yield "# Make sure toolbox is in memory"
        # Absolute path, easy
        yield "try:"
        if not relative_to:
            yield "    gp.addToolbox(__pathname__{})".format(alt_alias_string)
        else:
            yield "    # This python file was saved with a relative path"
            # Get where the .tbx will be relative to the output .py file
            relative_path = relpath(toolbox.pathname,
                                    os.path.dirname(relative_to))
            # Put it together at runtime
            yield "    import os"
            yield "    gp.addToolbox("
            yield "       os.path.abspath("
            yield "           os.path.join("
            yield "              os.path.dirname(__file__),"
            yield u"              %r))%s)" % (relative_path, alt_alias_string)
        yield "except RuntimeError:"
        yield "    raise ImportError('Could not import toolbox %%r' %% %r)" % (toolbox.pathname
                                                                               if not relative_to
                                                                               else relative_path)
        yield ""
    yield ""
    for toolsetname in sorted(toolsets):
        if toolsetname.strip():
            yield "# %s toolset" % toolsetname
        else:
            yield "# Tools"
        for tool in sorted(toolsets[toolsetname],
                           lambda x, y: cmp(x.name, y.name)):
            for line in code_for_tool(tool, include_add_toolbox, alt_alias, use_alt_alias):
                yield line
            yield ""
        yield ""
    yield "# End of generated toolbox code"
    yield "del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject"

def generate_toolbox_module(tbxfile, output_file=None,
                            include_gp_addtoolbox=False,
                            relative_paths=False,
                            system_toolbox=False,
                            alt_alias=None,
                            use_alt_alias=True):
    """Loads a file toolbox (.tbx) and creates Python code for it.
       if output_file is a string, it will treat it as a filename
       to open."""
    if isinstance(tbxfile, basestring):
        gp.addToolbox(tbxfile)
        toolbox = gp.createObject("Toolbox", tbxfile)
    else:
        toolbox = tbxfile
        gp.addToolbox(tbxfile.pathName, alt_alias if use_alt_alias else None)
    if relative_paths:
        if not isinstance(output_file, basestring):
            raise RuntimeError(gp.getIDMessage(89009,
                               "Cannot generate a path relative to unknown output"))
        relative_path = output_file
    else:
        relative_path=None
    code = u"\n".join(line if isinstance(line, unicode)
                           else line.decode("utf-8")
                        for line in
                            code_for_toolbox(toolbox,
                                             include_gp_addtoolbox,
                                             relative_path,
                                             system_toolbox,
                                             alt_alias,
                                             use_alt_alias))
    if output_file:
        open(output_file, 'wb').write(code.encode('utf-8'))
        return code
    else:
        newmodule = imp.new_module(alt_alias or toolbox.alias)
        try:
            code = code.encode('utf-8')
        except:
            try:
                code = code.encode('utf-8', 'replace')
            except:
                # Really, REALLY invalid unicode. Strip down to ASCII.
                code = ''.join(x for x in code if 32 <= ord(x) < 128)
        mycode = compile(code,
                         toolbox.pathName.encode(locale.getpreferredencoding() or "ascii",
                                                 "replace"),
                         'exec')
        # Virtual import
        exec mycode in newmodule.__dict__
        return newmodule

def import_toolbox(tbxfile, module_name=None):
    """Loads a file toolbox(.tbx) and creates a Python module for it.

       Sample usage:

       arcpy.import_toolbox(r"C:\Data\ArcToolbox\Sample Toolbox\demo.tbx",
                             'toolboxsample')

       This will then generate a python module for demo.tbx and make it
       available for import as arcpy.toolboxes.toolboxsample

       If the second argument is not provided, the function will use the alias
       of the toolbox, if it is set and a valid Python identifier."""
    use_alt_alias = True
    if isinstance(tbxfile, basestring):
        toolbox = gp.createObject("Toolbox", tbxfile)
        if (tbxfile.lower().startswith('http://') or
            tbxfile.lower().startswith("https://")):
            use_alt_alias = False
    else: # Assume non-strings are instances of Toolbox
        toolbox = tbxfile
    mymodule = generate_toolbox_module(toolbox, None, False, False, False, module_name, use_alt_alias)
    import arcpy
    for tool in mymodule.__all__:
        setattr(arcpy, tool + ('_' + mymodule.__alias__
                               if mymodule.__alias__ else ''),
                getattr(mymodule, tool, None))
    # Module already exists in arcpy?
    if hasattr(arcpy, mymodule.__alias__):
        existing_module = getattr(arcpy, mymodule.__alias__)
        # Is it a module?
        if not hasattr(existing_module, '__all__'):
            existing_module.__all__ = []
        # Add to the __all__
        existing_module.__all__ += mymodule.__all__
        # Then add the tool functions
        for tool in mymodule.__all__:
            setattr(existing_module, tool,
                    getattr(mymodule, tool, None))
    # arcpy.X = mymodule
    else:
        setattr(arcpy, mymodule.__alias__, mymodule)
    return mymodule
