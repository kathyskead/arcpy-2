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
import itertools
import os.path
import operator
import re
import types
import weakref
import xml.etree.ElementTree

from arcpy import env
from arcpy import gp
wildcardmatch = gp.wildcardMatch
from arcpy.arcobjects._base import _BaseArcObject, FromScriptingArcObject
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

__all__ = ['SupportsPropertyMixin', 'ArrayMixin', 'CursorMixin',
           'GeometrySpecializationMixin', 'LayoutElementSpecializationMixin',
           'LayerSymbologySpecializationMixin', 'RasterClassifiedExclusionMixin',
           'LayerIterationMixin', 'LayerMixin', 'TableViewMixin',
           'ImageFileExportMixin', 'DataFrameMixin', 'MapDocumentMixin',
           'PointMixin', 'ResultMixin']

pagesize_tuple = collections.namedtuple('PageSize', ['width', 'height'])
bookmark_tuple = collections.namedtuple('Bookmark', ['name', 'extent'])
webmap_tuple = collections.namedtuple('Webmap', ['mapDocument', 'DPI', 'outputSizeHeight', 'outputSizeWidth'])
excludedvalues_re = re.compile("(-?[0-9]+([.][0-9]+)?)( *- *-?[0-9.]+([.][0-9]+)?)?")

class SupportsPropertyMixin(object):
    def supports(self, attribute):
        """supports(layer_property)

           Not all layers support the same set of properties.  The supports property can be used to test which properties a layer does support.

             layer_property(String):
           The name of a particular layer property that will be tested.

            * BRIGHTNESS:   A raster layer's brightness value

            * CONTRAST:   A raster layer's contrast value

            * DATASETNAME: A layers dataset name the way it appears in the workspace

            * DATASOURCE:   A layer's file path or connection file

            * DEFINITIONQUERY:   A layer's definition query string

            * DESCRIPTION:   A layer's description string

            * LABELCLASSES: A layer's list of label classes

            * LONGNAME:   A layer's path including the group layer(s) it may be nested within

            * NAME:   A layer's name

            * SERVICEPROPERTIES: Connection information for SDE and web service layers

            * SHOWLABELS:   A Boolean indicating if a layer's lables are toggled on or off

            * SYMBOLOGY:   A layer's symbology class

            * SYMBOLOGYTYPE:   A layer's symbology class type

            * TIME:   A layer's time properties

            * TRANSPARENCY:   A layer's transparency value

            * VISIBLE:   A Boolean indicating if a layer is toggled on or off in the TOC

            * WORKSPACEPATH: A layer's workspace or connection file path"""
        if attribute.lower() in [x.lower() for x in dir(self) if not x.startswith('_')]:
            try:
                getattr(self, [x for x in dir(self) if x.lower() == attribute.lower()].pop())
                return True
            except Exception, e:
                return False
        else:
            return False

class LayerSupportsPropertyMixin(SupportsPropertyMixin):
    def supports(self, layer_property):
        """Layer.supports(layer_property)

           Not all layers support the same set of properties.  The supports
           property can be used to test which properties a layer does support.

             layer_property(String):
           The name of a particular layer property that will be tested.

            * BRIGHTNESS:   A raster layer's brightness value

            * CONTRAST:   A raster layer's contrast value

            * DATASETNAME: A layers dataset name the way it appears in the
            workspace

            * DATASOURCE:   A layer's file path or connection file

            * DEFINITIONQUERY:   A layer's definition query string

            * DESCRIPTION:   A layer's description string

            * LABELCLASSES: A layer's list of label classes

            * LONGNAME:   A layer's path including the group layer(s) it may be
            nested within

            * NAME:   A layer's name

            * SERVICEPROPERTIES: Connection information for SDE and web service
            layers

            * SHOWLABELS:   A Boolean indicating if a layer's lables are toggled
            on or off

            * SYMBOLOGY:   A layer's symbology class

            * SYMBOLOGYTYPE:   A layer's symbology class type

            * TIME:   A layer's time properties

            * TRANSPARENCY:   A layer's transparency value

            * VISIBLE:   A Boolean indicating if a layer is toggled on or off in
            the TOC

            * WORKSPACEPATH: A layer's workspace or connection file path"""
        return super(LayerSupportsPropertyMixin, self).supports(layer_property)

class CursorMixin(object):
    def __iter__(self):
        def _iterwrap():
            for item in self._arc_object:
                yield convertArcObjectToPythonObject(item)
        return _iterwrap()

class RowMixin(object):
    pass

class ArrayMixin(object):
    "Allows arcgisscripting array objects to behave similarly to Python lists."
    def __len__(self):
        return self._arc_object.count
    def __iter__(self):
        for index in xrange(len(self)):
            yield convertArcObjectToPythonObject(self._arc_object.GetObject(index))
    def __getitem__(self, index):
        return convertArcObjectToPythonObject(self._arc_object.GetObject(index))
    def __setitem__(self, index, value):
        self._arc_object.Insert(index, (value._arc_object if hasattr(value, '_arc_object') else value))
    def __repr__(self):
        return "<Array %r>" % list(convertArcObjectToPythonObject(x) for x in self)
    def __init__(self, items=[]):
        """Array({items})

             items{Object}:
           Items can include a list, a Point object, or another Array object."""
        _BaseArcObject.__init__(self)
        if isinstance(items, (types.TupleType, types.ListType, types.GeneratorType)):
            for item in items:
                self.append(item)
        elif type:
            self.append(items)
    def append(self, value):
        """Array.append(value)

           Appends an object to the array in the last position.

             value(Object):
           Either a point or array object can be appended to the array."""
        if isinstance(value, (types.TupleType, types.ListType, types.GeneratorType)):
            self.add(self.__class__(items=value))
        else:
            self.add(value)
    def extend(self, values):
        """Array.extend(items)

           Extends the array by appending elements.

             items(Object):
           Extends the array by adding strings, integers, or lists."""
        map(self.append, values)

class GeometrySpecializationMixin(object):
    "Registry for specializing Geometry instances to Geometry subclasses such as Line, Point, etc."
    __type_mapping__ = {}
    class _passthrough(object): pass
    @classmethod
    def __from_scripting_arc_object__(cls, obj): #arcobject):
        from arcpy.arcobjects.arcobjects import Geometry
        #obj = Geometry.fromScriptingArcObject(arcobject)
        instance = cls._passthrough()
        instance._arc_object = obj
        if obj.type.lower() in cls.__type_mapping__:
            instance.__class__ = cls.__type_mapping__[obj.type.lower()]
        return instance
    def __init__(self, *args, **kwargs):
        from arcpy.geoprocessing._base import gp_fixargs
        if not hasattr(self, '__type_string__'):
            if len(args) >= 1:
                self.__type_string__ = args[0]
                args = args[1:]
                self._arc_object = gp.CreateObject('geometry', self.__type_string__,
                                                   *gp_fixargs(args, True))
            else:
                self._arc_object = gp.CreateObject('geometry')
        else:
            self._arc_object = gp.CreateObject('geometry', self.__type_string__,
                                               *gp_fixargs(args, True))
        for attr, value in kwargs.iteritems():
            setattr(self._arc_object, attr, value)
        self._go()
    def __add__(self, other):
        return convertArcObjectToPythonObject(self._arc_object.intersect(other._arc_object))
    def __or__(self, other):
        return convertArcObjectToPythonObject(self._arc_object.union(other._arc_object))
    def __sub__(self, other):
        return convertArcObjectToPythonObject(self._arc_object.difference(other._arc_object))
    def __xor__(self, other):
        return convertArcObjectToPythonObject(self._arc_object.symmetricdifference(other._arc_object))
    def __reduce__(self):
        import arcpy
        return (arcpy.FromWKB, (self._arc_object.wkb, self.spatialReference))

class ParameterMixin(object):
    def __init__(self, name=None, displayName=None, direction=None, datatype=None,
                       parameterType=None, enabled=None, category=None, symbology=None,
                       multiValue=None):
        """Parameter({name}, {displayName}, {direction}, {datatype},
           {parameterType}, {enabled}, {category}, {symbology}, {multiValue})

             name{String}:
           The parameter name.

             displayName{String}:
           The parameter label as shown on the tool's dialog box.

             direction{String}:
           Input/Output direction of the parameter.

             datatype{String}:
           The data type of the parameter.

           For a list of parameter data types, see Geoprocessing data types .

             parameterType{String}:
           Can be Required , Optional, or Derived. Derived means that the user
           of your tool does not enter a value for the parameter. Derived types
           are always output parameters.

             enabled{Boolean}:
           False if the parameter is unavailable.

             category{String}:
           The category  of the parameter.

             symbology{String}:
           The path to a layer file (.lyr) used for drawing the output.

             multiValue{Boolean}:
           True if the parameter is a multivalue parameter ."""
        super(ParameterMixin, self).__init__()
        for attrib, attribvalue in (('name', name),
                                    ('displayName', displayName),
                                    ('direction', direction),
                                    ('datatype', datatype),
                                    ('parameterType', parameterType),
                                    ('enabled', enabled),
                                    ('category', category),
                                    ('symbology', symbology),
                                    ('multiValue', multiValue)):
            if attribvalue is not None:
                setattr(self, attrib, attribvalue)

class LayoutElementSpecializationMixin(object):
    "Registry for specializing LayoutElement instances to Layout subclasses such as PictureElement, Mapsurroundelement, etc."
    __type_mapping__ = {}
    class _passthrough(object): pass
    @classmethod
    def __from_scripting_arc_object__(cls, obj):
        from arcpy._mapping import LayoutElement
        from arcpy._mapping import GraphicElement
        instance = cls._passthrough()
        instance._arc_object = obj
        if obj.type.lower() in cls.__type_mapping__:
            instance.__class__ = cls.__type_mapping__[obj.type.lower()]
        else:
            instance.__class__ = GraphicElement
        return instance
    def __init__(self, *args, **kwargs):
        raise TypeError(gp.getIDMessage(89001, "Cannot instantiate a new Layout Element"))

class LayerSymbologySpecializationMixin(object):
    "Registry for specializing LayerSymbology instances to Symbology subclasses such as UniqueValueRenderer, etc."
    __type_mapping__ = {}
    class _passthrough(object): pass
    @classmethod
    def __from_scripting_arc_object__(cls, obj):
        from arcpy._mapping import GraphicElement
        instance = cls._passthrough()
        instance._arc_object = obj
        if obj.symbologyType.lower() in cls.__type_mapping__:
            new_type = cls.__type_mapping__[obj.symbologyType.lower()]
            if new_type is None:
                return new_type
            instance.__class__ = new_type
        else:
            instance.__class__ = cls
        return instance
    def __init__(self, *args, **kwargs):
        raise TypeError(gp.getIDMessage(89001, "Cannot instantiate a new Symbology"))

class RasterClassifiedExclusionMixin(object):
    "Data sanitizer to make RasterClassifiedSymbology.excludedValues look like the value in the ArcGIS UI"
    @property
    def excludedValues(self):
        individual_values, ranges = self._arc_object._excludedValues
        values_list = ["{0:n}".format(v) for v in individual_values]
        ranges_list = ["{0[0]:n} - {0[1]:n}".format(v) for v in ranges]
        return ";".join(values_list + ranges_list)
    @excludedValues.setter
    def excludedValues(self, value):
        if not value:
            self._arc_object._excludedValues = [(), ()]
            return
        if not isinstance(value, basestring):
            raise ValueError(value)
        matches = [excludedvalues_re.match(x.strip()) for x in value.split(';')]
        if None in matches:
            raise ValueError(value)
        value_list, range_list = [], []
        for start_value, stop_value in ((l.group(1), l.group(3)) for l in matches):
            first_value = float(start_value.strip())
            if stop_value:
                second_value = float(stop_value[stop_value.find('-')+1:].strip())
                range_list.append((first_value, second_value))
            else:
                value_list.append(first_value)
        new_value = [sorted(value_list), sorted(range_list)]
        self._arc_object._excludedValues = new_value

class LayerIterationMixin(object):
    "Allows an object with a .layers property to be iterated over in a for loop"
    def __iter__(self):
        if not hasattr(self, 'layers') and hasattr(self, '_arc_object'):
            self = self._arc_object
        try:
            self.layers
        except RuntimeError, AttributeError:
            return
        layer_queue = [convertArcObjectToPythonObject(l) for l in self.layers]
        map(lambda layer: setattr(layer, '_fullName', layer.name), layer_queue)
        while layer_queue:
            lyr = layer_queue.pop(0)
            if not hasattr(lyr, '_fullName'):
                lyr._fullName = lyr.name
            yield lyr
            if lyr._arc_object.isGroupLayer:
                layer_list = [convertArcObjectToPythonObject(l) for l in lyr._arc_object.layers]
                map(lambda layer: setattr(layer, '_fullName', "%s\\%s"%(lyr._fullName,layer.name)), layer_list)
                layer_queue = layer_list + layer_queue

class LayerMixin(object):
    "Represents specialization for map layer objects"
    def __init__(self, lyrfile=None):
        """Layer(lyr_file_path)

           References a layer ( .lyr ) file stored on disk.

             lyr_file_path(String):
           A string that includes the full path and file name of an existing
           layer ( .lyr ) file."""
        if lyrfile:
            if not isinstance(lyrfile, basestring):
                raise TypeError(repr(type(lyrfile)))
            super(LayerMixin, self).__init__(lyrfile)
            self._lyr = lyrfile
        else:
            super(LayerMixin, self).__init__()
    def __repr__(self):
        return "<map %slayer %r>" % ('group ' if self._arc_object.isGroupLayer else '', self.name)
    def __str__(self):
        return self.longName
    def save(self): #, version=None):
        """Layer.save()

           Saves a layer ( .lyr ) file."""
        version = None
        if not hasattr(self, '_lyr'):
            assert hasattr(self, '_lyr'), gp.getIDMessage(89003, "No filename set.")
        layer_file = self._lyr
        #from arcpy.management import SaveToLayerFile # Adds to TOC
        if version:
            self._arc_object.save(layer_file, version) # SaveToLayerFile(self._arc_object, layer_file)
        else:
            self._arc_object.save(layer_file) # SaveToLayerFile(self._arc_object, layer_file)
        self._lyr = layer_file
    def saveACopy(self, layer_file, version=None):
        """Layer.saveACopy(file_name, {version})

           Saves a layer ( .lyr ) file to a different file name and, optionally,
           a previous version.

             file_name(String):
           A string that includes the location and name of the output layer (
           .lyr ) file.

             version{String}:
           A string that sets the output version number. The default value will
           use the current version.

            * 10.3: Version 10.3

            * 10.1:   Version 10.1/10.2

            * 10.0: Version 10.0

            * 9.3:   Version 9.3

            * 9.2:   Version 9.2

            * 9.0:   Version 9.0/9.1

            * 8.3:   Version 8.3"""
        if version:
            self._arc_object.save(layer_file, version)
        else:
            self._arc_object.save(layer_file)
    @property
    def longName(self):
        return getattr(self, '_fullName', self.name)

LayerMixin.__esri_toolinfo__ = ["Layer File:::"]

class LayerDocumentMixin(object):
    def __init__(self, lyr, *args):
        self._lyr = lyr
    def listLayers(self, wildcard=None, dataframe=None):
        layers = [self._lyr] #+ (list(self._lyr) if self._lyr._arc_object.isGroupLayer else [])
        if self._lyr._arc_object.isGroupLayer:
            for layer in self._lyr:
                layers.append(layer)
            for layer in layers[1:]:
                layer._fullName = "\\".join([self._lyr.longName, layer.longName])
        if wildcard:
            return [layer for layer in layers if wildcardmatch(wildcard, layer.name)]
        return layers
    def listBrokenDataSources(self):
        broken = []
        for l in self.listLayers():
            try:
                l.dataSource
                # Call twice, it seems the first time after rehydration is always wrong
                l._arc_object.valid
                if not l._arc_object.valid:
                    broken.append(l)
            except:
                pass
        return broken

class TableViewMixin(object):
    "Represents specialization for tableview objects"
    def __init__(self, table_view_data_source):
        """TableView(table_view_data_source)

           Enables you to reference a table in a workspace as a TableView object
           so that it can be added to a map document.

             table_view_data_source(String):
           A string that includes the full workspace path, including the name of
           the table."""
        if table_view_data_source:
            if not isinstance(table_view_data_source, basestring):
                raise TypeError(repr(type(table_view_data_source)))
            super(TableViewMixin, self).__init__(table_view_data_source)
            self._table = table_view_data_source
        else:
            super(TableViewMixin, self).__init__()

class DataFrameMixin(object):
    @apply
    def elementPositionX():
        def get_(self):
            pass
        def set_(self, val):
            pass
        return property(get_, set_)
    @apply
    def elementPositionY():
        def get_(self):
            pass
        def set_(self, val):
            pass
        return property(get_, set_)
    @apply
    def elementHeight():
        def get_(self):
            pass
        def set_(self, val):
            pass
        return property(get_, set_)
    @apply
    def elementWidth():
        def get_(self):
            pass
        def set_(self, val):
            pass
        return property(get_, set_)

class ImageFileExportMixin(object):
    "Specialization to expose export to image file methods"
    def exportToAI(self, out_ai, df_export_width=640, df_export_height=480, resolution=300, image_quality=1,
                   colorspace=1, picture_symbol=1, convert_markers=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_ai,
                          df_export_width, df_export_height, resolution, image_quality, colorspace, picture_symbol,
                          convert_markers))
        return self._arc_object.exportToAI(*args)
    def exportToBMP(self, out_bmp, df_export_width=640, df_export_height=480, resolution=96, world_file=False, color_mode=1,
                    rle_compression=1, background_mask_color=''):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_bmp, df_export_width, df_export_height, resolution,
                          world_file, color_mode, rle_compression, background_mask_color))
        return self._arc_object.exportToBMP(*args)
    def exportToEMF(self, out_emf, df_export_width=640, df_export_height=480, resolution=300,
                    image_quality=1, description='', picture_symbol=1, convert_markers=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_emf, df_export_width, df_export_height, resolution,
                          image_quality, description, picture_symbol, convert_markers))
        return self._arc_object.exportToEMF(*args)
    def exportToEPS(self, out_eps, df_export_width=640, df_export_height=480, resolution=300,
                    image_quality=1, colorspace=1, ps_lang_level=3, image_compression=4,
                    picture_symbol=1, convert_markers=False, embed_fonts=False, page_layout_image=1,
                    page_layout_emulsion=1, jpeg_compression_quality=None):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_eps, df_export_width, df_export_height, resolution,
                          image_quality, colorspace, ps_lang_level, image_compression,
                          picture_symbol, convert_markers, embed_fonts,
                          page_layout_image, page_layout_emulsion, jpeg_compression_quality))
        return self._arc_object.exportToEPS(*args)
    def exportToGIF(self, out_gif, df_export_width=640, df_export_height=480, resolution=96,
                    world_file=False, color_mode=2, gif_compression=1, background_color='255, 255, 255',
                    transparent_color=None, interlaced=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_gif, df_export_width, df_export_height, resolution, world_file,
                          color_mode, gif_compression, background_color, transparent_color, interlaced))
        return self._arc_object.exportToGIF(*args)
    def exportToJPEG(self, out_jpeg, df_export_width=640, df_export_height=480, resolution=96,
                     world_file=False, color_mode=1, jpeg_quality=100, background_color='255, 255, 255',
                     progressive=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_jpeg, df_export_width, df_export_height, resolution,
                          world_file, color_mode, jpeg_quality, background_color,
                          progressive))
        return self._arc_object.exportToJPEG(*args)
    def exportToPDF(self, out_pdf, df_export_width=640, df_export_height=480, resolution=300, image_quality=1,
                    colorspace=1, compress_vectors=True, image_compression=4, picture_symbol=1,
                    convert_markers=False, embed_fonts=False, layers_attributes=2, georef_info=True,
                    jpeg_compression_quality=None):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_pdf, df_export_width, df_export_height, resolution, image_quality,
                          colorspace, compress_vectors, image_compression, picture_symbol,
                          convert_markers, embed_fonts, layers_attributes, georef_info,
                          jpeg_compression_quality))
        return self._arc_object.exportToPDF(*args)
    def exportToPNG(self, out_png, df_export_width=640, df_export_height=480, resolution=96,
                    world_file=False, color_mode=1, background_color='255, 255, 255',
                    transparent_color=None, interlaced=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_png, df_export_width, df_export_height, resolution,
                          world_file, color_mode, background_color,
                          transparent_color, interlaced))
        return self._arc_object.exportToPNG(*args)
    def exportToSVG(self, out_svg, df_export_width=640, df_export_height=480, resolution=300, image_quality=1,
                    compress_document=False, picture_symbol=1, convert_markers=False, embed_fonts=False):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_svg, df_export_width, df_export_height, resolution, image_quality,
                          compress_document, picture_symbol, convert_markers, embed_fonts))
        return self._arc_object.exportToSVG(*args)
    def exportToTIFF(self, out_tiff, df_export_width=640, df_export_height=480, resolution=96, world_file=False,
                     color_mode=1, tiff_compression=1, geoTIFFTags=None):
        from arcpy.geoprocessing._base import gp_fixargs
        args = gp_fixargs((out_tiff, df_export_width, df_export_height, resolution, world_file,
                          color_mode, tiff_compression, geoTIFFTags))
        return self._arc_object.exportToTIFF(*args)

class MapDocumentMethods(object):
    def __init__(self, mxd):
        """MapDocument(mxd_path)

           Provides a reference to a map document ( .mxd ) stored on disk or to
           the map document that is currently loaded within the ArcMap
           application (using the CURRENT keyword)

             mxd_path(String):
           A string that includes the full path and file name of an existing map
           document ( .mxd ) or a string that contains the keyword CURRENT."""
        assert (os.path.isfile(mxd) or (mxd.lower() == "current")), gp.getIDMessage(89004, "Invalid MXD filename")
        super(MapDocumentMethods, self).__init__(mxd)
    @property
    def dataDrivenPages(self):
        return convertArcObjectToPythonObject(self._arc_object.pageLayout.dataDrivenPages)
    @property
    def isDDPEnabled(self):
        return convertArcObjectToPythonObject(self._arc_object.pageLayout.isDDPEnabled)
    @property
    def pageSize(self):
        return pagesize_tuple(self._arc_object.pageLayout.width,
                              self._arc_object.pageLayout.height)

MapDocumentMethods.__esri_toolinfo__ = ["ArcMap Document:::"]

class MapDocumentMixin(ImageFileExportMixin):
    "Represents a map document"
    def __init__(self, mxd, *args):
        """MapDocument(mxd_path)

           Provides a reference to a map document ( .mxd ) stored on disk or to
           the map document that is currently loaded within the ArcMap
           application (using the CURRENT keyword)

             mxd_path(String):
           A string that includes the full path and file name of an existing map
           document ( .mxd ) or a string that contains the keyword CURRENT."""
        self._mxd = mxd
    def __iter__(self):
        return iter(self.pageLayout.dataFrames)
    def __repr__(self):
        return "<Map document %r %r>" % (self._mxd, tuple(self.layerNames))
    def __getitem__(self, search_layer):
        from arcpy._mapping import Layer, DataFrame
        if isinstance(search_layer, basestring): # Lookup by name/source
            if search_layer.upper() == "PAGE_LAYOUT":
                return self.pageLayout
            caseless_match_layer = None
            for layer in self.dataFrames + self.layers:
                if layer.name == search_layer or search_layer == "#":
                    return layer
                elif layer.name.lower() == search_layer.lower():
                    caseless_match_layer = layer
                elif hasattr(layer, '_fullName') and layer._fullName == search_layer:
                    return layer
                elif hasattr(layer, '_fullName') and layer._fullName.lower() == search_layer.lower():
                    caseless_match_layer = layer
                elif (isinstance(layer, Layer) and not layer._arc_object.isGroupLayer):
                    try:
                        ds = layer.dataSource
                        if ds.lower() == os.path.normpath(search_layer).lower():
                            caseless_match_layer = layer
                    except:
                        pass
            if caseless_match_layer is not None:
                return caseless_match_layer
        elif isinstance(search_layer, DataFrame):
            return list(search_layer)
        elif isinstance(search_layer, Layer):
            l = [search_layer]
            if search_layer.isGroupLayer:
                for extra_layer in search_layer._arc_object.layers:
                    l += self[convertArcObjectToPythonObject(extra_layer)]
            return l
        raise KeyError(gp.getIDMessage(89002, "No layer or data frame found: %r") % search_layer)
    @property
    def _arc_object(self):
        return self._mxd._arc_object.pageLayout
    @property
    def pageLayout(self):
        return convertArcObjectToPythonObject(self._mxd._arc_object.pageLayout)
    @property
    def layers(self):
        layers = []
        for frame in reversed(self.dataFrames):
            for layer in frame:
                layers.append(layer)
        return layers
    @property
    def layerNames(self):
        return [x._fullName for x in self.layers]
    @property
    def dataFrames(self):
        from arcpy._mapping import DataFrame
        if isinstance(self._mxd, DataFrame):
            return [self._mxd]
        return map(convertArcObjectToPythonObject, self.pageLayout.dataFrames)
    @property
    def dataFrameNames(self):
        return [x.name for x in self.dataFrames]
    def listLayoutElements(self, element_type='', wildcard=None):
        element_queue = [convertArcObjectToPythonObject(l) for l in self.elements]
        els = []
        while element_queue:
            el = element_queue.pop(0)
            if getattr(el._arc_object, 'isGroupElement', False):
                for subelement in el._arc_object.elements:
                    element_queue.insert(0, convertArcObjectToPythonObject(subelement))
            els.append(el)
        if element_type:
            els = [el for el in els if el.type.upper() == element_type.upper()]
        if not wildcard:
            return els
        else:
            return [el for el in els if wildcardmatch(wildcard, el.name)]
    def listTextElements(self, wildcard=None):
        if not wildcard:
            return self.textElements
        else:
            return [el for el in self.textElements if wildcardmatch(wildcard, el.name)]
    @property
    def elements(self):
        return self.pageLayout.elements
    @property
    def textElements(self):
        from arcpy._mapping import TextElement
        return [el for el in self.pageLayout.elements if isinstance(el, TextElement)]
    def listDataFrames(self, wildcard=None):
        if not wildcard:
            return list(reversed(list(self.dataFrames)))
        else:
            return list(reversed([fr for fr in self.dataFrames if wildcardmatch(wildcard, fr.name)]))
    def updateDataSources(self, existing_path, new_path, output_mxd=None):
        from arcpy._mapping import Layer, TableView
        import logging
        if isinstance(existing_path, (Layer, TableView)):
            existing_path = existing_path._arc_object.datasource
        if isinstance(new_path, (Layer, TableView)):
            new_path = new_path._arc_object.datasource
        return self._mxd._arc_object.updatedatasources(existing_path, new_path)
        #for df in self.listDataFrames():
        #    df._arc_object.replaceworkspacename(existing_path, new_path)
        gp.RefreshActiveView()
        gp.RefreshTOC()
    def updateSymbology(self, layer_name, layer_file, dataframe=None):
        from arcpy.management import ApplySymbologyFromLayer_management
        from arcpy._mapping import Layer, PageLayout
        import logging
        map = self
        if isinstance(layer_name, Layer):
            lyrs = [layer_name]
        elif dataframe and isinstance(layer_name, basestring):
            frame = self[dataframe]
            if isinstance(frame, PageLayout):
                lyrs = [lyr for lyr in self.layers if wildcardmatch(layer_name, lyr.name)]
            else:
                lyrs = [fr for fr in frame if wildcardmatch(layer_name, fr.name)]
        else:
            lyrs = [fr for fr in map.layers if wildcardmatch(layer_name, fr.name)]
        logging.debug("Matched layers are %r v. %r" % (lyrs, layer_file))
        for lyr in lyrs:
            ApplySymbologyFromLayer_management(lyr, layer_file)
        gp.RefreshActiveView()
    def replaceLayer(self, layer_name, layer_file, dataframe=None):
        from arcpy._mapping import Layer
        map = self
        # Open layer file
        if isinstance(layer_file, basestring):
            layer_file = Layer(layer_file)
        if dataframe and isinstance(layer_name, basestring):
            frame = self[dataframe]
            lyrs = [fr for fr in frame if wildcardmatch(layer_name, fr.name)]
        elif isinstance(layer_name, Layer):
            lyrs = [layer_name]
        else:
            lyrs = [fr for fr in map.layers if wildcardmatch(layer_name, fr.name)]
        for lyr in lyrs:
            if isinstance(lyr, Layer):
                if isinstance(layer_file, Layer):
                    layer_file = layer_file._arc_object
                lyr._arc_object.replace(layer_file)
            else:
                lyr.replace(layer_file)
        gp.RefreshActiveView()
    def updateTextElement(self, existing_text, new_text, output_mxd=None):
        from arcpy._mapping import TextElement
        for element in self.pageLayout.elements:
            if isinstance(element, TextElement):
                if element.text.strip() == existing_text:
                    element.text = new_text
        gp.RefreshActiveView()
    def _zoom_if_necessary(self, extent):
        if extent is not None:
            for frame in self.pageLayout.dataFrames:
                try:
                    frame.zoomToExtent(extent)
                except:
                    pass
    def layerVisibility(self, layer_name, visibility=None, extent=None):
        if visibility is not None:
            self[layer_name].visible = visibility
            gp.RefreshTOC()
            gp.RefreshActiveView()
        return self[layer_name].visible
    def containsLayer(self, layer_name):
        from arcpy._mapping import Layer
        try:
            lyr = self[layer_name]
            assert isinstance(lyr, Layer)
            return True
        except KeyError, ke:
            for layer in self.layers:
                if not layer._arc_object.isGroupLayer and layer.dataSource == layer_name:
                    return True
            return False
    def listLayers(self, wildcard=None, dataframe=None):
        """listLayers({wildcard})

           Returns a Python list of Layer objects in a Map .

             wildcard{String}:
           A wildcard is based on the layer name and is not case sensitive. A
           combination of asterisks (*) and characters can be used to help
           limit the resulting list."""
        layer_queue = []
        layers = []
        if dataframe:
            from arcpy._mapping import DataFrame
            if not isinstance(dataframe, DataFrame):
                raise TypeError(str(type(dataframe)))
            layers = list(self[dataframe])
        else:
            layers = self.layers
        if wildcard:
            return [layer for layer in layers if wildcardmatch(wildcard, layer.name)]
        return layers
    def saveToLayerFile(self, layer, out_file, version=10.0):
        if isinstance(layer, basestring):
            layer = self[layer]
        layer.saveToLayerFile(out_file, version)
    def listBrokenDataSources(self):
        """listBrokenDataSources()

           Returns a Python list of Layer and/or TableView objects that have
           broken connections to their original source data within a map."""
        broken_sources = [l for l in self.layers if not l._arc_object.valid]
        broken_sources += [l for l in self.listTableViews() if not l._arc_object.valid]
        return broken_sources
    def listTableViews(self, wildcard=None, dataframe=None):
        """listTableViews({wildcard})

           Returns a Python list of TableView objects that exist within a map.

             wildcard{String}:
           A combination of asterisks (*) and characters can be used to help
           limit the results."""
        if dataframe:
            from arcpy._mapping import DataFrame
            if not isinstance(dataframe, DataFrame):
                raise TypeError(str(type(dataframe)))
            dfs = [dataframe]
        else:
            dfs = self.listDataFrames()
        if dfs:
            tvl = [map(convertArcObjectToPythonObject,
                                            getattr(frame._arc_object,
                                                    'standaloneTables', []))
                                              for frame in dfs]
            tvs = reduce(operator.add, tvl, [])
        else:
            tvs = []
        if wildcard:
            return [tv for tv in tvs if wildcardmatch(wildcard, tv.name)]
        return tvs
    def listPageNames(self):
        "Gets the map's page names"
        return self.pageLayout.listPageNames()
    def printMap(self, *pages):
        return self.pageLayout.printMap(*pages)
    def convertToMSD(self, out_msd, dataframe, msd_anti_aliasing, msd_text_anti_aliasing):
        from arcpy._mapping import DataFrame
        map = self._mxd._arc_object
        if dataframe and dataframe != 'USE_ACTIVE_VIEW':
            df = dataframe
            assert isinstance(df, (DataFrame, basestring))
            if isinstance(df, DataFrame):
                df = df._arc_object
            map.activeview = df
        return map.convertToMSD(out_msd, dataframe, msd_anti_aliasing, msd_text_anti_aliasing)
    def analyzeForMSD(self):
        map = self._mxd._arc_object
        return convertArcObjectToPythonObject(map.analyzeForMSD())

class ArcSDESQLExecuteMixin(object):
    def __init__(self, server=None, instance=None, database=None, user=None, password=None):
        """ArcSDESQLExecute({server}, {instance}, {database}, {user},
           {password})

             server{String}:
           Name of the server on which the database is installed or a valid
           connection file.

             instance{String}:
           The port number.

             database{String}:
           Name of the database.

             user{String}:
           The user name.

             password{String}:
           The password for the user name."""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self, *gp_fixargs((server, instance, database, user, password), True))

class NetCDFFilePropertiesMixin(object):
    def __init__(self, netcdffile=None):
        """NetCDFFileProperties(netcdffile)

             netcdffile(String):
           The input netCDF file."""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self, *gp_fixargs((netcdffile,), True))

class SpatialReferenceMixin(object):
    def __init__(self, item=None,text=None):
        """SpatialReference({item})

             item{String}:
           The spatial reference can be created in three ways: Using the name of
           the coordinate system  sr = arcpy.SpatialReference("Hawaii Albers
           Equal Area Conic") Using a projection file (.prj) sr =
           arcpy.SpatialReference("c:/coordsystems/NAD 1983.prj") Using a
           coordinate system's factory code (or authority code)   # 32145 is the
           code for:
           #  NAD 1983 StatePlane Vermont FIPS 4400 (Meters)
           sr = arcpy.SpatialReference(32145)

           For more information on coordinate system names and factory codes,
           see geographic_coordinate_systems.pdf and
           projected_coordinate_systems.pdf files in the ArcGIS Documentation
           folder.

           For more information, see Using the spatial reference class ."""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self)
        if item:
            self._arc_object.createFromFile(item)
        elif text:
            self._arc_object.loadFromString(text)
    def __reduce__(self):
        import arcpy
        return (arcpy.SpatialReference, (None,self.exportToString(),))

class FieldMappingsMixin(object):
    def __init__(self):
        """FieldMappings()"""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self)
    def __iter__(self):
        return iter(self.fieldMappings)

class FieldMapMixin(object):
    def __init__(self):
        """FieldMap()"""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self)

class FieldMixin(object):
    def __init__(self):
        """Field()"""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self)

class ExtentMixin(object):
    def __init__(self, XMin=None, YMin=None, XMax=None, YMax=None, ZMin=None, ZMax=None, MMin=None, MMax=None):
        """Extent({XMin}, {YMin}, {XMax}, {YMax}, {ZMin}, {ZMax}, {MMin},
           {MMax})

             XMin{Double}:
           The extent XMin value.

             YMin{Double}:
           The extent YMin value.

             XMax{Double}:
           The extent XMax value.

             YMax{Double}:
           The extent YMax value.

             ZMin{Double}:
           The extent ZMin value. None if no Z value.

             ZMax{Double}:
           The extent ZMax value. None if no Z value.

             MMin{Double}:
           The extent MMin value. None if no M value.

             MMax{Double}:
           The extent MMax value. None if no M value."""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self, *gp_fixargs((XMin, YMin, XMax, YMax, ZMin, ZMax, MMin, MMax), True))

class ValueTableMixin(object):
    def __init__(self, columns=None):
        """ValueTable({columns})

             columns{Integer}:
           The number of columns."""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self, *gp_fixargs((columns,), True))

class FieldInfoMixin(object):
    def __init__(self):
        """FieldInfo()"""
        from arcpy.geoprocessing._base import gp_fixargs
        _BaseArcObject.__init__(self)

class FeatureSetMixin(object):
    def __init__(self, table=None):
        """FeatureSet({table})

             table{String}:
           Feature data to be loaded into the FeatureSet object."""
        _BaseArcObject.__init__(self)
        if table:
            self._arc_object.load(table)

class RecordSetMixin(object):
    def __init__(self, table=None):
        """RecordSet({table})

             table{String}:
           Table to be loaded into the RecordSet object."""
        _BaseArcObject.__init__(self)
        if table:
            self._arc_object.load(table)

class PointMixin(object):
    "Point creation/manipulation helpers"
    def __repr__(self):
        return "<Point (%s)>" % ', '.join(str(x) if x is not None
                                                 else '#'
                                          for x in (self.X, self.Y,
                                                    self.Z, self.M))
    def __init__(self, X=None, Y=None, Z=None, M=None, ID=None):
        """Point({X}, {Y}, {Z}, {M}, {ID})

             X{Double}:
           The X coordinate of the point.

             Y{Double}:
           The Y coordinate of the point.

             Z{Double}:
           The Z coordinate of the point.

             M{Double}:
           The M value of the point.

             ID{Integer}:
           The shape ID of the point."""
        _BaseArcObject.__init__(self)
        for attr, value in zip(('X', 'Y', 'Z', 'M', 'ID'), (X, Y, Z, M, ID)):
            if value is not None:
                setattr(self, attr, value)

class ResultMixin(object):
    def __init__(self, toolname='', resultID=''):
        """Result(toolname, resultID)

             toolname(String):
           The name of the executed tool.

             resultID(Integer):
           The job ID."""
        _BaseArcObject.__init__(self, "%s %s" % (str(toolname), str(resultID)))
    def __repr__(self):
        return "<Result %r>" % str(self._arc_object)
    def __str__(self):
        return str(self._arc_object)
    def __getitem__(self, item):
        return self.getOutput(item)
    def __len__(self):
        return self.outputCount
    def __iter__(self):
        for idx in xrange(self.outputCount):
            yield self.getOutput(idx)
