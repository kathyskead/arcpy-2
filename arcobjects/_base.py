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
from .. import gp
from .arcobjectconversion import convertArcObjectToPythonObject
import functools

__all__ = ['_BaseArcObject', 'passthrough_attr', 'FromScriptingArcObject']

class _ArcobjectPassthrough(object):
    def __getattr__(self, attr):
        if attr == "__methods__":
            return []
        x = getattr(self._arc_object, attr)
        if not callable(x):
            return convertArcObjectToPythonObject(x)
        raise AttributeError("%s" % attr)
    def __setattr__(self, attr, val):
        ao = val
        try:
            ao = val._arc_object
        except (AttributeError, RuntimeError):
            pass
        return setattr(self._arc_object, attr, ao)
    def __delattr__(self, attr):
        return delattr(self._arc_object, attr)

class _BaseArcObject(object):
    _arc_object = None
    def __init__(self, *args, **kwargs):
        """Wrapper for ArcGIS scripting Arc Objects --
           Create a new object instance if no reference is passed in."""
        super(_BaseArcObject, self).__init__()
        self._arc_object = gp._gp.CreateObject(self.__class__.__name__,
                    *((arg._arc_object if hasattr(arg, '_arc_object') else arg)
                        for arg in args))
        for attr, value in kwargs.iteritems():
            setattr(self._arc_object, attr, value)
        self._go()
    def _go(self):
        if getattr(self, '__passthrough_to_ao__', False):
            self.__class__ = type(self.__class__.__name__, (self.__class__, _ArcobjectPassthrough), self.__dict__)
    def __repr__(self):
        return "<%s object at %s[%s]>" % (self.__class__.__name__,
                         hex(id(self)),
                         hex(id(self._arc_object)))
    def __str__(self):
        return str(self._arc_object)
    def __cmp__(self, other):
        a1, a2 = id(self), id(other)
        a1 = getattr(self, '_arc_object', a1)
        if hasattr(a1, '_pointer'):
            a1 = getattr(a1, '_pointer', a1)
        a2 = getattr(other, '_arc_object', a2)
        if hasattr(a2, '_pointer'):
            a2 = getattr(a2, '_pointer', a2)
        return cmp(a1, a2)

def passthrough_attr(attr_name, doc=None):
    def _get(self):
        try:
            return convertArcObjectToPythonObject(getattr(self._arc_object, attr_name))
        except AttributeError:
            raise NameError(
                    gp.getIDMessage(89013,
                        "The attribute %r is not supported on this instance of %s.") %
                    (attr_name, self.__class__.__name__))
    def _set(self, val):
        def cval(val):
            try:
                return getattr(val, '_arc_object')
            except (RuntimeError, AttributeError):
                if isinstance(val, (set, list)):
                    return type(val)(map(cval, val))
                else:
                    return val
        try:
            return setattr(self._arc_object, attr_name, cval(val))
        except AttributeError:
            raise NameError(
                    gp.getIDMessage(89013,
                        "The attribute %r is not supported on this instance of %s.") %
                    (attr_name, self.__class__.__name__))
    def _del(self, val):
        return delattr(self._arc_object, val)
        delattr(self, val)
    return property(_get, _set, None, doc)

def FromScriptingArcObject(cls, obj):
    """Bypass the constructor for objects created from existing arc objects."""
    # Custom routine?
    if hasattr(cls, '__from_scripting_arc_object__'):
        return cls.__from_scripting_arc_object__(obj)
    # No; do normal thing.
    class conversion(object): pass
    new_obj = conversion()
    new_obj._arc_object = obj
    new_obj.__class__ = cls
    new_obj._go()
    return new_obj
