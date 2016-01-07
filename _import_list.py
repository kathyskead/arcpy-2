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
"""Recursively determines all Python library dependencies for a given Python
   script. Optionally can bundle files together as a .zip using zipout()."""
import dis
import imp
import marshal
import os.path
import site
import sys

__all__ = ['import_list', 'zipout']

_builtin_prefixes = None

def _disassemble(code_object):
    code_string = code_object.co_code
    linestarts = dict(dis.findlinestarts(code_object))
    labels = list(dis.findlabels(code_string))
    i = 0
    while i < len(code_string):
        opcode = ord(code_string[i])
        opname = dis.opname[opcode]
        i += 1
        if opcode >= dis.HAVE_ARGUMENT:
            oparg = (ord(code_string[i]) + ord(code_string[i+1])*256)
            if opcode in dis.hasconst:
                oparg = code_object.co_consts[oparg]
            elif opcode in dis.hasname:
                oparg = code_object.co_names[oparg]
            yield opname, oparg
            if hasattr(oparg, 'co_code'):
                for oc, oa in _disassemble(oparg):
                    yield oc, oa
            i += 2
        else:
            yield opname, None

def _imports_for_code(filename, source=None):
    if not source:
        if os.path.splitext(filename)[1].lower() in (".pyc", ".pyo"):
            # PYC files are 4 byte magic, 4 byte timestamp, rest marshaled data
            code_object = marshal.loads(open(filename, 'rb').read()[8:])
        else:
            try:
                if not source:
                    source = open(filename, 'rb').read().replace("\r", "")
                code_object = compile(source, filename, 'exec')
            except (IOError, SyntaxError):
                return
    if code_object:
        for opcode, opval in _disassemble(code_object):
            if opcode in ('IMPORT_NAME',):
                yield opval

def _is_builtin(pkgname):
    if not pkgname:
        return True
    pkgtop = pkgname.split('.')[0]
    try:
        path = imp.find_module(pkgtop)[1]
    except ImportError:
        return True
    global _builtin_prefixes
    if _builtin_prefixes is None:
        _builtin_prefixes = []
        if sys.platform == 'win32':
            join_prefixes = (('DLLs',), ('Lib',), ('lib',), ('lib', 'lib-tk'))
        else:
            join_prefixes = (('local', 'lib'), ('lib',))
        for prefix in join_prefixes:
            for site_prefix in set(site.PREFIXES):
                _builtin_prefixes.append(os.path.join(site_prefix, *prefix))
    if imp.is_builtin(path):
        return True
    elif os.path.dirname(path) in _builtin_prefixes:
        return True
    return False

def _import_path_for(filename):
    if os.path.isdir(filename):
        return [filename] + sys.path
    elif os.path.splitext(filename)[1].lower() == ".zip":
        return [filename] + sys.path
    return [os.path.dirname(filename)] + sys.path

def _import_list(filename, source=None, seen=None):
    if seen is None:
        seen = set()
    if os.path.isdir(filename):
        initpy = os.path.join(filename, '__init__.py')
        if (os.path.exists(initpy) and os.path.isfile(initpy)):
            for path, dirs, filenames in os.walk(filename):
                for fname in filenames:
                    fname = os.path.join(path, fname)
                    if os.path.splitext(fname)[1].lower() in ('.py', '.pyc'):
                        for extra_import_ in _import_list(fname, seen=seen):
                            if not extra_import_[1].startswith(filename):
                                yield extra_import_
        return
    sys.path.append(os.path.dirname(filename))
    for item in _imports_for_code(filename, source):
        if _is_builtin(item):
            continue # Skip system and builtin modules
        itemtop = item.split('.')[0]
        if itemtop in seen:
            continue

        (file, path, (ex, mode, modtype)) = imp.find_module(itemtop,
                                                   _import_path_for(filename))

        seen.add(itemtop)
        yield (itemtop, path, modtype)
        if modtype in (imp.PY_SOURCE, imp.PKG_DIRECTORY):
            for import_ in _import_list(path, seen=seen):
                yield import_
    sys.path.pop()

def import_list(filename, source=None):
    """Return a list of tuples (modulename, modulepath, moduletype) for the
       given python source file. moduletype is a constant defined in
       imp.PY_* and the other two are strings. Recursive."""
    return sorted(set(_import_list(filename, source)))

def zipout(filename, tempzip, source=None):
    """Output a zip file with all dependencies of the script file specified by
       the parameter filename to the path tempzip."""
    import zipfile
    outzip = zipfile.ZipFile(tempzip, 'w')
    for modname, modpath, modtype in import_list(filename, source):
        if os.path.isfile(modpath):
            outzip.write(modpath, os.path.basename(modpath))
        elif os.path.isdir(modpath):
            for path, dirs, files in os.walk(modpath):
                for file in files:
                    print outzip.write(os.path.join(path, file),
                                       os.path.join(modname,
                                                   os.path.relpath(
                                                        os.path.join(path,
                                                                     file),
                                                        modpath)))
    outzip.close()

if __name__ == "__main__":
    import sys
    fname = sys.argv[1] if len(sys.argv) > 1 else sys.argv[0]
    print " == Imports for %r == " % fname
    dependencies = map(repr, import_list(fname))
    print ",\n".join(dependencies)
    #zipout(fname, "out.zip")
