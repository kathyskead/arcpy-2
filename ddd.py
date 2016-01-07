# -*- coding: utf-8 -*-
#COPYRIGHT 2014 ESRI
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
"""The 3D Analyst toolbox provides a collection of geoprocessing tools that enable
a wide variety of analytical, data management, and data conversion operations on
surface models and three-dimensional vector data. The toolbox is conveniently
organized into toolsets which define the scope of tasks accomplished by the
tools therein."""
__all__ = ['InterpolateShape', 'SurfaceVolume', 'Idw', 'Kriging', 'NaturalNeighbor', 'Spline', 'TopoToRaster', 'TopoToRasterByFile', 'Trend', 'Divide', 'Float', 'Int', 'Minus', 'Plus', 'Times', 'Lookup', 'ReclassByASCIIFile', 'ReclassByTable', 'Reclassify', 'Slice', 'Aspect', 'Contour', 'ContourList', 'Curvature', 'HillShade', 'Slope', 'DecimateTinNodes', 'ExtrudeBetween', 'InterpolatePolyToPatch', 'Layer3DToFeatureClass', 'TinDomain', 'TinEdge', 'TinLine', 'TinNode', 'TinPolygonTag', 'TinRaster', 'TinTriangle', 'RasterDomain', 'RasterTin', 'Import3DFiles', 'MultiPatchFootprint', 'LASToMultipoint', 'TerrainToRaster', 'TerrainToTin', 'FeatureClassZToASCII', 'PointFileInformation', 'ContourWithBarriers', 'RasterToMultipoint', 'TerrainToPoints', 'SurfaceContour', 'PolygonVolume', 'AddZInformation', 'SurfaceAspect', 'SurfaceDifference', 'SurfaceSlope', 'LocateOutliers', 'FeatureTo3DByAttribute', 'Intersect3DLineWithMultiPatch', 'AddSurfaceInformation', 'LandXMLToTin', 'Near3D', 'Inside3D', 'Intersect3D', 'IsClosed3D', 'Union3D', 'Difference3D', 'CutFill', 'SplineWithBarriers', 'ConstructSightLines', 'Skyline', 'SkylineBarrier', 'SkylineGraph', 'LineOfSight', 'Viewshed', 'CopyTin', 'CreateTin', 'DelineateTinDataArea', 'EditTin', 'AddFeatureClassToTerrain', 'AddTerrainPyramidLevel', 'AppendTerrainPoints', 'BuildTerrain', 'ChangeTerrainReferenceScale', 'ChangeTerrainResolutionBounds', 'CreateTerrain', 'DeleteTerrainPoints', 'RemoveFeatureClassFromTerrain', 'RemoveTerrainPyramidLevel', 'ReplaceTerrainPoints', 'ObserverPoints', 'Buffer3D', 'LasDatasetToTin', 'ASCII3DToFeatureClass', 'ChangeLasClassCodes', 'SetLasClassCodesUsingFeatures', 'StackProfile', 'Intersect3DLineWithSurface', 'EncloseMultiPatch', 'SunShadowVolume', 'Intervisibility', 'Visibility', 'FeaturesFromCityEngineRules', 'ExportTo3DWebScene', 'ClassifyLasByHeight', 'LasPointStatsByArea', 'LocateLasPointsByProximity', 'Viewshed2']
__alias__ = u'3d'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# 3D Features toolset
@gptooldoc('AddZInformation_3d', None)
def AddZInformation(in_feature_class=None, out_property=None, noise_filtering=None):
    """AddZInformation(in_feature_class, out_property;out_property..., {noise_filtering})

        Adds information about elevation properties of features in a Z-enabled feature
        class.Each 3D shape is examined and the selected properties are appended to the
        attribute table of the input feature class. The output options vary based on the
        feature's geometry.

     INPUTS:
      in_feature_class (Feature Layer):
          The input features to process.
      out_property (String):
          The Z properties that will be added to the attribute table of the input feature
          class. The following options are available:

          * Z—Spot elevation of single-point feature.

          * POINT_COUNT—Number of points in each multipoint feature.

          * Z_MIN—Lowest Z value found in each multipoint, polyline, polygon, or
          multipatch feature.

          * Z_MAX—Highest Z value found in each multipoint, polyline, polygon, or
          multipatch feature.

          * Z_MEAN—Average Z value found in each multipoint, polyline, polygon, or
          multipatch feature.

          * LENGTH_3D—3-dimensional length of each polyline or polygon feature.

          * SURFACE_AREA—Total area of the surface of a multipatch feature.

          * VERTEX_COUNT—Total number of vertices in each polyline or polygon feature.

          * MIN_SLOPE—Lowest slope value calculated for each polyline, polygon, or
          multipatch feature.

          * MAX_SLOPE—Highest slope value calculated for each polyline, polygon, or
          multipatch feature.

          * AVG_SLOPE—Average slope value calculated for each polyline, polygon, or
          multipatch feature.

          * VOLUME—Volume of space enclosed by each multipatch feature.
      noise_filtering {String}:
          An optional numeric value used to exclude portions of features from the
          resulting calculations. This can be useful when the 3D input contains relatively
          small features with extreme slopes which may bias statistical results. If the 3D
          input's linear units are meters, specifying a value of 0.001 will result in the
          exclusion of lines or polygon edges that are shorter than 0.001 meters. For
          multipatch features, the same value will result in the exclusion of its subparts
          that have an area less than 0.001 square meters. This parameter does not apply
          to point and multipoint features.The Area filter is made available when the
          input is a multipatch, whereas the
          Length filter is provided when the input is a line or polygon."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddZInformation_3d(*gp_fixargs((in_feature_class, out_property, noise_filtering), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Buffer3D_3d', None)
def Buffer3D(in_features=None, out_feature_class=None, buffer_distance_or_field=None, buffer_joint_type=None, buffer_quality=None, simplification_tolerance=None):
    """Buffer3D(in_features, out_feature_class, buffer_distance_or_field, {buffer_joint_type}, {buffer_quality}, {simplification_tolerance})

        Creates a 3-dimensional buffer around points or lines to produce spherical or
        cylindrical multipatch features.

     INPUTS:
      in_features (Feature Layer):
          The line or point features to be buffered.
      buffer_distance_or_field (Linear unit / Field):
          The distance of the buffer around the input features, which can be provided as
          either a linear distance or be derived from a numeric field in the input
          feature's attribute table. If the buffer distance is specified from an input
          field, its unit of measurement will be derived from the feature's spatial
          reference. If the linear distance is specified as a numeric value, the following
          units of measure are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * MILLIMETERS

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS
      buffer_joint_type {String}:
          The shape of the buffer between the vertices of the line segments. This
          parameter is only valid for input line features.

          * STRAIGHT—The shape of connections between vertices will be straight.  This is
          the default.

          * ROUND—The shape of connections between vertices will be round.
      buffer_quality {Long}:
          The number of segments used to represent the resulting multipatch features.  The
          default is 20, but any number between the range of 6 to 60 can be entered. A
          higher Buffer Quality value produces smoother 3D features, but also lengthens
          the processing time.
      simplification_tolerance {Linear unit}:
          Simplifies the input lines by maintaining their shape within the specified
          offset of its original form. Simplification will not take place if no value is
          specified. The following units of measurement are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * MILLIMETERS

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS

     OUTPUTS:
      out_feature_class (Feature Class):
          The output multipatch containing the 3D buffers."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Buffer3D_3d(*gp_fixargs((in_features, out_feature_class, buffer_distance_or_field, buffer_joint_type, buffer_quality, simplification_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Difference3D_3d', None)
def Difference3D(in_features_minuend=None, in_features_subtrahend=None, out_feature_class=None, out_table=None):
    """Difference3D(in_features_minuend, in_features_subtrahend, out_feature_class, {out_table})

        Eliminates portions of multipatch features in a target feature class that
        overlap with enclosed volumes of multipatch features in the subtraction feature
        class.

     INPUTS:
      in_features_minuend (Feature Layer):
          The multipatch features that will have its features removed by the subtrahend
          features.
      in_features_subtrahend (Feature Layer):
          The multipatch features that will be subtracted from the input.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output multipatch feature class that will contain the resulting features.
      out_table {Table}:
          An optional table that stores information about the relationship between the
          input features and the difference output. The following fields are present in
          this table:

          * Output_ID—The ID of the output feature.

          * Minuend_ID—The ID of the input feature.

          * Subtrahend—The ID of the subtract feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Difference3D_3d(*gp_fixargs((in_features_minuend, in_features_subtrahend, out_feature_class, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EncloseMultiPatch_3d', None)
def EncloseMultiPatch(in_features=None, out_feature_class=None, grid_size=None):
    """EncloseMultiPatch(in_features, out_feature_class, {grid_size})

        Creates closed multipatch features in the output feature class using the
        features of the input multipatch.

     INPUTS:
      in_features (Feature Layer):
          The multipatch features that will be used to construct closed multipatches.
      grid_size {Double}:
          The resolution that will be used to construct the closed multipatch features.
          This value is defined using the linear units of the input feature's spatial
          reference.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output closed multipatch features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EncloseMultiPatch_3d(*gp_fixargs((in_features, out_feature_class, grid_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureTo3DByAttribute_3d', None)
def FeatureTo3DByAttribute(in_features=None, out_feature_class=None, height_field=None, to_height_field=None):
    """FeatureTo3DByAttribute(in_features, out_feature_class, height_field, {to_height_field})

        Creates 3D features using height values derived from the attribute of the input
        features.

     INPUTS:
      in_features (Feature Layer):
          The features that will be used to create 3D features.
      height_field (Field):
          The field whose values will define the height of the resulting 3D features.
      to_height_field {Field}:
          An optional second height field used for lines. When using two height fields,
          each line will start at the first height and end at the second (sloped).

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureTo3DByAttribute_3d(*gp_fixargs((in_features, out_feature_class, height_field, to_height_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Inside3D_3d', None)
def Inside3D(in_target_feature_class=None, in_container_feature_class=None, out_table=None, complex_output=None):
    """Inside3D(in_target_feature_class, in_container_feature_class, out_table, {complex_output})

        Determines if 3D features from an input feature class are contained inside a
        closed multipatch, and writes an output table recording the features that are
        partially or fully inside the multipatch.

     INPUTS:
      in_target_feature_class (Feature Layer):
          The input multipatch or 3D point, line, or polygon feature class.
      in_container_feature_class (Feature Layer):
          The closed multipatch features that will be used as the containers for the input
          features.
      complex_output {Boolean}:
          Specifies if the output table will identify the relationship between the Input
          Features and the Input Multipatch Features through the creation of a Contain_ID
          field that identifies the multipatch feature that contains the input feature.

          * Checked—The multipatch feature that contains an input feature will be
          identified.

          * Unchecked—The multipatch feature that contains an input feature will not be
          identified. This is the default.
          Specifies if the output table will identify the relationship between the Input
          Features and the Input Multipatch Features through the creation of a Contain_ID
          field that identifies the multipatch feature that contains the input feature.

          * COMPLEX—The multipatch feature that contains an input feature will be
          identified.

          * SIMPLE—The multipatch feature that contains an input feature will not be
          identified. This is the default.

     OUTPUTS:
      out_table (Table):
          The output table providing a list of 3D Input Features that are inside or
          partially inside  the Input Multipatch Features which are closed.  The output
          table contains an OBJECTID (object ID), Target_ID, and Status field. The Status
          field will state if the input feature (Target_ID) is inside or partially inside
          a multipatch."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Inside3D_3d(*gp_fixargs((in_target_feature_class, in_container_feature_class, out_table, complex_output), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Intersect3D_3d', None)
def Intersect3D(in_feature_class_1=None, out_feature_class=None, in_feature_class_2=None, output_geometry_type=None):
    """Intersect3D(in_feature_class_1, out_feature_class, {in_feature_class_2}, {output_geometry_type})

        Computes the intersection of multipatch features to produce closed multipatches
        encompassing the overlapping volumes, open multipatch features from the common
        surface areas, or lines from the intersecting edges.

     INPUTS:
      in_feature_class_1 (Feature Layer):
          The multipatch features that will be intersected. When only one input feature
          layer or feature class is provided, the output will indicate the intersection of
          its own features.
      in_feature_class_2 {Feature Layer}:
          The feature class that will be produced by this tool.
      output_geometry_type {String}:
          Determines the type of intersection geometry created.

          * SOLID—Creates a closed multipatch representing the overlapping volumes between
          input features. This is the default.

          * SURFACE—Creates a multipatch surface representing shared faces between input
          features.

          * LINE— Creates lines representing shared edges between input features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The optional second multipatch feature layer or feature class to be intersected
          with the first."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Intersect3D_3d(*gp_fixargs((in_feature_class_1, out_feature_class, in_feature_class_2, output_geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Intersect3DLineWithMultiPatch_3d', None)
def Intersect3DLineWithMultiPatch(in_line_features=None, in_multipatch_features=None, join_attributes=None, out_point_feature_class=None, out_line_feature_class=None):
    """Intersect3DLineWithMultiPatch(in_line_features, in_multipatch_features, {join_attributes}, {out_point_feature_class}, {out_line_feature_class})

        Returns the number of geometric intersections between 3D line and multipatch
        features and also provides optional features that represent points of
        intersection and also divide the 3D lines at such points.

     INPUTS:
      in_line_features (Feature Layer):
          The line features that will be intersected with the multipatch features.
      in_multipatch_features (Feature Layer):
          The multipatch features that the lines will be intersected against.
      join_attributes {String}:
          The input line feature attributes that will be stored with the optional output
          features.

          *  IDS_ONLY— Only feature identification numbers will be stored. This is the
          default.

          * ALL—All attributes will be stored.

     OUTPUTS:
      out_point_feature_class {Feature Class}:
          Optional features that represent points of intersection between the 3D line and
          multipatch.
      out_line_feature_class {Feature Class}:
          Optional line features that divide the input lines at each point of
          intersection with a multipatch feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Intersect3DLineWithMultiPatch_3d(*gp_fixargs((in_line_features, in_multipatch_features, join_attributes, out_point_feature_class, out_line_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IsClosed3D_3d', None)
def IsClosed3D(in_feature_class=None):
    """IsClosed3D(in_feature_class)

        Evaluates multipatch features to determine whether each feature completely
        encloses a volume of space.

     INPUTS:
      in_feature_class (Feature Layer):
          The multipatch features to be tested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IsClosed3D_3d(*gp_fixargs((in_feature_class,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Near3D_3d', None)
def Near3D(in_features=None, near_features=None, search_radius=None, location=None, angle=None, delta=None):
    """Near3D(in_features, near_features;near_features..., {search_radius}, {location}, {angle}, {delta})

        Calculates the three-dimensional distance from each input feature to the nearest
        feature that resides in one or more near feature classes.

     INPUTS:
      in_features (Feature Layer):
          The input feature class whose features will be attributed with information about
          the nearest feature.
      near_features (Feature Layer):
          The one or more features whose proximity to the input features will be
          calculated. If multiple feature classes are specified, an additional field named
          NEAR_FC will be added to the input feature class to identify which near feature
          class contained the closest feature.
      search_radius {Linear unit}:
          The maximum distance for which the nearest features from a given input will be
          determined. If no value is specified, the nearest feature at any distance will
          be determined.
      location {Boolean}:
          Determines whether the coordinates of the nearest point in the input and near
          feature will be added to the input's attribute table.

          * NO_LOCATION—The coordinates are not added to the input feature. This is the
          default.

          * LOCATION—The coordinates are added to the input feature.
      angle {Boolean}:
          Determines whether the horizontal arithmetic angle and vertical angle between
          the input feature and the nearest feature will be added to the input attribute
          table.

          * NO_ANGLE—The angles will not be added to the input's attribute table. This is
          the default.

          * ANGLE—The horizontal arithmetic angle and vertical angle will be added to the
          NEAR_ANG_H and NEAR_ANG_V fields in the input's attribute table.
      delta {Boolean}:
          Determines whether the distances along the X, Y, and Z axes between the input
          feature and the nearest feature will be added to the input attribute table.

          * NO_DELTA—No distances will be added to the input attribute table. This is the
          default.

          * DELTA—Distances along the X, Y, and Z axes will be calculated in the
          NEAR_DELTX, NEAR_DELTY, and NEAR_DELTZ fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Near3D_3d(*gp_fixargs((in_features, near_features, search_radius, location, angle, delta), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Union3D_3d', None)
def Union3D(in_feature_class=None, out_feature_class=None, group_field=None, disable_optimization=None, output_all=None, out_table=None):
    """Union3D(in_feature_class, out_feature_class, {group_field}, {disable_optimization}, {output_all}, {out_table})

        Merges closed, overlapping multipatch features from an input feature class.

     INPUTS:
      in_feature_class (Feature Layer):
          The multipatch features that will be unioned.
      group_field {Field}:
          The field used to identify the features that should be grouped together.
      disable_optimization {Boolean}:
          A many-to-one table that identifies the input features that contribute to each
          output.
      output_all {Boolean}:
          Specifies whether optimization is performed or not performed on the input data.
          Optimization will preprocess the input data by grouping them to improve
          performance and create unique outputs for each set of overlapping features.

          * ENABLE —Optimization is enabled, and the grouping field is ignored. This is
          the default. This is the default.

          *  DISABLE—No optimization is performed on the input data. Features will either
          be stored in a single output feature or be unioned according to their grouping
          field, if one is provided.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output multipatch feature class that will store the aggregated features.
      out_table {Table}:
          Determines if the output feature class contains all features or only the
          overlapping ones that were unioned.

          *  DISABLED —Only unioned features are written to the output. Non-overlapping
          features will be ignored.

          *  ENABLED—All input features are written to the output. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Union3D_3d(*gp_fixargs((in_feature_class, out_feature_class, group_field, disable_optimization, output_all, out_table), True)))
        return retval
    except Exception, e:
        raise e


# CityEngine toolset
@gptooldoc('ExportTo3DWebScene_3d', None)
def ExportTo3DWebScene(in_scene_document=None, out_3d_web_scene=None):
    """ExportTo3DWebScene(in_scene_document, out_3d_web_scene)

        Exports ArcScene documents (.sxd) to Esri CityEngine Web Scene (.3ws) format to
        display them in the CityEngine Web Viewer.The CityEngine Web Viewer uses HTML5
        and WebGL technology to draw 3D content in
        a web browser. There is no need for a plug-in or a Esri CityEngine license to
        view 3D scenes in browsers that support WebGL.

     INPUTS:
      in_scene_document (File):
          The input ArcScene document (.sxd) to be exported to a CityEngine Web Scene.

     OUTPUTS:
      out_3d_web_scene (File):
          The output 3D Web Scene (.3ws) that will be created from the ArcScene document."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportTo3DWebScene_3d(*gp_fixargs((in_scene_document, out_3d_web_scene), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeaturesFromCityEngineRules_3d', None)
def FeaturesFromCityEngineRules(in_features=None, in_rule_package=None, out_feature_class=None):
    """FeaturesFromCityEngineRules(in_features, in_rule_package, out_feature_class)

        Generates 3D geometries from existing 2D and 3D input features using rules
        authored in Esri CityEngine.

     INPUTS:
      in_features (Feature Layer):
          Input polygon, or multipatch features.
      in_rule_package (File):
          The CityEngine rule package *.rpk file containing CGA rule information and
          assets.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing multipatch features with CGA rules applied."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeaturesFromCityEngineRules_3d(*gp_fixargs((in_features, in_rule_package, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e


# Conversion toolset
@gptooldoc('Layer3DToFeatureClass_3d', None)
def Layer3DToFeatureClass(in_feature_layer=None, out_feature_class=None, group_field=None):
    """Layer3DToFeatureClass(in_feature_layer, out_feature_class, {group_field})

        Exports feature layers that have 3D properties defined to a multipatch feature
        class.

     INPUTS:
      in_feature_layer (Feature Layer):
          The input feature layer that has 3D properties defined.
      group_field {Field}:
          The field in the input feature class that identifies the features that will be
          combined into the same multipatch feature. The resulting attributes will be set
          to one of the input records.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output multipatch feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Layer3DToFeatureClass_3d(*gp_fixargs((in_feature_layer, out_feature_class, group_field), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From Feature Class toolset
@gptooldoc('FeatureClassZToASCII_3d', None)
def FeatureClassZToASCII(in_feature_class=None, output_location=None, out_file=None, format=None, delimiter=None, decimal_format=None, digits_after_decimal=None, decimal_separator=None):
    """FeatureClassZToASCII(in_feature_class, output_location, out_file, {format}, {delimiter}, {decimal_format}, {digits_after_decimal}, {decimal_separator})

        Exports 3D features to ASCII text files storing GENERATE, XYZ, or profile data.

     INPUTS:
      in_feature_class (Feature Layer):
          The 3D point, multipoint, polyline, or polygon feature class that will be
          exported to an ASCII file.
      output_location (Folder):
          The folder that output files will be written to.
      out_file (String):
          The name of the resulting ASCII file.If a line or polygon feature class is
          exported to XYZ format, the file name is
          used as a base name. Each feature will have a unique file output since the XYZ
          format only supports one line or polygon per file. Multipart features will also
          have each part written to a separate file. The file name will be appended with
          the OID of each feature, as well as any additional characters needed to make
          each file name unique.
      format {String}:
          The format of the ASCII file being created.

          * GENERATE—Writes output in the GENERATE format. This is the default.

          * XYZ—Writes XYZ information of input features. One file will be created for
          each line or polygon in the input feature.

          * PROFILE—Writes profile information for line features that can be used in
          external graphing applications.
      delimiter {String}:
          The delimiter used to indicate the separation of entries in the columns of the
          text file table.

          * SPACE—A space will be used to delimit field values. This is the default.

          * COMMA—A comma will be used to delimit field values. This option is not
          applicable if the decimal separator is also a comma.
      decimal_format {String}:
          The method used to determine the number of significant digits stored in the
          output files.

          * AUTOMATIC—The number of significant digits needed to preserve the available
          precision, while removing unnecessary trailing zeros, is automatically
          determined. This is the default.

          * FIXED—The number of significant digits is defined in the Digits after Decimal
          parameter.
      digits_after_decimal {Long}:
          Used when the Decimal Notation is set to FIXED. This determines how many digits
          after the decimal are written for floating-point values written to the output
          files.
      decimal_separator {String}:
          The decimal character used to differentiate the integer of a number from its
          fractional part.

          * DECIMAL_POINT—A point is used as the decimal character. This is the default.

          * DECIMAL_COMMA—A comma is used as the decimal character."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureClassZToASCII_3d(*gp_fixargs((in_feature_class, output_location, out_file, format, delimiter, decimal_format, digits_after_decimal, decimal_separator), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MultiPatchFootprint_3d', None)
def MultiPatchFootprint(in_feature_class=None, out_feature_class=None):
    """MultiPatchFootprint(in_feature_class, out_feature_class)

        Creates polygon footprints representing the two-dimensional area occupied by a
        multipatch feature class.

     INPUTS:
      in_feature_class (Feature Layer):
          The multipatch feature whose footprint will be generated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The resulting footprint polygon feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MultiPatchFootprint_3d(*gp_fixargs((in_feature_class, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From File toolset
@gptooldoc('ASCII3DToFeatureClass_3d', None)
def ASCII3DToFeatureClass(input=None, in_file_type=None, out_feature_class=None, out_geometry_type=None, z_factor=None, input_coordinate_system=None, average_point_spacing=None, file_suffix=None, decimal_separator=None):
    """ASCII3DToFeatureClass(input;input..., in_file_type, out_feature_class, out_geometry_type, {z_factor}, {input_coordinate_system}, {average_point_spacing}, {file_suffix}, {decimal_separator})

        Imports 3D features from one or more ASCII files stored in XYZ, XYZI, or
        GENERATE formats into a new feature class.

     INPUTS:
      input (Folder / File):
          The ASCII files or folders containing data in XYZ, XYZI (with lidar intensity),
          or 3D GENERATE format. All input files must be in the same format. If a folder
          is specified, the File Suffix parameter becomes required, and all the files that
          have the same extension as the specified suffix will be processed.
      in_file_type (String):
          The format of the ASCII files that will be converted to a feature class.

          * XYZ—Text file that contain geometry information stored as XYZ coordinates.

          * XYZI—Text files that contain XYZ coordinates alongside intensity measurements.

          * GENERATE—Text files structured in the Generate format.
      out_geometry_type (String):
          The geometry type of the output feature class.

          * MULTIPOINT—Multipoints are recommended the input data contains a large number
          of points and attributes per feature are not required.

          * POINT—Each XYZ coordinate will produce one point feature.

          * POLYLINES—The output will contain polyline features.

          * POLYGONS—The output will contain polygon features.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      input_coordinate_system {Coordinate System}:
          The coordinate system of the input data. The default is an Unknown Coordinate
          System. If specified, the output may or may not be projected into a different
          coordinate system. This depends the whether the geoprocessing environment has a
          coordinate system defined for the location of the target feature class.
      average_point_spacing {Double}:
          The average planimetric distance between points of the input. This parameter is
          only used when the output geometry is set to MULTIPOINT, and its function is to
          provide a means for grouping the points together. This value is used in
          conjunction with the points per shape limit to construct a virtual tile system
          used to group the points. The tile system's origin is based on the domain of the
          target feature class. Specify the spacing in the horizontal units of the target
          feature class.
      file_suffix {String}:
          The suffix of the files to import from an input folder. This parameter is
          required when a folder is specified as input.
      decimal_separator {String}:
          The decimal character used in the text file to differentiate the integer of a
          number from its fractional part.

          * DECIMAL_POINT—A point is used as the decimal character. This is the default.

          * DECIMAL_COMMA—A comma is used as the decimal character.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ASCII3DToFeatureClass_3d(*gp_fixargs((input, in_file_type, out_feature_class, out_geometry_type, z_factor, input_coordinate_system, average_point_spacing, file_suffix, decimal_separator), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Import3DFiles_3d', None)
def Import3DFiles(in_files=None, out_featureClass=None, root_per_feature=None, spatial_reference=None, y_is_up=None, file_suffix=None, in_featureClass=None, symbol_field=None):
    """Import3DFiles(in_files;in_files..., out_featureClass, {root_per_feature}, {spatial_reference}, {y_is_up}, {file_suffix}, {in_featureClass}, symbol_field)

        Imports one or more 3D models into a multipatch feature class.

     INPUTS:
      in_files (File):
          One or more 3D models or folders containing such files in the supported formats,
          which are 3D Studio Max (*.3ds), SketchUp (*.skp), VRML and GeoVRML (*.wrl),
          OpenFlight (*.flt), and COLLADA (*.dae).
      root_per_feature {Boolean}:
          Indicates whether to produce one feature per file or one feature for every root
          node in the file. This option only applies to VRML models.

          * ONE_ROOT_ONE_FEATURE—The generated output will contain one feature for each
          root node in the file.

          * ONE_FILE_ONE_FEATURE—The generated output will contain one file for each
          feature. This is the default.
      spatial_reference {Spatial Reference}:
          The coordinate system of the input data. For the majority of formats, this is
          unknown. Only the GeoVRML format stores its coordinate system, and its default
          will be obtained from the first file in the list unless a spatial reference is
          specified here.
      y_is_up {Boolean}:
          Identifies the axis that defines the vertical orientation of the input files.

          * Z_IS_UP—Indicates that z is up. This is the default.

          * Y_IS_UP—Indicated that y is up.
      file_suffix {String}:
          The file extension of the files to import from an input folder. This parameter
          is required when at least one folder is specified as an input.

          * *—All supported files. This is the default.

          * 3DS—3D Studio Max

          * WRL   —VRML or GeoVRML

          * SKP   —SketchUp 6.0

          * FLT—OpenFlight

          * DAE   —Collada
      in_featureClass {Feature Layer}:
          The point features whose coordinates define the real-world position of the
          input files. Each input file will be matched to its corresponding point based on
          the file names stored in the Symbol Field. The Coordinate System parameter
          should be defined to match the spatial reference of the points.
      symbol_field (Field):
          The field in the point features containing the name of the 3D file associated
          with each point.

     OUTPUTS:
      out_featureClass (Feature Class):
          The multipatch that will be created from the input files."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Import3DFiles_3d(*gp_fixargs((in_files, out_featureClass, root_per_feature, spatial_reference, y_is_up, file_suffix, in_featureClass, symbol_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LASToMultipoint_3d', None)
def LASToMultipoint(input=None, out_feature_class=None, average_point_spacing=None, class_code=None, _return=None, attribute=None, input_coordinate_system=None, file_suffix=None, z_factor=None, folder_recursion=None):
    """LASToMultipoint(input;input..., out_feature_class, average_point_spacing, {class_code;class_code...}, {_return;_return...}, {attribute;attribute...}, {input_coordinate_system}, {file_suffix}, {z_factor}, {folder_recursion})

        Creates multipoint features using one or more lidar files.

     INPUTS:
      input (Folder / File):
          The LAS files that will be imported to a multipoint feature class. If a folder
          is specified, all the LAS files that reside therein will be imported.
      average_point_spacing (Double):
          The average 2D distance between points in the input file or files. This can be
          an approximation. If areas have been sampled at different densities, specify the
          smaller spacing. The value needs to be provided in the projection units of the
          output coordinate system.
      class_code {Long}:
          The classification codes to use as a query filter for LAS data points. Valid
          values range from 1 to 32. No filter is applied by default.
      return {String}:
          The return values that will be used to filter the LAS points that get imported
          to multipoint features.

          * ANY_RETURNS

          * 1

          * 2

          * 3

          * 4

          * 5

          * 6

          * 7

          * 8

          * LAST_RETURNS
      attribute {Value Table}:
          The LAS point properties whose values will be stored in binary large object
          (BLOB) fields in the attribute table of the output. If the resulting features
          will participate in a terrain dataset, the stored attributes can be used to
          symbolize the terrain. The Name column indicates the name of the field that will
          be used to store the specified attributes. The following LAS properties are
          supported:

          * INTENSITY

          * RETURN_NUMBER

          * NUMBER_OF_RETURNS

          * SCAN_DIRECTION_FLAG

          * EDGE_OF_FLIGHTLINE

          * CLASSIFICATION

          * SCAN_ANGLE_RANK

          * FILE_MARKER

          * USER_BIT_FIELD

          * GPS_TIME

          * COLOR_RED

          * COLOR_GREEN

          * COLOR_BLUE
      input_coordinate_system {Coordinate System}:
          The coordinate system of the input LAS file.
      file_suffix {String}:
          The suffix of the files to import from an input folder. This parameter is
          required when a folder is specified as input.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      folder_recursion {Boolean}:
          Scans through subfolders when an input folder is selected containing data in a
          subfolders directory. The output feature class will be generated with a row for
          each file encountered in the directory structure.

          *  NO_RECURSION —Only LAS files found in an input folder will be converted to
          multipoint features. This is the default.

          * RECURSION—All LAS files residing in the subdirectories of an input folder will
          be converted to multipoint features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LASToMultipoint_3d(*gp_fixargs((input, out_feature_class, average_point_spacing, class_code, _return, attribute, input_coordinate_system, file_suffix, z_factor, folder_recursion), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LandXMLToTin_3d', None)
def LandXMLToTin(in_landxml_path=None, out_tin_folder=None, tin_basename=None, tinnames=None):
    """LandXMLToTin(in_landxml_path, out_tin_folder, tin_basename, {tinnames;tinnames...})

        This tool imports one or more triangulated irregular network (TIN) surfaces from
        a LandXML file to output Esri TINs.

     INPUTS:
      in_landxml_path (File):
          The input LandXML file.
      out_tin_folder (Folder):
          The folder that the output TINs will be created in.
      tin_basename (String):
          The basename of the resulting TIN. When several TINs will be exported from the
          LandXML file, the basename is used to define a unique name for each output TIN.
          If <basename> already exists, the tool will not write anything. If <basename>
          does not exist but <basename>2 exists, the tool will create <basename> and
          <basename>2_1, instead of <basename>2.
      tinnames {String}:
          The one or more LandXML TIN surfaces that will be exported to an Esri TIN. Each
          LandXML TIN can be specified by its name or its index position in the LandXML
          file, where the number 1 represents the first TIN, 2 identifies the second, and
          so on."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LandXMLToTin_3d(*gp_fixargs((in_landxml_path, out_tin_folder, tin_basename, tinnames), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PointFileInformation_3d', None)
def PointFileInformation(input=None, out_feature_class=None, in_file_type=None, file_suffix=None, input_coordinate_system=None, folder_recursion=None, extrude_geometry=None, decimal_separator=None, summarize_by_class_code=None, improve_las_point_spacing=None):
    """PointFileInformation(input;input..., out_feature_class, in_file_type, {file_suffix}, {input_coordinate_system}, {folder_recursion}, {extrude_geometry}, {decimal_separator}, {summarize_by_class_code}, {improve_las_point_spacing})

        Generates statistical information about one or more point files in a polygon or
        multipatch output.

     INPUTS:
      input (Folder / File):
          One or more point data files or folders that will be analyzed.
      in_file_type (String):
          The format of the input files.

          * LAS—Airborne lidar format defined by the American Society of Photogrammetry
          and Remote Sensing (ASPRS).

          * XYZ—XYZ file.

          * XYZI—XYZI file.

          * GENERATE—GENERATE file.
      file_suffix {String}:
          The suffix of the files to import when a folder is specified in the input. This
          parameter is required if an input folder is provided.
      input_coordinate_system {Coordinate System}:
          The coordinate system of the input data.
      folder_recursion {Boolean}:
          Scans through subfolders when an input folder is selected containing data in a
          subfolders directory. The output feature class will be generated with a row for
          each file encountered in the directory structure.

          *  NO_RECURSION —Only the data found in the input folder will be used to
          generate the results. This is the default.

          * RECURSION—Any data found in the input folder and its subdirectories will be
          used to generate results.
      extrude_geometry {Boolean}:
          Specifies whether to create a 2D polygon or multipatch feature class with
          extruded features that reflect the elevation range found in each file.

          *  NO_EXTRUSION —The output will be created as a 2D polygon feature class. This
          is the default.

          *  EXTRUSION—The output will be created as a multipatch feature class.
      decimal_separator {String}:
          The decimal character used in the text file to differentiate the integer of a
          number from its fractional part.

          * DECIMAL_POINT—A point is used as the decimal character. This is the default.

          * DECIMAL_COMMA—A comma is used as the decimal character.
      summarize_by_class_code {Boolean}:
          Specifies if the results will summarize LAS files per class code or LAS file.

          *  NO_ SUMMARIZE —Each output feature will represent all the class codes found
          in a lidar file. This is the default.

          *  SUMMARIZE—Each output feature will represent a single class code found in a
          lidar file.
      improve_las_point_spacing {Boolean}:
          Provides enhanced assessment of the point spacing in LAS files that can reduce
          over-estimation caused by irregular data distribution.

          * LAS_SPACING—Regular point spacing estimate is used for LAS files, where the
          extent is equally divided by the number of points. This is the default.

          * NO_LAS_SPACING—Binning will be used to obtain a more precise point spacing
          estimate for LAS files. This may increase the tool's execution time.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PointFileInformation_3d(*gp_fixargs((input, out_feature_class, in_file_type, file_suffix, input_coordinate_system, folder_recursion, extrude_geometry, decimal_separator, summarize_by_class_code, improve_las_point_spacing), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From LAS Dataset toolset
@gptooldoc('LasDatasetToTin_3d', None)
def LasDatasetToTin(in_las_dataset=None, out_tin=None, thinning_type=None, thinning_method=None, thinning_value=None, max_nodes=None, z_factor=None):
    """LasDatasetToTin(in_las_dataset, out_tin, {thinning_type}, {thinning_method}, {thinning_value}, {max_nodes}, {z_factor})

        Exports a triangulated irregular network (TIN) from a LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      thinning_type {String}:
          Specifies the technique used for selecting a subset of LAS data points that
          would be exported to TIN.

          * NONE—No thinning is applied. This is the default.

          * RANDOM—Randomly selects LAS data points based on the corresponding
          thinning_method selection and thinning_value entry.

          * WINDOW_SIZE—Divides the LAS dataset into square tiles defined by the
          thinning_value, then selects LAS points using the thinning_method.
      thinning_method {String}:
          Specifies the technique used for reducing the LAS data points, which impacts
          the interpretation of the Thinning Value. The available options depend on the
          selected Thinning Type.

          * PERCENT—Thinning value will reflect a percentage of points in the LAS dataset.

          * NODE_COUNT—Thinning value will reflect the total number of nodes that are
          allowed in the output.

          * MIN—LAS data point with the lowest elevation in each window size areas

          * MAX—Selects LAS data point with the highest elevation in each of the
          automatically determined window size areas.

          * CLOSEST_TO_MEAN—Selects LAS data point whose elevation is closest to the
          average value found in the automatically determined window size areas.
           Specifies the technique used for reducing the LAS data points, which impacts
          the interpretation of the thinning_value. The available options depend on the
          selected thinning_type.

          * PERCENT— The thinning_value will reflect a percentage of the total points in
          the LAS dataset. This option is only available when thinning_type = "RANDOM".

          * NODE_COUNT—The thinning_value will reflect the total number of nodes that are
          allowed in the output. This option is only available when thinning_type =
          "RANDOM".

          * MIN—Selects the LAS point with the lowest elevation in each window size area.
          This option is only available when thinning_type = "WINDOW_SIZE".

          * MAX—Selects the LAS point with the highest elevation in each window size area.
          This option is only available when thinning_type = "WINDOW_SIZE".

          * CLOSEST_TO_MEAN—Selects the LAS point whose elevation is closest to the
          average value of all LAS points in each window size areas. This option is only
          available when thinning_type = "WINDOW_SIZE".
      thinning_value {Double}:
          If thinning_type = "WINDOW_SIZE" this value represents the sampling area of that
          the LAS dataset will be divided by.If thinning_type = "RANDOM" and
          thinning_method = "PERCENT", this value
          represents the percent of points from the LAS dataset that will be exported to
          the TIN.If thinning_type = "RANDOM" and thinning_method = "NODE_COUNT", this
          value
          represents the total number of LAS points that can be exported to the TIN.
      max_nodes {Double}:
          The maximum number of nodes permitted in the output TIN. The default is 5
          million.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LasDatasetToTin_3d(*gp_fixargs((in_las_dataset, out_tin, thinning_type, thinning_method, thinning_value, max_nodes, z_factor), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From Raster toolset
@gptooldoc('RasterDomain_3d', None)
def RasterDomain(in_raster=None, out_feature_class=None, out_geometry_type=None):
    """RasterDomain(in_raster, out_feature_class, out_geometry_type)

        Creates a polygon or polyline footprint of the data portions of a raster
        dataset.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster to process.
      out_geometry_type (String):
          The geometry of the output feature class.

          *  LINE—The output will be a z-enabled line feature class.

          * POLYGON—The output will be a z-enabled polygon feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterDomain_3d(*gp_fixargs((in_raster, out_feature_class, out_geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterTin_3d', None)
def RasterTin(in_raster=None, out_tin=None, z_tolerance=None, max_points=None, z_factor=None):
    """RasterTin(in_raster, out_tin, {z_tolerance}, {max_points}, {z_factor})

        Converts a raster to a triangulated irregular network (TIN) dataset.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster to process.
      z_tolerance {Double}:
          The maximum allowable difference in (z units) between the height of the input
          raster and the height of the output TIN. By default, the z tolerance is 1/10 of
          the z range of the input raster.
      max_points {Long}:
          The maximum number of points that will be added to the TIN before the process is
          terminated. By default, the process will continue until all the points are
          added.
      z_factor {Double}:
          The factor that the height values of the raster will be multiplied by in the
          resulting TIN dataset. This is typically used to convert Z units to match XY
          units.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterTin_3d(*gp_fixargs((in_raster, out_tin, z_tolerance, max_points, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToMultipoint_3d', None)
def RasterToMultipoint(in_raster=None, out_feature_class=None, out_vip_table=None, method=None, kernel_method=None, z_factor=None):
    """RasterToMultipoint(in_raster, out_feature_class, {out_vip_table}, {method}, {kernel_method}, {z_factor})

        Converts raster cell centers into 3D multipoint features whose Z values reflect
        the raster cell value.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster to process.
      method {String}:
          The thinning method applied to the input raster to select a subset of cells that
          will be exported to the multipoint feature class.

          * NO_THIN—No thinning will be applied. This is the default.

          * ZTOLERANCE <value>—Only exports the cells that are required for maintaining a
          surface within the specified Z-range of the input raster. The corresponding
          value reflects the maximum allowable difference in z units between the input
          raster and the surface created from the output multipoint feature class. When
          selecting this method, the thinning value defaults to one tenth of the z range
          of the input raster.

          * KERNEL <value>—Divides the raster into equal sized tiles based on the thinning
          value, then selects one or two cells which meet the criteria defined by the
          designated kernel method. The corresponding value defaults to 3, which means the
          raster would be divided into 3 cell by 3 cell windows.

          * VIP <value>—Employs a roving 3 cell by 3 cell window that is used to create a
          3-dimensional best fit plane. Each cell is given a significance score based on
          its absolute deviation from this plane. A histogram of these scores is then used
          to determine the cells that get exported. The corresponding value reflects the
          percentile rank along the histogram of significance scores. This value defaults
          to 5.0, which means the cells whose score was within the top 5% of the histogram
          will be exported.

          * VIP_HISTOGRAM—Creates a table to view the actual significance values and the
          corresponding number of points associated with those values.
      kernel_method {String}:
          The selection method used within each kernel neighborhood when kernel thinning
          is applied on the input raster.

          * MIN—A point is created at the cell with the smallest elevation value found in
          the kernel neighborhood. This is the default.

          * MAX—A point is created at the cell with the largest elevation value found in
          the kernel neighborhood.

          * MINMAX—Two points are created at the cells with the smallest and largest Z
          values found in the kernel neighborhood.

          * MEAN—A point is created at the cell whose elevation value is closest to the
          average of the cells in the kernel neighborhood.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool.
      out_vip_table {Table}:
          The histogram table to be produced when VIP Histogram is specified for the
          Method parameter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToMultipoint_3d(*gp_fixargs((in_raster, out_feature_class, out_vip_table, method, kernel_method, z_factor), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From TIN toolset
@gptooldoc('TinDomain_3d', None)
def TinDomain(in_tin=None, out_feature_class=None, out_geometry_type=None):
    """TinDomain(in_tin, out_feature_class, out_geometry_type)

        Creates a line or polygon feature class representing the interpolation zone of a
        triangulated irregular network (TIN) dataset.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      out_geometry_type (String):
          The geometry of the output feature class.

          *  LINE—The output will be a z-enabled line feature class.

          * POLYGON—The output will be a z-enabled polygon feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinDomain_3d(*gp_fixargs((in_tin, out_feature_class, out_geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinEdge_3d', None)
def TinEdge(in_tin=None, out_feature_class=None, edge_type=None):
    """TinEdge(in_tin, out_feature_class, {edge_type})

        Creates 3D line features using the triangle edges of a triangulated irregular
        network (TIN) dataset.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      edge_type {String}:
          The triangle edge that will be exported.

          * DATA—Edges representing the interpolation zone. This is the default.

          * SOFT—Edges representing gradual breaks in slope.

          * HARD—Edges representing distinct breaks in slope.

          * ENFORCED—Edges that were not introduced by the TIN's triangulation.

          * REGULAR—Edges that were created by the TIN's triangulation.

          * OUTSIDE—Edges that are excluded from the interpolation zone.

          * ALL—All edges, included those that were excluded from the interpolation zone.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinEdge_3d(*gp_fixargs((in_tin, out_feature_class, edge_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinLine_3d', None)
def TinLine(in_tin=None, out_feature_class=None, code_field=None):
    """TinLine(in_tin, out_feature_class, {code_field})

        Exports breaklines from a triangulated irregular network (TIN) dataset to a 3D
        line feature class.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      code_field {String}:
          The name of the field in the output feature class that defines the breakline
          type. The default field name is Code.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinLine_3d(*gp_fixargs((in_tin, out_feature_class, code_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinNode_3d', None)
def TinNode(in_tin=None, out_feature_class=None, spot_field=None, tag_field=None):
    """TinNode(in_tin, out_feature_class, {spot_field}, {tag_field})

        Exports the nodes of a triangulated irregular network (TIN) dataset to a point
        feature class.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      spot_field {String}:
          The name of the elevation attribute field of the output feature class. If a name
          is given, the feature class will be 2D; otherwise, it will be 3D. No name is
          provided by default, which results in the creation of 3D point features.
      tag_field {String}:
          The name of the field storing the tag attribute in the output feature class. By
          default, no tag value field is created.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinNode_3d(*gp_fixargs((in_tin, out_feature_class, spot_field, tag_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinPolygonTag_3d', None)
def TinPolygonTag(in_tin=None, out_feature_class=None, tag_field=None):
    """TinPolygonTag(in_tin, out_feature_class, {tag_field})

        Creates polygon features using tag values in a triangulated irregular network
        (TIN) dataset.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      tag_field {String}:
          The name of the field storing the tag attribute in the output feature class. The
          default field name is Tag_Value.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinPolygonTag_3d(*gp_fixargs((in_tin, out_feature_class, tag_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinRaster_3d', None)
def TinRaster(in_tin=None, out_raster=None, data_type=None, method=None, sample_distance=None, z_factor=None):
    """TinRaster(in_tin, out_raster, {data_type}, {method}, {sample_distance}, {z_factor})

        Creates a raster by interpolating its cell values from the elevation of the
        input TIN at the specified sampling distance.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      data_type {String}:
          The data type of the output raster can be defined by the following keywords:

          * FLOAT—Output raster will use 32-bit floating point, which supports values
          ranging from -3.402823466e+38 to 3.402823466e+38. This is the default.

          * INT—Output raster will use an appropriate integer bit depth. This option will
          round Z-values to the nearest whole number and write an integer to each raster
          cell value.
      method {String}:
          The interpolation method used to create the raster.

          * LINEAR—Calculates cell values by applying linear interpolation to the TIN
          triangles. This is the default.

          * NATURAL_NEIGHBORS—Calculates cell values by using natural neighbors
          interpolation of TIN triangles
      sample_distance {String}:
          The sampling method and distance used to define the cell size of the output
          raster.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.

     OUTPUTS:
      out_raster (Raster Dataset):
          The location and name of the output raster. When storing a raster dataset in a
          geodatabase or in a folder such as an Esri Grid, no file extension should be
          added to the name of the raster dataset. A file extension can be provided to
          define the raster's format when storing it in a folder, such as .tif to generate
          a GeoTIFF or .img to generate an ERDAS IMAGINE format file.If the raster is
          stored as a TIFF file or in a geodatabase, its raster
          compression type and quality can be specified using geoprocessing environment
          settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinRaster_3d(*gp_fixargs((in_tin, out_raster, data_type, method, sample_distance, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TinTriangle_3d', None)
def TinTriangle(in_tin=None, out_feature_class=None, units=None, z_factor=None, hillshade=None, tag_field=None):
    """TinTriangle(in_tin, out_feature_class, {units}, {z_factor}, {hillshade}, {tag_field})

        Exports triangle faces from a TIN dataset to polygon features and provides
        slope, aspect, and optional attributes of hillshade and tag values for each
        triangle.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      units {String}:
          The units of measure to be used in calculating slope.

          * PERCENT—Slope is expressed as a percentage value. This is the default.

          * DEGREE—Slope is expressed as the angle of inclination from a horizontal plane.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      hillshade {String}:
          Specifies the azimuth and altitude angles of the light source when applying a
          hillshade effect for the feature layer output. Azimuth can range from 0 to 360
          degrees, whereas altitude can range from 0 to 90. An azimuth of 45 degrees and
          altitude of 30 degrees would be entered as "HILLSHADE 45, 30".
      tag_field {String}:
          The field name in the output feature that will store the triangle tag value.
          This parameter is empty by default, which will result in tag values not being
          written to the output.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TinTriangle_3d(*gp_fixargs((in_tin, out_feature_class, units, z_factor, hillshade, tag_field), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From Terrain toolset
@gptooldoc('TerrainToPoints_3d', None)
def TerrainToPoints(in_terrain=None, out_feature_class=None, pyramid_level_resolution=None, source_embedded_feature_class=None, out_geometry_type=None):
    """TerrainToPoints(in_terrain, out_feature_class, {pyramid_level_resolution}, {source_embedded_feature_class}, {out_geometry_type})

        Converts a terrain dataset into a new point or multipoint feature class.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.
      source_embedded_feature_class {String}:
          The name of the terrain dataset's embedded points to be exported. If an embedded
          feature is specified, only the points from the feature will be written to the
          output. Otherwise, all points from all data sources in the terrain will be
          exported.
      out_geometry_type {String}:
          The geometry of the output feature class.

          * MULTIPOINT—The output point features will be written to a multipoint feature
          class. This is the default.

          * POINT—The output point features will be written to a point feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TerrainToPoints_3d(*gp_fixargs((in_terrain, out_feature_class, pyramid_level_resolution, source_embedded_feature_class, out_geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TerrainToRaster_3d', None)
def TerrainToRaster(in_terrain=None, out_raster=None, data_type=None, method=None, sample_distance=None, pyramid_level_resolution=None):
    """TerrainToRaster(in_terrain, out_raster, {data_type}, {method}, {sample_distance}, {pyramid_level_resolution})

        Interpolates a raster from a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      data_type {String}:
          The data type of the output raster can be defined by the following keywords:

          * FLOAT—Output raster will use 32-bit floating point, which supports values
          ranging from -3.402823466e+38 to 3.402823466e+38. This is the default.

          * INT—Output raster will use an appropriate integer bit depth. This option will
          round Z-values to the nearest whole number and write an integer to each raster
          cell value.
      method {String}:
          The interpolation method that will be used to calculate cell values.

          * LINEAR—Applies a distance based weight to the Z of each node in the triangle
          encompassing the center of a given cell, then sums the weighted values to assign
          the cell value. This is the default.

          * NATURAL_NEIGHBORS—Applies an area based weighting scheme that uses Voronoi
          polygons to determine cell values.
      sample_distance {String}:
          The sampling method and distance used to define the cell size of the output
          raster.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_raster (Raster Dataset):
          The location and name of the output raster. When storing a raster dataset in a
          geodatabase or in a folder such as an Esri Grid, no file extension should be
          added to the name of the raster dataset. A file extension can be provided to
          define the raster's format when storing it in a folder, such as .tif to generate
          a GeoTIFF or .img to generate an ERDAS IMAGINE format file.If the raster is
          stored as a TIFF file or in a geodatabase, its raster
          compression type and quality can be specified using geoprocessing environment
          settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TerrainToRaster_3d(*gp_fixargs((in_terrain, out_raster, data_type, method, sample_distance, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TerrainToTin_3d', None)
def TerrainToTin(in_terrain=None, out_tin=None, pyramid_level_resolution=None, max_nodes=None, clip_to_extent=None):
    """TerrainToTin(in_terrain, out_tin, {pyramid_level_resolution}, {max_nodes}, {clip_to_extent})

        Converts a terrain dataset to a triangulated irregular network (TIN) dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.
      max_nodes {Long}:
          The maximum number of nodes permitted in the output TIN. The tool will return an
          error if the analysis extent and pyramid level would produce a TIN that exceeds
          this size. The default is 5 million.
      clip_to_extent {Boolean}:
          Specifies whether the resulting TIN will be clipped against the analysis extent.
          This only has an effect if the analysis extent is defined and it's smaller than
          the extent of the input terrain.

          * CLIP—Clips the output TIN against the analysis extent. This is the default.

          * NO_CLIP—Does not clip the output TIN against the analysis extent.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TerrainToTin_3d(*gp_fixargs((in_terrain, out_tin, pyramid_level_resolution, max_nodes, clip_to_extent), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\LAS Dataset toolset
@gptooldoc('ChangeLasClassCodes_3d', None)
def ChangeLasClassCodes(in_las_dataset=None, class_codes=None, compute_stats=None):
    """ChangeLasClassCodes(in_las_dataset, class_codes;class_codes..., {compute_stats})

        Modifies the class code values of LAS files referenced by a LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      class_codes (Value Table):
          Specify each pair of current and new class code values as a space-delimited
          string or a list of integers. For example, a current class code of 5 can be
          changed to 2 by specifying "5 2" or [5, 2]. Multiple class codes can be entered
          as a semicolon-delimited string ("5 2; 8 3; 1 4"), a list of strings (for
          example, [[5, 2], [8, 3], [1, 4]]).
      compute_stats {Boolean}:
          Specifies whether statistics should be computed for the LAS files referenced by
          the LAS dataset. The presence of statistics allows the LAS dataset layer's
          filtering and symbology options to only show LAS attribute values that exist in
          the LAS files.

          * COMPUTE_STATS—Statistics will be computed.

          * NO_COMPUTE_STATS—Statistics will not be computed. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ChangeLasClassCodes_3d(*gp_fixargs((in_las_dataset, class_codes, compute_stats), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ClassifyLasByHeight_3d', None)
def ClassifyLasByHeight(in_las_dataset=None, ground_source=None, height_classification=None, noise=None, compute_stats=None, extent=None, process_entire_files=None):
    """ClassifyLasByHeight(in_las_dataset, ground_source, height_classification;height_classification..., {noise}, {compute_stats}, {extent}, {process_entire_files})

        Reclassifies lidar points based on their height from the ground surface.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed. Only LAS points with class codes 0 and
          1 will be reclassified.
      ground_source (String):
          The source of ground measurements that will be used to determine height above
          ground.

          * GROUND—LAS points designated with the ground classification code value of 2
          and model key code value of 8 will be used.

          * MODEL_KEY—Only LAS points designated with the model key classification code
          value of 8 will be used.
      height_classification (Value Table):
          The class code value that will be assigned to LAS points that fall within the
          range of values derived from the specified height from ground. The order of
          entry influences the height ranges that are used to define the reclassification
          of LAS points. The first entry's Z-range will span from the ground surface to
          the specified height_from_ground value. The Z-range of subsequent entries will
          span from the upper limit of the preceding entry to its own height_from_ground
          value.
      noise {String}:
          Indicates whether to reclassify points as noise based on their proximity from
          the ground. Noise artifacts in lidar data can be introduced by sensor errors and
          the inadvertent interception of aerial obstructions like birds in the path of
          the lidar pulse.

          * ALL_NOISE—Both low and high noise will be classified.

          * HIGH_NOISE—Only points that are above the maximum height in the LAS
          classification table will be reclassified as high noise.

          * LOW_NOISE—Only points below the ground surface will be reclassified as noise.
          This is only available when all ground points are used to define the ground
          surface.

          * NONE—No points will be reclassified as noise.
      compute_stats {Boolean}:
          Specifies whether statistics should be computed for the LAS files referenced by
          the LAS dataset. The presence of statistics allows the LAS dataset layer's
          filtering and symbology options to only show LAS attribute values that exist in
          the LAS files.

          * COMPUTE_STATS—Statistics will be computed.

          * NO_COMPUTE_STATS—Statistics will not be computed. This is the default.
      extent {Extent}:
          Specify the extent of the data that will be evaluated by this tool.
      process_entire_files {Boolean}:
          Specify how the processing extent is applied.

          *  PROCESS_ENTIRE_FILE—Only LAS points that are within the processing extent
          will be evaluated. This is the default.

          * PROCESS_EXTENT—All points in the LAS files that intersect the processing
          extent will be evaluated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ClassifyLasByHeight_3d(*gp_fixargs((in_las_dataset, ground_source, height_classification, noise, compute_stats, extent, process_entire_files), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LasPointStatsByArea_3d', None)
def LasPointStatsByArea(in_las_dataset=None, in_features=None, out_property=None):
    """LasPointStatsByArea(in_las_dataset, in_features, {out_property;out_property...})

        Evaluates the statistics of LAS points that overlay the area defined by polygon
        features.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      in_features (Feature Layer):
          The polygon that defines the area for which statistics will be reported.
      out_property {String}:
          The properties that will be calculated.

          * Z_MIN—The lowest Z value of LAS points overlapping the feature.

          * Z_MAX—The highest Z value of LAS points overlapping the feature.

          * Z_MEAN—The average Z value of LAS points overlapping the feature.

          * POINT_COUNT—The tally of LAS points that were evaluated.

          * STANDARD_DEVIATION—The standard deviation of Z values."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LasPointStatsByArea_3d(*gp_fixargs((in_las_dataset, in_features, out_property), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LocateLasPointsByProximity_3d', None)
def LocateLasPointsByProximity(in_las_dataset=None, in_features=None, search_radius=None, count_field=None, out_features=None, geometry=None, class_code=None, compute_stats=None):
    """LocateLasPointsByProximity(in_las_dataset, in_features, {search_radius}, {count_field}, {out_features}, {geometry}, {class_code}, {compute_stats})

        Identifies lidar points within the three-dimensional proximity of z-enabled
        features while also providing the option to reclassify the points and export
        them to an output feature class.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      in_features (Feature Layer):
          The 3D point, line, or polygon features whose proximity will be used for
          identifying LAS points.
      search_radius {Linear unit / Field}:
          The distance of the space around the input features that will be evaluated for
          the presence of LAS points, which can be provided as either a linear distance or
          a numeric field in the input feature's attribute table.If the search radius is
          derived from a field or a linear distance whose units
          are specified as Unknown, the linear unit of the input features' XY spatial
          reference is used.The following units are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS
      count_field {String}:
          The name of the count field that will be added to the input feature's attribute
          table. The field's values will reflect the sum of LAS points that are in the
          proximity of an input feature.
      geometry {String}:
          The geometry of the output point features that represent the LAS points found
          within the specified proximity of the input features.

          * MULTIPOINT—Multipoint features that will have multiple points in each row.

          * POINT—Single-point features that will have a unique row for each identified
          LAS point.
      class_code {Long}:
          The class code value that will be used to reclassify the points found within
          the search radius of the input features.
      compute_stats {Boolean}:
          Specifies whether statistics should be computed for the LAS files referenced by
          the LAS dataset. The presence of statistics allows the LAS dataset layer's
          filtering and symbology options to only show LAS attribute values that exist in
          the LAS files.

          * COMPUTE_STATS—Statistics will be computed.

          * NO_COMPUTE_STATS—Statistics will not be computed. This is the default.

     OUTPUTS:
      out_features {Feature Class}:
          Output point features that represent the LAS points found within the specified
          proximity of the input features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LocateLasPointsByProximity_3d(*gp_fixargs((in_las_dataset, in_features, search_radius, count_field, out_features, geometry, class_code, compute_stats), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetLasClassCodesUsingFeatures_3d', None)
def SetLasClassCodesUsingFeatures(in_las_dataset=None, feature_class=None, compute_stats=None):
    """SetLasClassCodesUsingFeatures(in_las_dataset, feature_class;feature_class..., {compute_stats})

        Classifies data points in LAS files referenced by a LAS dataset using point,
        line, and polygon features.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      feature_class (Value Table):
          Specify one or more feature classes that will be used to define class code
          values for the lidar files referenced by a LAS dataset. Each feature will have
          the following options that can be specified:

          * features—The feature layer or full path to the input feature class.

          * buffer_distance—The selection tolerance used in determining which lidar points
          will be modified by the input features.

          * new_class—The class code to be assigned to the lidar files that intersect with
          the features and the associated buffer distance.

          * synthetic—Specifies whether to flag or remove a Synthetic designation, which
          implies that the point was not created with lidar, but an alternate technique
          (for example, digitized from photogrammetric stereo model).

          * key_point—Specifies whether to flag or remove a Key Point designation for the
          data point. A model key point is typically treated as an anchor point that does
          not get removed by any thinning algorithm.

          * withheld—Specifies whether to flag or remove a Withheld designation for the
          data point, which is generally used to signify erroneous data.
      compute_stats {Boolean}:
          Specifies whether statistics should be computed for the LAS files referenced by
          the LAS dataset. The presence of statistics allows the LAS dataset layer's
          filtering and symbology options to only show LAS attribute values that exist in
          the LAS files.

          * COMPUTE_STATS—Statistics will be computed.

          * NO_COMPUTE_STATS—Statistics will not be computed. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetLasClassCodesUsingFeatures_3d(*gp_fixargs((in_las_dataset, feature_class, compute_stats), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\TIN toolset
@gptooldoc('CopyTin_3d', None)
def CopyTin(in_tin=None, out_tin=None, version=None):
    """CopyTin(in_tin, out_tin, {version})

        Creates a copy of a triangulated irregular network (TIN) dataset.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      version {String}:
          The version of the output TIN.

          *  CURRENT—The current TIN version at ArcGIS 10.0, which supports constrained
          Delaunay triangulation. This is the default.

          * PRE_10.0—The TIN version supported prior to ArcGIS 10.0, which only supports
          conforming Delaunay triangulation.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyTin_3d(*gp_fixargs((in_tin, out_tin, version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateTin_3d', None)
def CreateTin(out_tin=None, spatial_reference=None, in_features=None, constrained_delaunay=None):
    """CreateTin(out_tin, {spatial_reference}, {in_features;in_features...}, {constrained_delaunay})

        Creates a triangulated irregular network (TIN) dataset.

     INPUTS:
      spatial_reference {Coordinate System}:
          The spatial reference of the output TIN.
      in_features {Value Table}:
          Add references to one or more feature classes that will be included in the TIN.
          For each feature class you'll need to set properties that indicate how it's used
          to define the surface.in_feature_class:  The feature class whose features will
          be imported into the
          TIN.height_field: The field that specifies the source of elevation values for
          the
          features. Any numeric field in the feature's attribute table can be used. If the
          feature supports z-values, the feature geometry can be read by selecting the
          Shape.Z option. If no height is desired, specify the keyword <None> to create
          Z-less features whose elevation would be interpolated from the surface.SF_type:
          The surface feature type defines how the geometry imported from the
          features are incorporated into the triangulation for the surface. Options with
          hard or soft designation refer to whether the feature edges represent distinct
          breaks in slope or a gradual change when the triangulated surface gets converted
          to a raster. The following keywords are available:

          * masspoints—Elevation points that will be imported as nodes

          * hardline or softline—Breaklines that enforce a height value

          * hardclip or softclip—Polygon dataset that defines the boundary of the TIN

          * harderase or softerase— Polygon dataset that defines holes in the interior
          portions of the TIN

          * hardreplace or softreplace—Polygon dataset that defines areas of constant
          height

          * hardvaluefill or softvaluefill—Polygon dataset that defines tag values for the
          triangles based on the integer field specified in the tag_value column
          tag_value: The integer field from the attribute table of the feature class that
          will be used when the surface feature type is set to a value fill option. Tag
          fill is used as a basic form of triangle attribution whose boundaries are
          enforced in the triangulation as breaklines. The default option is set to
          <none>.
      constrained_delaunay {Boolean}:
          Specifies the triangulation technique used along the breaklines of the TIN.

          * DELAUNAY—The TIN will use Delaunay conforming triangulation, which may densify
          each segment of the breaklines to produce multiple triangle edges. This is the
          default.

          *  CONSTRAINED_DELAUNAY—The TIN will use constrained Delaunay triangulation,
          which will add each segment as a single edge. Delaunay triangulation rules are
          honored everywhere except along breaklines, which will not get densified.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateTin_3d(*gp_fixargs((out_tin, spatial_reference, in_features, constrained_delaunay), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DelineateTinDataArea_3d', None)
def DelineateTinDataArea(in_tin=None, max_edge_length=None, method=None):
    """DelineateTinDataArea(in_tin, max_edge_length, {method})

        Redefines the data area, or interpolation zone, of a triangulated irregular
        network (TIN) based on its triangle edge length.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      max_edge_length (Double):
          The two-dimensional distance that defines the maximum length of a TIN triangle
          edge in the TIN's data area. Triangles with one or more edges that exceed this
          value will be considered outside the TIN's interpolation zone and will not be
          rendered in maps or used in surface analysis.
      method {String}:
          The TIN edges that will be evaluated when delineating the TIN's data area.

          * PERIMETER_ONLY—Iterates through triangles from the TIN's outer extent inward
          and will stop when the current iteration of boundary triangle edges does not
          exceed the Maximum Edge Length. This is the default.

          * ALL—Classifies the entire collection of TIN triangles by edge length."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DelineateTinDataArea_3d(*gp_fixargs((in_tin, max_edge_length, method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EditTin_3d', None)
def EditTin(in_tin=None, in_features=None, constrained_delaunay=None):
    """EditTin(in_tin, in_features;in_features..., {constrained_delaunay})

        Adds features from one or more input feature classes that define the surface
        area of a triangulated irregular network (TIN).

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      in_features (Value Table):
          Specify features that will be included in the TIN. Each input can have the
          following properties set to define the manner in which its features contribute
          to the surface: height_field—The field supplying elevation values for the
          features. Valid
          options include any numeric field and the Shape field, if the feature geometry
          supports Z-values. The <None> keyword is also available for features that do not
          have any qualifying fields or do not require elevation values. Z-less features
          have their values interpolated from the surrounding surface.tag_value—The fill
          polygons that assign integer values to triangles as a basic
          form of attribution. Their boundaries are enforced in the triangulation as
          breaklines. Triangles inside these polygons are attributed with the tag values.
          Specify the name of the feature class attribute to use as tag values in the TIN.
          If tag values are not to be used, specify <none>.SF_type—The surface feature
          type that defines how the feature geometry gets
          incorporated into the triangulation for the surface. Point features can only be
          used as masspoints, whereas line features can be defined as breaklines, and
          polygons can be defined as the masspoints option, whereas lines can be defined
          as clip, erase, replace, and value fill features. Breaklines and polygon surface
          types have 'hard' and 'soft' qualifiers that indicate whether the features
          represent smooth or sharp discontinuties on the surface.use_z—Specifies whether
          Z values are used when the SHAPE field of the input
          feature is indicated as the height source. Selecting true will result in Z
          values being used, and false will result in M, or measure values, being used.
          Z's are used by default.
      constrained_delaunay {Boolean}:
          A constrained Delaunay triangulation conforms to Delaunay rules everywhere
          except along breaklines. When using conforming Delaunay triangulation,
          breaklines are densified by the software; therefore, one input breakline segment
          can result in multiple triangle edges. When using constrained Delaunay
          triangulation no densication occurs and each breakline segment is added as a
          single edge.

          * DELAUNAY— The triangulation will fully conform to the Delaunay rules. This is
          the default.

          *  CONSTRAINED_DELAUNAY—The Delaunay triangulation will be constrained."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EditTin_3d(*gp_fixargs((in_tin, in_features, constrained_delaunay), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Terrain Dataset toolset
@gptooldoc('AddFeatureClassToTerrain_3d', None)
def AddFeatureClassToTerrain(in_terrain=None, in_features=None):
    """AddFeatureClassToTerrain(in_terrain, in_features;in_features...)

        Adds one or more feature classes to a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain to which feature classes will be added. The terrain dataset must
          already have one or more pyramid levels created.
      in_features (Value Table):
          Identifies features being added to the terrain. Each feature must reside in the
          same feature dataset as the terrain and have its role defined through the
          following properties:

          * Input Features—Name of the feature class being added to the terrain.

          * Height Field—Field containing the feature's height information. Any numeric
          field can be specified, and Z-enabled features can also choose the geometry
          field. If the <none> option is chosen, Z-values are interpolated from the
          surface.

          * SF Type—Surface feature type that defines how the features contributes to the
          terrain. Mass points denote features that contribute Z measurements; breaklines
          denote linear features with known Z measurements, and several polygon types.
          Breaklines and polygon-based feature types also have hard and soft qualifiers
          that define the interpolation behavior around the feature's edges when exporting
          to raster. Soft features exhibit gradual changes in slope, whereas hard features
          represent sharp discontinuities.

          * Group—Defines the group of each contributing feature. Unspecification of
          breaklines and polygon surface features representing the same geographic
          features at different levels of detail are intended for display at certain scale
          ranges. Data representing the same geographic features at different levels of
          detail can be grouped by assigning the same numeric value. For example,
          assigning two boundary features with a high and low level of detail to the same
          group would ensure there is no overlap in their associated display scale range.

          * Min/Max Resolution—Defines the range of pyramid resolutions at which the
          feature is enforced in the terrain. Mass points must use the smallest and
          largest range of values.

          * Overview—Indicates whether the feature is enforced at the coarsest
          representation of the terrain dataset. To maximize display performance, make
          sure that feature classes represented in the overview contain simplified
          geometry. Only valid for feature types other than mass points.

          * Embed—Setting this option to TRUE indicates the source features will be copied
          to a hidden feature class that will be referenced by and only available to the
          terrain. Embedded features will not be directly viewable, as they can only be
          accessed through terrain tools. Only valid for multipoint features.

          * Embed Name—Name of the embedded feature class. Only applies if the feature is
          being embedded.

          * Embed Fields—Specifies Blob field attributes to be retained in the embedded
          feature class. These attributes can be used to symbolize the terrain. LAS
          attribution can be stored in Blob fields of multipoint features through the LAS
          To Multipoint tool.

          * Anchor—Specifies whether the point feature class will be anchored through all
          terrain pyramid levels. Anchor points are never filtered or thinned away to
          ensure they persist in the terrain surface. This option only applies to single-
          point feature classes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddFeatureClassToTerrain_3d(*gp_fixargs((in_terrain, in_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddTerrainPyramidLevel_3d', None)
def AddTerrainPyramidLevel(in_terrain=None, pyramid_type=None, pyramid_level_definition=None):
    """AddTerrainPyramidLevel(in_terrain, {pyramid_type}, pyramid_level_definition;pyramid_level_definition...)

        Adds one or more pyramid levels to an existing terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      pyramid_type {String}:
          The z-tolerance or window size and its associated reference scale for each
          pyramid level being added to the terrain. Each pyramid level is entered as a
          space-delimited pair of the pyramid level resolution and reference scale (for
          example, "20 24000" for a window size of 20 and reference scale of 1:24000, or
          "1.5 10000" for a z-tolerance of 1.5 and reference scale of 1:10000). The
          pyramid level resolution can be provided as a floating-point value, while the
          reference scale must be entered as a whole number. The z-tolerance value
          represents the maximum deviation that can occur from the
          elevation of the terrain at full resolution, whereas the window size value
          defines the area of the terrain tile used in thinning elevation points by
          selecting one or two points from the area based on the window size method
          defined during the creation of the terrain. The reference scale represents the
          largest map scale at which the pyramid level is enforced. When the terrain is
          displayed at a scale larger than this value, the next highest pyramid level is
          displayed.
      pyramid_level_definition (String):
          The pyramid type used by the terrain dataset. This parameter is not used in
          ArcGIS 9.3 and beyond, as its purpose is to ensure backward-compatibility with
          scripts and models written using ArcGIS 9.2."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddTerrainPyramidLevel_3d(*gp_fixargs((in_terrain, pyramid_type, pyramid_level_definition), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AppendTerrainPoints_3d', None)
def AppendTerrainPoints(in_terrain=None, terrain_feature_class=None, in_point_features=None, polygon_features_or_extent=None):
    """AppendTerrainPoints(in_terrain, terrain_feature_class, in_point_features, {polygon_features_or_extent})

        Appends points to a point feature referenced by a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      terrain_feature_class (String):
          The feature class that contributes to the terrain dataset into which the points
          or multipoints will be added.This parameter only requires the name of the
          feature class and not its full
          path.
      in_point_features (Feature Layer):
          The feature class of points or multipoints to add as an additional data source
          for the terrain dataset.
      polygon_features_or_extent {Feature Layer / Extent}:
          Specify a polygon feature class or arcpy.Extent object to define the area where
          point features will be added. This parameter is empty by default, which results
          in all the points from the input feature class being loaded to the terrain
          feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AppendTerrainPoints_3d(*gp_fixargs((in_terrain, terrain_feature_class, in_point_features, polygon_features_or_extent), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildTerrain_3d', None)
def BuildTerrain(in_terrain=None, update_extent=None):
    """BuildTerrain(in_terrain, {update_extent})

        Performs tasks required for analyzing and displaying a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      update_extent {String}:
          Recalculates the data extent of a window-size-based terrain dataset when the
          data area has been reduced through editing.  It is not needed if the data extent
          has increased or if the terrain dataset is z-tolerance based. It will scan
          through all the terrain data to determine the new extent.

          * NO_UPDATE_EXTENT— The extent of the terrain dataset will not be recalculated.
          This is the default.

          * UPDATE_EXTENT— The extent of the terrain dataset will be recalculated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildTerrain_3d(*gp_fixargs((in_terrain, update_extent), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ChangeTerrainReferenceScale_3d', None)
def ChangeTerrainReferenceScale(in_terrain=None, old_refscale=None, new_refscale=None):
    """ChangeTerrainReferenceScale(in_terrain, old_refscale, new_refscale)

        Changes the reference scale associated with a terrain pyramid level.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      old_refscale (Long):
          The reference scale of an existing pyramid level.
      new_refscale (Long):
          The new reference scale for the pyramid level."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ChangeTerrainReferenceScale_3d(*gp_fixargs((in_terrain, old_refscale, new_refscale), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ChangeTerrainResolutionBounds_3d', None)
def ChangeTerrainResolutionBounds(in_terrain=None, feature_class=None, lower_pyramid_resolution=None, upper_pyramid_resolution=None, overview=None):
    """ChangeTerrainResolutionBounds(in_terrain, feature_class, {lower_pyramid_resolution}, {upper_pyramid_resolution}, {overview})

        Changes the pyramid levels at which a feature class will be enforced for a given
        terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      feature_class (String):
          The feature class referenced by the terrain that will have its pyramid-level
          resolutions modified.
      lower_pyramid_resolution {Double}:
          The new lower pyramid-level resolution for the chosen feature class.
      upper_pyramid_resolution {Double}:
          The new upper pyramid-level resolution for the chosen feature class.
      overview {Boolean}:
          Specifies whether the feature class will contribute to the overview of the
          terrain dataset.

          *  OVERVIEW — Enforces the feature class at the overview display of the terrain
          dataset. This is the default.

          * NO_OVERVIEW—Omits the feature class from the overview display of the terrain
          dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ChangeTerrainResolutionBounds_3d(*gp_fixargs((in_terrain, feature_class, lower_pyramid_resolution, upper_pyramid_resolution, overview), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateTerrain_3d', None)
def CreateTerrain(in_feature_dataset=None, out_terrain_name=None, average_point_spacing=None, max_overview_size=None, config_keyword=None, pyramid_type=None, windowsize_method=None, secondary_thinning_method=None, secondary_thinning_threshold=None):
    """CreateTerrain(in_feature_dataset, out_terrain_name, average_point_spacing, {max_overview_size}, {config_keyword}, {pyramid_type}, {windowsize_method}, {secondary_thinning_method}, {secondary_thinning_threshold})

        Creates a new terrain dataset.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          The feature dataset that will contain the terrain dataset.
      out_terrain_name (String):
          The name of the terrain dataset.
      average_point_spacing (Double):
          The average horizontal distance between the data points that will be used in
          modeling the terrain. Sensor based measurements, like photogrammetric, lidar,
          and sonar surveys, typically have a known spacing that should be used. The
          spacing should be expressed in the horizontal units of the feature dataset's
          coordinate system.
      max_overview_size {Long}:
          The terrain overview is akin to the image thumbnail concept. It is the coarsest
          representation of the terrain dataset, and the maximum size represents the upper
          limit of the number of measurement points that can be sampled to create the
          overview.
      config_keyword {String}:
          The configuration keyword for optimizing the terrain's storage in an enterprise
          database.
      pyramid_type {String}:
          The point thinning method used to construct the terrain pyramids.

          * WINDOWSIZE—Thinning is performed by selecting data points in the area defined
          by a given window size for each pyramid level using the criterion specified in
          the windowsize_method parameter.

          * ZTOLERANCE—Thinning is performed by specifying the vertical accuracy of each
          pyramid level relative to the full resolution of the data points.
      windowsize_method {String}:
          The criterion used for selecting points in the area defined by the window size.
          This parameter is only applicable when WINDOWSIZE is specified in the
          pyramid_type parameter.

          * ZMIN—The point with the smallest elevation value.

          * ZMAX—The point with the largest elevation value.

          * ZMEAN—The point with the elevation value closest to the average of all values.

          * ZMINMAX—The points with the smallest and largest elevation values.
      secondary_thinning_method {String}:
          Specifies additional thinning options to reduce the number of points used over
          flat areas when Window Size pyramids are being used. An area is considered flat
          if the heights of points in an area are within the value supplied for the
          Secondary Thinning Threshold parameter. Its effect is more evident at higher-
          resolution pyramid levels, since smaller areas are more likely to be flat than
          larger areas.

          * NONE—No secondary thinning will be performed. This is the default.

          * MILD—Works best to preserve linear discontinuities (for example, building
          sides and forest boundaries). It is recommended for lidar that includes both
          ground and nonground points. It will thin the fewest points.

          * MODERATE—Provides a good trade-off between performance and accuracy. It does
          not preserve as much detail as mild thinning but comes nearly as close while
          eliminating more points overall.

          * STRONG—Removes the most points but is less likely to preserve sharply
          delineated features. Its use should be limited to surfaces where slope tends to
          change gradually. For example, strong thinning would be efficient for bare-earth
          lidar and bathymetry.
      secondary_thinning_threshold {Double}:
          The vertical threshold used to activate secondary thinning with the WINDOWSIZE
          filter. The value should be set equal to or larger than the vertical accuracy of
          the data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateTerrain_3d(*gp_fixargs((in_feature_dataset, out_terrain_name, average_point_spacing, max_overview_size, config_keyword, pyramid_type, windowsize_method, secondary_thinning_method, secondary_thinning_threshold), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteTerrainPoints_3d', None)
def DeleteTerrainPoints(in_terrain=None, data_source=None, polygon_features_or_extent=None):
    """DeleteTerrainPoints(in_terrain, data_source;data_source..., polygon_features_or_extent)

        Deletes points within a specified area of interest from one or more features
        that participate in a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      data_source (String):
          One or more feature classes from which points will be removed.
      polygon_features_or_extent (Feature Layer / Extent):
          Specifies the area from which points will be removed. A polygon feature class or
          an extent can be used.If extent values are desired, use an arcpy.Extent object."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteTerrainPoints_3d(*gp_fixargs((in_terrain, data_source, polygon_features_or_extent), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveFeatureClassFromTerrain_3d', None)
def RemoveFeatureClassFromTerrain(in_terrain=None, feature_class=None):
    """RemoveFeatureClassFromTerrain(in_terrain, feature_class)

        Removes reference to a feature class participating in a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      feature_class (String):
          The feature class to be removed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveFeatureClassFromTerrain_3d(*gp_fixargs((in_terrain, feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveTerrainPyramidLevel_3d', None)
def RemoveTerrainPyramidLevel(in_terrain=None, pyramid_level_resolution=None):
    """RemoveTerrainPyramidLevel(in_terrain, pyramid_level_resolution)

        Removes a pyramid level from a terrain dataset.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      pyramid_level_resolution (Double):
          The pyramid level to be removed as specified by its resolution."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveTerrainPyramidLevel_3d(*gp_fixargs((in_terrain, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReplaceTerrainPoints_3d', None)
def ReplaceTerrainPoints(in_terrain=None, terrain_feature_class=None, in_point_features=None, polygon_features_or_extent=None):
    """ReplaceTerrainPoints(in_terrain, terrain_feature_class, in_point_features, {polygon_features_or_extent})

        Replaces points referenced by a terrain dataset with points from a specified
        feature class.

     INPUTS:
      in_terrain (Terrain Layer):
          The terrain dataset to process.
      terrain_feature_class (String):
          The terrain point features that will have its source data replaced.
      in_point_features (Feature Layer):
          The point or multipoint features that will replace the terrain point features.
      polygon_features_or_extent {Feature Layer / Extent}:
          An optional area of interest can be used to define the extent of the area in
          which the terrain points would be replaced."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReplaceTerrainPoints_3d(*gp_fixargs((in_terrain, terrain_feature_class, in_point_features, polygon_features_or_extent), True)))
        return retval
    except Exception, e:
        raise e


# Functional Surface toolset
@gptooldoc('AddSurfaceInformation_3d', None)
def AddSurfaceInformation(in_feature_class=None, in_surface=None, out_property=None, method=None, sample_distance=None, z_factor=None, pyramid_level_resolution=None, noise_filtering=None):
    """AddSurfaceInformation(in_feature_class, in_surface, out_property;out_property..., {method}, {sample_distance}, {z_factor}, {pyramid_level_resolution}, {noise_filtering})

        Attributes features with spatial information derived from a surface.

     INPUTS:
      in_feature_class (Feature Layer):
          The point, multipoint, polyline, or polygon features that define the locations
          for determining one or more surface properties.
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer):
          The LAS dataset, raster, terrain, or TIN surface used for interpolating
          z-values.
      out_property (String):
          The surface elevation property that will be added to the attribute table of the
          input feature class. The following list summarizes the available property
          keywords and their supported geometry types:

          * Z—Surface Z values interpolated for the XY location of each single-point
          feature.

          * Z_MIN—Lowest surface Z values in the area defined by the polygon, along the
          length of a line, or among the interpolated values for points in a multipoint
          record.

          * Z_MAX—Highest surface elevation in the area defined by the polygon, along the
          length of a line, or among the interpolated values for points in a multipoint
          record.

          * Z_MEAN—Average surface elevation of the area defined by the polygon, along the
          length of a line, or among the interpolated values for points in a multipoint
          record.

          * SURFACE_AREA—3D surface area for the region defined by each polygon.

          * SURFACE_LENGTH—3D distance of the line along the surface.

          * MIN_SLOPE—Slope value closest to zero along the line or within the area
          defined by the polygon.

          * MAX_SLOPE—Highest slope value along the line or within the area defined by the
          polygon.

          * AVG_SLOPE—Average slope value along the line or within the area defined by the
          polygon.
      method {String}:
          Interpolation method used in determining information about the surface. The
          available options depend on the data type of the input surface:

          * BILINEAR—An interpolation method exclusive to the raster surface which
          determines cell values from the four nearest cells. This is the only option
          available for a raster surface.

          * LINEAR— Default interpolation method for TIN, terrain, and LAS dataset.
          Obtains elevation from the plane defined by the triangle that contains the XY
          location of a query point.

          * NATURAL_NEIGHBORS— Obtains elevation by applying area-based weights to the
          natural neighbors of a query point.

          * CONFLATE_ZMIN— Obtains elevation from the smallest Z value found among the
          natural neighbors of a query point.

          * CONFLATE_ZMAX— Obtains elevation from the largest Z value found among the
          natural neighbors of a query point.

          * CONFLATE_NEAREST— Obtains elevation from the nearest value among the natural
          neighbors of a query point.

          * CONFLATE_CLOSEST_TO_MEAN — Obtains elevation from the Z value that is closest
          to the average of all the natural neighbors of a query point.
      sample_distance {Double}:
          The spacing at which z-values will be interpolated. By default, the raster cell
          size is used when the input surface is a raster, and the natural densification
          of the triangulated surface is used when the input is a terrain or TIN dataset.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.
      noise_filtering {String}:
          Excludes portions of the surface that are potentially characterized by
          anomalous measurements from contributing to slope calculations. Line features
          offer a length filter, whereas polygons provide an area filter. The value
          corresponding with either filtering option is evaluated in the linear units of
          the feature's coordinate system. Non-slope properties are not affected by this
          parameter.

          * NO_FILTER—No noise filter will be used to limit the line segments or surface
          triangles factored into the slope calculations. This is the default.

          * AREA <value>—Surface triangles with 3D areas less than the specified value
          will be excluded from contributing to slope calculations.

          * LENGTH <value>— Line segments whose 3D length after being interpolated on the
          surface is shorter than the specified value will be excluded from contributing
          to slope calculations."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddSurfaceInformation_3d(*gp_fixargs((in_feature_class, in_surface, out_property, method, sample_distance, z_factor, pyramid_level_resolution, noise_filtering), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('InterpolateShape_3d', None)
def InterpolateShape(in_surface=None, in_feature_class=None, out_feature_class=None, sample_distance=None, z_factor=None, method=None, vertices_only=None, pyramid_level_resolution=None):
    """InterpolateShape(in_surface, in_feature_class, out_feature_class, {sample_distance}, {z_factor}, {method}, {vertices_only}, {pyramid_level_resolution})

        Creates 3D features by interpolating z-values from a surface.

     INPUTS:
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer):
          The LAS dataset, raster, TIN, or terrain surface used for interpolating
          z-values.
      in_feature_class (Feature Layer):
          The input features to process.
      sample_distance {Double}:
          The spacing at which z-values will be interpolated. By default, this is a raster
          dataset's cell size or a triangulated surface's natural densification.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      method {String}:
          Interpolation method used to determine elevation values for the output
          features. The available options depend on the surface type being used:

          * BILINEAR—An interpolation method exclusive to the raster surface which
          determines cell values from the four nearest cells. This is the only option
          available for a raster surface.

          * LINEAR— Default interpolation method for TIN, terrain, and LAS dataset.
          Obtains elevation from the plane defined by the triangle that contains the XY
          location of a query point.

          * NATURAL_NEIGHBORS— Obtains elevation by applying area-based weights to the
          natural neighbors of a query point.

          * CONFLATE_ZMIN— Obtains elevation from the smallest Z value found among the
          natural neighbors of a query point.

          * CONFLATE_ZMAX— Obtains elevation from the largest Z value found among the
          natural neighbors of a query point.

          * CONFLATE_NEAREST— Obtains elevation from the nearest value among the natural
          neighbors of a query point.

          * CONFLATE_CLOSEST_TO_MEAN — Obtains elevation from the Z value that is closest
          to the average of all the natural neighbors of a query point.
      vertices_only {Boolean}:
          Specifies whether the interpolation will only occur along the vertices of an
          input feature, thereby ignoring the sample distance option.

          * DENSIFY—Interpolates using the sampling distance. This is the default.

          * VERTICES_ONLY—Interpolates along the vertices.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.InterpolateShape_3d(*gp_fixargs((in_surface, in_feature_class, out_feature_class, sample_distance, z_factor, method, vertices_only, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Intersect3DLineWithSurface_3d', None)
def Intersect3DLineWithSurface(in_line_features=None, in_surfaces=None, out_line_feature_class=None, out_point_feature_class=None):
    """Intersect3DLineWithSurface(in_line_features, in_surfaces;in_surfaces..., out_line_feature_class, {out_point_feature_class})

        Computes the geometric intersection of 3D line features and one or more
        surfaces to return the intersection as segmented line features and points.

     INPUTS:
      in_line_features (Feature Layer):
          Specify one or more input raster or TIN surfaces to construct the geometric
          intersections.
      in_surfaces (TIN Layer / Raster Layer / Mosaic Layer):
          The input 3D line features.

     OUTPUTS:
      out_line_feature_class (Feature Class):
          The output line feature class that will contain a copy of the input lines split
          at the points of intersection.
      out_point_feature_class {Feature Class}:
          The optional point feature class that will contain the points of intersection."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Intersect3DLineWithSurface_3d(*gp_fixargs((in_line_features, in_surfaces, out_line_feature_class, out_point_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('StackProfile_3d', None)
def StackProfile(in_line_features=None, profile_targets=None, out_table=None, out_graph=None):
    """StackProfile(in_line_features, profile_targets;profile_targets..., out_table, {out_graph})

        Creates a table and optional graph denoting the profile of line features over
        one or more multipatch, raster, TIN, or terrain surfaces.

     INPUTS:
      in_line_features (Feature Layer):
          The line features that will be profiled over the surface inputs.
      profile_targets (Feature Layer / TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer):
          The data being profiled, which can be comprised from any combination of
          multipatch features and surfaces models like raster, TIN, terrain, and LAS
          datasets.

     OUTPUTS:
      out_table (Table):
          The output table that will store the interpolated measurements for each
          profile.
      out_graph {Graph}:
          The name of the output graph that can be viewed in ArcMap, ArcScene, or
          ArcGlobe."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.StackProfile_3d(*gp_fixargs((in_line_features, profile_targets, out_table, out_graph), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SurfaceVolume_3d', None)
def SurfaceVolume(in_surface=None, out_text_file=None, reference_plane=None, base_z=None, z_factor=None, pyramid_level_resolution=None):
    """SurfaceVolume(in_surface, {out_text_file}, {reference_plane}, {base_z}, {z_factor}, {pyramid_level_resolution})

        Calculates the area and volume of the region between a surface and a reference
        plane.

     INPUTS:
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer):
          The raster, TIN, or terrain surface to process.
      reference_plane {String}:
          The direction from the reference plane for which to calculate the results.

          * ABOVE—Volume and area calculations will represent the region of space between
          the specified plane height and the portions of the surface that are above the
          plane. This is the default.

          * BELOW—Volume and area calculations will represent the region of space between
          the specified plane height and portions of the surface that are below the plane.
      base_z {Double}:
          The Z value of the plane that will be used to calculate area and volume.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_text_file {File}:
          A comma-delimited ASCII text file containing the area and volume calculations.
          If the file already exists, the new results will be appended to the file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SurfaceVolume_3d(*gp_fixargs((in_surface, out_text_file, reference_plane, base_z, z_factor, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e


# Raster Interpolation toolset
@gptooldoc('Idw_3d', None)
def Idw(in_point_features=None, z_field=None, out_raster=None, cell_size=None, power=None, search_radius=None, in_barrier_polyline_features=None):
    """Idw(in_point_features, z_field, out_raster, {cell_size}, {power}, {search_radius}, {in_barrier_polyline_features})

        Interpolates a raster surface from points using an inverse distance weighted
        (IDW) technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.
      power {Double}:
          The exponent of distance.Controls the significance of surrounding points on the
          interpolated value. A
          higher power results in less influence from distant points. It can be any real
          number greater than 0, but the most reasonable results will be obtained using
          values from 0.5 to 3. The default is 2.
      search_radius {Radius}:
          Defines which of the input points will be used to interpolate the value for each
          cell in the output raster.There are two ways to specify the searching
          neighborhood: Variable and Fixed.Variable uses a variable search radius in order
          to find a specified number of
          input sample points for the interpolation. Fixed uses a specified fixed distance
          within which all input points will be used. Variable is the default.The syntax
          for these parameters are:

          * Variable, number_of_points, maximum_distance, where

          * number_of_points—An integer value specifying the number of nearest input
          sample points to be used to perform interpolation. The default is 12 points.

          * maximum_distance—Specifies the distance, in map units, by which to limit the
          search for the nearest input sample points. The default value is the length of
          the extent's diagonal.


          * Fixed, distance, minimum_number_of_points , where

          * distance—Specifies the distance as a radius within which input sample points
          will be used to perform the interpolation. The value of the radius is expressed
          in map units. The default radius is five times the cell size of the output
          raster.

          * minimum_number_of_points—An integer defining the minimum number of points to
          be used for interpolation. The default value is 0.  If the required number of
          points is not found within the specified distance, the
          search distance will be increased until the specified minimum number of points
          is found.  When the search radius needs to be increased it is done so until the
          minimum_number_of_points fall within that radius, or the extent of the radius
          crosses the lower (southern) and/or upper (northern) extent of the output
          raster. NoData is assigned to all locations that do not satisfy the above
          condition.
      in_barrier_polyline_features {Composite Geodataset}:
          Polyline features to be used as a break or limit in searching for the input
          sample points.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Idw_3d(*gp_fixargs((in_point_features, z_field, out_raster, cell_size, power, search_radius, in_barrier_polyline_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Kriging_3d', None)
def Kriging(in_point_features=None, z_field=None, out_surface_raster=None, semiVariogram_props=None, cell_size=None, search_radius=None, out_variance_prediction_raster=None):
    """Kriging(in_point_features, z_field, out_surface_raster, semiVariogram_props, {cell_size}, {search_radius}, {out_variance_prediction_raster})

        Interpolates a raster surface from points using kriging.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.
      semiVariogram_props (SemiVariogram):
          The Semivariogram model to be used.There are two models for kriging: Ordinary
          and Universal. The Ordinary model has
          five types of semivariograms available. The Universal model has two types of
          semivariograms available. Each semivariogram has several optional parameters
          that can also be set.

          * Ordinary model semivariograms

          * Spherical—Spherical semivariogram model. This is the default.

          * Circular—Circular semivariogram model.

          * Exponential—Exponential semivariogram model.

          * Gaussian—Gaussian (or normal distribution) semivariogram model.

          * Linear—Linear semivariogram model with a sill.


          * Universal model semivariograms

          * LinearDrift—Universal Kriging with linear drift.

          * QuadraticDrift—Universal Kriging with quadratic drift.


          * After the semivariogram model is defined, the remaining parameters are common
          between Ordinary and Universal kriging. These include the following:

          * Lag size—The default is the output raster cell size.

          * MajorRange—Represents a distance beyond which there is little or no
          correlation.

          * PartialSill—The difference between the nugget and the sill.

          * Nugget—Represents the error and variation at spatial scales too fine to
          detect. The nugget effect is seen as a discontinuity at the origin.

          The form of the semivariogram is a text
          string:"{semivariogramType},{lagSize},{majorRange},{partialSill},{nugget}"For
          example:"Circular, 2000, 2.6, 542"
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.
      search_radius {Radius}:
          Defines which of the input points will be used to interpolate the value for each
          cell in the output raster.There are two ways to specify the searching
          neighborhood: Variable and Fixed.Variable uses a variable search radius in order
          to find a specified number of
          input sample points for the interpolation. Fixed uses a specified fixed distance
          within which all input points will be used. Variable is the default.The syntax
          for these parameters are:

          * Variable, number_of_points, maximum_distance, where

          * number_of_points—An integer value specifying the number of nearest input
          sample points to be used to perform interpolation. The default is 12 points.

          * maximum_distance—Specifies the distance, in map units, by which to limit the
          search for the nearest input sample points. The default value is the length of
          the extent's diagonal.


          * Fixed, distance, minimum_number_of_points , where

          * distance—Specifies the distance as a radius within which input sample points
          will be used to perform the interpolation. The value of the radius is expressed
          in map units. The default radius is five times the cell size of the output
          raster.

          * minimum_number_of_points—An integer defining the minimum number of points to
          be used for interpolation. The default value is 0.  If the required number of
          points is not found within the specified distance, the
          search distance will be increased until the specified minimum number of points
          is found.  When the search radius needs to be increased it is done so until the
          minimum_number_of_points fall within that radius, or the extent of the radius
          crosses the lower (southern) and/or upper (northern) extent of the output
          raster. NoData is assigned to all locations that do not satisfy the above
          condition.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster.
      out_variance_prediction_raster {Raster Dataset}:
          Optional output raster where each cell contains the predicted semi-variance
          values for that location."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Kriging_3d(*gp_fixargs((in_point_features, z_field, out_surface_raster, semiVariogram_props, cell_size, search_radius, out_variance_prediction_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('NaturalNeighbor_3d', None)
def NaturalNeighbor(in_point_features=None, z_field=None, out_raster=None, cell_size=None):
    """NaturalNeighbor(in_point_features, z_field, out_raster, {cell_size})

        Interpolates a raster surface from points using a natural neighbor technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.NaturalNeighbor_3d(*gp_fixargs((in_point_features, z_field, out_raster, cell_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Spline_3d', None)
def Spline(in_point_features=None, z_field=None, out_raster=None, cell_size=None, spline_type=None, weight=None, number_points=None):
    """Spline(in_point_features, z_field, out_raster, {cell_size}, {spline_type}, {weight}, {number_points})

        Interpolates a raster surface from points using a two-dimensional minimum
        curvature spline technique.The resulting smooth surface passes exactly through
        the input points.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.
      spline_type {String}:
          The type of spline to be used.

          * REGULARIZED — Yields a smooth surface and smooth first derivatives.

          * TENSION — Tunes the stiffness of the interpolant according to the character of
          the modeled phenomenon.
      weight {Double}:
          Parameter influencing the character of the surface interpolation.When the
          REGULARIZED option is used, it defines the weight of the third
          derivatives of the surface in the curvature minimization expression. If the
          TENSION option is used, it defines the weight of tension.The default weight is
          0.1.
      number_points {Long}:
          The number of points per region used for local approximation.The default is 12.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Spline_3d(*gp_fixargs((in_point_features, z_field, out_raster, cell_size, spline_type, weight, number_points), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SplineWithBarriers_3d', None)
def SplineWithBarriers(Input_point_features=None, Z_value_field=None, Input_barrier_features=None, Output_cell_size=None, Output_raster=None, Smoothing_Factor=None):
    """SplineWithBarriers(Input_point_features, Z_value_field, {Input_barrier_features}, {Output_cell_size}, Output_raster, {Smoothing_Factor})

        Interpolates a raster surface, using barriers, from points using a minimum
        curvature spline technique. The barriers are entered as either polygon or
        polyline features.

     INPUTS:
      Input_point_features (Feature Layer):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      Z_value_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.
      Input_barrier_features {Feature Layer}:
          The optional input barrier features to constrain the interpolation.
      Output_cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.If a value of 0 is
          entered, the shorter of the width or the height of the extent
          of the input point features in the input spatial reference, divided by 250, will
          be used as the cell size.
      Smoothing_Factor {Double}:
          The parameter that influences the smoothing of the output surface.No smoothing
          is applied when the value is zero and the maximum amount of
          smoothing is applied when the factor equals 1.The default is 0.0.

     OUTPUTS:
      Output_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SplineWithBarriers_3d(*gp_fixargs((Input_point_features, Z_value_field, Input_barrier_features, Output_cell_size, Output_raster, Smoothing_Factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TopoToRaster_3d', None)
def TopoToRaster(in_topo_features=None, out_surface_raster=None, cell_size=None, extent=None, Margin=None, minimum_z_value=None, maximum_z_value=None, enforce=None, data_type=None, maximum_iterations=None, roughness_penalty=None, discrete_error_factor=None, vertical_standard_error=None, tolerance_1=None, tolerance_2=None, out_stream_features=None, out_sink_features=None, out_diagnostic_file=None, out_parameter_file=None, profile_penalty=None, out_residual_feature=None, out_stream_cliff_error_feature=None, out_contour_error_feature=None):
    """TopoToRaster(in_topo_features, out_surface_raster, {cell_size}, {extent}, {Margin}, {minimum_z_value}, {maximum_z_value}, {enforce}, {data_type}, {maximum_iterations}, {roughness_penalty}, {discrete_error_factor}, {vertical_standard_error}, {tolerance_1}, {tolerance_2}, {out_stream_features}, {out_sink_features}, {out_diagnostic_file}, {out_parameter_file}, {profile_penalty}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

        Interpolates a hydrologically correct raster surface from point, line, and
        polygon data.

     INPUTS:
      in_topo_features (Topo features):
          The input features containing the z-values to be interpolated into a surface
          raster.Each feature input can have a field specified that contains the z-values
          and one
          of six types specified.

          * <Feature Layer>—The input feature dataset.

          * {Field}—The name of the field that stores the attributes, where appropriate.

          * {Type} —The type of input feature dataset.
          There are six types of accepted inputs:

          * POINTELEVATION—A point feature class representing surface elevations. The
          Field stores the elevations of the points.

          * CONTOUR—A line feature class that represents elevation contours. The Field
          stores the elevations of the contour lines.

          * STREAM—A line feature class of stream locations. All arcs must be oriented to
          point downstream. The feature class should only contain single arc streams.
          There is no Field option for this input type.

          * SINK—A point feature class that represents known topographic depressions. Topo
          to Raster will not attempt to remove from the analysis any points explicitly
          identified as sinks. The Field used should be one that stores the elevation of
          the legitimate sink. If NONE is selected, only the location of the sink is used.

          * BOUNDARY—A feature class containing a single polygon that represents the outer
          boundary of the output raster. Cells in the output raster outside this boundary
          will be NoData. This option can be used for clipping out water areas along
          coastlines before making the final output raster. There is no Field option for
          this input type.

          * LAKE—A polygon feature class that specifies the location of lakes. All output
          raster cells within a lake will be assigned to the minimum elevation value of
          all cells along the shoreline. There is no Field option for this input type.

          * CLIFF—A line feature class of the cliffs. The cliff line features must be
          oriented so that the left-hand side of the line is on the low side of the cliff
          and the right-hand side is the high side of the cliff. There is no Field option
          for this input type.

          * COAST—A polygon feature class containing the outline of a coastal area. Cells
          in the final output raster that lie outside these polygons are set to a value
          that is less than the user-specified minimum height limit. There is no Field
          option for this input type.

          * EXCLUSION—A polygon feature class of the areas in which the input data should
          be ignored. These polygons permit removal of elevation data from the
          interpolation process. This is typically used to remove elevation data
          associated with dam walls and bridges. This enables interpolation of the
          underlying valley with connected drainage structure. There is no Field option
          for this input type.
          Multiple input feature datasets should be enclosed by double quotes. The
          individual inputs are separated by a semicolon, with a space between each
          component.  See the first Code Sample below for an example.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.
      extent {Extent}:
          Extent for the output raster dataset.Interpolation will occur out to the x and y
          limits, and cells outside that
          extent will be NoData. For best interpolation results along the edges of the
          output raster, the x and y limits should be smaller than the extent of the input
          data by at least 10 cells on each side.

          * X_Minimum—The default is the smallest x coordinate of all inputs.

          * Y_Minimum—The default is the smallest y coordinate of all inputs.

          * X_Maximum—The default is the largest x coordinate of all inputs.

          * Y_Maximum—The default is the largest y coordinate of all inputs.
          The default extent is the largest of all extents of the input feature data.
      Margin {Long}:
          Distance in cells to interpolate beyond the specified output extent and
          boundary.The value must be greater than or equal to 0 (zero). The default value
          is 20.If the {extent} and Boundary feature dataset are the same as the limit of
          the
          input data (the default), values interpolated along the edge of the DEM will not
          match well with adjacent DEM data. This is because they have been interpolated
          using one-half as much data as the points inside the raster, which are
          surrounded on all sides by input data. The {margin} option allows input data
          beyond these limits to be used in the interpolation.
      minimum_z_value {Double}:
          The minimum z-value to be used in the interpolation.The default is 20 percent
          below the smallest of all the input values.
      maximum_z_value {Double}:
          The maximum z-value to be used in the interpolation.The default is 20 percent
          above the largest of all input values.
      enforce {String}:
          The type of drainage enforcement to apply.The drainage enforcement option can be
          set to attempt to remove all sinks or
          depressions so a hydrologically correct DEM can be created. If sink points have
          been explicitly identified in the input feature data, these depressions will not
          be filled.

          * ENFORCE— The algorithm will attempt to remove all sinks it encounters, whether
          they are real or spurious. This is the default.

          * NO_ENFORCE— No sinks will be filled.

          * ENFORCE_WITH_SINK — Points identified as sinks in Input feature data represent
          known topographic depressions and will not be altered. Any sink not identified
          in input feature data is considered spurious, and the algorithm will attempt to
          fill it.Having more than 8,000 spurious sinks causes the tool to fail.
      data_type {String}:
          The dominant elevation data type of the input feature data.

          * CONTOUR — The dominant type of input data will be elevation contours. This is
          the default.

          * SPOT — The dominant type of input will be point.
          Specifying the relevant selection optimizes the search method used during the
          generation of streams and ridges.
      maximum_iterations {Long}:
          The maximum number of interpolation iterations.The number of iterations must be
          greater than zero. A default of 20 is normally
          adequate for both contour and line data.A value of 30 will clear fewer sinks.
          Rarely, higher values (45–50) may be
          useful to clear more sinks or to set more ridges and streams. Iteration ceases
          for each grid resolution when the maximum number of iterations has been reached.
      roughness_penalty {Double}:
          The integrated squared second derivative as a measure of roughness.The roughness
          penalty must be zero or greater. If the primary input data type is
          CONTOUR, the default is zero. If the primary data type is SPOT, the default is
          0.5. Larger values are not normally recommended.
      discrete_error_factor {Double}:
          The discrete error factor is used to adjust the amount of smoothing when
          converting the input data to a raster.The value must be greater than zero. The
          normal range of adjustment is 0.25 to
          4, and the default is 1. A smaller value results in less data smoothing; a
          larger value causes greater smoothing.
      vertical_standard_error {Double}:
          The amount of random error in the z-values of the input data.The value must be
          zero or greater. The default is zero.The vertical standard error may be set to a
          small positive value if the data has
          significant random (non-systematic) vertical errors with uniform variance. In
          this case, set the vertical standard error to the standard deviation of these
          errors. For most elevation datasets, the vertical error should be set to zero,
          but it may be set to a small positive value to stabilize convergence when
          rasterizing point data with stream line data.
      tolerance_1 {Double}:
          This tolerance reflects the accuracy and density of the elevation points in
          relation to surface drainage.For point datasets, set the tolerance to the
          standard error of the data heights.
          For contour datasets, use one-half the average contour interval.The value must
          be zero or greater. The default is 2.5 if the data type is
          CONTOUR and zero if the data type is SPOT.
      tolerance_2 {Double}:
          This tolerance prevents drainage clearance through unrealistically high
          barriers.The value must be greater than zero. The default is 100 if the data
          type is
          CONTOUR and 200 if the data type is SPOT.
      profile_penalty {Double}:
          The profile curvature roughness penalty is a locally adaptive penalty that can
          be used to partly replace total curvature.It can yield good results with high-
          quality contour data but can lead to
          instability in convergence with poor data. Set to 0.0 for no profile curvature
          (the default), set to 0.5 for moderate profile curvature, and set to 0.8 for
          maximum profile curvature. Values larger than 0.8 are not recommended and should
          not be used.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster.
      out_stream_features {Feature Class}:
          The output line feature class of stream polyline features and ridge line
          features.The line features are created at the beginning of the interpolation
          process. It
          provides the general morphology of the surface for interpolation. It can be used
          to verify correct drainage and morphology by comparing known stream and ridge
          data. The polyline features are coded as follows:1. Input stream line not over
          cliff.2. Input stream line over cliff (waterfall).3. Drainage enforcement
          clearing a spurious sink.4. Stream line determined from contour corner.5. Ridge
          line determined from contour corner.6. Code not used.7. Data stream line side
          conditions.8. Code not used.9. Line indicating large elevation data clearance.
      out_sink_features {Feature Class}:
          The output point feature class of the remaining sink point features.These are
          the sinks that were not specified in the sink input feature data and
          were not cleared during drainage enforcement. Adjusting the values of the
          tolerances, tolerance_1 and tolerance_2, can reduce the number of remaining
          sinks. Remaining sinks often indicate errors in the input data that the drainage
          enforcement algorithm could not resolve. This can be an efficient way of
          detecting subtle elevation errors.
      out_diagnostic_file {File}:
          The output diagnostic file listing all inputs and parameters used and the number
          of sinks cleared at each resolution and iteration.
      out_parameter_file {File}:
          The output parameter file listing all inputs and parameters used, which can be
          used with Topo to Raster by File to run the interpolation again.
      out_residual_feature {Feature Class}:
          The output point feature class of all the large elevation residuals as scaled
          by the local discretisation error. All the scaled residuals larger than 10
          should be inspected for possible errors
          in input elevation and stream data. Large-scaled residuals indicate conflicts
          between input elevation data and streamline data. These may also be associated
          with poor automatic drainage enforcements. These conflicts can be remedied by
          providing additional streamline and/or point elevation data after first checking
          and correcting errors in existing input data. Large unscaled residuals usually
          indicate input elevation errors.
      out_stream_cliff_error_feature {Feature Class}:
          The output point feature class of locations where possible stream and cliff
          errors occur. The locations where the streams have closed loops, distributaries,
          and streams
          over cliffs can be identified from the point feature class. Cliffs with
          neighboring cells that are inconsistent with the high and low sides of the cliff
          are also indicated. This can be a good indicator of cliffs with incorrect
          direction. Points are coded as follows:1. True circuit in data streamline
          network.2. Circuit in stream network as encoded on the out raster.3. Circuit in
          stream network via connecting lakes.4. Distributaries point.5. Stream over a
          cliff (waterfall).6. Points indicating multiple stream outflows from lakes.7.
          Code not used.8. Points beside cliffs with heights inconsistent with cliff
          direction.9. Code not used.10. Circular distributary removed.11. Distributary
          with no inflowing stream.12. Rasterized distributary in output cell different to
          where the data stream
          line distributary occurs.13. Error processing side conditions—an indicator of
          very complex streamline
          data.
      out_contour_error_feature {Feature Class}:
          The output point feature class of possible errors pertaining to the input
          contour data. Contours with bias in height exceeding five times the standard
          deviation of the
          contour values as represented on the output raster are reported to this feature
          class. Contours that join other contours with a different elevation are flagged
          in this feature class by the code 1; this is a sure sign of a contour label
          error."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TopoToRaster_3d(*gp_fixargs((in_topo_features, out_surface_raster, cell_size, extent, Margin, minimum_z_value, maximum_z_value, enforce, data_type, maximum_iterations, roughness_penalty, discrete_error_factor, vertical_standard_error, tolerance_1, tolerance_2, out_stream_features, out_sink_features, out_diagnostic_file, out_parameter_file, profile_penalty, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TopoToRasterByFile_3d', None)
def TopoToRasterByFile(in_parameter_file=None, out_surface_raster=None, out_stream_features=None, out_sink_features=None, out_residual_feature=None, out_stream_cliff_error_feature=None, out_contour_error_feature=None):
    """TopoToRasterByFile(in_parameter_file, out_surface_raster, {out_stream_features}, {out_sink_features}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

        Interpolates a hydrologically correct raster surface from point, line, and
        polygon data using parameters specified in a file.

     INPUTS:
      in_parameter_file (File):
          The input ASCII text file containing the inputs and parameters to use for the
          interpolation.The file is typically created from a previous run of Topo to
          Raster with the
          optional output parameter file specified.In order to test the outcome of
          changing the parameters, it is easier to make
          edits to this file and rerun the interpolation than to correctly issue the Topo
          to Raster tool each time.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster.
      out_stream_features {Feature Class}:
          Output feature class of stream polyline features. The polyline features are
          coded as follows:1. Input stream line not over cliff.2. Input stream line over
          cliff (waterfall).3. Drainage enforcement clearing a spurious sink.4. Stream
          line determined from contour corner.5. Ridge line determined from contour
          corner.6. Code not used.7. Data stream line side conditions.8. Code not used.9.
          Line indicating large elevation data clearance.
      out_sink_features {Feature Class}:
          Output feature class of remaining sink point features.
      out_residual_feature {Feature Class}:
          The output point feature class of all the large elevation residuals as scaled
          by the local discretisation error. All the scaled residuals larger than 10
          should be inspected for possible errors
          in input elevation and stream data. Large-scaled residuals indicate conflicts
          between input elevation data and streamline data. These may also be associated
          with poor automatic drainage enforcements. These conflicts can be remedied by
          providing additional streamline and/or point elevation data after first checking
          and correcting errors in existing input data. Large unscaled residuals usually
          indicate input elevation errors.
      out_stream_cliff_error_feature {Feature Class}:
          The output point feature class of locations where possible stream and cliff
          errors occur. The locations where the streams have closed loops, distributaries,
          and streams
          over cliffs can be identified from the point feature class. Cliffs with
          neighboring cells that are inconsistent with the high and low sides of the cliff
          are also indicated. This can be a good indicator of cliffs with incorrect
          direction. Points are coded as follows:1. True circuit in data streamline
          network.2. Circuit in stream network as encoded on the out raster.3. Circuit in
          stream network via connecting lakes.4. Distributaries point.5. Stream over a
          cliff (waterfall).6. Points indicating multiple stream outflows from lakes.7.
          Code not used.8. Points beside cliffs with heights inconsistent with cliff
          direction.9. Code not used.10. Circular distributary removed.11. Distributary
          with no inflowing stream.12. Rasterized distributary in output cell different to
          where the data stream
          line distributary occurs.13. Error processing side conditions—an indicator of
          very complex streamline
          data.
      out_contour_error_feature {Feature Class}:
          The output point feature class of possible errors pertaining to the input
          contour data. Contours with bias in height exceeding five times the standard
          deviation of the
          contour values as represented on the output raster are reported to this feature
          class. Contours that join other contours with a different elevation are flagged
          in this feature class by the code 1; this is a sure sign of a contour label
          error."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TopoToRasterByFile_3d(*gp_fixargs((in_parameter_file, out_surface_raster, out_stream_features, out_sink_features, out_residual_feature, out_stream_cliff_error_feature, out_contour_error_feature), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Trend_3d', None)
def Trend(in_point_features=None, z_field=None, out_raster=None, cell_size=None, order=None, regression_type=None, out_rms_file=None):
    """Trend(in_point_features, z_field, out_raster, {cell_size}, {order}, {regression_type}, {out_rms_file})

        Interpolates a raster surface from points using a trend technique.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated into a
          surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This can be a
          numeric field or the Shape field if the input point features
          contain z-values.If the regression type is Logistic, the values in the field can
          only be 0 or 1.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This will be the value
          in the environment if it is explicitly set; otherwise, it
          is the shorter of the width or the height of the extent of the input point
          features, in the input spatial reference, divided by 250.
      order {Long}:
          The order of the polynomial.This must be an integer between 1 and 12. A value of
          1 will fit a flat plane to
          the points, and a higher value will fit a more complex surface. The default is
          1.
      regression_type {String}:
          The type of regression to be performed.

          * LINEAR — Polynomial regression is performed to fit a least-squares surface to
          the set of input points. This is applicable for continuous types of data.

          * LOGISTIC — Logistic trend surface analysis is performed. It generates a
          continuous probability surface for binary, or dichotomous, types of data.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point raster.
      out_rms_file {File}:
          File name for the output text file that contains information about the RMS error
          and the Chi-Square of the interpolation.The extension must be .txt."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Trend_3d(*gp_fixargs((in_point_features, z_field, out_raster, cell_size, order, regression_type, out_rms_file), True)))
        return retval
    except Exception, e:
        raise e


# Raster Math toolset
@gptooldoc('Divide_3d', None)
def Divide(in_raster_or_constant1=None, in_raster_or_constant2=None, out_raster=None):
    """Divide(in_raster_or_constant1, in_raster_or_constant2, out_raster)

        Divides the values of two rasters on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input whose values will be divided by the second input.A number can be used
          as an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input whose values the first input are to be divided by.A number can be used
          as an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the quotient of the first input raster
          (dividend) divided by
          the second input (divisor)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Divide_3d(*gp_fixargs((in_raster_or_constant1, in_raster_or_constant2, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Float_3d', None)
def Float(in_raster_or_constant=None, out_raster=None):
    """Float(in_raster_or_constant, out_raster)

        Converts each cell value of a raster into a floating-point representation.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster to be converted to floating point. In order to use a number as
          an input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the floating-point representation of the
          input values."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Float_3d(*gp_fixargs((in_raster_or_constant, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Int_3d', None)
def Int(in_raster_or_constant=None, out_raster=None):
    """Int(in_raster_or_constant, out_raster)

        Converts each cell value of a raster to an integer by truncation.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input raster to be converted to integer. In order to use a number as an
          input for this parameter, the cell size and
          extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the input values converted to integers by
          truncation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Int_3d(*gp_fixargs((in_raster_or_constant, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Minus_3d', None)
def Minus(in_raster_or_constant1=None, in_raster_or_constant2=None, out_raster=None):
    """Minus(in_raster_or_constant1, in_raster_or_constant2, out_raster)

        Subtracts the value of the second input raster from the value of the first input
        raster on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input from which to subtract the values in the second input.A number can be
          used as an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input values to subtract from the values in the first input.A number can be
          used as an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the result of subtracting the second input
          from the first."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Minus_3d(*gp_fixargs((in_raster_or_constant1, in_raster_or_constant2, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Plus_3d', None)
def Plus(in_raster_or_constant1=None, in_raster_or_constant2=None, out_raster=None):
    """Plus(in_raster_or_constant1, in_raster_or_constant2, out_raster)

        Adds (sums) the values of two rasters on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input whose values will be added to.A number can be used as an input for
          this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input whose values will be added to the first input.A number can be used as
          an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the sum of the first input added to the
          second."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Plus_3d(*gp_fixargs((in_raster_or_constant1, in_raster_or_constant2, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Times_3d', None)
def Times(in_raster_or_constant1=None, in_raster_or_constant2=None, out_raster=None):
    """Times(in_raster_or_constant1, in_raster_or_constant2, out_raster)

        Multiplies the values of two rasters on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant1 (Composite Geodataset):
          The input containing the values to be multiplied.A number can be used as an
          input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constant2 (Composite Geodataset):
          The input containing the values by which the first input will be multiplied.A
          number can be used as an input for this parameter, provided a raster is
          specified for the other parameter. To be able to specify a number for both
          inputs, the cell size and extent must first be set in the environment.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The cell values are the product of the first input multiplied
          by the second."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Times_3d(*gp_fixargs((in_raster_or_constant1, in_raster_or_constant2, out_raster), True)))
        return retval
    except Exception, e:
        raise e


# Raster Reclass toolset
@gptooldoc('Lookup_3d', None)
def Lookup(in_raster=None, lookup_field=None, out_raster=None):
    """Lookup(in_raster, lookup_field, out_raster)

        Creates a new raster by looking up values found in another field in the table of
        the input raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster that contains a field from which to create a new raster.
      lookup_field (Field):
          Field containing the desired values for the new raster.It can be a numeric or
          string type.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster whose values are determined by the specified field of the
          input raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Lookup_3d(*gp_fixargs((in_raster, lookup_field, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReclassByASCIIFile_3d', None)
def ReclassByASCIIFile(in_raster=None, in_remap_file=None, out_raster=None, missing_values=None):
    """ReclassByASCIIFile(in_raster, in_remap_file, out_raster, {missing_values})

        Reclassifies (or changes) the values of the input cells of a raster using an
        ASCII remap file.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      in_remap_file (File):
          ASCII remap file defining the single values or ranges to be reclassified and the
          values they will become.Allowed extensions for the ASCII remap files are .rmp,
          .txt, and .asc.
      missing_values {Boolean}:
          Denotes whether missing values in the reclass file retain their value or get
          mapped to NoData.

          * DATA — Signifies that if any cell location on the input raster contains a
          value that is not present or reclassed in the remap file, the value should
          remain intact and be written for that location to the output raster. This is the
          default.

          * NODATA — Signifies that if any cell location on the input raster contains a
          value that is not present or reclassed in the remap file, the value will be
          reclassed to NoData for that location on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReclassByASCIIFile_3d(*gp_fixargs((in_raster, in_remap_file, out_raster, missing_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReclassByTable_3d', None)
def ReclassByTable(in_raster=None, in_remap_table=None, from_value_field=None, to_value_field=None, output_value_field=None, out_raster=None, missing_values=None):
    """ReclassByTable(in_raster, in_remap_table, from_value_field, to_value_field, output_value_field, out_raster, {missing_values})

        Reclassifies (or changes) the values of the input cells of a raster using a
        remap table.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      in_remap_table (Table View):
          Table holding fields defining value ranges to be reclassified and the values
          they will become.
      from_value_field (Field):
          Field holding the beginning value for each value range to be reclassified.This
          is a numeric field of the input remap table.
      to_value_field (Field):
          Field holding the ending value for each value range to be reclassified.This is a
          numeric field of the input remap table.
      output_value_field (Field):
          Field holding the integer values to which each range should be changed.This is
          an integer field of the input remap table.
      missing_values {Boolean}:
          Denotes whether missing values in the reclass table retain their value or get
          mapped to NoData.

          * DATA —Signifies that if any cell location on the input raster contains a value
          not present or reclassed in a remap table, the value should remain intact and be
          written for that location to the output raster. This is the default.

          * NODATA — Signifies that if any cell location on the input raster contains a
          value not present or reclassed in a remap table, the value will be reclassed to
          NoData for that location on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReclassByTable_3d(*gp_fixargs((in_raster, in_remap_table, from_value_field, to_value_field, output_value_field, out_raster, missing_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Reclassify_3d', None)
def Reclassify(in_raster=None, reclass_field=None, remap=None, out_raster=None, missing_values=None):
    """Reclassify(in_raster, reclass_field, remap, out_raster, {missing_values})

        Reclassifies (or changes) the values in a raster.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      reclass_field (Field):
          Field denoting the values that will be reclassified.
      remap (Remap):
          A remap list that defines how the values will be reclassified.The remap list is
          composed of three components: From, To, and New values. Each
          row in the remap list is separated by a semicolon, and the three components are
          separated by spaces. For example:"0 5 1;5.01 7.5 2;7.5 10 3"
      missing_values {Boolean}:
          Denotes whether missing values in the reclass table retain their value or get
          mapped to NoData.

          * DATA —Signifies that if any cell location on the input raster contains a value
          that is not present or reclassed in a remap table, the value should remain
          intact and be written for that location to the output raster. This is the
          default.

          * NODATA —  Signifies that if any cell location on the input raster contains a
          value that is not present or reclassed in a remap table, the value will be
          reclassed to NoData for that location on the output raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Reclassify_3d(*gp_fixargs((in_raster, reclass_field, remap, out_raster, missing_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Slice_3d', None)
def Slice(in_raster=None, out_raster=None, number_zones=None, slice_type=None, base_output_zone=None):
    """Slice(in_raster, out_raster, number_zones, {slice_type}, {base_output_zone})

        Slices or reclassifies the range of values of the input cells into zones of
        equal interval, equal area, or by natural breaks.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster to be reclassified.
      number_zones (Long):
          The number of zones to reclassify the input raster into.When the slice method is
          EQUAL_AREA, the output raster will have the defined
          number of zones, with a similar number of cells in each.When EQUAL_INTERVAL is
          used, the output raster will have the defined number of
          zones, each containing equal value ranges on the output raster.When
          NATURAL_BREAKS is used, the output raster will have the defined number of
          zones, with the number of cells in each determined by the class breaks.
      slice_type {String}:
          The manner in which to slice the values in the input raster.

          * EQUAL_INTERVAL — Determines the range of the input values and divides the
          range into the specified number of output zones. Each zone on the sliced output
          raster has the potential of having input cell values that have the same range
          from the extremes. This is the default.

          * EQUAL_AREA — Specifies that the input values will be divided into the
          specified number of output zones, with each zone having a similar number of
          cells. Each zone will represent a similar amount of area.

          * NATURAL_BREAKS — Specifies that the classes will be based on natural groupings
          inherent in the data. Break points are identified by choosing the class breaks
          that best group similar values and that maximize the differences between
          classes. The cell values are divided into classes whose boundaries are set when
          there are relatively big jumps in the data values.
      base_output_zone {Long}:
          Defines the lowest zone value on the output raster dataset.The default value is
          1.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output reclassified raster.The output will always be of integer type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Slice_3d(*gp_fixargs((in_raster, out_raster, number_zones, slice_type, base_output_zone), True)))
        return retval
    except Exception, e:
        raise e


# Raster Surface toolset
@gptooldoc('Aspect_3d', None)
def Aspect(in_raster=None, out_raster=None):
    """Aspect(in_raster, out_raster)

        Derives aspect from a raster surface. The aspect identifies the downslope
        direction of the maximum rate of change in value from each cell to its
        neighbors.Aspect can be thought of as the slope direction. The values of the
        output raster
        will be the compass direction of the aspect.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output aspect raster.It will be floating point type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Aspect_3d(*gp_fixargs((in_raster, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Contour_3d', None)
def Contour(in_raster=None, out_polyline_features=None, contour_interval=None, base_contour=None, z_factor=None):
    """Contour(in_raster, out_polyline_features, contour_interval, {base_contour}, {z_factor})

        Creates a line feature class of contours (isolines) from a raster surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      contour_interval (Double):
          The interval, or distance, between contour lines.This can be any positive
          number.
      base_contour {Double}:
          The base contour value.Contours are generated above and below this value as
          needed to cover the entire
          value range of the input raster. The default is zero.
      z_factor {Double}:
          The unit conversion factor used when generating contours. The default value is
          1.The contour lines are generated based on the z-values in the input raster,
          which
          are often measured in units of meters or feet. With the default value of 1, the
          contours will be in the same units as the z-values of the input raster. To
          create contours in a different unit than that of the z-values, set an
          appropriate value for the z-factor. Note that it is not necessary to have the
          ground x,y and surface z-units be consistent for this tool. For example, if the
          elevation values in your input raster are in feet, but you
          want the contours to be generated based on units of meters, set the z-factor to
          0.3048 (since 1 ft = 0.3048 m).For another example, consider an input raster in
          WGS_84 geographic coordinates
          and elevation units of meters for which you want to generate contour lines every
          100 feet with a base of 50 feet (so the contours will be 50 ft, 150 ft, 250 ft,
          and so on). To do this, set the contour_interval to 100, the base_contour to 50,
          and the z_factor to 3.2808 (since 1 m = 3.2808 ft).

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output contour polyline features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Contour_3d(*gp_fixargs((in_raster, out_polyline_features, contour_interval, base_contour, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ContourList_3d', None)
def ContourList(in_raster=None, out_polyline_features=None, contour_values=None):
    """ContourList(in_raster, out_polyline_features, contour_values;contour_values...)

        Creates a feature class of selected contour values from a raster surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      contour_values (Double):
          List of z-values for which to create contours.

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output contour polyline features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ContourList_3d(*gp_fixargs((in_raster, out_polyline_features, contour_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ContourWithBarriers_3d', None)
def ContourWithBarriers(in_raster=None, out_contour_feature_class=None, in_barrier_features=None, in_contour_type=None, in_contour_values_file=None, explicit_only=None, in_base_contour=None, in_contour_interval=None, in_indexed_contour_interval=None, in_contour_list=None, in_z_factor=None):
    """ContourWithBarriers(in_raster, out_contour_feature_class, {in_barrier_features}, {in_contour_type}, {in_contour_values_file}, {explicit_only}, {in_base_contour}, {in_contour_interval}, {in_indexed_contour_interval}, {in_contour_list;in_contour_list...}, {in_z_factor})

        Creates contours from a raster surface. The inclusion of barrier features allows
        you to independently generate contours on either side of a barrier.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The input surface raster.
      in_barrier_features {Feature Layer}:
          The input barrier features.The features can be polyline or polygon type.
      in_contour_type {String}:
          The type of contour to create.

          * POLYLINES — The contour or isoline representation of the input raster.

          * POLYGONS — Closed polygons representing the contours.
          The current version of this tool only supports polyline output. If the polygon
          output option is used, it will be ignored and polyline output will be created.
      in_contour_values_file {File}:
          The base contour, contour interval, indexed contour interval, and explicit
          contour values can also be specified via a text file.
      explicit_only {Boolean}:
          Only explicit contour values are used. Base contour, contour interval, and
          indexed contour intervals are not specified.

          * NO_EXPLICIT_VALUES_ONLY — The default, contour interval must be specified.

          * EXPLICIT_VALUES_ONLY — Only explicit contour values are specified.
      in_base_contour {Double}:
          The base contour value.Contours are generated above and below this value as
          needed to cover the entire
          value range of the input raster. The default is zero.
      in_contour_interval {Double}:
          The interval, or distance, between contour lines.This can be any positive
          number.
      in_indexed_contour_interval {Double}:
          Contours will also be generated for this interval and will be flagged
          accordingly in the output feature class.
      in_contour_list {Double}:
          Explicit values at which to create contours.
      in_z_factor {Double}:
          The unit conversion factor used when generating contours. The default value is
          1.The contour lines are generated based on the z-values in the input raster,
          which
          are often measured in units of meters or feet. With the default value of 1, the
          contours will be in the same units as the z-values of the input raster. To
          create contours in a different unit than that of the z-values, set an
          appropriate value for the z-factor. Note that it is not necessary to have the
          ground x,y and surface z-units be consistent for this tool. For example, if the
          elevation values in your input raster are in feet, but you
          want the contours to be generated based on units of meters, set the z-factor to
          0.3048 (since 1 ft = 0.3048 m).

     OUTPUTS:
      out_contour_feature_class (Feature Class):
          The output contour features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ContourWithBarriers_3d(*gp_fixargs((in_raster, out_contour_feature_class, in_barrier_features, in_contour_type, in_contour_values_file, explicit_only, in_base_contour, in_contour_interval, in_indexed_contour_interval, in_contour_list, in_z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Curvature_3d', None)
def Curvature(in_raster=None, out_curvature_raster=None, z_factor=None, out_profile_curve_raster=None, out_plan_curve_raster=None):
    """Curvature(in_raster, out_curvature_raster, {z_factor}, {out_profile_curve_raster}, {out_plan_curve_raster})

        Calculates the curvature of a raster surface, optionally including profile and
        plan curvature.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).

     OUTPUTS:
      out_curvature_raster (Raster Dataset):
          The output curvature raster.It will be floating point type.
      out_profile_curve_raster {Raster Dataset}:
          Output profile curve raster dataset.This is the curvature of the surface in the
          direction of slope.It will be floating point type.
      out_plan_curve_raster {Raster Dataset}:
          Output plan curve raster dataset.This is the curvature of the surface
          perpendicular to the slope direction.It will be floating point type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Curvature_3d(*gp_fixargs((in_raster, out_curvature_raster, z_factor, out_profile_curve_raster, out_plan_curve_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CutFill_3d', None)
def CutFill(in_before_surface=None, in_after_surface=None, out_raster=None, z_factor=None):
    """CutFill(in_before_surface, in_after_surface, out_raster, {z_factor})

        Calculates the volume change between two surfaces. This is typically used for
        cut and fill operations.

     INPUTS:
      in_before_surface (Composite Geodataset):
          The input representing the surface before the cut or fill operation.
      in_after_surface (Composite Geodataset):
          The input representing the surface after the cut or fill operation.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster defining regions of cut and of fill.The values show the
          locations and amounts where the surface has been added to or
          removed from."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CutFill_3d(*gp_fixargs((in_before_surface, in_after_surface, out_raster, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('HillShade_3d', None)
def HillShade(in_raster=None, out_raster=None, azimuth=None, altitude=None, model_shadows=None, z_factor=None):
    """HillShade(in_raster, out_raster, {azimuth}, {altitude}, {model_shadows}, {z_factor})

        Creates a shaded relief from a surface raster by considering the illumination
        source angle and shadows.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      azimuth {Double}:
          Azimuth angle of the light source.The azimuth is expressed in positive degrees
          from 0 to 360, measured clockwise
          from north.The default is 315 degrees.
      altitude {Double}:
          Altitude angle of the light source above the horizon.The altitude is expressed
          in positive degrees, with 0 degrees at the horizon and
          90 degrees directly overhead.The default is 45 degrees.
      model_shadows {Boolean}:
          Type of shaded relief to be generated.

          * NO_SHADOWS—The output raster only considers local illumination angles; the
          effects of shadows are not considered.The output values can range from 0 to 255,
          with 0 representing the darkest areas, and 255 the brightest. This is the
          default.

          * SHADOWS — The output shaded raster considers both local illumination angles
          and shadows.The output values range from 0 to 255, with 0 representing the
          shadow areas, and 255 the brightest.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output hillshade raster.The hillshade raster has an integer value range of 0
          to 255."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HillShade_3d(*gp_fixargs((in_raster, out_raster, azimuth, altitude, model_shadows, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Slope_3d', None)
def Slope(in_raster=None, out_raster=None, output_measurement=None, z_factor=None):
    """Slope(in_raster, out_raster, {output_measurement}, {z_factor})

        Identifies the slope (gradient, or rate of maximum change in z-value) from each
        cell of a raster surface.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      output_measurement {String}:
          Determines the measurement units (degrees or percentages) of the output slope
          data.

          * DEGREE — The inclination of slope will be calculated in degrees.

          * PERCENT_RISE — Keyword to output the percent rise, also referred to as the
          percent slope.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).

     OUTPUTS:
      out_raster (Raster Dataset):
          The output slope raster.It will be floating point type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Slope_3d(*gp_fixargs((in_raster, out_raster, output_measurement, z_factor), True)))
        return retval
    except Exception, e:
        raise e


# Triangulated Surface toolset
@gptooldoc('DecimateTinNodes_3d', None)
def DecimateTinNodes(in_tin=None, out_tin=None, method=None, copy_breaklines=None):
    """DecimateTinNodes(in_tin, out_tin, method, {copy_breaklines})

        Creates a triangulated irregular network (TIN) dataset using a subset of nodes
        from a source TIN.

     INPUTS:
      in_tin (TIN Layer):
          The TIN dataset to process.
      method (Decimate):
          Specifies the decimation method for selecting a subset of nodes from the input
          TIN.

          * ZTOLERANCE <z_tolerance_value> <max_node_value>— Generalizes TIN within a
          specified vertical accuracy. An optional node limit can also be specified. This
          parameter is supplied as a string, so "ZTOLERANCE 0.5 5500" would represent a
          Z-tolerance value of 0.5 and a max node value of 5,500.

          * COUNT <max_node_value>—Generalizes TIN by constraining its size to a specified
          node limit. This parameter is supplied as a string, so "COUNT 5500" would
          represent a maximum node count of 5,500.
      copy_breaklines {Boolean}:
          Indicates whether breaklines from the input TIN are copied over to the output.

          * BREAKLINES—Breaklines will be copied.

          * NO_BREAKLINES—Breaklines will not be copied. This is the default.

     OUTPUTS:
      out_tin (TIN):
          The TIN dataset that will be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DecimateTinNodes_3d(*gp_fixargs((in_tin, out_tin, method, copy_breaklines), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExtrudeBetween_3d', None)
def ExtrudeBetween(in_tin1=None, in_tin2=None, in_feature_class=None, out_feature_class=None):
    """ExtrudeBetween(in_tin1, in_tin2, in_feature_class, out_feature_class)

        Creates 3D features by extruding each input feature between two triangulated
        irregular network (TIN) datasets.

     INPUTS:
      in_tin1 (TIN Layer):
          The first input TIN.
      in_tin2 (TIN Layer):
          The second input TIN.
      in_feature_class (Feature Layer):
          The features that will be extruded between the TINs.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output that will store the extruded features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExtrudeBetween_3d(*gp_fixargs((in_tin1, in_tin2, in_feature_class, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('InterpolatePolyToPatch_3d', None)
def InterpolatePolyToPatch(in_surface=None, in_feature_class=None, out_feature_class=None, max_strip_size=None, z_factor=None, area_field=None, surface_area_field=None, pyramid_level_resolution=None):
    """InterpolatePolyToPatch(in_surface, in_feature_class, out_feature_class, {max_strip_size}, {z_factor}, {area_field}, {surface_area_field}, {pyramid_level_resolution})

        Creates surface-conforming multipatch features by draping polygon feature class
        over a surface.Each polygon feature has its boundary profiled along the surface.
        Heights are
        obtained using linear interpolation by sampling at each input vertex and
        wherever the boundary line intersects surface triangle edges and nodes. This
        natural densification captures the full definition of the linear surface using a
        minimal number of samples. Then, all nodes that fall within the polygon are
        extracted. The nodes are retriangulated in a new memory-based TIN, and the 3D
        polygon boundary is enforced as a clip polygon. The triangles of this new TIN
        are then extracted in a series of strips that are used to define a multipatch-
        based feature.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer):
          The input triangulated irregular network (TIN) or terrain dataset surface.
      in_feature_class (Feature Layer):
          The input polygon feature.
      max_strip_size {Long}:
          Controls the maximum number of points used to create an individual triangle
          strip. Note that each multipatch is usually composed of multiple strips. The
          default value is 1,024.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      area_field {String}:
          The name of the output field containing the planimetric, or 2D, area of the
          resulting multipatches.
      surface_area_field {String}:
          The name of the output field containing the 3D area of the resulting
          multipatches. This area takes the surface undulations into consideration and is
          always larger than the planimetric area unless the surface is flat, in which
          case, the two are equal.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output multipatch feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.InterpolatePolyToPatch_3d(*gp_fixargs((in_surface, in_feature_class, out_feature_class, max_strip_size, z_factor, area_field, surface_area_field, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LocateOutliers_3d', None)
def LocateOutliers(in_surface=None, out_feature_class=None, apply_hard_limit=None, absolute_z_min=None, absolute_z_max=None, apply_comparison_filter=None, z_tolerance=None, slope_tolerance=None, exceed_tolerance_ratio=None, outlier_cap=None):
    """LocateOutliers(in_surface, out_feature_class, {apply_hard_limit}, {absolute_z_min}, {absolute_z_max}, {apply_comparison_filter}, {z_tolerance}, {slope_tolerance}, {exceed_tolerance_ratio}, {outlier_cap})

        Identifies anomalous elevation measurements from terrain, TIN, or LAS datasets
        that exceed a defined range of elevation values or have slope characteristics
        that are inconsistent with the surrounding surface.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer / LAS Dataset Layer):
          The terrain, TIN, or LAS dataset that will be analyzed.
      apply_hard_limit {Boolean}:
          Specifies use of absolute Z minimum and maximum to find outliers.

          * APPLY_HARD_LIMIT—Use the absolute Z minimum and maximum to find outliers.

          * NO_APPLY_HARD_LIMIT—Do not use the absolute Z minimum and maximum to find
          outliers. This is the default.
      absolute_z_min {Double}:
          If hard limits are applied, then any point with an elevation below this value
          will be considered as being an outlier. The default is 0.
      absolute_z_max {Double}:
          If hard limits are applied, then any point with an elevation above this value
          will be considered as being an outlier.  The default is 0.
      apply_comparison_filter {Boolean}:
          The comparison filter consists of three parameters for determining outliers
          (z_tolerance, slope_tolerance, and exceed_tolerance_ratio).

          * APPLY_COMPARISON_FILTER—Use the three comparison parameters (Z tolerance,
          slope tolerance, and exceed tolerance ratio) in assessing points. This is the
          default.

          * NO_APPLY_COMPARISON_FILTER—Do not use the three comparison parameters (Z
          tolerance, slope tolerance, and exceed tolerance ratio) in assessing points.
      z_tolerance {Double}:
          Used to compare Z values of neighboring points if the comparison filter is
          applied.  The default is 0.
      slope_tolerance {Double}:
          The threshold of slope variance between consecutive points that would be used
          to identify outlier points. Slope is expressed as a percentage, with the default
          being 150.
      exceed_tolerance_ratio {Double}:
          Defines the criteria for determining each outlier point as a function of the
          ratio of points in its natural neighborhood that must exceed the specified
          comparison filters. For example, the default value of 0.5 means at least half of
          the points surrounding the query point must exceed the comparison filters for
          the query point to be flagged as an outlier. A value of 0.7 means at least 70
          percent of the neighbor points must exceed the tolerances.
      outlier_cap {Long}:
          The maximum number of outlier points that can be written to the output. Once
          this value is reached, no further outliers are sought.  The default is 2,500.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LocateOutliers_3d(*gp_fixargs((in_surface, out_feature_class, apply_hard_limit, absolute_z_min, absolute_z_max, apply_comparison_filter, z_tolerance, slope_tolerance, exceed_tolerance_ratio, outlier_cap), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PolygonVolume_3d', None)
def PolygonVolume(in_surface=None, in_feature_class=None, in_height_field=None, reference_plane=None, out_volume_field=None, surface_area_field=None, pyramid_level_resolution=None):
    """PolygonVolume(in_surface, in_feature_class, in_height_field, {reference_plane}, {out_volume_field}, {surface_area_field}, {pyramid_level_resolution})

        Calculates the volume and surface area between a polygon and terrain or TIN
        surface.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer):
          The terrain or TIN surface that will be evaluated.
      in_feature_class (Feature Layer):
          The polygon features that determine the surface regions to process.
      in_height_field (String):
          The field in the polygon's attribute table that defines the height of the
          reference plane used in determining volumetric calculations.
      reference_plane {String}:
          Determines how volume and surface area are calculated.

          * ABOVE—Volume and surface area are calculated above the reference plane height
          of the polygons.

          * BELOW—Volume and surface area are calculated below the reference plane height
          of the polygons. This is the default.
      out_volume_field {String}:
          Specifies the name of the field that will contain volumetric calculations. The
          default is Volume.
      surface_area_field {String}:
          Specifies the name of the field that will contain the surface area calculations.
          The default is SArea.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PolygonVolume_3d(*gp_fixargs((in_surface, in_feature_class, in_height_field, reference_plane, out_volume_field, surface_area_field, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SurfaceAspect_3d', None)
def SurfaceAspect(in_surface=None, out_feature_class=None, class_breaks_table=None, aspect_field=None, pyramid_level_resolution=None):
    """SurfaceAspect(in_surface, out_feature_class, {class_breaks_table}, {aspect_field}, {pyramid_level_resolution})

        Creates polygon features that represent aspect measurements derived from a TIN,
        terrain, or LAS dataset surface.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer / LAS Dataset Layer):
          The TIN, terrain, or LAS dataset surface to process.
      class_breaks_table {Table}:
          A table containing the classification breaks that will be used to define the
          aspect ranges in the output feature class.
      aspect_field {String}:
          The field containing aspect code values.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SurfaceAspect_3d(*gp_fixargs((in_surface, out_feature_class, class_breaks_table, aspect_field, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SurfaceContour_3d', None)
def SurfaceContour(in_surface=None, out_feature_class=None, interval=None, base_contour=None, contour_field=None, contour_field_precision=None, index_interval=None, index_interval_field=None, z_factor=None, pyramid_level_resolution=None):
    """SurfaceContour(in_surface, out_feature_class, interval, {base_contour}, {contour_field}, {contour_field_precision}, {index_interval}, {index_interval_field}, {z_factor}, {pyramid_level_resolution})

        Creates contour lines derived from a terrain, TIN, or LAS dataset surface.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer / LAS Dataset Layer):
          The TIN, terrain, or LAS dataset surface to process.
      interval (Double):
          The interval between the contours.
      base_contour {Double}:
          Defines the starting Z value from which the contour interval is either added or
          subtracted to delineate contours. The default value is 0.0.
      contour_field {String}:
          The field that stores the contour value associated with each line in the output
          feature class.
      contour_field_precision {Long}:
          The precision of the contour field. Zero specifies an integer, and the numbers
          1–9 indicate how many decimal places the field will contain. By default, the
          field will be an integer (0).
      index_interval {Double}:
          Index contours are commonly used as a cartographic aid for assisting in the
          visualization of contour lines. The index interval is typically five times
          larger than the contour interval. Use of this parameter adds an integer field
          defined by the index_interval_field to the attribute table of the output feature
          class, where a value of 1 denotes the index contours.
      index_interval_field {String}:
          The name of the field used to identify index contours. This will only be used if
          the index_interval is defined. By default, the field name is Index.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SurfaceContour_3d(*gp_fixargs((in_surface, out_feature_class, interval, base_contour, contour_field, contour_field_precision, index_interval, index_interval_field, z_factor, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SurfaceDifference_3d', None)
def SurfaceDifference(in_surface=None, in_reference_surface=None, out_feature_class=None, pyramid_level_resolution=None, reference_pyramid_level_resolution=None, out_raster=None, raster_cell_size=None, out_tin_folder=None, out_tin_basename=None):
    """SurfaceDifference(in_surface, in_reference_surface, out_feature_class, {pyramid_level_resolution}, {reference_pyramid_level_resolution}, {out_raster}, {raster_cell_size}, {out_tin_folder}, {out_tin_basename})

        Calculates the volumetric difference between two surface models stored as either
        a triangulated irregular networks (TIN) or terrain dataset.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer):
          The input terrain or TIN dataset.
      in_reference_surface (TIN Layer / Terrain Layer):
          The reference terrain or TIN dataset.
      pyramid_level_resolution {Double}:
          The pyramid-level resolution of the input terrain dataset. The default is 0, or
          full resolution.
      reference_pyramid_level_resolution {Double}:
          The pyramid-level resolution of the reference terrain dataset. The default is 0,
          or full resolution.
      raster_cell_size {Double}:
          The output difference raster dataset. The raster will be converted from the
          integrated difference TIN using a linear interpolation method.
      out_tin_folder {Folder}:
          The folder location to write the TIN or TINs.
      out_tin_basename {String}:
          The base name given to each output TIN surface. If one TIN dataset is not
          sufficient to represent the data, multiple TINs will be created with the same
          base name.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing contiguous triangles and triangle parts that
          have the same classification grouped into polygons. The volume enclosed by each
          region of difference is listed in the attribute table.
      out_raster {Raster Dataset}:
          The cell size of the output raster dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SurfaceDifference_3d(*gp_fixargs((in_surface, in_reference_surface, out_feature_class, pyramid_level_resolution, reference_pyramid_level_resolution, out_raster, raster_cell_size, out_tin_folder, out_tin_basename), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SurfaceSlope_3d', None)
def SurfaceSlope(in_surface=None, out_feature_class=None, units=None, class_breaks_table=None, slope_field=None, z_factor=None, pyramid_level_resolution=None):
    """SurfaceSlope(in_surface, out_feature_class, {units}, {class_breaks_table}, {slope_field}, {z_factor}, {pyramid_level_resolution})

        Creates polygon features that represent ranges of slope values for triangulated
        surfaces.

     INPUTS:
      in_surface (TIN Layer / Terrain Layer / LAS Dataset Layer):
          The TIN, terrain, or LAS dataset whose slope measurements will be written to
          the output polygon feature.
      units {String}:
          The units of measure to be used in calculating slope.

          * PERCENT—Slope is expressed as a percentage value. This is the default.

          * DEGREE—Slope is expressed as the angle of inclination from a horizontal plane.
      class_breaks_table {Table}:
          A table containing classification breaks that will be used to group the output
          features. The first column of this table will indicate the break point, whereas
          the second will provide the classification code.
      slope_field {String}:
          The field containing slope values.
      z_factor {Double}:
          The factor by which Z values will be multiplied. This is typically used to
          convert Z linear units to match XY linear units. The default is 1, which leaves
          elevation values unchanged.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be produced by this tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SurfaceSlope_3d(*gp_fixargs((in_surface, out_feature_class, units, class_breaks_table, slope_field, z_factor, pyramid_level_resolution), True)))
        return retval
    except Exception, e:
        raise e


# Visibility toolset
@gptooldoc('ConstructSightLines_3d', None)
def ConstructSightLines(in_observer_points=None, in_target_features=None, out_line_feature_class=None, observer_height_field=None, target_height_field=None, join_field=None, sample_distance=None, output_the_direction=None):
    """ConstructSightLines(in_observer_points, in_target_features, out_line_feature_class, {observer_height_field}, {target_height_field}, {join_field}, {sample_distance}, {output_the_direction})

        Creates line features that represent sight lines from one or more observer
        points to features in a target feature class.

     INPUTS:
      in_observer_points (Feature Layer):
          The single-point features that represent observer points. Multipoint features
          are not supported.
      in_target_features (Feature Layer):
          The target features (points, multipoints, lines, and polygons).
      observer_height_field {String}:
          The source of the height values for the observer points obtained from its
          attribute table.A default Observer Height Field field is selected from among the
          options listed
          below by order of priority. If multiple fields exist, and the desired field does
          not have a higher priority in the default field selection, the desired field
          will need to be specified.

          * <None>—No Z values will be assigned to the resulting sight line features.

          *  Shape.Z

          * Spot

          *  Z

          *  Z_Value

          * Height

          *  Elev

          *  Elevation

          *  Contour
      target_height_field {String}:
          The height field for the target.A default Target Height Field field is selected
          from among the options listed
          below by order of priority. If multiple fields exist, and the desired field does
          not have a higher priority in the default field selection, the desired field
          will need to be specified.

          * <None>—No Z values will be assigned to the resulting sight line features.

          *  Shape.Z

          * Spot

          *  Z

          *  Z_Value

          * Height

          *  Elev

          *  Elevation

          *  Contour
      join_field {String}:
          The join field is used to match observers to specific targets.
      sample_distance {Double}:
          The distance between samples when the target is either a line or polygon
          feature class.  The Sampling Distance units are interpreted in the XY units of
          the output feature class.
      output_the_direction {Boolean}:
          Adds direction attributes to the output sight lines. Two additional fields will
          be added and populated to indicate direction: AZIMUTH and VERT_ANGLE (vertical
          angle).

          * NOT_OUTPUT_THE_DIRECTION — No direction attributes will be added to the output
          sight lines. This is the default.

          * OUTPUT_THE_DIRECTION— Two additional fields will be added and populated to
          indicate direction: AZIMUTH and VERT_ANGLE (vertical angle).

     OUTPUTS:
      out_line_feature_class (Feature Class):
          The output feature class containing the sight lines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConstructSightLines_3d(*gp_fixargs((in_observer_points, in_target_features, out_line_feature_class, observer_height_field, target_height_field, join_field, sample_distance, output_the_direction), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Intervisibility_3d', None)
def Intervisibility(sight_lines=None, obstructions=None, visible_field=None):
    """Intervisibility(sight_lines, obstructions;obstructions..., {visible_field})

        Determines the visibility of sight lines through potential obstructions.  The
        potential obstructions can be any combination of rasters, TINs, multipatches,
        and extruded polygons or lines.

     INPUTS:
      sight_lines (Feature Layer):
          The 3D sight lines.
      obstructions (Feature Layer / TIN Layer / Raster Layer / Mosaic Layer):
          One or more feature classes and/or surfaces that may obstruct the sight lines.
      visible_field {String}:
          Name of the field that will store the visibility results. A resulting value of
          0 indicates that the sight line's start and end points are not visible to one
          another.  A value of 1 indicates that the sight line's start and end points are
          visible to one another. The default field name is VISIBLE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Intervisibility_3d(*gp_fixargs((sight_lines, obstructions, visible_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LineOfSight_3d', None)
def LineOfSight(in_surface=None, in_line_feature_class=None, out_los_feature_class=None, out_obstruction_feature_class=None, use_curvature=None, use_refraction=None, refraction_factor=None, pyramid_level_resolution=None, in_features=None):
    """LineOfSight(in_surface, in_line_feature_class, out_los_feature_class, {out_obstruction_feature_class}, {use_curvature}, {use_refraction}, {refraction_factor}, {pyramid_level_resolution}, {in_features})

        Determines the visibility of sight lines over obstructions consisting of a
        surface and an optional multipatch dataset.

     INPUTS:
      in_surface (TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer):
          The LAS dataset, raster, TIN, or terrain surface used in determining visibility.
      in_line_feature_class (Feature Layer):
          The line features whose first vertex defines the observation point and last
          vertex identifies the target location. Height of the observation and target
          locations are obtained from the z-values of 3D features and interpolated from
          the surface for 2D features. 2D lines also have a default offset of 1 added to
          their elevation to raise the
          points above the surface. If the feature has an OffsetA field, its value will be
          added to the height of the observation point. If the OffsetB field is present,
          its value will be added to the height of the target position.
      use_curvature {Boolean}:
          Indicates whether the earth's curvature should be taken into consideration for
          the line-of-sight analysis.  For this option to be enabled, the surface needs to
          have a defined spatial reference in projected coordinates with defined z-units.

          * CURVATURE—The earth's curvature will be taken into consideration.

          * NO_CURVATURE—The earth's curvature will not be taken into consideration. This
          is the default.
      use_refraction {Boolean}:
          Indicates whether atmospheric refraction should be taken into consideration when
          generating a line of sight from a functional surface. This option does not apply
          if multipatch features are used.

          * REFRACTION—Atmospheric refraction will be taken into consideration.

          * NO_REFRACTION—Atmospheric refraction will not be taken into consideration.
          This is the default.
      refraction_factor {Double}:
          Provides a value to be used in the refraction factor. The default refraction
          factor is 0.13.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.
      in_features {Feature Layer}:
          A multipatch feature that may define additional obstructing elements, such as
          buildings. Refraction options are not honored for this input.

     OUTPUTS:
      out_los_feature_class (Feature Class):
          The output line feature class along which visibility has been determined. Two
          attribute fields are created. VisCode indicates visibility along the line, 1
          being visible and 2 not visible. TarIsVis indicates the target visibility, 0
          being not visible and 1 being visible.
      out_obstruction_feature_class {Feature Class}:
          An optional point feature class identifying the location of the first
          obstruction on the observer's sight line to its target."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LineOfSight_3d(*gp_fixargs((in_surface, in_line_feature_class, out_los_feature_class, out_obstruction_feature_class, use_curvature, use_refraction, refraction_factor, pyramid_level_resolution, in_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ObserverPoints_3d', None)
def ObserverPoints(in_raster=None, in_observer_point_features=None, out_raster=None, z_factor=None, curvature_correction=None, refractivity_coefficient=None, out_agl_raster=None):
    """ObserverPoints(in_raster, in_observer_point_features, out_raster, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})

        Identifies which observer points are visible from each raster surface location.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      in_observer_point_features (Composite Geodataset):
          The point feature class that identifies the observer locations.The maximum
          number of points allowed is 16.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).
      curvature_correction {Boolean}:
          Allows correction for the earth's curvature.

          * FLAT_EARTH — No curvature correction will be applied. This is the default.

          * CURVED_EARTH — Curvature correction will be applied.
      refractivity_coefficient {Double}:
          Coefficient of the refraction of visible light in air.The default value is 0.13.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output identifies exactly which observer points are
          visible from each raster
          surface location.
      out_agl_raster {Raster Dataset}:
          The output above ground level (AGL) raster.The AGL result is a raster where each
          cell value is the minimum height that must
          be added to an otherwise nonvisible cell to make it visible by at least one
          observer.Cells that were already visible will have a value of 0 in this output
          raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ObserverPoints_3d(*gp_fixargs((in_raster, in_observer_point_features, out_raster, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Skyline_3d', None)
def Skyline(in_observer_point_features=None, out_feature_class=None, in_surface=None, virtual_surface_radius=None, virtual_surface_elevation=None, in_features=None, feature_lod=None, from_azimuth_value_or_field=None, to_azimuth_value_or_field=None, azimuth_increment_value_or_field=None, max_horizon_radius=None, segment_skyline=None, scale_to_percent=None, scale_according_to=None, scale_method=None, use_curvature=None, use_refraction=None, refraction_factor=None, pyramid_level_resolution=None, create_silhouettes=None):
    """Skyline(in_observer_point_features, out_feature_class, {in_surface}, {virtual_surface_radius}, {virtual_surface_elevation}, {in_features;in_features...}, {feature_lod}, {from_azimuth_value_or_field}, {to_azimuth_value_or_field}, {azimuth_increment_value_or_field}, {max_horizon_radius}, {segment_skyline}, {scale_to_percent}, {scale_according_to}, {scale_method}, {use_curvature}, {use_refraction}, {refraction_factor}, {pyramid_level_resolution}, {create_silhouettes})

        Generates a line or multipatch feature class containing the results from a
        skyline or silhouette analysis.

     INPUTS:
      in_observer_point_features (Feature Layer):
          The 3D points representing observers. Each feature will have its own output.
      in_surface {TIN Layer / Raster Layer / Mosaic Layer / Terrain Layer / LAS Dataset Layer}:
          The topographic surface that will be used to define the horizon. If no surface
          is provided, then a virtual surface will be employed using the
          virtual_surface_radius and virtual_surface_elevation parameters.
      virtual_surface_radius {Linear unit}:
          The radius of the virtual surface that will be used to define the horizon when
          a topographic surface is not provided. The default is 1,000 meters.The following
          units are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * MILLIMETERS

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS
      virtual_surface_elevation {Linear unit}:
          The elevation of the virtual surface for defining the horizon in lieu of an
          actual surface. It is ignored if an actual surface is provided. The default is
          0.The following units are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * MILLIMETERS

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS
      in_features {Feature Layer}:
          The features used in determining the skyline. If no features are specified, then
          the skyline will consist solely of the horizon line as defined by the
          topographic or virtual surface.
      feature_lod {String}:
          The level of detail at which each feature should be examined in the skyline
          analysis.

          * FULL_DETAIL—Every edge within the feature is considered in the skyline
          analysis (only edges of triangles and exterior rings are considered). This time
          intensive operation is the most precise, and is also the default option.

          * CONVEX_FOOTPRINT—The skyline analysis will use the upper perimeter of the
          convex hull of each feature's footprint extruded to the elevation of the highest
          vertex within the feature.

          * ENVELOPE— The skyline analysis will use the perimeter of the 3-dimensional
          feature envelope. This is the fastest technique.
      from_azimuth_value_or_field {Double / Field}:
          The azimuth, in degrees, from which the skyline analysis should be started. The
          analysis starts from the observer point and goes to the right, from the From
          Azimuth until the To Azimuth is reached. Must be greater than minus 360 and less
          than 360. The default is 0.
      to_azimuth_value_or_field {Double / Field}:
          The direction, in degrees, at which the skyline analysis should be completed.
          The analysis starts from the observer point and goes to the right, from the From
          Azimuth until the To Azimuth is reached. Must be no more than 360 greater than
          the From Azimuth. The default is 360.
      azimuth_increment_value_or_field {Double / Field}:
          The angular interval, in degrees, at which the horizon should be evaluated while
          conducting the skyline analysis between the From Azimuth and the To Azimuth.
          Must be no greater than the To Azimuth minus the From Azimuth. The default is 1.
      max_horizon_radius {Linear unit}:
          The maximum distance for which a horizon should be sought from the observer
          location. A value of zero indicates that there should be no limit imposed. The
          default is 0.The following units are supported:

          * UNKNOWN

          * INCHES

          * FEET

          * YARDS

          * MILES

          * MILLIMETERS

          * CENTIMETERS

          * DECIMETERS

          * METERS

          * KILOMETERS
      segment_skyline {Boolean}:
          Determines whether the resulting skyline will have one feature for each observer
          point, or if each observer's skyline will be segmented by the unique elements
          that contribute to the skyline.If silhouettes are being generated, then this
          parameter will indicate whether
          divergent rays should be used; for sun shadows, this should generally be
          NO_SEGMENT_SKYLINE

          * NO_SEGMENT_SKYLINE—Each skyline feature will represent one observer. This is
          the default.

          * SEGMENT_SKYLINE—Each observer's skyline will be segmented by the unique
          elements that contribute to the skyline.
      scale_to_percent {Double}:
          Indicates to what percent of the original vertical angle (angle above the
          horizon, or angle of elevation) or elevation each skyline vertex should be
          placed. If either 0 or 100 is entered, then no scaling will occur. The default
          is 100.
      scale_according_to {String}:
          The values according to which the scaling should be determined.

          * VERTICAL_ANGLE—Scaling is done by considering the vertical angle of each
          vertex relative to the observer point. This is the default.

          * ELEVATION—Scaling is done by considering the elevation of each vertex relative
          to the observer point.
      scale_method {String}:
          The vertex to be used to calculate against.

          * SKYLINE_MAXIMUM—Vertices will be scaled relative to the vertical angle (or the
          elevation) of the vertex with the highest vertical angle (or elevation). This is
          the default.

          * EACH_VERTEX—Vertices will be scaled relative to the original vertical angle
          (or elevation) of each vertex.
      use_curvature {Boolean}:
          Indicates whether the earth's curvature should be taken into consideration when
          generating the ridgeline from a functional surface.

          * CURVATURE—The earth's curvature will be taken into consideration.

          * NO_CURVATURE—The earth's curvature will not be taken into consideration. This
          is the default.
      use_refraction {Boolean}:
          Indicates whether atmospheric refraction will be applied when generating the
          ridgeline from a functional surface.

          * NO_REFRACTION— Atmospheric refraction will not be taken into consideration.
          This is the default.

          * REFRACTION—Atmospheric refraction will be taken into consideration.
      refraction_factor {Double}:
          The refraction coefficient to be used if atmospheric refraction is being
          considered. The default is 0.13.
      pyramid_level_resolution {Double}:
          The z-tolerance or window-size resolution of the terrain pyramid level that will
          be used by this tool. The default is 0, or full resolution.
      create_silhouettes {Boolean}:
          Specifies whether output features will represent skylines or silhouettes.

          * NO_CREATE_SILHOUETTES—The resulting polyline features will represent the
          skyline. This is the default.

          * CREATE_SILHOUETTES—The resulting multipatch features will represent
          silhouettes.

     OUTPUTS:
      out_feature_class (Feature Class):
          The 3D features that will either be lines that represent the skyline or
          multipatches that represent silhouettes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Skyline_3d(*gp_fixargs((in_observer_point_features, out_feature_class, in_surface, virtual_surface_radius, virtual_surface_elevation, in_features, feature_lod, from_azimuth_value_or_field, to_azimuth_value_or_field, azimuth_increment_value_or_field, max_horizon_radius, segment_skyline, scale_to_percent, scale_according_to, scale_method, use_curvature, use_refraction, refraction_factor, pyramid_level_resolution, create_silhouettes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SkylineBarrier_3d', None)
def SkylineBarrier(in_observer_point_features=None, in_features=None, out_feature_class=None, min_radius_value_or_field=None, max_radius_value_or_field=None, closed=None, base_elevation=None, project_to_plane=None):
    """SkylineBarrier(in_observer_point_features, in_features, out_feature_class, {min_radius_value_or_field}, {max_radius_value_or_field}, {closed}, {base_elevation}, {project_to_plane})

        Generates a multipatch feature class representing a skyline barrier or shadow
        volume.

     INPUTS:
      in_observer_point_features (Feature Layer):
          The point feature class containing the observer points.
      in_features (Feature Layer):
          The input line feature class which represents the skylines, or the input
          multipatch feature class which represents the silhouettes.
      min_radius_value_or_field {Linear unit / Field}:
          The minimum radius to which triangle edges should be extended from the observer
          point. The default is 0, meaning no minimum.
      max_radius_value_or_field {Linear unit / Field}:
          The maximum radius to which triangle edges should be extended from the observer
          point. The default is 0, meaning no maximum.
      closed {Boolean}:
          Whether to close the skyline barrier with a skirt and a base so that the
          resulting multipatch will appear to be a solid.

          * NO_CLOSED—No skirt or base is added to the multipatch; just the multipatch
          representing the surface going from the observer to the skyline is represented.
          This is the default.

          * CLOSED— A skirt and a base are added to the multipatch so as to form what
          appears to be a closed solid.
      base_elevation {Linear unit / Field}:
          The elevation of the base of the closed multipatch; it is ignored if the
          barrier is not to be closed.  The default is 0.
      project_to_plane {Boolean}:
          Whether the front (nearer to the observer) and back (farther from the observer)
          ends of the barrier should each be projected onto a vertical plane. This is
          typically checked (turned on) in order to create a shadow volume.

          *  NO_PROJECT_TO_PLANE—The barrier will extend from the observer point to the
          skyline (or nearer or farther if nonzero values are provided for minimum and
          maximum radius). This is the default.

          *  PROJECT_TO_PLANE— The barrier will extend from a vertical plane to a vertical
          plane.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class into which the skyline barrier or shadow volume is
          placed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SkylineBarrier_3d(*gp_fixargs((in_observer_point_features, in_features, out_feature_class, min_radius_value_or_field, max_radius_value_or_field, closed, base_elevation, project_to_plane), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SkylineGraph_3d', None)
def SkylineGraph(in_observer_point_features=None, in_line_features=None, base_visibility_angle=None, additional_fields=None, out_angles_table=None, out_graph=None):
    """SkylineGraph(in_observer_point_features, in_line_features, {base_visibility_angle}, {additional_fields}, {out_angles_table}, {out_graph})

        Calculates sky visibility and generates an optional table and polar graph.The
        table and graph represent the horizontal and vertical angles going from the
        observer point to each of the vertices on the skyline.

     INPUTS:
      in_observer_point_features (Feature Layer):
          The input features containing one or more observer points.
      in_line_features (Feature Layer):
          The line feature class representing the skyline.
      base_visibility_angle {Double}:
          The vertical angle which is used as the baseline for calculating percentage of
          visible sky; 0 is the horizon, 90 is straight up; -90 is straight down. The
          default is 0.
      additional_fields {Boolean}:
          Determines whether to output additional fields to the table, rather than just
          the two angle values.

          * NO_ ADDITIONAL_FIELDS—The additional fields will not be output. This is the
          default.

          *  ADDITIONAL_FIELDS—The additional fields will be output.

     OUTPUTS:
      out_angles_table {Table}:
          The table to be created for outputting the angles. The default is blank, meaning
          no table.
      out_graph {Graph}:
          The name of the optional graph. A table has to be generated in order for the
          graph to be made. The graph will be displayed and can be saved and/or edited.
          The default is blank, meaning no graph."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SkylineGraph_3d(*gp_fixargs((in_observer_point_features, in_line_features, base_visibility_angle, additional_fields, out_angles_table, out_graph), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SunShadowVolume_3d', None)
def SunShadowVolume(in_features=None, start_date_and_time=None, out_feature_class=None, adjusted_for_dst=None, time_zone=None, end_date_and_time=None, iteration_interval=None, iteration_unit=None):
    """SunShadowVolume(in_features;in_features..., start_date_and_time, out_feature_class, {adjusted_for_dst}, {time_zone}, {end_date_and_time}, {iteration_interval}, {iteration_unit})

        Creates closed volumes that model shadows cast by each feature using sunlight
        for a given date and time.

     INPUTS:
      in_features (Feature Layer):
          The multipatch features that will be used to model shadows. Polygon and line
          features can also be used if they are added as an extruded 3D layer.
      start_date_and_time (Date):
          The date and time that the trajectory of sunlight will be calculated for
          modeling the shadows.
      adjusted_for_dst {Boolean}:
          Specifies if time value is adjusted for Daylight Savings Time (DST).

          * ADJUSTED_FOR_DST—DST is observed.

          * NOT_ADJUSTED_FOR_DST—DST is not observed. This is the default.
      time_zone {String}:
          The time zone in which the participating input is located. The default setting
          is the time zone to which the operating system is set.
      end_date_and_time {Date}:
          The final date and time for calculating sun position. If only a date is
          provided, the final time is presumed to be sunset.
      iteration_interval {Double}:
          The value used to define the iteration of time from the start date.
      iteration_unit {String}:
          The unit that defines the iteration value applied to the Start Date and Time.

          * DAYS—Iteration value will represent days. This is the default.

          * HOURS—Iteration value will represent one or more hours.

          * MINUTES—Iteration value will represent one or more minutes.

     OUTPUTS:
      out_feature_class (Feature Class):
          The multipatch feature class that will store the resulting shadow volumes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SunShadowVolume_3d(*gp_fixargs((in_features, start_date_and_time, out_feature_class, adjusted_for_dst, time_zone, end_date_and_time, iteration_interval, iteration_unit), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Viewshed_3d', None)
def Viewshed(in_raster=None, in_observer_features=None, out_raster=None, z_factor=None, curvature_correction=None, refractivity_coefficient=None, out_agl_raster=None):
    """Viewshed(in_raster, in_observer_features, out_raster, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})

        Determines the raster surface locations visible to a set of observer features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      in_observer_features (Composite Geodataset):
          The feature class that identifies the observer locations.The input can be point
          or polyline features.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface. If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).
      curvature_correction {Boolean}:
          Allows correction for the earth's curvature.

          * FLAT_EARTH — No curvature correction will be applied. This is the default.

          * CURVED_EARTH — Curvature correction will be applied.
      refractivity_coefficient {Double}:
          Coefficient of the refraction of visible light in air.The default value is 0.13.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output will only record the number of times that each cell
          location in the
          input surface raster can be seen by the input observation points (or vertices
          for polylines). The observation frequency will be recorded in the VALUE item in
          the output raster's attribute table.
      out_agl_raster {Raster Dataset}:
          The output above ground level (AGL) raster.The AGL result is a raster where each
          cell value is the minimum height that must
          be added to an otherwise nonvisible cell to make it visible by at least one
          observer.Cells that were already visible will have a value of 0 in this output
          raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Viewshed_3d(*gp_fixargs((in_raster, in_observer_features, out_raster, z_factor, curvature_correction, refractivity_coefficient, out_agl_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Viewshed2_3d', None)
def Viewshed2(in_raster=None, in_observer_features=None, out_raster=None, out_agl_raster=None, analysis_type=None, vertical_error=None, out_observer_region_relationship_table=None, refractivity_coefficient=None, surface_offset=None, observer_elevation=None, observer_offset=None, inner_radius=None, inner_radius_is_3d=None, outer_radius=None, outer_radius_is_3d=None, horizontal_start_angle=None, horizontal_end_angle=None, vertical_upper_angle=None, vertical_lower_angle=None, analysis_method=None):
    """Viewshed2(in_raster, in_observer_features, out_raster, {out_agl_raster}, {analysis_type}, {vertical_error}, {out_observer_region_relationship_table}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {inner_radius_is_3d}, {outer_radius}, {outer_radius_is_3d}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle}, {analysis_method})

        Determines the raster surface locations visible to a set of observer features,
        using geodesic methods.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster. It can be an integer or a floating-point raster.The
          input raster is transformed into a 3D geocentric coordinate system during
          the visibility calculation. NoData cells on the input raster do not block the
          visibility determination.
      in_observer_features (Composite Geodataset):
          The input feature class that identifies the observer locations. It can be point,
          multipoint, or polyline features.The input feature class is transformed into a
          3D geocentric coordinate system
          during the visibility calculation. Observers outside of the extent of the
          surface raster or located on NoData cells will be ignored in the calculation.
      analysis_type {String}:
          Choose which type of visibility analysis you wish to perform, either determining
          how visible each cell is to the observers, or identifying for each surface
          location which observers are visible.

          * FREQUENCY—The output records the number of times that each cell location in
          the input surface raster can be seen by the input observation locations (as
          points or as vertices for polyline observer features). This is the default.

          * OBSERVERS — The output identifies exactly which observer points are visible
          from each raster surface location. The allowed maximum number of input observers
          is 32 with this analysis type.
      vertical_error {Linear unit}:
          The amount of uncertainty (the Root-Mean-Square error, or RMSE) in the surface
          elevation values. It is a floating-point value representing the expected error
          of the input elevation values. When this parameter is assigned a value greater
          than 0, the output visibility raster will be floating point. In this case, each
          cell value on the output visibility raster represents the sum of probabilities
          that the cell is visible to any of the observers.When the analysis type is
          OBSERVERS or the analysis method is
          PERIMETER_SIGHTLINES, this parameter is disabled.
      refractivity_coefficient {Double}:
          Coefficient of the refraction of visible light in air.The default value is 0.13.
      surface_offset {Linear unit / Field}:
          This value indicates a vertical distance (in surface units) to be added to the
          z-value of each target cell as it is considered for visibility. It should be a
          positive integer or floating-point value.It can be a field in the input observer
          features dataset or a numerical value.
          If this parameter is set to a value, then that value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      observer_elevation {Linear unit / Field}:
          This value is used to define the surface elevations of the observer points or
          vertices.It can be a field in the input observer features dataset or a numerical
          value.
          If this parameter is not specified, the observer elevation will be obtained from
          the surface raster using bilinear interpolation. If this parameter is set to a
          value, then that value will be applied to all the observers. To specify
          different values for each observer, set this parameter to a field in the input
          observer features dataset.
      observer_offset {Linear unit / Field}:
          This value indicates a vertical distance (in surface units) to be added to
          observer elevation. It should be a positive integer or floating-point value.It
          can be a field in the input observer features dataset or a numerical value.
          If this parameter is set to a value, then that value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      inner_radius {Linear unit / Field}:
          This value defines the start (minimum) distance from which visibility is
          determined. Cells closer than this distance are considered not visible in the
          output but can still block visibility of the cells between the inner radius and
          the outer radius. The default value is 0.It can be a field in the input observer
          features dataset or a numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      inner_radius_is_3d {Boolean}:
          Type of distance for the inner radius parameter.

          * GROUND—Inner radius is to be interpreted as a 2D distance. This is the
          default.

          * 3D—Inner radius is to be interpreted as a 3D distance.
      outer_radius {Linear unit / Field}:
          This value defines the maximum distance from which visibility is determined.
          Cells beyond this distance are excluded from the analysis.It can be a field in
          the input observer features dataset or a numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      outer_radius_is_3d {Boolean}:
          Type of distance for the outer radius parameter.

          * GROUND—Outer radius is to be interpreted as a 2D distance. This is the
          default.

          * 3D —Outer radius is to be interpreted as a 3D distance.
      horizontal_start_angle {Double / Field}:
          This value defines the start angle of the horizontal scan range. The value
          should be specified in degrees from 0 to 360.0, with 0 oriented to north. The
          default value is 0.It can be a field in the input observer features dataset or a
          numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      horizontal_end_angle {Double / Field}:
          This value defines the end angle of the horizontal scan range. The value should
          be specified in degrees from 0 to 360.0, with 0 oriented to north. The default
          value is 360.0.It can be a field in the input observer features dataset or a
          numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      vertical_upper_angle {Double / Field}:
          This value defines the upper vertical angle limit of the scan above a horizontal
          plane. The value should be specified in degrees from 0 to 90.0, which can be
          integer or floating point. The default value is 90.0.It can be a field in the
          input observer features dataset or a numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      vertical_lower_angle {Double / Field}:
          This value defines the lower vertical angle limit of the scan below a horizontal
          plane. The value should be specified in degrees from -90.0 to 0, which can be
          integer or floating point. The default value is -90.0.It can be a field in the
          input observer features dataset or a numerical value.
          If this parameter is set to a value, then the value will be applied to all the
          observers. To specify different values for each observer, set this parameter to
          a field in the input observer features dataset.
      analysis_method {String}:
          Choose the method by which the visibility will be calculated. This option allows
          you to trade some accuracy for increased performance.

          * ALL_SIGHTLINES—A sightline is run to every cell on the raster in order to
          establish visible areas. This is the default method.

          * PERIMETER_SIGHTLINES— Sightlines are only run to the cells on the perimeter of
          the visible areas in order to establish visibility areas. This method has a
          better performance than the ALL_SIGHTLINES method since less sightlines are run
          in the calculation.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.For the FREQUENCY analysis type, when the vertical error
          parameter is 0 or not
          specified, the output raster records the number of times that each cell location
          in the input surface raster can be seen by the input observation points. When
          the vertical error parameter is greater than 0, each cell on the output raster
          records the sum of probabilities that the cell is visible to any of the
          observers. For the OBSERVERS analysis type, the output raster records the unique
          region IDs for the visible areas, which can be related back to the observer
          features through the output observer-region relationship table.
      out_agl_raster {Raster Dataset}:
          The output above ground level (AGL) raster.The AGL result is a raster where each
          cell value is the minimum height that must
          be added to an otherwise nonvisible cell to make it visible by at least one
          observer. Cells that were already visible will be assigned 0 in this output
          raster.When the vertical error parameter is 0, the output AGL raster is a one-
          band
          raster. When vertical error is greater than 0, to account for the random effects
          from the input raster, the output AGL raster is created as a three-band raster.
          The first band represents the mean AGL values, the second band represents the
          minimum AGL values, and the third band represents the maximum AGL values.
      out_observer_region_relationship_table {Table}:
          The output table for identifying the regions that are visible to each observer.
          This table can be related to the input observer feature class and the output
          visibility raster for identifying the regions visible to given observers.This
          output is only created when the analysis type is OBSERVERS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Viewshed2_3d(*gp_fixargs((in_raster, in_observer_features, out_raster, out_agl_raster, analysis_type, vertical_error, out_observer_region_relationship_table, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, inner_radius_is_3d, outer_radius, outer_radius_is_3d, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle, analysis_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Visibility_3d', None)
def Visibility(in_raster=None, in_observer_features=None, out_raster=None, out_agl_raster=None, analysis_type=None, nonvisible_cell_value=None, z_factor=None, curvature_correction=None, refractivity_coefficient=None, surface_offset=None, observer_elevation=None, observer_offset=None, inner_radius=None, outer_radius=None, horizontal_start_angle=None, horizontal_end_angle=None, vertical_upper_angle=None, vertical_lower_angle=None):
    """Visibility(in_raster, in_observer_features, out_raster, {out_agl_raster}, {analysis_type}, {nonvisible_cell_value}, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {outer_radius}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle})

        Determines the raster surface locations visible to a set of observer features,
        or identifies which observer points are visible from each raster surface
        location.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      in_observer_features (Composite Geodataset):
          The feature class that identifies the observer locations.The input can be point
          or polyline features.
      analysis_type {String}:
          The visibility analysis type.

          * FREQUENCY — The output records the number of times that each cell location in
          the input surface raster can be seen by the input observation locations (as
          points, or as vertices for polyline observer features). This is the default.

          * OBSERVERS — The output identifies exactly which observer points are visible
          from each raster surface location.
      nonvisible_cell_value {Boolean}:
          Value assigned to non-visible cells.

          * ZERO— 0 is assigned to nonvisible cells. This is the default.

          * NODATA— NoData is assigned to nonvisible cells.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts the units
          of measure for the z units when they are
          different from the x,y units of the input surface. The z-values of the input
          surface are multiplied by the z-factor when calculating the final output
          surface.If the x,y units and z units are in the same units of measure, the
          z-factor is
          1. This is the default.If the x,y units and z units are in different units of
          measure, the z-factor
          must be set to the appropriate factor, or the results will be incorrect. For
          example, if your z units are feet and your x,y units are meters, you would use a
          z-factor of 0.3048 to convert your z units from feet to meters (1 foot = 0.3048
          meter).
      curvature_correction {Boolean}:
          Allows correction for the earth's curvature.

          * FLAT_EARTH — No curvature correction will be applied. This is the default.

          * CURVED_EARTH — Curvature correction will be applied.
      refractivity_coefficient {Double}:
          Coefficient of the refraction of visible light in air.The default value is 0.13.
      surface_offset {String}:
          This value indicates a vertical distance (in surface units) to be added to the
          z-value of each cell as it is considered for visibility. It should be a positive
          integer or floating point value.It can be a field in the input observer features
          dataset or a numerical value.
          By default, a numerical field OFFSETB is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to 0.
      observer_elevation {String}:
          This value is used to define the surface elevations of the observer points or
          vertices.It can be a field in the input observer features dataset or a numerical
          value.
          By default, a numerical field SPOT is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it will be estimated through bilinear
          interpolation with the surface elevation values in the neighboring cells of the
          observer location.
      observer_offset {String}:
          This value indicates a vertical distance (in surface units) to be added to
          observer elevation. It should be a positive integer or floating point value.It
          can be a field in the input observer features dataset or a numerical value.
          By default, a numerical field OFFSETA is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to 1.
      inner_radius {String}:
          This value defines the start distance from which visibility is determined.
          Cells closer than this distance are not visible in the output, but can still
          block visibility of the cells between inner radius and outer radius. It can be a
          positive or negative integer or floating point value. If it is a positive value,
          then it is interpreted as three-dimensional, line-of-sight distance. If it is a
          negative value, then it is interpreted as two-dimensional planimetric
          distance.It can be a field in the input observer features dataset or a numerical
          value.
          By default, a numerical field RADIUS1 is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or a constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to 0.
      outer_radius {String}:
          This value defines the maximum distance from which visibility is determined.
          Cells beyond this distance are excluded from the analysis. It can be a positive
          or negative integer or floating point value. If it is a positive value, then it
          is interpreted as three-dimensional, line-of-sight distance. If it is a negative
          value, then it is interpreted as two-dimensional planimetric distance.It can be
          a field in the input observer features dataset or a numerical value.
          By default, a numerical field RADIUS2 is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to infinity.
      horizontal_start_angle {String}:
          This value defines the start angle of the horizontal scan range. The value
          should be specified in degrees from 0 to 360, with 0 oriented to north. The
          default value is 0.It can be a field in the input observer features dataset or a
          numerical value.
          By default, a numerical field AZIMUTH1 is used if it exists in the input
          observer features attribute table. You may overwrite it by specifying another
          numerical field or constant.If this parameter is unspecified and the default
          field does not exist in the
          input observer features attribute table, it defaults to 0.
      horizontal_end_angle {String}:
          This value defines the end angle of the horizontal scan range. The value should
          be specified in degrees from 0 to 360, with 0 oriented to north. The default
          value is 360.It can be a field in the input observer features dataset or a
          numerical value.
          By default, a numerical field AZIMUTH2 is used if it exists in the input
          observer features attribute table. You may overwrite it by specifying another
          numerical field or constant.If this parameter is unspecified and the default
          field does not exist in the
          input observer features attribute table, it defaults to 360.
      vertical_upper_angle {String}:
          This value defines the upper vertical angle limit of the scan above a
          horizontal plane. The value should be specified in degrees from 0 to 90, which
          can be integer or floating point.It can be a field in the input observer
          features dataset or a numerical value.
          By default, a numerical field VERT1 is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to 90.
      vertical_lower_angle {String}:
          This value defines the lower vertical angle limit of the scan below a
          horizontal plane. The value should be specified in degrees from -90 to 0, which
          can be integer or floating point.It can be a field in the input observer
          features dataset or a numerical value.
          By default, a numerical field VERT2 is used if it exists in the input observer
          features attribute table. You may overwrite it by specifying another numerical
          field or constant.If this parameter is unspecified and the default field does
          not exist in the
          input observer features attribute table, it defaults to -90.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output will either record the number of times that each
          cell location in the
          input surface raster can be seen by the input observation locations (the
          frequency analysis type), or record which observer locations are visible from
          each cell in the raster surface (the observers type option).
      out_agl_raster {Raster Dataset}:
          The output above-ground-level (AGL) raster.The AGL result is a raster where
          each cell value is the minimum height that must
          be added to an otherwise nonvisible cell to make it visible by at least one
          observer.Cells that were already visible will have a value of 0 in this output
          raster."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Visibility_3d(*gp_fixargs((in_raster, in_observer_features, out_raster, out_agl_raster, analysis_type, nonvisible_cell_value, z_factor, curvature_correction, refractivity_coefficient, surface_offset, observer_elevation, observer_offset, inner_radius, outer_radius, horizontal_start_angle, horizontal_end_angle, vertical_upper_angle, vertical_lower_angle), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject