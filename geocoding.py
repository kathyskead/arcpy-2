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
"""Geocoding is the process of assigning a location, usually in the form of
coordinate values, to an address by comparing the descriptive location elements
in the address to those present in the reference material. Addresses come in
many forms, ranging from the common address format of house number followed by
the street name and succeeding information to other location descriptions such
as postal zone or census tract. In essence, an address includes any type of
information that distinguishes a place."""
__all__ = ['CreateCompositeAddressLocator', 'CreateAddressLocator', 'GeocodeAddresses', 'RebuildAddressLocator', 'RematchAddresses', 'StandardizeAddresses', 'ReverseGeocode']

# Deprecated tools
__all__ += ['ConsolidateLocator', 'PackageLocator']

__alias__ = u'geocoding'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('CreateAddressLocator_geocoding', None)
def CreateAddressLocator(in_address_locator_style=None, in_reference_data=None, in_field_map=None, out_address_locator=None, config_keyword=None, enable_suggestions=None):
    """CreateAddressLocator_geocoding(in_address_locator_style, in_reference_data;in_reference_data..., in_field_map, out_address_locator, {config_keyword}, {enable_suggestions})

        Creates an address locator. The address locator can be used to find a location
        of an address, geocode a table of addresses, or get the address of a point
        location.

     INPUTS:
      in_address_locator_style (Address Locator Style):
          The address locator style on which to base the new address locator.
      in_reference_data (Value Table):
          The reference data feature classes and tables to be used by the address locator,
          along with their roles.

          * Primary table—Defines the primary reference dataset feature class for a
          locator, such as a street centerline feature class. This is a required table.

          * Alternate Name table—Defines an alternate street name table that contains
          alternate names for the street or point features. The table is required to have
          a JoinID that can be used to join to the primary table. This table is optional.

          * Alias table—Defines a place name alias table that contains place names and
          actual addresses for the names. User can find the location using either the
          place name such as Field Museum or the address 1400 S Lakeshore Drive Chicago,
          IL 60605. This table is optional.
          Custom locator styles or locator styles provided by third parties may define a
          different set of roles for reference datasets.
      in_field_map (Field Info):
          The mapping of reference data fields used by the address locator style to fields
          in the reference datasets. Each field mapping in this parameter is in the
          format:   # <locator field alias> <dataset field name> VISIBLE NONE # This shows
          as an
          example: reference_data_field_map = ''' "'Feature ID' FeatureID VISIBLE
          NONE;'*From Left' L_F_ADD VISIBLE NONE; '*To Left' L_T_ADD VISIBLE NONE;'*From
          Right' R_F_ADD VISIBLE NONE; '*To Right' R_T_ADD VISIBLE NONE;'Prefix Direction'
          PREFIX VISIBLE NONE; 'Prefix Type' PRE_TYPE VISIBLE NONE;'*Street Name' NAME
          VISIBLE NONE; 'Suffix Type' TYPE VISIBLE NONE;'Suffix Direction' SUFFIX VISIBLE
          NONE'''where <locator field alias> is the alias name for the reference data
          field used
          by the address locator, and <dataset field name> is the name of the field in the
          reference dataset. Fields with an asterisk ("*") next to their names are
          required by the address locator style.VISIBLE—Field is visible; NONE—the
          geometry is a copy of the original value.If you choose not to map an optional
          reference data field used by the address
          locator style to a field in a reference dataset, specify that there is no
          mapping by using "<None>" in place of a field name.To determine the alias name
          for a reference data field used by a locator style,
          open the Create Address Locator tool dialog box and choose the locator style.
          The name that appears in the Field Name column of the Field Map control is the
          field's alias name.
      config_keyword {String}:
          The configuration keyword that determines the storage parameters of the table in
          a Relational Database Management System (RDBMS)—enterprise and file geodatabases
          only.
      enable_suggestions {Boolean}:
          Allows character-by-character auto-complete suggestions to be generated for user
          input in a client application. This capability facilitates the interactive
          search user experience by reducing the number of characters that need to be
          typed before a suggested match is obtained. The idea is that a client
          application can provide a list of suggestions which is updated with each
          character entered by a user until the place they are looking for is returned in
          the list.Only the locator styles provided by Esri can be used to build locators
          with
          suggestions enabled. The suggestion functionality is only exposed when such a
          locator is published as a geocode service. Locators with suggestions enabled can
          only be saved in a file folder; they cannot be saved in a geodatabase.

          * ENABLED—Suggestions are enabled for the locator.

          * DISABLED—Suggestions are disabled for the locator. This is the default.

     OUTPUTS:
      out_address_locator (Address Locator):
          The address locator to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateAddressLocator_geocoding(*gp_fixargs((in_address_locator_style, in_reference_data, in_field_map, out_address_locator, config_keyword, enable_suggestions), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateCompositeAddressLocator_geocoding', None)
def CreateCompositeAddressLocator(in_address_locators=None, in_field_map=None, in_selection_criteria=None, out_composite_address_locator=None):
    """CreateCompositeAddressLocator_geocoding(in_address_locators;in_address_locators..., in_field_map, {in_selection_criteria;in_selection_criteria...}, out_composite_address_locator)

        Creates a composite address locator. A composite address locator consists of two
        or more individual address locators that allow addresses to be matched against
        the multiple address locators.

     INPUTS:
      in_address_locators (Value Table):
          The order of the participating address locators determines how candidates are
          searched and an address is matched. When you geocode a single address, the
          address will be matched against all participating address locators unless the
          locator is specified with a selection criterion. All the found candidates will
          be displayed based on the order of the listed participating address locators. If
          you geocode a table of addresses, addresses are matched automatically to the
          first best candidate found from the first participating address locators. If the
          address fails to match, it will fall back to the subsequent locator in the
          list.A reference name for each participating address locator is required. This
          is the
          name of the address locator referred to by the composite address locator. The
          name should contain no space or special symbols. The maximum length of the name
          is 14 characters.
      in_field_map (Field Mappings):
          The mapping of input fields used by each participating address locator to the
          input fields of the composite address locator.
      in_selection_criteria {Value Table}:
          Selection criteria for each participating address locator. Only one selection
          criterion is supported for each participating address locator. Using selection
          criteria will disqualify participating address locators that do
          not meet the criteria on a particular address so that the geocoding process will
          be more efficient. Refer to the topic Creating a  composite address locator to
          learn more about the use of selection criteria in the geocoding process.

     OUTPUTS:
      out_composite_address_locator (Address Locator):
          The composite address locator to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateCompositeAddressLocator_geocoding(*gp_fixargs((in_address_locators, in_field_map, in_selection_criteria, out_composite_address_locator), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GeocodeAddresses_geocoding', None)
def GeocodeAddresses(in_table=None, address_locator=None, in_address_fields=None, out_feature_class=None, out_relationship_type=None):
    """GeocodeAddresses_geocoding(in_table, address_locator, in_address_fields, out_feature_class, {out_relationship_type})

        Geocodes a table of addresses. This process requires a table that stores the
        addresses you want to geocode and an address locator or a composite address
        locator. This tool matches the addresses against the address locator and saves
        the result for each input record in a new point feature class.

     INPUTS:
      in_table (Table View):
          The table of addresses to geocode.
      address_locator (Address Locator):
          The address locator to use to geocode the table of addresses.
      in_address_fields (Field Info):
          Each field mapping in this parameter is in the format input_address_field,
          table_field_name where input_address_field is the name of the input address
          field specified by the address locator, and table_field_name is the name of the
          corresponding field in the table of addresses you want to geocode.You may
          specify one single input field that stores the complete address.
          Alternatively, you may also specify multiple fields if the input addresses are
          split into different fields such as Address, City, State, and ZIP for a general
          United States address.If you choose not to map an optional input address field
          used by the address
          locator to a field in the input table of addresses, specify that there is no
          mapping by using <None> in place of a field name.
      out_relationship_type {Boolean}:
          Indicates whether to create a static copy of the address table inside the
          geocoded feature class or to create a dynamically updated geocoded feature
          class.

          * STATIC—Creates a static copy of the fields input address table in the output
          feature class. This is the default.

          * DYNAMIC—Creates a relationship class between the input address table and
          output feature class so that edits to the addresses in the input address table
          are automatically updated in the output feature class. This option is supported
          only if the input address table and output feature class are in the same
          geodatabase workspace.  This option is only supported if you have ArcGIS for
          Desktop Standard or
          Advanced licences. An error message saying "Geocode addresses failed" will be
          displayed if you do not have the proper license.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output geocoded feature class or shapefile."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeocodeAddresses_geocoding(*gp_fixargs((in_table, address_locator, in_address_fields, out_feature_class, out_relationship_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RebuildAddressLocator_geocoding', None)
def RebuildAddressLocator(in_address_locator=None):
    """RebuildAddressLocator_geocoding(in_address_locator)

        Rebuilds an address locator to update the locator with the current reference
        data. Since an address locator contains a snapshot of the reference data when it
        was created, it will not geocode addresses against the updated data when the
        geometry and attributes of the reference data are changed. To geocode addresses
        against the current version of the reference data, the address locator must be
        rebuilt if you want to update the changes in the locator.

     INPUTS:
      in_address_locator (Address Locator):
          The address locator to rebuild."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RebuildAddressLocator_geocoding(*gp_fixargs((in_address_locator,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RematchAddresses_geocoding', None)
def RematchAddresses(in_geocoded_feature_class=None, in_where_clause=None):
    """RematchAddresses_geocoding(in_geocoded_feature_class, {in_where_clause})

        Rematches addresses in a geocoded feature class.

     INPUTS:
      in_geocoded_feature_class (Feature Class):
          The geocoded feature class you want to rematch.
      in_where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RematchAddresses_geocoding(*gp_fixargs((in_geocoded_feature_class, in_where_clause), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReverseGeocode_geocoding', None)
def ReverseGeocode(in_features=None, in_address_locator=None, out_feature_class=None, address_type=None, search_distance=None):
    """ReverseGeocode_geocoding(in_features, in_address_locator, out_feature_class, {address_type}, search_distance)

        Creates addresses from point locations in a feature class. The reverse
        geocoding process searches for the nearest address or intersection for the point
        location based on the specified search distance.

     INPUTS:
      in_features (Feature Layer):
          A point feature class or layer from which addresses are returned based on the
          features' point location.
      in_address_locator (Address Locator):
          The address locator to use to reverse geocode the input feature class.
      address_type {String}:
          Indicates whether to return addresses for the points as street addresses or
          intersection addresses if the address locator supports intersection matching.

          * ADDRESS—Returns street addresses or in the format defined by the input address
          locator. This is the default option.

          * INTERSECTION—Returns intersection addresses. This option is available if the
          address locator supports matching intersection addresses.
      search_distance (Linear unit):
          The distance used to search for the nearest address or intersection for the
          point location.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReverseGeocode_geocoding(*gp_fixargs((in_features, in_address_locator, out_feature_class, address_type, search_distance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('StandardizeAddresses_geocoding', None)
def StandardizeAddresses(in_address_data=None, in_input_address_fields=None, in_address_locator_style=None, in_output_address_fields=None, out_address_data=None, in_relationship_type=None):
    """StandardizeAddresses_geocoding(in_address_data, in_input_address_fields;in_input_address_fields..., in_address_locator_style, in_output_address_fields;in_output_address_fields..., out_address_data, {in_relationship_type})

        Standardizes the address information in a table or feature class. Addresses are
        often presented in different forms that may contain various
        abbreviations of words, such as "W" for "WEST" or "ST" for "STREET". Based on an
        address style you select,  the address can be broken into multiple parts, such
        as House Number, Prefix Direction, Prefix Type, Street Name and Street Type.
        Each part will contain a piece of address information and the standardized
        value, such as "1ST" instead of "FIRST" as Street Name, "AVE" instead of
        "AVENUE" as Street Type.  The address style specifies the components of an
        address and determines how the components are ordered and standardized.
        Depending on the applications, some address styles may expand the value of a
        word instead of abbreviating it.The input address you want to standardize can be
        stored in a single field. If
        the address information has already been split into multiple fields in the input
        feature class or table, this tool can concatenate the fields on the fly and
        standardize the information.

     INPUTS:
      in_address_data (Table View):
          The table or feature class containing address information that you want to
          standardize.
      in_input_address_fields (String):
          The set of fields in the input table or feature class that, when concatenated,
          forms the address to be standardized.
      in_address_locator_style (Address Locator Style):
          The address locator style to use to standardize the address information in the
          input table or feature class.
      in_output_address_fields (String):
          The set of standardized address fields to include in the output table or feature
          class.
      in_relationship_type {Boolean}:
          Indicates whether to create a static or dynamic output dataset.

          * Static—Creates an output table or feature class that contains a copy of the
          rows or features in the input table and the standardized address fields. This is
          the default option.

          * Dynamic—Creates a table containing the standardized address fields and a
          relationship class that joins to the input table or feature class. The option
          only works if both the input and output datasets are stored in the
          same geodatabase workspace. This option is only supported if you have ArcGIS for
          Desktop Standard or
          Advanced licences. An error message saying "Standardize addresses failed" will
          be displayed if you do not have the proper license.

     OUTPUTS:
      out_address_data (Dataset):
          The output table or feature class to create containing the standardized address
          fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.StandardizeAddresses_geocoding(*gp_fixargs((in_address_data, in_input_address_fields, in_address_locator_style, in_output_address_fields, out_address_data, in_relationship_type), True)))
        return retval
    except Exception, e:
        raise e



@gptooldoc('ConsolidateLocator_geocoding', None)
def ConsolidateLocator(in_locator=None, output_folder=None, copy_arcsde_locator=None):
    """ConsolidateLocator_geocoding(in_locator, output_folder, {copy_arcsde_locator})

        As of the 10.2 release, this tool has been deprecated.
        Use ConsolidateLocator_management instead.

        Consolidate a locator or composite locator by copying all locators into a
        single folder.

     INPUTS:
      in_locator (Address Locator):
          The input locator or composite locator that will be consolidated.
      copy_arcsde_locator {Boolean}:
          Specifies whether participating locators will be copied or their connection
          information will be preserved in the composite locator. This option only applies
          to composite locators.

          * COPY_ARCSDEâ€”All participating locators, including locators in ArcSDE, will be
          copied to the consolidated folder or package. This is the default.

          * PRESERVE_ARCSDEâ€” Connection information of the participating locators that are
          stored in ArcSDE will be preserved in the composite locator.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the locator or composite locator with its
          participating locators."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConsolidateLocator_geocoding(*gp_fixargs((in_locator, output_folder, copy_arcsde_locator), True)))
        return retval
    except Exception as e:
        raise e


@gptooldoc('PackageLocator_geocoding', None)
def PackageLocator(in_locator=None, output_file=None, copy_arcsde_locator=None, additional_files=None, summary=None, tags=None):
    """PackageLocator_geocoding(in_locator, output_file, {copy_arcsde_locator}, {additional_files;additional_files...}, {summary}, {tags})

	    As of the 10.2 release, this tool has been deprecated.

        Package a locator or composite locator to create a single compressed .gcpk
        file.

     INPUTS:
      in_locator (Address Locator):
          The locator or composite locator that will be packaged.
      copy_arcsde_locator {Boolean}:
          Specifies whether participating locators will be copied or their connection
          information will be preserved in the composite locator. This option only applies
          to composite locators.

          * COPY_ARCSDEâ€”All participating locators, including locators in ArcSDE, will be
          copied to the consolidated folder or package. This is the default.

          * PRESERVE_ARCSDEâ€” Connection information of the participating locators that are
          stored in ArcSDE will be preserved in the composite locator.
      additional_files {File}:
          Adds additional files to a package. Additional files, such as .doc, .txt, .pdf,
          and so on, are used to provide more information about the contents and purpose
          of the package.
      summary {String}:
          Adds Summary information to the properties of the package.
      tags {String}:
          Adds Tag information to the properties of the package. Multiple tags can be
          added or separated by a comma or semicolon.

     OUTPUTS:
      output_file (File):
          The name and location of the output locator package (.gcpk)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PackageLocator_geocoding(*gp_fixargs((in_locator, output_file, copy_arcsde_locator, additional_files, summary, tags), True)))
        return retval
    except Exception as e:
        raise e

# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject