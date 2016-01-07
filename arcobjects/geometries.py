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
from arcpy import gp
from arcpy.arcobjects.arcobjects import Geometry

import operator

__all__ = ['Annotation', 'Dimension', 'Multipatch', 'Multipoint', 'PointGeometry', 'Polygon', 'Polyline', 'AsShape']

class Annotation(Geometry):
    __type_string__ = "annotation"

class Dimension(Geometry):
    __type_string__ = "dimension"

class Multipatch(Geometry):
    __type_string__ = "multipatch"

class Multipoint(Geometry):
    """Multipoint objects are ordered collection of points."""
    __type_string__ = "multipoint"
    def __iter__(self):
        for x in xrange(self.partCount):
            yield self.getPart(x)
    @property
    def __geo_interface__(self):
        return {'type': 'Multipoint', 'coordinates': [(pt.X, pt.Y) for pt in self]}
    @classmethod
    def _fromGeoJson(cls, data):
        from .arcobjects import Point, Array
        coordkey = ([d for d in data if d.lower() == 'coordinates']
                     or ['coordinates']).pop()
        coordinates = data[coordkey]
        return cls(Array(map(lambda p: Point(*p), coordinates)))

class PointGeometry(Geometry):
    """A PointGeometry is a shape that has neither length nor area at a given
       scale."""
    __type_string__ = "point"
    @property
    def __geo_interface__(self):
        return {'type': 'Point', 'coordinates': (self.getPart(0).X,
                                                 self.getPart(0).Y)}
    @classmethod
    def _fromGeoJson(cls, data):
        from .arcobjects import Point
        coordkey = ([d for d in data if d.lower() == 'coordinates']
                     or ['coordinates']).pop()
        coordinates = data[coordkey]
        return cls(Point(*coordinates))

class Polygon(Geometry):
    """A Polygon object is a closed shape defined by a connected sequence of x,y
       coordinate pairs."""
    __type_string__ = "polygon"
    def __iter__(self):
        for x in xrange(self.partCount):
            yield self.getPart(x)
    @property
    def __geo_interface__(self):
        return {'type': 'Polygon', 'coordinates': [[((pt.X, pt.Y) if pt else None)
                                                        for pt in part]
                                                            for part in self]}
    @classmethod
    def _fromGeoJson(cls, data):
        from .arcobjects import Point, Array
        coordkey = ([d for d in data if d.lower() == 'coordinates']
                     or ['coordinates']).pop()
        coordinates = data[coordkey]
        typekey = ([d for d in data if d.lower() == 'type']
                     or ['type']).pop()
        # Merge coords if it's a multipolygon
        if data[typekey].lower() == "multipolygon":
            coordinates = reduce(operator.add, coordinates)
        return cls(Array([map(lambda p: Point(*p), part) for part in coordinates]))

class Polyline(Geometry):
    """A Polyline object is a shape defined by one or more paths, in which a
       path is a series of connected segments."""
    __type_string__ = "polyline"
    def __iter__(self):
        for x in xrange(self.partCount):
            yield self.getPart(x)
    @property
    def __geo_interface__(self):
        return {'type': 'MultiLineString', 'coordinates': [[((pt.X, pt.Y) if pt else None)
                                                                for pt in part]
                                                                    for part in self]}
    @classmethod
    def _fromGeoJson(cls, data):
        from .arcobjects import Point, Array
        coordkey = ([d for d in data if d.lower() == 'coordinates']
                     or ['coordinates']).pop()
        if data['type'].lower() == 'linestring':
            coordinates = [data[coordkey]]
        else:
            coordinates = data[coordkey]
        return cls(Array([map(lambda p: Point(*p), part) for part in coordinates]))

for cls in (Annotation, Dimension,
            Multipatch, Multipoint,
            PointGeometry, Polygon,
            Polyline):
    Geometry.__type_mapping__[cls.__type_string__] = cls

del cls

def AsShape(geojson_struct, esri_json=False):
    """AsShape(geojson_struct, {esri_json})

       Converts Esri JSON or GeoJSON to ArcPy geometry or feature set objects.
       GeoJSON is a geospatial data interchange format for encoding geographic
       data
       structures.

         geojson_struct(Dictionary):
       The geojson_struct includes type and coordinates .

       The following strings are  included for type : Point , LineString ,
       Polygon , MultiPoint , and MultiLineString .

         esri_json{Boolean}:
       Sets whether the input JSON is evaluated as Esri JSON or GeoJSON.  If
       True, the input is evaluated as Esri JSON."""
    if esri_json:
        if not isinstance(geojson_struct, basestring):
            import json
            geojson_struct = json.dumps(geojson_struct)
        from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(gp.fromEsriJson(geojson_struct))
    else:
        mappings = {
                        'point': PointGeometry,
                        'multipoint': Multipoint,
                        'polygon': Polygon,
                        'multipolygon': Polygon,
                        'multilinestring': Polyline,
                        'linestring': Polyline
                   }
        if isinstance(geojson_struct, basestring):
            import json
            geojson_struct = json.loads(geojson_struct)
        import arcpy
        assert isinstance(geojson_struct, dict),\
                arcpy.GetIDMessage(88023, 'Invalid Geometry Data')
        assert (geojson_struct.get('type', None) or '').lower() in mappings,\
                arcpy.GetIDMessage(88023, 'Invalid Geometry Data')
        return mappings[geojson_struct.get('type').lower()]._fromGeoJson(geojson_struct)
