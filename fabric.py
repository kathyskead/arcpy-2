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
"""The Parcel Fabric toolbox contains tools that work with the internal feature
classes and tables of a parcel fabric. Using the Parcel Fabric toolbox, you can
migrate data to a parcel fabric, upgrade an existing parcel fabric, copy and
append parcel fabrics and create layer and table views on the parcel fabric."""
__all__ = ['MakeParcelFabricLayer', 'MakeParcelFabricTableView', 'LoadTopologyToParcelFabric', 'AppendParcelFabric', 'CopyParcelFabric']

# Deprecated tools
__all__ += ['UpgradeParcelFabric']

__alias__ = u'fabric'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Data Migration toolset
@gptooldoc('LoadTopologyToParcelFabric_fabric', None)
def LoadTopologyToParcelFabric(target_parcel_fabric=None, in_topology_class=None, in_point_class=None, linestring_minimum_segments=None, control_match_tolerance=None, unjoined_group=None, direction_units=None, direction_type=None, compute_area=None, area_units=None, radial_point_tolerance=None, accuracy_units=None):
    """LoadTopologyToParcelFabric_fabric(target_parcel_fabric, in_topology_class, {in_point_class}, {linestring_minimum_segments}, {control_match_tolerance}, unjoined_group, {direction_units}, {direction_type}, compute_area, {area_units}, {radial_point_tolerance}, {accuracy_units})

        Loads polygon and line features that participate in a topology into a target
        parcel fabric. The topology requires a predefined set of topology rules:

        * Line—Must be Covered by Boundary Of (polygon)


        * Line—Must Not Self-Overlap


        * Line—Must Not Self-Intersect


        * Line—Must be Single Part


        * Line—Must Not Intersect Or Touch Interior


        * Polygon—Boundary Must be Covered By (Line)

     INPUTS:
      target_parcel_fabric (Parcel Fabric Layer):
          The target parcel fabric where the data will be migrated.
      in_topology_class (Feature Layer):
          Input feature class or layer that is part of a topology. The feature class can
          either be a line or polygon.
      in_point_class {Feature Layer}:
          Input point feature class or layer. The point feature class does not need to be
          part of a topology. Only user-defined attributes on the input point feature
          class will be migrated to corresponding points in the parcel fabric.
      linestring_minimum_segments {Long}:
          The minimum number of segments a polyline feature can have before it is
          considered and migrated as a line string or natural boundary in the parcel
          fabric. The default is a minimum of 10 segments.
      control_match_tolerance {Linear unit}:
          The tolerance in which new, migrated fabric points are linked with existing
          control points found in the fabric. The tolerance length units are the same as
          the length units of the coordinate system of the fabric. If a control match
          tolerance is not specified, the default of 0.1 meters is used.
      unjoined_group (Boolean):
          Determines how features will be migrated.

          * UNJOINED_GROUP—Features will be migrated as unjoined, stand-alone parcels to
          the parcel fabric.

          * JOINED_GROUP—Features will be migrated as joined parcels to the parcel fabric
      direction_units {String}:
          The direction units to be used when generating COGO bearing attributes for line
          features during the migration process.

          * DEGREES_MINUTES_SECONDS—One degree equals 1/360 of a circle. Fractions of a
          degree are represented in minutes and seconds, where one minute equals 1/60 of a
          degree and one second equals 1/60 of a minute. Degrees Minutes and Seconds are
          stored as strings and interpreted accordingly. This is the default.

          * DECIMAL_DEGREES—Similar to Degrees Minutes and Seconds, but fractions of
          degrees are represented as decimal values. Any number between 0 and 360 is
          valid.

          * RADIANS—An angular unit of measure, where there are 2 pi or approximately
          6.28318 in a complete circle. One radian is equivalent to about 57.296 degrees.
          Any number between 0 and 62318 is valid.

          * GONS—The same angular unit of measure as gradians where the right angle is
          divided into 100 parts. One gon is equal to 1/400 of a circle.

          * GRADIANS—An angular unit of measure where the right angle is divided into 100
          parts. One gradian is equal to 1/400 of a circle.
      direction_type {String}:
          The direction type to be used when generating COGO bearing attributes for line
          features during the migration process.

          * SOUTH_AZIMUTH—Directions are measured clockwise from south.

          * NORTH_AZIMUTH—Directions are measured clockwise from north.

          * POLAR—Directions are measured counterclockwise from the positive x-axis.

          * QUADRANT_BEARING—Directions are measured from a reference bearing of North or
          South, then East or West. NE bearings are measured clockwise from North. SE
          bearings are measured counterclockwise from South. SW bearings are measured
          clockwise from South. NW bearings are measured counterclockwise from North. This
          is the default.
      compute_area (Boolean):
          Determines how features will be migrated.

          * COMPUTE_AREA—Parcel area is computed from the polygon shape or COGO
          attributes. The Stated Area fabric system attribute on the fabric parcels table
          is populated with the computed value.

          * NO_COMPUTE—Parcel area is not computed from the polygon shape or COGO
          attributes. The Stated Area fabric system attribute on the fabric parcels table
          is not populated.
      area_units {String}:
          If the Compute Area for New Parcels option is checked, select the area units to
          be used when computing parcel area during the migration process.

          * SQUARE_METERS_HECTARE_OR_KILOMETERS—Depending on the size of the value, Square
          Meters, Hectares, or Kilometers is used as the unit of area. For example, if the
          area value is greater than 10,000, the area unit that will be used is Hectares.
          This is the default.

          * ACRES_ROODS_OR_PERCHES—Depending on the size of the value, Acres, Roods, or
          Perches is used as the unit of area. For example, if the area value is greater
          than 160, the area unit that will be used is Acres.

          * SQUARE_METERS—An International System of Units (SI) derived unit of area.
          Defined as the area of a square whose sides measure exactly one meter.

          * HECTARES—An SI unit of area equal to 10,000 Square Meters. Symbolized as ha.

          * ACRES—A United States Customary or Imperial unit of area equal to 4046.87 m²
          or 44,560 Square Feet.

          * SQUARE_RODS—A United States Customary or Imperial unit of area equal to 5.0292
          meters or 16.5 Feet. A Rod is the same length as a Perch and 160 Rods equals one
          Acre.

          * ROODS—A United States Customary or Imperial unit of area. One Acre equals four
          Roods and one Rood equals 40 Perches.

          * PERCHES—A United States Customary or Imperial unit of area equal to a Square
          Rod. 160 Perches equals one Acre.

          * SQUARE_FEET—A United States customary or Imperial unit of area. Defined as the
          area of a square whose sides measure exactly one Foot. One Foot equals 0.3048
          Meters.

          * SQUARE_US_FEET—A unit of area used when collecting survey data in the United
          States. One U.S. Foot equals 0.3048006 Meters.

          * QUARTER_SECTIONS—An area of unit used under the Public Land Survey System in
          the United States. A Section is an area equal to one Square Mile or 640 Acres. A
          Quarter Section is one-fourth of a Square Mile and is equal to 160 Acres.

          * SECTIONS—An area of unit used under the Public Land Survey System in the
          United States. A Section is an area equal to one Square Mile or 640 Acres.
      radial_point_tolerance {Linear unit}:
          The tolerance in which new, computed curve center points are matched with
          existing curve center points found in the fabric. Furthermore, if several
          computed curve center points lie within this tolerance, they are averaged and
          merged into a single center point. If a radial tolerance is not specified, the
          default of  0.5 meters is used.
      accuracy_units {String}:
          The accuracy category of the lines and polygons being migrated. Accuracy
          categories are defined by date of survey in the parcel fabric. Accuracy category
          1 is the highest data accuracy (recently surveyed) and accuracy category 6 is
          the lowest data accuracy (year 1800 or lower). Accuracy categories are used in
          the fabric adjustment.

          * 1_HIGHEST—Most recently surveyed and recorded data. Data accuracy is the
          highest.

          * 2_AFTER_1980—Data is surveyed and recorded after 1980.

          * 3_1908_TO_1980—Data is surveyed and recorded between 1908 and 1980.

          * 4_1881_TO_1907—Data is surveyed and recorded between 1881 and 1907.

          * 5_BEFORE_1881—Data is surveyed and recorded before 1881. Data accuracy is low.

          * 6_1800—Data is surveyed and recorded before 1800. Data accuracy is low. This
          is the default.

          * 7_LOWEST—Data is unreliable and data accuracy is unknown. Data is excluded
          from influencing the outcome of a fabric adjustment."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LoadTopologyToParcelFabric_fabric(*gp_fixargs((target_parcel_fabric, in_topology_class, in_point_class, linestring_minimum_segments, control_match_tolerance, unjoined_group, direction_units, direction_type, compute_area, area_units, radial_point_tolerance, accuracy_units), True)))
        return retval
    except Exception, e:
        raise e


# Layers and Table Views toolset
@gptooldoc('MakeParcelFabricLayer_fabric', None)
def MakeParcelFabricLayer(in_parcel_fabric=None, parcel_fabric_layer=None):
    """MakeParcelFabricLayer_fabric(in_parcel_fabric, parcel_fabric_layer)

        Creates a parcel fabric layer from an input parcel fabric. The parcel fabric
        layer that is created by the tool is temporary and will not persist after the
        session ends unless the document is saved. This tool is needed if you would like
        a parcel fabric sublayer to participate in a geoprocessing model.

     INPUTS:
      in_parcel_fabric (Parcel Fabric Layer):
          The parcel fabric dataset that will be used to create the parcel fabric layer.

     OUTPUTS:
      parcel_fabric_layer (Parcel Fabric Layer):
          The output parcel fabric layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeParcelFabricLayer_fabric(*gp_fixargs((in_parcel_fabric, parcel_fabric_layer), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeParcelFabricTableView_fabric', None)
def MakeParcelFabricTableView(in_parcel_fabric=None, parcel_fabric_table=None, out_view=None):
    """MakeParcelFabricTableView_fabric(in_parcel_fabric, parcel_fabric_table, out_view)

        Creates a table view from an input parcel fabric feature class or table. The
        table view that is created by the tool is temporary and will not persist after
        the session ends unless the document is saved. This tool is useful for accessing
        hidden, nonspatial parcel fabric tables, such as the Plans table or the
        Accuracies table.

     INPUTS:
      in_parcel_fabric (Parcel Fabric Layer):
          The parcel fabric dataset that contains the feature class or table that will be
          used to create a table view.
      parcel_fabric_table (String):
          The parcel fabric feature class or nonspatial table that will be used to create
          a table view.

     OUTPUTS:
      out_view (Table View):
          The name of the output table view."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeParcelFabricTableView_fabric(*gp_fixargs((in_parcel_fabric, parcel_fabric_table, out_view), True)))
        return retval
    except Exception, e:
        raise e


# Parcel Features toolset
@gptooldoc('AppendParcelFabric_fabric', None)
def AppendParcelFabric(in_parcels=None, target=None, unjoined_group=None, parcels_schema_type=None, field_mapping_parcels=None, parcels_subtype=None, lines_schema_type=None, field_mapping_lines=None, lines_subtype=None, control_schema_type=None, field_mapping_control=None, control_subtype=None):
    """AppendParcelFabric_fabric(in_parcels;in_parcels..., target, unjoined_group, {parcels_schema_type}, {field_mapping_parcels}, {parcels_subtype}, {lines_schema_type}, {field_mapping_lines}, {lines_subtype}, {control_schema_type}, {field_mapping_control}, {control_subtype})

        Appends one or multiple parcel fabrics into an existing target parcel fabric.
        The spatial reference of the input parcel fabrics must match the spatial
        reference of the target parcel fabric.

     INPUTS:
      in_parcels (Parcel Fabric Layer):
          The input parcel fabrics that will be appended into the target parcel fabric.
          The spatial reference of the input parcel fabric must match that of the target
          parcel fabric.
      target (Parcel Fabric):
          The existing parcel fabric that the input parcel fabrics will be appended into.
          The spatial reference of the input parcel fabric must match that of the target
          parcel fabric.
      unjoined_group (Boolean):
          Determines how parcels will be appended.

          * UNJOINED_GROUP—Parcels will be appended as unjoined, stand-alone parcels to
          the parcel fabric.

          * JOINED_GROUP—Parcels will be appended as joined parcels to the parcel fabric.
      parcels_schema_type {String}:
          Specifies if the schema (field definitions) of the input parcel fabric parcels
          table must match the schema of the target parcel fabric parcels table in order
          for data to be appended.

          * TEST—Input parcel fabric parcels table schema (field definitions) must match
          the schema of the target parcel fabric parcels table. An error will be returned
          if the schemas do not match.

          * NO_TEST—Input parcels table schema (field definitions) does not have to match
          that of the target parcels table. Any fields from the input parcels table that
          do not match the fields of the target parcels table will not be mapped to the
          target parcels table unless the same fields exist in the target parcels table.
      field_mapping_parcels {Field Mappings}:
          Lists the attribute fields that will be mapped to the target parcels table. The
          list includes the existing attribute fields of the target parcels table and
          attributes fields that match between the input parcels table and the target
          parcels table.Because the input parcel fabric is appended into an existing
          target parcel
          fabric that has a predefined schema (field definitions), the Parcels Extended
          Attribute Field Map control does not allow for fields to be added or removed
          from the target parcel fabric.
      parcels_subtype {String}:
          A subtype description to assign that subtype to all new parcel features in a
          parcel fabric which is appended to the target parcel fabric.
      lines_schema_type {String}:
          Specifies if the schema (field definitions) of the input parcel fabric lines
          table must match the schema of the target parcel fabric lines table in order for
          data to be appended.

          * TEST—Input parcel fabric lines table schema (field definitions) must match the
          schema of the target parcel fabric lines table. An error will be returned if the
          schemas do not match.

          * NO_TEST—Input lines table schema (field definitions) does not have to match
          that of the target lines table. Any fields from the input lines table that do
          not match the fields of the target lines table will not be mapped to the target
          lines table unless the same fields exist in the target lines table.
      field_mapping_lines {Field Mappings}:
          Lists the attribute fields that will be mapped to the target lines table. The
          list includes the existing attribute fields of the target lines table and
          attributes fields that match between the input lines table and the target lines
          table.Because the input parcel fabric is appended into an existing target parcel
          fabric that has a predefined schema (field definitions), the Lines Extended
          Attribute Field Map control does not allow for fields to be added or removed
          from the target parcel fabric.
      lines_subtype {String}:
          A subtype description to assign that subtype to all new line features in a
          parcel fabric which is appended to the target parcel fabric.
      control_schema_type {String}:
          Specifies if the schema (field definitions) of the input parcel fabric control
          table must match the schema of the target parcel fabric control table in order
          for data to be appended.

          * TEST—Input parcel fabric control table schema (field definitions) must match
          the schema of the target parcel fabric control table. An error will be returned
          if the schemas do not match.

          * NO_TEST—Input control table schema (field definitions) does not have to match
          that of the target control table. Any fields from the input control table that
          do not match the fields of the target control table will not be mapped to the
          target control table unless the same fields exist in the target control table.
      field_mapping_control {Field Mappings}:
          Lists the attribute fields that will be mapped to the target control table. The
          list includes the existing attribute fields of the target control table and
          attributes fields that match between the input control table and the target
          control table.Because the input parcel fabric is appended into an existing
          target parcel
          fabric that has a predefined schema (field definitions), the Control Points
          Extended Attribute Field Map control does not allow for fields to be added or
          removed from the target parcel fabric.
      control_subtype {String}:
          A subtype description to assign that subtype to all new control point features
          in a parcel fabric which is appended to the target parcel fabric."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AppendParcelFabric_fabric(*gp_fixargs((in_parcels, target, unjoined_group, parcels_schema_type, field_mapping_parcels, parcels_subtype, lines_schema_type, field_mapping_lines, lines_subtype, control_schema_type, field_mapping_control, control_subtype), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CopyParcelFabric_fabric', None)
def CopyParcelFabric(in_parcels=None, output_parcels=None, config_keyword=None):
    """CopyParcelFabric_fabric(in_parcels, output_parcels, {config_keyword})

        Copies parcels from the input parcel fabric dataset or layer to a new parcel
        fabric.

     INPUTS:
      in_parcels (Parcel Fabric Layer / Feature Layer):
          The parcels to be copied to another parcel fabric.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for parcel fabrics in file and
          ArcSDE geodatabases. Personal geodatabases do not use configuration
          keywords.ArcSDE configuration keywords for ArcSDE Enterprise Edition are set up
          by your
          database administrator.

     OUTPUTS:
      output_parcels (Parcel Fabric):
          The new parcel fabric to which the parcels will be copied. If the parcel fabric
          exists and you have chosen to overwrite the outputs of geoprocessing operations
          by setting arcpy.env.overwriteOutput to True,  the existing parcel fabric will
          be overwritten with a new parcel fabric containing the copied parcels."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyParcelFabric_fabric(*gp_fixargs((in_parcels, output_parcels, config_keyword), True)))
        return retval
    except Exception, e:
        raise e



# Parcel Fabric Management toolset
@gptooldoc('UpgradeParcelFabric_fabric', None)
def UpgradeParcelFabric(in_parcel_fabric=None):
    """UpgradeParcelFabric_fabric(in_parcel_fabric)

        Upgrades an existing parcel fabric to the latest released version of ArcGIS. An
        existing parcel fabric is upgraded to take advantage of the new parcel editing
        functionality available in the latest released version of ArcGIS.

        This tool has been deprecated. Use Upgrade Dataset tool instead.

     INPUTS:
      in_parcel_fabric (Parcel Fabric):
          The parcel fabric dataset that will be upgraded to the latest released version
          of ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeParcelFabric_fabric(*gp_fixargs((in_parcel_fabric,), True)))
        return retval
    except Exception as e:
        raise e

# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject