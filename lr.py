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
"""Organizations that collect data about linear features, such as highways, city
streets, railroads, rivers, pipelines, and water and sewer networks often use
linear referencing systems to store data. A linear reference system stores data
using a relative position along existing line features. That is, location is
given in terms of a known linear feature and a position, or measure, along it.
For example, route I-10, mile 23.2, uniquely identifies a position in geographic
space, and can be used instead of an x,y coordinate."""
__all__ = ['CalibrateRoutes', 'CreateRoutes', 'DissolveRouteEvents', 'LocateFeaturesAlongRoutes', 'MakeRouteEventLayer', 'OverlayRouteEvents', 'TransformRouteEvents']
__alias__ = u'lr'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('CalibrateRoutes_lr', None)
def CalibrateRoutes(in_route_features=None, route_id_field=None, in_point_features=None, point_id_field=None, measure_field=None, out_feature_class=None, calibrate_method=None, search_radius=None, interpolate_between=None, extrapolate_before=None, extrapolate_after=None, ignore_gaps=None, keep_all_routes=None, build_index=None):
    """CalibrateRoutes_lr(in_route_features, route_id_field, in_point_features, point_id_field, measure_field, out_feature_class, {calibrate_method}, {search_radius}, {interpolate_between}, {extrapolate_before}, {extrapolate_after}, {ignore_gaps}, {keep_all_routes}, {build_index})

        Recalculates route measures using points.

     INPUTS:
      in_route_features (Feature Layer):
          The route features to be calibrated.
      route_id_field (Field):
          The field containing values that uniquely identify each route. This field can be
          numeric or character.
      in_point_features (Feature Layer):
          The point features used to calibrate the routes.
      point_id_field (Field):
          The field that identifies the route on which each calibration point is located.
          The values in this field match those in the route identifier field. This field
          can be numeric or character.
      measure_field (Field):
          The field containing the measure value for each calibration point. This field
          must be numeric.
      calibrate_method {String}:
          Specifies how route measures will be recalculated.

          * DISTANCE—Measures will be recalculated using the shortest path distance
          between the calibration points. This is the default.

          * MEASURES—Measures will be recalculated using the pre-existing measure distance
          between the calibration points.
      search_radius {Linear unit}:
          Limits how far a calibration point can be from a route by specifying the
          distance and its unit of measure. If the units of measure are Unknown, the same
          units as the coordinate system of the route feature class will be used.
      interpolate_between {Boolean}:
          Specifies whether measure values will be interpolated between the calibration
          points.

          * BETWEEN—Interpolate between the calibration points. This is the default.

          * NO_BETWEEN—Do not interpolate between the calibration points.
      extrapolate_before {Boolean}:
          Specifies whether measure values will be extrapolated before the calibration
          points.

          * BEFORE—Extrapolate before the calibration points. This is the default.

          * NO_BEFORE—Do not extrapolate before the calibration points.
      extrapolate_after {Boolean}:
          Specifies whether measure values will be extrapolated after the calibration
          points.

          * AFTER—Extrapolate after the calibration points. This is the default.

          * NO_AFTER—Do not extrapolate after the calibration points.
      ignore_gaps {Boolean}:
          Specifies whether spatial gaps will be ignored when recalculating the measures
          on disjointed routes.

          * IGNORE—Spatial gaps will be ignored. Measure values will be continuous for
          disjointed routes. This is the default.

          * NO_IGNORE—Do not ignore spatial gaps. The measure values on disjointed routes
          will have gaps. The gap distance is calculated using the straight-line distance
          between the endpoints of the disjointed parts.
      keep_all_routes {Boolean}:
          Specifies whether route features that do not have any calibration points will be
          excluded from the output feature class.

          * KEEP—Keep all route features in the output feature class. This is the default.

          * NO_KEEP—Do not keep all route features in the output feature class. Features
          that have no calibration points will be excluded.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route identifier
          field that is written to the Output Route Feature Class.

          * INDEX—Create an attribute index. This is the default.

          * NO_INDEX—Do not create an attribute index.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created. It can be a shapefile or a geodatabase feature
          class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalibrateRoutes_lr(*gp_fixargs((in_route_features, route_id_field, in_point_features, point_id_field, measure_field, out_feature_class, calibrate_method, search_radius, interpolate_between, extrapolate_before, extrapolate_after, ignore_gaps, keep_all_routes, build_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRoutes_lr', None)
def CreateRoutes(in_line_features=None, route_id_field=None, out_feature_class=None, measure_source=None, from_measure_field=None, to_measure_field=None, coordinate_priority=None, measure_factor=None, measure_offset=None, ignore_gaps=None, build_index=None):
    """CreateRoutes_lr(in_line_features, route_id_field, out_feature_class, measure_source, {from_measure_field}, {to_measure_field}, {coordinate_priority}, {measure_factor}, {measure_offset}, {ignore_gaps}, {build_index})

        Creates routes from existing lines. The input line features that share a common
        identifier are merged to create a single route.

     INPUTS:
      in_line_features (Feature Layer):
          The features from which routes will be created.
      route_id_field (Field):
          The field containing values that uniquely identify each route.
      measure_source (String):
          Specifies how route measures will be obtained.

          * LENGTH—The geometric length of the input features will be used to accumulate
          the measures. This is the default.

          * ONE_FIELD—The value stored in a single field will be used to accumulate the
          measures.

          * TWO_FIELDS—The values stored in both from- and to- measure fields will be used
          to set the measures.
      from_measure_field {Field}:
          A field containing measure values. This field must be numeric and is required
          when the measure source is ONE_FIELD or TWO_FIELDS.
      to_measure_field {Field}:
          A field containing measure values. This field must be numeric and is required
          when the measure source is TWO_FIELDS.
      coordinate_priority {String}:
          The position from which measures will be accumulated for each output route. This
          parameter is ignored when the measure source is TWO_FIELDS.

          * UPPER_LEFT—Measures will be accumulated from the point closest to the minimum
          bounding rectangle's upper left corner. This is the default.

          * LOWER_LEFT—Measures will be accumulated from the point closest to the minimum
          bounding rectangle's lower left corner.

          * UPPER_RIGHT—Measures will be accumulated from the point closest to the minimum
          bounding rectangle's upper right corner.

          * LOWER_RIGHT—Measures will be accumulated from the point closest to the minimum
          bounding rectangle's lower right corner.
      measure_factor {Double}:
          A value multiplied by the measure length of each input line before they are
          merged to create route measures. The default is 1.
      measure_offset {Double}:
          A value added to the route measures after the input lines have been merged to
          create a route. The default is 0.
      ignore_gaps {Boolean}:
          Specifies whether spatial gaps will be ignored when calculating the measures on
          disjointed routes. This parameter is applicable when the measure source is
          LENGTH or ONE_FIELD.

          * IGNORE—Spatial gaps will be ignored. Measure values will be continuous for
          disjointed routes. This is the default.

          * NO_IGNORE—Do not ignore spatial gaps. The measure values on disjointed routes
          will have gaps. The gap distance is calculated using the straight-line distance
          between the endpoints of the disjointed parts.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route identifier
          field that is written to the output route feature class.

          * INDEX—Create an attribute index. This is the default.

          * NO_INDEX—Do not create an attribute index.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created. It can be a shapefile or a geodatabase feature
          class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRoutes_lr(*gp_fixargs((in_line_features, route_id_field, out_feature_class, measure_source, from_measure_field, to_measure_field, coordinate_priority, measure_factor, measure_offset, ignore_gaps, build_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DissolveRouteEvents_lr', None)
def DissolveRouteEvents(in_events=None, in_event_properties=None, dissolve_field=None, out_table=None, out_event_properties=None, dissolve_type=None, build_index=None):
    """DissolveRouteEvents_lr(in_events, in_event_properties, dissolve_field;dissolve_field..., out_table, out_event_properties, {dissolve_type}, {build_index})

        Removes redundant information from event tables or separates event tables having
        more than one descriptive attribute into individual tables.

     INPUTS:
      in_events (Table View):
          The table whose rows will be aggregated.
      in_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events in the
          input event table.

          * Route Identifier Field—The field containing values that indicate the route on
          which each event is located. This field can be numeric or character.

          * Event Type—The type of events in the input event table (POINT or LINE).

          * POINT—Point events occur at a precise location along a route. Only a from-
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field containing measure values. This field must be
          numeric and is required when the event type is POINT or LINE. Note when the
          Event Type is POINT, the label for this parameter becomes Measure Field.

          * To-Measure Field—A field containing measure values. This field must be numeric
          and is required when the event type is LINE.
      dissolve_field (Field):
          The field(s)used to aggregate rows.
      dissolve_type {Boolean}:
          Specifies whether the input events will be concatenated or dissolved.

          * DISSOLVE—Events will be aggregated wherever there is measure overlap. This is
          the default.

          * CONCATENATE—Events will be aggregated where the to-measure of one event
          matches the from-measure of the next event. This option is applicable only for
          line events.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route identifier
          field that is written to the output event table.

          * INDEX—Creates an attribute index. This is the default.

          * NO_INDEX—Does not create an attribute index.

     OUTPUTS:
      out_table (Table):
          The table to be created.
      out_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events that
          will be written to the output event table.

          * Route Identifier Field—The field that will contain values that indicate the
          route on which each event is located.

          * Event Type—The type of events the output event table will contain (POINT or
          LINE).

          * POINT—Point events occur at a precise location along a route. Only a single
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field that will contain measure values. Required when the
          event type is POINT or LINE. Note when the Event Type is POINT, the label for
          this parameter becomes Measure Field.

          * To-Measure Field—A field that will contain measure values. Required when the
          event type is LINE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DissolveRouteEvents_lr(*gp_fixargs((in_events, in_event_properties, dissolve_field, out_table, out_event_properties, dissolve_type, build_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LocateFeaturesAlongRoutes_lr', None)
def LocateFeaturesAlongRoutes(in_features=None, in_routes=None, route_id_field=None, radius_or_tolerance=None, out_table=None, out_event_properties=None, route_locations=None, distance_field=None, zero_length_events=None, in_fields=None, m_direction_offsetting=None):
    """LocateFeaturesAlongRoutes_lr(in_features, in_routes, route_id_field, radius_or_tolerance, out_table, out_event_properties, {route_locations}, {distance_field}, {zero_length_events}, {in_fields}, {m_direction_offsetting})

        Computes the intersection of input features (point, line, or polygon) and route
        features and writes the route and measure information to a new event table.

     INPUTS:
      in_features (Feature Layer):
          The input point, line, or polygon features.
      in_routes (Feature Layer):
          The routes with which the input features will be intersected.
      route_id_field (Field):
          The field containing values that uniquely identify each route. This field can be
          numeric or character.
      radius_or_tolerance (Linear unit):
          If the input features are points, the search radius is a numeric value defining
          how far around each point a search will be done to find a target route.If the
          input features are lines, the search tolerance is really a cluster
          tolerance, which is a numeric value representing the maximum tolerated distance
          between the input lines and the target routes.If the input features are
          polygons, this parameter is ignored and no search
          radius is used.
      route_locations {Boolean}:
          When locating points along routes, it is possible that more than one route may
          be within the search radius of any given point. This parameter is ignored when
          locating lines or polygons along routes.

          * FIRST—Only the closest route location will be written to the output event
          table. This is the default.

          * ALL—Every route location (within the search radius) will be written to the
          output event table.
      distance_field {Boolean}:
          Specifies whether a field named DISTANCE will be added to the output event
          table. The values in this field are in the units of the specified search radius.
          This parameter is ignored when locating lines or polygons along routes.

          * DISTANCE—A field containing the point-to-route distance will be added to the
          output event table. This is the default.

          * NO_DISTANCE—A field containing the point-to-route distance will not be added
          to the output event table.
      zero_length_events {Boolean}:
          When locating polygons along routes, it is possible that events can be created
          where the from-measure is equal to the to-measure. This parameter is ignored
          when locating points or lines along routes.

          * ZERO—Zero length line events will be written to the output event table. This
          is the default.

          * NO_ZERO—Zero length line events will not be written to the output event table.
      in_fields {Boolean}:
          Specifies whether the output event table will contain route location fields plus
          all the attributes from the input features.

          * FIELDS—The output event table will contain route location fields plus all the
          attributes from the input features. This is the default.

          * NO_FIELDS—The output event table will only contain route location fields plus
          the ObjectID field from the input features.
      m_direction_offsetting {Boolean}:
          Specifies whether the offset distance calculated should be based on the M
          direction or the digitized direction. Distances are included in the output event
          table if distance_field = "DISTANCE".

          * M_DIRECTION—The distance values in the output event table will be calculated
          based on the routes' M direction. Input features to the left of the M Direction
          of the route will be assigned a positive offset (+), and features to the right
          of the M Direction will be assigned a negative offset value (-). This is the
          default.

          * NO_M_DIRECTION—The distance values in the output event table will be
          calculated based on the routes' digitized direction. Input features to the left
          of the digitized direction of the route will be assigned a negative (-), offset
          and features to the right of the digitized direction will be assigned a positive
          offset value (+).

     OUTPUTS:
      out_table (Table):
          The table to be created.
      out_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events that
          will be written to the output event table.

          * Route Identifier Field—The field that will contain values that indicate the
          route on which each event is located.

          * Event Type—The type of events the output event table will contain (POINT or
          LINE).

          * POINT—Point events occur at a precise location along a route. Only a single
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field that will contain measure values. Required when the
          event type is POINT or LINE. Note when the Event Type is POINT, the label for
          this parameter becomes Measure Field.

          * To-Measure Field—A field that will contain measure values. Required when the
          event type is LINE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LocateFeaturesAlongRoutes_lr(*gp_fixargs((in_features, in_routes, route_id_field, radius_or_tolerance, out_table, out_event_properties, route_locations, distance_field, zero_length_events, in_fields, m_direction_offsetting), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeRouteEventLayer_lr', None)
def MakeRouteEventLayer(in_routes=None, route_id_field=None, in_table=None, in_event_properties=None, out_layer=None, offset_field=None, add_error_field=None, add_angle_field=None, angle_type=None, complement_angle=None, offset_direction=None, point_event_type=None):
    """MakeRouteEventLayer_lr(in_routes, route_id_field, in_table, in_event_properties, out_layer, {offset_field}, {add_error_field}, {add_angle_field}, {angle_type}, {complement_angle}, {offset_direction}, {point_event_type})

        Creates a temporary feature layer using routes and route events.When the
        temporary layer is used (displayed on a map, or used by another
        geoprocessing tool), dynamic segmentation is performed.

     INPUTS:
      in_routes (Feature Layer):
          The route features upon which events will be located.
      route_id_field (Field):
          The field containing values that uniquely identify each route.
      in_table (Table View):
          The table whose rows will be located along routes.
      in_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events in the
          input event table.

          * Route Identifier Field—The field containing values that indicate the route on
          which each event is located. This field can be numeric or character.

          * Event Type—The type of events in the input event table (POINT or LINE).

          * POINT—Point events occur at a precise location along a route. Only a from-
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field containing measure values. This field must be
          numeric and is required when the event type is POINT or LINE. Note when the
          Event Type is POINT, the label for this parameter becomes Measure Field.

          * To-Measure Field—A field containing measure values. This field must be numeric
          and is required when the event type is LINE.
      offset_field {Field}:
          The field containing values used to offset events from their underlying route.
          This field must be numeric.
      add_error_field {Boolean}:
          Specifies whether a field named LOC_ERROR will be added to the temporary layer
          that is created.

          * NO_ERROR_FIELD—Do not add a field to store locating errors. This is the
          default.

          * ERROR_FIELD—Add a field to store locating errors.
      add_angle_field {Boolean}:
          Specifies whether a field named LOC_ANGLE will be added to the temporary layer
          that is created. This parameter is only valid when the event type is POINT.

          * NO_ANGLE_FIELD—Do not add a field to store locating angles. This is the
          default.

          * ANGLE_FIELD—Add a field to store locating angles.
      angle_type {String}:
          Specifies the type of locating angle that will be calculated. This parameter is
          only valid if add_angle_field = "ANGLE_FIELD".

          * NORMAL—The normal (perpendicular) angle will be calculated. This is the
          default.

          * TANGENT—The tangent angle will be calculated.
          Specifies the type of locating angle that will be calculated. This parameter is
          only valid if Generate an angle field is checked.

          * NORMAL—The normal (perpendicular) angle will be calculated. This is the
          default.

          * TANGENT—The tangent angle will be calculated.
      complement_angle {Boolean}:
          Specifies whether the complement of the locating angle will be calculated. This
          parameter is only valid if add_angle_field = "ANGLE_FIELD".

          * ANGLE—Do not write the complement of the angle. Write only the calculated
          angle. This is the default.

          * COMPLEMENT—Write the complement of the angle.
      offset_direction {Boolean}:
          Specifies the side on which the route events with a positive offset are
          displayed. This parameter is only valid if an offset field has been specified.

          * LEFT—Events with a positive offset will be displayed to the left of the route.
          The side of the route is determined by the measures and not necessarily the
          digitized direction. This is the default.

          * RIGHT—Events with a positive offset will be displayed to the right of the
          route. The side of the route is determined by the digitized direction.
      point_event_type {Boolean}:
          Specifies whether point events will be treated as point features or multipoint
          features.

          * POINT—Point events will be treated as point features. This is the default.

          * MULTIPOINT—Point events will be treated as multipoint features.

     OUTPUTS:
      out_layer (Feature Layer):
          The layer to be created. This layer is stored in memory, so a path is not
          necessary."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeRouteEventLayer_lr(*gp_fixargs((in_routes, route_id_field, in_table, in_event_properties, out_layer, offset_field, add_error_field, add_angle_field, angle_type, complement_angle, offset_direction, point_event_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('OverlayRouteEvents_lr', None)
def OverlayRouteEvents(in_table=None, in_event_properties=None, overlay_table=None, overlay_event_properties=None, overlay_type=None, out_table=None, out_event_properties=None, zero_length_events=None, in_fields=None, build_index=None):
    """OverlayRouteEvents_lr(in_table, in_event_properties, overlay_table, overlay_event_properties, overlay_type, out_table, out_event_properties, {zero_length_events}, {in_fields}, {build_index})

        Overlays two event tables to create an output event table that represents the
        union or intersection of the input.

     INPUTS:
      in_table (Table View):
          The input event table.
      in_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events in the
          input event table.

          * Route Identifier Field—The field containing values that indicate the route on
          which each event is located. This field can be numeric or character.

          * Event Type—The type of events in the input event table (POINT or LINE).

          * POINT—Point events occur at a precise location along a route. Only a from-
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field containing measure values. This field must be
          numeric and is required when the event type is POINT or LINE. Note when the
          Event Type is POINT, the label for this parameter becomes Measure Field.

          * To-Measure Field—A field containing measure values. This field must be numeric
          and is required when the event type is LINE.
      overlay_table (Table View):
          The overlay event table.
      overlay_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events in the
          overlay event table.Route Identifier Field—The field containing values that
          indicate which route
          each event is along. This field can be numeric or character.Event Type—The type
          of events in the overlay event table (POINT or LINE).

          * POINT—Point events occur at a precise location along a route. Only a from-
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.
          From-Measure Field—A field containing measure values. This field must be numeric
          and is required when the event type is POINT or LINE. Note when the Event Type
          is POINT the label for this parameter becomes "Measure Field".To-Measure Field—A
          field containing measure values. This field must be numeric
          and is required when the event type is LINE.
      overlay_type (String):
          The type of overlay to be performed.

          * INTERSECT—Writes only overlapping events to the output event table. This is
          the default.

          * UNION—Writes all events to the output table. Linear events are split at their
          intersections.
      zero_length_events {Boolean}:
          Specifies whether to keep zero length line events in the output table. This
          parameter is only valid when the output event type is LINE.

          * ZERO—Keeps zero length line events. This is the default.

          * NO_ZERO—Does not keep zero length line events.
      in_fields {Boolean}:
          Specifies whether all the fields from the input and overlay event tables will be
          written to the output event table.

          * FIELDS—Includes all the fields from the input tables in the output table. This
          is the default.

          * NO_FIELDS—Does not include all the fields from the input tables in the output
          table. Only the ObjectID and the route location fields are kept.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route identifier
          field that is written to the output event table.

          * INDEX—Creates an attribute index. This is the default.

          * NO_INDEX—Does not create an attribute index.

     OUTPUTS:
      out_table (Table):
          The table to be created.
      out_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events that
          will be written to the output event table.

          * Route Identifier Field—The field that will contain values that indicate the
          route on which each event is located.

          * Event Type—The type of events the output event table will contain (POINT or
          LINE).

          * POINT—Point events occur at a precise location along a route. Only a single
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field that will contain measure values. Required when the
          event type is POINT or LINE. Note when the Event Type is POINT, the label for
          this parameter becomes Measure Field.

          * To-Measure Field—A field that will contain measure values. Required when the
          event type is LINE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.OverlayRouteEvents_lr(*gp_fixargs((in_table, in_event_properties, overlay_table, overlay_event_properties, overlay_type, out_table, out_event_properties, zero_length_events, in_fields, build_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TransformRouteEvents_lr', None)
def TransformRouteEvents(in_table=None, in_event_properties=None, in_routes=None, route_id_field=None, target_routes=None, target_route_id_field=None, out_table=None, out_event_properties=None, cluster_tolerance=None, in_fields=None):
    """TransformRouteEvents_lr(in_table, in_event_properties, in_routes, route_id_field, target_routes, target_route_id_field, out_table, out_event_properties, cluster_tolerance, {in_fields})

        This tool transforms the measures of events from one route reference to another
        and writes them to a new event table.

     INPUTS:
      in_table (Table View):
          The input event table.
      in_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events in the
          input event table.

          * Route Identifier Field—The field containing values that indicate the route on
          which each event is located. This field can be numeric or character.

          * Event Type—The type of events in the input event table (POINT or LINE).

          * POINT—Point events occur at a precise location along a route. Only a from-
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field containing measure values. This field must be
          numeric and is required when the event type is POINT or LINE. Note when the
          Event Type is POINT, the label for this parameter becomes Measure Field.

          * To-Measure Field—A field containing measure values. This field must be numeric
          and is required when the event type is LINE.
      in_routes (Feature Layer):
          The input route features.
      route_id_field (Field):
          The field containing values that uniquely identify each input route.
      target_routes (Feature Layer):
          The route features to which the input events will be transformed.
      target_route_id_field (Field):
          The field containing values that uniquely identify each target route.
      cluster_tolerance (Linear unit):
          The maximum tolerated distance between the input events and the target routes.
      in_fields {Boolean}:
          Specifies whether the output event table will contain route location fields plus
          all the attributes from the input events.

          * FIELDS—The output event table will contain route location fields plus all the
          attributes from the input events. This is the default.

          * NO_FIELDS—The output event table will only contain route location fields plus
          the ObjectID field from the input events.

     OUTPUTS:
      out_table (Table):
          The table to be created.
      out_event_properties (Route Measure Event Properties):
          Parameter consisting of the route location fields and the type of events that
          will be written to the output event table.

          * Route Identifier Field—The field that will contain values that indicate the
          route on which each event is located.

          * Event Type—The type of events the output event table will contain (POINT or
          LINE).

          * POINT—Point events occur at a precise location along a route. Only a single
          measure field must be specified.

          * LINE—Line events define a portion of a route. Both from- and to-measure fields
          must be specified.


          * From-Measure Field—A field that will contain measure values. Required when the
          event type is POINT or LINE. Note when the Event Type is POINT, the label for
          this parameter becomes Measure Field.

          * To-Measure Field—A field that will contain measure values. Required when the
          event type is LINE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TransformRouteEvents_lr(*gp_fixargs((in_table, in_event_properties, in_routes, route_id_field, target_routes, target_route_id_field, out_table, out_event_properties, cluster_tolerance, in_fields), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject