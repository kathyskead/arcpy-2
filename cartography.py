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
"""The tools in the Cartography toolbox are designed to produce and refine data to
support the production of maps. This includes the creation of annotation and
masks, the simplification of features and reduction of their density, the
refinement and management of symbolized features, the creation of grids and
graticules, and the management of data-driven pages for layout."""
__all__ = ['CulDeSacMasks', 'FeatureOutlineMasks', 'IntersectingLayersMasks', 'SetRepresentationControlPointByAngle', 'CreateOverpass', 'CreateUnderpass', 'AlignMarkerToStrokeOrFill', 'DisperseMarkers', 'SetRepresentationControlPointAtIntersect', 'DetectGraphicConflict', 'AddRepresentation', 'CalculateRepresentationRule', 'DropRepresentation', 'RemoveOverride', 'SelectFeatureByOverride', 'SetLayerRepresentation', 'UpdateOverride', 'CalculateLineCaps', 'CalculatePolygonMainAngle', 'CalculateUTMZone', 'CalculateAdjacentFields', 'CalculateGridConvergenceAngle', 'ThinRoadNetwork', 'PropagateDisplacement', 'ResolveBuildingConflicts', 'ResolveRoadConflicts', 'AggregatePolygons', 'CollapseDualLinesToCenterline', 'SimplifyBuilding', 'SimplifyLine', 'SmoothLine', 'MergeDividedRoads', 'GridIndexFeatures', 'StripMapIndexFeatures', 'SimplifyPolygon', 'SmoothPolygon', 'AggregatePoints', 'ContourAnnotation', 'MapServerCacheTilingSchemeToPolygons', 'TiledLabelsToAnnotation', 'CreateCartographicPartitions', 'CollapseRoadDetail', 'DelineateBuiltUpAreas', 'CalculateCentralMeridianAndParallels', 'DeleteGridsAndGraticules', 'MakeGridsAndGraticulesLayer']
__alias__ = u'cartography'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Annotation toolset
@gptooldoc('ContourAnnotation_cartography', None)
def ContourAnnotation(in_features=None, out_geodatabase=None, contour_label_field=None, reference_scale_value=None, out_layer=None, contour_color=None, contour_type_field=None, contour_alignment=None, enable_laddering=None):
    """ContourAnnotation_cartography(in_features, out_geodatabase, contour_label_field, reference_scale_value, out_layer, contour_color, {contour_type_field}, {contour_alignment}, {enable_laddering})

        Creates annotation for contour features.The tool creates an annotation feature
        class with corresponding mask polygons
        based on input contour features.

     INPUTS:
      in_features (Feature Layer):
          The contour line feature class for which the annotation will be created.
      out_geodatabase (Workspace / Feature Dataset):
          The workspace where the output feature classes will be saved. The workspace can
          be an existing geodatabase or an existing feature dataset.
      contour_label_field (Field):
          The field in the input layer attribute table upon which the annotation text
          will be based.
      reference_scale_value (Double):
          Enter the scale to use as a reference for the annotation. This sets the scale
          to which all symbol and text sizes in the annotation will be based.
      contour_color (String):
          The color of the output contour layer and annotation features.

          * BLACK—The output contour layer and annotation features will be drawn in black.
          This is the default.

          * BROWN—The output contour layer and annotation features will be drawn in brown.

          * BLUE—The output contour layer and annotation features will be drawn in blue.
      contour_type_field {Field}:
          The field in the input layer attribute table containing a value for the type of
          contour feature. An annotation class will be created for each type value.
      contour_alignment {String}:
          The annotation can be aligned to the contour elevations so that the top of the
          text is always placed uphill. This option allows the annotation to be placed
          upside down. The contour annotation can also be aligned to the page, ensuring
          that the text is never placed upside down.

          * PAGE— The annotation will be aligned to the page, ensuring that the text is
          never placed upside down. This is the default.

          * UPHILL—The annotation will be aligned to the contour elevations so that the
          top of the text is always placed uphill. This option allows the annotation to be
          placed upside down.
      enable_laddering {Boolean}:
          Placing annotation in ladders will place the text so it appears to step up and
          step down the contours in a straight path. These ladders will run from the top
          of a hill to the bottom, will not cross each other, will belong to a single
          slope, and will not cross any other slope.

          * ENABLE_LADDERING—Annotation will step up and down the contours in a straight
          path.

          * NOT_ENABLE_LADDERING—Annotation will not be placed up and down the contours in
          a straight path. This is the default.

     OUTPUTS:
      out_layer (Group Layer):
          The group layer that will contain the contour layer, the annotation, and the
          mask layer. When working in ArcCatalog, you can use the Save To Layer File tool
          to write the output group layer to a layer file. When using ArcMap, the tool
          adds the group layer to the display if this option is checked in the
          geoprocessing options. The group layer that is created is temporary and will not
          persist after the session ends unless the document is saved."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ContourAnnotation_cartography(*gp_fixargs((in_features, out_geodatabase, contour_label_field, reference_scale_value, out_layer, contour_color, contour_type_field, contour_alignment, enable_laddering), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MapServerCacheTilingSchemeToPolygons_cartography', None)
def MapServerCacheTilingSchemeToPolygons(map_document=None, data_frame=None, tiling_scheme=None, output_feature_class=None, use_map_extent=None, clip_to_horizon=None, antialiasing=None, levels=None):
    """MapServerCacheTilingSchemeToPolygons_cartography(map_document, data_frame, tiling_scheme, output_feature_class, use_map_extent, clip_to_horizon, {antialiasing}, {levels;levels...})

        Creates a new polygon feature class from an existing tiling scheme.This tool
        subdivides a data frame extent using the same scales as an existing
        map service cache tiling scheme and creates tiles over a large area, or
        "supertile". Since the supertile extent is larger than the actual tiles defined
        in the scheme, tiles used as input into the Tiled Labels to Annotation tool can
        convert labels to annotation over a larger area at a time. This process
        minimizes annotation duplication across tiles.

     INPUTS:
      map_document (ArcMap Document):
          The source map document.
      data_frame (String):
          The data frame from the source map document.
      tiling_scheme (File):
          Path to a predefined tiling scheme .xml file.
      use_map_extent (Boolean):
          Choose whether to produce tiles for the entire extent of the tiling scheme or
          only tiles that intersect the full extent of the data frame.

          * USE_MAP_EXTENT—Polygon features will be created for the full extent of the
          data frame. This is the default.

          * FULL_TILING_SCHEME—Polygon features will be created for the full extent of the
          tiling scheme.
      clip_to_horizon (Boolean):
          Choose whether to constrain the polygons to the valid area of use for the
          geographic or projected coordinate system of the data frame.

          *  CLIP_TO_HORIZON—Polygon features will only be created within the valid area
          of use for the geographic or projected coordinate system of the data frame.
          Tiles that are within the extent of the tiling scheme but outside the extent of
          the coordinate system horizon will be clipped. This is the default.

          * UNIFORM_TILE_SIZE—Polygon features will be created for the full extent of the
          tiling scheme. Within each scale level, polygons will be of a uniform size and
          will not be clipped at the coordinate system horizon. This may create data that
          is outside the valid area of use for the geographic or projected coordinate
          system.  If a scale within the tiling scheme would generate a tile that is
          larger than the spatial domain of the feature class, null geometry will be
          created for that feature.
      antialiasing {Boolean}:
          Choose whether to generate polygons that match map service caches with anti-
          aliasing enabled. A map service cache supertile is 2048 x 2048 pixels with
          antialiasing or 4096 x 4096 pixels without. To see if antialiasing was used in
          an existing cache, open the tiling scheme file, conf.xml, and check to see if
          the <Antialiasing> tag is set to true.

          * ANTIALIASING—Polygon tiles will be created to match the supertile extent of a
          map service cache with antialiasing enabled.

          * NONE—Polygon tiles will be created to match the supertile extent of a map
          service cache without antialiasing enabled. This is the default.
      levels {Double}:
          The scale levels at which you will create polygons. To create polygons for all
          scale levels included in a tiling scheme, leave this parameter blank. You may
          choose to create polygons for all or only some of the scale levels that are
          included in your tiling scheme. To add additional scale levels, however, you
          will need to modify your tiling scheme file or create a new one.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output polygon feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MapServerCacheTilingSchemeToPolygons_cartography(*gp_fixargs((map_document, data_frame, tiling_scheme, output_feature_class, use_map_extent, clip_to_horizon, antialiasing, levels), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TiledLabelsToAnnotation_cartography', None)
def TiledLabelsToAnnotation(map_document=None, data_frame=None, polygon_index_layer=None, out_geodatabase=None, out_layer=None, anno_suffix=None, reference_scale_value=None, reference_scale_field=None, tile_id_field=None, coordinate_sys_field=None, map_rotation_field=None, feature_linked=None, generate_unplaced_annotation=None):
    """TiledLabelsToAnnotation_cartography(map_document, data_frame, polygon_index_layer, out_geodatabase, out_layer, anno_suffix, {reference_scale_value}, {reference_scale_field}, {tile_id_field}, {coordinate_sys_field}, {map_rotation_field}, {feature_linked}, {generate_unplaced_annotation})

        Converts labels to annotation for layers in a map document based on a polygon
        index layer. The tool divides a map into tiles and creates annotation for each
        tile in turn.
        This is useful for converting a large number of labels to annotation. The
        polygon index layer can be one generated by the Map Server Cache Tiling Scheme
        To Polygons or Grid Index Features tools or any other polygon feature class that
        covers the area where you would like to create annotation.

     INPUTS:
      map_document (ArcMap Document):
          The source map document that contains the labels to convert to annotation.
      data_frame (String):
          The data frame from the map document that contains the labels to convert to
          annotation.
      polygon_index_layer (Table View):
          The polygon layer that contains tile features.
      out_geodatabase (Workspace / Feature Dataset):
          The workspace where the output feature classes will be saved. The workspace can
          be an existing geodatabase or an existing feature dataset.
      anno_suffix (String):
          The suffix that will be added to each new annotation feature class. This suffix
          will be appended to the name of the source feature class for each new annotation
          feature class. The reference scale for the annotation will follow this suffix.
      reference_scale_value {Double}:
          Enter the scale to use as a reference for the annotation. This sets the scale
          to which all symbol and text sizes in the annotation will be based.
      reference_scale_field {Field}:
          The field in the polygon index layer that will determine the reference scale of
          the annotation. This sets the scale to which all symbol and text sizes in the
          annotation will be based.
      tile_id_field {Field}:
          A field in the polygon index layer that uniquely identifies the tiled area.
          These values will populate the TileID field in the annotation feature class
          attribute table.
      coordinate_sys_field {Field}:
          A field in the polygon index layer that contains the coordinate system
          information for each tile. Due to the length required for a field to store
          coordinate system information, a polygon index layer that contains a coordinate
          system field must be a geodatabase feature class.
      map_rotation_field {Field}:
          A field in the polygon index layer that contains an angle by which the data
          frame is to be rotated.
      feature_linked {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Choose whether the output annotation feature class
          will be linked to the
          features in another feature class.

          * STANDARD— The output annotation feature class will not be linked to the
          features in another feature class. This is the default.

          * FEATURE_LINKED—The output annotation feature class will be linked to the
          features in another feature class.
      generate_unplaced_annotation {Boolean}:
          Choose whether to create unplaced annotation from unplaced labels.

          * NOT_GENERATE_UNPLACED_ANNOTATION—Annotation will only be created for features
          that are currently labeled. This is the default.

          * GENERATE_UNPLACED_ANNOTATION—Unplaced annotation are stored in the annotation
          feature class. The status field for these annotation is set to Unplaced.

     OUTPUTS:
      out_layer (Group Layer):
          The group layer that will contain the generated annotation. When working in
          ArcCatalog, you can use the Save To Layer File tool to write the output group
          layer to a layer file. When using ArcMap, the tool adds the group layer to the
          display if this option is checked in the geoprocessing options. The group layer
          that is created is temporary and will not persist after the session ends unless
          the document is saved."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TiledLabelsToAnnotation_cartography(*gp_fixargs((map_document, data_frame, polygon_index_layer, out_geodatabase, out_layer, anno_suffix, reference_scale_value, reference_scale_field, tile_id_field, coordinate_sys_field, map_rotation_field, feature_linked, generate_unplaced_annotation), True)))
        return retval
    except Exception, e:
        raise e


# Cartographic Refinement toolset
@gptooldoc('AlignMarkerToStrokeOrFill_cartography', None)
def AlignMarkerToStrokeOrFill(in_point_features=None, in_line_or_polygon_features=None, search_distance=None, marker_orientation=None):
    """AlignMarkerToStrokeOrFill_cartography(in_point_features, in_line_or_polygon_features, search_distance, {marker_orientation})

        Align the representation marker symbols of a point feature class to the nearest
        stroke or fill representation symbols in a line or polygon feature class within
        a specified search distance.

     INPUTS:
      in_point_features (Layer):
          The input point feature layer containing marker representations.
      in_line_or_polygon_features (Layer):
          The input line or polygon feature layer containing stroke or fill
          representations.
      search_distance (Linear unit):
          The search distance from graphical marker edge to graphical stroke edge. A
          distance greater than or equal to zero must be specified.
      marker_orientation {String}:
          Specifies the representation marker orientation relative to the stroke or fill
          edge.

          * PERPENDICULAR—aligns representation markers perpendicularly to the stroke or
          fill edge. This is the default.

          * PARALLEL—aligns representation markers parallel to the stroke or fill edge."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AlignMarkerToStrokeOrFill_cartography(*gp_fixargs((in_point_features, in_line_or_polygon_features, search_distance, marker_orientation), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateLineCaps_cartography', None)
def CalculateLineCaps(in_features=None, cap_type=None, dangle_option=None):
    """CalculateLineCaps_cartography(in_features, {cap_type}, {dangle_option})

        Modifies the cap type (ending style) for representation stroke symbols and
        stores it as a representation override.

     INPUTS:
      in_features (Layer):
          The input feature layer containing line representations.
      cap_type {String}:
          Defines how the ends of representation stroke symbols are drawn. The default cap
          type of representation strokes is round, where the symbol is terminated with a
          semicircle of radius equal to stroke width is centered at the line endpoint.
          This tool changes cap type to BUTT or SQUARE.

          * BUTT—Specifies to end the representation stroke symbol exactly where the line
          geometry ends. This is the default.

          * SQUARE—Specifies to end the representation stroke symbol with closed, square
          caps that extend past the endpoint of the line by half of the symbol width.
      dangle_option {String}:
          The Dangle parameter controls how line caps are calculated for adjoining line
          features that share an endpoint but are drawn with different representation
          symbology.

          * CASED_LINE_DANGLE—Modifies the cap style for dangling lines (those not
          connected at their endpoints to another line) and also for the lines where a
          cased-line representation stroke symbol is joined at the endpoint of a single-
          line representation stroke symbol. This is the default.

          * TRUE_DANGLE—Modifies the cap style only for endpoints that are not connected
          to another feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateLineCaps_cartography(*gp_fixargs((in_features, cap_type, dangle_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculatePolygonMainAngle_cartography', None)
def CalculatePolygonMainAngle(in_features=None, angle_field=None, rotation_method=None):
    """CalculatePolygonMainAngle_cartography(in_features, angle_field, {rotation_method})

        Calculates the dominant angles of input polygon features and assigns the values
        to a specified field in the feature class.

     INPUTS:
      in_features (Feature Layer):
          The input polygon features.
      angle_field (Field):
          The field that will be updated with the polygon main angle values.
      rotation_method {String}:
          Controls the method and origin point of rotation.

          * GEOGRAPHIC—Angle is calculated clockwise with 0 at top/north.

          * ARITHMETIC—Angle is calculated counterclockwise with 0 at the right/east.

          * GRAPHIC—Angle is calculated counterclockwise with 0 at top/north. This is the
          default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculatePolygonMainAngle_cartography(*gp_fixargs((in_features, angle_field, rotation_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateOverpass_cartography', None)
def CreateOverpass(in_above_features=None, in_below_features=None, margin_along=None, margin_across=None, out_overpass_feature_class=None, out_mask_relationship_class=None, where_clause=None, out_decoration_feature_class=None, wing_type=None, wing_tick_length=None):
    """CreateOverpass_cartography(in_above_features, in_below_features, margin_along, margin_across, out_overpass_feature_class, out_mask_relationship_class, {where_clause}, {out_decoration_feature_class}, {wing_type}, {wing_tick_length})

        Allows intersecting lines to be displayed as overpassing one another by creating
        bridge parapets and masks to cover the underlying road segment.

     INPUTS:
      in_above_features (Layer):
          The input line feature layer containing stroke representations that
          intersect—and will be symbolized as passing above—stroke representations in the
          Input Below Features.
      in_below_features (Layer):
          The input line feature layer containing stroke representations that
          intersect—and will be symbolized as passing below—stroke representations in the
          Input Above Features. These features will be masked by the polygons created in
          the Output Overpass feature class.
      margin_along (Linear unit):
          Sets the length of the mask polygons along the Input Above Features by
          specifying the distance in page units that the mask should extend beyond the
          width of the stroke symbol of the Input Below Features. The Margin Along must be
          specified, and it must be greater than or equal to zero. Choose a page unit
          (points, millimeters, and so on) for the margin; the default is points.
      margin_across (Linear unit):
          Sets the width of the mask polygons across the Input Above Features by
          specifying the distance in page units that the mask should extend beyond the
          width of the stroke symbol of the Input Below Features. The Margin Across must
          be specified, and it must be greater than or equal to zero. Choose a page unit
          (points, millimeters, and so on) for the margin; the default is points.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features in the Input Above
          Features with Representations parameter.Use quotes, "MY_FIELD", or if you're
          querying personal geodatabases, enclose
          fields in square brackets: [MY_FIELD]In the Python window, enclose the
          {where_clause} in parentheses to ensure the
          spaces (which are delimiters between parameters) are correctly interpreted.See
          SQL reference for query expressions used in ArcGIS for more information on
          SQL syntax.
      wing_type {String}:
          Specifies the wing style of the parapet features.

          * ANGLED—Specifies that the wing tick of the parapet will be angled between the
          Input Above Features and the Input Below Features. This is the default.

          * PARALLEL—Specifies that the wing tick of the overpass wing will be parallel to
          the Input Below Features.

          * NONE—Specifies that no wing ticks will be created on the parapets.
      wing_tick_length {Linear unit}:
          Sets the length of the parapet wings in page units. The length must be greater
          than or equal to zero; the default length is 1. Choose a page unit (Points,
          Millimeters, and so on) for the length; the default is Points. This parameter
          does not apply to the Wing Type - NONE.

     OUTPUTS:
      out_overpass_feature_class (Feature Class):
          The output feature class that will be created to store polygons to mask the
          Input Below features.
      out_mask_relationship_class (Relationship Class):
          The output relationship class that will be created to store links between
          Overpass mask polygons and the stroke representations of the Input Below
          Features.
      out_decoration_feature_class {Feature Class}:
          The output line feature class that will be created to store parapet features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateOverpass_cartography(*gp_fixargs((in_above_features, in_below_features, margin_along, margin_across, out_overpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateUnderpass_cartography', None)
def CreateUnderpass(in_above_features=None, in_below_features=None, margin_along=None, margin_across=None, out_underpass_feature_class=None, out_mask_relationship_class=None, where_clause=None, out_decoration_feature_class=None, wing_type=None, wing_tick_length=None):
    """CreateUnderpass_cartography(in_above_features, in_below_features, margin_along, margin_across, out_underpass_feature_class, out_mask_relationship_class, {where_clause}, {out_decoration_feature_class}, {wing_type}, {wing_tick_length})

        Allows intersecting lines to be displayed as underpassing one another by
        creating bridge parapets and masks to cover the underlying road segment.

     INPUTS:
      in_above_features (Layer):
          The input line feature layer containing stroke representations that
          intersect—and will be symbolized as passing above—stroke representations in the
          Input Below Features.
      in_below_features (Layer):
          The input line feature layer containing stroke representations that
          intersect—and will be symbolized as passing below—stroke representations in the
          Input Above Features. These features will be masked by the polygons created in
          the Output Overpass feature class.
      margin_along (Linear unit):
          Sets the length of the mask polygons along the Input Above Features by
          specifying the distance in page units that the mask should extend beyond the
          width of the stroke symbol of the Input Below features. The Margin Along must be
          specified, and it must be greater than or equal to zero. Choose a page unit for
          the margin; the default is points.
      margin_across (Linear unit):
          Sets the width of the mask polygons across the Input Above Features by
          specifying the distance in page units that the mask should extend beyond the
          width of the stroke symbol of the Input Below Features. The Margin Across must
          be specified, and it must be greater than or equal to zero. Choose a page unit
          for the margin; the default is points.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features in the Input Above
          Features with Representations parameter.Use quotes, "MY_FIELD", or if you're
          querying personal geodatabases, enclose
          fields in square brackets: [MY_FIELD]In the Python window, enclose the
          {where_clause} in parentheses to ensure the
          spaces (which are delimiters between parameters) are correctly interpreted.See
          SQL reference for query expressions used in ArcGIS for more information on
          SQL syntax.
      wing_type {String}:
          Specifies the wing style of the parapet features.

          * ANGLED—Specifies that the wing tick of the parapet will be angled between the
          Input Above Features and the Input Below Features. This is the default.

          * PARALLEL—Specifies that the wing tick of the overpass wing will be parallel to
          the Input Below Features.

          * NONE—Specifies that no wing ticks will be created on the parapets.
      wing_tick_length {Linear unit}:
          Sets the length of the parapet wings in page units. The length must be greater
          than or equal to zero; the default length is 1. Choose a page unit (points,
          millimeters, and so on) for the length; the default is points. This parameter
          does not apply to the Wing Type - NONE.

     OUTPUTS:
      out_underpass_feature_class (Feature Class):
          The output feature class that will be created to store polygons to mask the
          Input Below Features.
      out_mask_relationship_class (Relationship Class):
          The output relationship class that will be created to store links between
          Underpass mask polygons and the stroke representations of the Input Below
          Features.
      out_decoration_feature_class {Feature Class}:
          The output line feature class that will be created to store parapet features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateUnderpass_cartography(*gp_fixargs((in_above_features, in_below_features, margin_along, margin_across, out_underpass_feature_class, out_mask_relationship_class, where_clause, out_decoration_feature_class, wing_type, wing_tick_length), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DisperseMarkers_cartography', None)
def DisperseMarkers(in_point_features=None, minimum_spacing=None, dispersal_pattern=None):
    """DisperseMarkers_cartography(in_point_features, minimum_spacing, {dispersal_pattern})

        Finds representation markers that are overlapping or too close to one another
        and spreads them apart based on a minimum spacing and dispersal pattern.

     INPUTS:
      in_point_features (Layer):
          The input point feature layer containing marker representations.
      minimum_spacing (Linear unit):
          The minimum separation distance between individual markers, in page units. A
          distance must be specified and must be greater than or equal to zero. When a
          positive value is specified, markers will be separated by that value; when a
          value of zero is specified, markers will be touching. The default page unit is
          Points.
      dispersal_pattern {String}:
          Specifies the pattern in which the dispersed representation markers are placed.
          A group of markers will have a center of mass derived from the locations of each
          marker in the group. The center of mass is then used as the anchor point around
          which the dispersal pattern operates.

          * EXPANDED—The general pattern of the markers will be maintained as they are
          spread apart. Markers that were exactly coincident are dispersed to a circle
          around their center of mass. This is the default.

          * RANDOM—Representation markers are placed around the center of mass in a random
          dispersal that respects the minimum spacing.

          * SQUARES—Representation markers are placed in multiple square rings around the
          center of mass, ensuring that all markers are placed as closely together as
          allowable by the minimum spacing parameter.

          * RINGS—Representation markers are placed in multiple circular rings around the
          center of mass, ensuring that all markers are placed as closely together as
          allowable by the minimum spacing parameter.

          * SQUARE—Representation markers are placed evenly around the center of mass in a
          single square pattern.

          * RING—Representation markers are placed evenly around the center of mass in a
          single circular pattern.

          * CROSS—Representation markers are spaced evenly on horizontal and vertical axes
          originating from the center of mass.

          * X_CROSS—Representation markers are spaced evenly on 45° axes originating from
          the center of mass."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DisperseMarkers_cartography(*gp_fixargs((in_point_features, minimum_spacing, dispersal_pattern), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetRepresentationControlPointAtIntersect_cartography', None)
def SetRepresentationControlPointAtIntersect(in_line_or_polygon_features=None, in_features=None):
    """SetRepresentationControlPointAtIntersect_cartography(in_line_or_polygon_features, {in_features})

        This tool is commonly used to synchronize boundary symbology on adjacent
        polygons. It creates a representation control point at vertices that are shared
        by one or more line or polygon features.

     INPUTS:
      in_line_or_polygon_features (Layer):
          The input line or polygon feature layer symbolized with a feature class
          representation.
      in_features {Feature Layer}:
          The feature layer with coincident features. These features can be from a
          geodatabase, shapefile, or coverage."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetRepresentationControlPointAtIntersect_cartography(*gp_fixargs((in_line_or_polygon_features, in_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetRepresentationControlPointByAngle_cartography', None)
def SetRepresentationControlPointByAngle(in_features=None, maximum_angle=None):
    """SetRepresentationControlPointByAngle_cartography(in_features, maximum_angle)

        Places a representation control point at vertices along a line or polygon
        outline where the angle created by a change in line direction is less than or
        equal to a specified maximum angle.

     INPUTS:
      in_features (Layer):
          The input feature layer containing line or polygon representations.
      maximum_angle (Double):
          The angle used to determine whether or not a vertex along a line or polygon
          outline will be set as a representation control point. The angle value must be
          greater than zero and less than 180 decimal degrees."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetRepresentationControlPointByAngle_cartography(*gp_fixargs((in_features, maximum_angle), True)))
        return retval
    except Exception, e:
        raise e


# Data Driven Pages toolset
@gptooldoc('CalculateAdjacentFields_cartography', None)
def CalculateAdjacentFields(in_features=None, in_field=None):
    """CalculateAdjacentFields_cartography(in_features, in_field)

        The most common use case for using this tool is to populate fields that can be
        used to label the adjacent pages in a map book. This tool appends eight new
        fields (each field representing one of the eight points of the compass: North,
        Northeast, East, Southeast, South, Southwest, West and Northwest) to the input
        feature class and calculates values that identify the adjacent (neighboring)
        polygons, in each cardinal direction, for each feature in the input feature
        class.

     INPUTS:
      in_features (Feature Layer):
          Polygon grid index features to be appended with adjacent field data.
      in_field (Field):
          Field whose values will be used to populate adjacent field data. Use actual
          field names. Do not use field aliases."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateAdjacentFields_cartography(*gp_fixargs((in_features, in_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateCentralMeridianAndParallels_cartography', None)
def CalculateCentralMeridianAndParallels(in_features=None, in_field=None, standard_offset=None):
    """CalculateCentralMeridianAndParallels_cartography(in_features, in_field, {standard_offset})

        Calculates the central meridian and optional standard parallels based on the
        center point of a feature's extent; stores this coordinate system as a spatial
        reference string in a specified text field and repeats this for a set, or
        subset, of features.

     INPUTS:
      in_features (Feature Layer):
          Input feature layer.
      in_field (Field):
          Text field to store the coordinate system string.
      standard_offset {Double}:
          Percentage of the height of the input feature used to offset the standard
          parallels from the center latitude of the input feature. The default is 25% or
          0.25. Negative values and values greater than 1 are acceptable inputs."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateCentralMeridianAndParallels_cartography(*gp_fixargs((in_features, in_field, standard_offset), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateGridConvergenceAngle_cartography', None)
def CalculateGridConvergenceAngle(in_features=None, angle_field=None, rotation_method=None, coordinate_sys_field=None):
    """CalculateGridConvergenceAngle_cartography(in_features, angle_field, {rotation_method}, {coordinate_sys_field})

        Calculates the rotation angle for true north based on the center point of each
        feature in a feature class and populates this value in a specified field. This
        field can be used in conjunction with Data Driven Pages to rotate each map to
        true north.

     INPUTS:
      in_features (Feature Layer):
          Input feature class (points, multipoints, lines, and polygons).
      angle_field (Field):
          Existing field that will be populated with the true north calculation value in
          decimal degrees.
      rotation_method {String}:
          Method in which the rotation value is calculated. Geographic is the default
          value.

          * GEOGRAPHIC—Angle is calculated clockwise with 0 at top. This is the default.

          * ARITHMETIC—Angle is calculated counterclockwise with 0 at right.

          * GRAPHIC—Angle is calculated counterclockwise with 0 at top.
      coordinate_sys_field {Field}:
          Field containing a projection engine string for a projected coordinate system
          to be used for angle calculation. The angle calculation for each feature will be
          based on the projected coordinate system projection engine string for the
          specific feature. In cases where there is an invalid value the tool will use the
          Cartographic coordinate system specified in the Cartography environment
          settings. The default is none, or no field specified. When no field is
          specified, the projected coordinate system used for calculation will be taken
          from the Cartography environment settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateGridConvergenceAngle_cartography(*gp_fixargs((in_features, angle_field, rotation_method, coordinate_sys_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateUTMZone_cartography', None)
def CalculateUTMZone(in_features=None, in_field=None):
    """CalculateUTMZone_cartography(in_features, in_field)

        Calculates a UTM zone of each feature based on the center point and stores this
        spatial reference string in a specified field. This field can be used in
        conjunction with Data Driven Pages to update the spatial reference to the
        correct UTM zone for each map.

     INPUTS:
      in_features (Feature Layer):
          Input feature layer.
      in_field (Field):
          String field that stores the spatial reference string for the coordinate
          system. Field should have sufficient length (more than 600 characters) to hold
          the spatial reference string."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateUTMZone_cartography(*gp_fixargs((in_features, in_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GridIndexFeatures_cartography', None)
def GridIndexFeatures(out_feature_class=None, in_features=None, intersect_feature=None, use_page_unit=None, scale=None, polygon_width=None, polygon_height=None, origin_coord=None, number_rows=None, number_columns=None, starting_page_number=None, label_from_origin=None):
    """GridIndexFeatures_cartography(out_feature_class, {in_features;in_features...}, {intersect_feature}, {use_page_unit}, {scale}, {polygon_width}, {polygon_height}, {origin_coord}, {number_rows}, {number_columns}, {starting_page_number}, {label_from_origin})

        Creates a grid of rectangular polygon features that can be used as an index to
        specify pages for a map book using Data Driven Pages. A grid can be created that
        only includes polygon features that intersect another feature layer.

     INPUTS:
      in_features {Feature Layer / Raster Layer}:
          Input features can be used to define the extent of the polygon grid that is
          created.
      intersect_feature {Boolean}:
          Limits the output grid feature class to only areas that intersect input feature
          layers or datasets. When input features are specified, the default value is
          INTERSECTFEATURE. The intersection of input features will be used to create
          index features.

          * INTERSECTFEATURE—Limits the output grid feature class to only areas that
          intersect input feature layers or datasets.

          * NO_INTERSECTFEATURE—Output grid feature class is created using specified
          coordinates, rows, and columns.
      use_page_unit {Boolean}:
          Indicates whether index polygon size input is in page units. The default is
          NO_USEPAGEUNIT. The tool uses map units by default.

          * USEPAGEUNIT—Index polygon height and width are calculated in page units.

          * NO_USEPAGEUNIT—Index polygon height and width are calculated in map units.
      scale {Long}:
          Scale must be specified if the index polygon height and width are to be
          calculated in page units. If the tool is being used outside of an active ArcMap
          session the default scale value is 1.
      polygon_width {Linear unit}:
          Width of the index polygon specifed in either map or page units. If page units
          are being used the default value is 1 inch. If map units are being used the
          default is 1 degree.
      polygon_height {Linear unit}:
          Height of the index polygon specifed in either map or page units. If page units
          are being used the default value is 1 inch. If map units are being used the
          default is 1 degree.
      origin_coord {Point}:
          Coordinate for the lower left origin of the output grid feature class. If input
          features are specified the default value is determined by the extent of the
          union of extents for these features. If there are no input features specified,
          the default coordinates are 0 and 0.
      number_rows {Long}:
          Number of rows to create in the y direction from the point of origin. The
          default is 10.
      number_columns {Long}:
          Number of columns to create in the x direction from the point of origin. The
          default is 10.
      starting_page_number {Long}:
          Each grid index feature is assigned a sequential page number starting with a
          specified starting page number. The default is 1.
      label_from_origin {Boolean}:
          Page numbers (labels) starting with the specified starting page number (default
          is 1) begins with the cell in the lower left corner of the output grid. The
          default is NO_LABELFROMORIGIN.

          * LABELFROMORIGIN—Page numbers (labels) starting with the specified starting
          page number (default is 1) begins with the polygon feature in the lower left
          corner of the output grid.

          * NO_LABELFROMORIGIN—Page numbers (labels) starting with the specified starting
          page number (default is 1) begins with the cell in the upper left corner of the
          output grid.

     OUTPUTS:
      out_feature_class (Feature Class):
          Resulting feature class of polygon index features.The coordinate system of the
          ouput feature class is determined in this order.

          * If a coordinate system is specified by the Output Coordinate System variable
          in the Environment Settings the output feature class will use this coordinate
          system.

          * If a coordinate system is not specified by the Output Coordinate System the
          output feature class will use the coordinate system of the active data frame
          (ArcMap is open).

          * If a coordinate system is not specified by the Output Coordinate System and
          there is no active data frame (ArcMap is not open) the ouput feature class will
          use the coordinate system of the first input feature.

          * If a coordinate system is not specified by the Output Coordinate System, there
          is no active data frame (ArcMap is not open) and there is no specified input
          features the coordinate system of the ouput feature class will be unknown."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GridIndexFeatures_cartography(*gp_fixargs((out_feature_class, in_features, intersect_feature, use_page_unit, scale, polygon_width, polygon_height, origin_coord, number_rows, number_columns, starting_page_number, label_from_origin), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('StripMapIndexFeatures_cartography', None)
def StripMapIndexFeatures(in_features=None, out_feature_class=None, use_page_unit=None, scale=None, length_along_line=None, length_perpendicular_to_line=None, page_orientation=None, overlap_percentage=None, starting_page_number=None, direction_type=None):
    """StripMapIndexFeatures_cartography(in_features, out_feature_class, {use_page_unit}, {scale}, {length_along_line}, {length_perpendicular_to_line}, {page_orientation}, {overlap_percentage}, {starting_page_number}, {direction_type})

        Creates a series of rectangular polygons, or index features, that follow a
        single linear feature or a group of linear features. These index features can be
        used with Data Driven Pages to define pages within a strip map, or set of maps
        that follow a linear feature. The resulting index features contain attributes
        that can be used to rotate and orient the map on the page and determine which
        index features, or pages, are next to the current page (to the left and right or
        to the top and bottom).

     INPUTS:
      in_features (Feature Layer):
          Input polyline or polylines defining the path of the strip map index features.
      use_page_unit {Boolean}:
          Indicates whether index feature size input is in page space. The default value
          is NO_USEPAGEUNIT.

          * USEPAGEUNIT—Index polygon height and width are calculated in page space.

          * NO_USEPAGEUNIT—Index polygon height and width are calculated in map space.
      scale {Long}:
          Map scale must be specified if index feature lengths (along the line and
          perpendicular to the line) are to be calculated in page space. If ArcMap is open
          the default value will be the scale of the active data frame. If ArcMap is not
          open the default will be 1.
      length_along_line {Linear unit}:
          Length of the polygon index feature along the input line feature specifed in
          either map or page units. The default value is determined by the spatial
          reference of the input line feature or features. This value will be 1/100 of the
          input feature class extent along the X axis.
      length_perpendicular_to_line {Linear unit}:
          Length of the polygon index feature perpendicular to the input line feature
          specifed in either map or page units. The default value is determined by the
          spatial reference of the input line feature or features. This value will be 1/2
          the number used for the length along the line.
      page_orientation {String}:
          Used to determine the orientation of the input line features on the layout
          page. The default is HORIZONTAL.

          * VERTICAL—The direction of the strip map series on the page is top to bottom.

          * HORIZONTAL—The direction of the strip map series on the page is left to right.
      overlap_percentage {Double}:
          The approximate percentage of geographic overlap between an individual map page
          and its adjoining pages in the series. The default is 10.
      starting_page_number {Long}:
          Each grid index feature is assigned a sequential page number starting with a
          specified starting page number. The default value is 1.
      direction_type {String}:
          Index features are created in a sequential order and require a starting point.
          Setting the direction type for the strip map provides a starting point. The
          default is WE_NS. This means that the starting point for the strip map is either
          at the western end of the line feature if the line feature's directional trend
          is West to East/East to West or, if the directional trend is North to
          South/South to North, the starting point would be the northern most point of the
          line feature. The direction type is also applied to secondary line features.

          * WE_NS—West to East and North to South.

          * WE_SN— West to East and South to North.

          * EW_NS— East to West and North to South.

          * EW_SN— East to West and South to North.

     OUTPUTS:
      out_feature_class (Feature Class):
          Resulting feature class of polygon index features.The coordinate system of the
          ouput feature class is determined in this order.

          * If a coordinate system is specified by the Output Coordinate System variable
          in the Environment Settings the output feature class will use this coordinate
          system.

          * If a coordinate system is not specified by the Output Coordinate System the
          ouput feature class will use the coordinate system of the input feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.StripMapIndexFeatures_cartography(*gp_fixargs((in_features, out_feature_class, use_page_unit, scale, length_along_line, length_perpendicular_to_line, page_orientation, overlap_percentage, starting_page_number, direction_type), True)))
        return retval
    except Exception, e:
        raise e


# Generalization toolset
@gptooldoc('AggregatePoints_cartography', None)
def AggregatePoints(in_features=None, out_feature_class=None, aggregation_distance=None):
    """AggregatePoints_cartography(in_features, out_feature_class, aggregation_distance)

        Creates polygon features around clusters of proximate point features.

     INPUTS:
      in_features (Feature Layer):
          The input point features that will be assessed for proximity and clustering.
      aggregation_distance (Linear unit):
          The distance between points that will be clustered.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class created to hold the polygons that represent the point
          clusters."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AggregatePoints_cartography(*gp_fixargs((in_features, out_feature_class, aggregation_distance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AggregatePolygons_cartography', None)
def AggregatePolygons(in_features=None, out_feature_class=None, aggregation_distance=None, minimum_area=None, minimum_hole_size=None, orthogonality_option=None, barrier_features=None, out_table=None):
    """AggregatePolygons_cartography(in_features, out_feature_class, aggregation_distance, {minimum_area}, {minimum_hole_size}, {orthogonality_option}, {barrier_features;barrier_features...}, {out_table})

        Combines polygons within a specified distance of each other into new polygons.

     INPUTS:
      in_features (Feature Layer):
          The polygon features to be aggregated. If this is a layer referencing a
          representation and shape overrides are present on the input features, the
          overridden shapes, not the feature shapes, will be considered in aggregation
          processing.
      aggregation_distance (Linear unit):
          The distance to be satisfied between polygon boundaries for aggregation to
          happen. A distance must be specified, and it must be greater than zero. You can
          choose a preferred unit; the default is the feature unit.
      minimum_area {Areal unit}:
          The minimum area for an aggregated polygon to be retained. The default value is
          zero, that is, to keep all polygons. You can specify a preferred unit; the
          default is the feature unit.
      minimum_hole_size {Areal unit}:
          The minimum size of a polygon hole to be retained. The default value is zero,
          that is, to keep all polygon holes. You can specify a preferred unit; the
          default is the feature unit.
      orthogonality_option {Boolean}:
          Specifies the characteristic of the output features when constructing the
          aggregated boundaries.

          * NON_ORTHOGONAL—Organically shaped output features will be created. This is
          suitable for natural features, such as vegetation or soil polygons. This is the
          default.

          * ORTHOGONAL—Orthogonally shaped output features will be created. This option is
          suitable for preserving the geometric characteristic of anthropogenic input
          features, such as building footprints.
      barrier_features {Feature Layer}:
          The layers containing the line or polygon features that are aggregation
          barriers for input features. Features will not be aggregated across barrier
          features. Barrier features that are in geometric conflict with input features
          will be ignored.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created.
      out_table {Table}:
          A one-to-many relationship table that links the aggregated polygons to their
          source polygon features. This table contains two fields, OUTPUT_FID and
          INPUT_FID, storing the aggregated feature IDs and their source feature IDs,
          respectively. Use this table to derive necessary attributes for the output
          features from their source features. The default name for this table is the name
          of the output feature class, appended with _tbl. The default path is the same as
          the output feature class. No table is created when this parameter is left blank."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AggregatePolygons_cartography(*gp_fixargs((in_features, out_feature_class, aggregation_distance, minimum_area, minimum_hole_size, orthogonality_option, barrier_features, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CollapseDualLinesToCenterline_cartography', None)
def CollapseDualLinesToCenterline(in_features=None, out_feature_class=None, maximum_width=None, minimum_width=None):
    """CollapseDualLinesToCenterline_cartography(in_features, out_feature_class, maximum_width, {minimum_width})

        Derives centerlines from dual-line (or double-line) features, such as road
        casings, based on specified width tolerances.

     INPUTS:
      in_features (Feature Layer):
          The input dual-line features, such as road casings, from which centerlines are
          derived.
      maximum_width (Linear unit):
          Sets the maximum width of the dual-line features to derive centerline. A value
          must be specified, and it must be greater than zero. You can choose a preferred
          unit; the default is the feature unit.
      minimum_width {Linear unit}:
          Sets the minimum width of the dual-line features to derive centerline. The
          minimum width must be greater than or equal to zero, and it must be less than
          the maximum width. The default value is zero. You can specify a preferred unit;
          the default is the feature unit.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CollapseDualLinesToCenterline_cartography(*gp_fixargs((in_features, out_feature_class, maximum_width, minimum_width), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CollapseRoadDetail_cartography', None)
def CollapseRoadDetail(in_features=None, collapse_distance=None, output_feature_class=None):
    """CollapseRoadDetail_cartography(in_features, collapse_distance, output_feature_class)

        Collapses small, open configurations of road segments that interrupt the
        general trend of a road network, such as traffic circles, for example, and
        replaces them with a simplified depiction.Configurations are collapsed
        regardless of road class if the diameter across the
        open area is less than or equal to the Collapse Distance  parameter. All
        uncollapsed roads from the input collection are copied to the output feature
        class.To learn more, see How Collapse Road Detail works.This tool is generally
        used to simplify a relatively large-scale road collection
        at a smaller scale, where it is appropriate to depict traffic circles or other
        small interruptions to the network as a simple intersection. At medium scales,
        it may be preferable to retain these configurations as separate features and
        possibly exaggerate them. In that case, consider using the Resolve Road
        Conflicts tool instead to ensure that symbolized lines are displayed without
        symbol conflicts. If both Resolve Road Conflicts and Collapse Road Detail tools
        will be run on the same collection of roads, it is advisable to run Collapse
        Road Detail first.

     INPUTS:
      in_features (Feature Layer):
          The input features containing small enclosed road details, such as traffic
          circles, to be collapsed.
      collapse_distance (Linear unit):
          The diameter of or distance across the road detail that is to be considered for
          collapse.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output feature class containing the collapsed features—features that were
          modified to accommodate the collapse—and all unaffected features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CollapseRoadDetail_cartography(*gp_fixargs((in_features, collapse_distance, output_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateCartographicPartitions_cartography', None)
def CreateCartographicPartitions(in_features=None, out_features=None, feature_count=None):
    """CreateCartographicPartitions_cartography(in_features;in_features..., out_features, feature_count)

        Creates a mesh of polygon features that cover the input feature class where
        each polygon encloses no more than a specified number of input features,
        determined by the density and distribution of the input features. The resulting
        partition feature class is ideally suited for the Cartographic
        Partitions geoprocessing environment setting. The Cartographic Partitions
        environment setting dictates to certain generalization or conflict-resolution
        geoprocessing tools to load and process input features by partition. These tools
        operate contextually, meaning that multiple features, possibly from multiple
        themes, must be loaded simultaneously. Memory limitations are encountered with
        large datasets. Partitioning allows large datasets to be processed by these
        tools in portions sequentially.

     INPUTS:
      in_features (Feature Layer):
          The input feature classes or layers whose feature distribution and density
          dictate the size and arrangement of output polygons. The input features are
          typically destined for subsequent processing with contextual generalization or
          conflict resolution geoprocessing tools. Typically, the input features, when
          considered simultaneously, would exceed memory limitations of generalization or
          conflict-resolution geoprocessing tools, so partitions are created to subdivide
          inputs for processing.
      feature_count (Long):
          The ideal number of features to be enclosed by each polygon in the output
          feature class.  The recommended count is 50,000 features, which is the default
          value. The feature count cannot be lower than 500.

     OUTPUTS:
      out_features (Feature Class):
          The output polygon feature class of partitions, each of which encloses a
          manageable number of input features not exceeding the number specified by the
          Feature Count parameter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateCartographicPartitions_cartography(*gp_fixargs((in_features, out_features, feature_count), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DelineateBuiltUpAreas_cartography', None)
def DelineateBuiltUpAreas(in_buildings=None, identifier_field=None, edge_features=None, grouping_distance=None, minimum_detail_size=None, out_feature_class=None, minimum_building_count=None):
    """DelineateBuiltUpAreas_cartography(in_buildings;in_buildings..., {identifier_field}, {edge_features;edge_features...}, grouping_distance, minimum_detail_size, out_feature_class, {minimum_building_count})

        Creates polygons to represent built-up areas by delineating densely clustered
        arrangements of buildings on small-scale maps.The boundaries—or edges—of the
        output polygons can be dictated by the location
        of other features such as roads or hydrology. Input buildings can be attributed
        to identify which can be replaced in maps by the built-up area polygons for a
        more generalized depiction.

     INPUTS:
      in_buildings (Feature Layer):
          The layers containing buildings whose density and arrangement are used to
          define appropriate output built-up polygons. Multiple building layers can be
          assessed simultaneously. Building features can be points or polygons.
      identifier_field {String}:
          A field on the input feature classes that will hold a status code indicating
          whether the input feature is part of the resulting built-up area . This field
          must be either short or long integer type and common in all input layers, if
          multiple input layers are used.

          * 0 = The building is not represented by an output built-up area polygon.

          * 1 = The building is represented by an output built-up area polygon and is
          within the resulting polygon.

          * 2 = The building is represented by an output built-up area polygon and is
          outside the resulting polygon.
      edge_features {Feature Layer}:
          The output feature class containing built-up area polygons representing
          clustered arrangements of input buildings.
      grouping_distance (Linear unit):
          Buildings closer together than the grouping distance are considered
          collectively as candidates for representation by an output built-up area
          polygon. This distance is measured from the edges of polygon buildings and the
          centers of point buildings.
      minimum_detail_size (Linear unit):
          Defines the relative degree of detail in the output built-up area polygons.
          This roughly translates to the minimum allowable diameter of a hole or cavity in
          the built-up area polygon. The actual size and shape of holes and cavities
          within the polygon is determined also by the arrangement of the input buildings,
          the grouping distance, and the presence of edge features, if they are used.
      minimum_building_count {Long}:
          The minimum number of buildings that must be collectively considered for
          representation by an output built-up area polygon. The default value is 4. The
          minimum building count must be greater than or equal to 0.

     OUTPUTS:
      out_feature_class (Feature Class):
          The layers that can be used to define the edges of the built-up area polygons.
          Typically, these are roads, but other common examples are rivers, coastlines, or
          administrative areas. Built-up area polygons snap to an edge feature if one is
          generally aligned with the trend of the polygon edge and within the grouping
          distance away. Edge features can be lines or polygons."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DelineateBuiltUpAreas_cartography(*gp_fixargs((in_buildings, identifier_field, edge_features, grouping_distance, minimum_detail_size, out_feature_class, minimum_building_count), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MergeDividedRoads_cartography', None)
def MergeDividedRoads(in_features=None, merge_field=None, merge_distance=None, out_features=None, out_displacement_features=None):
    """MergeDividedRoads_cartography(in_features, merge_field, merge_distance, out_features, {out_displacement_features})

        Generates single-line road features in place of matched pairs of divided road
        lanes.Matched pairs of roads or lanes are merged if they are the same road
        class,
        trend generally parallel to one another, and are within the merge distance
        apart. The road class is specified by the Merge Field parameter. All nonmerged
        roads from the input collection are copied to the output feature class.This tool
        is generally used to simplify a relatively large-scale road collection
        at a smaller scale, where it is appropriate to depict divided highways and
        boulevards as a single line. At medium scales, it may be preferable to retain
        divided roads as separate features. In this case, you can use the Resolve Road
        Conflicts tool instead to ensure that symbolized lanes are displayed without
        symbol conflicts. If both Resolve Road Conflicts and Merge Divided Roads tools
        will be run on the same collection of roads, it is advisable to run Merge
        Divided Roads first. A warning is raised if the input features are not in a
        projected coordinate
        system. This tool relies on linear distance units, which will create unexpected
        results in an unprojected coordinate system. It is strongly suggested that you
        run this tool on data in a projected coordinate system to ensure valid results.
        An error is raised and the tool will not process if the coordinate system is
        missing or unknown.

     INPUTS:
      in_features (Feature Layer):
          The input linear road features that contain matched pairs of divided road lanes
          that should be merged together to a single output line feature.
      merge_field (Field):
          The field that contains road classification information. Only parallel,
          proximate roads of equal classification will be merged. A value of 0 (zero)
          locks a feature to prevent it from participating in merging.
      merge_distance (Linear unit):
          The minimum distance apart, in the specified units, for equal-class, relatively
          parallel road features to be merged. This distance must be greater than zero. If
          the units are in pt, mm, cm, or in, the value is considered as page units and
          takes into account the reference scale.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class containing single-line merged road features and all
          unmerged road features.
      out_displacement_features {Feature Class}:
          The output polygon features containing the degree and direction of road
          displacement, to be used by the Propagate Displacement tool to preserve spatial
          relationships."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MergeDividedRoads_cartography(*gp_fixargs((in_features, merge_field, merge_distance, out_features, out_displacement_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimplifyBuilding_cartography', None)
def SimplifyBuilding(in_features=None, out_feature_class=None, simplification_tolerance=None, minimum_area=None, conflict_option=None):
    """SimplifyBuilding_cartography(in_features, out_feature_class, simplification_tolerance, {minimum_area}, {conflict_option})

        Simplifies the boundary or footprint of building polygons while maintaining
        their essential shape and size.

     INPUTS:
      in_features (Feature Layer):
          The building polygons to be simplified.
      simplification_tolerance (Linear unit):
          Sets the tolerance for building simplification. A tolerance must be specified,
          and it must be greater than zero. You can choose a preferred unit; the default
          is the feature unit.
      minimum_area {Areal unit}:
          Sets the minimum area for a simplified building to be retained in feature units.
          The default value is zero, that is, to keep all buildings. You can specify a
          preferred unit; the default is the feature unit.
      conflict_option {Boolean}:
          Specifies whether or not to check for potential conflicts, that is, overlapping
          or touching, among buildings. A field named SimBldFlag is added to the output to
          store conflict flags. A value of 0 means no conflict; a value of 1 means
          conflict.

          * NO_CHECK—Specifies not to check for potential conflicts; the resulting
          buildings may overlap. This is the default.

          * CHECK_CONFLICTS—Specifies to check for potential conflicts; the conflicting
          buildings will be flagged.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimplifyBuilding_cartography(*gp_fixargs((in_features, out_feature_class, simplification_tolerance, minimum_area, conflict_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimplifyLine_cartography', None)
def SimplifyLine(in_features=None, out_feature_class=None, algorithm=None, tolerance=None, error_resolving_option=None, collapsed_point_option=None, error_checking_option=None):
    """SimplifyLine_cartography(in_features, out_feature_class, algorithm, tolerance, {error_resolving_option}, {collapsed_point_option}, {error_checking_option})

        Simplifies lines by removing extraneous bends while preserving essential shape.

     INPUTS:
      in_features (Feature Layer):
          The line features to be simplified.
      algorithm (String):
          Specifies the line simplification algorithm.

          * POINT_REMOVE—Retains critical points that depict the essential shape of a line
          and removes all other points. This is the default.

          * BEND_SIMPLIFY—Retains the critical bends in a line and removes extraneous
          bends.
      tolerance (Linear unit):
          The tolerance that determines the degree of simplification. A tolerance must be
          specified, and it must be greater than zero. You can choose a preferred unit;
          the default is the feature unit.

          * For the POINT_REMOVE algorithm, the tolerance you specify is the maximum
          allowable offset of each vertex from its original location. This value may be
          reduced locally in some areas when the option is used to resolve topological
          errors.

          * For the BEND_SIMPLIFY algorithm, the tolerance you specify is the length of
          the reference bend baseline.
      error_resolving_option {Boolean}:
          Specifies how the topological errors (possibly introduced in the process,
          including line crossing, line overlapping, and collapsed zero-length lines) will
          be handled. This parameter will be in effect when error_checking_option =
          "CHECK" (the default).

          * FLAG_ERRORS—Specifies to flag topological errors, if any are found. This is
          the default.

          * RESOLVE_ERRORS—Specifies to resolve topological errors, if any are found.
      collapsed_point_option {Boolean}:
          Specifies whether to keep collapsed zero-length lines as points if any are found
          in the process. This option applies only when NO_CHECK is specified or when both
          FLAG_ERRORS and CHECK options are specified.

          * KEEP_COLLAPSED_POINTS—Specifies to keep the collapsed zero-length lines as
          points. The endpoints of the collapsed lines will be stored in a point feature
          class at the output feature class location, taking the name of the output
          feature class plus a suffix _Pnt. This is the default.

          * NO_KEEP—Specifies not to keep the collapsed zero-length lines as points even
          if they are found in the process; therefore, the point feature class will be
          empty.
      error_checking_option {Boolean}:
          Specifies how the topological errors (possibly introduced in the process,
          including line crossing, line overlapping, and collapsed zero-length lines) will
          be handled.

          * CHECK—Specifies to check for topological errors and enables the
          error_resolving_option parameter. This is the default.

          * NO_CHECK—Specifies not to check for topological errors and disables the
          error_resolving_option parameter.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimplifyLine_cartography(*gp_fixargs((in_features, out_feature_class, algorithm, tolerance, error_resolving_option, collapsed_point_option, error_checking_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimplifyPolygon_cartography', None)
def SimplifyPolygon(in_features=None, out_feature_class=None, algorithm=None, tolerance=None, minimum_area=None, error_option=None, collapsed_point_option=None):
    """SimplifyPolygon_cartography(in_features, out_feature_class, algorithm, tolerance, {minimum_area}, {error_option}, {collapsed_point_option})

        Simplifies polygons by removing extraneous bends while preserving essential
        shape.

     INPUTS:
      in_features (Feature Layer):
          The polygon features to be simplified.
      algorithm (String):
          Specifies the polygon simplification algorithm.

          * POINT_REMOVE—Keeps the so-called critical points that depict the essential
          shape of a polygon and removes all other points. This is the default.

          * BEND_SIMPLIFY—Keeps the main shape of a polygon and removes extraneous bends
          in the boundary.
      tolerance (Linear unit):
          The tolerance that determines the degree of simplification. A tolerance must be
          specified, and it must be greater than zero. You can choose a preferred unit;
          the default is the feature unit.

          * For POINT_REMOVE algorithm, the tolerance you specify is the maximum allowable
          offset.

          * For BEND_SIMPLIFY algorithm, the tolerance you specify is the length of the
          reference bend baseline.
      minimum_area {Areal unit}:
          Sets the minimum area for a simplified polygon to be retained. The default value
          is zero, that is, to keep all polygons. You can choose a preferred unit for the
          specified value; the default is the feature unit.
      error_option {String}:
          Specifies how the topological errors (possibly introduced in the process,
          including line crossing, line overlapping, and collapsed zero-length lines) will
          be handled.

          * NO_CHECK—Specifies not to check topological errors. This is the default.

          * FLAG_ERRORS—Specifies to flag topological errors if any are found.

          * RESOLVE_ERRORS—Specifies to resolve topological errors if any are found.
      collapsed_point_option {Boolean}:
          Specifies whether to keep collapsed zero-area polygons as points if any are
          found in the process. This option applies only when NO_CHECK or FLAG_ERRORS is
          specified.

          * KEEP_COLLAPSED_POINTS—Specifies to keep the collapsed zero-area polygons as
          points. The endpoints of the collapsed polygon boundaries will be stored in a
          point feature class at the output feature class location, taking the name of the
          output feature class plus a suffix _Pnt. This is the default.

          * NO_KEEP—Specifies not to keep the collapsed zero-area polygons as points even
          if they are found in the process; therefore, the point feature class will be
          empty.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimplifyPolygon_cartography(*gp_fixargs((in_features, out_feature_class, algorithm, tolerance, minimum_area, error_option, collapsed_point_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SmoothLine_cartography', None)
def SmoothLine(in_features=None, out_feature_class=None, algorithm=None, tolerance=None, endpoint_option=None, error_option=None):
    """SmoothLine_cartography(in_features, out_feature_class, algorithm, tolerance, {endpoint_option}, {error_option})

        Smooths sharp angles in lines to improve aesthetic or cartographic quality.

     INPUTS:
      in_features (Feature Layer):
          The line features to be smoothed.
      algorithm (String):
          Specifies the smoothing algorithm.

          * PAEK—Acronym for Polynomial Approximation with Exponential Kernel. It
          calculates a smoothed line that will not pass through the input line vertices.
          This is the default.

          * BEZIER_INTERPOLATION—Fits Bezier curves between vertices. The resulting line
          passes through the vertices of the input line. This algorithm does not require a
          tolerance. Bezier curves will be approximated in shapefile output.
      tolerance (Linear unit):
          Sets a tolerance used by the PAEK algorithm. A tolerance must be specified, and
          it must be greater than zero. You can choose a preferred unit; the default is
          the feature unit. You must enter a 0 as a placeholder when using the
          BEZIER_INTERPOLATION smoothing algorithm.
      endpoint_option {Boolean}:
          Specifies whether to preserve the endpoints for closed lines. This option works
          with the PAEK algorithm only.

          * FIXED_CLOSED_ENDPOINT—Preserves the endpoint of a closed line. This is the
          default.

          * NO_FIXED—Smooths through the endpoint of a closed line.
      error_option {String}:
          Specifies how the topological errors (possibly introduced in the process, such
          as line crossing) will be handled.

          * NO_CHECK—Specifies not to check for topological errors. This is the default.

          * FLAG_ERRORS—Specifies to flag topological errors, if any are found.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SmoothLine_cartography(*gp_fixargs((in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SmoothPolygon_cartography', None)
def SmoothPolygon(in_features=None, out_feature_class=None, algorithm=None, tolerance=None, endpoint_option=None, error_option=None):
    """SmoothPolygon_cartography(in_features, out_feature_class, algorithm, tolerance, {endpoint_option}, {error_option})

        Smooths sharp angles in polygon outlines to improve aesthetic or cartographic
        quality.

     INPUTS:
      in_features (Feature Layer):
          The polygon features to be smoothed.
      algorithm (String):
          Specifies the smoothing algorithm.

          * PAEK—Acronym for Polynomial Approximation with Exponential Kernel. It
          calculates a smoothed polygon that will not pass through the input polygon
          vertices. This is the default.

          * BEZIER_INTERPOLATION—Fits Bezier curves between vertices. The resulting
          polygon passes through the vertices of input polygons. This algorithm does not
          require a tolerance. Bezier curves will be approximated in shapefile output.
      tolerance (Linear unit):
          Sets a tolerance used by the PAEK algorithm. A tolerance must be specified, and
          it must be greater than zero. You can specify a preferred unit; the default is
          the feature unit. You must enter a 0 as a placeholder when using the
          BEZIER_INTERPOLATION smoothing algorithm.
      endpoint_option {Boolean}:
          Specifies whether or not to preserve the endpoints for isolated polygon rings.
          This option works with the PAEK algorithm only.

          * FIXED_ENDPOINT—Preserves the endpoint of an isolated polygon ring. This is the
          default.

          * NO_FIXED—Smooths through the endpoint of an isolated polygon ring.
      error_option {String}:
          Specifies how the topological errors (possibly introduced in the process, such
          as line crossing or overlapping) will be handled.

          * NO_CHECK—Specifies not to check for topological errors. This is the default.

          * FLAG_ERRORS—Specifies to flag topological errors, if any are found.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SmoothPolygon_cartography(*gp_fixargs((in_features, out_feature_class, algorithm, tolerance, endpoint_option, error_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ThinRoadNetwork_cartography', None)
def ThinRoadNetwork(in_features=None, minimum_length=None, invisibility_field=None, hierarchy_field=None):
    """ThinRoadNetwork_cartography(in_features;in_features..., minimum_length, invisibility_field, hierarchy_field)

        Generates a simplified road network that retains connectivity and general
        character for display at a smaller scale.This tool does not generate new output.
        It assigns values in Invisibility Field
        in the input feature classes to identify features that are extraneous and can be
        removed from view to result in a simplified, yet representative, collection of
        roads. No feature geometry is altered or deleted.Features are not actually
        deleted by Thin Road Network. To actually remove
        features, consider using the Trim Line tool.The resulting simplified road
        collection is determined by feature significance,
        importance, and density. Segments that participate in very long itineraries
        across the extent of the data are more significant than those required only for
        local travel. Road classification, or importance, is specified by the Hierarchy
        Field parameter. The density of the resulting street network is determined by
        the Minimum Length parameter, which corresponds to the shortest segment that is
        visually sensible to show at scale. Learn more about how Thin Road Network works
        and see a table of recommended
        minimum length values to use as a starting point. A warning is raised if the
        input features are not in a projected coordinate
        system. This tool relies on linear distance units, which will create unexpected
        results in an unprojected coordinate system. It is strongly suggested that you
        run this tool on data in a projected coordinate system to ensure valid results.
        An error is raised and the tool will not process if the coordinate system is
        missing or unknown.

     INPUTS:
      in_features (Feature Layer):
          The input linear roads that should be thinned to create a simplified collection
          for display at smaller scales.
      minimum_length (Linear unit):
          An indication of the shortest road segment that is sensible to display at the
          output scale. This controls the resolution, or density, of the resulting road
          collection. If the units are in point, millimeters, centimeters, or inches, the
          value is considered in page units and the reference scale is taken into account.
      invisibility_field (String):
          The field that stores the results of the tool. Features that participate in the
          resulting simplified road collection have a value of 0 (zero). Those that are
          extraneous have a value of 1. A layer definition query can be used to display
          the resulting road collection. This field must be present and named the same for
          each input feature class.
      hierarchy_field (String):
          The field that contains hierarchical ranking of feature importance, where 1 is
          very important and larger integers reflect decreasing importance. A value of 0
          forces the feature to remain visible in the output collection. This field must
          be present and named the same for each input feature class. Hierarchy values
          equal to NULL are not accepted and will raise an error."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ThinRoadNetwork_cartography(*gp_fixargs((in_features, minimum_length, invisibility_field, hierarchy_field), True)))
        return retval
    except Exception, e:
        raise e


# Graphic Conflicts toolset
@gptooldoc('DetectGraphicConflict_cartography', None)
def DetectGraphicConflict(in_features=None, conflict_features=None, out_feature_class=None, conflict_distance=None, line_connection_allowance=None):
    """DetectGraphicConflict_cartography(in_features, conflict_features, out_feature_class, {conflict_distance}, {line_connection_allowance})

        Creates polygons where two or more symbolized features graphically conflict.

     INPUTS:
      in_features (Layer):
          The input feature layer containing symbolized features. CAD, coverage, or VPF
          annotation, dimensions, charts, dot-density or proportional symbols, raster
          layers, network datasets, or 3D symbols are not acceptable inputs.
      conflict_features (Layer):
          The feature layer containing symbolized features potentially in conflict with
          symbolized features in the input layer.
      conflict_distance {Linear unit}:
          Sets the conflict distance. Temporary buffers one-half the size of the conflict
          distance value are created around symbols in both the input and conflict layers.
          Conflict polygons will be generated where these buffers overlap. Conflict
          distance is measured in page units (Points, Inches, Millimeters, Centimeters).
          If you enter a conflict distance in map units, it will be converted to page
          units using the reference scale. The default conflict distance is 0, where no
          buffers are created and only symbols that physically overlap one another are
          detected as conflicts.
      line_connection_allowance {Linear unit}:
          The radius of a circle, centered where lines join, within which graphic overlaps
          won't be detected. This parameter is only considered when the input layer and
          the conflict layer are identical. Zero allowance will detect a conflict at each
          line join (if end caps are overlapping). Line connection allowance is calculated
          in page units (Points, Inches, Millimeters, Centimeters). If you enter a
          conflict distance in map units, it will be converted to page units using the
          reference scale. The value cannot be negative; the default value is 1 Point.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created to store conflict polygons. It cannot be
          one of the feature classes associated with the input layers."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DetectGraphicConflict_cartography(*gp_fixargs((in_features, conflict_features, out_feature_class, conflict_distance, line_connection_allowance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PropagateDisplacement_cartography', None)
def PropagateDisplacement(in_features=None, displacement_features=None, adjustment_style=None):
    """PropagateDisplacement_cartography(in_features, displacement_features, adjustment_style)

        Propagates the displacement resulting from road adjustment in the Resolve Road
        Conflicts and Merge Divided Roads tools to adjacent features to reestablish
        spatial relationships.An optional output of both the Resolve Road Conflicts and
        Merge Divided Roads
        tools is a displacement feature class. Displacement features store the amount
        and direction of change from the initial state of the data before these tools
        are run. Displacement information can then be applied to nearby features from
        different themes to ensure that spatial relationships are retained using this
        tool. For example, if roadways are separated by the Resolve Road Conflicts tool,
        it is often necessary to shift adjacent buildings along the roads
        accordingly.This tool does not produce output layers but instead alters the
        source feature
        classes of the input layers. If the input layers are drawn with a representation
        (whose editing behavior is set to store shape overrides), the modified features
        are stored as shape overrides in the representation. If the layer is not drawn
        with a representation, the geometry of the input features is modified. Using
        representations is recommended when working with the conflict resolution tools.
        That way, if the results are not acceptable, or to rerun the tool with different
        parameters, simply remove the overrides using the Remove Override tool. It is
        strongly suggested that you make a copy of your input features if you are not
        using representations whose editing behavior is set to store shape
        overrides.This tool will act cumulatively if run on the same dataset multiple
        times. In
        some cases, features may be moved further and further away from their original
        location, which may lead to unexpected and unwanted results.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer containing features that may be in conflict. May be
          point, line, or polygon.
      displacement_features (Feature Layer):
          The displacement polygon features created by the Resolve Road Conflicts or the
          Merge Divided Roads tools which contain the degree and direction of road
          displacement that took place. These polygons dictate the amount of displacement
          that will be propagated to the input features.
      adjustment_style (String):
          Defines the type of adjustment that will be used when displacing input features.

          * AUTO—The tool will decide for each input feature whether a SOLID or an ELASTIC
          adjustment is most appropriate. In general, features with orthogonal shapes will
          have SOLID adjustment applied, while organically shaped features will have
          ELASTIC adjustment applied. This is the default.

          * SOLID—The feature will be translated. All vertices will move the same distance
          and direction. Topological errors may be introduced. This option is most useful
          when input features have regular geometric shapes.

          * ELASTIC—The vertices of the feature may be moved independently to best fit the
          feature to the road network. The shape of the feature may be modified slightly.
          Topological errors are less likely to be introduced. This option only applies to
          line and polygon input features. This option is most useful for organically
          shaped input features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PropagateDisplacement_cartography(*gp_fixargs((in_features, displacement_features, adjustment_style), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ResolveBuildingConflicts_cartography', None)
def ResolveBuildingConflicts(in_buildings=None, invisibility_field=None, in_barriers=None, building_gap=None, minimum_size=None, hierarchy_field=None):
    """ResolveBuildingConflicts_cartography(in_buildings;in_buildings..., invisibility_field, in_barriers;in_barriers..., building_gap, minimum_size, {hierarchy_field})

        Resolves symbol conflicts among buildings and with respect to linear barrier
        features by moving or hiding buildings.This tool does not produce output layers
        but instead alters the source feature
        classes of the input layers. If the input layers are drawn with a representation
        (whose editing behavior is set to store shape overrides), the modified features
        are stored as shape overrides in the representation. If the layer is not drawn
        with a representation, the geometry of the input features is modified. Using
        representations is recommended when working with the conflict resolution tools.
        That way, if the results are not acceptable, or to rerun the tool with different
        parameters, simply remove the overrides using the Remove Override tool. It is
        strongly suggested that you make a copy of your input features if you are not
        using representations whose editing behavior is set to store shape overrides. A
        warning is raised if the input features are not in a projected coordinate
        system. This tool relies on linear distance units, which will create unexpected
        results in an unprojected coordinate system. It is strongly suggested that you
        run this tool on data in a projected coordinate system to ensure valid results.
        An error is raised and the tool will not process if the coordinate system is
        missing or unknown.

     INPUTS:
      in_buildings (Layer):
          The input layers containing building features that may be in conflict, or
          smaller than allowable size. Buildings can be either points or polygons.
          Buildings will be modified to resolve conflicts with other buildings and with
          barrier features.
      invisibility_field (String):
          The field that stores the invisibility values that can be used to remove some
          buildings from display in order to resolve symbol conflicts. Buildings with a
          value of 1 should be removed from display; those with a value of zero should
          remain. Use a definition query on the layer to display visible buildings only.
          No features are deleted.
      in_barriers (Value Table):
          The layers containing the linear or polygon features that are conflict barriers
          for input building features. Buildings will be modified to resolve conflicts
          between buildings and barriers. Orient value is Boolean, specifying whether
          buildings should be oriented to the barrier layer.Gap specifies the distance
          that buildings should move toward or away from the
          barrier layer. A unit must be entered with the value.

          * A gap value of 0 (zero) will snap buildings directly to the edge of barrier
          line or outline symbology.

          * A null (unspecified) gap value will mean that buildings will not be moved
          toward or away from barrier lines or outlines except for movement required by
          conflict resolution.
          If no unit is entered with the Gap value (that is, 10 instead of 10 meters), the
          linear unit from the input feature's coordinate system will be used.
      building_gap (Linear unit):
          The minimum allowable distance between symbolized buildings at scale. Buildings
          that are closer together will be displaced or hidden to enforce this distance.
          The minimum allowable distance is set relative to the reference scale (that is,
          15 meters at 1:50,000 scale). The value is 0 if reference scale is not set.
      minimum_size (Linear unit):
          The minimum allowable size of the shortest side of a rotated best-fit bounding
          box around the symbolized building feature drawn at the reference scale.
          Buildings with a bounding box side smaller than this value will be enlarged to
          meet it. Resizing may happen nonproportionally resulting in a change to building
          morphology.
      hierarchy_field {String}:
          The field that contains hierarchical ranking of feature importance, where 1 is
          very important and larger integers reflect decreasing importance. A value of 0
          (zero) forced the building to retain visibility, although it may be moved
          somewhat to resolve conflicts. If this parameter is not used, feature importance
          will be assessed by the tool based on perimeter length and proximity to barrier
          features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ResolveBuildingConflicts_cartography(*gp_fixargs((in_buildings, invisibility_field, in_barriers, building_gap, minimum_size, hierarchy_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ResolveRoadConflicts_cartography', None)
def ResolveRoadConflicts(in_layers=None, hierarchy_field=None, out_displacement_features=None):
    """ResolveRoadConflicts_cartography(in_layers;in_layers..., hierarchy_field, {out_displacement_features})

        Resolves graphic conflicts among symbolized road features by adjusting portions
        of line segments.This tool does not produce output layers but instead alters the
        source feature
        classes of the input layers. If the input layers are drawn with a representation
        (whose editing behavior is set to store shape overrides), the modified features
        are stored as shape overrides in the representation. If the layer is not drawn
        with a representation, the geometry of the input features is modified. Using
        representations is recommended when working with the conflict resolution tools.
        That way, if the results are not acceptable, or to rerun the tool with different
        parameters, simply remove the overrides using the Remove Override tool. It is
        strongly suggested that you make a copy of your input features if you are not
        using representations whose editing behavior is set to store shape overrides. A
        warning is raised if the input features are not in a projected coordinate
        system. This tool relies on linear distance units, which will create unexpected
        results in an unprojected coordinate system. It is strongly suggested that you
        run this tool on data in a projected coordinate system to ensure valid results.
        An error is raised and the tool will not process if the coordinate system is
        missing or unknown.

     INPUTS:
      in_layers (Layer):
          The input feature layers containing symbolized road features that may be in
          conflict.
      hierarchy_field (String):
          The field that contains hierarchical ranking of feature importance, where 1 is
          very important and larger integers reflect decreasing importance. A value of 0
          (zero) locks the feature to ensure that it is not moved. The hierarchy field
          must be present and named the same for all input feature classes.

     OUTPUTS:
      out_displacement_features {Feature Class}:
          The output polygon features containing the degree and direction of road
          displacement, to be used by the Propagate Displacement tool to preserve spatial
          relationships."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ResolveRoadConflicts_cartography(*gp_fixargs((in_layers, hierarchy_field, out_displacement_features), True)))
        return retval
    except Exception, e:
        raise e


# Grids and Graticules toolset
@gptooldoc('DeleteGridsAndGraticules_cartography', None)
def DeleteGridsAndGraticules(in_grid_dataset=None, grid_name=None):
    """DeleteGridsAndGraticules_cartography(in_grid_dataset, grid_name;grid_name...)

        Deletes all the features associated with one or more selected grid and
        graticule layers from a feature dataset.

     INPUTS:
      in_grid_dataset (Feature Dataset):
          The feature dataset location where the grid and graticule layers that can be
          deleted are stored.
      grid_name (String):
          Lists the grid and graticule layers in the feature dataset that can be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteGridsAndGraticules_cartography(*gp_fixargs((in_grid_dataset, grid_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeGridsAndGraticulesLayer_cartography', None)
def MakeGridsAndGraticulesLayer(in_template=None, in_aoi=None, input_feature_dataset=None, output_layer=None, name=None, refscale=None, rotation=None, mask_size=None, xy_tolerance=None, primary_coordinate_system=None, configure_layout=None, ancillary_coordinate_system_1=None, ancillary_coordinate_system_2=None, ancillary_coordinate_system_3=None, ancillary_coordinate_system_4=None):
    """MakeGridsAndGraticulesLayer_cartography(in_template, in_aoi, input_feature_dataset, output_layer, {name}, {refscale}, {rotation}, {mask_size}, {xy_tolerance}, {primary_coordinate_system}, {configure_layout}, {ancillary_coordinate_system_1}, {ancillary_coordinate_system_2}, {ancillary_coordinate_system_3}, {ancillary_coordinate_system_4})

        Creates a grouped layer of feature classes depicting grid, graticule, and
        border features using predefined cartographic specifications. Grid layers are
        ideal for advanced grid definitions which are scale and extent specific.Each
        grid layer can be composed of a mask polygon, clip polygon, segments
        (line), gridlines (line), ticks (line), endpoints (point), points (point), and
        annotation feature classes. These components are stored as features in
        corresponding feature classes. These features classes are saved within a
        specified feature dataset in a geodatabase. There are seven feature classes that
        store the basic components of a grid. Each feature class is named with a three-
        letter prefix that helps identify the grid component the feature class holds.
        These feature classes/components are:

        * ANO_ is the annotation feature class.


        * EPT_ is the endpoints feature class.


        * GLN_ is the gridlines feature class.


        * MSK_ is the masks feature class.


        * PNT_ is the points feature class.


        * SEG_ is the segments feature class.


        * TKS_ is the segments feature class.
        These feature classes can hold information for multiple grids. An eighth feature
        class (GRD_) contains organizational information, such as map name and grid
        types that are used to organize your grids.The grid definition template is
        stored in a predefined XML file. This file
        stores specification properties for each grid, such as the number, color, and
        line weight of gridlines. When the definition template is applied, features are
        created according to the specification based on the current extent or extent of
        a selected feature (area of interest), scale, and coordinate systems.

     INPUTS:
      in_template (File):
          The XML grid definition template stores the specification's graphic properties
          for each grid layer. In addition to the graphic properties, which cannot be
          altered before execution, the definition has specific default values, exposed as
          parameters, that can be modified before execution.Template files are located in
          the \ArcGIS\Desktop10.1\GridTemplates directory.
          Additional grid templates can be obtained and shared using the ArcGIS Resource
          Center.The Esri Production Mapping extension provides a grid designer that
          allows you
          to create new templates as well as modify existing ones.
      in_aoi (Feature Layer / Extent):
          The feature layer or x,y extent used to determine the extent of the grid layer
          created.

          * Feature layer—Indicates you can choose the layer to use for the area of
          interest. Only one selected feature will be used from this layer. For layers
          that have more than one feature, the tool will only create a grid layer based on
          the first feature. The first feature is based on object id. All remaining
          features are ignored.

          * Extent—Indicates you can use one of the following as the area of interest:

          * The default area of interest of the data frame.

          *  As Specified Below—When you specify an extent by directly adding coordinates,
          a spatial reference for those coordinates is derived from the following, in
          order: (1) ArcMap's focused data frame (2) if ArcMap is not active, the
          Cartographic Coordinate System environment setting.

          * The same AOI as the display.

          The only extent options valid for this tool are Default, As Specified Below, or
          Same as Display. Selecting any other option will result in an error.
      input_feature_dataset (Feature Dataset):
          The feature dataset that will store the features. Grid-specific feature classes
          will be created if they do not already exist. If they already exist, and a grid
          with the same name and type as the one being created also exists, it will be
          overwritten.A grid with the same name and type as the one created will always be
          overwritten, regardless of the geoprocessing overwrite outputs setting.
      name {String / Field}:
          The name for the cartographic grid created that allows for distinction between
          grids that are stored in the same feature dataset and set of feature classes,
          expressed in one of the following formats:

          * String—Enter a text string for the grid name.

          * Field—Enter a field from the feature layer. The value of the field for the
          selected feature is used to name the grid. An area of interest field name can be
          used when the Input Area of Interest parameter is defined as Feature Layer.
          The grid name cannot contain any special characters. These include:

          * '

          * "

          * ~

          * \

          * /

          * |

          * #

          * @

          * $

          * %

          * ^

          * &

          * *

          * (

          * )
      refscale {Double}:
          The scale at which the grid is created and should be viewed. When the reference
          scale from the XML grid definition file is defined as Use Environment, the
          reference scale is derived in the following order:

          * The geoprocessing Reference Scale environment setting

          * The active data frame's reference scale

          * The active data frame's scale

          * The value from the XML grid definition file
      rotation {Double}:
          The rotation angle for the grid components. Rotation is used to provide
          annotation that is level with the page. Unless otherwise specified, rotation is
          calculated using the area of interest feature. When the rotation type from the
          XML grid definition file is defined as Use Environment, the rotation is derived
          in the following order:

          * The active data frame's rotation

          * The value from the XML grid definition file
      mask_size {Linear unit}:
          The mask is a polygon feature that forms an outer ring around the extent of the
          neatline and is used to mask data that falls in the area reserved for coordinate
          labels. Mask size defines the width of the polygon mask feature in map or page
          units. The data frame may have to be resized to fit around the edge of the mask
          while including the coordinate labels.
      xy_tolerance {Linear unit}:
          The minimum tolerated distance between geodatabase features, expressed in linear
          units. This value is defaulted from the value set in the XML.You can set the
          value higher for data with less coordinate accuracy and lower
          for data with extremely high accuracy. Features that fall within the set XY
          tolerance will be considered coincident.
      primary_coordinate_system {Spatial Reference}:
          The grid template XML file creates grid components depicting coordinates or
          locations for a primary coordinate system and up to four ancillary coordinate
          systems. The number of ancillary grids is specified by the file. You cannot add
          or delete ancillary coordinate systems. All coordinate systems specified must
          share a common geographic coordinate system. If you want to change the primary
          coordinate system to one that uses a different datum than the default, say for
          example, you change the coordinate system from one that uses WGS 1984 to one
          that uses NAD 1983, you must change each default ancillary coordinate system to
          NAD 1983 as well.This is the primary coordinate system for the grid layer being
          created.
          Typically, it will be the coordinate system of the final product or data frame.
          This coordinate system must be a projected coordinate system.When the Primary
          Coordinate System in the XML grid definition file is defined as
          Use Environment, the Primary Coordinate System is derived in the following
          order:

          * The geoprocessing Cartographic Coordinate System environment setting

          * The active data frame's coordinate system, if it is a projected coordinate
          system

          * The Fixed value from the XML grid definition file
          In all cases user input takes the highest precedence.
      configure_layout {Boolean}:
          Adjusts the data frame settings to ensure they match the grid layer. The data
          frame's coordinate system, scale, rotation, size, extent, and clipping may be
          altered to enforce consistency. This setting is only available when the tool is
          executed from ArcMap's layout view and is not being run in the background. The
          default is to have this check box unchecked.

          * CONFIGURELAYOUT—Indicates data frame and layout are configured using grid
          settings.

          * NO_CONFIGURELAYOUT—Indicates data frame and layout are not configured. This is
          the default.
      ancillary_coordinate_system_1 {Spatial Reference}:
          The grid template XML file creates grid components depicting coordinates or
          locations for a primary coordinate system and up to four ancillary coordinate
          systems. The number of ancillary grids is specified by the file. You cannot add
          or delete ancillary coordinate systems. All coordinate systems specified must
          share a common geographic coordinate system. If you want to change the primary
          coordinate system to one that uses a different datum than the default, say for
          example, you change the coordinate system from one that uses WGS 1984 to one
          that uses NAD 1983, you must change each default ancillary coordinate system to
          NAD 1983 as well.This is the first ancillary coordinate system.
      ancillary_coordinate_system_2 {Spatial Reference}:
          The grid template XML file creates grid components depicting coordinates or
          locations for a primary coordinate system and up to four ancillary coordinate
          systems. The number of ancillary grids is specified by the file. You cannot add
          or delete ancillary coordinate systems. All coordinate systems specified must
          share a common geographic coordinate system. If you want to change the primary
          coordinate system to one that uses a different datum than the default, say for
          example, you change the coordinate system from one that uses WGS 1984 to one
          that uses NAD 1983, you must change each default ancillary coordinate system to
          NAD 1983 as well.This is the second ancillary coordinate system.
      ancillary_coordinate_system_3 {Spatial Reference}:
          The grid template XML file creates grid components depicting coordinates or
          locations for a primary coordinate system and up to four ancillary coordinate
          systems. The number of ancillary grids is specified by the file. You cannot add
          or delete ancillary coordinate systems. All coordinate systems specified must
          share a common geographic coordinate system. If you want to change the primary
          coordinate system to one that uses a different datum than the default, say for
          example, you change the coordinate system from one that uses WGS 1984 to one
          that uses NAD 1983, you must change each default ancillary coordinate system to
          NAD 1983 as well.This is the third ancillary coordinate system.
      ancillary_coordinate_system_4 {Spatial Reference}:
          The grid template XML file creates grid components depicting coordinates or
          locations for a primary coordinate system and up to four ancillary coordinate
          systems. The number of ancillary grids is specified by the file. You cannot add
          or delete ancillary coordinate systems. All coordinate systems specified must
          share a common geographic coordinate system. If you want to change the primary
          coordinate system to one that uses a different datum than the default, say for
          example, you change the coordinate system from one that uses WGS 1984 to one
          that uses NAD 1983, you must change each default ancillary coordinate system to
          NAD 1983 as well.This is the fourth ancillary coordinate system.

     OUTPUTS:
      output_layer (Group Layer):
          The grouped layer of feature classes depicting grid, graticule, and border
          features. Each grid layer can be composed of a mask polygon, a clip polygon,
          segments(line), gridlines(line), ticks(line), endpoints(point), points(point),
          and annotation feature classes.This is a temporary layer that you must save in
          the ArcMap document or as a
          layer file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeGridsAndGraticulesLayer_cartography(*gp_fixargs((in_template, in_aoi, input_feature_dataset, output_layer, name, refscale, rotation, mask_size, xy_tolerance, primary_coordinate_system, configure_layout, ancillary_coordinate_system_1, ancillary_coordinate_system_2, ancillary_coordinate_system_3, ancillary_coordinate_system_4), True)))
        return retval
    except Exception, e:
        raise e


# Masking Tools toolset
@gptooldoc('CulDeSacMasks_cartography', None)
def CulDeSacMasks(input_layer=None, output_fc=None, reference_scale=None, spatial_reference=None, margin=None, attributes=None):
    """CulDeSacMasks_cartography(input_layer, output_fc, reference_scale, spatial_reference, margin, {attributes})

        Creates a feature class of polygon masks from a symbolized input line layer.

     INPUTS:
      input_layer (Layer):
          Input line layer from which to create masks.
      reference_scale (Double):
          The reference scale used for calculating the masking geometry when masks are
          specified in page units. This is typically the reference scale of the map.
      spatial_reference (Spatial Reference):
          The spatial reference for which the masking polygons will be created. This is
          not the spatial reference that will be assigned to the output feature class. It
          is the spatial reference of the map in which the masking polygons will be used
          since the position of symbology may change when features are projected.
      margin (Linear unit):
          The space in page units surrounding the symbolized input features used to create
          the mask polygon. Typically, masking polygons are created with a small margin
          around the symbol to improve visual appearance. Margin values are specified in
          either page units or map units. Most of the time you will want to specify your
          margin distance value in page units.Margin value units are interpreted
          differently depending on which units you
          choose. If you choose points, inches, millimeters, or centimeters, then masks
          are created using the margin distance as calculated in page space (you can think
          of the margin as a distance measured on the paper). The reference scale
          parameter value is accounted for in this calculation.If you choose any other
          units for your margin, then masks are created using the
          margin distance as calculated in map space (you can think of the margin as a
          real-world distance measure on the earth). Also, in this case, the reference
          scale parameter value is not used as part of the calculation.
      attributes {String}:
          Determines which attributes will be transferred from the input features to the
          output features.

          * ONLY_FID—Only the FID field from the input features will be transferred to the
          output features. This is the default.

          * NO_FID—All the attributes except the FID from the input features will be
          transferred to the output features.

          * ALL—All the attributes from the input features will be transferred to the
          output features.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CulDeSacMasks_cartography(*gp_fixargs((input_layer, output_fc, reference_scale, spatial_reference, margin, attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureOutlineMasks_cartography', None)
def FeatureOutlineMasks(input_layer=None, output_fc=None, reference_scale=None, spatial_reference=None, margin=None, method=None, mask_for_non_placed_anno=None, attributes=None):
    """FeatureOutlineMasks_cartography(input_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, {attributes})

        Creates mask polygons at a specified distance and shape around the symbolized
        features in the input layer.

     INPUTS:
      input_layer (Layer):
          The symbolized input layer from which the masks will be created.
      reference_scale (Double):
          The reference scale used for calculating the masking geometry when masks are
          specified in page units. This is typically the reference scale of the map.
      spatial_reference (Spatial Reference):
          The spatial reference for which the masking polygons will be created. This is
          not the spatial reference that will be assigned to the output feature class. It
          is the spatial reference of the map in which the masking polygons will be used
          since the position of symbology may change when features are projected.
      margin (Linear unit):
          The space in page units surrounding the symbolized input features used to create
          the mask polygon. Typically, masking polygons are created with a small margin
          around the symbol to improve visual appearance. Margin values are specified in
          either page units or map units. Most of the time you will want to specify your
          margin distance value in page units.Margin value units are interpreted
          differently depending on which units you
          choose. If you choose points, inches, millimeters, or centimeters, then masks
          are created using the margin distance as calculated in page space (you can think
          of the margin as a distance measured on the paper). The reference scale
          parameter value is accounted for in this calculation.If you choose any other
          units for your margin, then masks are created using the
          margin distance as calculated in map space (you can think of the margin as a
          real-world distance measure on the earth). Also, in this case, the reference
          scale parameter value is not used as part of the calculation.
      method (String):
          The type of masking geometry created. There are four types:

          * BOX—A polygon representing the extent of the symbolized feature.

          * CONVEX_HULL—The convex hull of the symbolized geometry of the feature. This is
          the default.

          * EXACT_SIMPLIFIED—A generalized polygon representing the exact shape of the
          symbolized feature. Polygons created with this method will have a significantly
          smaller number of vertices compared to polygons created with the EXACT method.

          * EXACT—A polygon representing the exact shape of the symbolized feature.
      mask_for_non_placed_anno (String):
          Specifies whether to create masks for unplaced annotation. This option is only
          used when masking geodatabase annotation layers.

          * ALL_FEATURES —Creates masks for all the annotation features.

          * ONLY_PLACED —Only creates masks for features with a status of placed.
      attributes {String}:
          Determines which attributes will be transferred from the input features to the
          output features.

          * ONLY_FID—Only the FID field from the input features will be transferred to the
          output features. This is the default.

          * NO_FID—All the attributes except the FID from the input features will be
          transferred to the output features.

          * ALL— All the attributes from the input features will be transferred to the
          output features.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureOutlineMasks_cartography(*gp_fixargs((input_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IntersectingLayersMasks_cartography', None)
def IntersectingLayersMasks(masking_layer=None, masked_layer=None, output_fc=None, reference_scale=None, spatial_reference=None, margin=None, method=None, mask_for_non_placed_anno=None, attributes=None):
    """IntersectingLayersMasks_cartography(masking_layer, masked_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, {attributes})

        Creates masking polygons at a specified shape and size at the intersection of
        two symbolized input layers -- the Masking layer and the Masked layer.

     INPUTS:
      masking_layer (Layer):
          The symbolized input layer, which will be intersected with the masked layer to
          create masking polygons. This is the layer that will be more prominently
          displayed when masking is applied to the masked layer.
      masked_layer (Layer):
          The symbolized input layer to be masked. This is the layer that will be obscured
          by the masking polygons.
      reference_scale (Double):
          The reference scale used for calculating the masking geometry when masks are
          specified in page units. This is typically the reference scale of the map.
      spatial_reference (Spatial Reference):
          The spatial reference for which the masking polygons will be created. This is
          not the spatial reference that will be assigned to the output feature class. It
          is the spatial reference of the map in which the masking polygons will be used
          since the position of symbology may change when features are projected.
      margin (Linear unit):
          The space in page units surrounding the symbolized input features used to create
          the mask polygon. Typically, masking polygons are created with a small margin
          around the symbol to improve visual appearance. Margin values are specified in
          either page units or map units. Most of the time you will want to specify your
          margin distance value in page units.Margin value units are interpreted
          differently depending on which units you
          choose. If you choose points, inches, millimeters, or centimeters, then masks
          are created using the margin distance as calculated in page space (you can think
          of the margin as a distance measured on the paper). The reference scale
          parameter value is accounted for in this calculation.If you choose any other
          units for your margin, then masks are created using the
          margin distance as calculated in map space (you can think of the margin as a
          real-world distance measure on the earth). Also, in this case, the reference
          scale parameter value is not used as part of the calculation.
      method (String):
          The type of masking geometry created. There are four types:

          * BOX—A polygon representing the extent of the symbolized feature.

          * CONVEX_HULL—The convex hull of the symbolized geometry of the feature. This is
          the default.

          * EXACT_SIMPLIFIED—A generalized polygon representing the exact shape of the
          symbolized feature. Polygons created with this method will have a significantly
          smaller number of vertices compared to polygons created with the EXACT method.

          * EXACT—A polygon representing the exact shape of the symbolized feature.
      mask_for_non_placed_anno (String):
          Specifies whether to create masks for unplaced annotation. This option is only
          used when masking geodatabase annotation layers.

          * ALL_FEATURES—Creates masks for all the annotation features.

          * ONLY_PLACED —Only creates masks for features with a status of placed.
      attributes {String}:
          Determines which attributes will be transferred from the input features to the
          output features.

          * ONLY_FID—Only the FID field from the input features will be transferred to the
          output features. This is the default.

          * NO_FID —All the attributes except the FID from the input features will be
          transferred to the output features.

          * ALL —All the attributes from the input features will be transferred to the
          output features.

     OUTPUTS:
      output_fc (Feature Class):
          The feature class that will contain the mask features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IntersectingLayersMasks_cartography(*gp_fixargs((masking_layer, masked_layer, output_fc, reference_scale, spatial_reference, margin, method, mask_for_non_placed_anno, attributes), True)))
        return retval
    except Exception, e:
        raise e


# Representation Management toolset
@gptooldoc('AddRepresentation_cartography', None)
def AddRepresentation(in_features=None, representation_name=None, rule_id_field_name=None, override_field_name=None, geometry_editing_option=None, import_rule_layer=None, assign_rule_id_option=None):
    """AddRepresentation_cartography(in_features, representation_name, {rule_id_field_name}, {override_field_name}, {geometry_editing_option}, {import_rule_layer}, {assign_rule_id_option})

        Adds a feature class representation to a geodatabase feature class.

     INPUTS:
      in_features (Feature Layer):
          The input geodatabase feature class to which a new feature class representation
          will be added.
      representation_name (String):
          The name of the feature class representation to be added.
      rule_id_field_name {String}:
          The name of the RuleID field, which will hold a reference to the representation
          rule for each feature.
      override_field_name {String}:
          The name of the Override field, which will hold overrides to representation
          rules for each feature.
      geometry_editing_option {String}:
          Specifies what will happen to the supporting feature class geometry when
          features are modified with the representation editing tools.

          * STORE_CHANGE_AS_OVERRIDE—Geometry modification made to features with the
          representation editing tools or using any of the geoprocessing tools in the
          Cartography toolbox will be stored as shape overrides in the Override field.
          Supporting feature class geometry (stored in the Shape field of the feature
          class) will be unaffected. This is the default.

          * MODIFY_FEATURE_SHAPE—Geometry modifications made to features with the
          representation editing tools, or using any of the geoprocessing tools in the
          Cartography toolbox, will modify the supporting feature class geometry (stored
          in the Shape field of the feature class.) No shape overrides will be stored.
      import_rule_layer {Layer}:
          A feature layer that symbolizes features with a feature class representation,
          from which the representation rules are imported.
      assign_rule_id_option {String}:
          Specifies whether or not to assign representation rules to features to match the
          RuleID assignments of the import rule layer. This option applies only when
          Import Rule Layer is specified.

          * ASSIGN—assign RuleIDs to features to match the import rule layer. This is the
          default.

          * NO_ASSIGN—Specifies not to match RuleIDs to features from the import rule
          layer. Features will be assigned to the default representation rule instead."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddRepresentation_cartography(*gp_fixargs((in_features, representation_name, rule_id_field_name, override_field_name, geometry_editing_option, import_rule_layer, assign_rule_id_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateRepresentationRule_cartography', None)
def CalculateRepresentationRule(in_features=None, representation=None, representation_rule=None):
    """CalculateRepresentationRule_cartography(in_features, representation, representation_rule)

        Applies existing representation rules to features in a feature class
        representation by calculating the RuleID field.

     INPUTS:
      in_features (Feature Layer):
          The feature class that contains the features for which representation rules will
          be calculated.
      representation (String):
          The feature class representation that contains the representation rules that
          will be applied to features. This feature class representation must belong to
          the input feature class.
      representation_rule (String):
          The representation rule to be applied to the input features by calculating the
          RuleID field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateRepresentationRule_cartography(*gp_fixargs((in_features, representation, representation_rule), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DropRepresentation_cartography', None)
def DropRepresentation(in_features=None, representation=None):
    """DropRepresentation_cartography(in_features, representation)

        Deletes a feature class representation from a geodatabase feature class.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer containing representation(s).
      representation (String):
          The feature class representation to be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DropRepresentation_cartography(*gp_fixargs((in_features, representation), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveOverride_cartography', None)
def RemoveOverride(in_features=None, representation=None, remove_option=None):
    """RemoveOverride_cartography(in_features, representation, {remove_option})

        Removes geometry and/or property representation overrides from features
        participating in a feature class representation.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer containing at least one representation.
      representation (String):
          The representation from which representation overrides will be removed.
      remove_option {String}:
          Specifies which types of overrides will be removed.

          * BOTH—Remove both geometry and property representation overrides. This is the
          default.

          * GEOMETRY_OVERRIDE—Remove representation geometry overrides only.

          * REPRESENTATION_PROPERTY_OVERRIDE—Remove representation property overrides
          only."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveOverride_cartography(*gp_fixargs((in_features, representation, remove_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SelectFeatureByOverride_cartography', None)
def SelectFeatureByOverride(in_features=None, select_option=None):
    """SelectFeatureByOverride_cartography(in_features, {select_option})

        Selects features that have representation geometry and/or property overrides.

     INPUTS:
      in_features (Layer):
          The input feature layer containing representations.
      select_option {String}:
          Specifies the type of representation override to use as a selection criterion.

          * BOTH—Select features that have either representation geometry or property
          overrides. This is the default.

          * GEOMETRY_OVERRIDE—Select all features that have representation geometry
          overrides.

          * REPRESENTATION_PROPERTY_OVERRIDE—Select all features that have representation
          property overrides."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SelectFeatureByOverride_cartography(*gp_fixargs((in_features, select_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetLayerRepresentation_cartography', None)
def SetLayerRepresentation(in_layer=None, representation=None):
    """SetLayerRepresentation_cartography(in_layer, representation)

        Sets a representation for a feature layer. The layer is temporary and stored in
        memory during the ArcGIS session, available for use in models and scripts.

     INPUTS:
      in_layer (Layer):
          The input feature layer containing at least one representation.
      representation (String):
          The representation to be set for the input feature layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetLayerRepresentation_cartography(*gp_fixargs((in_layer, representation), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateOverride_cartography', None)
def UpdateOverride(in_features=None, representation=None, update_option=None):
    """UpdateOverride_cartography(in_features, representation, {update_option})

        Transfers feature representation overrides from the default override field to
        explicit fields as defined by the representation rules in the
        representation.Updating geometry overrides will transfer the geometry override
        from the
        representation override field into the Shape field. The original geometry of the
        feature will be overwritten.

     INPUTS:
      in_features (Feature Layer):
          The input feature layer containing at least one representation.
      representation (String):
          The representation containing overrides to be transferred to explicit fields.
      update_option {String}:
          Specifies the type of representation override to be transferred to explicit
          fields.

          * REPRESENTATION_PROPERTY_OVERRIDE—Transfers representation property overrides
          only. This is the default.

          * GEOMETRY_OVERRIDE—Transfers representation geometry overrides only, into the
          Shape field. The original geometry of the feature will be overwritten.

          * BOTH—Transfers both representation property and geometry overrides.
          Representation geometry overrides will be transferred into the Shape field,
          overwriting the original geometry of the feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateOverride_cartography(*gp_fixargs((in_features, representation, update_option), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject