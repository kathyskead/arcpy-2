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
import collections
import functools
import inspect
import logging
import operator
import os
import pprint
import re
import sys
import types

__all__ = ['inProcess', 'noisy', 'logcall', 'ArgAdaptor', 'wildcardmatch',
           'listofnamedtuples', 'getstartingpage', 'py3_syntax_report']

def inProcess():
	"""Checks if a script is running in process or not.
           Returns a boolean."""
	return (not ('GP_PROXY_OPS' in os.environ))

def noisy():
    """Turns on the noisiest level of logging for the logging module."""
    logging.getLogger().setLevel(0)

def logcall():
    """Performs a logging.debug line with the current function stack's
       function name with arguments. Useful as a sort of inline tracing.
       Use noisy() to ensure the visibility of these logging calls."""
    logging.debug("%s%s" % (
        sys._getframe().f_back.f_code.co_name,
        inspect.formatargvalues(
            *inspect.getargvalues(
                sys._getframe().f_back
            )
        )
    ))

class ArgAdaptor(object):
    """Function call argument hook -- meant to allow for string
       mappings to integer values.

        Sample usage:

        class MappingConstants(ArgAdaptor):
            __args__ = {
                "format": {"pdf": 1,
                           "svg": 2,
                           "eps": 3
                          }
            }

        @MappingConstants.maskargs
        def exportToVector(filename, format=1):
            full_filename = "%s.%s" % (filename,
                                       {1: 'pdf', 2: 'svg', 3: 'eps'}[format])
            return _c_api.export(full_filename, format)

        Then instead of

        >>> exportToVector("c:\\hello", 2)

        you can call

        >>> exportToVector("c:\\hello", "svg")

        which is easier to understand when inspecting source, and then you can
        add/change literal values as needed without breaking other parts of
        the codebase.

        This function masker will also treat args that are recognized in the
        class as mappings as bitmasks if a collection (set, list, tuple) are
        passed in. For example:

        class BitMaskedFunction(ArgAdaptor):
            __args__ = { "permissions": {"read": 1, "write": 2, "execute": 4} }

        @BitMaskedFunction.maskargs
        def createfile(filename, permissions):
            return _c_api.touchfile(filename, permissions)

        A call to

        >>> createfile("hello.txt", ("read", "execute"))

        will call the function with the value of permissions set to 5
        (composed of 4 | 1).

        PLEASE NOTE: Any STRING value being passed through will be LOWERCASED
        (for case insensitivity reasons), so ensure any string keys are in
        lowercase in the __args__ definition.
    """
    __args__ = {}
    @classmethod
    def maskargs(cls, fn):
        """Wraps a function so arguments map to the name/value pairs specified in cls.__args__"""
        argnames, varargs, varkw, defaults = inspect.getargspec(fn)
        # Special case - get rid of 'self' which gets lost in binding
        is_method = False
        adjusted_argnames = argnames
        if argnames and argnames[0] == 'self' \
                and not isinstance(fn, (staticmethod, classmethod)):
            adjusted_argnames = argnames[1:]
        @functools.wraps(fn)
        def fn_(*a, **k):
            args = list(a)
            for idx, val in enumerate(args):
                if isinstance(val, basestring):
                    val = val.upper()
                if len(argnames) > idx and argnames[idx]:
                    mod_name = "%s.%s" % (fn.__name__, argnames[idx])
                    arg_name = mod_name if mod_name in cls.__args__ else argnames[idx]
                    if arg_name in cls.__args__:
                        if isinstance(val, (set, list, tuple)):
                            args[idx] = 0
                            for ival in val:
                                ivl = (ival.upper()
                                        if isinstance(ival, basestring)
                                        else ival)
                                if ivl in cls.__args__[arg_name] \
                                        and isinstance(ivl, basestring):
                                    val = cls.__args__[arg_name][ivl]
                                    if isinstance(ivl, (int, float, long)):
                                        args[idx] |= val
                                    else:
                                        if not isinstance(args[idx], basestring):
                                            args[idx] = val
                                        else:
                                            args[idx] += "," + val
                                elif isinstance(ivl, (int, float, long)):
                                    args[idx] |= ivl
                                else:
                                    raise ValueError(
                                            "Value %r not found in list" % ival)
                        elif val in cls.__args__[arg_name]:
                            args[idx] = cls.__args__[arg_name][val]
                        elif val not in cls.__args__[arg_name].values():
                            raise ValueError(
                                    "Invalid value for %s: %r (choices are: %r)"
                                    % (arg_name, val,
                                       list(cls.__args__[
                                           arg_name].keys())))
            kw = k.copy()
            for key in kw.keys():
                val = kw[key]
                if isinstance(val, basestring):
                    val = val.upper()
                if key in cls.__args__:
                    if isinstance(val, (set, list, tuple)):
                        kw[key] = 0
                        for ival in val:
                            if ival.upper() in cls.__args__[key]:
                                val = cls.__args__[key][ival.upper()]
                                if isinstance(val, (int, float, long)):
                                    kw[key] |= val
                                else:
                                    if not isinstance(kw[key], basestring):
                                        kw[key] = val
                                    else:
                                        kw[key] += "," + val
                            else:
                                raise ValueError("Value %r not found in list" %
                                                 ival)
                    elif val in cls.__args__[key]:
                        kw[key] = cls.__args__[key][val]
                    elif val not in cls.__args__[key].values():
                        raise ValueError(
                                "Invalid value for %s: %r (choices are: %r)" %
                                (key, val, list(cls.__args__[key].values())))
            return fn(*args, **kw)
        # Add the old argspec to __doc__
        doc_addendum = "%s%s" % (fn.__name__,
                                     inspect.formatargspec(
                                        argnames, varargs, varkw, defaults,
                                        join=', '))
        needs_addendum = fn.__doc__ and not (fn.__name__+'('
                                             in fn.__doc__.strip()
                                                        .split('\n')[0])
        if fn_.__doc__ is None:
            fn_.__doc__ = doc_addendum
        elif needs_addendum:
            fn_.__doc__ = doc_addendum + "\n" + fn_.__doc__
        # functools.wraps doesn't cover __esri_toolinfo__,
        # copy manual or build one
        if hasattr(fn, '__esri_toolinfo__'):
            fn_.__esri_toolinfo__ = fn.__esri_toolinfo__
        else:
            # Build a default __esri_toolinfo__
            toolinfo = ["String|Long|Double:::"] * len(adjusted_argnames)
            for i, arg in enumerate(adjusted_argnames):
                farg = "%s.%s" % (fn.__name__, arg)
                if farg in cls.__args__:
                    toolinfo[i] = "String::%s:" % '|'.join(
                            cls.__args__[farg].keys())
                elif arg in cls.__args__:
                    toolinfo[i] = "String::%s:" % '|'.join(
                            cls.__args__[arg].keys())
            fn_.__esri_toolinfo__ = toolinfo
        return fn_
    @classmethod
    def maskmethods(cls, otherclass):
        "Mask the methods"
        new = {}
        # Find functions
        for name, value in otherclass.__dict__.iteritems():
            # Make decorated versions
            if callable(value) and not name.startswith("_"):
                new[name] = cls.maskargs(value)
        # Push decorated versions out
        for name, value in new.iteritems():
            setattr(otherclass, name, value)

def wildcardmatcher(string, wildcard, compare_no_case=True,
                    return_star_matches=False, anchor=False):
    """Matches ESRI-style wildcard strings.

    INPUTS
    string: string to match pattern against
    wildcard: the wildcard pattern, including *s. To do a literal * use ^*.
    compare_no_case: Case-sensitivity. Default is True,
                     meaning case-insensitive.
    return_star_matches: Boolean indicating the function should return the
                         matching string rather than a True/False value.
    anchor: Anchor match patterns to beginning of line?"""
    assert isinstance(string, basestring), "Must be string"
    assert isinstance(wildcard, basestring), "invalid wildcard (not a string)"
    star_matches = []
    # Caseless matching the default
    if compare_no_case:
        string_, wildcard = string.upper(), wildcard.upper()
    else:
        string_= string
    # Represents a string literal value
    class Value(object):
        def __repr__(self):
            return "<Match %s %r>" % (self.__class__.__name__, self.value)
        def __init__(self, value):
            self.value = value
        def __str__(self):
            if self.value is Ellipsis:
                return ""
            elif self.value in "*.+?^$()[]\\":
                return "\\%s" % str(self.value)
            return self.value
    # Represents * and *x, where x is a literal.
    class LookaheadFor(Value):
        def __str__(self):
            return "(.*)%s" % super(LookaheadFor, self).__str__()
    # Cut up and reassemble the wildcard string, yielding Value and
    # LookaheadFor instances
    def wildcard_state(wildcard):
        while wildcard:
            if wildcard[0] == "^":
                if len(wildcard) > 1:
                    if wildcard[1] == "*":
                        yield Value("*")
                        wildcard = wildcard[1:]
                    else:
                        yield Value("^")
                else:
                    yield Value("^")
            elif wildcard[0] == "*":
                while wildcard and wildcard[0] == "*":
                    wildcard = wildcard[1:]
                if wildcard:
                    if wildcard[:2] == "^*":
                        wildcard = wildcard[1:]
                        yield LookaheadFor("*")
                    else:
                        yield LookaheadFor(wildcard[0])
                else:
                    yield LookaheadFor(Ellipsis)
            else:
                yield Value(wildcard[0])
            wildcard = wildcard[1:]
    # Length of the string matched
    match = 0
    # * needs to behave like +
    bad = False
    regex_str = ''.join(str(wildcard) for wildcard in wildcard_state(wildcard))
    if anchor:
        regex_str = "^" + regex_str
    regex = re.compile(regex_str, re.I if compare_no_case else 0)
    srch = regex.search(string)
    if srch is not None:
        if return_star_matches:
            return srch.group(), srch.groups()
        else:
            return srch.group()
    return None

def wildcardmatch(string, wildcard):
    match = wildcardmatcher(string, wildcard, anchor = True)
    if not match:
        return False
    #return True
    return len(match) == len(string)

_whitespacere = re.compile("^[ \t]*")

def _mergelines(lines, newline):
    if not lines:
        return [newline.rstrip()]
    else:
        last_line, next_line = lines[-1], newline
        wsa_ = _whitespacere.match(last_line)
        wsb_ = _whitespacere.match(next_line)
        wsa = wsa_.group() if wsa_ else ''
        wsb = wsb_.group() if wsb_ else ''
        if wsa == wsb and next_line.strip():
            return lines[:-1] + [lines[-1] + ' ' + next_line.lstrip()]
        else:
            return lines + [next_line.rstrip()]
def _fixedwhitespace(whitespacestring):
    if isinstance(whitespacestring, basestring):
        if isinstance(whitespacestring, str):
            try:
                whitespacestring = whitespacestring.decode("utf-8")
            except:
                pass
        lines = whitespacestring.split("\n")
    else:
        lines = whitespacestring
    lines = [l.replace('\t', '    ') for l in lines]
    if len(lines) > 1:
        # Grab first non-blank line, use its leading whitespace as
        # standard for leading whitespace in subsequent lines
        allines = ([lines[lidx] for lidx in range(1, len(lines))
                               if lines[lidx].strip()]
                   or [''])
        whitespacematch = _whitespacere.match(allines[0])
        whitespacetostrip = (whitespacematch.group() if whitespacematch
                                                     else '')
        if whitespacetostrip:
            for index in xrange(1, len(lines)):
                if lines[index].startswith(whitespacetostrip):
                    lines[index] = lines[index][len(whitespacetostrip):]
    # _mergelines is an attempt to get rid of superfluous newlines
    # in wrapped paragraphs
    return "\n".join(reduce(_mergelines, [None] + lines))

def fixdocstring(object_to_fetch, _builtins, _globals, _locals):
    "Function for ArcGIS desktop - fetches side-panel help for objects"
    try:
        # Drill down in builtins, globals, locals from x.y.z to figure out
        # where exactly the object is question is
        obj_tokens = [item.strip() for item in object_to_fetch.split('.')
                      if item.strip()]
        if not obj_tokens:
            return ""

        object_of_interest, object_parent = None, None

        t1 = obj_tokens[0]
        if t1 in _locals:
            object_of_interest = _locals[t1]
        elif t1 in _globals:
            object_of_interest = _globals[t1]
        elif t1 in _builtins:
            object_of_interest = _builtins[t1]
        else:
            return ""

        try:
            for token in obj_tokens[1:]:
                object_of_interest, object_parent = getattr(object_of_interest, token), object_of_interest
        except:
            return ""

        if object_of_interest:
            # For x.y, if x.__class__.y is a property, then use that doc string
            if object_parent and not isinstance(object_parent, types.ModuleType):
                parent_class = getattr(object_parent, '__class__', None)
                if parent_class:
                    class_attr = getattr(parent_class, obj_tokens[-1], None)
                    if class_attr and isinstance(class_attr, property):
                        if class_attr.__doc__:
                            return object_to_fetch + "\n" + class_attr.__doc__
            # Base types, do a nice representation
            if isinstance(object_of_interest, basestring):
                return repr(object_of_interest)
            elif isinstance(object_of_interest, (int, float, long,
                                                 complex, dict, list,
                                                 tuple)):
                return pprint.pformat(object_of_interest)
            elif object_of_interest in (int, float, long,
                                        complex, dict, list,
                                        tuple):
                return object_of_interest.__doc__
            # Things with an __init__
            elif isinstance(object_of_interest, type):

                constructor = getattr(object_of_interest, '__init__', None)
                if constructor:
                    docstring = _fixedwhitespace(getattr(constructor, '__doc__', '') or
                                                 getattr(object_of_interest, '__doc__', ''))
                    # Fall back to .__class__.__doc__ if
                    # .__class__.__init__.__doc__ is blank
                    if not docstring:
                        docstring = _fixedwhitespace(
                                getattr(object_of_interest, '__doc__', None) or '')
                    if ('see x.__class__.__doc__ for signature' in docstring or
	                'see help(type(x)) for signature' in docstring):
                        docstring = getattr(object_of_interest, '__doc__', None) or ''
                    if obj_tokens[-1] + "(" not in docstring.split('\n')[0]:
                        try:
                            spec = inspect.formatargspec(
                                    *inspect.getargspec(constructor),
                                    join=', ')
                            docstring = (object_to_fetch + spec
                                         + "\n" + docstring)
                        except:
                            pass
                    return docstring
            # Methods/functions
            if isinstance(object_of_interest,
                    (types.FunctionType, types.MethodType)):
                # Grab the doc
                docstring = getattr(object_of_interest, '__doc__',  None) or ''
                if isinstance(docstring, str):
                    try:
                        docstring = docstring.decode("utf-8")
                    except:
                        pass
                # Look to see if the first line looks like a prototype of this
                # function, if not, inject a first-line prototype into it
                firstline = docstring.split('\n')[0]
                if any(t not in firstline for t in (obj_tokens[-1], "(", ")")):
                    spec = inspect.formatargspec(
                            *inspect.getargspec(object_of_interest), join=', ')
                    docstring = (unicode(object_to_fetch + spec + "\n") +
                                 _fixedwhitespace(docstring))
                # Prototype included, treat first line separately from rest
                elif '\n' in docstring:
                    lines = docstring.split('\n')
                    docstring = lines[0] + "\n" + _fixedwhitespace(lines[1:])
                return docstring
            # Common built-in constants
            elif object_of_interest in (True, False, None, Ellipsis):
                return str(object_of_interest)
            # Anything else
            docstring = _fixedwhitespace(getattr(object_of_interest, '__doc__',
                                                 repr(object_of_interest))
                                                    or '')
            if obj_tokens[-1] + "(" not in docstring.split('\n')[0]:
                docstring = object_to_fetch + "\n" + docstring
            return docstring
        return ""
    except:
        # Swallow error; side panel depends on getting back a blank string
        # when it is providing malformed input to this function to know it's
        # malformed.
        return ""
        #import traceback
        #return traceback.format_exc()

def listofnamedtuples(list_of_dicts, tuple_name=''):
    "Return a list of named tuples from a list of dicts (for gp.ListUsers)"
    columns = sorted(
                reduce(
                    operator.or_,
                    (set(dictionary)
                         for dictionary in list_of_dicts),
                    set()))
    tuple_type = collections.namedtuple(tuple_name, columns)
    return [tuple_type(*(dictionary.get(key, None)
                                for key in columns))
                                    for dictionary in list_of_dicts]

def getstartingpage(page_range_string):
    "Get the first specified number in a string like 5-10,11,12"
    all_pages = re.findall("(-?[0-9]+([.][0-9]+)?)( *- *-?[0-9.]+([.][0-9]+)?)?", page_range_string)
    range_list = [(int(start_page), int(end_page[1:]) if end_page else None)
                  for start_page, _, end_page, _ in all_pages]
    return min(p[0] for p in range_list)

ALL_FIX_NAMES = None
REFACTORING_TOOL = None

def get_all_fix_names():
    """Return a sorted list of all available fix names in the given package.
       Modified from implementation in stdlib to look at .pyc and .pyo files
       as well."""
    global ALL_FIX_NAMES

    if ALL_FIX_NAMES is None:
        import lib2to3.fixes
        fixer_dir = os.path.dirname(lib2to3.fixes.__file__)
        fix_names = []
        for name in sorted(os.listdir(fixer_dir)):
            fn, suffix = os.path.splitext(name)
            if fn.startswith("fix_") and suffix.lower() in (".py",
                                                            ".pyc",
                                                            ".pyo"):
                fn = fn[4:]
                fix_names.append(fn)
        ALL_FIX_NAMES = sorted(set(fix_names))
    return ALL_FIX_NAMES

def code_to_python_3(code_block, filename):
    global REFACTORING_TOOL

    if REFACTORING_TOOL is None:
        import lib2to3
        import lib2to3.refactor

        all_fixes = ["lib2to3.fixes.fix_{}".format(l)
                     for l in get_all_fix_names()]
        REFACTORING_TOOL = lib2to3.refactor.RefactoringTool(all_fixes,
                                             options={'print_function': False})
    # + "\n" to make it parse, then [:-1] to chop off tacked-on \n
    return unicode(REFACTORING_TOOL.refactor_string(code_block + u"\n",
                                                    filename))[:-1]

def code_diff_report(python_source, new_source, filename):
    line_commentary = []
    line_changes = {}

    import difflib
    line_number = 1
    for line in difflib.ndiff(python_source.split(u"\n"),
                              new_source.split(u"\n")):
        state = line[0]
        line_text = line[2:].rstrip()

        if state == " ":
            line_number += 1
        elif state == "+":
            if line_number in line_changes:
                line_change = line_changes[line_number]
                change_text = "Line {}: {} -> {}".format(line_number,
                                                         line_change,
                                                         line_text)
                line_commentary.append(change_text)
                del line_changes[line_number]
            else:
                change_text = "Line {}: {}".format(line_number, line_text)
            line_number += 1
        elif state == "-":
            line_changes[line_number] = line_text
        elif state == "?":
            pass
    return "\n".join(line_commentary)

def py3_syntax_report(python_source, filename=u"<script>"):
    "Return a report on Python 3 compatibility"
    # Assume UTF-8 if we don't have unicode
    if not isinstance(python_source, unicode):
        python_source = python_source.decode("utf-8")
    python_source = python_source.replace("\r\n", "\n")
    new_source = code_to_python_3(python_source, filename)
    if python_source == new_source:
        return "Python 3 OK"
    elif python_source and not new_source:
        return "Syntax Error in Python 2"
    else:
        return code_diff_report(python_source, new_source, filename)
