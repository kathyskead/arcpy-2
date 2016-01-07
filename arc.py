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
"""The Coverage toolbox provides a powerful set of tools to perform various
geoprocessing operations that use coverages. A coverage is a data model used to
store geographic features that has been superseded with the development and data
model structure of the geodatabase."""
__all__ = ['Clip', 'Erase', 'Identity', 'Intersect', 'Union', 'Update', 'Thiessen', 'Near', 'PointDistance', 'Build', 'Clean', 'CreateLabels', 'IDEdit', 'AddXY', 'Renode', 'PointNode', 'DefineProjection', 'JoinItem', 'Split', 'Buffer', 'PolyRegion', 'RegionPoly', 'ArcDLG', 'ArcRoute', 'DLGArc', 'Ungenerate', 'RegionClass', 'AddItem', 'IndexItem', 'DropIndex', 'DropItem', 'Tolerance', 'Create', 'Transform', 'Generate', 'Import', 'Export', 'S57Arc', 'ArcS57', 'VPFImport', 'VPFExport', 'VPFTile', 'SDTSExport', 'SDTSImport', 'TigerArc', 'Project', 'Append', 'TigerTool', 'Reselect', 'AggregatePolygons', 'CollapseDualLinesToCenterline', 'Dissolve', 'Eliminate', 'FindConflicts', 'SimplifyBuilding', 'SimplifyLineOrPolygon']
__alias__ = u'arc'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Analysis\Extract toolset
@gptooldoc('Clip_arc', None)
def Clip(in_cover=None, clip_cover=None, out_cover=None, feature_type=None, fuzzy_tolerance=None):
    """Clip_arc(in_cover, clip_cover, out_cover, {feature_type}, {fuzzy_tolerance})

        Uses the outside polygon boundary of the clip coverage to cookie-cut features
        and attributes from the input coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage containing features to be clipped.
      clip_cover (Coverage):
          The coverage whose outer polygon defines the clipping region.
      feature_type {String}:
          The feature class to be clipped:

          * POLY—Polygons and region subclasses are clipped and a PAT is saved. Label
          points for remaining polygons are moved only if their original location falls
          outside the clipping boundary. Route systems are ignored.

          * LINE—Arcs are clipped, and an AAT is saved. Route systems are maintained.

          * POINT—Points are clipped, and a PAT is saved.

          * NET—Polygons and arcs are clipped, and their PAT and AAT are saved. Route
          systems and regions are maintained and clipped.

          * LINK—Arcs and points are clipped, and their AAT and PAT are saved. Route
          systems are maintained.

          * RAW—Points, arcs, and annotation in a coverage with or without topology (no
          attribute files) are clipped. Route systems are maintained, but regions, PAT,
          and AAT are not saved.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input coverage and erase coverage is
          used.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created. The output coverage cannot already exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Clip_arc(*gp_fixargs((in_cover, clip_cover, out_cover, feature_type, fuzzy_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Reselect_arc', None)
def Reselect(in_cover=None, out_cover=None, info_express=None, in_feature_type=None, selection_file=None, out_feature_type=None):
    """Reselect_arc(in_cover, out_cover, info_express;info_express..., {in_feature_type}, {selection_file}, {out_feature_type})

        Extracts selected features from an input coverage and stores them in the output
        coverage.Features are selected for extraction based on logical expressions or by
        applying
        the criteria contained in a selection file. Any item, including redefined items,
        in the specified feature attribute table of the Input coverage can be used.

     INPUTS:
      in_cover (Coverage):
          The input coverage containing the features that will be selected.
      info_express (INFO Expression):
          Write a query that contains one or more logical expressions to select features
          from the input coverage. Each expression takes one of the following forms:

          * RESELECT <expression>—Reduces the selected set of records with a selection
          expression to those that meet its criteria. If no selection expression follows,
          the selected set will be empty.

          * ASELECT <expression>—Adds unselected records that meet the selection
          expression criteria to the currently selected set. If no selection expression
          follows, the selected set will contain all features.

          * NSELECT—Reverses the current selection to the unselected set.
      in_feature_type {String}:
          The feature class to select:

          * Poly—Polygons are reselected using PAT item values.

          * Line—Arcs are reselected using AAT item values.

          * Point—Points are reselected using PAT item values.

          * Anno.<subclass>—Annotation from the specified subclass is reselected using TAT
          subclass item values.

          * Route.<subclass>—Routes from the specified subclass are reselected using RAT
          subclass item values.

          * Section.<subclass>—Sections from the specified subclass are reselected using
          SEC subclass item values.

          * Region.<subclass>—Regions from the specified subclass are reselected using the
          region PAT subclass item values.
      selection_file {File}:
          A preexisting file that identifies the features to select.
      out_feature_type {String}:
          The feature class in the output coverage. This must be the same as that of the
          input feature class, with this exception: When the input feature class is an
          Anno, Route, Section, or Region subclass and the output coverage is the same as
          the Input coverage, the output feature class must have a different subclass
          name.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage containing the selected features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Reselect_arc(*gp_fixargs((in_cover, out_cover, info_express, in_feature_type, selection_file, out_feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Split_arc', None)
def Split(in_cover=None, split_cover=None, split_item=None, path=None, feature_type=None, fuzzy_tolerance=None):
    """Split_arc(in_cover, split_cover, split_item, {path}, {feature_type}, {fuzzy_tolerance})

        Clips portions of the input coverage into multiple coverages.Each new output
        coverage contains only those portions of the input coverage
        features overlapped by the split coverage polygons. The unique values in the
        Split Item are used to name the output coverages. The number of output coverages
        is determined by the number of unique values in the Split Item.

     INPUTS:
      in_cover (Coverage):
          The coverage to be split.
      split_cover (Coverage):
          The coverage used to split the input coverage.
      split_item (INFO Item):
          The item in the split coverage that will be used to split the input coverage.
          The unique values in the Split Item are used to name the output coverages. The
          number of output coverages is determined by the number of unique values in the
          Split Item.
      feature_type {String}:
          The feature classes to be split:

          * POLY—Polygons will be split. This is the default.

          * LINE—Arcs will be split.

          * POINT—Points will be split.

          * NET—Polygons and lines will be split.

          * LINK—Points and lines will be split.

          * RAW—Arcs, data points, and annotation in a coverage that does not have
          topology (no attribute files) will be split. Attributes are ignored.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in each output coverage. By default,
          the minimum fuzzy tolerance value from the input coverage and split coverage is
          used.

     OUTPUTS:
      path {Folder}:
          The workspace in which the output coverage will be maintained."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Split_arc(*gp_fixargs((in_cover, split_cover, split_item, path, feature_type, fuzzy_tolerance), True)))
        return retval
    except Exception, e:
        raise e


# Analysis\Overlay toolset
@gptooldoc('Erase_arc', None)
def Erase(in_cover=None, erase_cover=None, out_cover=None, feature_type=None, fuzzy_tolerance=None):
    """Erase_arc(in_cover, erase_cover, out_cover, {feature_type}, {fuzzy_tolerance})

        Creates a new output coverage by overlaying the polygons of the erase coverage
        with the features of the input coverage. Only those portions of the input
        coverage features falling outside the erase polygon outer boundaries are copied
        to the output coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage containing features to be erased.
      erase_cover (Coverage):
          The coverage whose outer polygon defines the erasing region.
      feature_type {String}:
          The set of features to be erased:

          * POLY—Polygons are erased, and the polygon attribute table (PAT) is updated.
          This is the default.

          * LINE—Arcs are erased, and the arc attribute table (AAT) is updated.

          * POINT—Points are erased, and the point attribute table (PAT) is updated.

          * NET—Polygons and arcs are erased, and their PAT and AAT are updated.

          * LINK—Arcs and points are erased, and their AAT and PAT are updated.

          * RAW—Arcs, data points, and annotation in a coverage that do not have topology
          (no attribute files) are erased. Route systems are maintained, but regions PAT
          and AAT are not saved.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input coverage and erase coverage is
          used.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Erase_arc(*gp_fixargs((in_cover, erase_cover, out_cover, feature_type, fuzzy_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Identity_arc', None)
def Identity(in_cover=None, identity_cover=None, out_cover=None, feature_type=None, fuzzy_tolerance=None, join_attributes=None):
    """Identity_arc(in_cover, identity_cover, out_cover, {feature_type}, {fuzzy_tolerance}, {join_attributes})

        Computes the geometric intersection of two coverages. All features of the input
        coverage, as well as those features of the identity coverage that overlap the
        input coverage, are preserved in the output coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage that will be overlaid with the identity coverage.
      identity_cover (Coverage):
          The coverage that will be identitied with the input coverage. Must have polygon
          features.
      feature_type {String}:
          The feature class from the input coverage that will be used.

          * POLY—Poly on poly overlay. This is the default option.

          * LINE—Line on poly overlay.

          * POINT—Point on poly overlay.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input and erase coverages is used.
      join_attributes {Boolean}:
          Specifies whether all items in both the input coverage feature attribute and
          identity coverage will be joined to the output coverage feature attribute table.

          * JOIN—All feature attribute items from both coverages will appear in the output
          coverage feature attribute table. If a duplicate item is encountered, the item
          in the input coverage will be maintained and the one in the join file will be
          dropped. This is the default option.

          * NO_JOIN—Only the feature's internal number (cover#) from the input coverage
          and the intersect coverage are joined in the output coverage feature attribute
          table. This option is useful in reducing the size of the output coverage feature
          attribute table. The Add Join tool can then be used to get the attributes to the
          output coverage features.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Identity_arc(*gp_fixargs((in_cover, identity_cover, out_cover, feature_type, fuzzy_tolerance, join_attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Intersect_arc', None)
def Intersect(in_cover=None, intersect_cover=None, out_cover=None, feature_type=None, fuzzy_tolerance=None, join_attributes=None):
    """Intersect_arc(in_cover, intersect_cover, out_cover, {feature_type}, {fuzzy_tolerance}, {join_attributes})

        Computes the geometric intersection of two coverages. Only those features in the
        area common to both coverages will be preserved in the output coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage whose polygon, line, or point features will be intersected with the
          intersect coverage.
      intersect_cover (Coverage):
          The intersect coverage. This coverage must contain polygon features.
      feature_type {String}:
          The input coverage feature class to be overlaid and preserved in the output
          coverage.

          * POLY—The input coverage's polygon feature class will be used as input. This is
          the default option.

          * LINE—The input coverage's line (arc) feature class will be used as input.

          * POINT—The input coverage's point feature class will be used as input.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input and erase coverages is used.
      join_attributes {Boolean}:
          Specifies whether all items in both the input coverage feature attribute and
          identity coverage will be joined to the output coverage feature attribute table.

          * JOIN—All feature attribute items from both coverages will appear in the output
          coverage feature attribute table. If a duplicate item is encountered, the item
          in the input coverage will be maintained and the one in the join file will be
          dropped. This is the default option.

          * NO_JOIN—Only the feature's internal number (cover#) from the input coverage
          and the intersect coverage are joined in the output coverage feature attribute
          table. This option is useful in reducing the size of the output coverage feature
          attribute table. The Add Join tool can then be used to get the attributes to the
          output coverage features.

     OUTPUTS:
      out_cover (Coverage):
          The coverage that will be created to contain the results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Intersect_arc(*gp_fixargs((in_cover, intersect_cover, out_cover, feature_type, fuzzy_tolerance, join_attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Union_arc', None)
def Union(in_cover=None, union_cover=None, out_cover=None, fuzzy_tolerance=None, join_attributes=None):
    """Union_arc(in_cover, union_cover, out_cover, {fuzzy_tolerance}, {join_attributes})

        Computes the geometric intersection of two polygon coverages. All polygons from
        both coverages will be split at their intersections and preserved in the output
        coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage whose polygons will be combined with the union coverage.
      union_cover (Coverage):
          The union coverage whose polygons will be combined with the input coverage.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input and union coverages is used.
      join_attributes {Boolean}:
          Specifies whether all items in both the input and the union coverage will be
          joined to the output coverage feature attribute table.

          * JOIN—All items from both coverages will appear in the output coverage feature
          attribute table. If duplicate item names are encountered, the item in the input
          coverage will be maintained, and the one in the join file will be dropped. This
          is the default option and is used unless NO_JOIN is specified.

          * NO_JOIN—Only the feature's internal number (cover#) from the input coverage
          and the union coverage are joined in the output coverage feature attribute
          table. This option is useful in reducing the size of the output coverage feature
          attribute table. The cover# field can then be used in the Add Join tool to link
          the features in the resulting coverage back to the features in the input or
          union coverage.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage that will be created containing the results of the
          operation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Union_arc(*gp_fixargs((in_cover, union_cover, out_cover, fuzzy_tolerance, join_attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Update_arc', None)
def Update(in_cover=None, update_cover=None, out_cover=None, feature_type=None, fuzzy_tolerance=None, keep_border=None):
    """Update_arc(in_cover, update_cover, out_cover, {feature_type}, {fuzzy_tolerance}, {keep_border})

        Replaces the input coverage areas with the update coverage polygons using a cut
        and paste operation.

     INPUTS:
      in_cover (Coverage):
          The coverage containing polygons to be updated.
      update_cover (Coverage):
          The coverage whose polygons will replace input coverage areas.
      feature_type {String}:
          The set of feature classes to be updated.

          * POLY—Polygons and PAT values are updated. This is the default option.

          * NET—Polygons and arcs, as well as PAT and AAT values, are updated.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the output coverage. By default, the
          minimum fuzzy tolerance value from the input and erase coverages is used.
      keep_border {Boolean}:
          Specifies whether the outside border of the update coverage will be kept after
          it is inserted into the input coverage.

          * KEEP_BORDER—The outside border of the update coverage will be kept in the
          output coverage. This is the default.

          * DROP_BORDER—The outside border of the update coverage is dropped after the
          update coverage is inserted into the input coverage. Item values of the update
          polygons take precedence over input coverage item values in the output coverage.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Update_arc(*gp_fixargs((in_cover, update_cover, out_cover, feature_type, fuzzy_tolerance, keep_border), True)))
        return retval
    except Exception, e:
        raise e


# Analysis\Proximity toolset
@gptooldoc('Buffer_arc', None)
def Buffer(in_cover=None, out_cover=None, feature_type=None, buffer_item=None, buffer_table=None, buffer_distance=None, fuzzy_tolerance=None, buffer_shape=None, buffer_side=None):
    """Buffer_arc(in_cover, out_cover, {feature_type}, {buffer_item}, {buffer_table}, {buffer_distance}, {fuzzy_tolerance}, {buffer_shape}, {buffer_side})

        Creates buffer polygons around specified input coverage features.

     INPUTS:
      in_cover (Coverage):
          The coverage containing features to be buffered.
      feature_type {String}:
          The feature class to be buffered:

          * LINE—Arcs will be buffered. This is the default.

          * POLY—Polygons will be buffered.

          * POINT—Points will be buffered.

          * NODE—Nodes will be buffered.
      buffer_item {String}:
          An item in the feature attribute table of input coverage whose value is used as
          the feature's buffer distance. If a buffer table is used, the buffer item
          functions as a lookup item in the buffer table.
      buffer_table {INFO Table}:
          An INFO lookup table that lists a buffer distance for each buffer item. A buffer
          table can be specified only if the buffer item is specified. The buffer table
          contains at least two items:

          * Buffer Item—Defined the same as buffer item in the input coverage feature
          attribute table. The buffer table must be sorted on this item in ascending
          order.

          * DIST—The buffer distance for each buffer item value. DIST must be defined as a
          numeric item (that is, N, I, F, or B). A lookup table will categorize item
          values.
      buffer_distance {Double}:
          The distance used to create buffer zones around input coverage features when
          buffer item and buffer table are not specified. The default buffer distance is
          0.125 coverage units. This default buffer distance will be applied whenever a
          value for this parameter is not specified.The smallest buffer distance that can
          be computed is 0.00000005 coverage units.
          Specifying a buffer distance below this threshold will result in an empty output
          coverage. For polygon features, if a negative buffer distance is used, buffers
          will be generated on the insides of polygons.
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in the out_cover. By default, the
          minimum fuzzy tolerance value from the in_cover is used.
      buffer_shape {String}:
          For lines, the shape of the buffer at the line endpoints.

          * ROUND—Will make an end in the shape of a halfcircle.

          * FLAT—Will construct rectangular line endings with the middle of the short side
          of the rectangle coincident with the endpoint of the line.
      buffer_side {String}:
          For lines, the topological side on which the buffer may be generated.

          * FULL—On all sides. This is the default.

          * LEFT—Half buffer on the topological left side of a line.

          * RIGHT—Half buffer on the topological right side of a line.

     OUTPUTS:
      out_cover (Coverage):
          The polygon buffer coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Buffer_arc(*gp_fixargs((in_cover, out_cover, feature_type, buffer_item, buffer_table, buffer_distance, fuzzy_tolerance, buffer_shape, buffer_side), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Near_arc', None)
def Near(in_cover=None, near_cover=None, out_cover=None, feature_type=None, search_radius=None, location=None):
    """Near_arc(in_cover, near_cover, out_cover, {feature_type}, {search_radius}, {location})

        Computes the distance from each point in a coverage to the nearest arc, point,
        or node in another coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage containing points from which distances are calculated to each
          closest arc, point, or node in the <near_cover:>.
      near_cover (Coverage):
          The line or point coverage whose features are used to calculate distances from
          each input cover point. This must be different from the input cover.
      feature_type {String}:
          The type of feature that will be searched from points to find the nearest
          feature and calculate the distance between them.

          * LINE—A point-to-arc distance will be determined. New items for distance and
          the internal number of the closest arc in the <near_cover:> will be added to the
          <input_cover> PAT. This is the default option.

          * POINT—A point-to-point distance will be determined. New items for distance and
          the internal number of the closest point in the <near_cover:> will be added to
          the <input_cover> PAT.

          * NODE—A point-to-node distance will be determined. New items for distance and
          the internal node number of the closest node in the <near_cover:> will be added
          to the <input_cover> PAT.
      search_radius {Double}:
          The maximum distance in coverage units between input cover features and near
          cover features for which distance and near cover internal number will be
          determined.If no near cover feature is within the search radius of a given input
          cover
          point or line, both the internal number and distance output by NEAR will be
          zero.The default search radius is the width or height of the near coverage BND
          divided by 100, whichever is larger. This default search radius is used whenever
          the search radius argument is set to zero or skipped.
      location {Boolean}:
          Determines whether the x,y coordinates of the "nearest point" of the closest
          arc, point, or node are to be saved as well as the cover# and distance. The new
          items are X-COORD and Y-COORD.

          * NO_LOCATION—The x,y coordinates of the nearest point are not saved. This is
          the default.

          * LOCATION—The x,y coordinates of the nearest point, as well as the cover# and
          distance, will be saved.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created. The <input_cover> is copied to the <output_cover:>,
          then NEAR is performed on the <output_cover:>."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Near_arc(*gp_fixargs((in_cover, near_cover, out_cover, feature_type, search_radius, location), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PointDistance_arc', None)
def PointDistance(from_cover=None, to_cover=None, out_info_table=None, search_radius=None):
    """PointDistance_arc(from_cover, to_cover, out_info_table, {search_radius})

        Computes the point-to-point distance between each point in a coverage to all
        points in the same or another coverage within a specified search radius.

     INPUTS:
      from_cover (Coverage):
          The point coverage for which distances to another coverage's points are to be
          computed.
      to_cover (Coverage):
          The point coverage from which point distances are to be measured. Distances
          between all points in the same coverage can be calculated by specifying the same
          coverage name for both <from_cover> and <to_cover> arguments.
      search_radius {Double}:
          The maximum distance in coverage units a feature can be from the current point
          for consideration as the closest feature. The default value is the diagonal
          width of the from coverage’s BND.

     OUTPUTS:
      out_info_table (INFO Table):
          The INFO data table created by Point Distance, which holds the distance
          measurements. The number of records created in <output Info table:> depends on
          the search radius used, but it can be as large as the number of points in the
          <from cover> times the number of points in the <to cover:>."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PointDistance_arc(*gp_fixargs((from_cover, to_cover, out_info_table, search_radius), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PointNode_arc', None)
def PointNode(point_cover=None, node_cover=None, search_radius=None):
    """PointNode_arc(point_cover, node_cover, {search_radius})

        Performs a spatial JOINITEM on the point coverage and the node coverage. It
        transfers the attributes from a point feature class to a node feature class.
        Each point feature in the point coverage is matched to the corresponding node
        feature in the node coverage. If any point is within the search radius of a
        node, the attributes are copied.

     INPUTS:
      point_cover (Coverage):
          The coverage containing point features to be transferred.
      node_cover (Coverage):
          An existing cover whose node attribute values will be updated or created if the
          NAT does not exist.
      search_radius {Double}:
          The maximum distance apart that points and nodes can be for the attributes of
          the point class to be transferred and recorded to the node coverage as a node
          class. The radius is given in coverage units. The default search radius is the
          width or height of the node coverage's BND divided by 100, whichever is larger."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PointNode_arc(*gp_fixargs((point_cover, node_cover, search_radius), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Thiessen_arc', None)
def Thiessen(in_cover=None, out_cover=None, proximal_tolerance=None):
    """Thiessen_arc(in_cover, out_cover, {proximal_tolerance})

        Converts input coverage points to an output coverage of Thiessen proximal
        polygons.

     INPUTS:
      in_cover (Coverage):
          The coverage that must have a point feature attribute table created by BUILD
          with the POINT option.
      proximal_tolerance {Double}:
          Tolerance used to eliminate Input Coverage points that fall within the specified
          distance of other Input Coverage points. The default Proximal Tolerance is the
          machine precision of the computer.

     OUTPUTS:
      out_cover (Coverage):
          The polygon coverage in which the Thiessen proximal polygons will be produced."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Thiessen_arc(*gp_fixargs((in_cover, out_cover, proximal_tolerance), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\From Coverage toolset
@gptooldoc('ArcDLG_arc', None)
def ArcDLG(in_cover=None, out_dlg_file=None, in_point_cover=None, in_projection_file=None, x_shift=None, y_shift=None, in_header_file=None, transform=None):
    """ArcDLG_arc(in_cover, out_dlg_file, {in_point_cover}, {in_projection_file}, {x_shift}, {y_shift}, {in_header_file}, {transform})

        Creates a Digital Line Graph from a coverage. The DLG is output in DLG-3
        Optional (as opposed to Standard) format.

     INPUTS:
      in_cover (Coverage):
          The coverage to be converted to DLG format. It may contain polygon, line, and
          node features.
      in_point_cover {Coverage}:
          A coverage containing point features to be written as zero length, degenerate
          Line (L) records in the output DLG.
      in_projection_file {File}:
          A text file containing input projection parameters to be saved in the DLG
          header.
      x_shift {Double}:
          A constant value to be added to all coverage x-coordinates during the conversion
          to DLG. X Shift overrides any x-shift parameters found in either projection file
          or input cover projection definition file. If a value for X Shift is not
          specified, the default is zero.
      y_shift {Double}:
          A constant value to be added to all y-coordinates during conversion to DLG. Y
          Shift overrides any y-shift parameters found in either the projection file or
          input cover projection definition file. If a value for Y Shift is not specified,
          the default is zero.
      in_header_file {File}:
          The file containing information to be written into the header of the DLG file.
      transform {Boolean}:
          This operation controls whether a coordinate transformation is performed.
          Usually, coordinates are transformed to preserve accuracy when written to the
          DLG.

          * TRANSFORM—Transforms coordinates in the DLG file

          * NOTRANSFORM—Does not transform coordinates in the DLG file

     OUTPUTS:
      out_dlg_file (File):
          The output DLG-3 Optional format file to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ArcDLG_arc(*gp_fixargs((in_cover, out_dlg_file, in_point_cover, in_projection_file, x_shift, y_shift, in_header_file, transform), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ArcS57_arc', None)
def ArcS57(in_workspace=None, log_file=None, out_workspace=None):
    """ArcS57_arc(in_workspace, log_file, {out_workspace})

        Converts coverages to S-57 object files.

     INPUTS:
      in_workspace (Folder):
          The workspace containing the coverage to be converted (exported).

     OUTPUTS:
      log_file (File):
          Contains the report of the export process.
      out_workspace {Folder}:
          The folder that will contain the S-57 object files."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ArcS57_arc(*gp_fixargs((in_workspace, log_file, out_workspace), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Export_arc', None)
def Export(feature_type=None, in_dataset=None, interchange_file=None, compression_type=None, max_lines=None):
    """Export_arc(feature_type, in_dataset, interchange_file, {compression_type}, {max_lines})

        Converts a coverage to an interchange file for transfer to another platform.

     INPUTS:
      feature_type (String):
          The data type to be exported.

          * COVER—a coverage, associated INFO files, and any index files.

          * FONT—an IGL font file.

          * GRID—an integer or floating-point grid.

          * INFO—an INFO file.

          * LINESET—a lineset file.

          * MAP—a map composition created with the ARCPLOT map composer.

          * MARKERSET—a markerset file.

          * PLOT—a plotfile or graphics file.

          * SHADESET—a shadeset file.

          * STACK—a stack.

          * STACKALL—a stack and all of the grids associated with that stack.

          * TEXT—any ASCII text file.

          * TEXTSET—a textset file.

          * TIN—a tin.
      in_dataset (Data Element):
          The dataset or file to export.
      compression_type {String}:
          Specifies how numbers and blanks will be compressed in the export file. There
          are three options:

          * NONE—No compression is performed. This option can also produce an export file
          that can be listed on your terminal or line printer. This is the default and the
          preferred method for creating export files.

          * PARTIAL—Compresses blanks but does not compress numbers.

          * FULL—Compresses both blanks and numbers using ASCII compression characters.
          This option requires the least amount of storage space (on tape or disk).
      max_lines {Long}:
          Maximum number of lines for each volume (for example, disk file) of an Export To
          Interchange File file. A volume has the extension .E00 through .E99. Only one
          export file is created if this is not specified.

     OUTPUTS:
      interchange_file (File):
          The prefix name of the interchange file or files to be created by Export. A
          volume ID of E00 will be appended to the file name of the first interchange
          file, E01 to the second file, and so on. Each subsequent file is created when
          the {max_lines} for each file is reached."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Export_arc(*gp_fixargs((feature_type, in_dataset, interchange_file, compression_type, max_lines), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SDTSExport_arc', None)
def SDTSExport(SDTS_type=None, in_dataset=None, out_transfer_prefix=None, in_point_cover=None, out_DD_transfer=None, Conv_Ctrl_File=None):
    """SDTSExport_arc(SDTS_type, in_dataset, out_transfer_prefix, {in_point_cover}, {out_DD_transfer}, {Conv_Ctrl_File})

        Creates a Spatial Data Transfer Standard (SDTS). Topological Vector Profile
        (TVP). or Point Profile Transfer from an ArcGIS coverage or grid.

     INPUTS:
      SDTS_type (String):
          The type of SDTS profile that will be created:

          * TVP—Topological Vector Profile, designed specifically for planar vector data
          with coverage topology.

          * POINT—Point profile, designed for high-precision point datasets.

          * RASTER—Raster profile. Grids and lattices are supported.
      in_dataset (Coverage / Raster Dataset):
          The input coverage or grid.
      in_point_cover {Coverage}:
          The name of the Point Coverage to be converted when the transfer type is TVP.
          This option will be ignored if the transfer type is set to POINT.
      Conv_Ctrl_File {File}:
          A file that can be used to add information during translation. The name of this
          file is defined by the user.

     OUTPUTS:
      out_transfer_prefix (String):
          A four-character prefix used to name each file in the transfer. The prefix may
          include a pathname to a directory. By default, the files in the transfer will be
          written to the current workspace.
      out_DD_transfer {String}:
          A four-character prefix for the Master Data Dictionary. A directory named
          MASTERDD will be created at the same directory level as the Out Transfer
          directory. This option is used for creating a single master data dictionary for
          coverages or grids that share a common data dictionary."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SDTSExport_arc(*gp_fixargs((SDTS_type, in_dataset, out_transfer_prefix, in_point_cover, out_DD_transfer, Conv_Ctrl_File), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Ungenerate_arc', None)
def Ungenerate(in_cover=None, out_generate_file=None, feature_type=None, duplicate_nodes=None, format=None):
    """Ungenerate_arc(in_cover, out_generate_file, feature_type, {duplicate_nodes}, {format})

        Creates a text file of x,y coordinates from the input coverage.

     INPUTS:
      in_cover (Coverage):
          The coverage from which feature coordinates will be written.
      feature_type (String):
          The type of features that will be used in the generation of the output file.

          * LINE—Coordinates for arcs will be written.

          * POINT—Coordinates for label points will be written.

          * POLY—Coordinates for arcs and labels that make up polygon features will be
          written.

          * TIC—Coordinates for tics will be written.

          * LINK—Coordinates that define links will be written.

          * REGION.subclass—Coordinates for the regions in the specified subclass will be
          written.

          * ANNO.subclass—Coordinates for the annotation in the specified subclass will be
          written.
      duplicate_nodes {Boolean}:
          Determines whether duplicate node coordinates will be retained or dropped in the
          Output Generate File. This applies only to the POLY option.

          * NODES—Specifies that duplicate node coordinates will be written to the Output
          Generate File. This applies only to the POLY option. This is the default.

          * NONODES—Specifies that duplicate node coordinates will be dropped from the
          Output Generate File. This applies only to the POLY option.
      format {String}:
          Selects either exponential or fixed representation of floating point numbers in
          the Output Generate File.

          * EXPONENTIAL—The coordinates will be written to the Output Generate File in
          exponential notation. This is the default. This option retains all significant
          digits and is recommended to preserve precision.

          * FIXED—The coordinates will be written using approximately seven significant
          digits for single-precision coverages and approximately 15 significant digits
          for double-precision coverages.

     OUTPUTS:
      out_generate_file (File):
          The text file to which the x,y coordinates will be written."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Ungenerate_arc(*gp_fixargs((in_cover, out_generate_file, feature_type, duplicate_nodes, format), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('VPFExport_arc', None)
def VPFExport(in_cover=None, out_file=None, tile_name=None, control_file=None, standard_table=None, index_table=None):
    """VPFExport_arc(in_cover, out_file, {tile_name}, {control_file}, {standard_table}, {index_table})

        Converts a coverage into either a Vector Product Format (VPF) Coverage or VPF
        Tile.

     INPUTS:
      in_cover (Coverage / INFO Table):
          The input coverage that will be converted to VPF format.
      tile_name {String}:
          The name of the VPF tile to be created.
      control_file {File}:
          A file that can be used to drop, add, change, or ignore items and other
          information during translation. The name of this file is defined by the user.
          Polycov.ccf, poly_cov_con, and conversionfile are all acceptable names.An input
          coverage defines feature translations for specified feature classes as
          well as specifies feature classes to be ignored. It can also be used to
          determine which values are to be filled in the database and library header files
          at creation.
      standard_table {Boolean}:
          Specifies whether nonstandard ArcInfo Workstation tables will be converted.

          * EXTRA—Translates all ArcInfo Workstation files to VPF. This option only needs
          to be used if the data being translated to VPF will be converted back using the
          Import From VPF tool. This is the default option.

          * NO_EXTRA—Prevents VPFEXPORT from creating extra tables when creating a VPF
          coverage. This option should only be used if the exported coverage will not be
          imported back using the Import From VPF tool. VPFEXPORT considers files such as
          TIC and LAB to be extra files. These files are not necessary to create a VPF
          coverage.
      index_table {Boolean}:
          Specifies whether to create a feature index table (FIT).

          * NO_FIT—Do not create a feature index table.

          * FIT—Create a feature index table.

     OUTPUTS:
      out_file (Data Element):
          The name of the VPF coverage or table to be created. The full pathname must be
          specified."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.VPFExport_arc(*gp_fixargs((in_cover, out_file, tile_name, control_file, standard_table, index_table), True)))
        return retval
    except Exception, e:
        raise e


# Conversion\To Coverage toolset
@gptooldoc('DLGArc_arc', None)
def DLGArc(in_dlg_file=None, out_cover=None, out_point_cover=None, area_calculation=None, x_shift=None, y_shift=None, category=None):
    """DLGArc_arc(in_dlg_file, out_cover, {out_point_cover}, {area_calculation}, {x_shift}, {y_shift}, {category})

        Converts a Standard or Optional formatted Digital Line Graph (DLG) file to a
        coverage.

     INPUTS:
      in_dlg_file (File):
          The DLG file to be converted to a coverage.
      area_calculation {String}:
          Determines how the area (A) records are written to the output coverage.

          * NOFIRST—The first area record is ignored. Labels are written for all other
          area records and the corresponding major/minor codes are written to the Output
          Coverage.PCODE file. This is the default option.

          * ALL—All area records are converted to output coverage label points and the
          major and minor codes for all area (A) records in the Output Coverage.PCODE
          file. Usually the label point for the first area record is in the outside
          polygon.

          * ATTRIBUTED—The label location in the DLG file is used only for those area
          records that carry major/minor codes. For some DLG categories, only area records
          with attributes have valid label locations. The first area (A) record is not
          included.
      x_shift {Double}:
          A constant value to be added to all x coordinates during DLG conversion. The
          default X Shift value is zero.
      y_shift {Double}:
          A constant value to be added to all y coordinates during DLG conversion. The
          default Y Shift value is zero.
      category {String}:
          The optional name of a specific DLG category to be converted from the DLG file.
          Only the specified category will be converted if one is given. Otherwise, only
          the first category in the DLG will be written to the output coverages: output
          coverage, point coverage.

     OUTPUTS:
      out_cover (Coverage):
          The name of the coverage to be created from the DLG data. If the input DLG file
          contains data produced by the United States Geological Survey (USGS), the output
          coverage will usually contain line, polygon, and node features created from
          nondegenerate line (L) records, area (A) records, and node (N) records. An
          Output Coverage.NAT for node features will be created.This is the only feature
          attribute table that is created by Import From DLG.An INFO table named Output
          Coverage.ACODE will be created that contains the
          major/minor pair values for all line (L) records. Similarly, an INFO table named
          Output Coverage.PCODE will store the major/minor codes for area (A) records.
      out_point_cover {Coverage}:
          The name of an Optional point coverage to be created from degenerate line (L)
          records in the DLG. In a DLG, points are stored as zero-length arcs (that is,
          degenerate lines).These are optionally converted to points by specifying an
          output point coverage.
          An INFO table named Output Point Coverage.XCODE will be created, which contains
          all major and minor code pair values for degenerate line (L) records.No coverage
          will be created from degenerate line records unless an Output Point
          Coverage is specified."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DLGArc_arc(*gp_fixargs((in_dlg_file, out_cover, out_point_cover, area_calculation, x_shift, y_shift, category), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Generate_arc', None)
def Generate(in_file=None, out_cover=None, feature_type=None):
    """Generate_arc(in_file, out_cover, feature_type)

        Generates a coverage from coordinates stored in a file.

     INPUTS:
      in_file (File):
          The file containing feature coordinates that will be used to generate a
          coverage.
      feature_type (String):
          The type of features to create:

          * ANNOTATIONS—Adds annotations to the coverage.

          * CIRCLES—Generates circles, each with a specified center and radius.

          * CURVES—Generates curves using the specified grain value as the distance
          between vertices on each curve.

          * FISHNET—Creates a fishnet of rectangular cells.

          * LINES—Adds arcs to the coverage.

          * LINKS—Adds links to the coverage.

          * POINTS—Adds label points to the coverage.

          * POLYGONS—Adds polygons and label points to the coverage.

          * TICS—Adds tics to the coverage.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Generate_arc(*gp_fixargs((in_file, out_cover, feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Import_arc', None)
def Import(feature_type=None, interchange_file=None, out_dataset=None):
    """Import_arc(feature_type, interchange_file, out_dataset)

        Converts an ArcInfo Workstation export interchange file.An ArcInfo Workstation
        interchange file can be used to transport coverages; INFO
        tables; text files, such as AML macros; and other ArcInfo Workstation files
        between various machine types. An interchange file contains all coverage
        information and appropriate INFO table information in a fixed-length ASCII
        format.There are many ways to use Import From Interchange. One way is to
        transport a
        coverage and its associated INFO tables. Each coverage file and its INFO tables
        are read from the interchange file into an output coverage. This is done by
        using the keyword COVER for the first argument. Another way is to transfer an
        INFO table. In this case, any INFO path name/user name can be used to specify
        the name of the output INFO table. This option is invoked by using the keyword
        INFO for the first argument. A third way is to use Import with the TEXT option
        to transfer key files, AML macros, and other text files.If multiple volumes are
        provided by Export To Interchange, the ASCII interchange
        file name for Import from Interchange must be in the format
        <interchange_file>.E00 through <interchange_file>.Enn, where nn is the last
        volume ID. Even if only one volume is produced, this file name must have the
        .E00 extension.

     INPUTS:
      feature_type (String):
          The type of file to be imported. Auto is the default option.

          * AUTO—

          * COVER—

          * FONT—

          * GRID —

          * INFO—

          * LINESET—

          * PLOT—

          * MAP—

          * MARKERSET—

          * SHADESET—

          * STACK—

          * TEXT—

          * TEXTSET—

          * TIN—
      interchange_file (File):
          The prefix name of the ArcInfo Workstation interchange file to be converted. A
          volume ID of .e00, .e01, and so on, will always be appended to the given
          interchange_file to specify the file or files to be imported.

     OUTPUTS:
      out_dataset (Data Element):
          The name of the output dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Import_arc(*gp_fixargs((feature_type, interchange_file, out_dataset), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('S57Arc_arc', None)
def S57Arc(in_s57_file=None, out_workspace=None, clean=None):
    """S57Arc_arc(in_s57_file, out_workspace, {clean})

        Converts data from S-57 format to one or more coverages.

     INPUTS:
      in_s57_file (File):
          The data catalog filename or base cell filename in the S-57 exchange set. If a
          catalog filename is specified, all base cell files listed in the catalog file
          will be converted. If a base cell filename is specified, only that base cell
          file will be converted.
      clean {Boolean}:
          Specifies whether to run the Clean command.

          * CLEAN—Cleans the newly created coverages. This is the default.

          * NO_CLEAN—Does not clean the newly created coverages.

     OUTPUTS:
      out_workspace (Folder):
          The workspace where all output coverages will be written."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.S57Arc_arc(*gp_fixargs((in_s57_file, out_workspace, clean), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SDTSImport_arc', None)
def SDTSImport(in_transfer_prefix=None, output=None, out_point_cover=None, layer_name=None, data_dictionary=None, convert_void=None):
    """SDTSImport_arc(in_transfer_prefix, output, {out_point_cover}, {layer_name}, {data_dictionary}, {convert_void})

        Creates ArcGIS coverages or grids from a Spatial Data Transfer Standard (SDTS)
        Topological Vector Profile (TVP) or Point Profile Transfer.

     INPUTS:
      in_transfer_prefix (String):
          A four-character prefix common to all files in the SDTS transfer. The prefix may
          include a pathname to a directory. If no directory pathname is given, the files
          in the transfer will be read from the current workspace.
      layer_name {String}:
          The name of an aggregated spatial object that represents a single data layer in
          a transfer. There can be multiple layers in a single transfer. By default, the
          first layer encountered is the only one that will be converted.
      data_dictionary {Boolean}:
          Option to retain or drop the data dictionary.

          * DD—Retain the data dictionary.

          * DROP_DD—Discard the data dictionary.
      convert_void {Boolean}:
          Used to convert or preserve void and fill values in the raster transfer. In the
          raster profile, NULL values are defined in two general categories: (Undefined,
          not relevant) or (Relevant but unknown or missing).

          * CONVERT—Convert void and fill values in the raster transfer.

          * PRESERVE—Preserve void and fill values in the raster transfer.

     OUTPUTS:
      output (Data Element):
          The coverage or grid to be created.
      out_point_cover {Coverage}:
          The name of an optional point coverage to be created when the Topological Vector
          Profile is converted. This option is ignored if the SDTS dataset is not the
          Point Profile Transfer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SDTSImport_arc(*gp_fixargs((in_transfer_prefix, output, out_point_cover, layer_name, data_dictionary, convert_void), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TigerArc_arc', None)
def TigerArc(in_tiger_file_prefix=None, out_cover=None, out_point_cover=None, out_landmark_cover=None, tiger_version=None):
    """TigerArc_arc(in_tiger_file_prefix, out_cover, {out_point_cover}, {out_landmark_cover}, {tiger_version})

        Converts a set of U.S. Bureau of Census TIGER/Line files into one or more
        coverages.

     INPUTS:
      in_tiger_file_prefix (String):
          The filename prefix, common to all files in the set of TIGER/Line files being
          converted. The prefix may include a directory path.
      tiger_version {String}:
          The input TIGER/Line files version.

          * 1995—

          * 1997—

          * 1998—

          * 1999—

          * 2000—

          * 2002—

          * 2003—

          * 20041—

          * 20042—

          * 20051—

          * 20052—

     OUTPUTS:
      out_cover (Coverage):
          The name of the output coverage to be created containing the basic line features
          and attribute data from the set of TIGER/Line files.
      out_point_cover {Coverage}:
          The name of the output coverage that contains point features that represent
          polygon label points for polygons in out_cover.
      out_landmark_cover {Coverage}:
          The name of the output point coverage containing landmark features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TigerArc_arc(*gp_fixargs((in_tiger_file_prefix, out_cover, out_point_cover, out_landmark_cover, tiger_version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TigerTool_arc', None)
def TigerTool(in_tiger_file_prefix=None, out_cover_prefix=None, join_attributes=None, projection=None, zone_number=None, tiger_version=None, restart=None):
    """TigerTool_arc(in_tiger_file_prefix, out_cover_prefix, {join_attributes}, {projection}, {zone_number}, {tiger_version}, {restart})

        Converts a set of U.S. Census Bureau TIGER/Line files to a set of coverages.

     INPUTS:
      in_tiger_file_prefix (String):
          The filename prefix, common to all files in the set of TIGER/Line files being
          converted. The prefix may include a directory pathname.
      join_attributes {Boolean}:
          Determines if the basic line, area, and landmark point features will be joined
          to their feature attribute tables.

          * JOIN—The output features will be joined to their feature attribute tables.

          * NO_JOIN—The output features will not be joined to their feature attribute
          tables.
      projection {String}:
          The spatial reference of the output coverages.

          * UTM—TIGER files will be projected to the Universal Transverse Mercator (UTM)
          coordinate system.

          * STATE—TIGER files will be projected to the State Plane coordinate system.
      zone_number {Long}:
          The zone number of the specified coordinate system.
      tiger_version {String}:
          The input TIGER/Line files version.

          * 1995—

          * 1997—

          * 1998—

          * 1999—

          * 2000—

          * 2002—

          * 2003—

          * 20041—

          * 20042—

          * 20051—

          * 20052—
      restart {Boolean}:
          Determines whether processing will continue if the TIGER data contains
          intersection errors.

          * RESTART—Processing will continue if the TIGER data contains intersection
          errors.

          * NO_RESTART—Processing will stop if the TIGER data contains intersection
          errors.

     OUTPUTS:
      out_cover_prefix (String):
          The prefix of the output coverages to be created from the TIGER/Line files."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TigerTool_arc(*gp_fixargs((in_tiger_file_prefix, out_cover_prefix, join_attributes, projection, zone_number, tiger_version, restart), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('VPFImport_arc', None)
def VPFImport(input_vpf=None, output=None, tile_name=None, control_file=None, standard_vpf=None):
    """VPFImport_arc(input_vpf, output, {tile_name}, {control_file}, {standard_vpf})

        Converts a VPF table to an INFO table, or converts either an untiled VPF
        coverage or VPF tile to an ArcGIS coverage.

     INPUTS:
      input_vpf (VPF Coverage / VPF Table):
          The name of the VPF table, untiled coverage, or tile to be converted. The full
          pathname must be specified.
      tile_name {String}:
          The input VPF tile, if one exists.
      control_file {File}:
          A file that can be used to ignore specific VPF feature classes or three-
          dimensional coordinates during translation. The name of this file is defined by
          the user.
      standard_vpf {Boolean}:
          Specifies whether nonstandard VPF tables will be converted.

          * NO_EXTRA—This option prevents VPFImport from importing extra tables created
          using VPFExport. This is the default.

          * EXTRA—This option only needs to be used if the data being translated was
          converted to VPF using VPFExport.

     OUTPUTS:
      output (Data Element):
          The output table or coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.VPFImport_arc(*gp_fixargs((input_vpf, output, tile_name, control_file, standard_vpf), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Aggregate toolset
@gptooldoc('Append_arc', None)
def Append(in_covers=None, out_cover=None, append_method=None, feature_classes=None, number_method=None):
    """Append_arc(in_covers;in_covers..., out_cover, {append_method}, {feature_classes;feature_classes...}, {number_method})

        Combines an unlimited number of coverages into a single coverage.Append checks
        for the existence of the coverage, verifies that the list of
        feature attribute table items matches the items in previously entered coverages
        (unless the FEATURES_ONLY option is used), and calculates Tic-ID and feature
        User-ID offsets according to the specified offset option.

     INPUTS:
      in_covers (Coverage):
          The input coverages to be appended. There is no limit to the number of coverages
          that can be entered.
      append_method {String}:
          Determines whether only coordinates will be appended (FEATURES_ONLY) or if
          features will also be appended.

          * FEATURES_ONLY—Location information for all feature classes that are appended.
          Feature attribute tables are not appended.

          * FEATURES_ATTRIBUTES—The features in the specified coverage define the set of
          features to be appended.
      feature_classes {String}:
          The feature class of the input coverage or coverages.

          * POLY—Polygon feature coordinates and attributes are appended, including label
          points.

          * LINE—Arc feature coordinates and attributes are appended.

          * POINT—Point feature coordinates and attributes are appended.

          * NODE—Arc and node feature coordinates and their attributes are appended.

          * NET—Arc and polygon feature coordinates and their attributes are appended.

          * LINK—Arc and point feature coordinates and their attributes are appended.

          * ANNO.subclass—Annotation features and attributes of the subclass are appended.

          * SECTION.subclass—Section feature coordinates and attributes of the subclass
          are appended.

          * ROUTE.subclass—Route and section feature coordinates and attributes of the
          subclass are appended.

          * REGION.subclass—Region feature coordinates and attributes of the subclass are
          appended. Polygon feature coordinates and attributes are also appended.
          The Add Value button, which is used only in ModelBuilder, allows you to add
          expected value(s) so you can complete the dialog and continue to build your
          model.
      number_method {String}:
          Specifies how tics and coverage features will be numbered in the Output
          Coverage. IDs can be offset to ensure unique ID values for Output Coverage
          features. The ID offset is equal to 1 plus the highest ID value in the
          previously appended coverages. Offsets can be calculated for the following types
          of IDs:

          * NO—Neither Tic-IDs nor feature User-IDs will be modified. This is the default
          option.

          * TICS_ONLY—ID offsets will be calculated for tics.

          * FEATURES_ONLY—User-ID offsets will be calculated for the feature class(es)
          specified by the feature classes argument. Tic-IDs are not modified.

          * FEATURES_TICS—ID offsets will be calculated for both tics and features.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage to be created. The output coverage cannot already exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Append_arc(*gp_fixargs((in_covers, out_cover, append_method, feature_classes, number_method), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Composite Features toolset
@gptooldoc('ArcRoute_arc', None)
def ArcRoute(in_cover=None, out_route_system=None, in_route_item=None, out_route_item=None, measure_item=None, coordinate_priority=None, use_blanks=None):
    """ArcRoute_arc(in_cover, out_route_system, {in_route_item}, {out_route_item}, {measure_item}, {coordinate_priority}, {use_blanks})

        Creates a route system by creating whole arc sections for each arc in the input
        coverage and can also be used to append arcs to an existing route system.

     INPUTS:
      in_cover (Coverage):
          The coverage from which the routes are to be created.
      out_route_system (String):
          The name of the route system to be created or appended.
      in_route_item {INFO Item}:
          The name of an item in the arc attribute table used to group arcs into separate
          routes. A new route is created in the route attribute table for each unique
          value in this item. The default is to create a route for each topologically
          connected set of arcs.
      out_route_item {String}:
          The name of the new item in the route attribute table that will contain the
          unique values in the input route item. When appending routes to an existing
          route system, it is an existing item in the route attribute table used to append
          routes. The default item is Input Route Item.
      measure_item {INFO Item}:
          An item in the arc attribute table of Input Coverage whose value is accumulated
          to produce the measure values. The default item is LENGTH.
      coordinate_priority {String}:
          Determines coordinate priority when choosing a start node for the route.

          * UL—Upper left. This is the default.

          * UR—Upper right.

          * LL—Lower left.

          * LR—Lower right.
      use_blanks {Boolean}:
          Specifies whether arcs having a null or 0 value for the input route item will be
          used to create a route.

          * BLANK—Arcs having a null or 0 value for the Input Route Item will be used to
          create routes. This is the default.

          * NOBLANK—Arcs having a null or 0 value for the Input Route Item will not be
          used to create routes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ArcRoute_arc(*gp_fixargs((in_cover, out_route_system, in_route_item, out_route_item, measure_item, coordinate_priority, use_blanks), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PolyRegion_arc', None)
def PolyRegion(in_cover=None, out_cover=None, out_subclass=None):
    """PolyRegion_arc(in_cover, out_cover, out_subclass)

        Converts polygons to regions in a one-to-one mapping in a region subclass.Each
        polygon in the Input Coverage becomes a region in the Output Subclass.
        Attributes in the polygon attribute table (PAT) are copied to the corresponding
        region PATsubclass. The Output Coverage can be the same as the Input Coverage;
        if so, the Output Subclass is then created in the Input Coverage.

     INPUTS:
      in_cover (Coverage):
          The polygon coverage to be converted to a region subclass. Each polygon of the
          <in_cover> is made into a region.
      out_subclass (String):
          The name of the region subclass that will be created.

     OUTPUTS:
      out_cover (Coverage):
          The coverage that will contain the new subclass."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PolyRegion_arc(*gp_fixargs((in_cover, out_cover, out_subclass), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RegionClass_arc', None)
def RegionClass(in_cover=None, out_cover=None, out_subclass=None, in_region_item=None, out_region_item=None, selection_file=None, method=None):
    """RegionClass_arc(in_cover, {out_cover}, out_subclass, {in_region_item}, {out_region_item}, {selection_file}, {method})

        Converts arcs to preliminary regions in a new or existing coverage or appends
        preliminary regions to an existing region subclass.Arcs are grouped into
        preliminary regions based on the unique value of the Line
        item and must form closed loops. The unique values are saved in the output
        subclass Region item.

     INPUTS:
      in_cover (Coverage):
          The coverage containing the arcs from which the preliminary regions are created.
      out_subclass (String):
          The name of the region subclass to be created or appended.
      in_region_item {INFO Item}:
          Item in the AAT of the input coverage whose values are used to group arcs into
          preliminary regions. The item is appended to the region PATsubclass. If not
          specified, each group of arcs becomes a preliminary region.
      out_region_item {String}:
          Output name for the input region Item to be used in the region PATsubclass
          instead of the Input Region Item name.
      selection_file {File}:
          The name of a selection file that can be used to specify a subset of the arcs to
          be grouped into preliminary regions.
      method {String}:
          Determines whether regions will be created from multiple rings of arcs or single
          rings of arcs.

          * MULTIRING—Creates regions from multiple rings of arcs whose values for the
          input region item are identical.

          * SINGLERING—Each ring of arcs becomes a region.

     OUTPUTS:
      out_cover {Coverage}:
          The coverage that will contain the preliminary regions. If the output coverage
          is not specified, the preliminary regions are created in the input coverage."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RegionClass_arc(*gp_fixargs((in_cover, out_cover, out_subclass, in_region_item, out_region_item, selection_file, method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RegionPoly_arc', None)
def RegionPoly(in_cover=None, out_cover=None, in_subclass=None, out_table=None):
    """RegionPoly_arc(in_cover, out_cover, in_subclass, {out_table})

        Converts a region subclass to a polygon coverage and creates an INFO table
        containing overlapping region information.

     INPUTS:
      in_cover (Coverage):
          The coverage containing the region subclass to convert to polygons.
      in_subclass (String):
          The region subclass of the Input Coverage that will be converted to a polygon
          coverage.

     OUTPUTS:
      out_cover (Coverage):
          The polygon coverage to be created from the Input Subclass. The coverage may not
          already exist.
      out_table {INFO Table}:
          The output INFO table that will contain information for regions associated with
          each polygon."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RegionPoly_arc(*gp_fixargs((in_cover, out_cover, in_subclass, out_table), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Generalization toolset
@gptooldoc('AggregatePolygons_arc', None)
def AggregatePolygons(in_cover=None, out_cover=None, cell_size=None, distance=None, orthogonal_option=None):
    """AggregatePolygons_arc(in_cover, out_cover, cell_size, distance, {orthogonal_option})

        Combines disjoint and adjacent polygons into new area features based on a
        distance.

     INPUTS:
      in_cover (Coverage):
          The coverage containing polygons to be aggregated.
      cell_size (Double):
          Sets cell size in coverage units for grid conversion. Cell size must be greater
          than 0.
      distance (Double):
          Sets the aggregation distance in coverage units. A distance must be equal to or
          greater than the cell size.
      orthogonal_option {Boolean}:
          Specifies the characteristic of the input features that will be preserved when
          constructing the aggregated boundaries.

          * NON_ORTHOGONAL—Specifies natural features, such as vegetation or soil
          polygons, which unlikely contain orthogonal shapes. This is the default.

          * ORTHOGONAL—Specifies building-like features for which orthogonal shapes will
          be preserved and constructed.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage containing aggregated features as preliminary regions with a
          subclass AREAAGG. The output coverage name must be different from the input
          coverage name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AggregatePolygons_arc(*gp_fixargs((in_cover, out_cover, cell_size, distance, orthogonal_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CollapseDualLinesToCenterline_arc', None)
def CollapseDualLinesToCenterline(in_cover=None, out_cover=None, maximum_width=None, minimum_width=None):
    """CollapseDualLinesToCenterline_arc(in_cover, out_cover, maximum_width, {minimum_width})

        Derives centerlines (single lines) from dual-line features, such as road
        casings, based on specified width tolerances.

     INPUTS:
      in_cover (Coverage):
          The coverage containing near parallel dual lines, such as road casings, from
          which centerlines are derived.
      maximum_width (Double):
          Sets the maximum width in coverage units.
      minimum_width {Double}:
          Sets the minimum width in coverage units. The default is zero.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage containing the derived centerlines. The output coverage name
          must be different from the input coverage name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CollapseDualLinesToCenterline_arc(*gp_fixargs((in_cover, out_cover, maximum_width, minimum_width), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Dissolve_arc', None)
def Dissolve(in_cover=None, out_cover=None, dissolve_item=None, feature_type=None):
    """Dissolve_arc(in_cover, out_cover, dissolve_item, {feature_type})

        Creates a new coverage by merging adjacent polygons, lines, or regions that have
        the same value for a specified item.

     INPUTS:
      in_cover (Coverage):
          The coverage containing features to be dissolved.
      dissolve_item (String):
          The item in the in_cover feature attribute table that is used to dissolve
          features.

          * Dissolve_item—An item name will be used to perform the dissolve. The item may
          be a redefined item.

          * #ALL—All items past the cover-ID in the PAT, AAT, or region subclass PAT will
          be used as a single dissolve item. If there are no items past the cover-ID, then
          the cover-ID will be used.
      feature_type {String}:
          The feature classes to be preserved in the output coverage:

          * POLY—Polygons will be dissolved; an AAT will not be created for the output
          coverage. This is the default option.

          * LINE—Nodes will be dissolved; a PAT will not be created for the output
          coverage.

          * NET—Polygons will be dissolved, and both a PAT and AAT will be created for the
          output coverage.

          * REGION.subclass—Region subclass will be dissolved, and all existing attributes
          of the input coverage will be maintained in the output coverage.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created. The output coverage cannot already exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Dissolve_arc(*gp_fixargs((in_cover, out_cover, dissolve_item, feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Eliminate_arc', None)
def Eliminate(in_cover=None, out_cover=None, info_express=None, polygon_boundary=None, feature_type=None, selection_file=None, polygon_option=None):
    """Eliminate_arc(in_cover, out_cover, info_express;info_express..., {polygon_boundary}, {feature_type}, {selection_file}, {polygon_option})

        Merges the selected polygons with neighboring polygons if they have the largest
        shared border or the largest area.Eliminate is often used to remove sliver
        polygons created during polygon overlay
        or buffering. With the LINE option, Eliminate merges selected arcs separated by
        pseudo nodes into single arcs.

     INPUTS:
      in_cover (Coverage):
          The coverage whose selected polygons or arcs will be merged into neighboring
          features.
      info_express (INFO Expression):
          An INFO query containing one or more logical expressions to select features from
          the input coverage.

          * Reselect—Reduces the selected set of records with a selection expression to
          those that meet its criteria. If no selection expression follows, the selected
          set will be empty.

          * Aselect—Adds unselected records that meet the selection expression criteria to
          the currently selected set. If no selection expression follows, the selected set
          will contain all features.

          * Nselect—Reverses the current selection to the unselected set.
      polygon_boundary {Boolean}:
          Ensures that polygons along the coverage boundary are not altered.

          * NO_KEEP_EDGE—Allows the elimination of outer polygon boundaries. This is the
          default.

          * KEEP_EDGE—Is only used with the POLYGON option. Any polygon which is a
          neighbor of the background polygon will not be eliminated when KEEP_EDGE is
          specified.
      feature_type {String}:
          The feature class(es) to be eliminated in the Output Coverage. This parameter is
          only used for polygon coverages.

          * POLY—Polygon features will be eliminated; an AAT will not be created for the
          Output Coverage.

          * LINE—Line features will be eliminated; a PAT will not be created for the
          Output Coverage.
      selection_file {File}:
          A Selection File is a preexisting file that identifies which features will be
          used.
      polygon_option {Boolean}:
          Specifies which method will be used for eliminating polygons. This parameter is
          only used for polygon coverages.

          * BORDER—Merges a selected polygon with a neighboring unselected polygon by
          dropping an Arc. The neighboring polygon is the one with the longest shared
          border. This is the default and the way Eliminate worked with the POLY option in
          all pre-6.1.1 releases.

          * AREA—Merges a selected polygon with a neighboring unselected polygon by
          dropping an Arc. The neighboring polygon is the one with the largest area.

     OUTPUTS:
      out_cover (Coverage):
          The new coverage with all the selected sliver polygons merged into larger
          features. There should be a smaller number of polygons than the Input Coverage
          contains."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Eliminate_arc(*gp_fixargs((in_cover, out_cover, info_express, polygon_boundary, feature_type, selection_file, polygon_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FindConflicts_arc', None)
def FindConflicts(in_cover=None, out_cover=None, conflict_distance=None):
    """FindConflicts_arc(in_cover, out_cover, conflict_distance)

        Finds where simplified buildings overlap or are too close to each other, based
        on a specified distance.

     INPUTS:
      in_cover (Coverage):
          The input coverage containing buildings as regions, with the subclass BLDGSIM
          and the item BDS-GROUP, obtained by the Simplify Building tool followed by the
          Clean tool with the POLY option.
      conflict_distance (Double):
          Sets the conflict distance in coverage units. Buildings within this distance are
          considered in spatial conflict. The distance must be greater than 0.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage containing overlapping region buffers, with a subclass BUF,
          that show spatial conflicts among buildings. This coverage will only be created
          when conflicts are found. The <out_cover> name must be different from the
          <in_cover> name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FindConflicts_arc(*gp_fixargs((in_cover, out_cover, conflict_distance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimplifyBuilding_arc', None)
def SimplifyBuilding(in_cover=None, out_cover=None, simplification_tolerance=None, minimum_area=None, selection_file=None, CheckConflict=None):
    """SimplifyBuilding_arc(in_cover, out_cover, simplification_tolerance, {minimum_area}, {selection_file}, {CheckConflict})

        Simplifies the boundary or footprint of building polygons while maintaining
        their essential shape and size.

     INPUTS:
      in_cover (Coverage):
          The input coverage containing building polygons.
      simplification_tolerance (Double):
          Sets the simplification tolerance in coverage units. A tolerance must be
          specified and must be greater than zero.
      minimum_area {Double}:
          Sets the minimum area to be retained in coverage units. The default is the
          square of the simplification tolerance. Enter 0 to include all buildings.
      selection_file {File}:
          A special file created using the ArcPlot command WRITESELECT (see ArcInfo
          Workstation Help for command reference). It identifies coverage features
          selected in ArcPlot. This option allows you to simplify selected buildings in
          the input coverage.
      CheckConflict {Boolean}:
          Specifies whether or not to check for potential conflicts, that is, overlapping
          or touching, among buildings.

          * NOT_CHECK—Specifies not to check for potential conflicts; the resulting
          buildings may overlap.

          * CHECK_CONFLICT—Specifies to check for potential conflicts so that some of the
          conflicts can be avoided and flagged.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage containing simplified buildings as preliminary regions with
          a subclass BLDGSIM. The output coverage name must be different from the input
          coverage name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimplifyBuilding_arc(*gp_fixargs((in_cover, out_cover, simplification_tolerance, minimum_area, selection_file, CheckConflict), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimplifyLineOrPolygon_arc', None)
def SimplifyLineOrPolygon(in_cover=None, out_cover=None, simplification_tolerance=None, simplification_operator=None, ErrorCheck=None):
    """SimplifyLineOrPolygon_arc(in_cover, out_cover, simplification_tolerance, {simplification_operator}, {ErrorCheck})

        Simplifies a line or a polygon boundary by removing small fluctuations or
        extraneous bends from it while preserving its essential shape.

     INPUTS:
      in_cover (Coverage):
          The coverage containing arcs or polygons to be simplified.
      simplification_tolerance (Double):
          Sets the tolerance in coverage units. A tolerance must be specified and must be
          greater than zero.
      simplification_operator {String}:
          Specifies the simplification operator.

          * POINT_REMOVE—Uses the Douglas-Peucker algorithm for line simplification with
          enhancements. This operator is the default.

          * BEND_SIMPLIFY—Detects and removes extraneous bends from the original line.
      ErrorCheck {Boolean}:
          Specifies whether to check for topological errors, including line-crossing,
          line-overlapping, zero-length lines, collapsed polygons, and holes falling
          outside of polygons.

          * NO_ERROR_CHECK—Specifies to not check for topological errors. This is the
          default.

          * ERROR_CHECK—Specifies to check for topological errors.

     OUTPUTS:
      out_cover (Coverage):
          The coverage to be created. The output coverage name must be different from the
          input coverage name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimplifyLineOrPolygon_arc(*gp_fixargs((in_cover, out_cover, simplification_tolerance, simplification_operator, ErrorCheck), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Indexes toolset
@gptooldoc('DropIndex_arc', None)
def DropIndex(in_info_table=None, index_item=None):
    """DropIndex_arc(in_info_table, {index_item;index_item...})

        Drops an attribute index from the specified item and INFO table.

     INPUTS:
      in_info_table (INFO Table):
          The name of the INFO table containing the item whose index is to be deleted.
      index_item {INFO Item}:
          Selects the item indexes from the input INFO table to be removed. If no Index
          Item is given, all item indexes for the file will be dropped.The Add Item
          button, which is used only in ModelBuilder, allows you to add
          expected items so you can complete the dialog and continue to build your model."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DropIndex_arc(*gp_fixargs((in_info_table, index_item), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IndexItem_arc', None)
def IndexItem(in_info_table=None, index_item=None):
    """IndexItem_arc(in_info_table, index_item)

        Creates an attribute index to increase access speed to the specified item during
        query operations.

     INPUTS:
      in_info_table (INFO Table):
          The name of the INFO table containing the item to be indexed
      index_item (INFO Item):
          The name of the item to be indexed"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IndexItem_arc(*gp_fixargs((in_info_table, index_item), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Items toolset
@gptooldoc('AddItem_arc', None)
def AddItem(in_info_table=None, out_info_table=None, item_name=None, item_width=None, output_width=None, item_type=None, decimal_places=None, start_item=None):
    """AddItem_arc(in_info_table, out_info_table, item_name, item_width, output_width, item_type, {decimal_places}, {start_item})

        Adds a new blank or zero item to a new or existing INFO table.

     INPUTS:
      in_info_table (INFO Table):
          The INFO table to which the item is to be added.
      item_name (String):
          The new item to be added to the INFO table.
      item_width (Long):
          The INFO width of the added item. Supported widths:

          * BINARY—Either 2 or 4 bytes

          * CHARACTER—1 to 320 characters

          * DATE—Always 8 bytes; stored as mm/dd/yy

          * FLOATING—Either 4 bytes (single precision) or 8 bytes (double precision)

          * NUMERIC—1 to 16 digits

          * INTEGER—1 to 16 digits
      output_width (Long):
          The output width of the added item. This is the number of characters used to
          display an item value.For example, in a 2-byte integer (item type BINARY),
          values can be as high as
          32767, which requires five characters for display. Dates can be displayed using
          eight (mm/dd/yy) or ten (mm/dd/yyyy) characters. For international date
          displays, months and days can be switched (for example, dd/mm/yy).
      item_type (String):
          The INFO item type of the added item.

          * BINARY—Binary integer; requires less storage than integer

          * CHARACTER—Text

          * DATE—Date; stores day, month, and year

          * FLOATING—Floating-point binary number, either single or double precision

          * NUMERIC—Decimal number stored as one byte per digit

          * INTEGER—Integer number stored as one byte per digit
      decimal_places {Long}:
          The number of decimal places for the added item. This needs to be specified for
          INFO item types NUMERIC and FLOATING.
      start_item {INFO Item}:
          The item in the in_info_table after which the new item is to be added. The
          default start_item is the last item in the in_info_table.

     OUTPUTS:
      out_info_table (INFO Table):
          The INFO table to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddItem_arc(*gp_fixargs((in_info_table, out_info_table, item_name, item_width, output_width, item_type, decimal_places, start_item), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DropItem_arc', None)
def DropItem(in_info_table=None, out_info_table=None, drop_item=None):
    """DropItem_arc(in_info_table, out_info_table, drop_item;drop_item...)

        Deletes one or more items from an INFO table.

     INPUTS:
      in_info_table (INFO Table):
          The INFO table containing the items to be dropped.
      drop_item (INFO Item):
          The item or items to be dropped from the input table.

     OUTPUTS:
      out_info_table (INFO Table):
          The INFO table to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DropItem_arc(*gp_fixargs((in_info_table, out_info_table, drop_item), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Joins toolset
@gptooldoc('JoinItem_arc', None)
def JoinItem(in_info_table=None, join_info_table=None, out_info_table=None, relate_item=None, start_item=None, relate_type=None):
    """JoinItem_arc(in_info_table, join_info_table, out_info_table, relate_item, {start_item}, {relate_type})

        Joins the item definitions and values of two tables based on a shared item.
        Joining involves appending items (fields) of one table to those of another
        through an attribute or item common to both tables. A join is usually used to
        attach more attributes to the attribute table of a geographic layer.A record in
        the Join Info Table is matched to each record of the Input Info
        Table when the Relate Item and Start Item values are equal. The item values from
        the two records are copied to the output table.

     INPUTS:
      in_info_table (INFO Table):
          The INFO data file to which items and their values are to be added.
      join_info_table (INFO Table):
          The INFO data file that contains the items and values to be added.
      relate_item (String):
          An item contained in the Input Info Table that is used as an index to records in
          the Join Info Table. This can be a redefined item.
      start_item {String}:
          The item in the Input Info Table list after which the Join Info Table items will
          be inserted. The default Start Item is the last item in the Input Info Table.
      relate_type {String}:
          How Join Info Table records are matched to Input Info Table records.

          * LINEAR—The values written to the Output Info Table are merged from the Input
          Info Table and Join Info Table records with matching Relate Item values. The
          Relate Item must exist for both files. Both files can be sorted in any order.
          This is the default option.

          * ORDERED—The Join Info Table must be sorted on Relate Item. Both the Join Info
          Table and Input Info Table must contain the Relate Item.

          * LINK—Only the Input Info Table must contain Relate Item. The Input Info Table
          can be sorted in any order. The Relate Item value in each record of the Input
          Info Table indicates the record number in the Join Info Table that is to be
          merged. This method is used when relating an INFO file to another file on the
          basis of its internal record number.

     OUTPUTS:
      out_info_table (INFO Table):
          The INFO data file produced by Join Info Tables. If Output Info Table already
          exists, it will be replaced."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.JoinItem_arc(*gp_fixargs((in_info_table, join_info_table, out_info_table, relate_item, start_item, relate_type), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Projections toolset
@gptooldoc('DefineProjection_arc', None)
def DefineProjection(in_cover=None, projection_file=None):
    """DefineProjection_arc(in_cover, projection_file)

        Records the coordinate system information of the Input Coverage including any
        associated projection parameters, such as datum and spheroid.It creates or
        modifies the Input Coverage's projection definition file (PRJ)
        that stores the projection parameters.

     INPUTS:
      in_cover (Coverage):
          The coverage for which the projection information is being defined.
      projection_file (File):
          The name of a text file defining the input projection parameters."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DefineProjection_arc(*gp_fixargs((in_cover, projection_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Project_arc', None)
def Project(in_cover=None, out_cover=None, projection_file=None):
    """Project_arc(in_cover, out_cover, projection_file)

        Changes the coordinate system of your coverage including its datum or spheroid.

     INPUTS:
      in_cover (Coverage):
          The coverage whose coordinates are to be converted.
      projection_file (File):
          The name of a text file defining the input and output projection parameters.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage whose coordinates have been converted to the new coordinate
          system. The output coverage may exist, but must be empty."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Project_arc(*gp_fixargs((in_cover, out_cover, projection_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Transform_arc', None)
def Transform(in_cover=None, out_cover=None, transform_type=None):
    """Transform_arc(in_cover, out_cover, {transform_type})

        Moves all features in a coverage based on a set of from and to control points.

     INPUTS:
      in_cover (Coverage):
          The coverage whose coordinates are to be transformed.
      out_cover (Coverage):
          The name of an existing coverage containing destination tics. The features from
          the input coverage will be transformed into this coverage.
      transform_type {String}:
          The type of coordinate transformation to be performed:

          * AFFINE—Performs an affine transformation. At least three tics are required to
          define this transformation. If only two tics are matched, a similarity
          transformation will be applied. The AFFINE equations use six parameters.

          * PROJECTIVE—Performs a projective transformation. This requires a minimum of
          four tics to define the transformation. The projective transformation is only
          used to transform coordinates digitized directly off high-altitude aerial
          photography or aerial photographs of relatively flat terrain, assuming there is
          no systematic distortion in the air photos. PROJECTIVE uses eight parameters.

          * SIMILARITY—Performs a similarity transformation. At least two tics are
          necessary for this transformation. This transformation is also known as a
          Helmert, orthogonal, two-dimensional linear conformal, or four-parameter
          transformation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Transform_arc(*gp_fixargs((in_cover, out_cover, transform_type), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Tables toolset
@gptooldoc('AddXY_arc', None)
def AddXY(in_cover=None, feature_type=None):
    """AddXY_arc(in_cover, {feature_type})

        Adds the items X-COORD and Y-COORD for labels or points to the input coverage
        PAT, or for nodes to the input coverage NAT, and calculates their values.The
        tool determines the feature classes of the input coverage and lists those
        available to which x,y coordinates can be added. The tool is most commonly used
        to gain access to a coverage's geometry to perform queries and analysis or to
        extract points or nodes based on their x,y location.

     INPUTS:
      in_cover (Coverage):
          The coverage containing points or polygon labels whose x,y coordinates will
          become attributes in the PAT, or in the coverage containing nodes, to the NAT.
      feature_type {String}:
          Type of coverage feature whose x,y coordinates will become feature attributes.

          * POINT—Point feature coordinates to be added to the PAT including label points.
          This is the default option.

          * NODE—Node feature coordinates to be added to the NAT."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddXY_arc(*gp_fixargs((in_cover, feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IDEdit_arc', None)
def IDEdit(in_cover=None, feature_type=None):
    """IDEdit_arc(in_cover, feature_type)

        Updates User-IDs in a coverage after they have been modified in a feature
        attribute table. The feature attribute table is used to determine the correct
        User-ID for each feature in the coverage. This value is recorded in all places
        where the feature User-ID is stored.

     INPUTS:
      in_cover (Coverage):
          The coverage for which User-IDs have been modified.
      feature_type (String):
          Specifies the class of features for which User-IDs are to be updated.

          * POLY—Polygon User-IDs will be updated. This is the default option.

          * LINE—Arc User-IDs will be updated.

          * POINT—Point User-IDs will be updated.

          * ANNO.subclass—Annotation User-IDs will be updated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IDEdit_arc(*gp_fixargs((in_cover, feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Renode_arc', None)
def Renode(in_cover=None, from_item=None, to_item=None):
    """Renode_arc(in_cover, {from_item}, {to_item})

        Updates arc–node topology by renumbering nodes for the input coverage arcs and
        identifies arcs that share the same node locations.The tool renumbers the
        internal node numbers for each arc, assigns the same node
        number for arcs that share a common node location, and updates the FNODE# and
        TNODE# items in the arc attribute table (AAT) when it exists.

     INPUTS:
      in_cover (Coverage):
          The coverage whose nodes will be renumbered.
      from_item {String}:
          The INFO item signifying the elevation of the from_node of each arc.
      to_item {String}:
          The INFO item signifying the elevation of the to_node of each arc."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Renode_arc(*gp_fixargs((in_cover, from_item, to_item), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Tolerances toolset
@gptooldoc('Tolerance_arc', None)
def Tolerance(in_cover=None, tolerance_type=None, tolerance_value=None):
    """Tolerance_arc(in_cover, {tolerance_type}, {tolerance_value})

        Sets a coverage's tolerances.

     INPUTS:
      in_cover (Coverage):
          The coverage for which tolerances will be set.
      tolerance_type {String}:
          The type of tolerance to be set.

          * FUZZY—Sets the Input Coverage's fuzzy tolerance to the value specified in the
          Tolerance Value. This is the default option.

          * DANGLE—Sets the Input Coverage's dangle length to the value specified in the
          Tolerance Value.

          * TIC_MATCH—Sets the tic match tolerance to the value specified in the Tolerance
          Value.

          * EDIT—Sets the Input Coverage's edit distance to the value specified in the
          Tolerance Value.

          * NODESNAP—Sets the Input Coverage's node snap distance to the value specified
          in the Tolerance Value.

          * WEED—Sets the weed tolerance to the value specified in the Tolerance Value.

          * GRAIN—Sets the grain tolerance to the value specified in the Tolerance Value.

          * SNAP—Sets the Input Coverage's general snapping distance to the value
          specified in the Tolerance Value.
      tolerance_value {Double}:
          The value to be set for the selected option's tolerance. A Tolerance Value of
          zero will not be accepted for the following options: FUZZY, EDIT, NODESNAP,
          WEED, GRAIN, and SNAP."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Tolerance_arc(*gp_fixargs((in_cover, tolerance_type, tolerance_value), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Topology toolset
@gptooldoc('Build_arc', None)
def Build(in_cover=None, feature_type=None, anno_subclass=None):
    """Build_arc(in_cover, feature_type, {anno_subclass})

        Creates or updates feature attribute tables and polygon topology. Build is also
        used to synchronize polygon User-IDs with label point User-IDs.

     INPUTS:
      in_cover (Coverage):
          The coverage to be built.
      feature_type (String):
          The feature class to be built.

          * POINT—Creates a PAT for label points. This is the default option.

          * LINE—Creates an AAT for arcs.

          * POLY—Creates a PAT and defines polygon topology.

          * NODE—Creates an NAT for nodes.

          * ANNO—Creates a TAT for the Annotation Subclass.
      anno_subclass {String}:
          The name of the Annotation Subclass to be built."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Build_arc(*gp_fixargs((in_cover, feature_type, anno_subclass), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Clean_arc', None)
def Clean(in_cover=None, out_cover=None, dangle_length=None, fuzzy_tolerance=None, feature_type=None):
    """Clean_arc(in_cover, {out_cover}, {dangle_length}, {fuzzy_tolerance}, {feature_type})

        Generates a coverage with correct polygon or arc–node topology. To do this,
        Clean edits and corrects geometric coordinate errors, assembles arcs into
        polygons, and creates feature attribute information for each polygon or arc
        (that is, creates a PAT or AAT).

     INPUTS:
      in_cover (Coverage):
          The coverage to be cleaned.
      dangle_length {Double}:
          The minimum length allowed for dangling arcs in the Output Coverage. A dangling
          arc is an arc that has the same polygon internal number on its left and right
          sides and ends at a dangling node. Dangling arcs are removed for both the POLY
          and LINE options. If the Dangle Length is not provided, the dangle length is
          read from the coverage TOL file if the TOL file exists;otherwise, dangle length
          is set to zero (the default).
      fuzzy_tolerance {Double}:
          The minimum distance between coordinates in each out_cover.
      feature_type {String}:
          Specifies whether to create polygon topology and a PAT or arc–node topology and
          an AAT. POLY is the default option. If POLY is used on a coverage that has an
          existing AAT, Clean will also automatically rebuild the AAT.

          * POLY—Polygon topology and a PAT are created. If POLY is used on a coverage
          that has an existing AAT, Clean will also automatically rebuild the AAT. POLY is
          the default option.

          * LINE—Arc–node topology and an AAT are created.

     OUTPUTS:
      out_cover {Coverage}:
          The coverage created by Clean. If the Input Coverage and the Output Coverage
          have the same name, the Input Coverage will be replaced. By default, the Input
          Coverage is replaced."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Clean_arc(*gp_fixargs((in_cover, out_cover, dangle_length, fuzzy_tolerance, feature_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateLabels_arc', None)
def CreateLabels(in_cover=None, id_base=None):
    """CreateLabels_arc(in_cover, {id_base})

        Creates label points for polygons that have no labels and assigns each a User-
        ID.

     INPUTS:
      in_cover (Coverage):
          The coverage to which label points are to be added.
      id_base {Long}:
          The minimum User-ID value to be assigned to new label points.The specified value
          will be the User-ID for the first polygon encountered that
          has no label point. User-IDs are then incremented by one for each subsequent
          polygon having no label point. Specifying an ID Base of zero will create new
          labels for all polygons, where each User-ID will equal the polygon's internal
          number minus one. This is the default value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateLabels_arc(*gp_fixargs((in_cover, id_base), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('VPFTile_arc', None)
def VPFTile(VPF_library=None, sig_digits=None, VPF_standard=None, spec_cover=None):
    """VPFTile_arc(VPF_library, {sig_digits}, {VPF_standard}, {spec_cover})

        Creates cross-tile topology for all tiled coverages in a Vector Product Format
        (VPF) database library, or topology for an individual tile in a VPF library.This
        tool is used for postprocessing a VPF coverage or library from Export to
        VPF output. For efficiency purposes, it's recommended that you build cross-tile
        topology only after you have finished converting all coverages in your VPF
        library.

     INPUTS:
      VPF_library (Folder):
          Location of the VPF database library for which cross-tile topology is to be
          created.
      sig_digits {Long}:
          The number of digits the software will use when trying to match node coordinates
          at tile boundaries. The larger the number, the smaller the search tolerance. The
          default value is 4.
      VPF_standard {Long}:
          The VPF Standard to be used. The VPF Standard has two ways of defining cross-
          tile topology.

          * 93—Creates cross-tile topology based on the September 30, 1993, version of the
          VPF Standard (MIL-STD-2407). 93 is the default option.

          * 96—Creates cross-tile topology based on the June 28, 1996, version of the VPF
          Standard (MIL-STD-2407).
      spec_cover {String}:
          Specifies whether to process all the coverages in the VPF library or only the
          specified coverage.

          * ALL—Process all the coverages in the VPF library

          * VPF_cover—Process only the specified coverage"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.VPFTile_arc(*gp_fixargs((VPF_library, sig_digits, VPF_standard, spec_cover), True)))
        return retval
    except Exception, e:
        raise e


# Data Management\Workspace Management toolset
@gptooldoc('Create_arc', None)
def Create(out_cover=None, template_cover=None):
    """Create_arc(out_cover, {template_cover})

        Creates a new coverage.The coverage can be initialized with the TIC, BND, and
        PRJ files copied from an
        existing coverage or grid.

     INPUTS:
      template_cover {Coverage}:
          An existing coverage or grid whose TIC file, boundary information (BND file),
          and projection information (PRJ file) will be copied to the Output Coverage.

     OUTPUTS:
      out_cover (Coverage):
          The name of the coverage that will be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Create_arc(*gp_fixargs((out_cover, template_cover), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject