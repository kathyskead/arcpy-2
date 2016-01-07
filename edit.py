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
"""The Editing tools allow you to apply bulk editing to all (or selected) features
in a feature class."""
__all__ = ['Densify', 'ErasePoint', 'ExtendLine', 'FlipLine', 'Snap', 'TrimLine', 'Generalize', 'EdgematchFeatures', 'GenerateEdgematchLinks', 'GenerateRubbersheetLinks', 'RubbersheetFeatures', 'TransferAttributes']
__alias__ = u'edit'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('Densify_edit', None)
def Densify(in_features=None, densification_method=None, distance=None, max_deviation=None, max_angle=None):
    """Densify_edit(in_features, {densification_method}, {distance}, {max_deviation}, {max_angle})

        Adds vertices along line or polygon features. Also replaces curve segments
        (Bezier, circular arcs, and elliptical arcs) with line segments.

     INPUTS:
      in_features (Feature Layer):
          The polygon or line feature class to be densified.
      densification_method {String}:
          The method selected to handle feature densification.

          * DISTANCE—The tool will apply the Distance method to curves the same as it does
          to straight lines. This is the default.

          * OFFSET—The tool will apply the value of the Maximum Offset Deviation parameter
          (max_deviation in Python) to curves.

          * ANGLE—The tool will apply the value of the Maximum Deflection Angle parameter
          (max_angle in Python) to curves.
      distance {Linear unit}:
          The maximum linear distance between vertices. This distance will always be
          applied to line segments and to simplify curves. The default value is a function
          of the data's xy tolerance.
      max_deviation {Linear unit}:
          The maximum distance the output segment can be from the original. This parameter
          only affects curves.  The default value is a function of the data's xy
          tolerance.
      max_angle {Double}:
          The maximum angle that the output geometry can be from the input geometry. The
          valid range is from 0 to 90. The default value is 10. This parameter only
          affects curves."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Densify_edit(*gp_fixargs((in_features, densification_method, distance, max_deviation, max_angle), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ErasePoint_edit', None)
def ErasePoint(in_features=None, remove_features=None, operation_type=None):
    """ErasePoint_edit(in_features, remove_features, {operation_type})

        Deletes points from the input that are either inside or outside the Remove
        Features, depending on the Operation Type.

     INPUTS:
      in_features (Feature Layer):
          The input point features.
      remove_features (Feature Layer):
          Input features inside or outside the Remove Features will be deleted, depending
          on the Operation Type parameter.
      operation_type {String}:
          Determines if points inside or outside the remove features will be deleted.

          * INSIDE—Input point features inside or on the boundary of the remove features
          will be deleted.

          * OUTSIDE—Input point features outside the remove features will be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ErasePoint_edit(*gp_fixargs((in_features, remove_features, operation_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExtendLine_edit', None)
def ExtendLine(in_features=None, length=None, extend_to=None):
    """ExtendLine_edit(in_features, {length}, {extend_to})

        This tool extends line segments to the first intersecting feature within a
        specified distance. If no intersecting feature is within the specified distance,
        the line segment will not be extended. Tool use is intended for quality control
        tasks such as cleaning up topology errors in features that were digitized
        without having set proper snapping environments.

     INPUTS:
      in_features (Feature Layer):
          The line input features to be extended.
      length {Linear unit}:
          The maximum distance a line segment can be extended to an intersecting feature.
      extend_to {Boolean}:
          Controls whether line segments can be extended to other extended line segments
          within the specified extend length.

          * EXTENSION—Line segments can be extended to other extended line segments as
          well as existing line features. This is the default.

          * FEATURE—Line segments can only be extended to existing line features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExtendLine_edit(*gp_fixargs((in_features, length, extend_to), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FlipLine_edit', None)
def FlipLine(in_features=None):
    """FlipLine_edit(in_features)

        Reverses the from-to direction of line features.You can view the orientation of
        line features by symbolizing line features with
        arrowheads.

     INPUTS:
      in_features (Feature Layer):
          The input line feature class or layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FlipLine_edit(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Generalize_edit', None)
def Generalize(in_features=None, tolerance=None):
    """Generalize_edit(in_features, {tolerance})

        Simplifies the input features using a specified maximum offset tolerance. The
        output features will contain a subset of the original input vertices.

     INPUTS:
      in_features (Feature Layer):
          The polygon or line features to be generalized.
      tolerance {Linear unit}:
          The tolerance sets the maximum allowable offset, which will determine the degree
          of simplification. This value limits the distance the output geometry can differ
          from the input geometry. You can specify a preferred unit of measurement. The
          default is the feature unit."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Generalize_edit(*gp_fixargs((in_features, tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Snap_edit', None)
def Snap(in_features=None, snap_environment=None):
    """Snap_edit(in_features, snap_environment;snap_environment...)

        Moves points or vertices to coincide exactly with the vertices, edges, or end
        points of other features. Snapping rules can be specified to control whether the
        input vertices are snapped to the nearest vertex, edge, or endpoint within a
        specified distance.

     INPUTS:
      in_features (Feature Layer):
          The input features whose vertices will be snapped to the vertices, edges, or end
          points of other features. The input features can be points, multipoints, lines,
          or polygons.
      snap_environment (Value Table):
          Enter the feature classes or feature layers containing the features you wish to
          snap to.Snapping Environment Components:

          * Features — Features that the input features' vertices will be snapped to.
          These features can be points, multipoints, lines, or polygons.

          * Type — Type of feature part that the input features' vertices can be snapped
          to (END | VERTEX | EDGE).

          * Distance — Distance within which the input features' vertices will be snapped
          to the nearest vertex, edge, or end point.
          Snapping Environment Type Options:

          * END — Input feature vertices will be snapped to feature ends.

          * VERTEX — Input feature vertices will be snapped to feature vertices.

          * EDGE — Input feature vertices will be snapped to feature edges.
          In the Snap Environment parameter, if no unit is entered with the Distance
          (i.e., 10 instead of 10 Meters), the linear or angular unit from the input
          feature's coordinate system will be used as default. If the input features have
          a projected coordinate system, its linear unit will be used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Snap_edit(*gp_fixargs((in_features, snap_environment), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TrimLine_edit', None)
def TrimLine(in_features=None, dangle_length=None, delete_shorts=None):
    """TrimLine_edit(in_features, {dangle_length}, {delete_shorts})

        Removes portions of a line that extend a specified distance past a line
        intersection (dangles). Any line that does not touch another line at both
        endpoints can be trimmed, but only the portion of the line that extends past the
        intersection by the specified distance will be removed.Tool use is intended for
        quality control tasks such as cleaning up topology
        errors in features that were digitized without having set proper snapping
        environments.

     INPUTS:
      in_features (Feature Layer):
          The line input features to be trimmed.
      dangle_length {Linear unit}:
          Line segments that are shorter than the specified Dangle Length and do not touch
          another line at both endpoints (dangles) will be trimmed.If no Dangle Length is
          specified, all dangling lines (line segments that do not
          touch another line at both endpoints), regardless of length, will be trimmed
          back to the point of intersection.
      delete_shorts {Boolean}:
          Controls whether line segments which are less than the dangle length and are
          free-standing will be deleted.

          * DELETE_SHORT— Delete short free-standing features. This is the default.

          * KEEP_SHORT—Do not delete short free-standing features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TrimLine_edit(*gp_fixargs((in_features, dangle_length, delete_shorts), True)))
        return retval
    except Exception, e:
        raise e


# Conflation toolset
@gptooldoc('EdgematchFeatures_edit', None)
def EdgematchFeatures(in_features=None, in_link_features=None, method=None, adjacent_features=None, border_features=None):
    """EdgematchFeatures_edit(in_features, in_link_features, {method}, {adjacent_features}, {border_features})

        Modifies input line features by spatially adjusting their shapes, guided by the
        specified edgematch links, so they become connected with the lines in the
        adjacent dataset.

     INPUTS:
      in_features (Feature Layer):
          Input line features to be adjusted.
      in_link_features (Feature Layer):
          Input line features representing edgematch links.
      method {String}:
          Edgematch method to be used to adjust either input features only or both input
          features and adjacent features to new connecting locations.

          *  MOVE_ENDPOINT—Moves the endpoint of a line to the new connecting location.
          This is the default.

          *  ADD_SEGMENT—Adds a straight segment at the end of a line so it ends at the
          new connecting location.

          * ADJUST_VERTICES—Adjusts the endpoint of a line to the new connecting location.
          The remaining vertices are also adjusted so its positional changes are gradually
          reduced toward the opposite end of the line.
      adjacent_features {Feature Layer}:
          Line features that are adjacent to input features. If specified, both the input
          and adjacent features are adjusted to meet at new connecting locations, either
          the midpoints of the edgematch links or locations nearest to the midpoints of
          the links on the border features (if specified). You must provide adjacent
          features if you provide border features.
      border_features {Feature Layer}:
          Line or polygon features representing borders between the input and adjacent
          features. When you specify the border features, you must also specify the
          adjacent features. Both input and adjacent features are adjusted to meet at new
          connecting locations nearest to the midpoints of the links on the border
          features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EdgematchFeatures_edit(*gp_fixargs((in_features, in_link_features, method, adjacent_features, border_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateEdgematchLinks_edit', None)
def GenerateEdgematchLinks(source_features=None, adjacent_features=None, out_feature_class=None, search_distance=None, match_fields=None):
    """GenerateEdgematchLinks_edit(source_features, adjacent_features, out_feature_class, search_distance, {match_fields;match_fields...})

        Finds matching but disconnected line features along the edges of the source
        data's area and its adjacent data's area, and generates edgematch links from the
        source lines to the matched adjacent lines.

     INPUTS:
      source_features (Feature Layer):
          Line features as edgematching source features. All edgematch links start at
          source features.
      adjacent_features (Feature Layer):
          Line features adjacent to source features. All edgematch links end at matched
          adjacent features.
      search_distance (Linear unit):
          The distance used to search for match candidates. A distance must be specified
          and it must be greater than zero. You can choose a preferred unit; the default
          is the feature unit.
      match_fields {Value Table}:
          Fields from source and target features, where target fields are from the
          adjacent features. If specified, each pair of fields are checked for match
          candidates to help determine the right match.

     OUTPUTS:
      out_feature_class (Feature Class):
          Output feature class containing lines representing edgematch links."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateEdgematchLinks_edit(*gp_fixargs((source_features, adjacent_features, out_feature_class, search_distance, match_fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateRubbersheetLinks_edit', None)
def GenerateRubbersheetLinks(source_features=None, target_features=None, out_feature_class=None, search_distance=None, match_fields=None, out_match_table=None):
    """GenerateRubbersheetLinks_edit(source_features, target_features, out_feature_class, search_distance, {match_fields;match_fields...}, {out_match_table})

        Finds where the source line features spatially match the target line features
        and generates lines representing links from source locations to corresponding
        target locations for rubbersheeting.

     INPUTS:
      source_features (Feature Layer):
          Line features as source features for generating rubbersheet links. All links
          start at source features.
      target_features (Feature Layer):
          Line features as target features for generating rubbersheet links. All links
          end at matched target features.
      search_distance (Linear unit):
          The distance used to search for match candidates. A distance must be specified
          and it must be greater than zero. You can choose a preferred unit; the default
          is the feature unit.
      match_fields {Value Table}:
          Lists of fields from source and target features. If specified, each pair of
          fields are checked for match candidates to help determine the right match.

     OUTPUTS:
      out_feature_class (Feature Class):
          Output feature class containing lines representing regular rubbersheet links.
      out_match_table {Table}:
          The output table containing complete feature matching information."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateRubbersheetLinks_edit(*gp_fixargs((source_features, target_features, out_feature_class, search_distance, match_fields, out_match_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RubbersheetFeatures_edit', None)
def RubbersheetFeatures(in_features=None, in_link_features=None, in_identity_links=None, method=None):
    """RubbersheetFeatures_edit(in_features, in_link_features, {in_identity_links}, {method})

        Modifies input line features by spatially adjusting them through
        rubbersheeting, using the specified rubbersheet links, so they are better
        aligned with the intended target features.

     INPUTS:
      in_features (Feature Layer):
          Input line features to be adjusted.
      in_link_features (Feature Layer):
          Input line features representing regular links for rubbersheeting.
      in_identity_links {Feature Layer}:
          Input point features representing identity links for rubbersheeting.
      method {String}:
          Rubbersheeting method to be used to adjust features.

          *  LINEAR—This method is slightly faster and produces good results when you have
          many links spread uniformly over the data you are adjusting. This is the
          default.

          * NATURAL_NEIGHBOR—This method should be used when you have few links spaced
          widely apart."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RubbersheetFeatures_edit(*gp_fixargs((in_features, in_link_features, in_identity_links, method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TransferAttributes_edit', None)
def TransferAttributes(source_features=None, target_features=None, transfer_fields=None, search_distance=None, match_fields=None, out_match_table=None):
    """TransferAttributes_edit(source_features, target_features, transfer_fields;transfer_fields..., search_distance, {match_fields;match_fields...}, {out_match_table})

        Finds where the source line features spatially match the target line features
        and transfers specified attributes from source features to matched target
        features. Attribute transfer is typically used to copy attributes from features
        in one
        dataset to corresponding features in another dataset. For example, it can be
        used to transfer the names of road features from a previously digitized and
        maintained dataset to features in a new dataset that are newly collected and
        more accurate. The two datasets are usually referred to as source features and
        target features. This tool finds corresponding source and target line features
        within the specified search distance and transfers the specified attributes from
        source lines to target lines.

     INPUTS:
      source_features (Feature Layer):
          Line features from which to transfer attributes.
      target_features (Feature Layer):
          Line features to which to transfer attributes. The specified transfer fields
          are added to the target features.
      transfer_fields (Field):
          List of source fields to be transferred to target features. At least one field
          must be specified.
      search_distance (Linear unit):
          The distance used to search for match candidates. A distance must be specified
          and it must be greater than zero. You can choose a preferred unit; the default
          is the feature unit.
      match_fields {Value Table}:
          Lists of fields from source and target features. If specified, each pair of
          fields are checked for match candidates to help determine the right match.

     OUTPUTS:
      out_match_table {Table}:
          The output table containing complete feature matching information."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TransferAttributes_edit(*gp_fixargs((source_features, target_features, transfer_fields, search_distance, match_fields, out_match_table), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject