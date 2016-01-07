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
from _mapping import MapDocument, Layer, TableView, constants
from arcpy.arcobjects import mixins
from arcpy.arcobjects._base import _BaseArcObject, passthrough_attr
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
from arcpy.geoprocessing._base import gp_fixargs
from arcpy.utils import logcall, ArgAdaptor
import logging
import os
@constants.maskargs
def AddLayer(data_frame, add_layer, add_position='AUTO_ARRANGE'):
    """AddLayer(data_frame, add_layer, {add_position})
       Provides the ability to add a layer to a data frame within a map document (
       .mxd ) using simple placement options.
       
         data_frame(DataFrame):
       A reference to a DataFrame object within a map document.
       
         add_layer(Layer):
       A reference to a Layer object representing the layer to be added. This
       reference can point to a layer file on disk or a layer within a map
       document.
       
         add_position{String}:
       A constant that determines the placement of the added layer within a data
       frame.
       
        * AUTO_ARRANGE: Automatically places the layer similar to how the Add Data
       button works in ArcMap
       
        * BOTTOM: Places the layer at the bottom of the data frame
       
        * TOP: Places the layer at the top of the data frame"""
    from ._mapping import DataFrame, Layer
    assert isinstance(data_frame, DataFrame)
    assert isinstance(add_layer, Layer)
    my_copy = add_layer._arc_object.copy()
    if add_position.upper() == 'BOTTOM':
        lyrlist = data_frame._arc_object.layers
        data_frame._arc_object.InsertLayer(None, my_copy, len(lyrlist))
    elif add_position.upper() == 'TOP':
        data_frame._arc_object.InsertLayer(None, my_copy, 0)
    elif add_position.upper() == 'AUTO_ARRANGE':
        data_frame._arc_object.InsertLayer(None, my_copy)
@constants.maskargs
def AddLayerToGroup(data_frame, target_group_layer, add_layer, add_position='AUTO_ARRANGE'):
    """AddLayerToGroup(data_frame, target_group_layer, add_layer, {add_position})
       Provides the ability to add a layer to a group layer within a map document
       ( .mxd ) using simple placement options.
       
         data_frame(DataFrame):
       A reference to a DataFrame object that contains the group layer to which
       the new layer will be added.
       
         target_group_layer(Layer):
       A Layer object representing the group layer to which the new layer will be
       added. It must be a group layer.
       
         add_layer(Layer):
       A reference to a Layer object representing the layer to be added. This
       reference can point to a layer file on disk or a layer in a map document.
       
         add_position{String}:
       A constant that determines the placement of the added layer within a data
       frame.
       
        * AUTO_ARRANGE: Automatically places the layer similar to how the Add Data
       button works in ArcMap
       
        * BOTTOM: Places the layer at the bottom of the data frame
       
        * TOP: Places the layer at the top of the data frame"""
    from ._mapping import DataFrame, Layer
    assert isinstance(data_frame, DataFrame)
    assert isinstance(target_group_layer, Layer) and target_group_layer._arc_object.isGroupLayer
    assert isinstance(add_layer, Layer)
    my_copy = add_layer._arc_object.copy()
    if add_position.upper() == 'BOTTOM':
        lyrlist = target_group_layer._arc_object.layers
        data_frame._arc_object.InsertLayer(target_group_layer._arc_object, my_copy, len(lyrlist)+1)
    elif add_position.upper() == 'TOP':
        lyrlist = target_group_layer._arc_object.layers
        data_frame._arc_object.InsertLayer(target_group_layer._arc_object, my_copy, 0)
    elif add_position.upper() == 'AUTO_ARRANGE':
        data_frame._arc_object.InsertLayer(target_group_layer._arc_object, my_copy)
@constants.maskargs
def AddTableView(data_frame, add_table):
    """AddTableView(data_frame, add_table)
       Provides the ability to add a table to a data frame within a map document (
       .mxd ).
       
         data_frame(DataFrame):
       A reference to a DataFrame object within a map document.
       
         add_table(TableView):
       A reference to a TableView object representing the table to be added. This
       reference can point to a table  within an existing map document or it can
       reference a table in a workspace via the TableView function."""
    from ._mapping import DataFrame, TableView
    assert isinstance(data_frame, DataFrame)
    assert isinstance(add_table, TableView)
    data_frame._arc_object.InsertTableView(add_table._arc_object)
@constants.maskargs
def AnalyzeForMSD(map_document):
    """AnalyzeForMSD(map_document)
       Starting at ArcGIS 10.1 for Server , Map Server Definition ( .msd ) files
       have been replaced with Service Definition Draft ( .sddraft ) and Service
       Definition ( .sd ) files. Please use  the AnalyzeForSD function instead.
       
       Analyzes map documents ( .mxd ) to determine sources for potential
       suitability and performance issues when converting a map to a map service
       definition ( .msd ) file.
       
         map_document(MapDocument):
       A variable that references a MapDocument object."""
    result = mixins.MapDocumentMixin(map_document).analyzeForMSD()
    return result
def AnalyzeForSD(sddraft):
    """AnalyzeForSD(sddraft)
       Analyzes Service Definition Draft ( .sddraft ) files to determine
       suitability and sources of potential performance issues before  converting
       a Service Definition Draft file to a Service Definition ( .sd )  file.
       
         sddraft(String):
       A string that represents the path and file name for the Service Definition
       Draft ( .sddraft ) file."""
    import arcgisscripting
    return convertArcObjectToPythonObject(arcgisscripting._analyzeForSD(*gp_fixargs([sddraft], True)))
@constants.maskargs
def ConvertToMSD(map_document, out_msd, data_frame='USE_ACTIVE_VIEW', msd_anti_aliasing=0, msd_text_anti_aliasing=0):
    """ConvertToMSD(map_document, out_msd, {data_frame}, {msd_anti_aliasing}, {msd_text_anti_aliasing})
       Starting at ArcGIS 10.1 for Server , Map Server Definition ( .msd ) files
       have been replaced with Service Definition Draft ( .sddraft ) and Service
       Definition ( .sd ) files. Please use the CreateMapSDDraft function instead.
       
       Converts a map to a map service definition ( .msd ) file.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_msd(String):
       A string that represents the path and file name for the output MSD file.
       
         data_frame{DataFrame}:
       A variable that references a DataFrame object.  If more than one data frame
       exists, it is important to specify which data frame will be the active data
       frame for the published service.  The default value is the active data
       frame.
       
         msd_anti_aliasing{String}:
       A string that sets  antialiasing for nontext items within the saved MSD.
       
        * NONE:  No antialiasing is performed.
       
        * FASTEST: Minimal antialiasing is performed, optimized for speed.
       
        * FAST:  Some antialiasing is performed, optimized for speed with better
       quality than FASTEST.
       
        * NORMAL:  A good balance of speed and quality.
       
        * BEST:  The best quality antialiasing. This option takes the longest to
       render.
       
         msd_text_anti_aliasing{String}:
       A string that sets  antialiasing for text items within the saved MSD.
       
        * FORCE:  Text is always drawn with antialiasing, regardless of the
       individual font's parameters.
       
        * NORMAL: Antialiasing is performed as determined by the font. Each
       individual font has parameters created within it by the font author that
       defines which sizes the font should draw with antialiasing.
       
        * NONE:  No antialiasing is performed."""
    result = mixins.MapDocumentMixin(map_document).convertToMSD(out_msd, data_frame, msd_anti_aliasing, msd_text_anti_aliasing)
    return result
def ConvertWebMapToMapDocument(webmap_json, template_mxd=None, notes_gdb=None, extra_conversion_options=None):
    """ConvertWebMapToMapDocument(webmap_json, {template_mxd}, {notes_gdb}, {extra_conversion_options})
       Converts a web map (in JSON format) that you intend to print or export to a
       map document.
       The map document can be further modified before finally being printed or
       exported.
       
         webmap_json(String):
       The web map for printing in JavaScript Object Notation (JSON).
       See the ExportWebMap JSON specification for more information. The ArcGIS
       Web APIs (JavaScript, Flex, and Silverlight) allow developers to easily get
       this JSON string from the web application.
       
         template_mxd{String}:
       A string representing the path and file name to a map document (. mxd ) to
       use as the template for the page layout.  The contents of the web map will
       be inserted into the data frame that was active at the time the
       template_mxd was saved. Layers in the template_mxd file's active data frame
       (and all other data frames) will be preserved in the output mapDocument .
       
         notes_gdb{String}:
       A string representing the path to a new or existing file geodatabase or an
       existing enterprise geodatabase connection where graphic features should be
       written. This parameter should only be used if graphic features from the
       web map JSON need to be preserved permanently. In most cases, this
       parameter is not required, as a temporary in-memory  workspace will be used
       to store graphic features. This parameter allows you to save graphic
       features to persistent storage, which is essential if you plan to use the
       map document for operations that require saving or loading from disk (for
       example, packaging or consolidating). The path must end with a .gdb or .sde
       extension.
       
         extra_conversion_options{Dictionary}:
       A dictionary of credentials for secured services. This parameter is
       required if the services in the web map JSON require a user name and
       password to view.   Keys accepted in the dictionary are as follows:
       SERVER_CONNECTION_FILE WMS_CONNECTION_FILE WMTS_CONNECTION_FILE
       
       An example of key value pairs is as follows: credentials =
       {"SERVER_CONNECTION_FILE":r"Z:\ArcGIS2 on MyServer (user).ags",
                      "WMS_CONNECTION_FILE":r"Z:\USA on MyServer.wms"}
       result = arcpy.mapping.ConvertWebMapToMapDocument(json,
       extra_conversion_options=credentials)
       
       Lists of connection files can be used when there are multiple secured
       services: agsConnections = [r"Z:\ArcGIS on SecuredServerA (user).ags",
                         r"Z:\ArcGIS on SecuredServerB (user).ags"]
       credentials = {"SERVER_CONNECTION_FILE":agsConnections,
                      "WMS_CONNECTION_FILE":r"Z:\USA on MyServer.wms"}
       result = arcpy.mapping.ConvertWebMapToMapDocument(json,
       extra_conversion_options=credentials)"""
    from .arcobjects.mixins import webmap_tuple
    import arcgisscripting
    return webmap_tuple(*convertArcObjectToPythonObject(arcgisscripting._convertWebMapToMapDocument(webmap_json, template_mxd, notes_gdb, extra_conversion_options)))
@constants.maskargs
def CreateGISServerConnectionFile(connection_type, out_folder_path, out_name, server_url, server_type=None, use_arcgis_desktop_staging_folder=None, staging_folder_path=None, username=None, password=None, save_username_password=None):
    """CreateGISServerConnectionFile(connection_type, out_folder_path, out_name, server_url, server_type, {use_arcgis_desktop_staging_folder}, {staging_folder_path}, {username}, {password}, {save_username_password})
       This function creates a connection file that can be used to connect to a
       GIS Server.
       
         connection_type(String):
       A string that represents the connection type.
       You can create a connection to use, publish, or administer GIS Services.
       
        * USE_GIS_SERVICES: Use GIS Services.
       
        * PUBLISH_GIS_SERVICES: Publish GIS Services.
       
        * ADMINISTER_GIS_SERVICES: Administer GIS Services.
       
         out_folder_path(String):
       The folder path where the .ags file will be stored. Entering a value of GIS
       Servers will put the .ags file in the GIS Servers node in the Catalog
       window.
       
         out_name(String):
       The name of the .ags file. The output file extension must end with .ags.
       
         server_url(String):
       A string that represents the URL to the server.
       
         server_type(String):
       A string that represents the type of server.
       
        * ARCGIS_SERVER: ArcGIS for Server server type
       
        * SPATIAL_DATA_SERVER: Spatial Data Server server type
       
       If you are using SPATIAL_DATA_SERVER  server_type , starting at ArcGIS
       10.2.1 for Desktop , only USE_GIS_SERVICES  connection_type is supported.
       Any connection_type is supported for ARCGIS_SERVER  server_type .
       
         use_arcgis_desktop_staging_folder{Boolean}:
       A Boolean that determines whether to use ArcGIS for Desktop 's staging
       folder. If set to true, you do not have to enter a staging_folder_path as
       ArcGIS for Desktop 's staging folder will be used. This parameter is only
       used if the connection_type is PUBLISH_GIS_SERVICES or
       ADMINISTER_GIS_SERVICES .
       
         staging_folder_path{String}:
       A string that represents the staging folder path.  If you will be using
       this connection to create and save service definitions, you can choose
       where the service definition files will be staged on disk. By default, they
       are staged in a folder on your local machine. If this parameter is set to
       None, ArcGIS for Desktop 's staging folder will be used. This parameter is
       only used if the connection_type is PUBLISH_GIS_SERVICES or
       ADMINISTER_GIS_SERVICES .
       
         username{String}:
       A string that represents the user name to the GIS server.
       
         password{String}:
       A string that represents the password to the GIS server.
       
         save_username_password{Boolean}:
       A Boolean that represents whether the user name and password to the GIS
       Server will be saved in the connection file.
       
        * SAVE_USERNAME: Save the user name and password in the connection file.
       
        * DO_NOT_SAVE_USERNAME: Do not save the user name and password in the
       connection file."""
    import arcgisscripting
    return convertArcObjectToPythonObject(arcgisscripting._createGISServerConnectionFile(*gp_fixargs([connection_type, out_folder_path, out_name, server_url, server_type, use_arcgis_desktop_staging_folder, staging_folder_path, username, password, save_username_password], True, False)))
@constants.maskargs
def CreateMapSDDraft(map_document, out_sddraft, service_name=None, server_type='ARCGIS_SERVER', connection_file_path=None, copy_data_to_server=False, folder_name=None, summary=None, tags=None):
    """CreateMapSDDraft(map_document, out_sddraft, service_name, {server_type}, {connection_file_path}, {copy_data_to_server}, {folder_name}, {summary}, {tags})
       Converts Map Document ( .mxd ) files to Service Definition Draft ( .sddraft
       )  files.
       
         map_document(MapDocument):
       A variable that references a MapDocument object. The data frame that was
       active at the time the map_document was saved will be published.
       
         out_sddraft(String):
       A string that represents the path and file name for the output Service
       Definition Draft ( .sddraft ) file.
       
         service_name(String):
       A string that represents the name of the service. This is the name people
       will see and use to identify the service. The name can only contain
       alphanumeric characters and underscores. No spaces or special characters
       are allowed. The name cannot be more than 120 characters in length.
       
         server_type{String}:
       A string representing the server type.
       If a connection_file_path parameter is not supplied, then a server_type
       must be provided. If a connection_file_path parameter is supplied, then the
       server_type is taken from the connection file. In this case, you can choose
       FROM_CONNECTION_FILE or skip the parameter entirely.
       
        * ARCGIS_SERVER:  ArcGIS for Server server type
       
        * FROM_CONNECTION_FILE: Get the server_type as specified in the
       connection_file_path parameter
       
        * MY_HOSTED_SERVICES:  My Hosted Services server type for ArcGIS Online or
       Portal for ArcGIS
       
       Starting at ArcGIS 10.2.1 for Desktop , SPATIAL_DATA_SERVER is not a
       supported server_type .
       
         connection_file_path{String}:
       A string that represents the path and file name to the ArcGIS for Server
       connection file  ( .ags ).
       
       When the server_type is set to MY_HOSTED_SERVICES , connection_file_path is
       not required.
       
         copy_data_to_server{Boolean}:
       A Boolean that indicates whether the data referenced in the map document
       will be copied to the server or not.
       The copy_data_to_server parameter is only used if the server_type is
       ARCGIS_SERVER and the connection_file_path isn't specified. If the
       connection_file_path is specified, then the server's registered data stores
       are used. For example, if the data in the map_document is registered with
       the server, then copy_data_to_server will always be False . Conversely, if
       the data in the map_document is not registered with the server, then
       copy_data_to_server will always be True .
       
       When the server_type is set to MY_HOSTED_SERVICES , copy_data_to_server
       will always be True . My Hosted Maps services always copy data to the
       server.
       
         folder_name{String}:
       A string that represents  a folder name to which you want to publish the
       service definition. If the folder does not currently exist, it will be
       created.  The default folder is the server root level.
       
         summary{String}:
       A string that represents the Item Description Summary.
       
       By default, the Summary from the ArcMap Map Properties dialog box or
       Catalog window Item Description dialog box for the map_document will be
       used. Use this parameter to override the user interface summary, or to
       provide a summary if one does not exist. The summary provided here will not
       be persisted in the map document.
       
         tags{String}:
       A string that represents the Item Description Tags.
       
       By default, the Tags from the ArcMap Map Properties dialog box or Catalog
       window Item Description dialog box for the map_document will be used. Use
       this parameter to override the user interface tags, or to provide tags if
       they do not exist. The tags provided here will not be persisted in the map
       document."""
    import arcgisscripting
    return convertArcObjectToPythonObject(arcgisscripting._createMapSDDraft(*gp_fixargs([map_document, out_sddraft, service_name, server_type, connection_file_path, copy_data_to_server, folder_name, summary, tags], True, False)))
def DeleteMapService(connection_url_or_name, server, service_name, folder_name='', connection_username=None, connection_password=None, connection_domain=None):
    """DeleteMapService(connection_url_or_name, server, service_name, {folder_name}, {connection_username}, {connection_password}, {connection_domain})
       This method has been deprecated starting at ArcGIS 10.1 for Server and
       ArcGIS  10.1 for Desktop and will return a runtime error. Please consult
       the ArcGIS documentation for the usage of the new ArcGIS for Server
       Administrator API . Deletes a map service from a designated ArcGIS for
       Server .
       
         connection_url_or_name(String):
       A string that represents the URL of the ArcGIS for Server for which you
       want to delete a service.
       
         server(String):
       A string that represents the ArcGIS for Server host name.
       
         service_name(String):
       A string that represents the name of the service. This is the name people
       will see and use to identify the service. The name can only contain
       alphanumeric characters and underscores. No spaces or special characters
       are allowed. The name cannot be more than 120 characters in length.
       
         folder_name{String}:
       A string that represents  a folder name.
       
         connection_username{String}:
       A string that represents a user name used to connect to ArcGIS for Server .
       This variable is only necessary when connecting to a UNIX/Linux ArcGIS for
       Server .
       
         connection_password{String}:
       A string that represents a password used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server .
       
         connection_domain{String}:
       A string that represents a domain name used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server ."""
    from arcpy import GetIDMessage
    raise Exception(GetIDMessage(88014, 'This method has been deprecated. Please consult the help for the usage of the new ArcGIS Server APIs.'))
@constants.maskargs
def ExportReport(report_source, report_layout_file, output_file, dataset_option='USE_RLF', report_title=None, starting_page_number=1, page_range=None, report_definition_query=None, extent=None, field_map=None):
    """ExportReport(report_source, report_layout_file, output_file, {dataset_option}, {report_title}, {starting_page_number}, {page_range}, {report_definition_query}, {extent}, {field_map})
       Exports a formatted, tabular report using data from layers or stand-alone
       tables in a map document along with the report template information that is
       provided in a report layout file ( .rlf ).
       
         report_source(Object):
       A reference to a Layer or TableView object.
       
         report_layout_file(String):
       A string that represents the path and file name of the report layout  file
       ( .rlf ).
       
         output_file(String):
       A string that represents the path and file name of the output file.  The
       specified file extension controls the output format.  The following
       extensions/formats are supported: .htm, .html, .pdf, .rtf, .tif, .tiff,
       .txt, and  .xls .
       
         dataset_option{String}:
       A keyword that specifies which dataset rows will be processed in the output
       report.  This value will override the Dataset Options value stored in the
       report layout file which is found in the Report Properties dialog box.  If
       the dataset_option parameter is not set, it will default to the value
       stored in the report layout file.  If the dataset_option is set to
       DEFINITION_QUERY , then a valid string needs to be provided for the
       report_definition_query parameter.  If the dataset_option is set to EXTENT
       , then a valid Extent object needs to be provided for the extent parameter.
       Because the dataset_option keyword controls which additional parameter to
       use, only one of these parameters can be set at a time, just like in the
       user interface.
       
        * ALL: Override the report layout file dataset option and process all data
       source records.
       
        * DEFINITION_QUERY: Override the report layout file dataset option and
       provide a new or updated definition query.
       
        * EXTENT: Override the report layout file dataset option and provide a new
       or updated extent.
       
        * SELECTED: Override the  report layout file dataset option and process
       only the selected records.
       
        * USE_RLF: Use the settings saved in the report layout file.
       
         report_title{String}:
       A string that represents the report's title which appears in the report
       layout file header section.
       
         starting_page_number{Long}:
       A number that represents the printed page number for the first page of the
       output report.  This value is useful for offsetting page numbers for
       reports that get appended to the end  of existing documents.
       
         page_range{String}:
       A string that identifies the report pages to be exported to file (for
       example, 1, 3, 5?12 ).
       
         report_definition_query{String}:
       A string that represents a valid  definition query that controls which rows
       will be exported to the output report.  This parameter can only be set if
       the dataset_option parameter is set to DEFINITION_QUERY .This value will
       overwrite any settings stored in the report layout file.  If the
       report_source layer or table has an  existing definition query, then the
       report_definition_query will be applied to the existing subset of records.
       
         extent{Extent}:
       A geoprocessing Extent object.  This parameter can only be set if the
       dataset_option parameter is set to EXTENT . When an extent object is passed
       into this parameter, the rows will be based on those features that
       intersect the extent.
       
         field_map{Dictionary}:
       This parameter allows you to use a report layout file with a data source
       that has similar data types but different field names.  A dictionary of
       mapped field names is used to remap the fields used in the report layout
       file with the new fields in the data source. The following shows an example
       of the field_map dictionary structure:
       field_map={'rlf_field1':'data_source_field1',
       'rlf_field2':'data_source_field2'}"""
    from ._mapping import MapDocument, TableView, Layer
    from .utils import getstartingpage
    from .geoprocessing._base import gp_fixargs
    assert isinstance(report_source, (MapDocument, TableView, Layer)), str(type(report_source))
    if starting_page_number != 1 and ',' in (page_range or ''):
        raise ValueError(page_range)
    if page_range and starting_page_number != 1:
        min_page = getstartingpage(page_range)
        starting_page_number -= (min_page - 1)
    if isinstance(dataset_option, basestring) and dataset_option.upper() == 'USE_RLF':
        dataset_option = 2
    return report_source._arc_object.ExportReport(*gp_fixargs((report_layout_file, output_file, dataset_option, report_title, starting_page_number, page_range, report_definition_query, extent, field_map), True))
@constants.maskargs
def ExportToAI(map_document, out_ai, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=300, image_quality='BEST', colorspace='RGB', picture_symbol='RASTERIZE_BITMAP', convert_markers=False):
    """ExportToAI(map_document, out_ai, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {colorspace}, {picture_symbol}, {convert_markers})
       Exports the page layout or data frame of a map document ( .mxd ) to Adobe
       Illustrator (AI) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_ai(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting  a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5.
       
         colorspace{String}:
       A string that defines which color space will be written to the export file.
       
        * CMYK:  Cyan, Magenta,Yellow, and blacK color model.
       
        * RGB:  Red, Green, and Blue color model.
       
         picture_symbol{String}:
       A string that defines whether picture markers and picture fills will be
       converted to vector or rasterized on output.
       
        * RASTERIZE_BITMAP:   Rasterize layers with bitmap markers/fills.
       
        * RASTERIZE_PICTURE:   Rasterize layers with any picture marker/fill.
       
        * VECTORIZE_BITMAP:   Vectorize layers with bitmap markers/fills.
       
         convert_markers{Boolean}:
       A Boolean that controls the coversion of character-based marker symbols to
       polygons. This allows the symbols to appear correctly if the symbol font is
       not available or cannot be embedded. However, setting this parameter to
       True disables font embedding for all character-based marker symbols, which
       can result in a change in their appearance."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_ai, df_export_width, df_export_height, resolution, image_quality, colorspace, picture_symbol, convert_markers))
    layout.exportToAI(*args)
@constants.maskargs
def ExportToBMP(map_document, out_bmp, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=96, world_file=None, color_mode='24-BIT_TRUE_COLOR', rle_compression='NONE'):
    """ExportToBMP(map_document, out_bmp, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {world_file}, {color_mode}, {rle_compression})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Microsoft Windows Bitmap (BMP) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_bmp(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         world_file{Boolean}:
       If set to True , a georeferenced world file is created. The file contains
       pixel scale information and real-world coordinate information.
       
         color_mode{String}:
       This value specifies the number of bits used to describe color.
       
        * 24-BIT_TRUE_COLOR:   24-bit true color.
       
        * 8-BIT_PALETTE:   8-bit palette.
       
        * 8-BIT_GRAYSCALE:   8-bit grayscale.
       
        * 1-BIT_MONOCHROME_MASK:   1-bit monochrome mask.
       
        * 1-BIT_MONOCHROME_THRESHOLD:   1-bit monochrome threshold.
       
         rle_compression{String}:
       This value represents a compression scheme.
       
        * NONE:   Compression is not applied.
       
        * RLE:   Run-length encoded compression."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_bmp, df_export_width, df_export_height, resolution, world_file, color_mode, rle_compression))
    layout.exportToBMP(*args)
@constants.maskargs
def ExportToEMF(map_document, out_emf, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=300, image_quality='BEST', description='', picture_symbol='RASTERIZE_BITMAP', convert_markers=False):
    """ExportToEMF(map_document, out_emf, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {description}, {picture_symbol}, {convert_markers})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Enhanced Metafile (EMF) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_emf(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5.
       
         description{String}:
       A string that assigns a description to the output file.
       
         picture_symbol{String}:
       A string that defines whether picture markers and picture fills will be
       converted to vector or rasterized on output.
       
        * RASTERIZE_BITMAP:   Rasterize layers with bitmap markers/fills.
       
        * RASTERIZE_PICTURE:   Rasterize layers with any picture marker/fill.
       
        * VECTORIZE_BITMAP:   Vectorize layers with bitmap markers/fills.
       
         convert_markers{Boolean}:
       A Boolean that controls the coversion of character-based marker symbols to
       polygons. This allows the symbols to appear correctly if the symbol font is
       not available or cannot be embedded. However, setting this parameter to
       True disables font embedding for all character-based marker symbols, which
       can result in a change in their appearance."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_emf, df_export_width, df_export_height, resolution, image_quality, description, picture_symbol, convert_markers))
    layout.exportToEMF(*args)
@constants.maskargs
def ExportToEPS(map_document, out_eps, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=300, image_quality='BEST', colorspace='RGB', ps_lang_level=3, image_compression='ADAPTIVE', picture_symbol='RASTERIZE_BITMAP', convert_markers=False, embed_fonts=False, jpeg_compression_quality=80):
    """ExportToEPS(map_document, out_eps, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {colorspace}, {ps_lang_level}, {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts}, {jpeg_compression_quality})
       Exports the page layout or data frame of a map document ( .mxd ) to an
       Encapsulated Postscript (EPS) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_eps(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5.
       
         colorspace{String}:
       A string that defines the colorspace of the export file.
       
        * CMYK:  Cyan, Magenta,Yellow, and blacK color model.
       
        * RGB:  Red, Green, and Blue color model.
       
         ps_lang_level{Integer}:
       A number that represents the PostScript Language level. Level 3 is the most
       recent release, but some older PostScript interpreters may not be able to
       read files created using this version.  Valid levels are 2 and 3.
       
         image_compression{String}:
       A string that defines the compression scheme used to compress image or
       raster data in the output file.
       
        * ADAPTIVE:   Automatically selects the best compression type for each
       image on the page.   JPEG will be used for large images with many unique
       colors.  DEFLATE will be used for all other images.
       
        * JPEG:   A lossy data compression.
       
        * DEFLATE:   A lossless data compression.
       
        * LZW:   Lempel-Ziv-Welch, a lossless data compression.
       
        * NONE:   Compression is not applied.
       
        * RLE:   Run-length encoded compression.
       
         picture_symbol{String}:
       A string that defines whether picture markers and picture fills will be
       converted to vector or rasterized on output.
       
        * RASTERIZE_BITMAP:   Rasterize layers with bitmap markers/fills.
       
        * RASTERIZE_PICTURE:   Rasterize layers with any picture marker/fill.
       
        * VECTORIZE_BITMAP:   Vectorize layers with bitmap markers/fills.
       
         convert_markers{Boolean}:
       A Boolean that controls the coversion of character-based marker symbols to
       polygons. This allows the symbols to appear correctly if the symbol font is
       not available or cannot be embedded. However, setting this parameter to
       True disables font embedding for all character-based marker symbols, which
       can result in a change in their appearance.
       
         embed_fonts{Boolean}:
       A Boolean that controls the embedding of fonts in export files. Font
       embedding allows text and character markers to be displayed correctly when
       the document is viewed on a computer that does not have necessary fonts
       installed.
       
         jpeg_compression_quality{Integer}:
       A number that controls compression quality value when image_compression is
       set to ADAPTIVE or JPEG. The valid range is 1 to 100.    A
       jpeg_compression_quality of 100 provides the best quality images but
       creates large export files.   The recommended range is between 70 and 90."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_eps, df_export_width, df_export_height, resolution, image_quality, colorspace, ps_lang_level, image_compression, picture_symbol, convert_markers, embed_fonts, jpeg_compression_quality))
    layout.exportToEPS(*args)
@constants.maskargs
def ExportToGIF(map_document, out_gif, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=96, world_file=None, color_mode='8-BIT_PALETTE', gif_compression='NONE', background_color='255, 255, 255', transparent_color=None, interlaced=False):
    """ExportToGIF(map_document, out_gif, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {world_file}, {color_mode}, {gif_compression}, {background_color}, {transparent_color}, {interlaced})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Graphic Interchange (GIF) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_gif(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         world_file{Boolean}:
       If set to True , a georeferenced world file is created. The file contains
       pixel scale information and real-world coordinate information.
       
         color_mode{String}:
       This value specifies the number of bits used to describe color.
       
        * 24-BIT_TRUE_COLOR:   24-bit true color.
       
        * 8-BIT_PALETTE:   8-bit palette.
       
        * 8-BIT_GRAYSCALE:   8-bit grayscale.
       
        * 1-BIT_MONOCHROME_MASK:   1-bit monochrome mask.
       
        * 1-BIT_MONOCHROME_THRESHOLD:   1 bit monochrome threshold.
       
         gif_compression{String}:
       This value represents a compression scheme.
       
        * LZW:   Lempel-Ziv-Welch, a lossless data compression.
       
        * NONE:   Compression is not applied.
       
        * RLE:   Run-length encoded compression.
       
         background_color{String}:
       A defined color is used as a background to the image, or as a mask in the
       case of monochrome masked exports.
       
         transparent_color{String}:
       A defined color to be displayed as transparent in the image.
       
         interlaced{Boolean}:
       If set to True , an interlaced image will be created. An interlaced image
       displays as a series of scan lines rather than as a whole image at one
       time."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_gif, df_export_width, df_export_height, resolution, world_file, color_mode, gif_compression, background_color, transparent_color, interlaced))
    layout.exportToGIF(*args)
@constants.maskargs
def ExportToJPEG(map_document, out_jpeg, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=96, world_file=None, color_mode='24-BIT_TRUE_COLOR', jpeg_quality=100, progressive=False):
    """ExportToJPEG(map_document, out_jpeg, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {world_file}, {color_mode}, {jpeg_quality}, {progressive})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Joint Photographic Experts Group (JPEG) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_jpeg(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         world_file{Boolean}:
       If set to True , a georeferenced world file is created. The file contains
       pixel scale information and real-world coordinate information.
       
         color_mode{String}:
       This value specifies the number of bits used to describe color.
       
        * 24-BIT_TRUE_COLOR:   24-bit true color.
       
        * 8-BIT_PALETTE:   8-bit palette.
       
        * 8-BIT_GRAYSCALE:   8-bit grayscale.
       
        * 1-BIT_MONOCHROME_MASK:   1-bit monochrome mask.
       
        * 1-BIT_MONOCHROME_THRESHOLD:   1-bit monochrome threshold.
       
         jpeg_quality{Integer}:
       This value (0?100) controls the amount of compression applied to the
       output image. For JPEG, image quality is adversely affected the more
       compression is applied. A higher quality (highest = 100) setting will
       produce sharper images and larger file sizes. A lower quality setting will
       produce more image artifacts and smaller files.
       
         progressive{Boolean}:
       If set to True , a progressive JPEG file will be created. A progressive
       image is one that displays in a series of scans of increasing quality
       rather than displaying the whole image at once."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_jpeg, df_export_width, df_export_height, resolution, world_file, color_mode, jpeg_quality, progressive))
    layout.exportToJPEG(*args)
@constants.maskargs
def ExportToPDF(map_document, out_pdf, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=300, image_quality='BEST', colorspace='RGB', compress_vectors=True, image_compression='ADAPTIVE', picture_symbol='RASTERIZE_BITMAP', convert_markers=False, embed_fonts=True, layers_attributes='LAYERS_ONLY', georef_info=True, jpeg_compression_quality=80):
    """ExportToPDF(map_document, out_pdf, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {colorspace}, {compress_vectors}, {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts}, {layers_attributes}, {georef_info}, {jpeg_compression_quality})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Portable Document Format (PDF).
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_pdf(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5.
       
         colorspace{String}:
       A string that defines the colorspace of the export file. Valid values are
       CYMK and RGB.
       
        * CMYK:  Cyan, Magenta,Yellow, and blacK color model.
       
        * RGB:  Red, Green, and Blue color model.
       
         compress_vectors{Boolean}:
       A Boolean that controls compression of vector and text portions of the
       output file. Image compression is defined separately.
       
         image_compression{String}:
       A string that defines the compression scheme used to compress image or
       raster data in the output file.
       
        * ADAPTIVE:   Automatically selects the best compression type for each
       image on the page.   JPEG will be used for large images with many unique
       colors.  DEFLATE will be used for all other images.
       
        * JPEG:   A lossy data compression.
       
        * DEFLATE:   A lossless data compression.
       
        * LZW:   Lempel-Ziv-Welch, a lossless data compression.
       
        * NONE:   Compression is not applied.
       
        * RLE:   Run-length encoded compression.
       
         picture_symbol{String}:
       A string that defines whether picture markers and picture fills will be
       converted to vector or rasterized on output.
       
        * RASTERIZE_BITMAP:   Rasterize layers with bitmap markers/fills.
       
        * RASTERIZE_PICTURE:   Rasterize layers with any picture marker/fill.
       
        * VECTORIZE_BITMAP:   Vectorize layers with bitmap markers/fills.
       
         convert_markers{Boolean}:
       A Boolean that controls the coversion of character-based marker symbols to
       polygons. This allows the symbols to appear correctly if the symbol font is
       not available or cannot be embedded. However, setting this parameter to
       True disables font embedding for all character-based marker symbols, which
       can result in a change in their appearance.
       
         embed_fonts{Boolean}:
       A Boolean that controls the embedding of fonts in the export file. Font
       embedding allows text and character markers to be displayed correctly when
       the document is viewed on a computer that does not have the necessary fonts
       installed.
       
         layers_attributes{String}:
       A string that controls inclusion of PDF layer and PDF object data
       (attributes) in the export file.
       
        * LAYERS_ONLY:  Export PDF layers only.
       
        * LAYERS_AND_ATTRIBUTES:  Export PDF layers and feature attributes.
       
        * NONE:  None.
       
         georef_info{Boolean}:
       A Boolean that enables the export of coordinate system information for each
       data frame into the output PDF file.
       
         jpeg_compression_quality{Integer}:
       A number that controls compression quality value when image_compression is
       set to ADAPTIVE or JPEG. The valid range is 1 to 100.    A
       jpeg_compression_quality of 100 provides the best quality images but
       creates large export files.   The recommended range is between 70 and 90."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc._arc_object
    args = gp_fixargs((out_pdf, df_export_width, df_export_height, resolution, image_quality, colorspace, compress_vectors, image_compression, picture_symbol, convert_markers, embed_fonts, layers_attributes, georef_info, jpeg_compression_quality), True)
    layout.exportToPDF(*args)
@constants.maskargs
def ExportToPNG(map_document, out_png, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=96, world_file=None, color_mode='24-BIT_TRUE_COLOR', background_color='255, 255, 255', transparent_color=None, interlaced=False):
    """ExportToPNG(map_document, out_png, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {world_file}, {color_mode}, {background_color}, {transparent_color}, {interlaced})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Portable Network Graphics (PNG) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_png(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         world_file{Boolean}:
       If set to True , a georeferenced world file is created. The file contains
       pixel scale information and real-world coordinate information.
       
         color_mode{String}:
       This value specifies the number of bits used to describe color.
       
        * 24-BIT_TRUE_COLOR:   24-bit true color
       
        * 8-BIT_PALETTE:   8-bit palette
       
        * 8-BIT_GRAYSCALE:   8-bit grayscale
       
        * 1-BIT_MONOCHROME_MASK:   1-bit monochrome mask
       
        * 1-BIT_MONOCHROME_THRESHOLD:   1-bit monochrome threshold
       
         background_color{String}:
       A defined color is used as a background to the image, or as a mask in the
       case of monochrome masked exports.
       
         transparent_color{String}:
       A defined color to be displayed as transparent in the image.
       
         interlaced{Boolean}:
       If set to True, an interlaced image will be created. An interlaced image
       displays as a series of scan lines rather than as a whole image at one
       time."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_png, df_export_width, df_export_height, resolution, world_file, color_mode, background_color, transparent_color, interlaced))
    layout.exportToPNG(*args)
@constants.maskargs
def ExportToSVG(map_document, out_svg, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=300, image_quality='BEST', compress_document=False, picture_symbol='RASTERIZE_BITMAP', convert_markers=False, embed_fonts=False):
    """ExportToSVG(map_document, out_svg, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {compress_document}, {picture_symbol}, {convert_markers}, {embed_fonts})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Scalable Vector Graphics (SVG) format.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_svg(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the height of the export image in pixels for a data
       frame export. df_export_height is only used when exporting a data frame.
       Exporting a page layout uses the map document page height instead of
       df_export_height .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in dots per inch
       (DPI).
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5.
       
         compress_document{Boolean}:
       If set to True , a compressed export will be created. For SVG, the entire
       document is compressed and it changes the file extension to *.svgz.
       
         picture_symbol{String}:
       A string that defines whether picture markers and picture fills will be
       converted to vector or rasterized on output.
       
        * RASTERIZE_BITMAP:   Rasterize layers with bitmap markers/fills.
       
        * RASTERIZE_PICTURE:   Rasterize layers with any picture marker/fill.
       
        * VECTORIZE_BITMAP:   Vectorize layers with bitmap markers/fills.
       
         convert_markers{Boolean}:
       A Boolean that controls the coversion of character-based marker symbols to
       polygons. This allows the symbols to appear correctly if the symbol font is
       not available or cannot be embedded. However, setting this parameter to
       True disables font embedding for all character-based marker symbols, which
       can result in a change in their appearance.
       
         embed_fonts{Boolean}:
       A Boolean that controls the embedding of fonts in export files. Font
       embedding allows text and character markers to be displayed correctly when
       the document is viewed on a computer that does not have the necessary fonts
       installed."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_svg, df_export_width, df_export_height, resolution, image_quality, compress_document, picture_symbol, convert_markers, embed_fonts))
    layout.exportToSVG(*args)
@constants.maskargs
def ExportToTIFF(map_document, out_tiff, data_frame='PAGE_LAYOUT', df_export_width=640, df_export_height=480, resolution=96, world_file=None, color_mode='24-BIT_TRUE_COLOR', tiff_compression='LZW', geoTIFF_tags=False):
    """ExportToTIFF(map_document, out_tiff, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {world_file}, {color_mode}, {tiff_compression}, {geoTIFF_tags})
       Exports the page layout or data frame of a map document ( .mxd ) to the
       Tagged Image File Format (TIFF).
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         out_tiff(String):
       A string that represents the path and file name for the output export file.
       
         data_frame{Object}:
       A variable that references a DataFrame object. Use the string/constant
       "PAGE_LAYOUT" to export the map document's page layout instead of an
       individual data frame.
       
         df_export_width{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         df_export_height{Integer}:
       A number that defines the width of the export image in pixels for a data
       frame export. df_export_width is only used when exporting a data frame.
       Exporting a page layout uses the map document page width instead of
       df_export_width .
       
         resolution{Integer}:
       A number that defines the resolution of the export file in DPI (dots per
       inch).
       
         world_file{Boolean}:
       If set to True , a georeferenced world file is created. The file contains
       pixel scale information and real-world coordinate information.
       
         color_mode{String}:
       This value specifies the number of bits used to describe color.
       
        * 24-BIT_TRUE_COLOR:   24-bit true color.
       
        * 8-BIT_PALETTE:   8-bit palette.
       
        * 8-BIT_GRAYSCALE:   8-bit grayscale.
       
        * 1-BIT_MONOCHROME_MASK:   1-bit monochrome mask.
       
        * 1-BIT_MONOCHROME_THRESHOLD:   1-bit monochrome threshold.
       
         tiff_compression{String}:
       This value represents a compression scheme.
       
        * DEFLATE:   A lossless data compression.
       
        * JPEG:   JPEG compression.
       
        * LZW:   Lempel-Ziv-Welch, a lossless data compression.
       
        * NONE:   Compression is not applied.
       
        * PACK_BITS:   Pack bits compression.
       
         geoTIFF_tags{Boolean}:
       If set to True , georeferencing tags are included in the structure of the
       TIFF export file. The tags contain pixel scale information and real-world
       coordinate information. These tags can be read by applications that support
       GeoTIFF format."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((out_tiff, df_export_width, df_export_height, resolution, world_file, color_mode, tiff_compression, geoTIFF_tags))
    layout.exportToTIFF(*args)
@constants.maskargs
def InsertLayer(data_frame, reference_layer, insert_layer, insert_position='BEFORE'):
    """InsertLayer(data_frame, reference_layer, insert_layer, {insert_position})
       Provides the ability to insert a layer at a specific location within a data
       frame or within a group layer in a map document ( .mxd ).
       
         data_frame(DataFrame):
       A reference to a DataFrame object into which the new layer will be
       inserted.
       
         reference_layer(Layer):
       A Layer object representing an existing layer that determines the location
       where the new layer will be inserted.
       
         insert_layer(Layer):
       A reference to a Layer object representing the layer to be inserted.
       
         insert_position{String}:
       A constant that determines the placement of the added layer relative to the
       reference layer.
       
        * AFTER: Inserts the new layer after or below the reference layer
       
        * BEFORE: Inserts the new layer before or above the reference layer"""
    def insertlayer(df, target_container, insert_layer, reference_layer, insert_position):
        if getattr(target_container, 'layers', None):
            layerlist = target_container.layers
            if reference_layer in target_container.layers:
                index = layerlist.index(reference_layer) + 1
                if insert_position.upper() == 'BEFORE':
                    index -= 1
                df.InsertLayer(target_container, insert_layer.copy(), index)
                return True
            else:
                return any(insertlayer(df, child, insert_layer, reference_layer, insert_position)
                           for child in target_container.layers)
        else:
            return False
    from ._mapping import DataFrame, Layer
    assert isinstance(data_frame, DataFrame)
    assert isinstance(insert_layer, Layer)
    assert isinstance(reference_layer, Layer)
    tc = data_frame._arc_object
    il = insert_layer._arc_object
    rl = reference_layer._arc_object
    if not insertlayer(tc, tc, il, rl, insert_position):
        raise Exception('Could not find reference layer')
def ListBookmarks(map_document, wildcard=None, data_frame=None):
    """ListBookmarks(map_document, {wildcard}, {data_frame})
       Returns a Python list of named tuples that provide access to each spatial
       bookmark's name and extent.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results. It is used to filter spatial bookmark names.
       
         data_frame{DataFrame}:
       A variable that references a DataFrame object.  This is used to find a
       spatial bookmark associated with a specific data frame."""
    from arcpy._mapping import MapDocument, DataFrame
    from arcpy.arcobjects.mixins import bookmark_tuple
    from arcpy.geoprocessing import gp
    from operator import add
    assert isinstance(map_document, MapDocument)
    if data_frame:
        assert isinstance(data_frame, DataFrame)
    dfs = (map_document._arc_object.pagelayout.dataframes
               if not data_frame
               else [data_frame._arc_object])
    bmarks1 = [[bookmark_tuple(*bmark) for bmark in data_frame.bookmarks]
               for data_frame in dfs]
    bookmarks = reduce(add, bmarks1, [])
    if wildcard:
        bookmarks = [b for b in bookmarks if gp.wildcardMatch(wildcard, b.name)]
    return bookmarks
@constants.maskargs
def ListBrokenDataSources(map_document_or_layer):
    """ListBrokenDataSources(map_document_or_layer)
       Returns a Python list of Layer objects within a  map document ( .mxd ) or
       layer ( .lyr ) file that have broken connections to their original source
       data.
       
         map_document_or_layer(Object):
       A variable that references a MapDocument or Layer object."""
    if isinstance(map_document_or_layer, Layer):
      result = mixins.LayerDocumentMixin(map_document_or_layer).listBrokenDataSources()
    else:
      result = mixins.MapDocumentMixin(map_document_or_layer).listBrokenDataSources()
    return result
@constants.maskargs
def ListDataFrames(map_document, wildcard=None):
    """ListDataFrames(map_document, {wildcard})
       Returns a Python list of DataFrame objects that exist within a single map
       document ( .mxd ).
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results."""
    result = mixins.MapDocumentMixin(map_document).listDataFrames(wildcard)
    return result
@constants.maskargs
def ListLayers(map_document_or_layer, wildcard=None, data_frame=None):
    """ListLayers(map_document_or_layer, {wildcard}, {data_frame})
       Returns a Python list of Layer objects that exist within a  map document (
       .mxd ), a  data frame within a map document, or layers within a layer (
       .lyr ) file.
       
         map_document_or_layer(Object):
       A variable that references a MapDocument or Layer object.
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results.
       
         data_frame{DataFrame}:
       A variable that references a DataFrame object."""
    if isinstance(map_document_or_layer, Layer):
      result = mixins.LayerDocumentMixin(map_document_or_layer).listLayers(wildcard, data_frame)
    else:
      result = mixins.MapDocumentMixin(map_document_or_layer).listLayers(wildcard, data_frame)
    return result
@constants.maskargs
def ListLayoutElements(map_document, element_type='', wildcard=None):
    """ListLayoutElements(map_document, {element_type}, {wildcard})
       Returns a Python list of layout elements  that exist within a  map document
       ( .mxd ) layout.
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         element_type{String}:
       A string that represents the element type that will be used to filter the
       returned list of elements.
       
        * DATAFRAME_ELEMENT:   Dataframe element
       
        * GRAPHIC_ELEMENT:   Graphic element
       
        * LEGEND_ELEMENT:   Legend element
       
        * MAPSURROUND_ELEMENT:   Mapsurround element
       
        * PICTURE_ELEMENT:   Picture element
       
        * TEXT_ELEMENT:   Text element
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results."""
    result = mixins.MapDocumentMixin(map_document).listLayoutElements(element_type, wildcard)
    return result
def ListMapServices(connection_url_or_name, server, connection_username=None, connection_password=None, connection_domain=None):
    """ListMapServices(connection_url_or_name, server, {connection_username}, {connection_password}, {connection_domain})
       This method has been deprecated starting at ArcGIS 10.1 for Server and
       ArcGIS  10.1 for Desktop and will return a runtime error. Please consult
       the ArcGIS documentation for the usage of the new ArcGIS for Server
       Administrator API .
       
       Lists the names of map services for a designated ArcGIS for Server .
       
         connection_url_or_name(String):
       A string that represents the URL of the ArcGIS for Server to which you want
       to get a list of services.
       
         server(String):
       A string that represents the ArcGIS for Server host name.
       
         connection_username{String}:
       A string that represents a user name used to connect to the ArcGIS for
       Server . In order to get a list of map services this user name should be a
       member of the ArcGIS for Server admin group. This variable is only
       necessary when connecting to a UNIX/Linux ArcGIS for Server .
       
         connection_password{String}:
       A string that represents a password used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server .
       
         connection_domain{String}:
       A string that represents a domain name used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server ."""
    from arcpy import GetIDMessage
    raise Exception(GetIDMessage(88014, 'This method has been deprecated. Please consult the help for the usage of the new ArcGIS Server APIs.'))
def ListPrinterNames():
    """ListPrinterNames()
       
       Returns a Python list of available printers on the local computer."""
    from arcpy.geoprocessing import gp
    return gp.listPrinterNames()
def ListStyleItems(style_file_path, style_folder_name, wildcard=None):
    """ListStyleItems(style_file_path, style_folder_name, {wildcard})
       Returns a Python list of StyleItem objects.  A referenced legend item from
       a style file ( .style or .ServerStyle ) can then be used to update already
       existing legend items in a layout.
       
         style_file_path(String):
       A full path to an existing style  ( .style ) or server style ( .ServerStyle
       ) file.
       
       There are two additional shortcuts that don't require a full path.  First,
       type the name of the ArcGIS system style file, for example, "ESRI.style" or
       "ESRI.ServerStyle" or "Transportation.style" .   The function will
       automatically search for the style in the appropriate ArcGIS  installation
       style folder.  Second, with ArcGIS for Desktop installations, you can use
       the keyword "USER_STYLE" .  This will automatically search the local user
       profile rather than requiring the full path.  If the style file does not
       exist in either of these two known system locations, then the full path
       including the file extension must be provided, for example,
       "C:/Project/CustomStyles.style" .
       
         style_folder_name(String):
       The name of the style folder in the style file the way it appears in the
       Style manager window.  Currently, only Legend Items can be used with other
       arcpy.mapping methods.
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results based on the style item name property."""
    import arcgisscripting
    return convertArcObjectToPythonObject(arcgisscripting._listStyleItems(*gp_fixargs([style_file_path, style_folder_name, wildcard], True, False)))
@constants.maskargs
def ListTableViews(map_document, wildcard=None, data_frame=None):
    """ListTableViews(map_document, {wildcard}, {data_frame})
       Returns a Python list of TableView objects that exist within a  map
       document ( .mxd ).
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         wildcard{String}:
       A combination of asterisks (*) and characters can be used to help limit the
       results.
       
         data_frame{DataFrame}:
       A variable that references a DataFrame object."""
    result = mixins.MapDocumentMixin(map_document).listTableViews(wildcard, data_frame)
    return result
@constants.maskargs
def MoveLayer(data_frame, reference_layer, move_layer, insert_position='BEFORE'):
    """MoveLayer(data_frame, reference_layer, move_layer, {insert_position})
       Provides the ability to move a layer to a specific location within a data
       frame or group layer in a map document ( .mxd ).
       
         data_frame(DataFrame):
       A reference to a DataFrame object within which the layer will be moved.
       
         reference_layer(Layer):
       A reference to a Layer object representing an existing layer that
       determines the location in relation to where the layer will be moved.
       
         move_layer(Layer):
       A reference to a Layer object representing the layer to be moved.
       
         insert_position{String}:
       A constant that determines the placement of the moved layer relative to the
       referenced layer.
       
        * AFTER: Inserts the new layer after or below the referenced layer
       
        * BEFORE: Inserts the new layer before or above the referenced layer"""
    def findcontaininglayer(container, layer):
        if layer in getattr(container, 'layers', []):
            return container
        else:
            for lyr in getattr(container, 'layers', []):
                retval = findcontaininglayer(lyr, layer)
                if retval is not None:
                    return retval
            return None
    from ._mapping import DataFrame, Layer
    assert isinstance(data_frame, DataFrame)
    assert isinstance(move_layer, Layer)
    assert isinstance(reference_layer, Layer)
    tc = data_frame._arc_object
    ml = move_layer._arc_object
    rl = reference_layer._arc_object
    move_c = findcontaininglayer(tc, ml)
    refe_c = findcontaininglayer(tc, rl)
    assert move_c is not None, 'Did not find move layer.'
    assert refe_c is not None, 'Did not find reference layer.'
    RemoveLayer(data_frame, move_layer)
    InsertLayer(data_frame, reference_layer, move_layer, insert_position)
def PDFDocumentCreate(pdf_path):
    """PDFDocumentCreate(pdf_path)
       Creates an empty PDFDocument object in memory.
       
         pdf_path(String):
       A string that specifies the  path and file name for the resulting PDF file
       when the saveAndClose method is called."""
    import arcpy
    from arcpy.geoprocessing import gp
    from arcpy.geoprocessing import env
    from arcpy._mapping import PDFDocument
    if os.path.exists(pdf_path):
        # respect overwriteoutput and delete before re-creating.
        if env.overwriteOutput:
            os.unlink(pdf_path)
        else:
            raise ValueError(gp.getIDMessage(89000, 'File %r already exists!') % pdf_path) #'File %r already exists!'
    return PDFDocument(pdf_path)
def PDFDocumentOpen(pdf_path, user_password=None, master_password=None):
    """PDFDocumentOpen(pdf_path, {user_password}, {master_password})
       Returns a PDFDocument object  (the contents of the object come from a PDF
       file on disk, and subsequent operations followed by a call to saveAndClose
       will modify the original PDF file).
       
         pdf_path(String):
       A string that specifies the path and file name of the PDF file to open.
       
         user_password{String}:
       A string that specifies the user password.  User passwords are typically
       used to restrict opening and specific master-defined operations for a PDF
       file.
       
         master_password{String}:
       A string that specifies the master password. Master passwords are typically
       used to restrict setting of user permissions for a PDF file."""
    from arcpy._mapping import PDFDocument
    if not os.path.exists(pdf_path):
        from arcpy.geoprocessing import gp
        raise IOError(gp.getIDMessage(89013, 'PDF file does not exist'))
    return PDFDocument(pdf_path, user_password, master_password)
@constants.maskargs
def PrintMap(map_document, printer_name=None, data_frame='PAGE_LAYOUT', out_print_file=None, image_quality=None):
    """PrintMap(map_document, {printer_name}, {data_frame}, {out_print_file}, {image_quality})
       Prints a specific data frame or a map document ( .mxd ) layout to a printer
       or file
       
         map_document(MapDocument):
       A variable that references a MapDocument object.
       
         printer_name{String}:
       A string that represents the name of a printer on the local computer.
       
         data_frame{DataFrame}:
       A variable that references a DataFrame object.
       
         out_print_file{String}:
       A path that includes the name of an output print file. The format created
       is dependent on the printer. If you are using a postscript printer, the
       format will be postscript, and it is recommended that a .ps extension be
       provided; if you are using a Windows printer, use a .prn extension.
       
         image_quality{String}:
       A string that defines output image quality, the draw resolution of map
       layers that draw as rasters. Using the default value of "None" will cause
       the function to use the image quality saved in the map document.
       
        * BEST:  An output image quality resample ratio of 1.
       
        * BETTER:  An output image quality resample ratio of 2.
       
        * NORMAL:  An output image quality resample ratio of 3.
       
        * FASTER:  An output image quality resample ratio of 4.
       
        * FASTEST:  An output image quality resample ratio of 5."""
    from .geoprocessing._base import gp_fixargs
    from ._mapping import MapDocument, DataFrame
    assert isinstance(map_document, MapDocument)
    mapdoc = mixins.MapDocumentMixin(map_document)
    if data_frame:
        assert isinstance(data_frame, DataFrame) or (isinstance(data_frame, basestring) and data_frame.lower() == 'page_layout')
        if isinstance(data_frame, basestring):
            data_frame = None
    layout = data_frame._arc_object if data_frame else mapdoc
    args = gp_fixargs((printer_name, out_print_file, image_quality))
    layout.printMap(*args)
@constants.maskargs
def PublishMSDToServer(msd_path, connection_url_or_name, server, service_name, folder_name="", service_capabilities="", connection_username=None, connection_password=None, connection_domain=None):
    """PublishMSDToServer(msd_path, connection_url_or_name, server, service_name, {folder_name}, {service_capabilities}, {connection_username}, {connection_password}, {connection_domain})
       Starting at ArcGIS 10.1 for Server , Map Server Definition ( .msd ) files
       have been replaced with Service Definition Draft ( .sddraft ) and Service
       Definition ( .sd ) files. Please use  the Upload Service Definition
       Geoprocessing tool  instead.
       
       Publishes an existing map service definition (MSD) file to a designated
       ArcGIS for Server .
       
         msd_path(String):
       A string that represents the path and name of an existing MXD document you
       want to serve.
       
         connection_url_or_name(String):
       A string that represents the URL of the ArcGIS for Server to which you want
       to publish the MSD.
       
         server(String):
       A string that represents the ArcGIS for Server host name to which you want
       to publish the MSD.
       
         service_name(String):
       A string that represents the name of the service. This is the name people
       will see and use to identify the service. The name can only contain
       alphanumeric characters and underscores. No spaces or special characters
       are allowed. The name cannot be more than 120 characters in length.
       
         folder_name{String}:
       A string that represents  a folder name to which you want to publish the
       MSD. If the folder does not currently exist, it will be created.  The
       default folder is the server root level.
       
         service_capabilities{String}:
       A list of strings that represents additional capabilities in addition to
       the map service capability.
       
        * MAPPING: The default ArcGIS for Server capability
       
        * KML: Keyhole Markup Language
       
        * WCS: Web Coverage Service
       
        * WFS: Web Feature Service
       
        * WMS: Web Map Service
       
         connection_username{String}:
       A string that represents a user name used to connect to the ArcGIS for
       Server . To publish a map service, this user name should be a member of the
       ArcGIS for Server admin group. This variable is only necessary when
       connecting to a UNIX/Linux ArcGIS for Server .
       
         connection_password{String}:
       A string that represents a password used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server .
       
         connection_domain{String}:
       A string that represents a domain name used to connect to the ArcGIS for
       Server . This variable is only necessary when connecting to a UNIX/Linux
       ArcGIS for Server ."""
    from arcpy import GetIDMessage
    raise Exception(GetIDMessage(88014, 'This method has been deprecated. Please consult the help for the usage of the new ArcGIS Server APIs.'))
@constants.maskargs
def RemoveLayer(data_frame, remove_layer):
    """RemoveLayer(data_frame, remove_layer)
       Provides the ability to remove a layer within a data frame in a map
       document ( .mxd ).
       
         data_frame(DataFrame):
       A reference to a DataFrame object that contains the layer to be removed.
       
         remove_layer(Layer):
       A reference to a Layer object representing the layer to be removed."""
    from ._mapping import DataFrame, Layer
    assert isinstance(data_frame, DataFrame)
    assert isinstance(remove_layer, Layer)
    tc = data_frame._arc_object
    rl = remove_layer._arc_object
    tc.RemoveLayer(rl)
@constants.maskargs
def RemoveTableView(data_frame, remove_table):
    """RemoveTableView(data_frame, remove_table)
       Provides the ability to remove a table within a data frame in a map
       document ( .mxd ).
       
         data_frame(DataFrame):
       A reference to a DataFrame object that contains the layer to be removed.
       
         remove_table(TableView):
       A reference to a Layer object representing the layer to be removed."""
    from ._mapping import DataFrame, TableView
    assert isinstance(data_frame, DataFrame)
    assert isinstance(remove_table, TableView)
    tc = data_frame._arc_object
    rl = remove_table._arc_object
    tc.RemoveTableView(rl)
@constants.maskargs
def UpdateLayer(data_frame, update_layer, source_layer, symbology_only=True):
    """UpdateLayer(data_frame, update_layer, source_layer, {symbology_only})
       Provides the ability to update all layer properties or just the symbology
       for a layer in a map document ( .mxd ) by extracting the information from a
       source layer.
       
         data_frame(DataFrame):
       A reference to a DataFrame object that contains the layer to be updated.
       
         update_layer(Layer):
       A Layer object representing an existing layer that will be updated.
       
         source_layer(Layer):
       A reference to a Layer object that contains the information to be applied
       to the update_layer.
       
         symbology_only{Boolean}:
       A Boolean that determines whether or not to update only the layer's
       symbology, or all other properties as well. If set to True , only the
       layer's symbology will be updated."""
    from ._mapping import DataFrame, Layer
    assert isinstance(update_layer, Layer)
    assert isinstance(source_layer, Layer)
    assert isinstance(data_frame, DataFrame)
    tl = update_layer._arc_object
    rl = source_layer._arc_object
    tc = data_frame._arc_object
    if not symbology_only:
        tc.ReplaceLayer(tl, rl)
    else:
        tl._update(rl, symbology_only)
@constants.maskargs
def UpdateLayerTime(data_frame, update_layer, source_layer):
    """UpdateLayerTime(data_frame, update_layer, source_layer)
       Provides the ability to update a layer's  time properties for a layer in a
       map document ( .mxd ) by extracting time properties from a source layer.
       
         data_frame(DataFrame):
       A reference to a DataFrame object that contains the layer to be updated.
       
         update_layer(Layer):
       A Layer object representing an existing layer that will be updated.
       
         source_layer(Layer):
       A reference to a Layer object that contains the information to be applied
       to the update_layer."""
    tl = update_layer._arc_object
    rl = source_layer._arc_object
    tl._updatetime(rl)
