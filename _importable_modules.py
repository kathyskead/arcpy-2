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
import imp
import os
import sys

__all__ = ['importable_modules']

importable_modules = []

def _refresh():
    global importable_modules
    module_list = set()
    suffixes = set(x[0].lower() for x in imp.get_suffixes())
    syspath = map(os.path.normcase, sys.path)
    for apath in syspath:
        if not apath:
            continue
        for path, dirs, files in os.walk(apath):
            path = os.path.normcase(path)
            if path != apath and path in syspath:
                continue
            elif path.lower().endswith(".egg"): # Skip .egg paths
                continue
            modname = os.path.relpath(path, apath).replace(os.sep, ".") + "."
            if "-" in modname:
                continue
            elif modname == "..":
                modname = ""
            for module in [file for file in files if os.path.splitext(file)[1].lower() in suffixes]:
                amod = modname + os.path.splitext(os.path.basename(module))[0]
                if amod.endswith(".__init__"):
                    amod = os.path.splitext(amod)[0]
                if not os.path.basename(module).startswith("_"):
                    module_list.add(amod)
    importable_modules = sorted(module_list)

_refresh()

if __name__ == "__main__":
    print "\n".join(importable_modules)
