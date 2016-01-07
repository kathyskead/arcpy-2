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
"""The Network Analyst toolbox contains tools that perform network analysis and
network dataset maintenance. With the tools in this toolbox, you can maintain
network datasets that model transportation networks and perform route, closest
facility, service area, origin-destination cost matrix, vehicle routing problem,
and location-allocation network analyses on transportation networks. Use the
tools in this toolbox whenever you want to perform an analysis on a
transportation network."""
__all__ = ['MakeRouteLayer', 'AddLocations', 'Directions', 'MakeClosestFacilityLayer', 'MakeServiceAreaLayer', 'MakeODCostMatrixLayer', 'CalculateLocations', 'AddFieldToAnalysisLayer', 'IncreaseMaximumEdges', 'CreateTurnFeatureClass', 'PopulateAlternateIDFields', 'TurnTableToTurnFeatureClass', 'UpdateByAlternateIDFields', 'UpdateByGeometry', 'BuildNetwork', 'UpdateAnalysisLayerAttributeParameter', 'MakeVehicleRoutingProblemLayer', 'Solve', 'MakeLocationAllocationLayer', 'DissolveNetwork', 'SolveVehicleRoutingProblem', 'GenerateServiceAreas', 'UpdateTrafficData', 'UpdateTrafficIncidents', 'CopyTraversedSourceFeatures', 'FindClosestFacilities', 'SolveLocationAllocation', 'FindRoutes']

# Deprecated tools
__all__ += ['UpgradeNetwork']

__alias__ = u'na'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
import _na
from _na import *
__all__ += _na.__all__

# Analysis toolset
@gptooldoc('AddFieldToAnalysisLayer_na', None)
def AddFieldToAnalysisLayer(in_network_analysis_layer=None, sub_layer=None, field_name=None, field_type=None, field_precision=None, field_scale=None, field_length=None, field_alias=None, field_is_nullable=None):
    """AddFieldToAnalysisLayer_na(in_network_analysis_layer, sub_layer, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable})

        Adds a field to a sublayer of a network analysis layer.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          Network analysis layer to which the new field will be added.
      sub_layer (String):
          The sublayer of the network analysis layer to which the new field will be added.
      field_name (String):
          The name of the field that will be added to the specified sublayer of the
          network analysis layer.
      field_type (String):
          The field type used in the creation of the new field.

          * LONG— Whole numbers between -2,147,483,648 and 2,147,483,647.

          * TEXT—Any string of characters.

          * FLOAT— Fractional numbers between -3.4E38 and 1.2E38.

          * DOUBLE— Fractional numbers between -3.4E38 and 1.2E38.

          * SHORT— Whole numbers between -32,768 and 32,767.

          * DATE—Date and/or time.

          * BLOB—Long sequence of binary numbers. You need a custom loader or viewer or a
          third-party application to load items into a BLOB field or view the contents of
          a BLOB field.
      field_precision {Long}:
          The number of digits that can be stored in the field. All digits are counted no
          matter what side of the decimal they are on.The parameter value is valid only
          for numeric field types.
      field_scale {Long}:
          The number of decimal places stored in a field. This parameter is only used in
          float and double data field types.
      field_length {Long}:
          The length of the field being added. This sets the maximum number of allowable
          characters for each record of the field. This option is only applicable on
          fields of type text or blob.
      field_alias {String}:
          The alternate name given to the field name. This name is used to give more
          descriptive names to cryptic field names. The field alias parameter only applies
          to geodatabases and coverages.
      field_is_nullable {Boolean}:
          Specifies whether the field can contain null values. Null values are different
          from zero or empty fields and are only supported for fields in a geodatabase.

          * NON_NULLABLE—The field will not allow null values.

          * NULLABLE—The field will allow null values. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddFieldToAnalysisLayer_na(*gp_fixargs((in_network_analysis_layer, sub_layer, field_name, field_type, field_precision, field_scale, field_length, field_alias, field_is_nullable), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddLocations_na', None)
def AddLocations(in_network_analysis_layer=None, sub_layer=None, in_table=None, field_mappings=None, search_tolerance=None, sort_field=None, search_criteria=None, match_type=None, append=None, snap_to_position_along_network=None, snap_offset=None, exclude_restricted_elements=None, search_query=None):
    """AddLocations_na(in_network_analysis_layer, sub_layer, in_table, field_mappings, search_tolerance, {sort_field}, {search_criteria;search_criteria...}, {match_type}, {append}, {snap_to_position_along_network}, {snap_offset}, {exclude_restricted_elements}, {search_query;search_query...})

        Adds network analysis objects to a network analysis layer. The objects are added
        to specific sublayers such as Stops and Barriers. Objects are input as features
        or records.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          Network analysis layer to which the network analysis objects will be added.
      sub_layer (String):
          The sublayer of the network analysis layer to which the network analysis objects
          will be added.
      in_table (Table View):
          The feature class or the table that is the source for the new network analysis
          objects.
      field_mappings (Network Analyst Class FieldMap):
          Sets the values for the properties of the network analysis objects. Properties
          can be set to a constant or mapped to a field from the input feature class or
          table.An  NAClassFieldMappings object obtained from NAClassFieldMappings class
          is used
          to specify the parameter value. The NAClassFieldMappings object is a collection
          of NAClassFieldMap objects that allows you to specify the default values or map
          a field name from the input features for the properties of the network analysis
          object. If the data you are loading contains network locations or location
          ranges based on the network dataset used for the analysis, map the network
          location fields from your input features to the network location properties.
          Specifying the network location fields in the field mappings is similar to using
          the Use Network Location fields instead of geometry parameter from the tool
          dialog box.If you specify the field mapping for any of the network location
          properties, you
          need to specify the field mappings for the remaining network location properties
          to avoid a tool execution error.
      search_tolerance (Linear unit):
          The search tolerance for locating the input features on the network. Features
          that are outside the search tolerance are left unlocated. The parameter includes
          a value and units for the tolerance.The parameter is not used when adding
          locations to the Line Barriers or Polygon
          Barriers sublayers. In such cases, use "#" as the parameter value.
      sort_field {Field}:
          A field on which the network analysis objects are sorted as they are added to
          the network analysis layer. The default is the ObjectID field on the input
          feature class or the table.
      search_criteria {Value Table}:
          Specifies which sources in the network dataset will be searched when finding
          locations and what portions of geometry (also known as snap types) will be
          used.The parameter value is specified as a list with nested lists. The nested
          list is
          made up of two values indicating the name and the snap type for each network
          source. The snap type is specified using the SHAPE, MIDDLE, END, or NONE
          keywords.

          * SHAPE—The point will locate on the closest point of an element in this network
          source.

          * MIDDLE—The point will locate on the closest midpoint of an element in this
          network source.

          * END—The point will locate on the closest endpoint of an element in this
          network source.

          * NONE—The point will not locate on elements in this network source.
          For example, when finding locations, the parameter value
          [["Streets","SHAPE"],["Streets_ND_Junctions","NONE"]] specifies that the search
          can locate on the shape of the Streets source but not on the
          Streets_ND_Junctions source.To specify multiple snap types for a single network
          source, use the combination
          of the snap type keywords separated by an underscore. For example, MIDDLE_END
          specifies that the locations can be snapped to the middle or end of the network
          source.When adding line or polygon network locations, only the Shape snap type
          is used
          even if other snap types are specified.Any network source not included in this
          list will use its default snap type. It
          is safest to include all network sources in your list and explicitly set the
          snap type for each.
      match_type {Boolean}:
          * MATCH_TO_CLOSEST—Matches the new network locations to the closest network
          source among all the sources that have a snap type specified in the search
          criteria. This is the default.

          * PRIORITY—Matches the new network locations to the first network source having
          a snap type specified in the search criteria. The sources are searched in the
          priority order and the searching stops when the location is found within the
          search tolerance.
          The parameter is not used when adding locations to the Line Barriers or Polygon
          Barriers sublayers. In such cases, use "#" as the parameter value.
      append {Boolean}:
          Specifies whether or not to append new network analysis objects to existing
          objects.

          * APPEND—Adds the new network analysis objects to the existing set of objects in
          the selected sublayer.

          * CLEAR—Deletes the existing network analysis objects and replaces them with the
          new objects.
      snap_to_position_along_network {Boolean}:
          Specifies that you want to snap the network locations along the network dataset
          or at some specified offset from the network dataset.

          * NO_SNAP— The geometries of the network locations are based on the geometries
          of the input features. This is useful if you want to use the curb approach which
          requires that the network locations know which side of the edge they are on.

          * SNAP— if you have point features, the point will be snapped to the network and
          you will not be able to use curb approach. This is useful if you don't care how
          a vehicle approaches a stop. If your input features are lines or polygons, use
          this parameter value.
          The parameter is not used when adding locations to the Line Barriers or Polygon
          Barriers sublayers. In such cases, use "#" as the parameter value.
      snap_offset {Linear unit}:
          When snapping a point to the network, you can apply an offset distance. An
          offset distance of zero means the point will be coincident with the network
          feature (typically a line). To offset the point from the network feature, enter
          an offset distance. The offset is in relation to the original point location;
          that is, if the original point was on the left side, its new location will be
          offset to the left. If it was originally on the right side, its new location
          will be offset to the right.The parameter is not used when adding locations to
          the Line Barriers or Polygon
          Barriers sublayers. In such cases, use "#" as the parameter value.
      exclude_restricted_elements {Boolean}:
          * EXCLUDE—Specifies that the network locations are only placed on traversable
          portions of the network. This prevents placing network locations on elements
          that you can't reach due to restrictions or barriers. Before adding your network
          locations using this option, make sure that you have already added all the
          restriction barriers to the input network analysis layer to get expected
          results. This parameter is not applicable when adding barrier objects. In such
          cases, use "#" as the parameter value.

          * INCLUDE—Specifies that the network locations are placed on all the elements of
          the network. The network locations that are added with this option may be
          unreachable during the solve process if they are placed on restricted elements.
      search_query {Value Table}:
          Specifies a query to restrict the search to a subset of the features within a
          source feature class. This is useful if you don't want to find features that may
          be unsuited for a network location. For example, if you are loading centroids of
          polygons and don't want to locate on local roads, you can define a query that
          searches for major roads only.The parameter value is specified as a list with
          nested lists. The nested list is
          made up of two values indicating the name and the SQL expression for all of  the
          network sources. The syntax for the SQL expression differs slightly depending on
          the type of the network source feature class. For example, if you're querying
          source feature classes stored in file or enterprise geodatabases, shapefiles, or
          SDC, enclose field names in double quotes: "CFCC". If you're querying source
          feature classes stored in personal geodatabases, enclose fields in square
          brackets: [CFCC].If you don't want to specify a query for a particular source,
          use "#" as the
          value for the SQL expression or exclude the source name and the SQL expression
          from the parameter value. If you don't want to specify a query for all of the
          network sources, use "#" as the parameter value.For example, the parameter value
          [["Streets","\"CFCC\" = 'A15'"],
          ["Streets_ND_Junctions",""]] specifies an SQL expression for the Streets source
          feature class and no expression for Streets_ND_Junctions source feature class.
          Note that the double quotes used to enclose the field name CFCC are escaped
          using back slash characters to avoid a parsing error from the Python
          interpreter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddLocations_na(*gp_fixargs((in_network_analysis_layer, sub_layer, in_table, field_mappings, search_tolerance, sort_field, search_criteria, match_type, append, snap_to_position_along_network, snap_offset, exclude_restricted_elements, search_query), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateLocations_na', None)
def CalculateLocations(in_point_features=None, in_network_dataset=None, search_tolerance=None, search_criteria=None, match_type=None, source_ID_field=None, source_OID_field=None, position_field=None, side_field=None, snap_X_field=None, snap_Y_field=None, distance_field=None, snap_Z_field=None, location_field=None, exclude_restricted_elements=None, search_query=None):
    """CalculateLocations_na(in_point_features, in_network_dataset, search_tolerance, search_criteria;search_criteria..., {match_type}, {source_ID_field}, {source_OID_field}, {position_field}, {side_field}, {snap_X_field}, {snap_Y_field}, {distance_field}, {snap_Z_field}, {location_field}, {exclude_restricted_elements}, {search_query;search_query...})

        Adds fields to the input features that contain the network location of the
        features. The tool is used to store the network location information as feature
        attributes to quickly load the features as inputs for a network analysis layer.

     INPUTS:
      in_point_features (Table View):
          The input features for which the network locations will be calculated. For line
          and polygon features, since the network location information is stored
          in a blob field (specified in the Location ranges field parameter), only
          geodatabase feature classes are supported.
      in_network_dataset (Network Dataset Layer):
          The network dataset used to calculate the locations.If a sublayer of a network
          analysis layer is used as input features, the
          parameter must be set to the network dataset referenced by the network analysis
          layer.
      search_tolerance (Linear unit):
          The search tolerance for locating the input features on the network. Features
          that are outside the search tolerance are left unlocated. The parameter includes
          a value and units for the tolerance.The parameter is not used when calculating
          locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      search_criteria (Value Table):
          Specifies which sources in the network dataset will be searched when finding
          locations and what portions of geometry (also known as snap types) will be
          used.The parameter value is specified as a list with nested lists. The nested
          list is
          made up of two values indicating the name and the snap type for each network
          source. The snap type is specified using the SHAPE, MIDDLE, END, or NONE
          keywords.

          * SHAPE—The point will locate on the closest point of an element in this network
          source.

          * MIDDLE—The point will locate on the closest midpoint of an element in this
          network source.

          * END—The point will locate on the closest endpoint of an element in this
          network source.

          * NONE—The point will not locate on elements in this network source.
          For example, when finding locations, the parameter value
          [["Streets","SHAPE"],["Streets_ND_Junctions","NONE"]] specifies that the search
          can locate on the shape of the Streets source but not on the
          Streets_ND_Junctions source.To specify multiple snap types for a single network
          source, use the combination
          of the snap type keywords separated by an underscore. For example, MIDDLE_END
          specifies that the locations can be snapped to the middle or end of the network
          source.For geodatabase network datasets, the snap types can be specified for
          each
          subtype of the network source (["Streets : Local Streets","SHAPE"]).When
          calculating locations for line or polygon features, only the Shape snap
          type is used even if other snap types are specified.Any network source not
          included in this list will use its default snap type. It
          is safest to include all network sources in your list and explicitly set the
          snap type for each.
      match_type {Boolean}:
          * MATCH_TO_CLOSEST—Matches the new network locations to the closest network
          source among all the sources that have a snap type specified in the search
          criteria. This is the default.

          * PRIORITY—Matches the new network locations to the first network source having
          a snap type specified in the search criteria. The sources are searched in the
          priority order and the searching stops when the location is found within the
          search tolerance.
          The parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      source_ID_field {Field}:
          Name of the field to be created or updated with the source ID of the computed
          network location. A field named SourceID is created or updated by default.The
          parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      source_OID_field {Field}:
          Name of the field to be created or updated with the source OID of the computed
          network location. A field named SourceOID is created or updated by default.The
          parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      position_field {Field}:
          Name of the field to be created or updated with the percent along of the
          computed network location. A field named PosAlong is created or updated by
          default.The parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      side_field {Field}:
          Name of the field to be created or updated with the side of edge on which the
          point feature is located on the computed network location. A field named
          SideOfEdge is created or updated by default.The parameter is not used when
          calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      snap_X_field {Field}:
          Name of the field to be created or updated with the x-coordinate of the computed
          network location. A field named SnapX is created or updated by default.The
          parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      snap_Y_field {Field}:
          Name of the field to be created or updated with the y-coordinate of the computed
          network location. A field named SnapY is created or updated by default.The
          parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.
      distance_field {Field}:
          Name of the field to be created or updated with the distance of the point
          feature from the computed network location. A field named Distance is created or
          updated by default.The parameter is not used when calculating locations for line
          or polygon
          features. In such cases, use "#" as the parameter value.
      snap_Z_field {Field}:
          Name of the field to be created or updated with the z-coordinate of the
          computed network location. A field named SnapZ is created or updated by
          default.The parameter is not used when calculating locations for line or polygon
          features. In such cases, use "#" as the parameter value.When calculating
          locations for point features, the parameter is used only when
          the input network dataset supports connectivity based on z-coordinate values of
          the network sources. In all other cases, use "#" as the parameter value.
      location_field {Field}:
          Name of the field to be created or updated with the location ranges of the
          computed network locations for the line or polygon features. A field named
          Locations is created or updated by default.The parameter is used only when the
          calculating locations for line or polygon
          features. For input point features, use "#" as the parameter value.
      exclude_restricted_elements {Boolean}:
          This parameter is applicable only when the input features are from the sub layer
          of a network analysis layer and are not barrier objects. In all other cases, use
          "#" as the parameter value.

          * EXCLUDE—Specifies that the network locations are only placed on traversable
          portions of the network. This prevents placing network locations on elements
          that you can't reach due to restrictions or barriers. Before relocating your
          network locations using this option, make sure that you have already added all
          the restriction barriers to the network analysis layer to get expected results.

          * INCLUDE—Specifies that the network locations are placed on all the elements of
          the network. The network locations that are relocated with this option may be
          unreachable during the solve process if they are placed on restricted elements.
      search_query {Value Table}:
          Specifies a query to restrict the search to a subset of the features within a
          source feature class. This is useful if you don't want to find features that may
          be unsuited for a network location. For example, if you are loading centroids of
          polygons and don't want to locate on local roads, you can define a query that
          searches for major roads only.The parameter value is specified as a list with
          nested lists. The nested list is
          made up of two values indicating the name and the SQL expression for all of  the
          network sources. The syntax for the SQL expression differs slightly depending on
          the type of the network source feature class. For example, if you're querying
          source feature classes stored in file or enterprise geodatabases, shapefiles, or
          SDC, enclose field names in double quotes: "CFCC". If you're querying source
          feature classes stored in personal geodatabases, enclose fields in square
          brackets: [CFCC].If you don't want to specify a query for a particular source,
          use "#" as the
          value for the SQL expression or exclude the source name and the SQL expression
          from the parameter value. If you don't want to specify a query for all of the
          network sources, use "#" as the parameter value.For example, the parameter value
          [["Streets","\"CFCC\" = 'A15'"],
          ["Streets_ND_Junctions",""]] specifies an SQL expression for the Streets source
          feature class and no expression for Streets_ND_Junctions source feature class.
          Note that the double quotes used to enclose the field name CFCC are escaped
          using back slash characters to avoid a parsing error from the Python
          interpreter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateLocations_na(*gp_fixargs((in_point_features, in_network_dataset, search_tolerance, search_criteria, match_type, source_ID_field, source_OID_field, position_field, side_field, snap_X_field, snap_Y_field, distance_field, snap_Z_field, location_field, exclude_restricted_elements, search_query), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CopyTraversedSourceFeatures_na', None)
def CopyTraversedSourceFeatures(input_network_analysis_layer=None, output_location=None, edge_feature_class_name=None, junction_feature_class_name=None, turn_table_name=None):
    """CopyTraversedSourceFeatures_na(input_network_analysis_layer, output_location, edge_feature_class_name, junction_feature_class_name, turn_table_name)

        Creates two feature classes and a table, which together contain information
        about the edges, junctions, and turns that are traversed while solving a network
        analysis layer.

     INPUTS:
      input_network_analysis_layer (Network Analyst Layer):
          The network analysis layer from which traversed source features will be copied.
          If the network analysis layer does not have a valid result, the layer will be
          solved to produce one.
      output_location (Workspace / Feature Dataset):
          The workspace where the output table and two feature classes will be saved.
      edge_feature_class_name (String):
          The name of the feature class that will contain information about the traversed
          edge source features. If the solved network analysis layer doesn't traverse any
          edge features, an empty feature class is created.
      junction_feature_class_name (String):
          The name of the feature class that will contain information about the traversed
          junction source features, including system junctions and relevant points from
          the input network analysis layer. If the solved network analysis layer doesn't
          traverse any junctions, an empty feature class is created.
      turn_table_name (String):
          The name of the table that will contain information about the traversed global
          turns and turn features that scale cost for the underlying edges. If the solved
          network analysis layer doesn't traverse any turns, an empty table is created.
          Since restricted turns are never traversed, they are never included in the
          output."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyTraversedSourceFeatures_na(*gp_fixargs((input_network_analysis_layer, output_location, edge_feature_class_name, junction_feature_class_name, turn_table_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Directions_na', None)
def Directions(in_network_analysis_layer=None, file_type=None, out_directions_file=None, report_units=None, report_time=None, time_attribute=None, language=None, style_name=None, stylesheet=None):
    """Directions_na(in_network_analysis_layer, file_type, out_directions_file, report_units, {report_time}, {time_attribute}, {language}, {style_name}, {stylesheet})

        Generates turn-by-turn directions from a network analysis layer with routes. The
        directions can be written to a file in text, XML, or HTML format. If you provide
        an appropriate stylesheet, the directions can be written to any other file
        format.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          Network analysis layer for which directions will be generated. Directions can be
          generated only for route, closest facility, and vehicle routing problem network
          analysis layers.
      file_type (String):
          The format of the output directions file. This parameter is ignored if the
          stylesheet parameter has a value.

          * XML—The output directions file will be generated as an XML file. Apart from
          direction strings and the length and time information for the routes, the file
          will also contain information about the maneuver type and the turn angle for
          each direction.

          * TEXT—The output directions file will be generated as a simple TXT file
          containing the direction strings, the length and, optionally, the time
          information for the routes.

          * HTML—The output directions file will be generated as an HTML file containing
          the direction strings, the length and, optionally, the time information for the
          routes.
      report_units (String):
          Specifies the linear units in which the length information will be reported in
          the directions file. For example, even though your impedance was in meters, you
          can show directions in miles.

          * Feet

          * Yards

          * Miles

          * Meters

          * Kilometers

          * NauticalMiles
      report_time {Boolean}:
          * NO_REPORT_TIME—Do not report travel times in the directions file.

          * REPORT_TIME—Report travel times in the directions file. This is the default.
      time_attribute {String}:
          The time-based cost attribute to provide travel times in the directions. The
          cost attribute must exist on the network dataset used by the input network
          analysis layer.
      language {String}:
          Choose a language in which to generate driving directions. The languages that
          are shown in the drop-down list depend on which ArcGIS language packs are
          installed on your computer.Note that if you are going to publish this tool as
          part of a service on a
          separate server, the ArcGIS language pack that corresponds with the language you
          choose must be installed on that server for the tool to function properly. Also,
          if a language pack isn't installed on your computer, the language won't appear
          in the drop-down list; however, you can type a language code instead of choosing
          one.
      style_name {String}:
          Choose the name of the formatting style for the directions.

          * NA Desktop—Printable turn-by-turn directions

          * NA Navigation—Turn-by-turn directions designed for an in-vehicle navigation
          device

          * NA Campus—Turn-by-turn walking directions, which are designed for pedestrian
          routes
      stylesheet {File}:
          The stylesheet for generating a formatted output file type (such as a PDF,
          Word, or HTML file). The suffix of the file in the output directions file
          parameter should match the file type that the stylesheet generates. The
          Directions tool overrides the output file type parameter if this parameter
          contains a value.If you want a head start on creating your own text and HTML
          stylesheets, copy
          and edit the stylesheets Network Analyst uses. You can find them in the
          following directory: <ArcGIS installation
          directory>\ArcGIS\Desktop10.2.1\NetworkAnalyst\Directions\Styles. The stylesheet
          is Dir2PHTML.xsl, and the text stylesheet is Dir2PlainText.xsl.

     OUTPUTS:
      out_directions_file (File):
          If you provide a stylesheet in the stylesheet  parameter, make sure the file
          suffix for  out_directions_file matches the file type your stylesheet produces."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Directions_na(*gp_fixargs((in_network_analysis_layer, file_type, out_directions_file, report_units, report_time, time_attribute, language, style_name, stylesheet), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeClosestFacilityLayer_na', None)
def MakeClosestFacilityLayer(in_network_dataset=None, out_network_analysis_layer=None, impedance_attribute=None, travel_from_to=None, default_cutoff=None, default_number_facilities_to_find=None, accumulate_attribute_name=None, UTurn_policy=None, restriction_attribute_name=None, hierarchy=None, hierarchy_settings=None, output_path_shape=None, time_of_day=None, time_of_day_usage=None):
    """MakeClosestFacilityLayer_na(in_network_dataset, out_network_analysis_layer, impedance_attribute, {travel_from_to}, {default_cutoff}, {default_number_facilities_to_find}, {accumulate_attribute_name;accumulate_attribute_name...}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {hierarchy}, {hierarchy_settings}, {output_path_shape}, {time_of_day}, {time_of_day_usage})

        Makes a closest facility network analysis layer and sets its analysis
        properties. A closest facility analysis layer is useful in determining the
        closest facility or facilities to an incident based on a specified network
        cost.The Find Closest Facilities and Make Closest Facility Layer tools are
        similar,
        but they are designed for different purposes. Use Find Closest Facilities if you
        are setting up a geoprocessing service; it simplifies the setup process.
        Otherwise, use Make Closest Facility Layer.To create a closest facility
        geoprocessing service using Find Closest
        Facilities, you only need to set up one tool, and you can publish the tool
        directly as a service. In contrast, you need to create a model with the Make
        Closest Facility Layer tool, properly connect it to various other tools, and
        publish the model to create a closest-facility geoprocessing service. See
        Overview of the Network Analyst geoprocessing service examples to learn how to
        set up a closest facility service using tutorial data. One other option to
        consider is the ArcGIS Online Closest Facility service. It is a service that
        runs like a geoprocessing tool within ArcMap, can be accessed from other
        applications, and includes high quality road data for much of the world.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the closest facility analysis will be performed.
      out_network_analysis_layer (String):
          Name of the closest facility network analysis layer to create.
      impedance_attribute (String):
          The cost attribute to be used as impedance in the analysis.
      travel_from_to {String}:
          Specifies the direction of travel between facilities and incidents.

          * TRAVEL_FROM—Direction of travel is from facilities to incidents.

          * TRAVEL_TO—Direction of travel is from incidents to facilities.
          Using this option can find different facilities on a network with one-way
          restrictions and different impedances based on direction of travel. For
          instance, a facility may be a 10-minute drive from the incident while traveling
          from the incident to the facility, but while traveling from the facility to the
          incident, it may be a 15-minute journey because of different travel time in that
          direction.Fire departments commonly use the TRAVEL_FROM setting since they are
          concerned
          with the time it takes to travel from the fire station (facility) to the
          location of the emergency (incident). A retail store (facility) is more
          concerned with the time it takes the shoppers (incidents) to reach the store;
          therefore, stores commonly use the TRAVEL_TO option.
      default_cutoff {Double}:
          Default impedance value at which to stop searching for facilities for a given
          incident. The default can be overridden by specifying the cutoff value on
          incidents when the TRAVEL_TO option is used or by specifying the cutoff value on
          facilities when the TRAVEL_FROM option is used.
      default_number_facilities_to_find {Long}:
          Default number of closest facilities to find per incident. The default can be
          overridden by specifying a value for the TargetFacilityCount property on the
          incidents.
      accumulate_attribute_name {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Impedance attribute parameter to calculate the route.For each
          cost attribute that is accumulated, a Total_[Impedance] property is
          added to the routes that are output by the solver.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      hierarchy_settings {Network Analyst Hierarchy Settings}:
          Prior to version 10, this parameter allowed you to change the hierarchy ranges
          for your analysis from the default hierarchy ranges established in the network
          dataset. At version 10, this parameter is no longer supported and should be
          specified as an empty string. If you wish to change the hierarchy ranges for
          your analysis, update the default hierarchy ranges in the network dataset.
      output_path_shape {String}:
          Specifies the shape type for the route features that are output by the analysis.

          * TRUE_LINES_WITH_MEASURES—The output routes will have the exact shape of the
          underlying network sources. Furthermore, the output includes route measurements
          for linear referencing. The measurements increase from the first stop and record
          the cumulative impedance to reach a given position.

          * TRUE_LINES_WITHOUT_MEASURES—The output routes will have the exact shape of the
          underlying network sources.

          * STRAIGHT_LINES—The output route shape will be a single straight line between
          each paired incident and facility.

          * NO_LINES—No shape will be generated for the output routes.
          No matter which output shape type is chosen, the best route is always determined
          by the network impedance, never Euclidean distance. This means only the route
          shapes are different, not the underlying traversal of the network.
      time_of_day {Date}:
          Specifies the time and date at which the routes should begin or end.  The
          interpretation of this value depends on whether Time of Day Usage is set to
          START_TIME or END_TIME.If you have chosen a traffic-based impedance attribute,
          the solution will be
          generated given dynamic traffic conditions at the time of day specified here. A
          date and time can be specified as 5/14/2012 10:30 AM. Instead of using a
          particular date, a day of the week can be specified using
          the following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that travel should begin at 5:00 PM on Tuesday, specify
          the parameter value as 1/2/1900 5:00 PM.
      time_of_day_usage {String}:
          Indicates whether the value of the Time of Day parameter represents the arrival
          or departure time for the route or routes.

          * START_TIME —Time of Day is interpreted as the departure time from
          the facility or incident.When START_TIME is chosen, Time of Day indicates the
          solver should find the best route given a departure time. NOT_USED can be chosen
          if a value isn't specified in the Time of Day parameter.

          * END_TIME—Time of Day is interpreted as the arrival time at the facility or
          incident. This option is useful if you want to know what time to depart from a
          location so that you arrive at the destination at the time specified in Time of
          Day.

          * NOT_USED—When Time of Day doesn't have a value, NOT_USED is the only choice.
          When Time of Day has a value, NOT_USED isn't available."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeClosestFacilityLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, impedance_attribute, travel_from_to, default_cutoff, default_number_facilities_to_find, accumulate_attribute_name, UTurn_policy, restriction_attribute_name, hierarchy, hierarchy_settings, output_path_shape, time_of_day, time_of_day_usage), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeLocationAllocationLayer_na', None)
def MakeLocationAllocationLayer(in_network_dataset=None, out_network_analysis_layer=None, impedance_attribute=None, loc_alloc_from_to=None, loc_alloc_problem_type=None, number_facilities_to_find=None, impedance_cutoff=None, impedance_transformation=None, impedance_parameter=None, target_market_share=None, accumulate_attribute_name=None, UTurn_policy=None, restriction_attribute_name=None, hierarchy=None, output_path_shape=None, default_capacity=None, time_of_day=None):
    """MakeLocationAllocationLayer_na(in_network_dataset, out_network_analysis_layer, impedance_attribute, {loc_alloc_from_to}, {loc_alloc_problem_type}, {number_facilities_to_find}, {impedance_cutoff}, {impedance_transformation}, {impedance_parameter}, {target_market_share}, {accumulate_attribute_name;accumulate_attribute_name...}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {hierarchy}, {output_path_shape}, {default_capacity}, {time_of_day})

        Makes a location-allocation network analysis layer and sets its analysis
        properties. A location-allocation analysis layer is useful for choosing a given
        number of facilities from a set of potential locations such that a demand will
        be allocated to facilities in an optimal and efficient manner.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the location-allocation analysis will be performed.
      out_network_analysis_layer (String):
          Name of the location-allocation network analysis layer to create.
      impedance_attribute (String):
          The cost attribute to be used as impedance in the analysis.
      loc_alloc_from_to {String}:
          Specifies the direction of travel between facilities and demand points when
          calculating the network costs.

          * FACILITY_TO_DEMAND—Direction of travel is from facilities to demand points.
          Fire departments commonly use the this setting, since they are concerned with
          the time it takes to travel from the fire station to the location of the
          emergency.

          * DEMAND_TO_FACILITY—Direction of travel is from demand points to facilities.
          Retail stores commonly use this setting, since they are concerned with the time
          it takes the shoppers to reach the store.
          Using this option can affect the allocation of the demand points to the
          facilities on a network with one-way restrictions and different impedances based
          on direction of travel. For instance, a facility may be a 15-minute drive from
          the demand point to the facility, but only a 10-minute trip when traveling from
          the facility to the demand point.
      loc_alloc_problem_type {String}:
          The problem type that will be solved. The choice of the problem type depends on
          the kind of facility being located. Different kinds of facilities have different
          priorities and constraints.

          * MINIMIZE_IMPEDANCE—This option solves the warehouse location problem. It
          selects a set of facilities such that the total sum of weighted impedances
          (demand at a location times the impedance to the closest facility) is minimized.
          This problem type is often known as the P-Median problem.

          * MAXIMIZE_COVERAGE—This option solves the fire station location problem. It
          chooses facilities such that all or the greatest amount of demand is within a
          specified impedance cutoff.

          * MAXIMIZE_CAPACITATED_COVERAGE—This option solves the location problem where
          facilities have a finite capacity. It chooses facilities such that all or the
          greatest amount of demand can be served without exceeding the capacity of any
          facility. In addition to honoring capacity, it selects facilities such that the
          total sum of weighted impedance (demand allocated to a facility multiplied by
          the impedance to or from the facility) is minimized.

          * MINIMIZE_FACILITIES—This option solves the fire station location problem. It
          chooses the minimum number of facilities needed to cover all or the greatest
          amount of demand within a specified impedance cutoff.

          * MAXIMIZE_ATTENDANCE—This option solves the neighborhood store location problem
          where the proportion of demand allocated to the nearest chosen facility falls
          with increasing distance. The set of facilities that maximize the total
          allocated demand is chosen. Demand further than the specified impedance cutoff
          does not affect the chosen set of facilities.

          * MAXIMIZE_MARKET_SHARE—This option solves the competitive facility location
          problem. It chooses facilities to maximize market share in the presence of
          competitive facilities. Gravity model concepts are used to determine the
          proportion of demand allocated to each facility. The set of facilities that
          maximizes the total allocated demand is chosen.

          * TARGET_MARKET_SHARE—This option solves the competitive facility location
          problem. It chooses facilities to reach a specified target market share in the
          presence of competitive facilities. Gravity model concepts are used to determine
          the proportion of demand allocated to each facility. The minimum number of
          facilities needed to reach the specified target market share is chosen.
      number_facilities_to_find {Long}:
          Specifies the number of facilities that the solver should locate.The facilities
          with a FacilityType value of Required are always part of the
          solution when there are more facilities to find than required facilities; any
          excess facilities to choose are picked from candidate facilities.Any facilities
          that have a FacilityType value of Chosen before solving are
          treated as candidate facilities at solve time.The parameter value is not
          considered for the MINIMIZE_FACILITIES problem type
          since the solver determines the minimum number of facilities to locate to
          maximize coverage.The parameter value is overridden for the TARGET_MARKET_SHARE
          problem type
          because the solver searches for the minimum number of facilities required to
          capture the specified market share.
      impedance_cutoff {Double}:
          Impedance Cutoff specifies the maximum impedance at which a demand point can be
          allocated to a facility. The maximum impedance is measured by the least-cost
          path along the network. If a demand point is outside the cutoff, it is left
          unallocated. This property might be used to model the maximum distance that
          people are willing to travel to visit your stores or the maximum time that is
          permitted for a fire department to reach anyone in the community.Demand points
          have a Cutoff_[Impedance] property, which, if set, overrides the
          Impedance Cutoff property of the analysis layer. You might find that people in
          rural areas are willing to travel up to 10 miles to reach a facility while
          urbanites are only willing to travel up to two miles. You can model this
          behavior by setting the impedance cutoff value of the analysis layer to 10 and
          setting the Cutoff_Miles value of the demand points in urban areas to 2.
      impedance_transformation {String}:
          This sets the equation for transforming the network cost between facilities and
          demand points. This property, coupled with the Impedance Parameter, specifies
          how severely the network impedance between facilities and demand points
          influences the solver's choice of facilities.

          * LINEAR—The transformed network impedance between the facility and the demand
          point is the same as the shortest-path network impedance between them. With this
          option, the impedance parameter is always set to one. This is the default.

          * POWER—The transformed network impedance between the facility and the demand
          point is equal to the shortest-path network impedance raised to the power
          specified by the impedance parameter. Use this option with a positive impedance
          parameter to specify higher weight to nearby facilities.

          * EXPONENTIAL —The transformed network impedance between the facility and the
          demand point is equal to the mathematical constant e raised to the power
          specified by the shortest-path network impedance multiplied with the impedance
          parameter. Use this option with a positive impedance parameter to specify a very
          high weight to nearby facilities.Exponential transformations are commonly used
          in conjunction with an impedance cutoff.
          Demand points have an ImpedanceTransformation property, which, if set, overrides
          the Impedance Transformation property of the analysis layer. You might determine
          the impedance transformation should be different for urban and rural residents.
          You can model this by setting the impedance transformation for the analysis
          layer to match that of rural residents and setting the impedance transformation
          for the demand points in urban areas to match that of urbanites.
      impedance_parameter {Double}:
          Provides a parameter value to the equations specified in the Impedance
          transformation parameter. The parameter value is ignored when the impedance
          transformation is of type LINEAR. For POWER and EXPONENTIAL impedance
          transformations, the value should be nonzero.Demand points have an
          ImpedanceParameter property, which, if set, overrides the
          Impedance Parameter property of the analysis layer. You might determine that the
          impedance parameter should be different for urban and rural residents. You can
          model this by setting the impedance transformation for the analysis layer to
          match that of rural residents and setting the impedance transformation for the
          demand points in urban areas to match that of urbanites.
      target_market_share {Double}:
          Specifies the target market share in percentage to solve for when the Location-
          Allocation Problem Type parameter is set to TARGET_MARKET_SHARE . It is the
          percentage of the total demand weight that you want your solution facilities to
          capture. The solver chooses the minimum number of facilities required to capture
          the target market share specified by this numeric value.
      accumulate_attribute_name {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Impedance attribute parameter to calculate the route.For each
          cost attribute that is accumulated, a Total_[Impedance] property is
          added to the routes that are output by the solver.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      output_path_shape {String}:
          * NO_LINES—No shape will be generated for the output of the analysis.

          * STRAIGHT_LINES—The output line shapes will be straight lines connecting the
          solution facilities to their allocated demand points.
      default_capacity {Double}:
          Specifies the default capacity of facilities when the loc_alloc_problem_type
          parameter is set to MAXIMIZE_CAPACITATED_COVERAGE. This parameter is ignored for
          all other problem types.Facilities have a Capacity property, which, if set to a
          nonnull value, overrides
          the default_capacity parameter for that facility.
      time_of_day {Date}:
          Indicates the time and date of departure. The departure time can be from
          facilities or demand points, depending on whether travel is from demand to
          facility or facility to demand.If you have chosen a traffic-based impedance
          attribute, the solution will be
          generated given dynamic traffic conditions at the time of day specified here. A
          date and time can be specified as 5/14/2012 10:30 AM. Instead of using a
          particular date, a day of the week can be specified using
          the following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that travel should begin at 5:00 PM on Tuesday, specify
          the parameter value as 1/2/1900 5:00 PM."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeLocationAllocationLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, impedance_attribute, loc_alloc_from_to, loc_alloc_problem_type, number_facilities_to_find, impedance_cutoff, impedance_transformation, impedance_parameter, target_market_share, accumulate_attribute_name, UTurn_policy, restriction_attribute_name, hierarchy, output_path_shape, default_capacity, time_of_day), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeODCostMatrixLayer_na', None)
def MakeODCostMatrixLayer(in_network_dataset=None, out_network_analysis_layer=None, impedance_attribute=None, default_cutoff=None, default_number_destinations_to_find=None, accumulate_attribute_name=None, UTurn_policy=None, restriction_attribute_name=None, hierarchy=None, hierarchy_settings=None, output_path_shape=None, time_of_day=None):
    """MakeODCostMatrixLayer_na(in_network_dataset, out_network_analysis_layer, impedance_attribute, {default_cutoff}, {default_number_destinations_to_find}, {accumulate_attribute_name;accumulate_attribute_name...}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {hierarchy}, {hierarchy_settings}, {output_path_shape}, {time_of_day})

        Makes an origin–destination (OD) cost matrix network analysis layer and sets its
        analysis properties. An OD cost matrix analysis layer is useful for representing
        a matrix of costs going from a set of origin locations to a set of destination
        locations.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the OD cost matrix analysis will be performed.
      out_network_analysis_layer (String):
          Name of the OD cost matrix network analysis layer to create.
      impedance_attribute (String):
          The cost attribute to be used as impedance in the analysis.
      default_cutoff {Double}:
          Default impedance value at which to cut off searching for destinations for a
          given origin. If the accumulated impedance becomes higher than the cutoff value,
          the traversal stops. The default can be overridden by specifying the cutoff
          value on the origins.
      default_number_destinations_to_find {Long}:
          Default number of destinations to find for each origin. The default can be
          overridden by specifying a value for the TargetDestinationCount property on the
          origins.
      accumulate_attribute_name {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Impedance attribute parameter to calculate the route.For each
          cost attribute that is accumulated, a Total_[Impedance] property is
          added to the routes that are output by the solver.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      hierarchy_settings {Network Analyst Hierarchy Settings}:
          Prior to version 10, this parameter allowed you to change the hierarchy ranges
          for your analysis from the default hierarchy ranges established in the network
          dataset. At version 10, this parameter is no longer supported and should be
          specified as an empty string. If you wish to change the hierarchy ranges for
          your analysis, update the default hierarchy ranges in the network dataset.
      output_path_shape {String}:
          * NO_LINES—No shape will be generated for the output routes. This is useful when
          you have large number of origins and destinations and are interested only in the
          OD cost matrix table (and not the output line shapes).

          * STRAIGHT_LINES—The output route shape will be a single straight line between
          each of the origin-destination pairs.
          No matter which output shape type is chosen, the best route is always determined
          by the network impedance, never Euclidean distance. This means only the route
          shapes are different, not the underlying traversal of the network.
      time_of_day {Date}:
          Indicates the departure time from origins.If you have chosen a traffic-based
          impedance attribute, the solution will be
          generated given dynamic traffic conditions at the time of day specified here. A
          date and time can be specified as 5/14/2012 10:30 AM. Instead of using a
          particular date, a day of the week can be specified using
          the following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that travel should begin at 5:00 PM on Tuesday, specify
          the parameter value as 1/2/1900 5:00 PM."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeODCostMatrixLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, impedance_attribute, default_cutoff, default_number_destinations_to_find, accumulate_attribute_name, UTurn_policy, restriction_attribute_name, hierarchy, hierarchy_settings, output_path_shape, time_of_day), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeRouteLayer_na', None)
def MakeRouteLayer(in_network_dataset=None, out_network_analysis_layer=None, impedance_attribute=None, find_best_order=None, ordering_type=None, time_windows=None, accumulate_attribute_name=None, UTurn_policy=None, restriction_attribute_name=None, hierarchy=None, hierarchy_settings=None, output_path_shape=None, start_date_time=None):
    """MakeRouteLayer_na(in_network_dataset, out_network_analysis_layer, impedance_attribute, {find_best_order}, {ordering_type}, {time_windows}, {accumulate_attribute_name;accumulate_attribute_name...}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {hierarchy}, {hierarchy_settings}, {output_path_shape}, {start_date_time})

        Makes a route network analysis layer and sets its analysis properties. A route
        analysis layer is useful for determining the best route between a set of network
        locations based on a specified network cost.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the route analysis will be performed.
      out_network_analysis_layer (String):
          Name of the route network analysis layer to create.
      impedance_attribute (String):
          The cost attribute to be used as impedance in the analysis.
      find_best_order {Boolean}:
          * FIND_BEST_ORDER—The stops will be reordered to find the optimal route. This
          option changes the route analysis from a shortest-path problem to a traveling
          salesperson problem (TSP).

          * USE_INPUT_ORDER—The stops will be visited in the input order. This is the
          default.
      ordering_type {String}:
          Specifies the ordering of stops when FIND_BEST_ORDER is used.

          * PRESERVE_BOTH—Preserves the first and last stops by input order as the first
          and last stops in the route.

          * PRESERVE_FIRST—Preserves the first stop by input order as the first stop in
          the route, but the last stop is free to be reordered.

          * PRESERVE_LAST—Preserves the last stop by input order as the last stop in the
          route, but the first stop is free to be reordered.

          * PRESERVE_NONE—Frees both the first and last stop to be reordered.
      time_windows {Boolean}:
          Specifies whether time windows will be used at the stops.

          * USE_TIMEWINDOWS—The route will consider time windows on the stops. If a stop
          is arrived at before its time window, there will be wait time until the time
          window starts. If a stop is arrived at after its time window, there will be a
          time window violation. Total time window violation is balanced against minimum
          impedance when computing the route. This is a valid option only when the
          impedance is in time units.

          * NO_TIMEWINDOWS—The route will ignore time windows on the stops. This is the
          default.
      accumulate_attribute_name {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Impedance attribute parameter to calculate the route.For each
          cost attribute that is accumulated, a Total_[Impedance] property is
          added to the routes that are output by the solver.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      hierarchy_settings {Network Analyst Hierarchy Settings}:
          Prior to version 10, this parameter allowed you to change the hierarchy ranges
          for your analysis from the default hierarchy ranges established in the network
          dataset. At version 10, this parameter is no longer supported and should be
          specified as an empty string. If you wish to change the hierarchy ranges for
          your analysis, update the default hierarchy ranges in the network dataset.
      output_path_shape {String}:
          Specifies the shape type for the route features that are output by the analysis.

          * TRUE_LINES_WITH_MEASURES—The output routes will have the exact shape of the
          underlying network sources. Furthermore, the output includes route measurements
          for linear referencing. The measurements increase from the first stop and record
          the cumulative impedance to reach a given position.

          * TRUE_LINES_WITHOUT_MEASURES—The output routes will have the exact shape of the
          underlying network sources.

          * STRAIGHT_LINES—The output route shape will be a single straight line between
          the stops.

          * NO_LINES—No shape will be generated for the output routes.
          No matter which output shape type is chosen, the best route is always determined
          by the network impedance, never Euclidean distance. This means only the route
          shapes are different, not the underlying traversal of the network.
      start_date_time {Date}:
          Specifies a start date and time for the route. Route start time is mostly used
          to find routes based on the impedance attribute that varies with the time of the
          day. For example, a start time of 9 AM could be used to find a route that
          considers the rush hour traffic. The default value for this parameter is 8:00
          AM. A date and time can be specified as 10/21/05 10:30 AM. If the route spans
          multiple days, and only the start time is specified, then the current date is
          used. Instead of using a particular date, a day of the week can be specified
          using
          the following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that travel should begin at 5:00 PM on Tuesday, specify
          the parameter value as 1/2/1900 5:00 PM. After the solve, the start and end time
          of the route are populated in the
          output routes. These start and end times are also used when directions are
          generated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeRouteLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, impedance_attribute, find_best_order, ordering_type, time_windows, accumulate_attribute_name, UTurn_policy, restriction_attribute_name, hierarchy, hierarchy_settings, output_path_shape, start_date_time), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeServiceAreaLayer_na', None)
def MakeServiceAreaLayer(in_network_dataset=None, out_network_analysis_layer=None, impedance_attribute=None, travel_from_to=None, default_break_values=None, polygon_type=None, merge=None, nesting_type=None, line_type=None, overlap=None, split=None, excluded_source_name=None, accumulate_attribute_name=None, UTurn_policy=None, restriction_attribute_name=None, polygon_trim=None, poly_trim_value=None, lines_source_fields=None, hierarchy=None, time_of_day=None):
    """MakeServiceAreaLayer_na(in_network_dataset, out_network_analysis_layer, impedance_attribute, {travel_from_to}, {default_break_values}, {polygon_type}, {merge}, {nesting_type}, {line_type}, {overlap}, {split}, {excluded_source_name;excluded_source_name...}, {accumulate_attribute_name;accumulate_attribute_name...}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {polygon_trim}, {poly_trim_value}, {lines_source_fields}, {hierarchy}, {time_of_day})

        Makes a service area network analysis layer and sets its analysis properties. A
        service area analysis layer is useful in determining the area of accessibility
        within a given cutoff cost from a facility location.The Generate Service Areas
        and Make Service Area Layer tools are similar, but
        they are designed for different purposes. Use Generate Service Areas if you are
        setting up a geoprocessing service; it will simplify the setup process.
        Otherwise, use Make Service Area Layer. Also, use Make Service Area Layer if you
        need to generate service area lines; Generate Service Areas doesn't provide the
        option to generate lines.To create a service-area geoprocessing service using
        Generate Service Areas, you
        only need to set up one tool, and you can publish the tool directly as a
        service. In contrast, you need to create a model with the Make Service Area
        Layer, properly connect it to various other tools, and publish the model to
        create a service-area geoprocessing service. See Geoprocessing service example:
        Drive-time polygons to learn how to set up a drive-time polygons service using
        tutorial data. One other option to consider is the ArcGIS Online Generate
        Service Areas service. It is a service that runs like a geoprocessing tool
        within ArcMap, can be accessed from other applications, and includes high
        quality road data for much of the world.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the service area analysis will be performed.
      out_network_analysis_layer (String):
          Name of the service area network analysis layer to create.
      impedance_attribute (String):
          The cost attribute to be used as impedance in the analysis.
      travel_from_to {String}:
          Specifies the direction of travel to or from the facilities.

          * TRAVEL_FROM—The service area is created in the direction away from the
          facilities.

          * TRAVEL_TO—The service area is created in the direction towards the facilities.
           Using this option can result in different service areas on a network with one-
          way restrictions and having different impedances based on direction of travel.
          The service area for a pizza delivery store, for example, should be created away
          from the facility, whereas the service area of a hospital should be created
          toward the facility.
      default_break_values {String}:
          Default impedance values indicating the extent of the service area to be
          calculated. The default can be overridden by specifying the break value on the
          facilities.Multiple polygon breaks can be set to create concentric service
          areas. For
          instance, to find 2-, 3-, and 5-minute service areas for the same facility,
          specify "2 3 5" as the value for the Default break values parameter (the numbers
          2, 3, and 5 should be separated by a space).
      polygon_type {String}:
          Specifies the type of polygons to be generated.

          * SIMPLE_POLYS—Creates generalized polygons, which are generated quickly and are
          fairly accurate, except on the fringes. This is the default.

          * DETAILED_POLYS—Creates detailed polygons, which accurately model the service
          area lines and may contain islands of unreached areas. This option is slower
          than generating generalized polygons.

          * NO_POLYS—Turns off polygon generation for the case in which only service area
          lines are desired.
          If your data is of an urban area with a gridlike network, the difference between
          generalized and detailed polygons would be minimal. However, for mountain and
          rural roads, the detailed polygons may present significantly more accurate
          results than generalized polygons.
      merge {String}:
          Specifies the options to merge polygons that share similar break values. This
          option is applicable only when generating polygons for multiple facilities.

          * NO_MERGE—Creates individual polygons for each facility. The polygons can
          overlap each other.

          * NO_OVERLAP—Creates individual polygons that are closest for each facility. The
          polygons do not overlap each other.

          * MERGE— Joins the polygons of multiple facilities that have the same break
          value.
      nesting_type {String}:
          Specifies the option to create concentric service area polygons as disks or
          rings. This option is applicable only when multiple break values are specified
          for the facilities.

          * RINGS—Do not include the area of the smaller breaks. This creates polygons
          going between consecutive breaks. Use this option if you want to find the area
          from one break to another.

          * DISKS— Creates the polygons going from the facility to the break. For
          instance, If you create 5- and 10-minute service areas, then the 10-minute
          service area polygon will include the area under the 5-minute service area
          polygon. Use this option if you want to find the entire area from the facility
          to the break for each break.
      line_type {String}:
          Specifies the type of lines to be generated based on the service area analysis.
          Selecting the TRUE_LINES or TRUE_LINES_WITH_MEASURES option for large service
          areas will increase the amount of memory consumed by the analysis.

          * NO_LINES—Do not generate lines. This is the default.

          * TRUE_LINES—Lines are generated without measures.

          * TRUE_LINES_WITH_MEASURES—Lines are generated with measures. The measure values
          are generated based on the impedance value on each end of the edge with the
          intermediate vertices interpolated. Do not use this option if faster performance
          is desired.
      overlap {Boolean}:
          Determines if overlapping lines are generated when the service area lines are
          computed.

          * OVERLAP— Include a separate line feature for each facility when the facilities
          have service area lines that are coincident.

          * NON_OVERLAP— Include each service area line at most once and associate it with
          its closest (least impedance) facility.
      split {Boolean}:
          * SPLIT—Split every line between two breaks into two lines, each lying within
          its break. This is useful if you want to symbolize the service area lines by
          break. Otherwise, use the NO_SPLIT option for optimal performance.

          * NO_SPLIT—The lines are not split at the boundaries of the breaks. This is the
          default.
      excluded_source_name {String}:
          Specifies the list of network sources to be excluded when generating the
          polygons. The geometry of traversed elements from the excluded sources will be
          omitted from all polygons.This is useful if you have some network sources that
          you don't want to be
          included in the polygon generation because they create less accurate polygons or
          are inconsequential for the service area analysis. For example, while creating a
          drive time service area in a multimodal network of streets and rails, you should
          choose to exclude the rail lines from polygon generation so as to correctly
          model where a vehicle could travel.Excluding a network source from service area
          polygons does not prevent those
          sources from being traversed. Excluding sources from service area polygons only
          influences the polygon shape of the service areas. If you want to prevent
          traversal of a given network source, you must create an appropriate restriction
          when defining your network dataset.
      accumulate_attribute_name {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Impedance attribute parameter to calculate the route.For each
          cost attribute that is accumulated, a Total_[Impedance] property is
          added to the routes that are output by the solver.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      polygon_trim {Boolean}:
          * TRIM_POLYS—Trims the polygons containing the edges at the periphery of the
          service area to be within the specified distance of these outer edges. This is
          useful if the network is very sparse and you don't want the service area to
          cover large areas where there are no features.

          * NO_TRIM_POLYS—Do not trim polygons.
      poly_trim_value {Linear unit}:
          Specifies the distance within which the service area polygons are trimmed. The
          parameter includes a value and units for the distance. The default value is 100
          meters.
      lines_source_fields {Boolean}:
          * LINES_SOURCE_FIELDS— Add the SourceID, SourceOID, FromPosition, and ToPosition
          fields to the service area lines to hold information about the underlying source
          features traversed during the analysis. This can be useful to join the results
          of the service area lines to the original source data.

          * NO_LINES_SOURCE_FIELDS—Do not add the source fields (SourceID, SourceOID,
          FromPosition, and ToPosition) to the service area lines.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields a service area measured along all edges of the network dataset
          regardless of hierarchy level.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      time_of_day {Date}:
          The time to depart from or arrive at the facilities of the service area layer.
          The interpretation of this value as a depart or arrive time depends on whether
          travel is away from or toward the facilities.

          * It represents the departure time if Travel From or To Facility is set to
          TRAVEL_FROM.

          * It represents the arrival time if Travel From or To Facility is set to
          TRAVEL_TO.
          If you have chosen a traffic-based impedance attribute, the solution will be
          generated given dynamic traffic conditions at the time of day specified here. A
          date and time can be specified as 5/14/2012 10:30 AM. Instead of using a
          particular date, a day of the week can be specified using
          the following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that travel should begin at 5:00 PM on Tuesday, specify
          the parameter value as 1/2/1900 5:00 PM.Repeatedly solving the same analysis,
          but using different Time of Day values,
          allows you to see how a facility's reach changes over time. For instance, the
          five-minute service area around a fire station may start out large in the early
          morning, diminish during the morning rush hour, grow in the late morning, and so
          on throughout the day."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeServiceAreaLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, impedance_attribute, travel_from_to, default_break_values, polygon_type, merge, nesting_type, line_type, overlap, split, excluded_source_name, accumulate_attribute_name, UTurn_policy, restriction_attribute_name, polygon_trim, poly_trim_value, lines_source_fields, hierarchy, time_of_day), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeVehicleRoutingProblemLayer_na', None)
def MakeVehicleRoutingProblemLayer(in_network_dataset=None, out_network_analysis_layer=None, time_impedance=None, distance_impedance=None, time_units=None, distance_units=None, default_date=None, capacity_count=None, time_window_factor=None, excess_transit_factor=None, UTurn_policy=None, restriction_attribute_name=None, hierarchy=None, hierarchy_settings=None, output_path_shape=None):
    """MakeVehicleRoutingProblemLayer_na(in_network_dataset, out_network_analysis_layer, time_impedance, {distance_impedance}, {time_units}, {distance_units}, {default_date}, {capacity_count}, {time_window_factor}, {excess_transit_factor}, {UTurn_policy}, {restriction_attribute_name;restriction_attribute_name...}, {hierarchy}, {hierarchy_settings}, {output_path_shape})

        Makes a vehicle routing problem (VRP) network analysis layer and sets its
        analysis properties. A vehicle routing problem analysis layer is useful for
        optimizing a set of routes using a fleet of vehicles.The Make Vehicle Routing
        Problem Layer and Solve Vehicle Routing Problem tools
        are similar, but they are designed for different purposes. Use the Solve Vehicle
        Routing Problem tool if you are setting up a geoprocessing service; it will
        simplify the setup process. Otherwise, use the Make Vehicle Routing Problem
        Layer tool.To create a VRP geoprocessing service using Solve Vehicle Routing
        Problem Layer,
        you only need to set up one tool and publish it as a service. In contrast, you
        need to create a model with the Make Vehicle Routing Problem Layer, properly
        connect it to various other tools, and publish the model to create a service.
        One other option to consider is the ArcGIS Online Vehicle Routing Problem
        services. The services run like geoprocessing tools within ArcMap, can be
        accessed from other applications, and include high quality road data for much of
        the world.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset on which the vehicle routing problem analysis will be
          performed. The network dataset must have a time based cost attribute since the
          VRP solver minimizes time.
      out_network_analysis_layer (String):
          Name of the vehicle routing problem network analysis layer to create.
      time_impedance (String):
          The time cost attribute used to define the traversal time along the elements of
          the network. The time cost attribute is required, since the vehicle routing
          problem solver minimizes time.
      distance_impedance {String}:
          The distance cost attribute used to define the length along the elements of the
          network. The distance cost attribute is optional.
      time_units {String}:
          The time units used by the temporal fields of the analysis layer's sublayers and
          tables (network analysis classes). This does not have to be the same as the
          units of the time cost attribute.

          * Seconds

          * Minutes

          * Hours

          * Days
      distance_units {String}:
          The distance units used by distance fields of the analysis layer's sublayers
          and tables (network analysis classes). This does not have to be the same as the
          units of the optional distance cost attribute.

          * Miles

          * Kilometers

          * Feet

          * Yards

          * Meters

          * Inches

          * Centimeters

          * Millimeters

          * Decimeters

          * NauticalMiles
      default_date {Date}:
          The implied date for time field values that don't have a date specified with the
          time. If a time field for an order object, such as TimeWindowStart1, has a time-
          only value, the date is assumed to be the default date. For example, if an order
          has a TimeWindowStart1 value of 9:00 AM and the default date is March 6, 2013,
          then the entire time value for the field is 9:00 A.M., March 6, 2013. The
          default date has no effect on time field values that already have a date.The day
          of the week can also be specified as the default date using the
          following dates.

          * Today—12/30/1899

          * Sunday—12/31/1899

          * Monday—1/1/1900

          * Tuesday—1/2/1900

          * Wednesday—1/3/1900

          * Thursday—1/4/1900

          * Friday—1/5/1900

          * Saturday—1/6/1900
          For example, to specify that the implied date for time field values should be
          Tuesday, specify the parameter value as 1/2/1900.If your network dataset
          includes traffic data, the results of the analysis could
          change depending on the date that you specify here. For example, if your routes
          start at 8:00 a.m. on Sunday, when there is not much traffic, versus 8:00 a.m.
          on Monday during rush hour, the Monday route would take longer. Furthermore, the
          best path could change depending on traffic conditions.
      capacity_count {Long}:
          The number of capacity constraint dimensions required to describe the relevant
          limits of the vehicles. In an order delivery case, each vehicle may have a
          limited amount of weight and volume it can carry at one time based on physical
          and legal limitations. In this case, if you track the weight and volume on the
          orders, you can use these two capacities to prevent the vehicles from getting
          overloaded. The capacity count for this scenario is two (weight and volume).
          Depending on the problem, you may need to track different types or amounts of
          capacities. The capacities entered into the capacity fields (DeliveryQuantities
          and PickupQuantities for the Orders class and Capacities for the Routes class)
          are space-delimited strings of numbers, which can hold up to the number of
          values specified in Capacity Count. Each capacity dimension should appear in the
          same positional order for all capacity field values in the same VRP analysis
          layer. The capacities themselves are unnamed, so to avoid accidentally
          transposing capacity dimensions, ensure that the space-delimited capacity lists
          are always entered in the same order for all capacity field values.
      time_window_factor {String}:
          This parameter allows you to rate the importance of honoring time windows
          without causing violations. A time window violation occurs when a route arrives
          at an order, depot, or break after a time window has closed. The violation is
          the interval between the end of the time window and the arrival time of a
          route.The VRP solution can change according to the value you choose for the Time
          Window Violation Importance parameter. The following list describes what the
          values mean and how the resulting VRP solution can vary:

          * High—The solver tries to find a solution that minimizes time window violations
          at the expense of increasing the overall travel time. Choose this setting if
          arriving on time at orders is more important to you than minimizing your overall
          solution cost. This may be the case if you are meeting customers at your orders
          and you don't want to inconvenience them with tardy arrivals (another option is
          to use hard time windows that can't be violated at all).Given other constraints
          of a vehicle routing problem, it may be impossible to visit all the orders
          within their time windows. In this case, even a High setting might produce
          violations.

          * Medium—This is the default setting. The solver looks for a balance between
          meeting time windows and reducing the overall solution cost.

          * Low—The solver tries to find a solution that minimizes overall travel time,
          regardless of time windows. Choose this setting if respecting time windows is
          less important than reducing your overall solution cost. You may want to use
          this setting if you have a growing backlog of service requests. For the purpose
          of servicing more orders in a day and reducing the backlog, you can choose this
          setting even though customers will be inconvenienced with your fleet's late
          arrivals.
      excess_transit_factor {String}:
          This parameter allows you to rate the importance of reducing excess transit
          time. Excess transit time is the amount of time exceeding the time required to
          travel directly between the paired orders. The excess time results from breaks
          or travel to other orders or depots between visits to the paired orders.The VRP
          solution can change according to the value you choose for the Excess
          Transit Time Importance. The following list describes what the values mean and
          how the resulting VRP solution can vary:

          * High—The solver tries to find a solution with less excess transit time between
          paired orders at the expense of increasing the overall travel costs. It makes
          sense to use this setting if you are transporting people between paired orders
          and you want to shorten their ride time. This is characteristic of taxi
          services.

          * Medium—This is the default setting. The solver looks for a balance between
          reducing excess transit time and reducing the overall solution cost.

          * Low—The solver tries to find a solution that minimizes overall solution cost,
          regardless of excess transit time. This setting is commonly used with courier
          services. Since couriers transport packages as opposed to people, they don't
          need to worry about ride time. Using this setting allows the couriers to service
          paired orders in the proper sequence and minimize the overall solution cost.
      UTurn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      restriction_attribute_name {String}:
          List of restriction attributes to apply during the analysis.
      hierarchy {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.
      hierarchy_settings {Network Analyst Hierarchy Settings}:
          Prior to version 10, this parameter allowed you to change the hierarchy ranges
          for your analysis from the default hierarchy ranges established in the network
          dataset. At version 10, this parameter is no longer supported and should be
          specified as an empty string. If you wish to change the hierarchy ranges for
          your analysis, update the default hierarchy ranges in the network dataset.
      output_path_shape {String}:
          * TRUE_LINES_WITH_MEASURES—The output routes will have the exact shape of the
          underlying network sources. Furthermore, the output includes route measurements
          for linear referencing. The measurements increase from the first stop and record
          the cumulative impedance to reach a given position.

          * TRUE_LINES_WITHOUT_MEASURES—The output routes will have the exact shape of the
          underlying network sources.

          * STRAIGHT_LINES—The output route shape will be straight lines connecting orders
          and depot visits as per the route sequence.

          * NO_LINES—No shape will be generated for the output routes. You will also not
          be able to generate driving directions."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeVehicleRoutingProblemLayer_na(*gp_fixargs((in_network_dataset, out_network_analysis_layer, time_impedance, distance_impedance, time_units, distance_units, default_date, capacity_count, time_window_factor, excess_transit_factor, UTurn_policy, restriction_attribute_name, hierarchy, hierarchy_settings, output_path_shape), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Solve_na', None)
def Solve(in_network_analysis_layer=None, ignore_invalids=None, terminate_on_solve_error=None, simplification_tolerance=None):
    """Solve_na(in_network_analysis_layer, {ignore_invalids}, {terminate_on_solve_error}, {simplification_tolerance})

        Solves the network analysis layer problem based on its network locations and
        properties.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer on which the analysis will be computed.
      ignore_invalids {Boolean}:
          * SKIP—The solver will skip over network locations that are unlocated and solve
          the analysis layer from valid network locations only. It will also continue
          solving if locations are on nontraversable elements or have other errors. This
          is useful if you know your network locations are not all correct, but you want
          to solve with the network locations that are valid.

          * HALT—Do not solve if there are invalid locations. You can then correct these
          and re-run the analysis.
      terminate_on_solve_error {Boolean}:
          * TERMINATE—The tool will fail to execute when the solver encounters an error.
          This is the default. When you use this option, the result object is not created
          when the tool fails to execute due to a solver error. You should obtain the
          geoprocessing messages from the ArcPy object.

          * CONTINUE—The tool will not fail and continue execution even when the solver
          encounters an error. All of the error messages returned by the solver will be
          converted to warning messages. When you use this option, the result object is
          always created and the maxSeverity property of the result object is set to 1
          even when the solver encounters an error. Use the getOutput method of the result
          object with an index value of 1 to determine if the solve was successful.
      simplification_tolerance {Linear unit}:
          The tolerance that determines the degree of simplification for the output
          geometry. If a tolerance is specified, it must be greater than zero. You can
          choose a preferred unit; the default unit is decimal degrees.Specifying a
          simplification tolerance tends to reduce the time it takes to
          render routes or service areas. The drawback, however, is that simplifying
          geometry removes vertices, which may lessen the spatial accuracy of the output
          at larger scales.Because a line with only two vertices cannot be simplified any
          further, this
          parameter has no effect on drawing times for single-segment output, such as
          straight-line routes,  OD cost matrix lines, and location-allocation lines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Solve_na(*gp_fixargs((in_network_analysis_layer, ignore_invalids, terminate_on_solve_error, simplification_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateAnalysisLayerAttributeParameter_na', None)
def UpdateAnalysisLayerAttributeParameter(in_network_analysis_layer=None, parameterized_attribute=None, attribute_parameter_name=None, attribute_parameter_value=None):
    """UpdateAnalysisLayerAttributeParameter_na(in_network_analysis_layer, parameterized_attribute, attribute_parameter_name, {attribute_parameter_value})

        Updates the network attribute parameter value for a network analysis layer. The
        tool should be used to update the value of an attribute parameter for a network
        analysis layer prior to solving with the Solve tool. This ensures that the solve
        operation uses the specified value of the attribute parameter to produce
        appropriate results.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          Network analysis layer for which the attribute parameter value will be updated.
      parameterized_attribute (String):
          The network attribute whose attribute parameter will be updated.
      attribute_parameter_name (String):
          The parameter of the network attribute that will be updated. The parameters of
          type Object cannot be updated using the tool.
      attribute_parameter_value {String}:
          The value that will be set for the attribute parameter. It can be a string,
          number, date, or Boolean (True, False). If the value is not specified, then the
          attribute parameter value is set to Null.If the attribute parameter has a
          restriction usage type, the value can be
          specified as a string keyword or a numeric value. The string keyword or the
          numeric value determines whether the restriction attribute prohibits, avoids, or
          prefers the network elements it is associated with. Furthermore, the degree to
          which network elements are avoided or preferred can be defined by choosing HIGH,
          MEDIUM, or LOW keywords. The following keywords are supported:

          * PROHIBITED

          * AVOID_HIGH

          * AVOID_MEDIUM

          * AVOID_LOW

          * PREFER_LOW

          * PREFER_MEDIUM

          * PREFER_HIGH
          Numeric values that are greater than one cause restricted elements to be
          avoided; the larger the number, the more the elements are avoided. Numeric
          values between zero and one cause restricted elements to be preferred; the
          smaller the number, the more restricted elements are preferred. Negative numbers
          prohibit restricted elements. If the parameter value holds an array, separate
          the items in the array with the
          localized separator character. For example, in the U.S., you would most likely
          use the comma character to separate the items. So representing an array of three
          numbers might look like the following: "5,10,15"."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateAnalysisLayerAttributeParameter_na(*gp_fixargs((in_network_analysis_layer, parameterized_attribute, attribute_parameter_name, attribute_parameter_value), True)))
        return retval
    except Exception, e:
        raise e


# Network Dataset toolset
@gptooldoc('BuildNetwork_na', None)
def BuildNetwork(in_network_dataset=None):
    """BuildNetwork_na(in_network_dataset)

        Reconstructs the network connectivity and attribute information of a network
        dataset. The network dataset needs to be rebuilt after making edits to the
        attributes or the features of a participating source feature class. After the
        source features are edited, the tool establishes the network connectivity only
        in the areas that have been edited to speed up the build process; however, when
        the network attributes are edited, the entire extent of the network dataset is
        rebuilt. This may be a slow operation on a large network dataset.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset to be built."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildNetwork_na(*gp_fixargs((in_network_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DissolveNetwork_na', None)
def DissolveNetwork(in_network_dataset=None, out_workspace_location=None):
    """DissolveNetwork_na(in_network_dataset, out_workspace_location)

        Creates a network dataset that minimizes the number of line features required
        to correctly model the input network dataset. The more efficient output network
        dataset reduces the time required to solve analyses, draw results, and generate
        driving directions. This tool outputs a new network dataset and source feature
        classes; the input network dataset and its source features remain unchanged.
        Learn more about how Dissolve Network works

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset to be dissolved. The input network dataset must be a file
          or personal geodatabase network
          dataset with exactly one edge source. Any number of junction sources and turn
          sources is allowed. The edge source must have:

          * End point connectivity policy

          * An elevation policy of either None or Elevation Fields
           The input network dataset must be built before it can be used in this tool.
      out_workspace_location (Workspace):
          The geodatabase workspace in which to create the dissolved network dataset. The
          workspace must be an ArcGIS 10 geodatabase or later, and it must be a different
          geodatabase than the one where the input network dataset resides."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DissolveNetwork_na(*gp_fixargs((in_network_dataset, out_workspace_location), True)))
        return retval
    except Exception, e:
        raise e


# Server toolset
@gptooldoc('FindClosestFacilities_na', None)
def FindClosestFacilities(Incidents=None, Facilities=None, Measurement_Units=None, Network_Dataset=None, Output_Geodatabase=None, Output_Routes_Name=None, Output_Directions_Name=None, Output_Closest_Facilities_Name=None, Number_of_Facilities_to_Find=None, Default_Cutoff=None, Travel_Direction=None, Time_of_Day=None, Time_of_Day_Usage=None, Time_Zone_for_Time_of_Day=None, UTurn_Policy=None, Point_Barriers=None, Line_Barriers=None, Polygon_Barriers=None, Time_Attribute=None, Time_Attribute_Units=None, Distance_Attribute=None, Distance_Attribute_Units=None, Use_Hierarchy_in_Analysis=None, Restrictions=None, Attribute_Parameter_Values=None, Accumulate_Attributes=None, Maximum_Snap_Tolerance=None, Feature_Locator_WHERE_Clause=None, Route_Shape=None, Route_Line_Simplification_Tolerance=None, Populate_Directions=None, Directions_Language=None, Directions_Distance_Units=None, Directions_Style_Name=None, Maximum_Features_Affected_by_Point_Barriers=None, Maximum_Features_Affected_by_Line_Barriers=None, Maximum_Features_Affected_by_Polygon_Barriers=None, Maximum_Facilities=None, Maximum_Facilities_to_Find=None, Maximum_Incidents=None, Force_Hierarchy_Beyond_Distance=None, Save_Output_Network_Analysis_Layer=None, Travel_Mode=None):
    """FindClosestFacilities_na(Incidents, Facilities, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Routes_Name, Output_Directions_Name, Output_Closest_Facilities_Name, {Number_of_Facilities_to_Find}, {Default_Cutoff}, {Travel_Direction}, {Time_of_Day}, {Time_of_Day_Usage}, {Time_Zone_for_Time_of_Day}, {UTurn_Policy}, {Point_Barriers}, {Line_Barriers}, {Polygon_Barriers}, {Time_Attribute}, {Time_Attribute_Units}, {Distance_Attribute}, {Distance_Attribute_Units}, {Use_Hierarchy_in_Analysis}, {Restrictions;Restrictions...}, {Attribute_Parameter_Values}, {Accumulate_Attributes;Accumulate_Attributes...}, {Maximum_Snap_Tolerance}, {Feature_Locator_WHERE_Clause}, {Route_Shape}, {Route_Line_Simplification_Tolerance}, {Populate_Directions}, {Directions_Language}, {Directions_Distance_Units}, {Directions_Style_Name}, {Maximum_Features_Affected_by_Point_Barriers}, {Maximum_Features_Affected_by_Line_Barriers}, {Maximum_Features_Affected_by_Polygon_Barriers}, {Maximum_Facilities}, {Maximum_Facilities_to_Find}, {Maximum_Incidents}, {Force_Hierarchy_Beyond_Distance}, {Save_Output_Network_Analysis_Layer}, {Travel_Mode})

        Finds one or more facilities closest to an incident based on travel time,
        distance, or other cost and outputs the best route, chosen facility, and driving
        directions between the incident and the facility. For example, you can use this
        tool to find the closest hospital to an accident, the closest police cars to a
        crime scene, or the closest store to a customer's address.When finding closest
        facilities, you can specify how many facilities to find and
        whether the direction of travel is toward or away from them. If your network
        dataset supports traffic, you can also specify the time of day to account for
        travel times for that time and date. For instance, you can use this tool to
        search for hospitals within a 15-minute drive time of the site of an accident at
        a given time of day. Any hospitals that take longer than 15 minutes to reach
        based on the traffic conditions will not be included in the results.The Find
        Closest Facilities and Make Closest Facility Layer tools are similar,
        but they are designed for different purposes. Use Find Closest Facilities if you
        are setting up a geoprocessing service; it simplifies the setup process.
        Otherwise, use Make Closest Facility Layer.To create a closest facility
        geoprocessing service using Find Closest
        Facilities, you only need to set up one tool, and you can publish the tool
        directly as a service. In contrast, you need to create a model with the Make
        Closest Facility Layer tool, properly connect it to various other tools, and
        publish the model to create a closest-facility geoprocessing service. See
        Overview of the Network Analyst geoprocessing service examples to learn how to
        set up a closest facility service using tutorial data. One other option to
        consider is the ArcGIS Online Closest Facility service. It is a service that
        runs like a geoprocessing tool within ArcMap, can be accessed from other
        applications, and includes high quality road data for much of the world.

     INPUTS:
      Incidents (Feature Set):
          This tool determines which facilities are closest to incidents, and this
          parameter specifies those incidents. A minimum of one incident is necessary to
          solve an analysis.When specifying the incidents, you can set properties for each
          one, such as its
          name or service time, by using attributes. The incidents can be specified with
          the following attributes:OBJECTID—The system-managed ID field.SHAPE—The geometry
          field indicating the geographic location of the incident. Name—The name of the
          incident. The name is used in the driving directions. If
          the name is not specified, a unique name prefixed with Location is automatically
          generated in the output routes and directions. ID—A unique identifier for the
          incident. The identifier is included in the
          output routes (as the IncidentID field) and can help join additional information
          from the output routes, such as the total travel time or total distance, to
          attributes from your incidents or vice versa. If the ID isn't specified, the
          service autogenerates a unique identifier for each incident. AdditionalTime—The
          amount of time spent at the incident, which is added to the
          total time of the route. The units for this attribute value are specified by the
          Measurement Units parameter. The attribute value is included in the analysis
          only when the measurement units are time based. The default value is 0.If you
          are finding the closest fire stations from fire incidents to estimate
          response times, the AdditionalTime attribute can store the amount of time it
          takes firefighters to hook up their equipment at the location of the incident
          before they can begin fighting the fire. AdditionalDistance—The extra distance
          traveled at the incident, which is added
          to the total distance of the route. The units for this attribute value are
          specified by the Measurement Units parameter. The attribute value is included in
          the analysis only when the measurement units are distance based. The default
          value is 0.Generally, the location of an incident, such as a home, isn't exactly
          on the
          streets; it is set back somewhat from the road. This attribute value can be used
          to model the distance between the actual incident location and its location on
          the street, if it is important to include that distance in the total travel
          distance. CurbApproach—Specifies the direction a vehicle may arrive at and
          depart from
          the incident. The field value is specified as one of the following integers (use
          the numeric code, not the name in parentheses):

          *  0 (Either side of vehicle)—The vehicle can approach and depart the incident
          in either direction, so a U-turn is allowed at the incident. This setting can be
          chosen if it is possible and practical for your vehicle to turn around at the
          incident. This decision may depend on the width of the road and the amount of
          traffic or whether the incident has a parking lot where vehicles can pull in and
          turn around.

          * 1 ( Right side of vehicle)—When the vehicle approaches and departs the
          incident, the incident must be on the right side of the vehicle. A U-turn is
          prohibited. This is typically used for vehicles such as buses that must arrive
          with the bus stop on the right-hand side.

          * 2 (Left side of vehicle)—When the vehicle approaches and departs the incident,
          the curb must be on the left side of the vehicle. A U-turn is prohibited. This
          is typically used for vehicles such as buses that must arrive with the bus stop
          on the left-hand side.

          *  3 (No U-Turn)—When the vehicle approaches the incident, the curb can be on
          either side of the vehicle; however, the vehicle must depart without turning
          around.
          The CurbApproach property is designed to work with both kinds of national
          driving standards: right-hand traffic (United States) and left-hand traffic
          (United Kingdom). First, consider an incident on the left side of a vehicle. It
          is always on the left side regardless of whether the vehicle travels on the left
          or right half of the road. What may change with national driving standards is
          your decision to approach an incident from one of two directions, that is, so it
          ends up on the right or left side of the vehicle. For example, if you want to
          arrive at an incident and not have a lane of traffic between the vehicle and the
          incident, you would choose Right side of vehicle (1) in the United States but
          Left side of vehicle (2) in the United Kingdom.
      Facilities (Feature Set):
          This tool finds the nearest facilities to incidents, and this parameter
          specifies those facilities. A minimum of one facility is necessary to solve an
          analysis.When specifying the facilities, you can set properties for each one,
          such as its
          name or service time, by using attributes. The facilities can be specified with
          the following attributes: Name—The name of the facility. The name is used in the
          driving directions. If
          the name is not specified, a unique name prefixed with Location is automatically
          generated in the output routes and directions. ID—A unique identifier for the
          facility. The identifier is included in the
          output routes (as the FacilityID field) and the output closest facilities as
          FacilityID fields. The FacilityID field can be used to join additional
          information from the output routes, such as the total travel time or total
          distance, to attributes from your facilities. If the ID isn't specified, the
          service autogenerates a unique identifier for each facility. AdditionalTime—The
          amount of time spent at the facility, which is added to the
          total time of the route. The units for this attribute value are specified by the
          Measurement Units parameter. The attribute value is included in the analysis
          only when the measurement units are time based. The default value is 0.If you
          are finding the closest fire stations to fire incidents, AdditionalTime
          can store the time it tends to takes a crew to don the appropriate protective
          equipment and exit the fire station. AdditionalDistance—The extra distance
          traveled at the facility, which is added
          to the total distance of the route. The units for this attribute value are
          specified by the Measurement Units parameter. The attribute value is included in
          the analysis only when the measurement units are distance based. The default
          value is 0.Generally the location of a facility, such as a fire station, isn't
          exactly on a
          street; it is set back somewhat from the road. AdditionalDistance can model the
          distance between the actual facility location and its location on the street, if
          it is important to include that distance in the total travel distance.
          CurbApproach: Specifies the direction a vehicle may arrive at and depart from
          the facility. The field value is specified as one of the following integers (use
          the numeric code, not the name in parentheses):

          *  0 (Either side of vehicle)—The vehicle can approach and depart the facility
          in either direction, so a U-turn is allowed at the facility. This setting can be
          chosen if it is possible and practical for your vehicle to turn around at the
          facility. This decision may depend on the width of the road and the amount of
          traffic or whether the facility has a parking lot where vehicles can pull in and
          turn around.

          *  1 (Right side of vehicle)—When the vehicle approaches and departs the
          facility, the facility must be on the right side of the vehicle. A U-turn is
          prohibited. This is typically used for vehicles such as buses that must arrive
          with the bus stop on the right-hand side.

          *  2 (Left side of vehicle)—When the vehicle approaches and departs the
          facility, the curb must be on the left side of the vehicle. A U-turn is
          prohibited. This is typically used for vehicles such as buses that must arrive
          with the bus stop on the left-hand side.

          * 3 (No U-Turn)—When the vehicle approaches the facility, the curb can be on
          either side of the vehicle; however, the vehicle must depart without turning
          around.
          The CurbApproach property was designed to work with both kinds of national
          driving standards: right-hand traffic (United States) and left-hand traffic
          (United Kingdom). First, consider a facility on the left side of a vehicle. It
          is always on the left side regardless of whether the vehicle travels on the left
          or right half of the road. What may change with national driving standards is
          your decision to approach a facility from one of two directions, that is, so it
          ends up on the right or left side of the vehicle. For example, if you want to
          arrive at a facility and not have a lane of traffic between the vehicle and the
          facility, you would choose Right side of vehicle (1) in the United States but
          Left side of vehicle (2) in the United Kingdom.
      Measurement_Units (String):
          Specify the units that should be used to measure and report the total travel
          time or travel distance for the output routes. The tool finds the closest
          facility by measuring the travel time or the travel distance along streets.The
          units you choose for this parameter determine whether the tool will measure
          driving distance or driving time to find what is closest. Choose a time unit to
          measure driving time. To measure driving distance, choose a distance unit. Your
          choice also determines in which units the tool will report total driving time or
          distance in the results. The choices include the following:

          * Meters

          * Kilometers

          * Feet

          * Yards

          * Miles

          * NauticalMiles

          * Seconds

          * Minutes

          * Hours

          * Days
          The tool chooses whether to use the network cost attribute specified in the Time
          Attribute or Distance Attribute parameter depending on whether the chosen
          measurement units are time or distance based.The tool performs the necessary
          unit conversion when the Measurement Units value
          differs from the units of the corresponding time or distance cost attribute.
      Network_Dataset (Network Dataset Layer):
          The network dataset on which the analysis will be performed. Network datasets
          most often represent street networks but may represent other kinds of
          transportation networks as well. The network dataset needs at least one time-
          based and one distance-based cost attribute.
      Output_Geodatabase (Workspace):
          The output workspace. This workspace must already exist. The default output
          workspace is in_memory.
      Output_Routes_Name (String):
          The name of the output feature class containing routes or the lines that
          connect incidents to their closest facilities. This feature class also contains,
          as an attribute, the total cost of travel between the incidents and their
          nearest facilities.The help topic Output from Find Closest Facilities describes
          the schema of this
          output feature class.
      Output_Directions_Name (String):
          The name of the output feature class containing directions.The help topic
          Output from Find Closest Facilities describes the schema of this
          output feature class.
      Output_Closest_Facilities_Name (String):
          The name of the output feature class containing the closest facilities.The help
          topic Output from Find Closest Facilities describes the schema of this
          output feature class.
      Number_of_Facilities_to_Find {Long}:
          Specify the number of closest facilities to find per incident. This is useful
          in situations, such as a fire, where multiple fire engines may be required from
          different fire stations. You can specify, for example, to find the three nearest
          fire stations to a fire.If you are setting up a service from this tool, and you
          want to limit resource
          usage such as processing time on your server, use the Maximum Facilities to Find
          parameter to limit the maximum number of facilities a user can enter in Number
          of Facilities to Find.
      Default_Cutoff {Double}:
          Specify the travel time or travel distance value at which to stop searching for
          facilities for a given incident. For instance, while finding the closest
          hospitals from the site of an accident, a cutoff value of 15 minutes would mean
          that the tool would search for the closest hospital within 15 minutes from the
          incident. If the closest hospital is 17 minutes away, no routes will be returned
          in the output routes. A cutoff value is especially useful when searching for
          multiple facilities. The units for this parameter is specified by the
          Measurement Units parameter.
      Travel_Direction {String}:
          Specify whether you want to search for the closest facility as measured from
          the incident to the facility or from the facility to the incident.

          * TRAVEL_FROM—Direction of travel is from facilities to incidents. Fire
          departments commonly use the this setting, since they are concerned with the
          time it takes to travel from the fire station (facility) to the location of the
          emergency (incident).

          * TRAVEL_TO—Direction of travel is from incidents to facilities. Retail stores
          commonly use this setting, since they are concerned with the time it takes the
          shoppers (incidents) to reach the store (facility).
           Using one of the parameter values can find different facilities as the travel
          time along some streets may vary based on the travel direction and one-way
          restrictions. For instance, a facility may be a 10-minute drive from the
          incident while traveling from the incident to the facility, but while traveling
          from the facility to the incident, it may be a 15-minute journey because of
          different travel time in that direction. If you are setting a value for Time of
          Day, traffic may also cause the Facility to Incident and Incident to Facility
          options to return different results.
      Time_of_Day {Date}:
          Specifies the time and date at which the routes should begin or end. The value
          is used as the start time or end time for the route depending on the value for
          the Time of Day Usage parameter. If you specify the current date and time as the
          value for this parameter, the tool will use live traffic conditions to find the
          closest facilities and the total travel time will be based on traffic
          conditions.If your network dataset contains live or historical traffic data,
          specifying a
          time of day results in more accurate estimation of travel time between the
          incident and facility because the travel times account for the traffic
          conditions that are applicable for that date and time.The Time Zone for Time of
          Day parameter specifies whether this time and date
          refer to UTC or the time zone in which the facility or incident is located.
          Irrespective of the Time Zone for Time of Day setting, if your facilities and
          incidents are in multiple time zones, the following rules are enforced by the
          tool:

          *  All incidents must be in the same time zone when:

          *  Specifying a start time and traveling from incident to facility.

          *  Specifying an end time and traveling from facility to incident.


          *  All facilities must be in the same time zone when:

          *  Specifying a start time and traveling from facility to incident.

          *  Specifying an end time and traveling from incident to facility.
      Time_of_Day_Usage {String}:
          Indicates whether the Time of Day parameter value represents the arrival or
          departure time for the routes.

          * START_TIME— When this option is chosen, the tool finds the best route
          considering the time of day parameter value as the departure time from the
          facility or incident.

          * END_TIME— When this option is chosen, the tool considers the time of day
          parameter value as the arrival time at the facility or incident. This option is
          useful if you want to know what time to depart from a location so that you
          arrive at the destination at the time specified in the time of day parameter.

          * NOT_USED—When this option is chosen, the tool does not use a time of day when
          calculating the closest facilities. Live and historical traffic data will not be
          used.
      Time_Zone_for_Time_of_Day {String}:
          Specifies the time zone of the Time of Day parameter.

          * GEO_LOCAL—The Time_of_Day parameter refers to the time zone in which the
          facilities or incidents are located.

          * If Time_of_Day_Usage is set to START_TIME and Travel_Direction is TRAVEL_FROM,
          this is the time zone of the facilities.

          *  If Time_of_Day_Usage is set to START_TIME and Travel_Direction is TRAVEL_TO,
          this is the time zone of the incidents.

          * If Time_of_Day_Usage is set to END_TIME and Travel_Direction is TRAVEL_FROM,
          this is the time zone of the incidents.

          * If Time_of_Day_Usage is set to END_TIME and Travel_Direction is TRAVEL_TO,
          this is the time zone of the facilities.


          * UTC—The Time_of_Day parameter refers to Coordinated Universal Time (UTC).
          Choose this option if you want to find what's nearest for a specific time, such
          as now, but aren't certain in which time zone the facilities or incidents will
          be located.
           Irrespective of the Time Zone for Time of Day setting, if your facilities and
          incidents are in multiple time zones, the following rules are enforced by the
          tool:

          *  All incidents must be in the same time zone when:

          *  Specifying a start time and traveling from incident to facility.

          *  Specifying an end time and traveling from facility to incident.


          *  All facilities must be in the same time zone when:

          *  Specifying a start time and traveling from facility to incident.

          *  Specifying an end time and traveling from incident to facility.
      UTurn_Policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.If you need a more precisely
          defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.
      Point_Barriers {Feature Set}:
          Specifies point barriers, which are split into two types: restriction and added
          cost point barriers. They temporarily restrict traversal across or add impedance
          to points on the network. The point barriers are defined by a feature set, and
          the attribute values you specify for the point features determine whether they
          are restriction or added cost barriers. The fields in the attribute table are
          listed and described below. ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object.Name:The name of the barrier.BarrierType: Specifies whether the barrier
          restricts travel completely or adds cost when
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through the barrier. This is the default
          value.

          * Added Cost  (2)—Traversing through the barrier increases the network cost by
          the amount specified in the Additional_Time and Additional_Distance fields.
          Use the value 0 for Restriction and 2 for Added Cost.Additional_Time:Indicates
          how much travel time is added when the barrier is traversed. This
          field is applicable only for added-cost barriers and only if the measurement
          units are time based. This field value must be greater than or equal to zero,
          and its units are the same as those specified in the measurement units
          parameter.Additional_Distance:Indicates how much distance is added when the
          barrier is traversed. This field
          is applicable only for added-cost barriers and only if the measurement units are
          distance based. The field value must be greater than or equal to zero, and its
          units are the same as those specified in the measurement units parameter.
      Line_Barriers {Feature Set}:
          Specifies line barriers, which temporarily restrict traversal across them. The
          line barriers are defined by a feature set. The fields in the attribute table
          are listed and described below. ObjectID:The system-managed ID field.Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the barrier.
      Polygon_Barriers {Feature Set}:
          Specifies polygon barriers, which are split into two types: restriction and
          scaled cost polygon barriers. They temporarily restrict traversal or scale
          impedance on the parts of the network they cover. The polygon barriers are
          defined by a feature set, and the attribute values you specify for the polygon
          features determine whether they are restriction or scaled cost barriers. The
          fields in the attribute table are listed and described below. ObjectID:The
          system-managed ID field. Shape:The geometry field indicating the geographic
          location of the network analysis
          object. Name:The name of the barrier. BarrierType: Specifies whether the barrier
          restricts travel completely or scales the cost of
          traveling through it. There are two options:

          * Restriction (0)—Prohibits traversing through any part of the barrier. This is
          the default value.

          * Scaled Cost (1)—Scales the impedance of underlying edges by multiplying them
          by the value of the ScaledCostFactor property. If edges are partially covered by
          the barrier, the impedance is apportioned and multiplied.
          Use the value 0 for Restriction and 1 for Scaled Cost.ScaledTimeFactor:This is
          the factor by which the travel time of the streets intersected by the
          barrier is multiplied. This field is applicable only for scaled-cost barriers
          and only if the measurement units are time based. The field value must be
          greater than zero.ScaledDistanceFactor:This is the factor by which the distance
          of the streets intersected by the
          barrier is multiplied. This attribute is applicable only for scaled-cost
          barriers and only if the measurement units are distance based. The attribute
          value must be greater than zero.
      Time_Attribute {String}:
          Defines the network cost attribute to use when the measurement units value is a
          time unit.The tool performs the necessary time-unit conversion when the
          measurement units
          value differs from the units of the cost attribute defined here. In other words,
          the time units of the default cutoff and the network cost attribute don't need
          to be the same.The value of this parameter is overridden when Travel Mode
          (Travel_Mode in
          Python) is set to any value other than Custom.
      Time_Attribute_Units {String}:
          The units of the time attribute. You can explicitly set the time attribute
          units, but it is recommended to pass nothing or "#" and let the solver determine
          the units.The value of this parameter is overridden when Travel_Mode is set to
          any value
          other than CUSTOM.
      Distance_Attribute {String}:
          Defines the network cost attribute to use when the measurement units value is a
          distance unit.The tool performs the necessary distance-unit conversion when the
          measurement
          units value differs from the units of the cost attribute defined here. In other
          words, the measurement units and the distance units of the network cost
          attribute don't need to be the same.The value of this parameter is overridden
          when Travel Mode (Travel_Mode in
          Python) is set to any value other than Custom.
      Distance_Attribute_Units {String}:
          The units of the distance attribute. You can explicitly set the distance
          attribute units, but it is recommended to pass nothing or "#" and let the solver
          determine the units.The value of this parameter is overridden when Travel_Mode
          is set to any value
          other than CUSTOM.
      Use_Hierarchy_in_Analysis {Boolean}:
          Specify whether hierarchy should be used when finding the shortest routes
          between points.

          * True— Use hierarchy when finding routes. When hierarchy is used, the tool
          prefers higher-order streets (such as freeways) to lower-order streets (such as
          local roads) and can be used to simulate the driver preference of traveling on
          freeways instead of local roads even if that means a longer trip. This is
          especially true when finding routes to faraway facilities, because drivers on
          long-distance trips tend to prefer traveling on freeways where stops,
          intersections, and turns can be avoided. Using hierarchy is computationally
          faster, especially for long-distance routes, because the tool has to select the
          best route from a relatively smaller subset of streets.

          * False— Do not use hierarchy when finding routes. If hierarchy is not used, the
          tool considers all the streets and doesn't prefer higher-order streets when
          finding the route. This is often used when finding short-distance routes within
          a city.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.You can use the Force_Hierarchy_Beyond_Distance parameter to force the
          solve to
          use hierarchy even if  Use_Hierarchy_in_Analysis is set to False.This parameter
          is ignored unless Travel_Mode is set to CUSTOM. When modeling a
          custom walking mode, it is recommended to turn off hierarchy since the hierarchy
          is designed for motorized vehicles.
      Restrictions {String}:
          Indicates which network restriction attributes are respected during solve
          time.The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Attribute_Parameter_Values {Record Set}:
          Specifies the parameter values for network attributes that have parameters. The
          record set has two columns that work together to uniquely identify parameters
          and another column that specifies the parameter value.The value of this
          parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.The attribute parameter values
          record set has associated attributes. The fields
          in the attribute table are listed below and described. ObjectID:The system-
          managed ID field.AttributeName:The name of the network attribute whose attribute
          parameter is set by the table
          row.ParameterName:The name of the attribute parameter whose value is set by the
          table row. (Object
          type parameters cannot be updated using this tool.)ParameterValue:The value you
          want for the attribute parameter. If a value is not specified, the
          attribute parameter is set to null.
      Accumulate_Attributes {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Time Attribute (Time_Attribute in Python) or Distance Attribute
          (Distance_Attribute in Python) parameter to calculate the shortest paths. For
          each cost attribute that is accumulated, a Total_[attribute] field is added
          to the routes that are output by the solver.
      Maximum_Snap_Tolerance {Linear unit}:
          The maximum snap tolerance is the furthest distance that Network Analyst
          searches when locating or relocating a point onto the network. The search looks
          for suitable edges or junctions and snaps the point to the nearest one. If a
          suitable location isn't found within the maximum snap tolerance, the object is
          marked as unlocated.
      Feature_Locator_WHERE_Clause {String}:
          An SQL expression used to select a subset of source features that limits on
          which network elements facilities can be located. The syntax for this parameter
          consists of two parts: the first is the source feature class name (followed by a
          space) and the second is the SQL expression. To write an SQL expression for two
          or more source feature classes, separate them with a semicolon.To ensure
          facilities are not located on limited-access highways, for example,
          write an SQL expression like the following to exclude those source features:
          "Streets" "FUNC_CLASS not in('1', '2')".Note that barriers ignore the feature
          locator WHERE clause when loading.
      Route_Shape {String}:
          Specify the type of route features that are output by the tool. The parameter
          can be specified using one of the following values:

          * TRUE_LINES_WITH_MEASURES— Return the exact shape of the resulting route based
          on the underlying streets. Additionally, construct measures so the shape may be
          used in linear referencing.

          * TRUE_LINES_WITHOUT_MEASURES— Return the exact shape of the resulting route
          based on the underlying streets.

          * STRAIGHT_LINES— Return a straight line between the incident and the facility.

          * NO_LINES— Do not return any shapes for the routes. This value can be useful in
          cases where you are only interested in determining the total travel time or
          travel distance between the closest facility and the incident.
           When the Route Shape parameter is set to True Shape, the generalization of the
          route shape can be further controlled using the appropriate values for the Route
          Line Simplification Tolerance parameters. No matter which value you choose for
          the Route Shape parameter, the best route
          is always determined by minimizing the travel time or the travel distance, never
          using the straight-line distance between incidents and facilities. This means
          that only the route shapes are different, not the underlying streets that are
          searched when finding the route.
      Route_Line_Simplification_Tolerance {Linear unit}:
          Specify by how much you want to simplify the route geometry.The tool ignores
          this parameter if the Route_Shape parameter isn't set to
          TRUE_LINES_WITH_MEASURES or TRUE_LINES_WITHOUT_MEASURES. Simplification
          maintains critical points on a route, such as turns at
          intersections, to define the essential shape of the route and removes other
          points. The simplification distance you specify is the maximum allowable offset
          that the simplified line can deviate from the original line. Simplifying a line
          reduces the number of vertices that are part of the route geometry. This
          improves the tool execution time.The value of this parameter is overridden when
          Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Populate_Directions {Boolean}:
          Specify whether the tool should generate driving directions for each route.

          * Checked (True)—Indicates that the directions will be generated and configured
          based on the values for the Directions Language, Directions Style Name, and
          Directions Distance Units parameters.

          * Unchecked (False)—Directions are not generated, and the tool returns an empty
          Directions layer.
      Directions_Language {String}:
          Specify the language that should be used when generating driving
          directions.This parameter is used only when the Populate Directions parameter is
          checked,
          or set to True.The directions languages that are available depend on what ArcGIS
          language packs
          you have installed on your computer. The values are entered in two- or five-
          character language codes, for example, en for English or zh-CN for simplified
          Chinese. If an unsupported language code is specified, the tool returns the
          directions
          using the default language, English.
      Directions_Distance_Units {String}:
          Specify the units for displaying travel distance in the driving directions.
          This parameter is used only when the Populate Directions parameter is checked,
          or set to True.

          * Miles

          * Kilometers

          * Meters

          * Feet

          * Yards

          * NauticalMiles
      Directions_Style_Name {String}:
          Specify the name of the formatting style for the directions. This parameter is
          used only when the Populate Directions parameter is checked, or set to True. The
          parameter can be specified using the following values:

          * NA Desktop— Generates turn-by-turn directions suitable for printing.

          * NA Navigation— Generates turn-by-turn directions designed for an in-vehicle
          navigation device.

          * NA Campus—Generates directions appropriate for pedestrian networks, including
          sidewalks and building interiors.
      Maximum_Features_Affected_by_Point_Barriers {Long}:
          Limits how many features can be affected by point barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Line_Barriers {Long}:
          Limits how many features can be affected by line barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Polygon_Barriers {Long}:
          Limits how many features can be affected by polygon barriers.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Facilities {Long}:
          Limits how many facilities can be added to the closest facility analysis.This
          parameter helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Facilities_to_Find {Long}:
          Limits how many facilities the user can ask the service to find.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Incidents {Long}:
          Limits how many incidents can be added to the closest facility analysis.This
          parameter helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Force_Hierarchy_Beyond_Distance {Double}:
          Specifies the distance after which the solver will force hierarchy, even if
          hierarchy is not enabled, when finding closest facilities. The units of this
          parameter are the same as those shown in the Distance Attribute Units
          parameter.Finding closest facilities that are far away while using the network's
          hierarchy
          tends to incur much less processing than finding the same closest facilities
          without using the hierarchy. This parameter helps you govern the amount of
          processing that occurs when solving.A null value indicates that the hierarchy
          will never be enforced and the value
          of the Use Hierarchy in Analysis parameter will always be honored. If the input
          network dataset does not support hierarchy, specifying a value for this
          parameter will result in an error. A null value should be used in this case.
      Save_Output_Network_Analysis_Layer {Boolean}:
          * NO_SAVE_OUTPUT_LAYER—A network analysis layer isn't included in the output.

          * SAVE_OUTPUT_LAYER—The output includes a network analysis layer of the results.
          In either case, feature classes with routes and directions are returned.
          However, a server administrator may want to choose to output a network analysis
          layer as well so the setup and results of the tool can be debugged using the
          Network Analyst controls in the ArcGIS for Desktop environment. This can make
          the debugging process much easier.In ArcGIS for Desktop, the default output
          location for the network analysis
          layer is in the scratch folder. You can determine the location of the scratch
          folder by evaluating the value of arcpy.env.scratchFolder geoprocessing
          environment. The output network analysis layer is stored as an LYR file whose
          name begins with _ags_gpna and is followed by an alphanumeric GUID.
      Travel_Mode {String}:
          Choose the mode of transportation for the analysis. CUSTOM is always a choice.
          For other travel mode names to appear, they must be present in the network
          dataset specified in the Network_Dataset parameter. (The arcpy.na.GetTravelModes
          function provides a dictionary of the travel mode objects configured on a
          network dataset, and the name property returns the name of a travel mode
          object.) A travel mode is defined on a network dataset and provides override
          values for
          parameters that, together, model car, truck, pedestrian, or other modes of
          travel. By choosing a travel mode here, you don't need to provide values for the
          following parameters, which are overridden by values specified in the network
          dataset:

          * UTurn_Policy

          * Time_Attribute

          * Time_Attribute_Units

          * Distance_Attribute

          * Distance_Attribute_Units

          * Use_Hierarchy_in_Analysis

          * Restrictions

          * Attribute_Parameter_Values

          * Route_Line_Simplification_Tolerance

          * CUSTOM—Define a travel mode that fits your specific needs. When CUSTOM is
          chosen, the tool does not override the travel mode parameters listed above. This
          is the default value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FindClosestFacilities_na(*gp_fixargs((Incidents, Facilities, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Routes_Name, Output_Directions_Name, Output_Closest_Facilities_Name, Number_of_Facilities_to_Find, Default_Cutoff, Travel_Direction, Time_of_Day, Time_of_Day_Usage, Time_Zone_for_Time_of_Day, UTurn_Policy, Point_Barriers, Line_Barriers, Polygon_Barriers, Time_Attribute, Time_Attribute_Units, Distance_Attribute, Distance_Attribute_Units, Use_Hierarchy_in_Analysis, Restrictions, Attribute_Parameter_Values, Accumulate_Attributes, Maximum_Snap_Tolerance, Feature_Locator_WHERE_Clause, Route_Shape, Route_Line_Simplification_Tolerance, Populate_Directions, Directions_Language, Directions_Distance_Units, Directions_Style_Name, Maximum_Features_Affected_by_Point_Barriers, Maximum_Features_Affected_by_Line_Barriers, Maximum_Features_Affected_by_Polygon_Barriers, Maximum_Facilities, Maximum_Facilities_to_Find, Maximum_Incidents, Force_Hierarchy_Beyond_Distance, Save_Output_Network_Analysis_Layer, Travel_Mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FindRoutes_na', None)
def FindRoutes(Stops=None, Measurement_Units=None, Network_Dataset=None, Output_Geodatabase=None, Output_Routes_Name=None, Output_Route_Edges_Name=None, Output_Directions_Name=None, Output_Stops_Name=None, Reorder_Stops_to_Find_Optimal_Routes=None, Preserve_Terminal_Stops=None, Return_to_Start=None, Use_Time_Windows=None, Time_of_Day=None, Time_Zone_for_Time_of_Day=None, UTurn_Policy=None, Point_Barriers=None, Line_Barriers=None, Polygon_Barriers=None, Time_Attribute=None, Time_Attribute_Units=None, Distance_Attribute=None, Distance_Attribute_Units=None, Use_Hierarchy_in_Analysis=None, Restrictions=None, Attribute_Parameter_Values=None, Accumulate_Attributes=None, Maximum_Snap_Tolerance=None, Feature_Locator_WHERE_Clause=None, Route_Shape=None, Route_Line_Simplification_Tolerance=None, Populate_Route_Edges=None, Populate_Directions=None, Directions_Language=None, Directions_Distance_Units=None, Directions_Style_Name=None, Maximum_Features_Affected_by_Point_Barriers=None, Maximum_Features_Affected_by_Line_Barriers=None, Maximum_Features_Affected_by_Polygon_Barriers=None, Maximum_Stops=None, Maximum_Stops_per_Route=None, Force_Hierarchy_Beyond_Distance=None, Save_Output_Network_Analysis_Layer=None, Travel_Mode=None):
    """FindRoutes_na(Stops, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Routes_Name, Output_Route_Edges_Name, Output_Directions_Name, Output_Stops_Name, {Reorder_Stops_to_Find_Optimal_Routes}, {Preserve_Terminal_Stops}, {Return_to_Start}, {Use_Time_Windows}, {Time_of_Day}, {Time_Zone_for_Time_of_Day}, {UTurn_Policy}, {Point_Barriers}, {Line_Barriers}, {Polygon_Barriers}, {Time_Attribute}, {Time_Attribute_Units}, {Distance_Attribute}, {Distance_Attribute_Units}, {Use_Hierarchy_in_Analysis}, {Restrictions;Restrictions...}, {Attribute_Parameter_Values}, {Accumulate_Attributes;Accumulate_Attributes...}, {Maximum_Snap_Tolerance}, {Feature_Locator_WHERE_Clause}, {Route_Shape}, {Route_Line_Simplification_Tolerance}, {Populate_Route_Edges}, {Populate_Directions}, {Directions_Language}, {Directions_Distance_Units}, {Directions_Style_Name}, {Maximum_Features_Affected_by_Point_Barriers}, {Maximum_Features_Affected_by_Line_Barriers}, {Maximum_Features_Affected_by_Polygon_Barriers}, {Maximum_Stops}, {Maximum_Stops_per_Route}, {Force_Hierarchy_Beyond_Distance}, {Save_Output_Network_Analysis_Layer}, {Travel_Mode})

        Finding a route analysis can mean determining the quickest or shortest way to
        travel between locations. You might want to use this tool to generate driving
        directions to visit multiple stops or to measure the distance or travel time
        between locations. The tool is capable of finding routes for one or more
        vehicles each time it runs, so you can determine the best routes for several
        drivers to visit preassigned stops, for instance, or measure in a single solve
        the distance of home-to-work trips for many commuters.The Find Routes and Make
        Route Layer tools are similar, but they are designed
        for different purposes. Use Find Routes if you are setting up a geoprocessing
        service; it simplifies the setup process. Otherwise, use Make Route Layer.To
        create a routing geoprocessing service using Find Routes, you only need to
        set up one tool, and you can publish the tool directly as a service. In
        contrast, you need to create a model with the Make Routes Layer tool, properly
        connect it to various other tools, and publish the model to create a
        geoprocessing service. See Overview of the Network Analyst geoprocessing service
        examples to learn how to set up a closest facility service using tutorial data.
        One other option to consider is the ArcGIS Online Find Routes service. It is a
        service that runs like a geoprocessing tool within ArcMap, can be accessed from
        other applications, and includes high quality road data for much of the world.

     INPUTS:
      Stops (Feature Set):
          This tool routes between the stops specified in this parameter. A minimum of two
          stops are necessary to solve an analysis.When specifying the stops, you can set
          properties for each one, such as its name
          or service time, by using attributes. The stops can be specified with the
          following attributes:OBJECTID—The system-managed ID field.SHAPE—The geometry
          field indicating the geographic location of the incident.Name—The name of the
          stop. The name is used in the driving directions. If the
          name is not specified, a unique name prefixed with Location is automatically
          generated in the output stops, routes, and directions.RouteName—The name of the
          route to which the stop is assigned. Assigning the
          same route name to different stops causes those stops to be grouped together and
          visited by the same route. You can generate many routes in a single solve by
          assigning unique route names to different groups of stops. With this tool you
          can group up to 150 stops into one route.Sequence—The output routes will visit
          the stops in the order you specify with
          this attribute. Within a group of stops that have the same RouteName value, the
          sequence number should be greater than 0 but not greater than the total number
          of stops. Also, the sequence number should not be duplicated.If Reorder Stops To
          Find Optimal Routes is checked (True), all but possibly the
          first and last sequence values for each route name are ignored so the tool can
          find the sequence that minimizes overall travel for each route. (The settings
          for Preserve Ordering of Stops and Return to Start determine whether the first
          or last sequence values for each route are ignored.)AdditionalTime—The amount of
          time spent at the stop, which is added to the total
          time of the route. The units for this attribute value are specified by the
          Measurement Units parameter. The attribute value is included in the analysis
          only when the measurement units are time based. The default value is
          0.Generally, the location of a stop, such as a home, isn't exactly on the
          streets;
          it is set back somewhat from the road. This attribute value can be used to model
          the distance between the actual stop location and its location on the street, if
          it is important to include that distance in the total travel
          distance.AdditionalDistance—The extra distance traveled at the stops, which is
          added to
          the total distance of the route. The units for this attribute value are
          specified by the Measurement Units parameter. The attribute value is included in
          the analysis only when the measurement units are distance based. The default
          value is 0.Generally, the location of a stop, such as a home, isn't exactly on
          the streets;
          it is set back somewhat from the road. This attribute value can be used to model
          the distance between the actual stop location and its location on the street, if
          it is important to include that distance in the total travel
          distance.TimeWindowStart—The earliest time the stop can be visited. Make sure
          you specify
          the value as a date and time value, such as 8/12/2015 12:15 PM. By specifying a
          start and end time for a stop's time window, you are defining when a route
          should visit the stop. As long as Use Time Windows is checked and you've chosen
          a time-based unit for Measurement Units, the tool will try to find a solution
          that minimizes overall travel and reaches the stop within the prescribed time
          window. When solving a problem that spans multiple time zones, time-window
          values refer
          to the time zone in which the stop is located.This field can contain a null
          value; a null value indicates a route can arrive
          at any time before the time indicated in the TimeWindowEnd attribute. If a null
          value is also present in TimeWindowEnd, a route can visit the stop at any
          time.TimeWindowEnd—The latest time the stop can be visited. Make sure you
          specify the
          value as a date and time value, such as 8/12/2015 12:15 PM. By specifying a
          start and end time for a stop's time window, you are defining when a route
          should visit the stop. As long as Use Time Windows is checked and you've chosen
          a time-based unit for Measurement Units, the tool will try to find a solution
          that minimizes overall travel and reaches the stop within the prescribed time
          window. When solving a problem that spans multiple time zones, time-window
          values refer
          to the time zone in which the stop is located.This field can contain a null
          value; a null value indicates a route can arrive
          at any time after the time indicated in the TimeWindowStart attribute. If a null
          value is also present in TimeWindowStart, a route can visit the stop at any
          time.CurbApproach—Specifies the direction a vehicle may arrive at and depart
          from the
          stop. The field value is specified as one of the following integers (use the
          numeric code, not the name in parentheses):

          *  0 (Either side of vehicle)—The vehicle can approach and depart the stop in
          either direction, so a U-turn is allowed at the stop. This setting can be chosen
          if it is possible and practical for your vehicle to turn around at the stop.
          This decision may depend on the width of the road and the amount of traffic or
          whether the stop has a parking lot where vehicles can enter and turn around.

          * 1 ( Right side of vehicle)—When the vehicle approaches and departs the stop,
          the stop must be on the right side of the vehicle. A U-turn is prohibited. This
          is typically used for vehicles such as buses that must arrive with the bus stop
          on the right-hand side.

          * 2 (Left side of vehicle)—When the vehicle approaches and departs the stop, the
          curb must be on the left side of the vehicle. A U-turn is prohibited. This is
          typically used for vehicles such as buses that must arrive with the bus stop on
          the left-hand side.

          *  3 (No U-Turn)—When the vehicle approaches the stop, the curb can be on either
          side of the vehicle; however, the vehicle must depart without turning around.
          The CurbApproach property is designed to work with both kinds of national
          driving standards: right-hand traffic (United States) and left-hand traffic
          (United Kingdom). First, consider a stop on the left side of a vehicle. It is
          always on the left side regardless of whether the vehicle travels on the left or
          right half of the road. What may change with national driving standards is your
          decision to approach a stop from one of two directions, that is, so it ends up
          on the right or left side of the vehicle. For example, if you want to arrive at
          a stop and not have a lane of traffic between the vehicle and the stop, you
          would choose Right side of vehicle (1) in the United States but Left side of
          vehicle (2) in the United Kingdom.
      Measurement_Units (String):
          Specify the units that should be used to measure and report the total travel
          time or travel distance for the output routes.The units you choose for this
          parameter determine whether the tool will measure
          distance or time to find the best routes. Choose a time unit to minimize travel
          time for your chosen travel mode (driving or walking time, for instance). To
          minimize travel distance for the given travel mode, choose a distance unit. Your
          choice also determines in which units the tool will report total time or
          distance in the results. The choices include the following:

          * Meters

          * Kilometers

          * Feet

          * Yards

          * Miles

          * NauticalMiles

          * Seconds

          * Minutes

          * Hours

          * Days
          The tool chooses whether to use the network cost attribute specified in the Time
          Attribute or Distance Attribute parameter depending on whether the chosen
          measurement units are time or distance based.The tool performs the necessary
          unit conversion when the Measurement Units value
          differs from the units of the corresponding time or distance cost attribute.
      Network_Dataset (Network Dataset Layer):
          The network dataset on which the analysis will be performed. Network datasets
          most often represent street networks but may represent other kinds of
          transportation networks as well. The network dataset needs at least one time-
          based and one distance-based cost attribute.
      Output_Geodatabase (Workspace):
          The output workspace. This workspace must already exist. The default output
          workspace is in_memory.
      Output_Routes_Name (String):
          The name of the output feature class containing routes or the lines that
          connect stops. This feature class also contains, as an attribute, the total
          travel time or distance.The help topic Output from Find Routes describes the
          schema of this output
          feature class.
      Output_Route_Edges_Name (String):
          The name of the output feature class containing the route edges. Route edges
          represent the individual street features that are traversed by a route.The help
          topic Output from Find Routes describes the schema of this output
          feature class.
      Output_Directions_Name (String):
          The name of the output feature class containing directions.The help topic
          Output from Find Routes describes the schema of this output
          feature class.
      Output_Stops_Name (String):
          The name of the output feature class containing the output stops.The help topic
          Output from Find Routes describes the schema of this output
          feature class.
      Reorder_Stops_to_Find_Optimal_Routes {Boolean}:
          Specify whether to visit the stops in the order you define or the order the
          tool determines will minimize overall travel.

          * Checked (True)—The stops are visited in the order you define. This is the
          default option. You can set the order of stops using a Sequence attribute in the
          input stops features or let the sequence be determined by the object ID of the
          stops.

          * Unchecked (False)—The tool determines the sequence that will minimize overall
          travel distance or time. It can reorder stops and account for time windows at
          stops. Additional parameters allow you to preserve the first or last stops while
          allowing the tool to reorder the intermediary stops.
           Finding the optimal stop order and the best routes is commonly known as solving
          the traveling salesman problem (TSP).
      Preserve_Terminal_Stops {String}:
          When Reorder Stops to Find Optimal Routes is checked (or True), you have
          options to preserve the starting or ending stops and the tool can reorder the
          rest.The first and last stops are determined by their Sequence attribute values
          or,
          if the Sequence values are null, by their Object ID values.

          * PRESERVE_BOTH—Preserves the first and last stops by input order as the first
          and last stops in the route.

          * PRESERVE_FIRST—Preserves the first stop by input order as the first stop in
          the route, but the last stop is free to be reordered.

          * PRESERVE_LAST—Preserves the last stop by input order as the last stop in the
          route, but the first stop is free to be reordered.

          * PRESERVE_NONE—Frees both the first and last stop to be reordered.
          Preserve Terminal Stops is ignored when Reorder Stops to Find Optimal Routes is
          unchecked (or False).
      Return_to_Start {Boolean}:
          Choose whether routes should start and end at the same location. With this
          option you can avoid duplicating the first stop feature and sequencing the
          duplicate stop at the end.The starting location of the route is the stop feature
          with the lowest value in
          the Sequence attribute. If the Sequence values are null, it is the stop feature
          with the lowest Object ID value.

          * Checked (True)—The route should start and end at the first stop feature. This
          is the default value.

          * Unchecked (False)—The route won't start and end at the first stop feature.
      Use_Time_Windows {Boolean}:
          Choose the mode of transportation for the analysis. CUSTOM is always a choice.
          For other travel mode names to appear, they must be present in the network
          dataset specified in the Network_Dataset parameter. (The arcpy.na.GetTravelModes
          function provides a dictionary of the travel mode objects configured on a
          network dataset, and the name property returns the name of a travel mode
          object.) A travel mode is defined on a network dataset and provides override
          values for
          parameters that, together, model car, truck, pedestrian, or other modes of
          travel. By choosing a travel mode here, you don't need to provide values for the
          following parameters, which are overridden by values specified in the network
          dataset:

          * UTurn_Policy

          * Time_Attribute

          * Time_Attribute_Units

          * Distance_Attribute

          * Distance_Attribute_Units

          * Use_Hierarchy_in_Analysis

          * Restrictions

          * Attribute_Parameter_Values

          * Route_Line_Simplification_Tolerance

          * CUSTOM—Define a travel mode that fits your specific needs. When CUSTOM is
          chosen, the tool does not override the travel mode parameters listed above. This
          is the default value.
      Time_of_Day {Date}:
          Check this option (or set it to True) if any input stops have time windows that
          specify when the route should reach the stop. You can add time windows to input
          stops by entering time values in the TimeWindowStart and TimeWindowEnd
          attributes.

          * Checked (True)—The input stops have time windows and you want the tool to try
          to honor them.

          * Unchecked (False)—The input stops don't have time windows, or if they do, you
          don't want the tool to try to honor them. This is the default value.
          The tool will take slightly longer to run when Use Time Windows is checked (or
          True), even when none of the input stops have time windows, so it is recommended
          to uncheck this option (set to False) if possible.
      Time_Zone_for_Time_of_Day {String}:
          Specifies the time and date at which the routes should begin.If your network
          dataset contains live or historical traffic data, specifying a
          time of day results in more accurate estimation of travel time between stops
          because the travel times account for the traffic conditions that are applicable
          for that date and time.The Time Zone for Time of Day parameter specifies whether
          this time and date
          refer to UTC or the time zone in which the stop is located.The tool ignores this
          parameter when Measurement Units isn't set to a time-based
          unit.
      UTurn_Policy {String}:
          Specifies the time zone of the Time of Day parameter.

          * GEO_LOCAL—The Time of Day parameter refers to Coordinated Universal Time
          (UTC). Choose this option if you want to generate a route for a specific time,
          such as now, but aren't certain in which time zone the first stop will be
          located.If you are generating many routes spanning multiple times zones, the
          start times in UTC are simultaneous. For example, a Time of Day value of 10:00
          a.m., 2 January, would mean a start time of 5:00 a.m. Eastern Standard Time
          (UTC-5:00) for routes beginning in the Eastern Time Zone and 4:00 a.m. Central
          Standard Time (UTC-6:00) for routes beginning in the Central Time Zone. Both
          routes would start at 10:00 a.m. UTC.The arrive and depart times and dates
          recorded in the output Stops feature class will refer to UTC.

          * UTC—The Time of Day parameter refers to the time zone in which the first stop
          of a route is located. If you are generating many routes that start in multiple
          times zones, the start times are staggered in Coordinated Universal Time (UTC).
          For example, a Time of Day value of 10:00 a.m., 2 January, would mean a start
          time of 10:00 a.m. Eastern Standard Time (3:00 p.m. UTC) for routes beginning in
          the Eastern Time Zone and 10:00 a.m. Central Standard Time (4:00 p.m. UTC) for
          routes beginning in the Central Time Zone. The start times are offset by one
          hour in UTC.The arrive and depart times and dates recorded in the output Stops
          feature class will refer to the local time zone of the first stop for each
          route.
      Point_Barriers {Feature Set}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges, or streets, connect
          to the junction, which is known as junction valency. The acceptable values for
          this parameter are listed below; each is followed by a description of its
          meaning in terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges, or streets. This is the default value.

          * NO_UTURNS     —U-turns are prohibited at all junctions, regardless of junction
          valency.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks modeling streets have
          extraneous junctions in the middle of road segments. This option prevents
          vehicles from making U-turns at these locations.
          The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Line_Barriers {Feature Set}:
          Specifies point barriers, which are split into two types: restriction and added
          cost point barriers. They temporarily restrict traversal across or add impedance
          to points on the network. The point barriers are defined by a feature set, and
          the attribute values you specify for the point features determine whether they
          are restriction or added cost barriers. The fields in the attribute table are
          listed and described below. ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object.Name:The name of the barrier.BarrierType: Specifies whether the barrier
          restricts travel completely or adds cost when
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through the barrier. This is the default
          value.

          * Added Cost  (2)—Traversing through the barrier increases the network cost by
          the amount specified in the Additional_Time and Additional_Distance fields.
          Use the value 0 for Restriction and 2 for Added Cost.Additional_Time:Indicates
          how much travel time is added when the barrier is traversed. This
          field is applicable only for added-cost barriers and only if the measurement
          units are time based. This field value must be greater than or equal to zero,
          and its units are the same as those specified in the Measurement Units
          parameter.Additional_Distance:Indicates how much distance is added when the
          barrier is traversed. This field
          is applicable only for added-cost barriers and only if the measurement units are
          distance based. The field value must be greater than or equal to zero, and its
          units are the same as those specified in the Measurement Units parameter.
      Polygon_Barriers {Feature Set}:
          Specifies line barriers, which temporarily restrict traversal across them. The
          line barriers are defined by a feature set. The fields in the attribute table
          are listed and described below. ObjectID:The system-managed ID field.Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the barrier.
      Time_Attribute {String}:
          Specifies polygon barriers, which are split into two types: restriction and
          scaled cost polygon barriers. They temporarily restrict traversal or scale
          impedance on the parts of the network they cover. The polygon barriers are
          defined by a feature set, and the attribute values you specify for the polygon
          features determine whether they are restriction or scaled cost barriers. The
          fields in the attribute table are listed and described below. ObjectID:The
          system-managed ID field. Shape:The geometry field indicating the geographic
          location of the network analysis
          object. Name:The name of the barrier. BarrierType: Specifies whether the barrier
          restricts travel completely or scales the cost of
          traveling through it. There are two options:

          * Restriction (0)—Prohibits traversing through any part of the barrier. This is
          the default value.

          * Scaled Cost (1)—Scales the impedance of underlying edges by multiplying them
          by the value of the ScaledCostFactor property. If edges are partially covered by
          the barrier, the impedance is apportioned and multiplied.
          Use the value 0 for Restriction and 1 for Scaled Cost.ScaledTimeFactor:This is
          the factor by which the travel time of the streets intersected by the
          barrier is multiplied. This field is applicable only for scaled-cost barriers
          and only if the measurement units are time based. The field value must be
          greater than zero.ScaledDistanceFactor:This is the factor by which the distance
          of the streets intersected by the
          barrier is multiplied. This attribute is applicable only for scaled-cost
          barriers and only if the measurement units are distance based. The attribute
          value must be greater than zero.
      Time_Attribute_Units {String}:
          Defines the network cost attribute to use when the measurement units value is a
          time unit.The tool performs the necessary time-unit conversion when the
          measurement units
          value differs from the units of the cost attribute defined here. In other words,
          the time units of the default cutoff and the network cost attribute don't need
          to be the same.The value of this parameter is overridden when Travel Mode
          (Travel_Mode in
          Python) is set to any value other than Custom.
      Distance_Attribute {String}:
          The units of the time attribute. You can explicitly set the time attribute
          units, but it is recommended to pass nothing or "#" and let the solver determine
          the units.The value of this parameter is overridden when Travel_Mode is set to
          any value
          other than CUSTOM.
      Distance_Attribute_Units {String}:
          Defines the network cost attribute to use when the measurement units value is a
          distance unit.The tool performs the necessary distance-unit conversion when the
          measurement
          units value differs from the units of the cost attribute defined here. In other
          words, the measurement units and the distance units of the network cost
          attribute don't need to be the same.The value of this parameter is overridden
          when Travel Mode (Travel_Mode in
          Python) is set to any value other than Custom.
      Use_Hierarchy_in_Analysis {Boolean}:
          The units of the distance attribute. You can explicitly set the distance
          attribute units, but it is recommended to pass nothing or "#" and let the solver
          determine the units.The value of this parameter is overridden when Travel_Mode
          is set to any value
          other than CUSTOM.
      Restrictions {String}:
          Specify whether hierarchy should be used when finding the shortest routes
          between points.

          * True— Use hierarchy when finding routes. When hierarchy is used, the tool
          prefers higher-order streets (such as freeways) to lower-order streets (such as
          local roads) and can be used to simulate the driver preference of traveling on
          freeways instead of local roads even if that means a longer trip. This is
          especially true when finding routes to faraway facilities, because drivers on
          long-distance trips tend to prefer traveling on freeways where stops,
          intersections, and turns can be avoided. Using hierarchy is computationally
          faster, especially for long-distance routes, because the tool has to select the
          best route from a relatively smaller subset of streets.

          * False— Do not use hierarchy when finding routes. If hierarchy is not used, the
          tool considers all the streets and doesn't prefer higher-order streets when
          finding the route. This is often used when finding short-distance routes within
          a city.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.You can use the Force_Hierarchy_Beyond_Distance parameter to force the
          solve to
          use hierarchy even if  Use_Hierarchy_in_Analysis is set to False.This parameter
          is ignored unless Travel_Mode is set to CUSTOM. When modeling a
          custom walking mode, it is recommended to turn off hierarchy since the hierarchy
          is designed for motorized vehicles.
      Attribute_Parameter_Values {Record Set}:
          Indicates which network restriction attributes are respected during solve
          time.The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Accumulate_Attributes {String}:
          Specifies the parameter values for network attributes that have parameters. The
          record set has two columns that work together to uniquely identify parameters
          and another column that specifies the parameter value.The value of this
          parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.The attribute parameter values
          record set has associated attributes. The fields
          in the attribute table are listed below and described. ObjectID:The system-
          managed ID field.AttributeName:The name of the network attribute whose attribute
          parameter is set by the table
          row.ParameterName:The name of the attribute parameter whose value is set by the
          table row. (Object
          type parameters cannot be updated using this tool.)ParameterValue:The value you
          want for the attribute parameter. If a value is not specified, the
          attribute parameter is set to null.
      Maximum_Snap_Tolerance {Linear unit}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Time Attribute (Time_Attribute in Python) or Distance Attribute
          (Distance_Attribute in Python) parameter to calculate the shortest paths. For
          each cost attribute that is accumulated, a Total_[attribute] field is added
          to the routes that are output by the solver.
      Feature_Locator_WHERE_Clause {String}:
          The maximum snap tolerance is the furthest distance that Network Analyst
          searches when locating or relocating a point onto the network. The search looks
          for suitable edges or junctions and snaps the point to the nearest one. If a
          suitable location isn't found within the maximum snap tolerance, the object is
          marked as unlocated.
      Route_Shape {String}:
          An SQL expression used to select a subset of source features that limits on
          which network elements stops can be located. The syntax for this parameter
          consists of two parts: the first is the source feature class name (followed by a
          space) and the second is the SQL expression. To write an SQL expression for two
          or more source feature classes, separate them with a semicolon.To ensure
          facilities are not located on limited-access highways, for example,
          write an SQL expression like the following to exclude those source features:
          "Streets" "FUNC_CLASS not in('1', '2')".Note that barriers ignore the feature
          locator WHERE clause when loading.
      Route_Line_Simplification_Tolerance {Linear unit}:
          Specify the type of route features that are output by the tool. The parameter
          can be specified using one of the following values:

          * TRUE_LINES_WITHOUT_MEASURES— Return the exact shape of the resulting route
          based on the underlying streets.

          * TRUE_LINES_WITH_MEASURES— Return the exact shape of the resulting route based
          on the underlying streets. Additionally, construct measures so the shape may be
          used in linear referencing.

          * STRAIGHT_LINES— Return a straight line between the stops.

          * NO_LINES— Do not return any shapes for the routes. This value can be useful in
          cases where you are only interested in determining the total travel time or
          travel distance between the stops.
           When the Route Shape parameter is set to True Shape, the generalization of the
          route shape can be further controlled using the appropriate value for the Route
          Line Simplification Tolerance parameter. No matter which value you choose for
          the Route Shape parameter, the best route
          is always determined by minimizing the travel time or the travel distance, never
          using the straight-line distance between stops. This means that only the route
          shapes are different, not the underlying streets that are searched when finding
          the route.
      Populate_Route_Edges {Boolean}:
          Specify by how much you want to simplify the route geometry.The tool ignores
          this parameter if the Route_Shape parameter isn't set to
          TRUE_LINES_WITH_MEASURES or TRUE_LINES_WITHOUT_MEASURES. Simplification
          maintains critical points on a route, such as turns at
          intersections, to define the essential shape of the route and removes other
          points. The simplification distance you specify is the maximum allowable offset
          that the simplified line can deviate from the original line. Simplifying a line
          reduces the number of vertices that are part of the route geometry. This
          improves the tool execution time.The value of this parameter is overridden when
          Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Populate_Directions {Boolean}:
          Specify whether the tool should generate driving directions for each route.

          * Checked (True)—Indicates that the directions will be generated and configured
          based on the values for the Directions Language, Directions Style Name, and
          Directions Distance Units parameters.

          * Unchecked (False)—Directions are not generated, and the tool returns an empty
          Directions layer.
      Directions_Language {String}:
          Specify whether the tool should generate edges for each route. Route edges
          represent the individual street features or other similar features that are
          traversed by a route. The output Route Edges layer is commonly used to see which
          streets or paths are traveled on the most or least by the resultant routes.

          * Checked (True)—Generate route edges. The output Route Edges layer is populated
          with line features.

          * Unchecked (False)—Don't generate route edges. The output Route Edges layer is
          returned, but it is empty.
      Directions_Distance_Units {String}:
          Specify whether the tool should generate driving directions for each route.

          * Checked (True)—Indicates that the directions will be generated and configured
          based on the values for the Directions Language, Directions Style Name, and
          Directions Distance Units parameters.

          * Unchecked (False)—Directions are not generated, and the tool returns an empty
          Directions layer.
      Directions_Style_Name {String}:
          Specify the language that should be used when generating driving
          directions.This parameter is used only when the Populate Directions parameter is
          checked,
          or set to True.The directions languages that are available depend on what ArcGIS
          language packs
          you have installed on your computer. The values are entered in two- or five-
          character language codes, for example, en for English or zh-CN for simplified
          Chinese. If an unsupported language code is specified, the tool returns the
          directions
          using the default language, English.
      Maximum_Features_Affected_by_Point_Barriers {Long}:
          Specify the units for displaying travel distance in the driving directions.
          This parameter is used only when the Populate Directions parameter is checked,
          or set to True.

          * Miles

          * Kilometers

          * Meters

          * Feet

          * Yards

          * NauticalMiles
      Maximum_Features_Affected_by_Line_Barriers {Long}:
          Specify the name of the formatting style for the directions. This parameter is
          used only when the Populate Directions parameter is checked, or set to True. The
          parameter can be specified using the following values:

          * NA Desktop— Generates turn-by-turn directions suitable for printing.

          * NA Navigation— Generates turn-by-turn directions designed for an in-vehicle
          navigation device.

          * NA Campus—Generates directions appropriate for pedestrian networks, including
          sidewalks and building interiors.
      Maximum_Features_Affected_by_Polygon_Barriers {Long}:
          Limits how many features can be affected by point barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Stops {Long}:
          Limits how many features can be affected by line barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Stops_per_Route {Long}:
          Limits how many features can be affected by polygon barriers.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Force_Hierarchy_Beyond_Distance {Double}:
          Limits how many stops can be added to the route analysis. This parameter is
          related to the Stops parameter.This parameter helps you govern the amount of
          processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Save_Output_Network_Analysis_Layer {Boolean}:
          Limits the maximum number of stops that can be assigned to each route in an
          analysis.Stops are preassigned to routes using the RouteName field of points in
          the Stops
          parameter.This parameter helps you govern the amount of processing that occurs
          when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Travel_Mode {String}:
          Specifies the distance after which the solver will force hierarchy when finding
          routes, even if hierarchy is not enabled. The units of this parameter are the
          same as those shown in the Distance Attribute Units parameter.Finding routes
          between stops that are far away while using the network's
          hierarchy tends to incur much less processing than finding the same routes
          without using the hierarchy. This parameter helps you govern the amount of
          processing that occurs when solving.A null value indicates that the hierarchy
          will never be enforced and the value
          of the Use Hierarchy in Analysis parameter will always be honored. If the input
          network dataset does not support hierarchy, specifying a value for this
          parameter will result in an error. A null value should be used in this case.This
          parameter is disabled unless the network dataset includes a hierarchy
          attribute."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FindRoutes_na(*gp_fixargs((Stops, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Routes_Name, Output_Route_Edges_Name, Output_Directions_Name, Output_Stops_Name, Reorder_Stops_to_Find_Optimal_Routes, Preserve_Terminal_Stops, Return_to_Start, Use_Time_Windows, Time_of_Day, Time_Zone_for_Time_of_Day, UTurn_Policy, Point_Barriers, Line_Barriers, Polygon_Barriers, Time_Attribute, Time_Attribute_Units, Distance_Attribute, Distance_Attribute_Units, Use_Hierarchy_in_Analysis, Restrictions, Attribute_Parameter_Values, Accumulate_Attributes, Maximum_Snap_Tolerance, Feature_Locator_WHERE_Clause, Route_Shape, Route_Line_Simplification_Tolerance, Populate_Route_Edges, Populate_Directions, Directions_Language, Directions_Distance_Units, Directions_Style_Name, Maximum_Features_Affected_by_Point_Barriers, Maximum_Features_Affected_by_Line_Barriers, Maximum_Features_Affected_by_Polygon_Barriers, Maximum_Stops, Maximum_Stops_per_Route, Force_Hierarchy_Beyond_Distance, Save_Output_Network_Analysis_Layer, Travel_Mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateServiceAreas_na', None)
def GenerateServiceAreas(Facilities=None, Break_Values=None, Break_Units=None, Network_Dataset=None, Service_Areas=None, Travel_Direction=None, Time_of_Day=None, UTurn_Policy=None, Point_Barriers=None, Line_Barriers=None, Polygon_Barriers=None, Time_Attribute=None, Time_Attribute_Units=None, Distance_Attribute=None, Distance_Attribute_Units=None, Use_Hierarchy_in_Analysis=None, Restrictions=None, Attribute_Parameter_Values=None, Maximum_Snap_Tolerance=None, Exclude_Restricted_Portions_of_the_Network=None, Feature_Locator_WHERE_Clause=None, Polygons_for_Multiple_Facilities=None, Polygon_Overlap_Type=None, Detailed_Polygons=None, Polygon_Trim_Distance=None, Polygon_Simplification_Tolerance=None, Maximum_Facilities=None, Maximum_Number_of_Breaks=None, Maximum_Features_Affected_by_Point_Barriers=None, Maximum_Features_Affected_by_Line_Barriers=None, Maximum_Features_Affected_by_Polygon_Barriers=None, Maximum_Break_Time_Value=None, Maximum_Break_Distance_Value=None, Force_Hierarchy_beyond_Break_Time_Value=None, Force_Hierarchy_beyond_Break_Distance_Value=None, Save_Output_Network_Analysis_Layer=None, Time_Zone_for_Time_of_Day=None, Travel_Mode=None):
    """GenerateServiceAreas_na(Facilities, Break_Values, Break_Units, Network_Dataset, Service_Areas, {Travel_Direction}, {Time_of_Day}, {UTurn_Policy}, {Point_Barriers}, {Line_Barriers}, {Polygon_Barriers}, {Time_Attribute}, {Time_Attribute_Units}, {Distance_Attribute}, {Distance_Attribute_Units}, {Use_Hierarchy_in_Analysis}, {Restrictions;Restrictions...}, {Attribute_Parameter_Values}, {Maximum_Snap_Tolerance}, {Exclude_Restricted_Portions_of_the_Network}, {Feature_Locator_WHERE_Clause}, {Polygons_for_Multiple_Facilities}, {Polygon_Overlap_Type}, {Detailed_Polygons}, {Polygon_Trim_Distance}, {Polygon_Simplification_Tolerance}, {Maximum_Facilities}, {Maximum_Number_of_Breaks}, {Maximum_Features_Affected_by_Point_Barriers}, {Maximum_Features_Affected_by_Line_Barriers}, {Maximum_Features_Affected_by_Polygon_Barriers}, {Maximum_Break_Time_Value}, {Maximum_Break_Distance_Value}, {Force_Hierarchy_beyond_Break_Time_Value}, {Force_Hierarchy_beyond_Break_Distance_Value}, {Save_Output_Network_Analysis_Layer}, {Time_Zone_for_Time_of_Day}, {Travel_Mode})

        Creates a service area network analysis layer, sets the analysis properties, and
        solves the analysis. This tool is ideal for setting up a service area
        geoprocessing service on the web. A network service area is a region that
        encompasses all streets that can be accessed within a given distance or travel
        time from one or more facilities. Service areas are commonly used to visualize
        and measure accessibility. For
        example, a three-minute, drive-time polygon around a grocery store can determine
        which residents are able to reach the store within three minutes and are thus
        more likely to shop there.The Generate Service Areas and Make Service Area Layer
        tools are similar, but
        they are designed for different purposes. Use Generate Service Areas if you are
        setting up a geoprocessing service; it will simplify the setup process.
        Otherwise, use Make Service Area Layer. Also, use Make Service Area Layer if you
        need to generate service area lines; Generate Service Areas doesn't provide the
        option to generate lines.To create a service-area geoprocessing service using
        Generate Service Areas, you
        only need to set up one tool, and you can publish the tool directly as a
        service. In contrast, you need to create a model with the Make Service Area
        Layer, properly connect it to various other tools, and publish the model to
        create a service-area geoprocessing service. See Geoprocessing service example:
        Drive-time polygons to learn how to set up a drive-time polygons service using
        tutorial data. One other option to consider is the ArcGIS Online Generate
        Service Areas service. It is a service that runs like a geoprocessing tool
        within ArcMap, can be accessed from other applications, and includes high
        quality road data for much of the world.

     INPUTS:
      Facilities (Feature Set):
          The facilities around which service areas are generated.The facilities feature
          set has three attributes: ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the facility. If the name is empty, blank, or null, a
          name is
          automatically generated at solve time.
      Break_Values (String):
          Specifies the size and number of service area polygons to generate for each
          facility. The units are determined by the Break Units value.When the Generate
          Service Areas tool runs, a noteworthy interaction occurs among
          the following parameters: Break Values, Break Units, and either Time Attribute
          or Distance Attribute. Together, Break Values and Break Units define how far or
          how long the service area should extend around the facility or facilities. The
          Time Attribute and Distance Attribute parameters each define one network cost
          attribute. Only one of these two cost attributes is used, however, and the one
          that the solver chooses to use corresponds with the Break Units value; that is,
          when you specify a time-based Break Unit value, such as seconds or minutes, the
          tool solves using the cost attribute defined in the Time Attribute parameter.
          When you specify a distance-based Break Unit value, such as kilometers or miles,
          it uses the cost attribute defined in the Distance Attribute parameter.Multiple
          polygon breaks can be set to create concentric service areas per
          facility. For instance, to find two-, three-, and five-mile service areas for
          each facility, enter 2 3 5, separating the values with a space. Set Break Units
          to Miles and ensure that you have chosen a distance-based network attribute for
          the Distance Attribute parameter.
      Break_Units (String):
          The units for the Break Values parameter.

          * Meters

          * Kilometers

          * Feet

          * Yards

          * Miles

          * NauticalMiles

          * Seconds

          * Minutes

          * Hours

          * Days
          The Generate Service Areas tool chooses whether to use the network cost
          attribute specified in the Time Attribute or Distance Attribute parameter
          depending on whether the units you specify here are time or distance based.The
          tool performs the necessary units conversion when the Break Units value
          differs from the units of the corresponding time or distance cost attribute.
      Network_Dataset (Network Dataset Layer):
          The network dataset on which the analysis will be performed. Network datasets
          most often represent street networks but may represent other kinds of
          transportation networks as well. The network dataset needs at least one time-
          based and one distance-based cost attribute.
      Travel_Direction {String}:
          Choose whether the direction of travel used to generate the service area
          polygons is toward or away from the facilities.

          * TRAVEL_FROM—The service area is generated in the direction away from the
          facilities.

          * TRAVEL_TO—The service area is created in the direction toward the facilities.
           The direction of travel may change the shape of the polygons because impedances
          on opposite sides of a street may differ, or one-way streets may exist. The
          direction you should choose depends on the nature of your service area analysis.
          The service area for a pizza delivery store, for example, should be created away
          from the facility, whereas the service area of a hospital should be created
          toward the facility since the critical travel time for a patient is traveling to
          the hospital.
      Time_of_Day {Date}:
          The time to depart from or arrive at the facilities. The interpretation of this
          value depends on whether travel is toward or away from the facilities.

          * It represents the departure time if Travel Direction is set to travel away
          from facilities.

          * It represents the arrival time if Travel Direction is set to travel toward
          facilities.
          Your network dataset must include traffic data for this parameter to have any
          effect.Repeatedly solving the same analysis, but using different Time of Day
          values,
          allows you to see how a facility's reach changes over time. For instance, the
          five-minute service area around a fire station may start out large in the early
          morning, diminish during the morning rush hour, grow in the late morning, and so
          on, throughout the day.
      UTurn_Policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.The
          value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Point_Barriers {Feature Set}:
          Specifies point barriers, which are split into two types: restriction and added
          cost point barriers. They temporarily restrict traversal across or add impedance
          to points on the network. The point barriers are defined by a feature set, and
          the attribute values you specify for the point features determine whether they
          are restriction or added cost barriers. The fields in the attribute table are
          listed and described below. ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object.Name:The name of the barrier.BarrierType: Specifies whether the barrier
          restricts travel completely or adds cost when
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through the barrier. This is the default
          value.

          * Added Cost  (2)—Traversing through the barrier increases the network cost by
          the amount specified in the Additional_Time and Additional_Distance fields.
          Use the value 0 for Restriction and 2 for Added
          Cost.AdditionalCost:AdditionalCost indicates how much impedance is added when a
          service area passes
          through the barrier.The unit for this field value is the same as the units
          specified for Break
          Units.
      Line_Barriers {Feature Set}:
          Specifies line barriers, which temporarily restrict traversal across them. The
          line barriers are defined by a feature set. The fields in the attribute table
          are listed and described below. ObjectID:The system-managed ID field.Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the barrier.
      Polygon_Barriers {Feature Set}:
          Specifies polygon barriers, which are split into two types: restriction and
          scaled cost polygon barriers. They temporarily restrict traversal or scale
          impedance on the parts of the network they cover. The polygon barriers are
          defined by a feature set, and the attribute values you specify for the polygon
          features determine whether they are restriction or scaled cost barriers. The
          fields in the attribute table are listed and described below. ObjectID:The
          system-managed ID field. Shape:The geometry field indicating the geographic
          location of the network analysis
          object. Name:The name of the barrier. BarrierType: Specifies whether the barrier
          restricts travel completely or scales the cost of
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through any part of the barrier. This is
          the default value.

          * Scaled Cost  (1)—Scales the impedance of underlying edges by multiplying them
          by the value of the ScaledCostFactor property. If edges are partially covered by
          the barrier, the impedance is apportioned and multiplied.
          Use the value 0 for Restriction and 1 for Scaled
          Cost.ScaledCostFactor:ScaledCostFactor indicates how much the impedance is
          multiplied by when a
          service area passes through the barrier.
      Time_Attribute {String}:
          Defines the network cost attribute to use when the Break Units value is a time
          unit.The tool performs the necessary time-unit conversion when the Break Units
          value
          differs from the units of the cost attribute defined here. In other words, the
          time units of the breaks and the network cost attribute don't need to be the
          same.The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Time_Attribute_Units {String}:
          The units of the network cost attribute specified by the Time Attribute
          parameter. This is merely an informational parameter that cannot be changed
          without directly editing the network dataset. It is also unnecessary to change
          since the unit conversions between break value units and the cost attribute are
          handled for you.The value of this parameter is overridden when Travel Mode
          (Travel_Mode in
          Python) is set to any value other than custom.
      Distance_Attribute {String}:
          Defines the network cost attribute to use when the Break Units value is a
          distance unit.The tool performs the necessary distance-unit conversion when the
          Break Units
          value differs from the units of the cost attribute defined here. In other words,
          the distance units of the breaks and the network cost attribute don't need to be
          the same.The value of this parameter is overridden when Travel Mode (Travel_Mode
          in
          Python) is set to any value other than custom.
      Distance_Attribute_Units {String}:
          The units of the network cost attribute specified by the Distance Attribute
          parameter. This is merely an informational parameter that cannot be changed
          without directly editing the network dataset. It is also unnecessary to change
          since the unit conversions between break value units and the cost attribute are
          handled for you.The value of this parameter is overridden when Travel Mode
          (Travel_Mode in
          Python) is set to any value other than custom.
      Use_Hierarchy_in_Analysis {Boolean}:
          * Checked—Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is enabled only if the
          input network dataset has a hierarchy attribute.

          * Unchecked—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is disabled if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis.You can use the Force Hierarchy Beyond
          Distance parameter to force the solver to
          use hierarchy even if Use Hierarchy in Analysis is set to false.This parameter
          is ignored unless Travel Mode is set to Custom. When modeling a
          custom walking mode, it is recommended to turn off hierarchy since the hierarchy
          is designed for motorized vehicles.

          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.You can use the Force_Hierarchy_Beyond_Distance parameter to force the
          solve to
          use hierarchy even if  Use_Hierarchy_in_Analysis is set to False.This parameter
          is ignored unless Travel_Mode is set to CUSTOM. When modeling a
          custom walking mode, it is recommended to turn off hierarchy since the hierarchy
          is designed for motorized vehicles.
      Restrictions {String}:
          Indicates which network restriction attributes are respected during solve
          time.The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Attribute_Parameter_Values {Record Set}:
          Specifies the parameter values for network attributes that have parameters. The
          record set has two columns that work together to uniquely identify parameters
          and another column that specifies the parameter value.The value of this
          parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.The attribute parameter values
          record set has associated attributes. The fields
          in the attribute table are listed below and described. ObjectID:The system-
          managed ID field.AttributeName:The name of the network attribute whose attribute
          parameter is set by the table
          row.ParameterName:The name of the attribute parameter whose value is set by the
          table row. (Object
          type parameters cannot be updated using this tool.)ParameterValue:The value you
          want for the attribute parameter. If a value is not specified, the
          attribute parameter is set to null.
      Maximum_Snap_Tolerance {Linear unit}:
          The maximum snap tolerance is the furthest distance that Network Analyst
          searches when locating or relocating a point onto the network. The search looks
          for suitable edges or junctions and snaps the point to the nearest one. If a
          suitable location isn't found within the maximum snap tolerance, the object is
          marked as unlocated.
      Exclude_Restricted_Portions_of_the_Network {Boolean}:
          * EXCLUDE—Facilities are only located on traversable portions of the network.
          This prevents locating them on elements that can't be reached during the solve
          process due to restrictions or barriers. Bear in mind that facilities may be
          located farther from their intended location than if this option were left
          unchecked.

          * INCLUDE—Facilities can be located on any of the elements of the network;
          however, the facilities that are located on restricted elements cannot be used
          during the solve process.
      Feature_Locator_WHERE_Clause {String}:
          An SQL expression used to select a subset of source features that limits which
          network elements facilities can be located on. The syntax for this parameter
          consists of two parts: the first is the source feature class name (followed by a
          space), and the second is the SQL expression. To write an SQL expression for two
          or more source feature classes, separate them with a semicolon.To ensure
          facilities are not located on limited-access highways, for example,
          write an SQL expression like the following to exclude those source features:
          "Streets" "FUNC_CLASS not in('1', '2')".Note that barriers ignore the feature
          locator WHERE clause when loading.
      Polygons_for_Multiple_Facilities {String}:
          Choose how service area polygons are generated when multiple facilities are
          present in the analysis.

          * NO_MERGE—Creates individual polygons for each facility. The polygons can
          overlap each other.

          * NO_OVERLAP— Creates individual polygons such that a polygon from one facility
          cannot overlap polygons from other facilities; furthermore, any portion of the
          network can only be covered by the service area of the nearest facility.

          * MERGE— Creates and joins the polygons of different facilities that have the
          same break value.
      Polygon_Overlap_Type {String}:
          Specifies the option to create concentric service area polygons as disks or
          rings. This option is applicable only when multiple break values are specified
          for the facilities.

          * RINGS—Does not include the area of the smaller breaks. This creates polygons
          going between consecutive breaks. Use this option if you want to find the area
          from one break to another. For instance, if you create five- and 10-minute
          service areas, then the 10-minute service area polygon will exclude the area
          under the five-minute service area polygon.

          * DISKS— Creates polygons going from the facility to the break. For instance, if
          you create five- and 10-minute service areas, then the 10-minute service area
          polygon will include the area under the five-minute service area polygon.
      Detailed_Polygons {Boolean}:
          Specifies the option to create detailed or generalized polygons.

          * SIMPLE_POLYS—Creates generalized polygons which are generated quickly and are
          fairly accurate. This is the default.

          * DETAILED_POLYS—Creates detailed polygons which accurately model the service
          area lines and may contain islands of unreached areas. This option is much
          slower than generating generalized polygons. This option isn't supported when
          using hierarchy.
      Polygon_Trim_Distance {Linear unit}:
          Specifies the distance within which the service area polygons are trimmed. This
          is useful when your data is very sparse and you don't want the service area to
          cover large areas where there are no features. No value or a value of 0 for this
          parameter specifies that the service area
          polygons should not be trimmed. The parameter value is ignored when using
          hierarchy.
      Polygon_Simplification_Tolerance {Linear unit}:
          Specify by how much you want to simplify the polygon geometry.Simplification
          maintains critical points of a polygon to define its essential
          shape and removes other points. The simplification distance you specify is the
          maximum allowable offset from the original polygon from which the simplified
          polygon can deviate. Simplifying a polygon reduces the number of vertices and
          tends to reduce drawing times.
      Maximum_Facilities {Long}:
          Limits how many facilities can be added to the service area analysis.This
          parameter helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Number_of_Breaks {Long}:
          Limits how many breaks can be added to the service area analysis.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Point_Barriers {Long}:
          Limits how many features can be affected by point barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Line_Barriers {Long}:
          Limits how many features can be affected by line barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Polygon_Barriers {Long}:
          Limits how many features can be affected by polygon barriers.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Break_Time_Value {Double}:
          Limits how large the value of the Break Value parameter can be when solving
          time-based service areas.This parameter helps you govern the amount of
          processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Break_Distance_Value {Double}:
          Limits how large the value of the Break Value parameter can be when solving
          distance-based service areas.This parameter helps you govern the amount of
          processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Force_Hierarchy_beyond_Break_Time_Value {Double}:
          Specifies the break value after which the solver will force hierarchy even if
          hierarchy was not enabled when solving time-based service areas.Solving service
          areas for high break values while using the network's hierarchy
          tends to incur much less processing than solving the same service areas without
          using the hierarchy. This parameter helps you govern the amount of processing
          that occurs when solving.A null value indicates that the hierarchy will never be
          enforced and the value
          of the Use Hierarchy in Analysis parameter will always be honored. If the input
          network dataset does not support hierarchy, specifying a value for this
          parameter will result in an error. A null value should be used in this case.
      Force_Hierarchy_beyond_Break_Distance_Value {Double}:
          Specifies the break value after which the solver will force hierarchy even if
          hierarchy was not enabled when solving distance-based service areas.Solving
          service areas for high break values while using the network's hierarchy
          tends to incur much less processing than solving the same service areas without
          using the hierarchy. This parameter helps you govern the amount of processing
          that occurs when solving.A null value indicates that the hierarchy will never be
          enforced and the value
          of the Use Hierarchy in Analysis parameter will always be honored. If the input
          network dataset does not support hierarchy, specifying a value for this
          parameter will result in an error. A null value should be used in this case.
      Save_Output_Network_Analysis_Layer {Boolean}:
          * NO_SAVE_OUTPUT_LAYER—A network analysis layer isn't included in the output.

          * SAVE_OUTPUT_LAYER—The output includes a network analysis layer of the results.
          In either case, a feature class with service area polygons is returned. However,
          a server administrator may want to choose to output a network analysis layer as
          well so that the setup and results of the tool can be debugged using the Network
          Analyst controls in the ArcGIS for Desktop environment. This can make the
          debugging process much easier.In ArcGIS for Desktop, the default output location
          for the network analysis
          layer is in the scratch folder. You can determine the location of the scratch
          folder by evaluating the value of arcpy.env.scratchFolder geoprocessing
          environment. The output network analysis layer is stored as an LYR file whose
          name starts with _ags_gpna and is followed by an alphanumeric GUID.
      Time_Zone_for_Time_of_Day {String}:
          Specifies the time zone or zones of the Time of Day parameter.

          * GEO_LOCAL—The Time of Day parameter refers to the time zone or zones in which
          the facilities are located. Therefore, the start or end times of the service
          areas are staggered by time zone.Setting Time of Day to 9:00 a.m., choosing
          geographically local for Time Zone for Time of Day, and solving causes service
          areas to be generated for 9:00 a.m. Eastern Time for any facilities in the
          Eastern Time Zone, 9:00 a.m. Central Time for facilities in the Central Time
          Zone, 9:00 a.m. Mountain Time for facilities in the Mountain Time Zone, and so
          on, for facilities in different time zones.If stores in a chain that span the
          U.S. open at 9:00 a.m. local time, this parameter value could be chosen to find
          market territories at opening time for all stores in one solve. First, the
          stores in the Eastern Time Zone open and a polygon is generated, then an hour
          later stores open in Central Time, and so on. Nine o'clock is always in local
          time but staggered in real time.

          * UTC—The Time of Day parameter refers to Coordinated Universal Time (UTC).
          Therefore, all facilities are reached or departed from simultaneously,
          regardless of the time zone or zones they are in.Setting Time of Day to 2:00
          p.m., choosing UTC, then solving causes service areas to be generated for 9:00
          a.m. Eastern Standard Time for any facilities in the Eastern Time Zone, 8:00
          a.m. Central Standard Time for facilities in the Central Time Zone, 7:00 a.m.
          Mountain Standard Time for facilities in the Mountain Time Zone, and so on, for
          facilities in different time zones. The scenario above assumes standard time.
          During daylight saving time, the
          Eastern, Central, and Mountain Times would each be one hour ahead (that is,
          10:00, 9:00, and 8:00 a.m., respectively). One of the cases in which the UTC
          option is useful is to visualize emergency-response coverage for a jurisdiction
          that is split into two time zones. The emergency vehicles are loaded as
          facilities. Time of Day is set to now in UTC. (You need to determine what the
          current time and date are in terms of UTC to correctly use this option.) Other
          properties are set and the analysis is solved. Even though a time-zone boundary
          divides the vehicles, the results show areas that can be reached given current
          traffic conditions. This same process can be used for other times as well, not
          just for now.
          Irrespective of the Time Zone for Time of Day setting, all facilities must be in
          the same time zone when Time of Day has a nonnull value and Polygons for
          Multiple Facilities is set to create merged or nonoverlapping polygons.
      Travel_Mode {String}:
          Choose the mode of transportation for the analysis. CUSTOM is always a choice.
          For other travel mode names to appear, they must be present in the network
          dataset specified in the Network_Dataset parameter. (The arcpy.na.GetTravelModes
          function provides a dictionary of the travel mode objects configured on a
          network dataset, and the name property returns the name of a travel mode
          object.) A travel mode is defined on a network dataset and provides override
          values for
          parameters that, together, model car, truck, pedestrian, or other modes of
          travel. By choosing a travel mode here, you don't need to provide values for the
          following parameters, which are overridden by values specified in the network
          dataset:

          * UTurn_Policy

          * Time_Attribute

          * Time_Attribute_Units

          * Distance_Attribute

          * Distance_Attribute_Units

          * Use_Hierarchy_in_Analysis

          * Restrictions

          * Attribute_Parameter_Values

          * Polygon_Simplification_Tolerance

          * CUSTOM—Define a travel mode that fits your specific needs. When CUSTOM is
          chosen, the tool does not override the travel mode parameters listed above. This
          is the default value.

     OUTPUTS:
      Service_Areas (Feature Class):
          The output workspace and name of the output features. This workspace must
          already exist. The default output workspace is in_memory."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateServiceAreas_na(*gp_fixargs((Facilities, Break_Values, Break_Units, Network_Dataset, Service_Areas, Travel_Direction, Time_of_Day, UTurn_Policy, Point_Barriers, Line_Barriers, Polygon_Barriers, Time_Attribute, Time_Attribute_Units, Distance_Attribute, Distance_Attribute_Units, Use_Hierarchy_in_Analysis, Restrictions, Attribute_Parameter_Values, Maximum_Snap_Tolerance, Exclude_Restricted_Portions_of_the_Network, Feature_Locator_WHERE_Clause, Polygons_for_Multiple_Facilities, Polygon_Overlap_Type, Detailed_Polygons, Polygon_Trim_Distance, Polygon_Simplification_Tolerance, Maximum_Facilities, Maximum_Number_of_Breaks, Maximum_Features_Affected_by_Point_Barriers, Maximum_Features_Affected_by_Line_Barriers, Maximum_Features_Affected_by_Polygon_Barriers, Maximum_Break_Time_Value, Maximum_Break_Distance_Value, Force_Hierarchy_beyond_Break_Time_Value, Force_Hierarchy_beyond_Break_Distance_Value, Save_Output_Network_Analysis_Layer, Time_Zone_for_Time_of_Day, Travel_Mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SolveLocationAllocation_na', None)
def SolveLocationAllocation(Facilities=None, Demand_Points=None, Measurement_Units=None, Network_Dataset=None, Output_Geodatabase=None, Output_Allocation_Lines_Name=None, Output_Facilities_Name=None, Output_Demand_Points_Name=None, Output_Route_Edges_Name=None, Problem_Type=None, Number_of_Facilities_to_Find=None, Default_Measurement_Cutoff=None, Default_Capacity=None, Target_Market_Share=None, Measurement_Transformation_Model=None, Measurement_Transformation_Factor=None, Travel_Direction=None, Time_of_Day=None, Time_Zone_for_Time_of_Day=None, UTurn_Policy=None, Point_Barriers=None, Line_Barriers=None, Polygon_Barriers=None, Time_Attribute=None, Time_Attribute_Units=None, Distance_Attribute=None, Distance_Attribute_Units=None, Use_Hierarchy_in_Analysis=None, Restrictions=None, Attribute_Parameter_Values=None, Accumulate_Attributes=None, Maximum_Snap_Tolerance=None, Feature_Locator_WHERE_Clause=None, Allocation_Line_Shape=None, Allocation_Line_Simplification_Tolerance=None, Maximum_Features_Affected_by_Point_Barriers=None, Maximum_Features_Affected_by_Line_Barriers=None, Maximum_Features_Affected_by_Polygon_Barriers=None, Maximum_Facilities=None, Maximum_Facilities_to_Find=None, Maximum_Demand_Points=None, Force_Hierarchy_Beyond_Distance=None, Save_Output_Network_Analysis_Layer=None, Travel_Mode=None):
    """SolveLocationAllocation_na(Facilities, Demand_Points, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Allocation_Lines_Name, Output_Facilities_Name, Output_Demand_Points_Name, Output_Route_Edges_Name, {Problem_Type}, {Number_of_Facilities_to_Find}, {Default_Measurement_Cutoff}, {Default_Capacity}, {Target_Market_Share}, {Measurement_Transformation_Model}, {Measurement_Transformation_Factor}, {Travel_Direction}, {Time_of_Day}, {Time_Zone_for_Time_of_Day}, {UTurn_Policy}, {Point_Barriers}, {Line_Barriers}, {Polygon_Barriers}, {Time_Attribute}, {Time_Attribute_Units}, {Distance_Attribute}, {Distance_Attribute_Units}, {Use_Hierarchy_in_Analysis}, {Restrictions;Restrictions...}, {Attribute_Parameter_Values}, {Accumulate_Attributes;Accumulate_Attributes...}, {Maximum_Snap_Tolerance}, {Feature_Locator_WHERE_Clause}, {Allocation_Line_Shape}, {Allocation_Line_Simplification_Tolerance}, {Maximum_Features_Affected_by_Point_Barriers}, {Maximum_Features_Affected_by_Line_Barriers}, {Maximum_Features_Affected_by_Polygon_Barriers}, {Maximum_Facilities}, {Maximum_Facilities_to_Find}, {Maximum_Demand_Points}, {Force_Hierarchy_Beyond_Distance}, {Save_Output_Network_Analysis_Layer}, {Travel_Mode})

        The Solve Location-Allocation tool chooses the best locations from a set of
        input locations. Input to this tool includes facilities, which provide goods or
        services, and
        demand points, which consume the goods and services. The objective is to find
        the facilities that supply the demand points most efficiently. The tool solves
        this problem by analyzing various ways the demand points can be assigned to the
        different facilities. The solution is the scenario that allocates the most
        demand to facilities and minimizes overall travel. The output includes the
        solution facilities, demand points associated with their assigned facilities,
        and lines connecting demand points to their facilities.The location-allocation
        tool can be configured to solve specific problem types.
        Examples include the following:

        * A retail store wants to see which potential store locations would need to be
        developed to capture 10 percent of the retail market in the area.


        * A fire department wants to determine where it should locate fire stations to
        reach 90 percent of the community within a four-minute response time.


        * A police department wants to preposition personnel given past criminal
        activity
        at night.


        * After a storm, a disaster response agency wants to find the best locations to
        set up triage facilities, with limited patient capacities, to tend to the
        affected population.

     INPUTS:
      Facilities (Feature Set):
          Specify one or more facilities. The tool chooses the best locations from the
          set of facilities you specify here.In a competitive analysis, in which you try
          to find the best locations in the
          face of competition, the facilities of the competitors are specified here as
          well.When defining the facilities, you can set properties for each one, such as
          the
          facility name or type, by using attributes. Facilities can be specified with the
          following fields:OBJECTID—The system-managed ID field.SHAPE—The geometry field
          indicating the geographic location of the facility.Name—The name of the
          facility. The name is included in the name of output
          allocation lines if the facility is part of the solution.FacilityType—Specifies
          whether the facility is a candidate, required, or
          competitor facility. The field value is specified as one of the following
          integers (use the numeric code, not the name in parentheses):

          * 0 (Candidate)—A facility that may be part of the solution.

          * 1 (Required)—A facility that must be part of the solution.

          * 2 (Competitor)—A rival facility that potentially removes demand from your
          facilities. Competitor facilities are specific to the Maximize Market Share and
          Target Market Share problem types; they are ignored in other problem types.
          Weight—The relative weighting of the facility, which is used to rate the
          attractiveness, desirability, or bias of one facility compared to another. For
          example, a value of 2.0 could capture the preference of customers who
          prefer, at a ratio of 2 to 1, shopping in one facility over another facility.
          Factors that potentially affect facility weight include square footage,
          neighborhood, and age of the building. Weight values other than one are only
          honored by the maximize market share and target market share problem types; they
          are ignored in other problem types.Capacity—The Capacity field is specific to
          the Maximize Capacitated Coverage
          problem type; the other problem types ignore this field.Capacity specifies how
          much weighted demand the facility is capable of
          supplying. Excess demand won't be allocated to a facility even if that demand is
          within the facility's default measurement cutoff.Any value assigned to the
          Capacity field overrides the Default Capacity
          parameter (Default_Capacity in Python) for the given facility.
          CurbApproach—Specifies the direction a vehicle may arrive at or depart from the
          facility. The field value is specified as one of the following integers (use the
          numeric code, not the name in parentheses):

          *  0 (Either side of vehicle)—The facility can be visited from either the right
          or left side of the vehicle.

          * 1 (Right side of vehicle)—Arrive at or depart the facility so that it is on
          the right side of the vehicle. This is typically used for vehicles such as buses
          that must arrive with the bus stop on the right-hand side so that passengers can
          disembark at the curb.

          * 2 (Left side of vehicle)—Arrive at or depart the facility so that it is on the
          left side of the vehicle. When the vehicle approaches and departs the facility,
          the curb must be on the left side of the vehicle. This is typically used for
          vehicles such as buses that must arrive with the bus stop on the left-hand side
          so that passengers can disembark at the curb.
          The CurbApproach property is designed to work with both kinds of national
          driving standards: right-hand traffic (United States) and left-hand traffic
          (United Kingdom). First, consider a facility on the left side of a vehicle. It
          is always on the left side regardless of whether the vehicle travels on the left
          or right half of the road. What may change with national driving standards is
          your decision to approach a facility from one of two directions, that is, so it
          ends up on the right or left side of the vehicle. For example, if you want to
          arrive at a facility and not have a lane of traffic between the vehicle and the
          incident, you would choose Right side of vehicle (1) in the United States but
          Left side of vehicle (2) in the United Kingdom.
      Demand_Points (Feature Set):
          Specify one or more demand points. The tool chooses the best facilities based
          in large part on how they serve the demand points specified here.When defining
          the demand points, you can set properties for each one, such as
          the demand-point name or weight, by using attributes. Demand points can be
          specified with the following fields:OBJECTID—The system-managed ID
          field.SHAPE—The geometry field indicating the geographic location of the
          facility.Name—The name of the demand point. The name is included in the name of
          an output
          allocation line or lines if the demand point is part of the
          solution.GroupName—The name of the group the demand point is part of. This
          property is
          ignored for the maximize capacitated coverage, target market share, and maximize
          market share problem types.If demand points share a group name, the solver
          allocates all members of the
          group to the same facility. (If constraints, such as a cutoff distance, prevent
          any of the demand points in the group from reaching the same facility, none of
          the demand points are allocated.)Weight—The relative weighting of the demand
          point. A value of 2.0 means the
          demand point is twice as important as one with a weight of 1.0. If demand points
          represent households, weight could indicate the number of people in each
          household.Cutoff_Time—The demand point can't be allocated to a facility that is
          beyond the
          travel time indicated here. This field value overrides the value of the Default
          Measurement Cutoff parameter. The units for this attribute value are specified
          by the Measurement Units
          parameter. The attribute value is referenced during the analysis only when the
          measurement units are time based. The default value is null, which means there
          isn't an override cutoff.Cutoff_Distance—The demand point can't be allocated to
          a facility that is beyond
          the travel distance indicated here. This field value overrides the value of the
          Default Measurement Cutoff parameter. The units for this attribute value are
          specified by the Measurement Units
          parameter. The attribute value is referenced during the analysis only when the
          measurement units are distance based. The default value is null, which means
          there isn't an override cutoff. CurbApproach—Specifies the direction a vehicle
          may arrive at or depart from the
          facility. The field value is specified as one of the following integers (use the
          numeric code, not the name in parentheses):

          *  0 (Either side of vehicle)—The demand point can be visited from either the
          right or left side of the vehicle.

          * 1 (Right side of vehicle)—Arrive at or depart the demand point so that it is
          on the right side of the vehicle. This is typically used for vehicles such as
          buses that must arrive with the bus stop on the right-hand side so that
          passengers can disembark at the curb.

          * 2 (Left side of vehicle)—Arrive at or depart the demand point so that it is on
          the left side of the vehicle. When the vehicle approaches and departs the demand
          point, the curb must be on the left side of the vehicle. This is typically used
          for vehicles such as buses that must arrive with the bus stop on the left-hand
          side so that passengers can disembark at the curb.
          The CurbApproach property is designed to work with both kinds of national
          driving standards: right-hand traffic (United States) and left-hand traffic
          (United Kingdom). First, consider a demand point on the left side of a vehicle.
          It is always on the left side regardless of whether the vehicle travels on the
          left or right half of the road. What may change with national driving standards
          is your decision to approach a demand point from one of two directions, that is,
          so it ends up on the right or left side of the vehicle. For example, if you want
          to arrive at a demand point and not have a lane of traffic between the vehicle
          and the demand point, you would choose Right side of vehicle (1) in the United
          States but Left side of vehicle (2) in the United Kingdom.
      Measurement_Units (String):
          Specify the units that should be used to measure the travel times or travel
          distances between demand points and facilities. The tool chooses the best
          facilities based on which ones can reach, or be reached by, the most amount of
          weighted demand with the least amount travel.The output allocation lines report
          travel distance or travel time in different
          units, including the units you specify for this parameter. The choices are

          * Miles

          * Kilometers

          * Feet

          * Yards

          * Meters

          * Inches

          * Centimeters

          * Decimeters

          * NauticalMiles
          The tool chooses whether to use the network cost attribute specified in the Time
          Attribute or Distance Attribute parameter depending on whether the chosen
          measurement units are time or distance based.The tool performs the necessary
          unit conversion when the Measurement Units value
          differs from the units of the corresponding time or distance cost attribute.
      Network_Dataset (Network Dataset Layer):
          The network dataset on which the analysis will be performed. Network datasets
          most often represent street networks but may represent other kinds of
          transportation networks as well. The network dataset needs at least one time-
          based and one distance-based cost attribute.
      Output_Geodatabase (Workspace):
          The output workspace. This workspace must already exist. The default output
          workspace is in_memory.
      Output_Allocation_Lines_Name (String):
          The name of the output feature class containing the lines that connect demand
          points to their assigned facilities.The help topic Output from Solve Location-
          Allocation describes the schema of
          this output feature class.
      Output_Facilities_Name (String):
          The name of the output feature class containing the facilities.The help topic
          Output from Solve Location-Allocation describes the schema of
          this output feature class.
      Output_Demand_Points_Name (String):
          The name of the output feature class containing the demand points.The help
          topic Output from Solve Location-Allocation describes the schema of
          this output feature class.
      Output_Route_Edges_Name (String):
          The name of the output feature class containing the route edges. Route edges
          represent the individual street features that are traversed along the shortest
          path between the demand points and the facilities to which they are
          allocated.This output is often used to determine which street segments would
          experience
          the most traffic when traveling to facilities. This information can be used, for
          example, to place advertisements or expand roads to support traffic loads during
          evacuations.To populate the output RouteEdges feature class, you need to set the
          Allocation
          Line Shape parameter to true lines.The help topic Output from Solve Location-
          Allocation describes the schema of
          this output feature class.
      Problem_Type {String}:
          Specifies the objective of the location-allocation analysis. The default
          objective is to minimize impedance.

          * MINIMIZE_ATTENDANCE—This is also known as the P-Median problem type.
          Facilities are located such that the sum of all weighted travel time or distance
          between demand points and solution facilities is minimized. (Weighted travel is
          the amount of demand allocated to a facility multiplied by the travel distance
          or time to the facility.)This problem type is traditionally used to locate
          warehouses, because it can reduce the overall transportation costs of delivering
          goods to outlets. Since Minimize Impedance reduces the overall distance the
          public needs to travel to reach the chosen facilities, the minimize impedance
          problem without an impedance cutoff is ordinarily regarded as more equitable
          than other problem types for locating some public-sector facilities such as
          libraries, regional airports, museums, department of motor vehicles offices, and
          health clinics.The following list describes how the minimize impedance problem
          type handles demand:

          * A demand point that cannot reach any facilities, due to setting a cutoff
          distance or time, is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          * A demand point that can reach two or more facilities has all its demand weight
          allocated to the nearest facility only.


          * MAXIMIZE_CAPACITATED_COVERAGE—Facilities are located such that all or the
          greatest amount of demand can be served without exceeding the capacity of any
          facility.Maximize Capacitated Coverage behaves like either the Minimize
          Impedance or Maximize Coverage problem type but with the added constraint of
          capacity. You can specify a capacity for an individual facility by assigning a
          numeric value to its corresponding Capacity field on the input facilities. If
          the Capacity field value is null, the facility is assigned a capacity from the
          Default Capacity property.Use-cases for Maximize Capacitated Coverage include
          creating territories that encompass a given number of people or businesses,
          locating hospitals or other medical facilities with a limited number of beds or
          patients who can be treated, or locating warehouses whose inventory isn't
          assumed to be unlimited. The following list describes how the Maximize
          Capacitated Coverage problem handles demand:

          * Unlike Maximize Coverage, Maximize Capacitated Coverage doesn't require a
          value for the Default Measurement Cutoff; however, when an cutoff is specified,
          any demand point outside the cutoff time or distance of all facilities is not
          allocated.

          * An allocated demand point has all or none of its demand weight assigned to a
          facility; that is, demand isn't apportioned with this problem type.

          * If the total demand that can reach a facility is greater than the capacity of
          the facility, only the demand points that maximize total captured demand and
          minimize total weighted travel are allocated.  You may notice an apparent
          inefficiency when a demand point is allocated to a
          facility that isn't the nearest solution facility. This may occur when demand
          points have varying weights and when the demand point in question can reach more
          than one facility. This kind of result indicates the nearest solution facility
          didn't have adequate capacity for the weighted demand, or the most efficient
          solution for the entire problem required one or more local inefficiencies. In
          either case, the solution is correct.


          * MAXIMIZE_COVERAGE—Facilities are located such that as much demand as possible
          is allocated to solution facilities within the impedance cutoff.Maximize
          Coverage is frequently used to locate fire stations, police stations, and ERS
          centers, because emergency services are often required to arrive at all demand
          points within a specified response time. Note that it is important for all
          organizations, and critical for emergency services, to have accurate and precise
          data so that analysis results correctly model real-world results.Pizza delivery
          businesses, as opposed to eat-in pizzerias, try to locate stores where they can
          cover the most people within a certain drive time. People who order pizzas for
          delivery don't typically worry about how far away the pizzeria is; they are
          mainly concerned with the pizza arriving within an advertised time window.
          Therefore, a pizza-delivery business would subtract pizza-preparation time from
          their advertised delivery time and solve a maximize coverage problem to choose
          the candidate facility that would capture the most potential customers in the
          coverage area. (Potential customers of eat-in pizzerias are more affected by
          distance, since they need to travel to the restaurant; thus, the attendance
          maximizing or market share problem types would better suit eat-in
          restaurants.)The following list describes how the Maximize Coverage problem
          handles demand:

          * A demand point that cannot reach any facilities due to cutoff distance or time
          is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          * A demand point that can reach two or more facilities has all its demand weight
          allocated to the nearest facility only.


          * MAXIMIZE_MARKET_SHARE—A specific number of facilities are chosen such that the
          allocated demand is maximized in the presence of competitors. The goal is to
          capture as much of the total market share as possible with a given number of
          facilities, which you specify. The total market share is the sum of all demand
          weight for valid demand points.The market share problem types require the most
          data because, along with knowing your own facilities' weight, you also need to
          know that of your competitors' facilities. The same types of facilities that use
          the Maximize Attendance problem type can also use market share problem types
          given that they have comprehensive information that includes competitor data.
          Large discount stores typically use Maximize Market Share to locate a finite set
          of new stores. The market share problem types use a Huff model, which is also
          known as a gravity model or spatial interaction.The following list describes how
          the Maximize Market Share problem handles demand:

          * A demand point that cannot reach any facilities due to a cutoff distance or
          time is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          *  A demand point that can reach two or more facilities has all its demand
          weight
          allocated to them; furthermore, the weight is split among the facilities
          proportionally to the facilities' attractiveness (facility weight) and inversely
          proportional to the distance between the facility and demand point. Given equal
          facility weights, this means more demand weight is assigned to near facilities
          than far facilities.

          *  The total market share, which can be used to calculate the captured market
          share, is the sum of the weight of all valid demand points.


          * MINIMIZE_FACILITIES—Facilities are chosen such that as much weighted demand as
          possible are allocated to solution facilities within the travel time or distance
          cutoff; additionally, the number of facilities required to cover demand is
          minimized.Minimize Facilities is the same as Maximize Coverage but with the
          exception of the number of facilities to locate, which in this case is
          determined by the solver. When the cost of building facilities is not a limiting
          factor, the same kinds of organizations that use Maximize Coverage (emergency
          response, for instance) use Minimize Facilities so that all possible demand
          points will be covered. The following list describes how the Minimize Facilities
          problem handles demand:

          * A demand point that cannot reach any facilities due to a cutoff distance or
          time is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          * A demand point that can reach two or more facilities has all its demand weight
          allocated to the nearest facility only.


          * MAXIMIZE_IMPEDANCE—This is also known as the P-Median problem type. Facilities
          are located such that the sum of all weighted travel time or distance between
          demand points and solution facilities is minimized. (Weighted travel is the
          amount of demand allocated to a facility multiplied by the travel distance or
          time to the facility.)This problem type is traditionally used to locate
          warehouses, because it can reduce the overall transportation costs of delivering
          goods to outlets. Since Minimize Impedance reduces the overall distance the
          public needs to travel to reach the chosen facilities, the minimize impedance
          problem without an impedance cutoff is ordinarily regarded as more equitable
          than other problem types for locating some public-sector facilities such as
          libraries, regional airports, museums, department of motor vehicles offices, and
          health clinics.The following list describes how the minimize impedance problem
          type handles demand:

          * A demand point that cannot reach any facilities, due to setting a cutoff
          distance or time, is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          * A demand point that can reach two or more facilities has all its demand weight
          allocated to the nearest facility only.


          * TARGET_MARKET_SHARE—Target Market Share chooses the minimum number of
          facilities necessary to capture a specific percentage of the total market share
          in the presence of competitors. The total market share is the sum of all demand
          weight for valid demand points. You set the percent of the market share you want
          to reach and let the solver choose the fewest number of facilities necessary to
          meet that threshold.The market share problem types require the most data
          because, along with knowing your own facilities' weight, you also need to know
          that of your competitors' facilities. The same types of facilities that use the
          Maximize Attendance problem type can also use market share problem types given
          that they have comprehensive information that includes competitor data.Large
          discount stores typically use the Target Market Share problem type when they
          want to know how much expansion would be required to reach a certain level of
          the market share or see what strategy would be needed just to maintain their
          current market share given the introduction of new competing facilities. The
          results often represent what stores would like to do if budgets weren't a
          concern. In other cases where budget is a concern, stores revert to the Maximize
          Market Share problem and simply capture as much of the market share as possible
          with a limited number of facilities.The following list describes how the target
          market share problem handles demand:

          * The total market share, which is used in calculating the captured market
          share, is the sum of the weight of all valid demand points.

          * A demand point that cannot reach any facilities due to a cutoff distance or
          time is not allocated.

          * A demand point that can only reach one facility has all its demand weight
          allocated to that facility.

          * A demand point that can reach two or more facilities has all its demand weight
          allocated to them; furthermore, the weight is split among the facilities
          proportionally to the facilities' attractiveness (facility weight) and inversely
          proportional to the distance between the facility and demand point. Given equal
          facility weights, this means more demand weight is assigned to near facilities
          than far facilities.
      Number_of_Facilities_to_Find {Long}:
          Specify the number of facilities the solver should choose. The default value is
          1.The facilities with a FacilityType field value of 1 (Required) are always
          chosen
          first. Any excess facilities to choose are picked from candidate facilities,
          which have a FacilityType field value of 2.Any facilities that have a
          FacilityType value of 3 (Chosen) before solving are
          treated as candidate facilities at solve time.If the number of facilities to
          find is less than the number of required
          facilities, an error occurs.Number of Facilities to Find is disabled for the
          Minimize Facilities and Target
          Market Share problem types since the solver determines the minimum number of
          facilities needed to meet the objectives.
      Default_Measurement_Cutoff {Double}:
          Specifies the maximum travel time or distance allowed between a demand point
          and the facility it is allocated to. If a demand point is outside the cutoff of
          a facility, it cannot be allocated to that facility.The default value is none,
          which means the cutoff limit doesn't apply.The units for this parameter are the
          same as those specified by the Measurement
          Units parameter.The travel time or distance cutoff is measured by the shortest
          path along roads.This property might be used to model the maximum distance that
          people are
          willing to travel to visit stores or the maximum time that is permitted for a
          fire department to reach anyone in the community.Note that demand points have
          Cutoff_Time and Cutoff_Distance fields, which, if
          set accordingly, overrides the Default Measurement Cutoff parameter. You might
          find that people in rural areas are willing to travel up to 10 miles to reach a
          facility while urbanites are only willing to travel up to two miles. Assuming
          Measurement Units is set to Miles, you can model this behavior by setting the
          default measurement cutoff to 10 and the Cutoff_Distance field value of the
          demand points in urban areas to 2.
      Default_Capacity {Double}:
          This property is specific to the Maximize Capacitated Coverage problem type. It
          is the default capacity assigned to all facilities in the analysis. You can
          override the default capacity for a facility by specifying a value in the
          facility's Capacity field. The default value is 1.
      Target_Market_Share {Double}:
          This parameter is specific to the Target Market Share problem type. It is the
          percentage of the total demand weight that you want the chosen and required
          facilities to capture. The solver chooses the minimum number of facilities
          needed to capture the target market share specified here. The default value is
          10 percent.
      Measurement_Transformation_Model {String}:
          This sets the equation for transforming the network cost between facilities and
          demand points. This property, coupled with the Impedance Parameter, specifies
          how severely the network impedance between facilities and demand points
          influences the solver's choice of facilities.In the following list of
          transformation options, d refers to demand points and
          f, facilities. "Impedance" refers to the shortest travel distance or time
          between two locations. So impedancedf is the shortest-path (time or distance)
          between demand point d and facility f, and costdf is the transformed travel time
          or distance between the facility and demand point. Lambda (λ) denotes the
          impedance parameter. The Measurement Units setting determines whether travel
          time or distance is analyzed.

          * LINEAR—costdf = λ * impedancedfThe transformed travel time or distance between
          the facility and the demand point is the same as the time or distance of the
          shortest path between the two locations. With this option, the impedance
          parameter (λ) is always set to one. This is the default.

          * POWER—costdf = impedancedfλThe transformed travel time or distance between the
          facility and the demand point is equal to the time or distance of the shortest
          path raised to the power specified by the impedance parameter (λ). Use the Power
          option with a positive impedance parameter to specify higher weight to nearby
          facilities.

          * EXPONENTIAL—costdf = e(λ * impedancedf)The transformed travel time or distance
          between the facility and the demand point is equal to the mathematical constant
          e raised to the power specified by the shortest-path network impedance
          multiplied with the impedance parameter (λ). Use the Exponential option with a
          positive impedance parameter to specify a high weight to nearby facilities.
      Measurement_Transformation_Factor {Double}:
          Provides a parameter value to the equations specified in the Measurement
          Transformation Model parameter. The parameter value is ignored when the
          impedance transformation is of type linear. For power and exponential impedance
          transformations, the value should be nonzero.The default value is 1.
      Travel_Direction {String}:
          Specify whether to measure travel times or distances from facilities to demand
          points or from demand points to facilities. The default value is to measure from
          facilities to demand points.

          * FACILITY_TO_DEMAND—Direction of travel is from facilities to demand points.
          This is the default.

          * DEMAND_TO_FACILITY—Direction of travel is from demand points to facilities.
          Travel times and distances may change based on direction of travel. If going
          from point A to point B, you may encounter less traffic or have a shorter path,
          due to one-way streets and turn restrictions, than if you were traveling in the
          opposite direction. For instance, going from point A to point B may only take 10
          minutes, but going the other direction may take 15 minutes. These differing
          measurements may affect whether demand points can be assigned to certain
          facilities because of cutoffs or, in problem types where demand is apportioned,
          affect how much demand is captured.Fire departments commonly measure from
          facilities to demand points since they
          are concerned with the time it takes to travel from the fire station to the
          location of the emergency. A retail store is more concerned with the time it
          takes shoppers to reach the store; therefore, stores commonly measure from
          demand points to facilities.Travel Direction also determines the meaning of any
          start time that is provided.
          See the Time of Day parameter for more information.
      Time_of_Day {Date}:
          Specify the time at which travel begins. This property is ignored unless
          Measurement Units are time based. The default is no time or date. When Time of
          Day isn't specified, the solver uses generic speeds—typically those from posted
          speed limits.Traffic constantly changes in reality, and as it changes, travel
          times between
          facilities and demand points also fluctuate. Therefore, indicating different
          time and date values over several analyses may affect how demand is allocated to
          facilities and which facilities are chosen in the results.The time of day always
          indicates a start time. However, travel may start from
          facilities or demand points; it depends on what you choose for the Travel
          Direction parameter.The Time Zone for Time of Day parameter specifies whether
          this time and date
          refer to UTC or the time zone in which the facility or demand point is located.
      Time_Zone_for_Time_of_Day {String}:
          Specifies the time zone of the Time of Day parameter. The default is
          geographically local.

          * GEO_LOCAL—The Time of Day parameter refers to the time zone in which the
          facilities or demand points are located. If Travel Direction is facilities to
          demand points, this is the time zone of the facilities. If Travel Direction is
          demand points to facilities, this is the time zone of the demand points.

          * UTC   —The Time of Day parameter refers to Coordinated Universal Time (UTC).
          Choose this option if you want to choose the best location for a specific time,
          such as now, but aren't certain in which time zone the facilities or demand
          points will be located.
           Irrespective of the Time Zone for Time of Day setting, the following rules are
          enforced by the tool if your facilities and demand points are in multiple time
          zones:

          * All facilities must be in the same time zone when specifying a time of day and
          travel is from facility to demand.

          * All demand points must be in the same time zone when specifying a time of day
          and travel is from demand to facility.
      UTurn_Policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges, or streets, connect
          to the junction, which is known as junction valency. The acceptable values for
          this parameter are listed below; each is followed by a description of its
          meaning in terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges, or streets. This is the default value.

          * NO_UTURNS     —U-turns are prohibited at all junctions, regardless of junction
          valency.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks modeling streets have
          extraneous junctions in the middle of road segments. This option prevents
          vehicles from making U-turns at these locations.
          The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Point_Barriers {Feature Set}:
          Specifies point barriers, which are split into two types: restriction and added
          cost point barriers. They temporarily restrict traversal across or add impedance
          to points on the network. The point barriers are defined by a feature set, and
          the attribute values you specify for the point features determine whether they
          are restriction or added cost barriers. The fields in the attribute table are
          listed and described below. ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object.Name:The name of the barrier.BarrierType: Specifies whether the barrier
          restricts travel completely or adds cost when
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through the barrier. This is the default
          value.

          * Added Cost  (2)—Traversing through the barrier increases the network cost by
          the amount specified in the Additional_Time and Additional_Distance fields.
          Use the value 0 for Restriction and 2 for Added Cost.Additional_Time:Indicates
          how much travel time is added when the barrier is traversed. This
          field is applicable only for added-cost barriers and only if the measurement
          units are time based. This field value must be greater than or equal to zero,
          and its units are the same as those specified in the Measurement Units
          parameter.Additional_Distance:Indicates how much distance is added when the
          barrier is traversed. This field
          is applicable only for added-cost barriers and only if the measurement units are
          distance based. The field value must be greater than or equal to zero, and its
          units are the same as those specified in the Measurement Units parameter.
      Line_Barriers {Feature Set}:
          Specifies line barriers, which temporarily restrict traversal across them. The
          line barriers are defined by a feature set. The fields in the attribute table
          are listed and described below. ObjectID:The system-managed ID field.Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the barrier.
      Polygon_Barriers {Feature Set}:
          Specifies polygon barriers, which are split into two types: restriction and
          scaled cost polygon barriers. They temporarily restrict traversal or scale
          impedance on the parts of the network they cover. The polygon barriers are
          defined by a feature set, and the attribute values you specify for the polygon
          features determine whether they are restriction or scaled cost barriers. The
          fields in the attribute table are listed and described below. ObjectID:The
          system-managed ID field. Shape:The geometry field indicating the geographic
          location of the network analysis
          object. Name:The name of the barrier. BarrierType: Specifies whether the barrier
          restricts travel completely or scales the cost of
          traveling through it. There are two options:

          * Restriction (0)—Prohibits traversing through any part of the barrier. This is
          the default value.

          * Scaled Cost (1)—Scales the impedance of underlying edges by multiplying them
          by the value of the ScaledCostFactor property. If edges are partially covered by
          the barrier, the impedance is apportioned and multiplied.
          Use the value 0 for Restriction and 1 for Scaled Cost.ScaledTimeFactor:This is
          the factor by which the travel time of the streets intersected by the
          barrier is multiplied. This field is applicable only for scaled-cost barriers
          and only if the measurement units are time based. The field value must be
          greater than zero.ScaledDistanceFactor:This is the factor by which the distance
          of the streets intersected by the
          barrier is multiplied. This attribute is applicable only for scaled-cost
          barriers and only if the measurement units are distance based. The attribute
          value must be greater than zero.
      Time_Attribute {String}:
          Defines the network cost attribute to use when the measurement units value is a
          time unit.The tool performs the necessary time-unit conversion when the
          measurement units
          value differs from the units of the cost attribute defined here. In other words,
          the time units of the default cutoff and the network cost attribute don't need
          to be the same.The value of this parameter is overridden when Travel Mode
          (Travel_Mode in
          Python) is set to any value other than Custom.
      Time_Attribute_Units {String}:
          The units of the time attribute. You can explicitly set the time attribute
          units, but it is recommended to pass nothing or "#" and let the solver determine
          the units.The value of this parameter is overridden when Travel_Mode is set to
          any value
          other than CUSTOM.
      Distance_Attribute {String}:
          Defines the network cost attribute to use when the measurement units value is a
          distance unit.The tool performs the necessary distance-unit conversion when the
          measurement
          units value differs from the units of the cost attribute defined here. In other
          words, the measurement units and the distance units of the network cost
          attribute don't need to be the same.The value of this parameter is overridden
          when Travel Mode (Travel_Mode in
          Python) is set to any value other than Custom.
      Distance_Attribute_Units {String}:
          The units of the distance attribute. You can explicitly set the distance
          attribute units, but it is recommended to pass nothing or "#" and let the solver
          determine the units.The value of this parameter is overridden when Travel_Mode
          is set to any value
          other than CUSTOM.
      Use_Hierarchy_in_Analysis {Boolean}:
          Specify whether hierarchy should be used when finding the shortest routes
          between points.

          * True— Use hierarchy when finding routes. When hierarchy is used, the tool
          prefers higher-order streets (such as freeways) to lower-order streets (such as
          local roads) and can be used to simulate the driver preference of traveling on
          freeways instead of local roads even if that means a longer trip. This is
          especially true when finding routes to faraway facilities, because drivers on
          long-distance trips tend to prefer traveling on freeways where stops,
          intersections, and turns can be avoided. Using hierarchy is computationally
          faster, especially for long-distance routes, because the tool has to select the
          best route from a relatively smaller subset of streets.

          * False— Do not use hierarchy when finding routes. If hierarchy is not used, the
          tool considers all the streets and doesn't prefer higher-order streets when
          finding the route. This is often used when finding short-distance routes within
          a city.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.You can use the Force_Hierarchy_Beyond_Distance parameter to force the
          solve to
          use hierarchy even if  Use_Hierarchy_in_Analysis is set to False.This parameter
          is ignored unless Travel_Mode is set to CUSTOM. When modeling a
          custom walking mode, it is recommended to turn off hierarchy since the hierarchy
          is designed for motorized vehicles.
      Restrictions {String}:
          Indicates which network restriction attributes are respected during solve
          time.The value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Attribute_Parameter_Values {Record Set}:
          Specifies the parameter values for network attributes that have parameters. The
          record set has two columns that work together to uniquely identify parameters
          and another column that specifies the parameter value.The value of this
          parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.The attribute parameter values
          record set has associated attributes. The fields
          in the attribute table are listed below and described. ObjectID:The system-
          managed ID field.AttributeName:The name of the network attribute whose attribute
          parameter is set by the table
          row.ParameterName:The name of the attribute parameter whose value is set by the
          table row. (Object
          type parameters cannot be updated using this tool.)ParameterValue:The value you
          want for the attribute parameter. If a value is not specified, the
          attribute parameter is set to null.
      Accumulate_Attributes {String}:
          List of cost attributes to be accumulated during analysis. These accumulation
          attributes are purely for reference; the solver only uses the cost attribute
          specified by the Time Attribute (Time_Attribute in Python) or Distance Attribute
          (Distance_Attribute in Python) parameter to calculate the shortest paths. For
          each cost attribute that is accumulated, a Total_[attribute] field is added
          to the routes that are output by the solver.
      Maximum_Snap_Tolerance {Linear unit}:
          The maximum snap tolerance is the furthest distance that Network Analyst
          searches when locating or relocating a point onto the network. The search looks
          for suitable edges or junctions and snaps the point to the nearest one. If a
          suitable location isn't found within the maximum snap tolerance, the object is
          marked as unlocated.
      Feature_Locator_WHERE_Clause {String}:
          An SQL expression used to select a subset of source features that limits on
          which network elements facilities and demand points can be located. The syntax
          for this parameter consists of two parts: the first is the source feature class
          name (followed by a space) and the second is the SQL expression. To write an SQL
          expression for two or more source feature classes, separate them with a
          semicolon.To ensure facilities are not located on limited-access highways, for
          example,
          write an SQL expression like the following to exclude those source features:
          "Streets" "FUNC_CLASS not in('1', '2')".Note that barriers ignore the feature
          locator WHERE clause when loading.
      Allocation_Line_Shape {String}:
          Specify the type of line features that are output by the tool. The parameter
          accepts one of the following values:

          * STRAIGHT_LINES—Return straight lines between solution facilities and the
          demand points allocated to them. This is the default. Drawing straight lines on
          a map helps you visualize how demand is allocated.

          * TRUE_LINES_WITHOUT_MEASURES—Return the exact shape of the shortest paths
          connecting solution facilities to their allocated demand points.

          * NO_LINES—Return a table containing data about the shortest paths between
          solution facilities and the demand points allocated to them, but don't return
          lines.
           No matter which value you choose for the Allocation Line Shape parameter, the
          shortest route is always determined by minimizing the travel time or the travel
          distance, never using the straight-line distance between demand points and
          facilities. That is, this parameter only changes the output line shapes; it
          doesn't change the measurement method. When the Allocation Line Shape
          (Allocation_Line_Shape in Python) parameter is
          set to True lines without measures, the generalization of the route shape can be
          further controlled using the appropriate value for the Allocation Line
          Simplification Tolerance (Allocation_Line_Simplification_Tolerance in Python)
          parameter.
      Allocation_Line_Simplification_Tolerance {Linear unit}:
          Specify by how much you want to simplify the allocation line geometry.The tool
          ignores this parameter if the Allocation Line Shape parameter
          (Allocation_Line_Shape in Python) isn't set to output true lines. Simplification
          maintains critical points on a route, such as turns at
          intersections, to define the essential shape of the route and removes other
          points. The simplification distance you specify is the maximum allowable offset
          that the simplified line can deviate from the original line. Simplifying a line
          reduces the number of vertices that are part of the route geometry. This
          improves the tool execution time and reduces the time it takes to draw lines.The
          value of this parameter is overridden when Travel Mode (Travel_Mode in
          Python) is set to any value other than custom.
      Maximum_Features_Affected_by_Point_Barriers {Long}:
          Limits how many features can be affected by point barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Line_Barriers {Long}:
          Limits how many features can be affected by line barriers.This parameter helps
          you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Features_Affected_by_Polygon_Barriers {Long}:
          Limits how many features can be affected by polygon barriers.This parameter
          helps you govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Facilities {Long}:
          Limits how many facilities can be added to the location-allocation analysis.
          This parameter is related to the Facilities parameter.This parameter helps you
          govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Facilities_to_Find {Long}:
          Limits how many facilities can be added to the location-allocation analysis.
          This parameter is related to the Number of Facilities to Find
          (Number_of_Facilities_to_Find in Python) parameter.This parameter helps you
          govern the amount of processing that occurs when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Maximum_Demand_Points {Long}:
          Limits how many demand points can be added to the location-allocation analysis.
          This parameter is related to the Demand Points (Demand_Points in Python)
          parameter.This parameter helps you govern the amount of processing that occurs
          when
          solving. For example, you could assign  a low value to this parameter for a free
          version of the service you are creating and use a higher value for a paid-
          subscription version of the service.A null value indicates there is no limit.
      Force_Hierarchy_Beyond_Distance {Double}:
          Specifies the distance after which the solver will force hierarchy, even if
          hierarchy is not enabled, when finding shortest paths between facilities and
          demand points. The units of this parameter are the same as those shown in the
          Distance Attribute Units (Distance_Attribute_Units in Python) parameter.Finding
          shortest routes between facilities and demand points that are far away
          while using the network's hierarchy tends to incur much less processing than
          finding the same routes without using the hierarchy. This parameter helps you
          govern the amount of processing that occurs when solving.A null value indicates
          that the hierarchy will never be enforced and the value
          of the Use Hierarchy in Analysis (Use_Hierarchy_in_Analysis in Python) parameter
          will always be honored. If the input network dataset does not support hierarchy,
          specifying a value for this parameter will result in an error. A null value
          should be used in this case.This parameter is disabled unless the network
          dataset includes a hierarchy
          attribute.
      Save_Output_Network_Analysis_Layer {Boolean}:
          * NO_SAVE_OUTPUT_LAYER—A network analysis layer isn't included in the output.

          * SAVE_OUTPUT_LAYER—The output includes a network analysis layer of the results.
          In either case, feature classes containing the results are returned. However, a
          server administrator may want to choose to output a network analysis layer as
          well so the setup and results of the tool can be debugged using the Network
          Analyst controls in the ArcGIS for Desktop environment. This can make the
          debugging process much easier.In ArcGIS for Desktop, the default output location
          for the network analysis
          layer is in the scratch folder. You can determine the location of the scratch
          folder by evaluating the value of arcpy.env.scratchFolder geoprocessing
          environment. The output network analysis layer is stored as an LYR file whose
          name begins with _ags_gpna and is followed by an alphanumeric GUID.
      Travel_Mode {String}:
          Choose the mode of transportation for the analysis. CUSTOM is always a choice.
          For other travel mode names to appear, they must be present in the network
          dataset specified in the Network_Dataset parameter. (The arcpy.na.GetTravelModes
          function provides a dictionary of the travel mode objects configured on a
          network dataset, and the name property returns the name of a travel mode
          object.) A travel mode is defined on a network dataset and provides override
          values for
          parameters that, together, model car, truck, pedestrian, or other modes of
          travel. By choosing a travel mode here, you don't need to provide values for the
          following parameters, which are overridden by values specified in the network
          dataset:

          * UTurn_Policy

          * Time_Attribute

          * Time_Attribute_Units

          * Distance_Attribute

          * Distance_Attribute_Units

          * Use_Hierarchy_in_Analysis

          * Restrictions

          * Attribute_Parameter_Values

          * Route_Line_Simplification_Tolerance

          * CUSTOM—Define a travel mode that fits your specific needs. When CUSTOM is
          chosen, the tool does not override the travel mode parameters listed above. This
          is the default value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SolveLocationAllocation_na(*gp_fixargs((Facilities, Demand_Points, Measurement_Units, Network_Dataset, Output_Geodatabase, Output_Allocation_Lines_Name, Output_Facilities_Name, Output_Demand_Points_Name, Output_Route_Edges_Name, Problem_Type, Number_of_Facilities_to_Find, Default_Measurement_Cutoff, Default_Capacity, Target_Market_Share, Measurement_Transformation_Model, Measurement_Transformation_Factor, Travel_Direction, Time_of_Day, Time_Zone_for_Time_of_Day, UTurn_Policy, Point_Barriers, Line_Barriers, Polygon_Barriers, Time_Attribute, Time_Attribute_Units, Distance_Attribute, Distance_Attribute_Units, Use_Hierarchy_in_Analysis, Restrictions, Attribute_Parameter_Values, Accumulate_Attributes, Maximum_Snap_Tolerance, Feature_Locator_WHERE_Clause, Allocation_Line_Shape, Allocation_Line_Simplification_Tolerance, Maximum_Features_Affected_by_Point_Barriers, Maximum_Features_Affected_by_Line_Barriers, Maximum_Features_Affected_by_Polygon_Barriers, Maximum_Facilities, Maximum_Facilities_to_Find, Maximum_Demand_Points, Force_Hierarchy_Beyond_Distance, Save_Output_Network_Analysis_Layer, Travel_Mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SolveVehicleRoutingProblem_na', None)
def SolveVehicleRoutingProblem(orders=None, depots=None, routes=None, breaks=None, time_units=None, distance_units=None, network_dataset=None, output_workspace_location=None, output_unassigned_stops_name=None, output_stops_name=None, output_routes_name=None, output_directions_name=None, default_date=None, uturn_policy=None, time_window_factor=None, spatially_cluster_routes=None, route_zones=None, route_renewals=None, order_pairs=None, excess_transit_factor=None, point_barriers=None, line_barriers=None, polygon_barriers=None, time_attribute=None, distance_attribute=None, use_hierarchy_in_analysis=None, restrictions=None, attribute_parameter_values=None, maximum_snap_tolerance=None, exclude_restricted_portions_of_the_network=None, feature_locator_where_clause=None, populate_route_lines=None, route_line_simplification_tolerance=None, populate_directions=None, directions_language=None, directions_style_name=None, save_output_layer=None, service_capabilities=None, ignore_invalid_order_locations=None, travel_mode=None):
    """SolveVehicleRoutingProblem_na(orders, depots, routes, breaks, time_units, distance_units, network_dataset, output_workspace_location, output_unassigned_stops_name, output_stops_name, output_routes_name, output_directions_name, {default_date}, {uturn_policy}, {time_window_factor}, {spatially_cluster_routes}, {route_zones}, {route_renewals}, {order_pairs}, {excess_transit_factor}, {point_barriers}, {line_barriers}, {polygon_barriers}, {time_attribute}, {distance_attribute}, {use_hierarchy_in_analysis}, {restrictions;restrictions...}, {attribute_parameter_values}, {maximum_snap_tolerance}, {exclude_restricted_portions_of_the_network}, {feature_locator_where_clause;feature_locator_where_clause...}, {populate_route_lines}, {route_line_simplification_tolerance}, {populate_directions}, {directions_language}, {directions_style_name}, {save_output_layer}, {service_capabilities;service_capabilities...}, {ignore_invalid_order_locations}, {travel_mode})

        Creates a vehicle routing problem (VRP) network analysis layer, sets the
        analysis properties, and solves the analysis, which is ideal for setting up a
        VRP web service. A vehicle routing problem analysis layer finds the best routes
        for a fleet of vehicles.The Make Vehicle Routing Problem Layer and Solve Vehicle
        Routing Problem tools
        are similar, but they are designed for different purposes. Use the Solve Vehicle
        Routing Problem tool if you are setting up a geoprocessing service; it will
        simplify the setup process. Otherwise, use the Make Vehicle Routing Problem
        Layer tool.To create a VRP geoprocessing service using Solve Vehicle Routing
        Problem Layer,
        you only need to set up one tool and publish it as a service. In contrast, you
        need to create a model with the Make Vehicle Routing Problem Layer, properly
        connect it to various other tools, and publish the model to create a service.
        One other option to consider is the ArcGIS Online Vehicle Routing Problem
        services. The services run like geoprocessing tools within ArcMap, can be
        accessed from other applications, and include high quality road data for much of
        the world.See Overview of the Network Analyst geoprocessing service examples for
        information about tutorial data for setting up a sample VRP geoprocessing
        service.

     INPUTS:
      orders (Feature Set):
          The orders that the routes of the VRP analysis should visit. An order can
          represent a delivery (for example, furniture delivery), a pickup (such as an
          airport shuttle bus picking up a passenger), or some type of service or
          inspection (a tree trimming job or building inspection, for instance).The orders
          feature set has an associated attribute table. The fields in the
          attribute table are listed below and described.ObjectID:The system-managed ID
          field.Shape:The geometry field indicating the geographic location of the network
          analysis
          object.Name:The name of the order. The name must be unique. If the name is left
          null, a name
          is automatically generated at solve time.ServiceTime: This property specifies
          how much time will be spent at the network location
          when the route visits it; that is, it stores the impedance value for the network
          location. A zero or null value indicates the network location requires no
          service time.The unit for this field value is specified by the Time Field Units
          parameter
          (time_units in Python).TimeWindowStart1:The beginning time of the first time
          window for the network location. This field
          can contain a null value; a null value indicates no beginning time.

          *  A time window only states when a vehicle can arrive at an order; it doesn't
          state when the service time must be completed. To account for service time and
          leave before the time window is over, subtract ServiceTime from the
          TimeWindowEnd1 field.

          *  The time window fields can contain a time-only value or a date and time
          value.
          If a time field such as TimeWindowStart1 has a time-only value (for example,
          8:00 AM), the date is assumed to be the date specified by the Default Date
          property of the analysis layer. Using date and time values (for example,
          7/11/2010 8:00 AM) allows you to set time windows that span multiple days.

          * The default date is ignored when any time window field includes a date with
          the
          time. To avoid an error in this situation, format all time windows in Depots,
          Routes, Orders, and Breaks to also include the date with the time.

          *  If you're using traffic data, the time-of-day fields for the network location
          always reference the same time zone as the edge on which the network location is
          located.
          TimeWindowEnd1: The ending time of the first window for the network location.
          This field can
          contain a null value; a null value indicates no ending time.TimeWindowStart2:The
          beginning time of the second time window for the network location. This
          field can contain a null value; a null value indicates that there is no second
          time window.If the first time window is null as specified by the
          TimeWindowStart1 and
          TimeWindowEnd1 fields, the second time window must also be null.If both time
          windows are nonnull, they can't overlap. Also, the second time
          window must occur after the first.TimeWindowEnd2: The ending time of the second
          time window for the network location. This field
          can contain a null value.When TimeWindowStart2 and TimeWindowEnd2 are both null,
          there is no second time
          window.When TimeWindowStart2 is not null but TimeWindowEnd2 is null, there is a
          second
          time window that has a starting time but no ending time. This is
          valid.MaxViolationTime1: A time window is considered violated if the arrival
          time occurs after the time
          window has ended. This field specifies the maximum allowable violation time for
          the first time window of the order. It can contain a zero value but can't
          contain negative values. A zero value indicates that a time window violation at
          the first time window of the order is unacceptable; that is, the first time
          window is hard. On the other hand, a null value indicates that there is no limit
          on the allowable violation time. A nonzero value specifies the maximum amount of
          lateness; for example, a route can arrive at an order up to 30 minutes beyond
          the end of its first time window.The unit for this field value is specified by
          the Time Field Units parameter
          (time_units in Python).Time window violations can be tracked and weighted by the
          solver. Because of
          this, you can direct the VRP solver to take one of three approaches:

          * Minimize the overall violation time, regardless of the increase in travel cost
          for the fleet.

          * Find a solution that balances overall violation time and travel cost.

          * Ignore the overall violation time; instead, minimize the travel cost for the
          fleet.
          By assigning an importance level for the Time Window Violation Importance
          parameter (time_window_factor for Python), you are essentially choosing one of
          these three approaches. In any case, however, the solver will return an error if
          the value set for MaxViolationTime1 is surpassed.MaxViolationTime2: The maximum
          allowable violation time for the second time window of the order.
          This field is analogous to the MaxViolationTime1 field.InboundArriveTime:Defines
          when the item to be delivered to the order will be ready at the starting
          depot.The order can be assigned to a route only if the inbound arrive time
          precedes
          the route's latest start time value; this way, the route cannot leave the depot
          before the item is ready to be loaded onto it.This field can help model
          scenarios involving inbound-wave transshipments. For
          example, a job at an order requires special materials that are not currently
          available at the depot. The materials are being shipped from another location
          and will arrive at the depot at 11:00 a.m. To ensure a route that leaves before
          the shipment arrives isn't assigned to the order, the order's inbound arrive
          time is set to 11:00 a.m. The special materials arrive at 11:00 a.m., they are
          loaded onto the vehicle, and the vehicle departs from the depot to visit its
          assigned orders.Notes:

          * The route's start time, which includes service times, must occur after the
          inbound arrive time. If a route begins before an order's inbound arrive time,
          the order cannot be assigned to the route. The assignment is invalid even if the
          route has a start-depot service time that lasts until after the inbound arrive
          time.

          * This time field can contain a time-only value or a date and time value. If a
          time-only value is set (for example, 11:00 AM), the date is assumed to be the
          date specified by the Default Date property of the analysis layer. The default
          date is ignored, however, when any time field in Depots, Routes, Orders, or
          Breaks includes a date with the time. In that case, specify all such fields with
          a date and time (for example, 7/11/2015 11:00 AM).

          * The VRP solver honors InboundArriveTime regardless of the DeliveryQuantities
          value.

          * If an outbound depart time is also specified, its time value must occur after
          the inbound arrive time.
          OutboundDepartTime:Defines when the item to be picked up at the order must
          arrive at the ending
          depot.The order can be assigned to a route only if the route can visit the order
          and
          reach its end depot before the specified outbound depart time.This field can
          help model scenarios involving outbound-wave transshipments. For
          instance, a shipping company sends out delivery trucks to pick up packages from
          orders and bring them into a depot where they are forwarded on to other
          facilities, en route to their final destination. At 3:00 p.m. every day, a
          semitrailer stops at the depot to pick up the high-priority packages and take
          them directly to a central processing station. To avoid delaying the high-
          priority packages until the next day's 3:00 p.m. trip, the shipping company
          tries to have delivery trucks pick up the high-priority packages from orders and
          bring them to the depot before the 3:00 p.m. deadline. This is done by setting
          the outbound depart time to 3:00 p.m.Notes:

          * The route's end time, including service times, must occur before the outbound
          depart time. If a route reaches a depot but doesn't complete its end-depot
          service time prior to the order's outbound depart time, the order cannot be
          assigned to the route.

          * This time field can contain a time-only value or a date and time value. If a
          time-only value is set (for example, 11:00 AM), the date is assumed to be the
          date specified by the Default Date property of the analysis layer. The default
          date is ignored, however, when any time field in Depots, Routes, Orders, or
          Breaks includes a date with the time. In that case, specify all such fields with
          a date and time (for example, 7/11/2015 11:00 AM).

          * The VRP solver honors OutboundDepartTime regardless of the PickupQuantities
          value.

          * If an inbound arrive time is also specified, its time value must occur before
          the outbound depart time.
          DeliveryQuantities:The size of the delivery. You can specify size in any
          dimension you want, such
          as weight, volume, or quantity. You can even specify multiple dimensions, for
          example, weight and volume.Enter delivery quantities without indicating units.
          For example, if a 300-pound
          object needs to be delivered to an order, enter 300. You will need to remember
          that the value is in pounds.If you are tracking multiple dimensions, separate
          the numeric values with a
          space. For instance, if you are recording the weight and volume of a delivery
          that weighs 2,000 pounds and has a volume of 100 cubic feet, enter 2000 100.
          Again, you need to remember the units—in this case, pounds and cubic feet. You
          also need to remember the sequence the values and their corresponding units are
          entered in.Make sure that Capacities for Routes and DeliveryQuantities and
          PickupQuantities
          for Orders are specified in the same manner; that is, the values need to be in
          the same units, and if you are using multiple dimensions, the dimensions need to
          be listed in the same sequence for all parameters. So if you specify weight in
          pounds, followed by volume in cubic feet for DeliveryQuantities, the capacity of
          your routes and the pickup quantities of your orders need to be specified the
          same way: weight in pounds, then volume in cubic feet. If you mix units or
          change the sequence, you will get unwanted results without receiving any warning
          messages.An empty string or null value is equivalent to all dimensions being
          zero. If the
          string has an insufficient number of values in relation to the capacity count,
          or dimensions being tracked, the remaining values are treated as zeros. Delivery
          quantities can't be negative.PickupQuantities:The size of the pickup. You can
          specify size in any dimension you want, such as
          weight, volume, or quantity. You can even specify multiple dimensions, for
          example, weight and volume. You cannot, however, use negative values. This field
          is analogous to the DeliveryQuantities field of Orders.In the case of an
          exchange visit, an order can have both delivery and pickup quantities.
          Revenue:The income generated if the order is included in a solution. This field
          can
          contain a null value—a null value indicates zero revenue—but it can't have a
          negative value.Revenue is included in optimizing the objective function value
          but is not part
          of the solution's operating cost. That is, the TotalCost field in the route
          class never includes revenue in its output; however, revenue weights the
          relative importance of servicing orders.SpecialtyNames: A space-separated string
          containing the names of the specialties required by
          the order. A null value indicates that the order doesn't require specialties.The
          spelling of any specialties listed in the Orders and Routes classes must
          match exactly so that the VRP solver can link them together.To illustrate what
          specialties are and how they work, assume a lawn care and
          tree trimming company has a portion of its orders that requires a bucket truck
          to trim tall trees. The company would enter BucketTruck in the SpecialtyNames
          field for these orders to indicate their special need. SpecialtyNames would be
          left as null for the other orders. Similarly, the company would also enter
          BucketTruck in the SpecialtyNames field of routes that are driven by trucks with
          hydraulic booms. It would leave the field null for the other routes. At solve
          time, the VRP solver assigns orders without special needs to any route, but it
          only assigns orders that need bucket trucks to routes that have
          them.AssignmentRule: This field specifies the rule for assigning the order to a
          route. It is
          constrained by a domain of values, which are listed below (their coded values
          are shown in parentheses).

          * Exclude  (0)—The order is to be excluded from the subsequent solve operation.

          * Preserve route and relative sequence  (1)—The solver must always assign the
          order to the preassigned route and at the preassigned relative sequence during
          the solve operation. If this assignment rule can't be followed, it results in an
          order violation. With this setting, only the relative sequence is maintained,
          not the absolute
          sequence. To illustrate what this means, imagine there are two orders: A and B.
          They have sequence values of 2 and 3, respectively. If you set their
          AssignmentRule field values to Preserve route and relative sequence, A's and B's
          actual sequence values may change after solving because other orders, breaks,
          and depot visits could still be sequenced before, between, or after A and B.
          However, B cannot be sequenced before A.

          * Preserve route  (2)—The solver must always assign the order to the preassigned
          route during the solve operation. A valid sequence must also be set even though
          the sequence may or may not be preserved. If the order can't be assigned to the
          specified route, it results in an order violation.

          * Override  (3)—The solver tries to preserve the route and sequence
          preassignment for the order during the solve operation. However, a new route
          and/or sequence for the order may be assigned if it helps minimize the overall
          value of the objective function. This is the default value.
          This field can't contain a null value.CurbApproach:The CurbApproach property
          specifies the direction a vehicle may arrive at and
          depart from the network location. There are four choices (their coded values are
          shown in parentheses):

          * Either side of vehicle  (0)—The vehicle can approach and depart the network
          location in either direction. U-turns are allowed. You should choose this
          setting if your vehicle can make a U-turn at the stop or if it can pull into a
          driveway or parking lot and turn around.

          * Right side of vehicle  (1)—When the vehicle approaches and departs the network
          location, the curb must be on the right side of the vehicle. A U-turn is
          prohibited.

          * Left side of vehicle  (2)—When the vehicle approaches and departs the network
          location, the curb must be on the left side of the vehicle. A U-turn is
          prohibited.

          * No U-Turn  (3)—When the vehicle approaches the network location, the curb can
          be on either side of the vehicle; however, the vehicle must depart without
          turning around.
          RouteName: The name of the route to which the order is assigned.As an input
          field, this field is used to preassign an order to a specific route.
          It can contain a null value, indicating that the order is not preassigned to any
          route, and the solver determines the best possible route assignment for the
          order. If this is set to null, the sequence field must also be set to null.After
          a solve operation, if the order is routed, the RouteName field contains
          the name of the route that the order is assigned to.Sequence: This indicates the
          sequence of the order on its assigned route.As an input field, this field is
          used to specify the relative sequence for an
          order on the route. This field can contain a null value specifying that the
          order can be placed anywhere along the route. A null value can only occur
          together with a null RouteName value.The input sequence values are positive and
          unique for each route (shared across
          renewal depot visits, orders, and breaks), but do not need to start from 1 or be
          contiguous.After a solve operation, the Sequence field contains the sequence
          value of the
          order on its assigned route. Output sequence values for a route are shared
          across depot visits, orders, and breaks; start from 1 (at the starting depot);
          and are consecutive. So the smallest possible output sequence value for a routed
          order is 2, since a route always begins at a depot.
      depots (Feature Set):
          A depot is a location that a vehicle departs from at the beginning of its
          workday and returns to at the end of the workday. Vehicles are loaded (for
          deliveries) or unloaded (for pickups) at depots at the start of the route. In
          some cases, a depot can also act as a renewal location whereby the vehicle can
          unload or reload and continue performing deliveries and pickups. A depot has
          open and close times, as specified by a hard time-window. Vehicles can't arrive
          at a depot outside of this time window.The depots feature set has an associated
          attribute table. The fields in the
          attribute table are listed below and described.ObjectID:The system-managed ID
          field.Shape:The geometry field indicating the geographic location of the network
          analysis
          object.Name:The name of the depot. The StartDepotName and EndDepotName fields of
          the Routes
          record set reference the names you specify here. It is also referenced by the
          Route Renewals record set, when used. Depot names are case insensitive and have
          to be nonempty and unique.TimeWindowStart1:The beginning time of the first time
          window for the network location. This field
          can contain a null value; a null value indicates no beginning time.

          *  Time window fields can contain a time-only value or a date and time value. If
          a
          time field has a time-only value (for example, 8:00 AM), the date is assumed to
          be the date specified by the Default Date parameter of the analysis layer. Using
          date and time values (for example, 7/11/2010 8:00 AM) allows you to set time
          windows that span multiple days.

          * The default date is ignored when any time window field includes a date with
          the
          time. To avoid an error in this situation, format all time windows in Depots,
          Routes, Orders, and Breaks to also include the date with the time.

          *  If you're using traffic data, the time-of-day fields for the network location
          always reference the same time zone as the edge on which the network location is
          located.
          TimeWindowEnd1: The ending time of the first window for the network location.
          This field can
          contain a null value; a null value indicates no ending time.TimeWindowStart2:The
          beginning time of the second time window for the network location. This
          field can contain a null value; a null value indicates that there is no second
          time window.If the first time window is null as specified by the
          TimeWindowStart1 and
          TimeWindowEnd1 fields, the second time window must also be null.If both time
          windows are nonnull, they can't overlap. Also, the second time
          window must occur after the first.TimeWindowEnd2: The ending time of the second
          time window for the network location. This field
          can contain a null value.When TimeWindowStart2 and TimeWindowEnd2 are both null,
          there is no second time
          window.When TimeWindowStart2 is not null but TimeWindowEnd2 is null, there is a
          second
          time window that has a starting time but no ending time. This is
          valid.CurbApproach:The CurbApproach property specifies the direction a vehicle
          may arrive at and
          depart from the network location. There are four choices (their coded values are
          shown in parentheses):

          * Either side of vehicle  (0)—The vehicle can approach and depart the network
          location in either direction. U-turns are allowed. You should choose this
          setting if your vehicle can make a U-turn at the stop or if it can pull into a
          driveway or parking lot and turn around.

          * Right side of vehicle  (1)—When the vehicle approaches and departs the network
          location, the curb must be on the right side of the vehicle. A U-turn is
          prohibited.

          * Left side of vehicle  (2)—When the vehicle approaches and departs the network
          location, the curb must be on the left side of the vehicle. A U-turn is
          prohibited.

          * No U-Turn  (3)—When the vehicle approaches the network location, the curb can
          be on either side of the vehicle; however, the vehicle must depart without
          turning around.
          Bearing:The direction in which a point is moving. The units are degrees and are
          measured
          in a clockwise fashion from true north. This field is used in conjunction with
          the BearingTol field.Bearing data is usually sent automatically from a mobile
          device that is equipped
          with a GPS receiver. Try to include bearing data if you are loading an order
          that is moving, such as a pedestrian or a vehicle.Using this field tends to
          prevent adding locations to the wrong edges, which can
          occur when a vehicle is near an intersection or an overpass, for example.
          Bearing also helps Network Analyst determine which side of the street the point
          is on.For more information, see Bearing and BearingTol.BearingTol:The bearing
          tolerance value creates a range of acceptable bearing values when
          locating moving points on an edge using the Bearing field. If the value from the
          Bearing field is within the range of acceptable values that are generated from
          the bearing tolerance on an edge, the point can be added as a network location
          there; otherwise, the closest point on the next-nearest edge is evaluated.The
          units are in degrees, and the default value is 30. Values must be greater
          than zero and less than 180.A value of 30 means that when Network Analyst
          attempts to add a network location
          on an edge, a range of acceptable bearing values is generated 15º to either side
          of the edge (left and right) and in both digitized directions of the edge.For
          more information, see Bearing and BearingTol.NavLatency:This field is only used
          in the solve process if Bearing and BearingTol also have
          values; however, entering a NavLatency value is optional, even when values are
          present in Bearing and BearingTol. NavLatency indicates how much time is
          expected to elapse from the moment GPS information is sent from a moving vehicle
          to a server and the moment the processed route is received by the vehicle's
          navigation device. The time units of NavLatency are the same as the units of the
          cost attribute specified by the parameter Time Attribute.
      routes (Record Set):
          The routes that are available for the given vehicle routing problem. A route
          specifies vehicle and driver characteristics; after solving, it also represents
          the path between depots and orders.A route can have start and end depot service
          times, a fixed or flexible starting
          time, time-based operating costs, distance-based operating costs, multiple
          capacities, various constraints on a driver's workday, and so on.The routes
          record set has several attributes. The fields in the attribute table
          are listed below and described. Name:The name of the route. The name must be
          unique.Network Analyst generates a unique name at solve time if the field value
          is
          null. Therefore, entering a value is optional in most cases. However, you must
          enter a name if your analysis includes breaks, route renewals, route zones, or
          orders that are preassigned to a route because the route name is used as a
          foreign key in these cases. Note that route names are case insensitive.
          StartDepotName: The name of the starting depot for the route. This field is a
          foreign key to
          the Name field in Depots.If the StartDepotName value is null, the route will
          begin from the first order
          assigned. Omitting the start depot is useful when the vehicle's starting
          location is unknown or irrelevant to your problem. However, when StartDepotName
          is null, EndDepotName cannot also be null.If the route is making deliveries and
          StartDepotName is null, it is assumed the
          cargo is loaded on the vehicle at a virtual depot before the route begins. For a
          route that has no renewal visits, its delivery orders (those with nonzero
          DeliveryQuantities values in the Orders class) are loaded at the start depot or
          virtual depot. For a route that has renewal visits, only the delivery orders
          before the first renewal visit are loaded at the start depot or virtual depot.
          EndDepotName: The name of the ending depot for the route. This field is a
          foreign key to the
          Name field in the Depots class. StartDepotServiceTime: The service time at the
          starting depot. This can be used to model the time
          spent for loading the vehicle. This field can contain a null value; a null value
          indicates zero service time.The unit for this field value is specified by the
          Time Field Units parameter
          (time_units in Python).The service times at the start and end depots are fixed
          values (given by the
          StartDepotServiceTime and EndDepotServiceTime field values) and do not take into
          account the actual load for a route. For example, the time taken to load a
          vehicle at the starting depot may depend on the size of the orders. As such, the
          depot service times could be given values corresponding to a full truckload or
          an average truckload, or you could make your own time estimate.
          EndDepotServiceTime: The service time at the ending depot. This can be used to
          model the time spent
          for unloading the vehicle. This field can contain a null value; a null value
          indicates zero service time.The unit for this field value is specified by the
          Time Field Units parameter
          (time_units in Python).The service times at the start and end depots are fixed
          values (given by the
          StartDepotServiceTime and EndDepotServiceTime field values) and do not take into
          account the actual load for a route. For example, the time taken to load a
          vehicle at the starting depot may depend on the size of the orders. As such, the
          depot service times could be given values corresponding to a full truckload or
          an average truckload, or you could make your own time estimate.
          EarliestStartTime: The earliest allowable starting time for the route. This is
          used by the solver
          in conjunction with the time window of the starting depot for determining
          feasible route start times.This field can't contain null values and has a
          default time-only value of 8:00
          AM; the default value is interpreted as 8:00 a.m. on the date given by the
          Default Date parameter (default_date for Python).The default date is ignored
          when any time window field includes a date with the
          time. To avoid an error in this situation, format all time windows in Depots,
          Routes, Orders, and Breaks to also include the date with the time.When using
          network datasets with traffic data across multiple time zones, the
          time zone for EarliestStartTime is the same as the time zone of the edge or
          junction on which the starting depot is located. LatestStartTime: The latest
          allowable starting time for the route. This field can't contain null
          values and has a default time-only value of 10:00 AM; the default value is
          interpreted as 10:00 a.m. on the date given by the Default Date property of the
          analysis layer.When using network datasets with traffic data across multiple
          time zones, the
          time zone for LatestStartTime is the same as the time zone of the edge or
          junction on which the starting depot is located.ArriveDepartDelayThis field
          stores the amount of travel time needed to accelerate the vehicle to
          normal travel speeds, decelerate it to a stop, and move it off and on the
          network (for example, in and out of parking). By including an ArriveDepartDelay
          value, the VRP solver is deterred from sending many routes to service physically
          coincident orders.The cost for this property is incurred between visits to
          noncoincident orders,
          depots, and route renewals. For example, when a route starts from a depot and
          visits the first order, the total arrive/depart delay is added to the travel
          time. The same is true when traveling from the first order to the second order.
          If the second and third orders are coincident, the ArriveDepartDelay value is
          not added between them since the vehicle doesn't need to move. If the route
          travels to a route renewal, the value is added to the travel time again.Although
          a vehicle needs to slow down and stop for a break and accelerate
          afterwards, the VRP solver cannot add the ArriveDepartDelay value for breaks.
          This means that if a route leaves an order, stops for a break, and continues to
          the next order, the arrive/depart delay is added only once, not twice.To
          illustrate, assume there are five coincident orders in a high-rise building,
          and they are serviced by three different routes. This means three arrive/depart
          delays would be incurred; that is, three drivers would need to separately find
          parking places and enter the same building. However, if the orders could be
          serviced by just one route instead, only one driver would need to park and enter
          the building—only one arrive/depart delay would be incurred. Since the VRP
          solver tries to minimize cost, it will try to limit the arrive/depart delays and
          thus choose the single-route option. (Note that multiple routes may need to be
          sent when other constraints—such as specialties, time windows, or
          capacities—require it.)The unit for this field value is specified by the Time
          Field Units parameter
          (time_units in Python). Capacities: The maximum capacity of the vehicle. You can
          specify capacity in any dimension
          you want, such as weight, volume, or quantity. You can even specify multiple
          dimensions, for example, weight and volume.Enter capacities without indicating
          units. For example, assume your vehicle can
          carry a maximum of 40,000 pounds; you would enter 40000. You need to remember
          for future reference that the value is in pounds.If you are tracking multiple
          dimensions, separate the numeric values with a
          space. For instance, if you are recording both weight and volume and your
          vehicle can carry a maximum weight of 40,000 pounds and a maximum volume of
          2,000 cubic feet, Capacities should be entered as 40000 2000. Again, you need to
          remember the units. You also need to remember the sequence the values and their
          corresponding units are entered in (pounds followed by cubic feet in this
          case).Remembering the units and the unit sequence is important for a couple of
          reasons: one, so you can reinterpret the information later; two, so you can
          properly enter values for the DeliveryQuantities and PickupQuantities fields for
          Orders. To elaborate on the second point, note that the VRP solver
          simultaneously refers to Capacities, DeliveryQuantities, and PickupQuantities to
          make sure that a route doesn't become overloaded. Since units can't be entered
          in the field, Network Analyst can't make unit conversions, so you need to enter
          the values for the three fields using the same units and the same unit sequence
          to ensure the values are correctly interpreted. If you mix units or change the
          sequence in any of the three fields, you will get unwanted results without
          receiving any warning messages. Thus, it is a good idea to set up a unit and
          unit-sequence standard beforehand and continually refer to it whenever entering
          values for these three fields.An empty string or null value is equivalent to all
          values being zero. Capacity
          values can't be negative.If the Capacities string has an insufficient number of
          values in relation to the
          DeliveryQuantities or PickupQuantities fields for orders, the remaining values
          are treated as zero.The VRP solver only performs a simple Boolean test to
          determine whether
          capacities are exceeded. If a route's capacity value is greater than or equal to
          the total quantity being carried, the VRP solver will assume the cargo fits in
          the vehicle. This could be incorrect, depending on the actual shape of the cargo
          and the vehicle. For example, the VRP solver allows you to fit a 1,000-cubic-
          foot sphere into a 1,000-cubic-foot truck that is 8 feet wide. In reality,
          however, since the sphere is 12.6 feet in diameter, it won't fit in the 8-foot
          wide truck. FixedCost: A fixed monetary cost that is incurred only if the route
          is used in a solution
          (that is, it has orders assigned to it). This field can contain null values; a
          null value indicates zero fixed cost. This cost is part of the total route
          operating cost. CostPerUnitTime: The monetary cost incurred—per unit of work
          time—for the total route duration,
          including travel times as well as service times and wait times at orders,
          depots, and breaks. This field can't contain a null value and has a default
          value of 1.0.The unit for this field value is specified by the Time Field Units
          parameter
          (time_units in Python). CostPerUnitDistance: The monetary cost incurred—per unit
          of distance traveled—for the route length
          (total travel distance). This field can contain null values; a null value
          indicates zero cost.The unit for this field value is specified by the Distance
          Field Units parameter
          (distance_units for Python). OvertimeStartTime: The duration of regular work
          time before overtime computation begins. This
          field can contain null values; a null value indicates that overtime does not
          apply.The unit for this field value is specified by the Time Field Units
          parameter
          (time_units in Python).For example, if the driver is to be paid overtime pay
          when the total route
          duration extends beyond eight hours, OvertimeStartTime is specified as 480 (8
          hours * 60 minutes/hour), given the Time Field Units parameter is set to
          Minutes.CostPerUnitOvertime: The monetary cost incurred per time unit of
          overtime work. This field can
          contain null values; a null value indicates that the CostPerUnitOvertime value
          is the same as the CostPerUnitTime value. MaxOrderCount The maximum allowable
          number of orders on the route. This field can't contain
          null values and has a default value of 30. MaxTotalTime The maximum allowable
          route duration. The route duration includes travel times
          as well as service and wait times at orders, depots, and breaks. This field can
          contain null values; a null value indicates that there is no constraint on the
          route duration.The unit for this field value is specified by the Time Field
          Units parameter
          (time_units in Python). MaxTotalTravelTime The maximum allowable travel time for
          the route. The travel time includes only
          the time spent driving on the network and does not include service or wait
          times. This field can contain null values; a null value indicates there is no
          constraint on the maximum allowable travel time. This field value can't be
          larger than the MaxTotalTime field value.The unit for this field value is
          specified by the Time Field Units parameter
          (time_units in Python). MaxTotalDistance The maximum allowable travel distance
          for the route.The unit for this field value is specified by the Distance Field
          Units parameter
          (distance_units for Python).This field can contain null values; a null value
          indicates that there is no
          constraint on the maximum allowable travel distance. SpecialtyNames A space-
          separated string containing the names of the specialties supported by
          the route. A null value indicates that the route does not support any
          specialties.This field is a foreign key to the SpecialtyNames field in the
          orders class.To illustrate what specialties are and how they work, assume a lawn
          care and
          tree trimming company has a portion of its orders that requires a bucket truck
          to trim tall trees. The company would enter BucketTruck in the SpecialtyNames
          field for these orders to indicate their special need. SpecialtyNames would be
          left as null for the other orders. Similarly, the company would also enter
          BucketTruck in the SpecialtyNames field of routes that are driven by trucks with
          hydraulic booms. It would leave the field null for the other routes. At solve
          time, the VRP solver assigns orders without special needs to any route, but it
          only assigns orders that need bucket trucks to routes that have them.
          AssignmentRule This specifies whether or not the route can be used when solving
          the problem.
          This field is constrained by a domain of values, and the possible values are the
          following:

          * Include —The route is included in the solve operation. This is the default
          value.

          * Exclude —The route is excluded from the solve operation.
      breaks (Record Set):
          The rest periods, or breaks, for the routes in a given vehicle routing problem.
          A break is associated with exactly one route, and it can be taken after
          completing an order, while en route to an order, or prior to servicing an order.
          It has a start time and a duration, for which the driver may or may not be paid.
          There are three options for establishing when a break begins: using a time
          window, a maximum travel time, or a maximum work time.The breaks record set has
          associated attributes. The fields in the attribute
          table are listed below and described. ObjectID:The system-managed ID field.
          RouteName: The name of the route that the break applies to. Although a break is
          assigned
          to exactly one route, many breaks can be assigned to the same route.This field
          is a foreign key to the Name field in the Routes class and can't have
          a null value. Precedence:Precedence values sequence the breaks of a given route.
          Breaks with a precedence
          value of 1 occur before those with a value of 2, and so on.All breaks must have
          a precedence value, regardless of whether they are time-
          window, maximum-travel-time, or maximum-work-time breaks. ServiceTime The
          duration of the break. This field can contain null values; a null value
          indicates no service time.The unit for this field value is specified by the Time
          Field Units parameter
          (time_units in Python). TimeWindowStart: The starting time of the break's time
          window.If this field is null and TimeWindowEnd has a valid time-of-day value,
          the break
          is allowed to start anytime before the TimeWindowEnd value.If this field has a
          value, MaxTravelTimeBetweenBreaks and MaxCumulWorkTime must
          be null; moreover, all other breaks in the analysis layer must have null values
          for MaxTravelTimeBetweenBreaks and MaxCumulWorkTime.An error will occur at solve
          time if a route has multiple breaks with
          overlapping time windows.The time window fields in breaks can contain a time-
          only value or a date and
          time value. If a time field, such as TimeWindowStart, has a time-only value (for
          example, 12:00 PM), the date is assumed to be the date specified by the Default
          Date parameter (default_date for Python). Using date and time values (for
          example, 7/11/2012 12:00 PM) allows you to specify time windows that span two or
          more days. This is especially beneficial when a break should be taken sometime
          before and after midnight.The default date is ignored when any time window field
          includes a date with the
          time. To avoid an error in this situation, format all time windows in Depots,
          Routes, Orders, and Breaks to also include the date with the time.When you use
          network datasets with traffic data across multiple time zones, the
          time zone for TimeWindowStart and TimeWindowEnd is assumed to be the same as the
          time zone of the edge or junction on which the starting depot is located.
          TimeWindowEnd: The ending time of the break's time window.If this field is null
          and TimeWindowStart has a valid time-of-day value, the
          break is allowed to start anytime after the TimeWindowStart value.If this field
          has a value, MaxTravelTimeBetweenBreaks and MaxCumulWorkTime must
          be null; moreover, all other breaks in the analysis layer must have null values
          for MaxTravelTimeBetweenBreaks and MaxCumulWorkTime. MaxViolationTime: This
          field specifies the maximum allowable violation time for a time-window
          break. A time window is considered violated if the arrival time falls outside
          the time range.A zero value indicates the time window cannot be violated; that
          is, the time
          window is hard. A nonzero value specifies the maximum amount of lateness; for
          example, the break can begin up to 30 minutes beyond the end of its time window,
          but the lateness is penalized as per the Time Window Violation Importance
          parameter (time_window_factor for Python).This property can be null; a null
          value with TimeWindowStart and TimeWindowEnd
          values indicates that there is no limit on the allowable violation time. If
          MaxTravelTimeBetweenBreaks or MaxCumulWorkTime has a value, MaxViolationTime
          must be null.The unit for this field value is specified by the Time Field Units
          parameter
          (time_units in Python). MaxTravelTimeBetweenBreaks:The maximum amount of travel
          time that can be accumulated before the break is
          taken. The travel time is accumulated either from the end of the previous break
          or, if a break has not yet been taken, from the start of the route.If this is
          the route's final break, MaxTravelTimeBetweenBreaks also indicates
          the maximum travel time that can be accumulated from the final break to the end
          depot.This field is designed to limit how long a person can drive until a break
          is
          required. For instance, if the Time Field Units parameter (time_units for
          Python) of the analysis is set to Minutes, and MaxTravelTimeBetweenBreaks has a
          value of 120, the driver will get a break after  two hours of driving. To assign
          a second break after two more hours of driving, the second break's
          MaxTravelTimeBetweenBreaks property should be 120.If this field has a value,
          TimeWindowStart, TimeWindowEnd, MaxViolationTime, and
          MaxCumulWorkTime must be null for an analysis to solve successfully.The unit for
          this field value is specified by the Time Field Units parameter
          (time_units in Python). MaxCumulWorkTime:The maximum amount of work time that
          can be accumulated before the break is
          taken. Work time is always accumulated from the beginning of the route.Work time
          is the sum of travel time and service times at orders, depots, and
          breaks. Note, however, that this excludes wait time, which is the time a route
          (or driver) spends waiting at an order or depot for a time window to begin.This
          field is designed to limit how long a person can work until a break is
          required. For instance, if the Time Field Units property (time_units for Python)
          is set to Minutes, MaxCumulWorkTime has a value of 120, and ServiceTime has a
          value of 15, the driver will get a 15-minute break after  two hours of
          work.Continuing with the last example, assume a second break is needed after
          three
          more hours of work. To specify this break, you would enter 315 (five hours and
          15 minutes) as the second break's MaxCumulWorkTime value. This number includes
          the MaxCumulWorkTime and ServiceTime values of the preceding break, along with
          the three additional hours of work time before granting the second break. To
          avoid taking maximum-work-time breaks prematurely, remember that they accumulate
          work time from the beginning of the route and that work time includes the
          service time at previously visited depots, orders, and breaks.If this field has
          a value, TimeWindowStart, TimeWindowEnd, MaxViolationTime, and
          MaxTravelTimeBetweenBreaks must be null for an analysis to solve
          successfully.The unit for this field value is specified by the Time Field Units
          parameter
          (time_units in Python). IsPaid: A Boolean value indicating whether the break is
          paid or unpaid. A True value
          indicates that the time spent at the break is included in the route cost
          computation and overtime determination. A False value indicates otherwise. The
          default value is True. Sequence: As an input field, this indicates the sequence
          of the break on its route. This
          field can contain null values. The input sequence values are positive and unique
          for each route (shared across renewal depot visits, orders, and breaks) but need
          not start from 1 or be contiguous.The solver modifies the sequence field. After
          solving, this field contains the
          sequence value of the break on its route. Output sequence values for a route are
          shared across depot visits, orders, and breaks; start from 1 (at the starting
          depot); and are consecutive.
      time_units (String):
          The time units for all time-based field values in the analysis.

          * Seconds

          * Minutes

          * Hours

          * Days
          Many features and records in a VRP analysis have fields for storing time values,
          such as ServiceTime for Orders and CostPerUnitTime for Routes. To minimize data
          entry requirements, these field values don't include units. Instead, all
          distance-based field values must be entered in the same units, and this
          parameter is used to specify the units of those values.Note that output time-
          based fields use the same units specified by this
          parameter.This time unit doesn't need to match the time unit of the network Time
          Attribute
          parameter (time_attribute).
      distance_units (String):
          The distance units for all distance-based field values in the analysis.

          * Miles

          * Kilometers

          * Feet

          * Yards

          * Meters

          * NauticalMiles
          Many features and records in a VRP analysis have fields for storing distance
          values, such as MaxTotalDistance and CostPerUnitDistance for Routes. To minimize
          data entry requirements, these field values don't include units. Instead, all
          distance-based field values must be entered in the same units, and this
          parameter is used to specify the units of those values.Note that output
          distance-based fields use the same units specified by this
          parameter. This distance unit doesn't need to match the distance unit of the
          network
          Distance Attribute (distance attribute).
      network_dataset (Network Dataset Layer):
          The network dataset on which the vehicle routing problem analysis will be
          performed. The network dataset must have a time-based cost attribute since the
          VRP solver minimizes time.
      output_workspace_location (Workspace):
          The enterprise geodatabase, file geodatabase, or in-memory workspace in which
          the output feature classes will be created. This workspace must already exist.
          The default output workspace is in memory.
      output_unassigned_stops_name (String):
          The name of the output feature class that will contain any unreachable depots
          or unassigned orders.
      output_stops_name (String):
          The name of the feature class that will contain the stops visited by routes.
          This feature class includes stops at depots, orders, and breaks.
      output_routes_name (String):
          The name of the feature class that will contain the routes of the analysis.
      output_directions_name (String):
          The name of the feature class that will contain the directions for the routes.
      default_date {Date}:
          The default date for time field values that specify a time of day without
          including a date.
      uturn_policy {String}:
          The U-Turn policy at junctions. Allowing U-turns implies the solver can turn
          around at a junction and double back on the same street.  Given that junctions
          represent street intersections and dead ends, different vehicles may be able to
          turn around at some junctions but not at others—it depends on whether the
          junction represents an intersection or dead end. To accommodate, the U-turn
          policy parameter is implicitly specified by how many edges connect to the
          junction, which is known as junction valency. The acceptable values for this
          parameter are listed below; each is followed by a description of its meaning in
          terms of junction valency.

          * ALLOW_UTURNS—U-turns are permitted at junctions with any number of connected
          edges. This is the default value.

          * NO_UTURNS—U-turns are prohibited at all junctions, regardless of junction
          valency. Note, however, that U-turns are still permitted at network locations
          even when this setting is chosen; however, you can set the individual network
          locations' CurbApproach property to prohibit U-turns there as well.

          * ALLOW_DEAD_ENDS_ONLY—U-turns are prohibited at all junctions, except those
          that have only one adjacent edge (a dead end).

          * ALLOW_DEAD_ENDS_AND_INTERSECTIONS_ONLY—U-turns are prohibited at junctions
          where exactly two adjacent edges meet but are permitted at intersections
          (junctions with three or more adjacent edges) and dead ends (junctions with
          exactly one adjacent edge). Oftentimes, networks have extraneous junctions in
          the middle of road segments. This option prevents vehicles from making U-turns
          at these locations.
          If you need a more precisely defined U-turn policy, consider adding a global
          turn delay evaluator to a network cost attribute, or adjusting its settings if
          one exists, and pay particular attention to the configuration of reverse turns.
          Also, look at setting the CurbApproach property of your network locations.The
          value of this parameter is overridden when Travel Mode (travel_mode in
          Python) is set to any value other than custom.
      time_window_factor {String}:
          Rates the importance of honoring time windows. There are three options, which
          are listed and described below.

          * Low—Places more importance on minimizing drive times and less on arriving at
          stops on time. You may want to use this setting if you have a growing backlog of
          service requests. For the purpose of servicing more orders in a day and reducing
          the backlog, you can choose this setting even though customers might be
          inconvenienced with your late arrivals.

          * Medium—This is the default value. Balances the importance of minimizing drive
          times and arriving within time windows.

          * High—Places more importance on arriving at stops on time than on minimizing
          drive times. Organizations that make time-critical deliveries or that are very
          concerned with customer service would choose this setting.
      spatially_cluster_routes {Boolean}:
          * CLUSTER— Dynamic seed points are created for all routes automatically and the
          orders assigned to an individual route are spatially clustered. Clustering
          orders tends to keep routes in smaller areas and reduce how often different
          route lines intersect one another; yet, clustering also tends to increase
          overall travel times.

          * NO_CLUSTER— Dynamic seed points aren't created. Choose this option if route
          zones are specified.
      route_zones {Feature Set}:
          Delineates work territories for given routes. A route zone is a polygon feature
          and is used to constrain routes to servicing only those orders that fall within
          or near the specified area. Here are some examples of when route zones may be
          useful:

          *  Some of your employees don't have the required permits to perform work in
          certain states or communities. You can create a hard route zone so they only
          visit orders in areas where they meet the requirements.

          * One of your vehicles breaks down frequently so you want to minimize response
          time by having it only visit orders that are close to your maintenance garage.
          You can create a soft or hard route zone to keep the vehicle nearby.
          The route zones feature set has an associated attribute table. The fields in the
          attribute table are listed below and described. ObjectID:The system-managed ID
          field. Shape:The geometry field indicating the geographic location of the
          network analysis
          object. RouteName: The name of the route to which this zone applies. A route
          zone can have a
          maximum of one associated route. This field can't contain null values, and it is
          a foreign key to the Name field in the Routes feature layer. IsHardZone: A
          Boolean value indicating a hard or soft route zone. A True value indicates
          that the route zone is hard; that is, an order that falls outside the route zone
          polygon can't be assigned to the route. The default value is True (1). A False
          value (0) indicates that such orders can still be assigned, but the cost of
          servicing the order is weighted by a function that is based on the Euclidean
          distance from the route zone. Basically, this means that as the straight-line
          distance from the soft zone to the order increases, the likelihood of the order
          being assigned to the route decreases.
      route_renewals {Record Set}:
          Specifies the intermediate depots that routes can visit to reload or unload the
          cargo they are delivering or picking up. Specifically, a route renewal links a
          route to a depot. The relationship indicates the route can renew (reload or
          unload while en route) at the associated depot.Route renewals can be used to
          model scenarios in which a vehicle picks up a full
          load of deliveries at the starting depot, services the orders, returns to the
          depot to renew its load of deliveries, and continues servicing more orders. For
          example, in propane gas delivery, the vehicle may make several deliveries until
          its tank is nearly or completely depleted, visit a refueling point, and make
          more deliveries.Here are a few rules and options to consider when also working
          with route seed
          points:

          * The reload/unload point, or renewal location, can be different from the start
          or end depot.

          * Each route can have one or many predetermined renewal locations.

          * A renewal location may be used more than once by a single route.

          * In some cases where there may be several potential renewal locations for a
          route, the closest available renewal location is chosen by the solver.
          The route renewals record set has associated attributes. The fields in the
          attribute table are listed below and described. ObjectIDThe system-managed ID
          field. DepotName: The name of the depot where this renewal takes place. This
          field can't contain
          a null value and is a foreign key to the Name field in the Depots feature layer.
          RouteName: The name of the route that this renewal applies to. This field can't
          contain a
          null value and is a foreign key to the Name field in the Routes feature layer.
          ServiceTime: The service time for the renewal. This field can contain a null
          value; a null
          value indicates zero service time. The unit for this field value is specified by
          the Time Field Units property of
          the analysis layer.The time taken to load a vehicle at a renewal depot may
          depend on the size of
          the vehicle and how full or empty the vehicle is. However, the service time for
          a route renewal is a fixed value and does not take into account the actual load.
          As such, the renewal service time should be given a value corresponding to a
          full truckload, an average truckload, or another time estimate of your choice.
      order_pairs {Record Set}:
          Pairs pickup and delivery orders so they are serviced by the same route.
          Sometimes it is required that the pickup and delivery for orders be paired. For
          example, a courier company might need to have a route pick up a high-priority
          package from one order and deliver it to another without returning to a depot,
          or sorting station, to minimize delivery time. These related orders can be
          assigned to the same route with the appropriate sequence by using order pairs.
          Moreover, restrictions on how long the package can stay in the vehicle can also
          be assigned; for example, the package might be a blood sample that has to be
          transported from the doctor's office to the lab within two hours.The order pairs
          record set has associated attributes. The fields in the
          attribute table are listed below and described. ObjectID:The system-managed ID
          field. FirstOrderName: The name of the first order of the pair. This field is a
          foreign key to the
          Name field in the Orders feature layer. SecondOrderName: The name of the second
          order of the pair. This field is a foreign key to the
          Name field in the Orders feature layer.The first order in the pair must be a
          pickup order; that is, the value for its
          DeliveryQuantities field is null. The second order in the pair must be a
          delivery order; that is, the value for its PickupQuantities field is null. The
          quantity that is picked up at the first order must agree with the quantity that
          is delivered at the second order. As a special case, both orders may have zero
          quantities for scenarios where capacities are not used.The order quantities are
          not loaded or unloaded at depots. MaxTransitTime: The maximum transit time for
          the pair. The transit time is the duration from
          the departure time of the first order to the arrival time at the second order.
          This constraint limits the time-on-vehicle, or ride time, between the two
          orders. When a vehicle is carrying people or perishable goods, the ride time is
          typically shorter than that of a vehicle carrying packages or nonperishable
          goods. This field can contain null values; a null value indicates that there is
          no constraint on the ride time. The unit for this field value is specified by
          the Time Field Units property of
          the analysis layer.Excess transit time (measured with respect to the direct
          travel time between
          order pairs) can be tracked and weighted by the solver. Because of this, you can
          direct the VRP solver to take one of three approaches: (1) minimize the overall
          excess transit time, regardless of the increase in travel cost for the fleet;
          (2) find a solution that balances overall violation time and travel cost; and
          (3) ignore the overall excess transit time and, instead, minimize the travel
          cost for the fleet. By assigning an importance level for the Excess Transit Time
          Importance parameter (excess_transit_factor for Python), you are in effect
          choosing one of these three approaches. Regardless of the importance level, the
          solver will always return an error if the MaxTransitTime value is surpassed.
      excess_transit_factor {String}:
          Rates the importance of reducing excess transit time of order pairs. Excess
          transit time is the amount of time exceeding the time required to travel
          directly between the paired orders. Excess time can be caused by driver breaks
          or travel to intermediate orders and depots.  Listed below are the three values
          you can choose from.

          * Low—The solver tries to find a solution that minimizes overall solution cost,
          regardless of excess transit time. This setting is commonly used with courier
          services. Since couriers transport packages as opposed to people, they don't
          need to worry about ride time. Using this setting allows the couriers to service
          paired orders in the proper sequence and minimize the overall solution cost.

          * Medium—This is the default setting. The solver looks for a balance between
          reducing excess transit time and reducing the overall solution cost.

          * High—The solver tries to find a solution with the least excess transit time
          between paired orders at the expense of increasing the overall travel costs. It
          makes sense to use this setting if you are transporting people between paired
          orders and you want to shorten their ride time. This is characteristic of taxi
          services.
      point_barriers {Feature Set}:
          Specifies point barriers, which are split into two types: restriction and added
          cost point barriers. They temporarily restrict traversal across or add impedance
          to points on the network. The point barriers are defined by a feature set, and
          the attribute values you specify for the point features determine whether they
          are restriction or added cost barriers. The fields in the attribute table are
          listed and described below. ObjectID:The system-managed ID field. Shape:The
          geometry field indicating the geographic location of the network analysis
          object.Name:The name of the barrier.BarrierType: Specifies whether the barrier
          restricts travel completely or adds cost when
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through the barrier. This is the default
          value.

          * Added Cost  (2)—Traversing through the barrier increases the network cost by
          the amount specified in the Additional_Time and Additional_Distance fields.
          Additional_Time:If BarrierType is set to added cost, the value of the
          Additional_Time field
          indicates how much time is added to a route when the route passes through the
          barrier. The unit for this field value is specified by the Time Field Units
          property of
          the analysis layer.Additional_Distance:If BarrierType is set to added cost, the
          value of the Additional_Distance field
          indicates how much impedance is added to a route when the route passes through
          the barrier.The unit for this field value is specified by the Distance Field
          Units
          parameter.
      line_barriers {Feature Set}:
          Specifies line barriers, which temporarily restrict traversal across them. The
          line barriers are defined by a feature set. The fields in the attribute table
          are listed and described below. ObjectID:The system-managed ID field.Shape:The
          geometry field indicating the geographic location of the network analysis
          object. Name:The name of the barrier.
      polygon_barriers {Feature Set}:
          Specifies polygon barriers, which are split into two types: restriction and
          scaled cost polygon barriers. They temporarily restrict traversal or scale
          impedance on the parts of the network they cover. The polygon barriers are
          defined by a feature set, and the attribute values you specify for the polygon
          features determine whether they are restriction or scaled cost barriers. The
          fields in the attribute table are listed and described below. ObjectID:The
          system-managed ID field. Shape:The geometry field indicating the geographic
          location of the network analysis
          object. Name:The name of the barrier. BarrierType: Specifies whether the barrier
          restricts travel completely or scales the cost of
          traveling through it. There are two options:

          * Restriction  (0)—Prohibits traversing through any part of the barrier. This is
          the default value.

          * Scaled Cost  (1)—Scales the impedance of underlying edges by multiplying them
          by the value of the Attr_[Impedance] property. If edges are partially covered by
          the barrier, the impedance is apportioned and multiplied.
          Scaled_Time:The time-based impedance values of the edges underlying the barrier
          are
          multiplied by the value set in this field. This field is only relevant when the
          barrier is a scaled cost barrier.Scaled_Distance:The distance-based impedance
          values of the edges underlying the barrier are
          multiplied by the value set in this field. This field is only relevant when the
          barrier is a scaled cost barrier.
      time_attribute {String}:
          Defines the network cost attribute to use when determining the travel time of
          network elements.The value of this parameter is overridden when Travel Mode
          (travel_mode in
          Python) is set to any value other than custom.
      distance_attribute {String}:
          Defines the network cost attribute to use when determining the distance of
          network elements.The value of this parameter is overridden when Travel Mode
          (travel_mode in
          Python) is set to any value other than custom.
      use_hierarchy_in_analysis {Boolean}:
          * USE_HIERARCHY— Use the hierarchy attribute for the analysis. Using a hierarchy
          results in the solver preferring higher-order edges to lower-order edges.
          Hierarchical solves are faster, and they can be used to simulate the preference
          of a driver who chooses to travel on freeways over local roads when
          possible—even if that means a longer trip. This option is valid only if the
          input network dataset has a hierarchy attribute.

          * NO_HIERARCHY—Do not use the hierarchy attribute for the analysis. Not using a
          hierarchy yields an exact route for the network dataset.
          The parameter is not used if a hierarchy attribute is not defined on the network
          dataset used to perform the analysis. In such cases, use "#" as the parameter
          value.The value of this parameter is overridden when Travel Mode (travel_mode in
          Python) is set to any value other than custom.
      restrictions {String}:
          Indicates which network restriction attributes are respected during solve
          time.The value of this parameter is overridden when Travel Mode (travel_mode in
          Python) is set to any value other than custom.
      attribute_parameter_values {Record Set}:
          Specifies the parameter values for network attributes that have parameters. The
          record set has two columns that work together to uniquely identify parameters
          and another column that specifies the parameter value.The value of this
          parameter is overridden when Travel Mode (travel_mode in
          Python) is set to any value other than custom.The attribute parameter values
          record set has associated attributes. The fields
          in the attribute table are listed below and described. ObjectID:The system-
          managed ID field.AttributeName:The name of the network attribute whose attribute
          parameter is set by the table
          row.ParameterName:The name of the attribute parameter whose value is set by the
          table row. (Object
          type parameters cannot be updated using this tool.)ParameterValue:The value you
          want for the attribute parameter. If a value is not specified, the
          attribute parameter is set to null.
      maximum_snap_tolerance {Linear unit}:
          The maximum snap tolerance is the furthest distance that Network Analyst
          searches when locating or relocating a point onto the network. The search looks
          for suitable edges or junctions and snaps the point to the nearest one. If a
          suitable location isn't found within the maximum snap tolerance, the object is
          marked as unlocated.
      exclude_restricted_portions_of_the_network {Boolean}:
          * EXCLUDE—Specifies that the network locations are only placed on traversable
          portions of the network. This prevents placing network locations on elements
          that you can't reach due to restrictions or barriers. Before adding your network
          locations using this option, make sure that you have already added all the
          restriction barriers to the input network analysis layer to get expected
          results. This parameter is not applicable when adding barrier objects. In such
          cases, use "#" as the parameter value.

          * INCLUDE—Specifies that the network locations are placed on all the elements of
          the network. The network locations that are added with this option may be
          unreachable during the solve process if they are placed on restricted elements.
      feature_locator_where_clause {Value Table}:
          An SQL expression used to select a subset of source features that limits which
          network elements orders and depots can be located on. For example, to ensure
          orders and depots are not located on limited-access highways, write an SQL
          expression that excludes those source features. (Note that the other network
          analysis objects, such as barriers, ignore the feature locator WHERE clause when
          loading.)For more information on SQL syntax and how it differs between data
          sources, see
          SQL reference for query expressions used in ArcGIS.
      populate_route_lines {Boolean}:
          * NO_ROUTE_LINES—No shape is generated for the output routes. You won't be able
          to generate driving directions if route lines aren't created.

          * ROUTE_LINES—The output routes will have the exact shape of the underlying
          network sources.
      route_line_simplification_tolerance {Linear unit}:
          Specify by how much you want to simplify the route geometry.Simplification
          maintains critical points on a route, such as turns at
          intersections, to define the essential shape of the route and removes other
          points. The simplification distance you specify is the maximum allowable offset
          that the simplified line can deviate from from the original line. Simplifying a
          line reduces the number of vertices and tends to reduce drawing times.The value
          of this parameter is overridden when Travel Mode (travel_mode in
          Python) is set to any value other than custom.
      populate_directions {Boolean}:
          * DIRECTIONS—The feature class specified in the Output Directions Name parameter
          is populated with turn-by-turn instructions for each route. The network dataset
          must support driving directions; otherwise, an error occurs when solving with
          directions.

          * NO_DIRECTIONS—Directions aren't generated.
      directions_language {String}:
          Choose a language to generate driving directions in. The languages that are
          available in the drop-down list depend on what ArcGIS language packs are
          installed on your computer.Note that if you are going to publish this tool as
          part of a service on a
          separate server, the ArcGIS language pack that corresponds with the language you
          choose must be installed on that server for the tool to function properly. Also,
          if a language pack isn't installed on your computer, the language won't appear
          in the drop-down list; however, you can type a language code instead.
      directions_style_name {String}:
          The name of the formatting style of directions.
      save_output_layer {Boolean}:
          * NO_SAVE_OUTPUT_LAYER—A network analysis layer isn't included in the output.

          * SAVE_OUTPUT_LAYER—The output includes a network analysis layer of the results.
          In either case, stand-alone tables and feature classes are returned. However, a
          server administrator may want to choose to output a network analysis layer as
          well so that the setup and results of the tool can be debugged using the Network
          Analyst controls in the ArcGIS for Desktop environment. This can make the
          debugging process much easier.In ArcGIS for Desktop, the default output location
          for the network analysis
          layer is in the scratch workspace, at the same level as the scratch geodatabase.
          That is, it is stored as a sibling of the scratch geodatabase. The output
          network analysis layer is stored as an LYR file whose name starts with _ags_gpna
          and is followed by an alphanumeric GUID.
      service_capabilities {Value Table}:
          This property helps you govern the maximum amount of computer processing that
          occurs when running this tool as a geoprocessing service. You might want to do
          this for one of two reasons: one, to avoid letting your server solve problems
          that require more resources or processing time than you want to allow; two, to
          create multiple services with different VRP capabilities to support a business
          model. For example, if you have a tiered-service business model, you might want
          to provide a free VRP service that supports a maximum of five routes per solve
          and another service that is fee-based and supports more than five routes per
          solve.Along with limiting the maximum number of routes, you can limit how many
          orders
          or point barriers can be added to the analysis. Another way to govern problem
          sizes is by setting a maximum number of features—usually street features—that
          line or polygon barriers can intersect. The last method is to force a
          hierarchical solve, even if the user chooses not to use a hierarchy, when orders
          are geographically dispersed beyond a given straight-line distance.

          * MAXIMUM POINT BARRIERS—The maximum number of point barriers allowed. An error
          is returned if this limit is exceeded. A null value indicates there is no limit.

          * MAXIMUM FEATURES INTERSECTING LINE BARRIERS—The maximum number of source
          features that can be intersected by all line barriers in the analysis. An error
          is returned if this limit is exceeded. A null value indicates there is no limit.

          * MAXIMUM FEATURES INTERSECTING POLYGON BARRIERS—The maximum number of source
          features that can be intersected by all polygon barriers in the analysis. An
          error is returned if this limit is exceeded. A null value indicates there is no
          limit.

          * MAXIMUM ORDERS—The maximum number of orders allowed in the analysis. An error
          is returned if this limit is exceeded. A null value indicates there is no limit.

          * MAXIMUM ROUTES—The maximum number of routes allowed in the analysis. An error
          is returned if this limit is exceeded. A null value indicates there is no limit.

          * FORCE HIERARCHY BEYOND DISTANCE—The maximum straight-line distance between
          orders before the vehicle routing problem is solved using the network's
          hierarchy. The units for this value are the same as those specified in the
          Distance Field Units parameter.If the network doesn't have a hierarchy
          attribute, this constraint is ignored. If Use Hierarchy in Analysis is checked,
          hierarchy is always used. If the Use Hierarchy in Analysis parameter is
          unchecked and this constraint has a null value, hierarchy is not forced.
      ignore_invalid_order_locations {Boolean}:
          * HALT— The solve operation fails when any invalid orders are encountered. An
          invalid order is an order that the VRP solver can't reach. An order may be
          unreachable for a variety of reasons, including the following: it is located on
          a prohibited network element; it isn't located on the network at all; and it is
          located on a disconnected portion of the network. This is the default value.

          * SKIP— The solve operation skips any invalid orders and returns a solution,
          given it didn't encounter any other errors.If you need to generate routes and
          deliver them to drivers immediately, you may be able to skip invalid orders,
          solve, and distribute the routes to your drivers. Next, resolve any invalid
          orders from the last solve, and then include them in the VRP analysis for the
          next workday or work shift.
      travel_mode {String}:
          Choose the mode of transportation for the analysis. CUSTOM is always a choice.
          For other travel mode names to appear, they must be present in the network
          dataset specified in the Network_Dataset parameter. (The arcpy.na.GetTravelModes
          function provides a dictionary of the travel mode objects configured on a
          network dataset, and the name property returns the name of a travel mode
          object.) A travel mode is defined on a network dataset and provides override
          values for
          parameters that, together, model car, truck, pedestrian, or other modes of
          travel. By choosing a travel mode here, you don't need to provide values for the
          following parameters, which are overridden by values specified in the network
          dataset:

          * uturn_policy

          * time_attribute

          * distance_attribute

          * use_hierarchy_in_analysis

          * restrictions

          * attribute_parameter_values

          * route_line_simplification_tolerance

          * CUSTOM—Define a travel mode that fits your specific needs. When CUSTOM is
          chosen, the tool does not override the travel mode parameters listed above. This
          is the default value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SolveVehicleRoutingProblem_na(*gp_fixargs((orders, depots, routes, breaks, time_units, distance_units, network_dataset, output_workspace_location, output_unassigned_stops_name, output_stops_name, output_routes_name, output_directions_name, default_date, uturn_policy, time_window_factor, spatially_cluster_routes, route_zones, route_renewals, order_pairs, excess_transit_factor, point_barriers, line_barriers, polygon_barriers, time_attribute, distance_attribute, use_hierarchy_in_analysis, restrictions, attribute_parameter_values, maximum_snap_tolerance, exclude_restricted_portions_of_the_network, feature_locator_where_clause, populate_route_lines, route_line_simplification_tolerance, populate_directions, directions_language, directions_style_name, save_output_layer, service_capabilities, ignore_invalid_order_locations, travel_mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateTrafficData_na', None)
def UpdateTrafficData(provider=None, user_name=None, password=None, regions=None, traffic_data_output_folder=None, expected_update_interval=None, prediction_cutoff=None, compress_data=None, maximum_file_age=None, speed_unit=None):
    """UpdateTrafficData_na(provider, user_name, password, regions;regions..., traffic_data_output_folder, expected_update_interval, prediction_cutoff, compress_data, {maximum_file_age}, {speed_unit})

        Downloads live traffic data from a web service and stores it in a dynamic
        traffic format (DTF) file, which is a file that network datasets can read for
        live-traffic analysis and display.

     INPUTS:
      provider (String):
          Choose the name of your traffic data provider and the region.

          * NAVTEQ North America

          * NAVTEQ Europe

          * NAVTEQ South America

          * NAVTEQ Oceania

          * NAVTEQ Middle East & Africa

          * NAVTEQ India

          * NAVTEQ South East Asia

          * TomTom North America

          * TomTom Europe

          * INRIX

          * INRIX California
      user_name (String):
          The user name authorized by the data provider to download traffic data. The
          tool fails to execute if the user name cannot be authenticated by the data
          provider.If the Provider parameter is TomTom North America or TomTom Europe, use
          "APIKEY"
          as the parameter value.
      password (Encrypted String):
          The password provided by the data provider to download traffic data. The tool
          fails to execute if the password cannot be authenticated by the data provider.
      regions (String):
          Enter the regions for which you want to download traffic data. To download all
          available regions, enter "#".
      traffic_data_output_folder (Folder):
          The folder in which the DTF file will be created. If the folder is empty, the
          tool creates a TrafficIndex.xml file along with the DTF file. For subsequent
          tool runs, the tool updates TrafficIndex.xml and creates a DTF file.If you
          download data from multiple data providers, a unique folder should be
          specified for each data provider.
      expected_update_interval (Long):
          The time interval in minutes after which the downloaded traffic data is no
          longer up-to-date, and the data provider makes available refreshed  data. After
          this interval has elapsed, it is recommended that you rerun the tool and
          download the latest data.
      prediction_cutoff (Long):
          The time interval (in minutes) for which the predictive traffic data is
          processed by the tool. Data providers may supply predictive data for the next 24
          hours, week, or other time period. The time-span value for this parameter is
          used to limit the amount of predictive traffic data that is processed by the
          tool to speed up tool execution. For example, if your traffic provider has a
          prediction depth of 24 hours, but you need only one hour of prediction depth,
          you can save time by specifying 60 here.
      compress_data (Boolean):
          * COMPRESS—Downloads the TrafficIndex.xml and DTF files, then creates copies of
          the DTF files in a zipped folder. Use this option if network datasets will
          connect to the live traffic data via a geoprocessing service; transferring the
          zipped folder of DTF files to clients is quicker than transferring the DTF files
          themselves.

          * NO_COMPRESS—Downloads the TrafficIndex.xml and DTF files without creating
          copies of them in a zipped folder. Use this option if network datasets will
          connect to the live traffic data via a folder connection. This is the default
          value.
      maximum_file_age {Long}:
          The time interval (in minutes) for which the traffic files (that is, the DTF
          files) will be kept in the traffic data output folder. This parameter
          facilitates deleting traffic files that are no longer required. When the tool is
          rerun, any traffic data files that are older than the maximum file age are
          deleted automatically. The default value is 720 minutes (12 hours).
      speed_unit {String}:
          The speed units when downloading data from a custom traffic feed. This parameter
          is ignored if you are using one of the standard commercial feeds that are
          documented in the Provider parameter.

          * MPH—Miles per hour. This is the default value.

          * KPH—Kilometers per hour.
          Specifying the proper speed units of a custom traffic feed ensures the network
          dataset will interpret the speed values correctly."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateTrafficData_na(*gp_fixargs((provider, user_name, password, regions, traffic_data_output_folder, expected_update_interval, prediction_cutoff, compress_data, maximum_file_age, speed_unit), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateTrafficIncidents_na', None)
def UpdateTrafficIncidents(provider=None, user_name=None, password=None, regions=None, incidents_feature_class_location=None, incidents_feature_class_name=None, time_zone_boundaries=None, time_zone_id_field=None):
    """UpdateTrafficIncidents_na(provider, user_name, password, regions;regions..., incidents_feature_class_location, incidents_feature_class_name, {time_zone_boundaries}, {time_zone_id_field})

        Creates a point feature class containing live traffic-incident data from a web
        service. Traffic incidents include events such as accidents and road
        construction.

     INPUTS:
      provider (String):
          Choose the name of your traffic-incident data provider and the region.

          * NAVTEQ North America

          * NAVTEQ Europe

          * NAVTEQ South America

          * NAVTEQ Oceania

          * NAVTEQ Middle East & Africa

          * TomTom North America

          * TomTom Europe
      user_name (String):
          The user name authorized by the data provider to download incidents. The tool
          fails to execute if the user name cannot be authenticated by the data
          provider.If the Provider parameter is TomTom North America or TomTom Europe, use
          APIKEY
          as the parameter value.
      password (Encrypted String):
          The password provided by the data provider to download traffic-incident data.
          The tool fails to execute if the password cannot be authenticated by the data
          provider.
      regions (String):
          Enter the regions for which you want to download traffic-incident data. To
          download all available regions, type "#".
      incidents_feature_class_location (Workspace / Feature Dataset):
          The geodatabase in which the output feature class will be created. This
          workspace must already exist.
      incidents_feature_class_name (String):
          The name of the feature class to be created. If the tool has been run before
          and the feature class already exists, the tool will delete existing features and
          create new ones based on the most recent incident data.
      time_zone_boundaries {Feature Layer}:
          The polygon feature class whose features delineate time zones. By providing this
          feature class, incidents occurring within time zone boundaries can be reported
          in local time, not only Coordinated Universal Time.If you don't provide a time
          zone boundaries feature class, incident start and
          end times can be reported in Coordinated Universal Time (UTC) only; all local
          time fields are assigned null values. Occasionally, certain incidents from
          traffic feeds such as weather events have null geometries. In this situation,
          the local time fields are assigned null values even if the time zone boundaries
          feature class is provided.Setting the Time Zone ID Field property is required if
          you provide a time-zone-
          boundaries feature class.
      time_zone_id_field {Field}:
          The text field, from the time-zone-boundaries feature class, that contains
          Windows time zone identifiers.The values in this field correspond to time zone
          keys in the Windows registry.
          You can follow similar steps to those outlined in the topic Adding time zones to
          a network dataset to find proper time zone names for the polygons in your input
          feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateTrafficIncidents_na(*gp_fixargs((provider, user_name, password, regions, incidents_feature_class_location, incidents_feature_class_name, time_zone_boundaries, time_zone_id_field), True)))
        return retval
    except Exception, e:
        raise e


# Turn Feature Class toolset
@gptooldoc('CreateTurnFeatureClass_na', None)
def CreateTurnFeatureClass(out_location=None, out_feature_class_name=None, maximum_edges=None, in_network_dataset=None, in_template_feature_class=None, spatial_reference=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None, has_z=None):
    """CreateTurnFeatureClass_na(out_location, out_feature_class_name, {maximum_edges}, {in_network_dataset}, {in_template_feature_class}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3}, {has_z})

        Creates a new turn feature class to store turn features that model turning
        movements in a network dataset.

     INPUTS:
      out_location (Workspace / Feature Dataset):
          The file, personal, workgroup, or enterprise geodatabase, or the folder in which
          the output turn feature class will be created. This workspace must already
          exist.
      out_feature_class_name (String):
          The name of the turn feature class to be created.
      maximum_edges {Long}:
          The maximum number of edges that turns in the new turn feature class can model.
          The default value is 5. The maximum value is 50.
      in_network_dataset {Network Dataset Layer}:
          The network dataset in which the turn feature class will participate. The
          resulting turn feature class will be added as a turn source to the network
          dataset. If no network dataset is specified, the turn feature class will be
          created as not participating in a network dataset.
      in_template_feature_class {Feature Layer}:
          The feature class used as a template to define the attribute schema of the new
          turn feature class.If the template feature class has the following fields, they
          are not created on
          the output turn feature class; NODE_, NODE#, JUNCTION, F_EDGE, T_EDGE, F-EDGE,
          T-EDGE, ARC1_, ARC2_, ARC1#, ARC2#, ARC1-ID, ARC2-ID, AZIMUTH, ANGLE.
      spatial_reference {Spatial Reference}:
          The spatial reference to be applied to the output turn feature class. This
          parameter is ignored if the output location is a geodatabase feature dataset as
          the output turn feature class will inherit the spatial reference of the feature
          dataset.If you want to import the spatial reference from an existing feature
          class,
          specify its path as the parameter value.
      config_keyword {String}:
          Specifies the configuration keyword that determines the storage parameters of
          the new turn feature class. This parameter is used only if the output location
          is an workgroup or enterprise geodatabase
      spatial_grid_1 {Double}:
          The Spatial Grid 1, 2, and 3 parameters are used to compute a spatial index and
          only apply to  file geodatabases and certain workgroup and enterprise
          geodatabase feature classes. If you are unfamiliar with setting grid sizes,
          leave these options as 0,0,0 and ArcGIS will compute optimal sizes for you.
          Since no features are written by this tool, the spatial index will be in an
          unbuilt state. The index will be built when features are written to the feature
          class such as by the Append tool or editing operations. For more information
          about this parameter, refer to the Add Spatial Index tool documentation.
      spatial_grid_2 {Double}:
          Cell size of the second spatial grid. Leave the size at 0 if you only want one
          grid. Otherwise, set the size to at least three times larger than Spatial Grid
          1.
      spatial_grid_3 {Double}:
          Cell size of the third spatial grid. Leave the size at 0 if you only want two
          grids. Otherwise, set the size to at least three times larger than Spatial Grid
          2.
      has_z {Boolean}:
          * ENABLED—The coordinates in the new turn feature class will have elevation (Z)
          values. This value should be used if the input network dataset is specified and
          it supports connectivity based on z coordinate values of the network sources.

          * DISABLED—The coordinates in the new turn feature class will not have elevation
          (Z) values."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateTurnFeatureClass_na(*gp_fixargs((out_location, out_feature_class_name, maximum_edges, in_network_dataset, in_template_feature_class, spatial_reference, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3, has_z), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IncreaseMaximumEdges_na', None)
def IncreaseMaximumEdges(in_turn_features=None, maximum_edges=None):
    """IncreaseMaximumEdges_na(in_turn_features, maximum_edges)

        Increases the maximum number of edges per turn in a turn feature class.

     INPUTS:
      in_turn_features (Feature Layer):
          The turn feature class that is having its maximum number of edges raised.
      maximum_edges (Long):
          The new maximum number of edges in the input turn feature class. The value must
          be at least one higher than the existing maximum number of edges and cannot be
          greater than 50."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IncreaseMaximumEdges_na(*gp_fixargs((in_turn_features, maximum_edges), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PopulateAlternateIDFields_na', None)
def PopulateAlternateIDFields(in_network_dataset=None, alternate_ID_field_name=None):
    """PopulateAlternateIDFields_na(in_network_dataset, alternate_ID_field_name)

        Creates and populates additional fields on the turn feature classes that
        reference the edges by alternate IDs. The alternate IDs allow for another set of
        IDs that can help maintain the integrity of the turn features in case the source
        edges are being edited.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset whose turn feature classes are to receive alternate ID
          fields. The fields will be created on all of the turn feature classes added as a
          turn source to the network dataset.
      alternate_ID_field_name (String):
          The name of the alternate ID field on the edge feature sources of the network
          dataset. All edge feature sources referenced by turns must have the same name
          for the alternate ID field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PopulateAlternateIDFields_na(*gp_fixargs((in_network_dataset, alternate_ID_field_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TurnTableToTurnFeatureClass_na', None)
def TurnTableToTurnFeatureClass(in_turn_table=None, reference_line_features=None, out_feature_class_name=None, reference_nodes_table=None, maximum_edges=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None):
    """TurnTableToTurnFeatureClass_na(in_turn_table, reference_line_features, out_feature_class_name, {reference_nodes_table}, {maximum_edges}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Converts an ArcView turn table or ArcInfo Workstation coverage turn table to an
        ArcGIS turn feature class.

     INPUTS:
      in_turn_table (Table View):
          The .dbf or INFO turn table from which the new turn feature class is being
          created.INFO tables do not support mixed case path names on Linux and Solaris.
      reference_line_features (Feature Class):
          The line feature class to which the input turn table refers. The feature class
          must be a source in a network dataset.
      out_feature_class_name (String):
          The name of the new turn feature class to create.
      reference_nodes_table {dBASE Table}:
          The nodes.dbf table in the .nws folder containing the original ArcView GIS
          network in which the input turn table participated.This parameter is ignored if
          the input turn table is an INFO table.If the input turn table is a .dbf table
          and this parameter is omitted, then
          U-turns and turns that traverse between edges connected to each other at both
          ends will not be created in the output turn feature class.Errors will be
          reported in an error file written to the directory defined by the
          TEMP system variable. The full path name to the error file is reported as a
          warning message.
      maximum_edges {Long}:
          The maximum number of edges per turn in the new turn feature class. The default
          value is 5. The maximum value is 50.
      config_keyword {String}:
          Specifies the configuration keyword that determines the storage parameters of
          the output turn feature class. This parameter is used only if the output turn
          feature class is created in a workgroup or enterprise geodatabase.
      spatial_grid_1 {Double}:
          The Spatial Grid 1, 2, and 3 parameters apply only to file geodatabases and
          certain workgroup and enterprise geodatabase feature classes. If you are
          unfamiliar with setting grid sizes, leave these options as 0,0,0 and ArcGIS will
          compute optimal sizes for you. For more information about this parameter, refer
          to the Add Spatial Index tool documentation.
      spatial_grid_2 {Double}:
          Cell size of the second spatial grid. Leave the size at 0 if you only want one
          grid. Otherwise, set the size to at least three times larger than Spatial Grid
          1.
      spatial_grid_3 {Double}:
          Cell size of the third spatial grid. Leave the size at 0 if you only want two
          grids. Otherwise, set the size to at least three times larger than Spatial Grid
          2."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TurnTableToTurnFeatureClass_na(*gp_fixargs((in_turn_table, reference_line_features, out_feature_class_name, reference_nodes_table, maximum_edges, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateByAlternateIDFields_na', None)
def UpdateByAlternateIDFields(in_network_dataset=None, alternate_ID_field_name=None):
    """UpdateByAlternateIDFields_na(in_network_dataset, alternate_ID_field_name)

        Updates all the edge references in turn feature classes using an alternate ID
        field. This tool should be used after making edits to the input line features
        that are referenced by the turn features to synchronize the turn features based
        on the alternate ID fields.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset whose turn feature classes are being updated by their
          alternate ID fields.
      alternate_ID_field_name (String):
          The name of the alternate ID field on the edge feature sources of the network
          dataset. All edge feature sources referenced by turns must have the same name
          for the alternate ID field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateByAlternateIDFields_na(*gp_fixargs((in_network_dataset, alternate_ID_field_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateByGeometry_na', None)
def UpdateByGeometry(in_turn_features=None):
    """UpdateByGeometry_na(in_turn_features)

        Updates all the edge references in the turn feature class using the geometry of
        the turn features. This tool is useful when the IDs listed for the turn can no
        longer find the edges participating in the turn due to edits to the underlying
        edges.

     INPUTS:
      in_turn_features (Feature Layer):
          The turn feature class to be updated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateByGeometry_na(*gp_fixargs((in_turn_features,), True)))
        return retval
    except Exception, e:
        raise e



@gptooldoc('UpgradeNetwork_na', None)
def UpgradeNetwork(in_network_dataset=None):
    """UpgradeNetwork_na(in_network_dataset)

        Upgrades the schema of the network dataset. Upgrading the network dataset allows
        the network dataset to make use of the new functionality available in the
        current software release.

        This tool has been deprecated. Use Upgrade Dataset tool in the
         Geodatabase Administration toolset instead.

     INPUTS:
      in_network_dataset (Network Dataset Layer):
          The network dataset to be upgraded. The network dataset must be a geodatabase-
          based network dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeNetwork_na(*gp_fixargs((in_network_dataset,), True)))
        return retval
    except Exception as e:
        raise e

# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject