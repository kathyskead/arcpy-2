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
from operator import attrgetter

arcobject_to_python_class_mapping = {}

def initialize_conversion_mapping():
    from .arcobjects import FieldInfo, Field, Index, Cursor, Row, \
                            Geometry, SpatialReference, FieldMappings, \
                            FieldMap, Point, Extent, RandomNumberGenerator, \
                            Array, ValueTable, FieldInfo, NetCDFFileProperties, \
                            Result, RecordSet, Parameter, Schema, Filter, \
                            ArcSDESQLExecute
    from .._mapping import MapDocument, PageLayout, DataFrame, DataFrameTime, DataDrivenPages, \
                           Layer, LayerTime, BaseLayerSymbology, TextElement, GraphicElement, \
                           TableView, LabelClass, StyleItem
    for k, v in (
        ("geoprocessing describe field object",  Field),
        ("geoprocessing describe index object",  Index),
        ("geoprocessing cursor object",  Cursor),
        ("geoprocessing row object",  Row),
        ("geoprocessing describe data object",  None),
        ("geoprocessing describe geometry object",  Geometry),
        ("geoprocessing spatial reference object",  SpatialReference),
        ("geoprocessing field mapping object",  FieldMappings),
        ("geoprocessing field map object",  FieldMap),
        ("geoprocessing point object",  Point),
        ("geoprocessing extent object",  Extent),
        ("geoprocessing random number generator object",  RandomNumberGenerator),
        ("geoprocessing array object",  Array),
        ("geoprocessing value table object",  ValueTable),
        ("geoprocessing field info object",  FieldInfo),
        ("geoprocessing NetCDF Workspace object",  NetCDFFileProperties),
        ("geoprocessing server result object",  Result),
        ("geoprocessing record set object",  RecordSet),
        ("geoprocessing parameter object",  Parameter),
        ("geoprocessing schema object",  Schema),
        ("geoprocessing filter object",  Filter),
        ("geoprocessing ArcSDE SQL Execute object",  ArcSDESQLExecute),
        ("geoprocessing Map object",  MapDocument),
        ("geoprocessing Page Layout object",  PageLayout),
        ("geoprocessing Page Layout DDP object",  DataDrivenPages),
        ("geoprocessing pageLayout element object",  GraphicElement),
        ("geoprocessing Data Frame object",  DataFrame),
        ("geoprocessing Data Frame Time object",  DataFrameTime),
        ("geoprocessing Layer object",  Layer),
        ("geoprocessing Layer Time object",  LayerTime),
        ("geoprocessing Layer Symbology object",  BaseLayerSymbology),
        ("geoprocessing Text Element object",  TextElement),
        ("geoprocessing Standalone Table object",  TableView),
        ("geoprocessing Label Properties object",  LabelClass),
        ("geoprocessing Style Item object",  StyleItem),
    ):
        arcobject_to_python_class_mapping[k] = v

def convertArcObjectToPythonObject(obj):
    try:
        name=type(obj).__name__
        if name in arcobject_to_python_class_mapping:
            obj_conversion = arcobject_to_python_class_mapping[name]
            if obj_conversion is None:
                return obj
            else:
                from ._base import FromScriptingArcObject
                return FromScriptingArcObject(obj_conversion, obj)
    except AttributeError:
        pass

    if isinstance(obj, (int, long, float, complex, basestring)):
        return obj
    elif isinstance(obj, (list, tuple)):
        return type(obj)(map(convertArcObjectToPythonObject, obj))
    elif isinstance(obj, dict):
        return dict((convertArcObjectToPythonObject(k),
                     convertArcObjectToPythonObject(v))
                            for (k, v) in obj.iteritems())
    else:
        return obj
