# -*- coding: utf-8 -*-
# COPYRIGHT 1995-2014 ESRI
#
# TRADE SECRETS: ESRI PROPRIETARY AND CONFIDENTIAL
# Unpublished material - all rights reserved under the
# Copyright Laws of the United States.
#
# For additional information, contact:
# Environmental Systems Research Institute, Inc.
# Attn: Contracts Dept
# 380 New York Street
# Redlands, California, USA 92373
#
# email: contracts@esri.com
"""
Module containing the base class for compound parameter classes.
"""
try:
    from . import Utils
except:
    import Utils



class _DataSetName(str):
    """
    A data set name is a string with special rules when explicitly converted to a string.
    """

    def __new__(cls,
            *arguments,
            **keywords):
        return str.__new__(cls, *arguments, **keywords)

    def __str__(self):
        return "'{0}'".format(str.__str__(self))


class _CompoundParameter(object):
    """
    Base class for specialized, compound parameter classes.

    A compound parameter is a tool parameter which encapsulates multiple values.
    When a tool is called these values are formatted into a single string.

    Most of these parameters start with a keyword.
    """

    @classmethod
    def _useDefault(cls,
            value):
        return Utils.useDefaultArgumentValue(value)

    @classmethod
    def _toString(cls,
            values):
        userProvidedPounds = [value == "#" for value in values]
        result = [str(value) if not cls._useDefault(value) else "#"
            for value in values]

        for i in range(len(result) - 1, -1, -1):
            if result[i] == "#" and not userProvidedPounds[i]:
                del result[i]
            else:
                break

        return " ".join(result)

    @classmethod
    def _toRepresentation(cls,
            values):
        userProvidedPounds = [value == "#" for value in values]
        result = [repr(value) if not cls._useDefault(value)
            else "'#'" for value in values]

        for i in range(len(result) - 1, -1, -1):
            if result[i] == "'#'" and not userProvidedPounds[i]:
                del result[i]
            else:
                break

        return "%s(%s)" % (cls.__name__, ", ".join(result))

    @classmethod
    def _addProperty(cls,
            name,
            defaultValue=None):
        """Add a property to the class.

        name -- Name of the property.
        defaultValue -- Value to use when the default is asked for.
        """
        # Add a property attribute to the class.
        if not hasattr(cls, name):
            setattr(cls, name, property(
                fget=lambda instance:
                    cls.__propertyGetter(instance, name),
                fset=lambda instance, value:
                    cls.__propertySetter(instance, name, value, defaultValue)))

    def __init__(self,
            keyword=None):
        """Create a CompoundParameter.

        keyword -- Argument keyword.
        """
        self._keyword = keyword

    def __eq__(self,
            rhs):
        return self.__class__ == rhs.__class__ and self.__dict__ == rhs.__dict__

    def __propertyGetter(self,
            name):
        assert hasattr(self, "__%s" % (name)), str(type(self))
        return getattr(self, "__%s" % (name))

    def __propertySetter(self,
            name,
            value,
            defaultValue):
        # Creates member variable whenever necessary.
        if self._useDefault(value) and not defaultValue is None:
            value = defaultValue
        setattr(self, "__%s" % (name), value)

_CompoundParameter._addProperty("_keyword")
