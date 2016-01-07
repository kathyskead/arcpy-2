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
Module containing utilities used by the other modules.
"""
import types
from arcpy import gp, Extent

try:
    long, basestring
except NameError:  # Python 3
    long = int
    basestring = unicode = str


class StateSwapper(object):

    SingleRasterResult = 1
    NoSingleRasterResult = 2

    def __init__(self,
            outputCategory=SingleRasterResult):
        self.__outputCategory = outputCategory

    def __call__(self,
            wrapper):
        def swapper(
                *args,
                **kwargs):
            # New data created by the wrapper is temporary and should not
            # automatically be added to the toc. Save current state so we can
            # restore it later.
            addToResultState = gp._gp.AddOutputsToMap

            if self.__outputCategory == self.SingleRasterResult:
                gp._gp.AddOutputsToMap = False

            result = None

            try:
                result = wrapper(*args, **kwargs)
            finally:
                # Reset the geoprocessor state to the original setting.
                # Whatever the result of calling the wrapper function, this
                # code will run.
                gp._gp.AddOutputsToMap = addToResultState

            return result

        return swapper


def compoundParameterToString(
        parameter,
        cls):
    """
    Convert parameter if it is a compound parameter object, otherwise do
    nothing.

    parameter -- Parameter to a function.
    cls -- Compound parameter class or base class of compound parameter class
           family.
    """
    if isinstance(parameter, cls):
        # Instance has the expected type.
        if cls == Extent:
            # trac266
            return "%g %g %g %g" % (parameter.XMin, parameter.YMin,
                parameter.XMax, parameter.YMax)
        else:
            return str(parameter)
    else:
        return parameter


def multiValueCompoundParameterToString(
        parameter,
        cls):
    """
    Convert parameter if it is a single compound parameter object or a list of
    compund parameter objects, otherwise do nothing.

    parameter -- Parameter to a function.
    cls -- Compound parameter class or base class of compound parameter class
           family.
    """
    if not isinstance(parameter, list):
        return compoundParameterToString(parameter, cls)
    else:
        if parameter and all(map(lambda item: isinstance(item, cls),
                parameter)):
            return ";".join(map(lambda item: str(item), parameter))
        else:
            return parameter


def isNumerical(
        object):
    """
    Return whether object is an instance of one of Python's built-in numeric
    types.

    object -- Object to test.
    """
    return isinstance(object, (bool, int, long, float, complex))


def flattenLists(
        iterable):
    """
    Flatten nested list elements in the iterable passed in, non-recursively.

    Return a list.
    """
    result = []

    if isinstance(iterable, basestring):
        result.append(iterable)
    else:
        for item in iterable:
            if isinstance(item, list):
                result += item
            else:
                result.append(item)

    return result


def argumentValueEqualsString(
        argument,
        string):
    return isinstance(argument, (str, unicode)) and argument == string


def useDefaultArgumentValue(
        argument):
    return argument is None or (isinstance(argument, (str, unicode)) and
        argument in ["", "#"])
