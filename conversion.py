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
"""The Conversion toolbox contains tools that convert data between various formats."""
__all__ = ['ImportCoverageAnnotation', 'ImportCADAnnotation', 'RasterToASCII', 'RasterToFloat', 'RasterToPoint', 'RasterToPolygon', 'RasterToPolyline', 'FeatureClassToGeodatabase', 'RasterToGeodatabase', 'TableToGeodatabase', 'ASCIIToRaster', 'DEMToRaster', 'FeatureToRaster', 'FloatToRaster', 'FeatureClassToShapefile', 'TableToDBASE', 'FeatureclassToCoverage', 'FeatureClassToFeatureClass', 'TableToTable', 'ESRITranslator', 'USGSMPTranslator', 'XSLTransform', 'MDPublisher', 'PointToRaster', 'PolygonToRaster', 'PolylineToRaster', 'MetadataImporter', 'AddCADFields', 'ExportCAD', 'RasterToVideo', 'RasterToOtherFormat', 'SynchronizeMetadata', 'XMLSchemaValidator', 'ImportMetadata', 'MultipatchToCollada', 'ImportFromE00', 'ValidateMetadata', 'ValidateMetadataMultiple', 'ExportMetadataMultiple', 'ExportMetadata', 'WFSToFeatureClass', 'CADToGeodatabase', 'GPXtoFeatures', 'LasDatasetToRaster', 'TableToExcel', 'ExcelToTable', 'FeaturesToJSON', 'JSONToFeatures', 'MultipatchToRaster', 'UpgradeMetadata', 'CopyRuntimeGdbToFileGdb', 'PDFToTIFF', 'KMLToLayer', 'LayerToKML', 'MapToKML']
__alias__ = u'conversion'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Excel toolset
@gptooldoc('ExcelToTable_conversion', None)
def ExcelToTable(Input_Excel_File=None, Output_Table=None, Sheet=None):
    """ExcelToTable_conversion(Input_Excel_File, Output_Table, {Sheet})

        Converts Microsoft Excel files into a table.

     INPUTS:
      Input_Excel_File (File):
          The Microsoft Excel file to convert.
      Sheet {String}:
          The name of the particular sheet within the Excel file to import. If
          unspecified, the first sheet in the workbook will be used by default.

     OUTPUTS:
      Output_Table (Table):
          The output table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExcelToTable_conversion(*gp_fixargs((Input_Excel_File, Output_Table, Sheet), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToExcel_conversion', None)
def TableToExcel(Input_Table=None, Output_Excel_File=None, Use_field_alias_as_column_header=None, Use_domain_and_subtype_description=None):
    """TableToExcel_conversion(Input_Table, Output_Excel_File, {Use_field_alias_as_column_header}, {Use_domain_and_subtype_description})

        Converts a table to a Microsoft Excel file.

     INPUTS:
      Input_Table (Table View):
          The table to be converted to Microsoft Excel format.
      Use_field_alias_as_column_header {Boolean}:
          How column names in the output are determined.

          * NAME—Column headers will be set using the input's field names. This is the
          default.

          * ALIAS—Column headers will be set using the input's field aliases.
      Use_domain_and_subtype_description {Boolean}:
          Controls how values from subtype fields or fields with a coded value domain are
          transferred to the output.

          * CODE—All field values will be used as they are stored in the table. This is
          the default.

          * DESCRIPTION—For subtype fields, the subtype description will be used. For
          fields with a coded value domain, the coded value descriptions will be used.

     OUTPUTS:
      Output_Excel_File (File):
          The output Microsoft Excel file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToExcel_conversion(*gp_fixargs((Input_Table, Output_Excel_File, Use_field_alias_as_column_header, Use_domain_and_subtype_description), True)))
        return retval
    except Exception, e:
        raise e


# From GPS toolset
@gptooldoc('GPXtoFeatures_conversion', None)
def GPXtoFeatures(Input_GPX_File=None, Output_Feature_class=None):
    """GPXtoFeatures_conversion(Input_GPX_File, Output_Feature_class)

        Converts GPX files into features.

     INPUTS:
      Input_GPX_File (File):
          The GPX file to convert.

     OUTPUTS:
      Output_Feature_class (Feature Class):
          The feature class to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GPXtoFeatures_conversion(*gp_fixargs((Input_GPX_File, Output_Feature_class), True)))
        return retval
    except Exception, e:
        raise e


# From KML toolset
@gptooldoc('KMLToLayer_conversion', None)
def KMLToLayer(in_kml_file=None, output_folder=None, output_data=None, include_groundoverlay=None):
    """KMLToLayer_conversion(in_kml_file, output_folder, {output_data}, {include_groundoverlay})

        Converts a KML or KMZ file into feature classes and a layer file. The layer
        file maintains the symbology found within the original KML or KMZ file.

     INPUTS:
      in_kml_file (File):
          The KML or KMZ file to translate.
      output_folder (Folder):
          The destination folder for the file geodatabase and layer (.lyr) file.
      output_data {String}:
          The name of the output file geodatabase and layer file. The default is the name
          of the input KML file.
      include_groundoverlay {Boolean}:
          Include ground overlay (raster, air photos, and so on). Use caution if the KMZ
          points to a service that serves raster imagery. The tool will attempt to
          translate the raster imagery at all available scales. This process could be
          lengthy and possibly overwhelm the service.

          * GROUNDOVERLAY—Ground overlays are included in the output.

          * NO_GROUNDOVERLAY—Ground overlays are not included in the output. This is the
          default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.KMLToLayer_conversion(*gp_fixargs((in_kml_file, output_folder, output_data, include_groundoverlay), True)))
        return retval
    except Exception, e:
        raise e


# From PDF toolset
@gptooldoc('PDFToTIFF_conversion', None)
def PDFToTIFF(in_pdf_file=None, out_tiff_file=None, pdf_password=None, pdf_page_number=None, pdf_map=None, clip_option=None, resolution=None, color_mode=None, tiff_compression=None, geotiff_tags=None):
    """PDFToTIFF_conversion(in_pdf_file, out_tiff_file, {pdf_password}, {pdf_page_number}, {pdf_map}, {clip_option}, {resolution}, {color_mode}, {tiff_compression}, {geotiff_tags})

        Exports an existing PDF file to a Tagged Image File Format (TIFF). If the PDF
        has georeference information, the TIFF can be a GeoTIFF. These TIFFs can be used
        as a source for heads-up digitizing and viewing in ArcMap. Both GeoPDF and ISO
        standards of georeferenced PDFs are supported.

     INPUTS:
      in_pdf_file (File):
          The path and name of the PDF file that is going to be converted into a TIFF.
      pdf_password {Encrypted String}:
          If the PDF is password protected the tool requires an appropriate password for
          processing. Different passwords can be provided based on the security setting
          embedded in the PDF. If the PDF is protected by restricting access to

          * Open the document—enter the PDF open password.

          * Copy contents—enter the PDF file's permission password.

          * Open and to copy contents—enter the PDF file's permission password.
      pdf_page_number {Long}:
          The page number containing the content you want to export to TIFF. You can only
          enter one page, not a range of pages.
      pdf_map {String}:
          In a PDF file, a map is a defined container of graphics on the PDF page that has
          a spatial reference. A PDF map is equivalent to an ArcMap data frame in that it
          is the container for spatial data. A PDF may have one or more maps. For example,
          a page may have a main map and an additional smaller overview or key map.The PDF
          Map is used for setting the output spatial reference of the TIFF, if the
          Write GeoTIFF Tags setting is enabled.The PDF Map is also used to define the
          extent of the output TIFF, if the Clip
          Output to Map option is enabled.You can specify the map you wish to use by name.
          You can also use LARGEST to use
          the largest map in the PDF. This will also be the default if the parameter is
          not specified.When entering the map's name, replace any spaces with an
          underscore. For
          example, My Map becomes My_Map.
      clip_option {Boolean}:
          Specifies what should be clipped/extracted.

          * CLIP_TO_MAP—Only extracts the map you choose in the pdf_map parameter.

          * NO_CLIP—Converts the entire page you specified into a TIFF. This is the
          default.
      resolution {Long}:
          A number that defines the resolution of the exported TIFF in DPI (dots per
          inch). The default is 250.
      color_mode {String}:
          This value specifies the number of bits used to describe color. The default is
          RGB_TRUE_COLOR.

          *  RGB_TRUE_COLOR—32-bit RGBA color. When you choose this option with the JPEG
          compression, it will produce a 24-bit RGB color.

          *  CMYK_TRUE_COLOR—32-bit CMYK color.

          * RGB_PALETTE—8-bit RGB palette.
      tiff_compression {String}:
          The compression scheme for the output TIFF. The default is LZW.

          * LZW—Lempel-Ziv-Welch, a lossless data compression.

          * DEFLATE —A lossless data compression.

          * JPEG —JPEG lossy compression. Quality setting is 100 and cannot be changed.

          * NONE—Compression is not applied.

          * PACK_BITS—Pack bits lossless compression.
      geotiff_tags {Boolean}:
          If the PDF contains a spatial reference, you can choose to add GeoTIFF tags.

          * GEOTIFF_TAGS—Adds GeoTIFF tags to the output unless the PDF has no spatial
          reference. This is the default.

          * NO_GEOTIFF_TAGS—Does not add GeoTIFF tags, even if the PDF contains a spatial
          reference.

     OUTPUTS:
      out_tiff_file (Raster Dataset):
          The path and name of the output TIFF file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PDFToTIFF_conversion(*gp_fixargs((in_pdf_file, out_tiff_file, pdf_password, pdf_page_number, pdf_map, clip_option, resolution, color_mode, tiff_compression, geotiff_tags), True)))
        return retval
    except Exception, e:
        raise e


# From Raster toolset
@gptooldoc('RasterToASCII_conversion', None)
def RasterToASCII(in_raster=None, out_ascii_file=None):
    """RasterToASCII_conversion(in_raster, out_ascii_file)

        Converts a raster dataset to an ASCII text file representing raster data.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point type.

     OUTPUTS:
      out_ascii_file (File):
          The output ASCII raster file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToASCII_conversion(*gp_fixargs((in_raster, out_ascii_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToFloat_conversion', None)
def RasterToFloat(in_raster=None, out_float_file=None):
    """RasterToFloat_conversion(in_raster, out_float_file)

        Converts a raster dataset to a file of binary floating-point values representing
        raster data.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point type.

     OUTPUTS:
      out_float_file (File):
          The output floating-point raster file.The file name must have a .flt extension."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToFloat_conversion(*gp_fixargs((in_raster, out_float_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToPoint_conversion', None)
def RasterToPoint(in_raster=None, out_point_features=None, raster_field=None):
    """RasterToPoint_conversion(in_raster, out_point_features, {raster_field})

        Converts a raster dataset to point features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster can be integer or floating-point type.
      raster_field {Field}:
          The field to assign values from the cells in the input raster to the points in
          the output dataset.It can be an integer, floating point, or string field.

     OUTPUTS:
      out_point_features (Feature Class):
          The output feature class that will contain the converted points."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToPoint_conversion(*gp_fixargs((in_raster, out_point_features, raster_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToPolygon_conversion', None)
def RasterToPolygon(in_raster=None, out_polygon_features=None, simplify=None, raster_field=None):
    """RasterToPolygon_conversion(in_raster, out_polygon_features, {simplify}, {raster_field})

        Converts a raster dataset to polygon features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster must be integer type.
      simplify {Boolean}:
          Determines if the output polygons will be smoothed into simpler shapes or
          conform to the input raster's cell edges.

          * SIMPLIFY—The polygons will be smoothed into simpler shapes. The smoothing is
          done in such a way that the polygons contain a minimum number of segments while
          remaining as close as possible the original raster cell edges. This is the
          default.

          * NO_SIMPLIFY—The edge of the polygons will conform exactly to the input
          raster's cell edges. With this option, converting the resulting polygon feature
          class back to a raster would produce a raster the same as the original.
      raster_field {Field}:
          The field used to assign values from the cells in the input raster to the
          polygons in the output dataset.It can be an integer or a string field.

     OUTPUTS:
      out_polygon_features (Feature Class):
          The output feature class that will contain the converted polygons."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToPolygon_conversion(*gp_fixargs((in_raster, out_polygon_features, simplify, raster_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToPolyline_conversion', None)
def RasterToPolyline(in_raster=None, out_polyline_features=None, background_value=None, minimum_dangle_length=None, simplify=None, raster_field=None):
    """RasterToPolyline_conversion(in_raster, out_polyline_features, {background_value}, {minimum_dangle_length}, {simplify}, {raster_field})

        Converts a raster dataset to polyline features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster must be integer type.
      background_value {String}:
          Specifies the value that will identify the background cells. The raster dataset
          is viewed as a set of foreground cells and background cells. The linear features
          are formed from the foreground cells.

          * ZERO—The background is composed of cells of zero or less or NoData. All cells
          with a value greater than zero are considered a foreground value.

          * NODATA—The background is composed of NoData cells. All cells with valid values
          belong to the foreground.
      minimum_dangle_length {Double}:
          Minimum length of dangling polylines that will be retained. The default is zero.
      simplify {Boolean}:
          Simplifies a line by removing small fluctuations or extraneous bends from it
          while preserving its essential shape.

          * SIMPLIFY—The polylines will be simplified into simpler shapes such that each
          contains a minimum number of segments. This is the default.

          * NO_SIMPLIFY—The polylines will not be simplified.
      raster_field {Field}:
          The field used to assign values from the cells in the input raster to the
          polyline features in the output dataset.It can be an integer or a string field.

     OUTPUTS:
      out_polyline_features (Feature Class):
          The output feature class that will contain the converted polylines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToPolyline_conversion(*gp_fixargs((in_raster, out_polyline_features, background_value, minimum_dangle_length, simplify, raster_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToVideo_conversion', None)
def RasterToVideo(input_folder=None, out_video_file=None, image_format=None, codec=None, duration_method=None, time=None, quality=None):
    """RasterToVideo_conversion(input_folder, out_video_file, {image_format}, {codec}, {duration_method}, {time}, {quality})

        Creates a video file from a set of images.

     INPUTS:
      input_folder (Folder):
          The folder containing the images. The images in the folder should be of the
          same type (BMP or JPEG).
      image_format {String}:
          The format of the images files in the folder. The output video will be created
          using the images of the chosen format.

          * BMP— Windows Bitmap (*.bmp)

          * JPG—JPEG (*.jpg)
      codec {String}:
          The codec used for compressing the frames while writing the video file. The
          list of codecs can vary on different machines.
      duration_method {String}:
          The method to be used for defining the output video duration.

          * FRAME_RATE— Defines the duration of the output video based on the number of
          frames per second

          * TIME— Defines the duration of the output video in seconds
      time {Double}:
          Duration of the video to be output.
      quality {Long}:
          The quality of the output video. The video can be exported at different
          qualities ranging from 1 to 100. The default value is 100.

     OUTPUTS:
      out_video_file (File):
          The output video file (*.avi or *.mov)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToVideo_conversion(*gp_fixargs((input_folder, out_video_file, image_format, codec, duration_method, time, quality), True)))
        return retval
    except Exception, e:
        raise e


# From WFS toolset
@gptooldoc('WFSToFeatureClass_conversion', None)
def WFSToFeatureClass(input_WFS_server=None, WFS_feature_type=None, out_path=None, out_name=None):
    """WFSToFeatureClass_conversion(input_WFS_server, WFS_feature_type, out_path, out_name)

        Imports a feature type from a web feature service (WFS) to a feature class in a
        geodatabase.

     INPUTS:
      input_WFS_server (String):
          The URL of the source WFS service.
      WFS_feature_type (String):
          The name of the feature type to extract from the input WFS service.
      out_path (Workspace / Feature Dataset):
          The output location can be the root level of a geodatabase or a feature dataset
          within a geodatabase. If the output location is a feature dataset, the
          coordinates are converted from the source coordinate system to the coordinate
          system of the feature dataset.
      out_name (String):
          The name of the feature class to create within the output location. If the
          feature class name already exists in the geodatabase, the name will be auto-
          incremented. By default, the feature type name is used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.WFSToFeatureClass_conversion(*gp_fixargs((input_WFS_server, WFS_feature_type, out_path, out_name), True)))
        return retval
    except Exception, e:
        raise e


# JSON toolset
@gptooldoc('FeaturesToJSON_conversion', None)
def FeaturesToJSON(in_features=None, out_json_file=None, format_json=None, include_z_values=None, include_m_values=None):
    """FeaturesToJSON_conversion(in_features, out_json_file, {format_json}, {include_z_values}, {include_m_values})

        Converts features to JSON format. The fields, geometry, and spatial reference
        of features will be converted to their corresponding JSON representation and
        written to a file with a .json extension.

     INPUTS:
      in_features (Feature Layer):
          The features to convert to JSON.
      format_json {Boolean}:
          The JSON can be formatted to improve human readability similar to ArcGIS REST
          API specification's PJSON (Pretty JSON) format.

          * NOT_FORMATTED— The features will not be formatted. This is the default.

          * FORMATTED—The features will be formatted to improve human readability.
      include_z_values {Boolean}:
          Include Z value of the features to the JSON.

          * NO_Z_VALUES— The Z values will not be included in geometries and the hasZ
          property of the JSON will not be included. This is the default.

          * Z_VALUES—The Z values will be included in geometries and the hasZ property of
          the JSON will be set to True.
      include_m_values {Boolean}:
          Include M value of the features to the JSON.

          * NO_M_VALUES— The M values will not be included in geometries and the hasM
          property of the JSON will not be included. This is the default.

          * M_VALUES—The M values will be included in geometries and the hasM property of
          the JSON will be set to True.

     OUTPUTS:
      out_json_file (File):
          The output JSON file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeaturesToJSON_conversion(*gp_fixargs((in_features, out_json_file, format_json, include_z_values, include_m_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('JSONToFeatures_conversion', None)
def JSONToFeatures(in_json_file=None, out_features=None):
    """JSONToFeatures_conversion(in_json_file, out_features)

        Converts JSON features based on ArcGIS REST API specification into a feature
        class. The feature class will have fields, geometry type, and spatial reference
        as defined in the JSON.

     INPUTS:
      in_json_file (File):
          The JSON file (.json) to convert.

     OUTPUTS:
      out_features (Feature Class):
          The output feature class to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.JSONToFeatures_conversion(*gp_fixargs((in_json_file, out_features), True)))
        return retval
    except Exception, e:
        raise e


# Metadata toolset
@gptooldoc('ESRITranslator_conversion', None)
def ESRITranslator(source=None, translator=None, output=None, logfile=None):
    """ESRITranslator_conversion(source, translator, {output}, {logfile})

        Uses the ArcGIS metadata translation engine or an XSLT transformation to export
        metadata content from ArcGIS to a stand-alone metadata XML file. The exported
        metadata will be formatted to satisfy the metadata standard associated with the
        specified translation.Metadata for items in ArcGIS is stored in the ArcGIS
        metadata format. Use the
        ArcGIS to translations to export ArcGIS metadata to another metadata XML format.
        For example, do this to share information outside of ArcGIS by publishing it to
        a metadata catalog. Different metadata catalogs accept information in different
        XML formats. ArcGIS metadata can be exported to different formats if you must
        publish your information to metadata catalogs with different requirements.When
        using a to ISO 19139 translation, the exported metadata will be formatted
        following the rules defined in ISO standard 19139, Geographic information —
        Metadata — XML schema implementation, and its associated XML Schemas. The same
        translation is used to export metadata according to an ISO metadata profile. The
        translation accounts for the metadata style selected in ArcGIS. For example,
        when the selected metadata style is North American Profile of ISO 19115:2003 –
        Geographic information – Metadata, the output file will be formatted
        appropriately for that ISO metadata profile.When using the ArcGIS to FGDC
        translation, the exported metadata will be
        formatted following the Federal Geographic Data Committee (FGDC) Content
        Standard for Digital Geospatial Metadata (CSDGM) XML format. The resulting file
        can be published to geodata.gov, for example.FGDC to translations handle
        information in the item's metadata which is
        formatted according to the FGDC CSDGM XML format. This content appears under the
        FGDC Metadata (read-only) heading in the Description tab when you are using a
        metadata style that gives you full access to the item's metadata. This content
        may have been provided with the current release of ArcGIS for Desktop using the
        FGDC metadata editor add-in or using the FGDC metadata editor provided with
        ArcGIS Desktop 9.3.1 or earlier releases.The to ArcGIS translations convert
        other metadata XML formats to the ArcGIS
        metadata format. This is an important step in the process of importing metadata
        that exists in another format to an ArcGIS item; however, several additional
        steps are also required to achieve the best results. Use the Import Metadata
        tool with the appropriate translation to complete this task instead.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be converted or a stand-alone XML file that will be
          converted.
      translator (File):
          An XML file that defines the conversion that will be performed.The translator
          files provided with ArcGIS for Desktop can be found in the
          <ArcGIS Installation Location>\Metadata\Translator folder. The following
          translators are provided:

          * ARCGIS2FGDC.xml—Translates content stored in the ArcGIS metadata format to the
          FGDC CSDGM XML format. This translator is used by default when you export
          metadata from the Description tab using the FGDC CSDGM Metadata style. Metadata
          is converted using an XSLT transformation and won't produce a log file.

          * ARCGIS2ISO19139.xml—Translates content stored in the ArcGIS metadata format to
          the ISO 19139 XML format. This translator is used by default when you export
          metadata from the Description tab using any of the ISO-based metadata styles. It
          is the preferred translator for exporting metadata to the ISO 19139 XML format.
          Metadata is converted using an XSLT transformation and won't produce a log file.

          * ESRI_ISO2ISO19139.xml—Translates content stored in either the ArcGIS metadata
          format or the ESRI-ISO metadata format to the ISO 19139 XML format. This
          translator is provided for backwards compatibility to support existing models
          and Python scripts. It has some known limitations with exporting metadata to the
          ISO 19139 XML format. Use the ARCGIS2ISO19139.xml translator instead. Metadata
          is converted using the Esri Metadata Translator tool's translation engine and
          produces a log file containing messages produced by the translation engine.

          * FGDC2ESRI_ISO.xml—Translates content stored in the FGDC CSDGM XML format to
          the ArcGIS metadata format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab. This
          translator is used when you import FGDC-formatted metadata by running the Import
          Metadata tool with the FROM_FGDC type and when you upgrade metadata by running
          the Upgrade Metadata tool with the FGDC_TO_ARCGIS type. Metadata is converted
          using the Esri Metadata Translator tool's translation engine and produces a log
          file containing messages produced by the translation engine.

          * FGDC2ISO19139.xml—Translates content stored in the FGDC CSDGM XML format to
          the ISO 19139 XML format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab.
          Metadata is converted using the Esri Metadata Translator tool's translation
          engine and produces a log file containing messages produced by the translation
          engine.

          * ISO19139_2ESRI_ISO.xml—Translates content stored in the ISO 19139 XML format
          to the ArcGIS metadata format. This translator is used when you import ISO
          19139-formatted metadata by running the Import Metadata tool with the
          FROM_ISO_19139 type. Metadata is converted using the Esri Metadata Translator
          tool's translation engine and produces a log file containing messages produced
          by the translation engine.
          A translator file must be specified. This tool does not have a default value for
          this parameter.

     OUTPUTS:
      output {File}:
          A stand-alone XML file that will be created containing the converted metadata.To
          check for problems in the metadata using the Esri Metadata Translator's
          translation engine and not produce an output XML file, provide the pound sign
          (#) instead of a file name.
      logfile {File}:
          A text file that will be created listing the warnings and errors that occurred
          during the conversion process.To export metadata without producing a log file,
          provide the pound sign (#)
          instead of a file name.A log file will not be created when using the ArcGIS to
          FGDC translation even if
          a log file name is provided."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ESRITranslator_conversion(*gp_fixargs((source, translator, output, logfile), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportMetadata_conversion', None)
def ExportMetadata(Source_Metadata=None, Translator=None, Output_File=None):
    """ExportMetadata_conversion(Source_Metadata, Translator, {Output_File})

        Updates metadata to contain the most current properties of the ArcGIS item
        before processing the metadata and finally exporting it to an XML file that
        conforms to a standard metadata format.Initial processing is performed to
        produce the best results when exporting
        information to a standard metadata format. Afterwards, the metadata is exported
        using the ESRI Metadata Translator.

     INPUTS:
      Source_Metadata (Data Element / Layer):
          The item whose metadata will be converted or a stand-alone XML file that will be
          converted.
      Translator (File):
          An XML file that defines the conversion that will be performed.The translator
          files provided with ArcGIS for Desktop can be found in the
          <ArcGIS Installation Location>\Metadata\Translator folder. The following
          translators are provided:

          * ARCGIS2FGDC.xml—Translates content stored in the ArcGIS metadata format to the
          FGDC CSDGM XML format. This translator is used by default when you export
          metadata from the Description tab using the FGDC CSDGM Metadata style. Metadata
          is converted using an XSLT transformation and won't produce a log file.

          * ARCGIS2ISO19139.xml—Translates content stored in the ArcGIS metadata format to
          the ISO 19139 XML format. This translator is used by default when you export
          metadata from the Description tab using any of the ISO-based metadata styles. It
          is the preferred translator for exporting metadata to the ISO 19139 XML format.
          Metadata is converted using an XSLT transformation and won't produce a log file.

          * ESRI_ISO2ISO19139.xml—Translates content stored in either the ArcGIS metadata
          format or the ESRI-ISO metadata format to the ISO 19139 XML format. This
          translator is provided for backwards compatibility to support existing models
          and Python scripts. It has some known limitations with exporting metadata to the
          ISO 19139 XML format. Use the ARCGIS2ISO19139.xml translator instead. Metadata
          is converted using the Esri Metadata Translator tool's translation engine and
          produces a log file containing messages produced by the translation engine.

          * FGDC2ESRI_ISO.xml—Translates content stored in the FGDC CSDGM XML format to
          the ArcGIS metadata format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab. This
          translator is used when you import FGDC-formatted metadata by running the Import
          Metadata tool with the FROM_FGDC type and when you upgrade metadata by running
          the Upgrade Metadata tool with the FGDC_TO_ARCGIS type. Metadata is converted
          using the Esri Metadata Translator tool's translation engine and produces a log
          file containing messages produced by the translation engine.

          * FGDC2ISO19139.xml—Translates content stored in the FGDC CSDGM XML format to
          the ISO 19139 XML format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab.
          Metadata is converted using the Esri Metadata Translator tool's translation
          engine and produces a log file containing messages produced by the translation
          engine.

          * ISO19139_2ESRI_ISO.xml—Translates content stored in the ISO 19139 XML format
          to the ArcGIS metadata format. This translator is used when you import ISO
          19139-formatted metadata by running the Import Metadata tool with the
          FROM_ISO_19139 type. Metadata is converted using the Esri Metadata Translator
          tool's translation engine and produces a log file containing messages produced
          by the translation engine.

     OUTPUTS:
      Output_File {File}:
          A stand-alone XML file that will be created containing the converted metadata."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportMetadata_conversion(*gp_fixargs((Source_Metadata, Translator, Output_File), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportMetadataMultiple_conversion', None)
def ExportMetadataMultiple(Source_Metadata=None, Translator=None, Output_Folder=None):
    """ExportMetadataMultiple_conversion(Source_Metadata;Source_Metadata..., Translator, Output_Folder)

        Exports metadata for many ArcGIS items to a designated folder. This tool is a
        model that uses Export Metadata to export metadata for many ArcGIS items.

     INPUTS:
      Source_Metadata (Data Element):
          The set of items whose metadata will be converted, or the set of stand-alone XML
          files that will be converted.
      Translator (File):
          An XML file that defines the conversion that will be performed.The translator
          files provided with ArcGIS for Desktop can be found in the
          <ArcGIS Installation Location>\Metadata\Translator folder. The following
          translators are provided:

          * ARCGIS2FGDC.xml—Translates content stored in the ArcGIS metadata format to the
          FGDC CSDGM XML format. This translator is used by default when you export
          metadata from the Description tab using the FGDC CSDGM Metadata style. Metadata
          is converted using an XSLT transformation and won't produce a log file.

          * ARCGIS2ISO19139.xml—Translates content stored in the ArcGIS metadata format to
          the ISO 19139 XML format. This translator is used by default when you export
          metadata from the Description tab using any of the ISO-based metadata styles. It
          is the preferred translator for exporting metadata to the ISO 19139 XML format.
          Metadata is converted using an XSLT transformation and won't produce a log file.

          * ESRI_ISO2ISO19139.xml—Translates content stored in either the ArcGIS metadata
          format or the ESRI-ISO metadata format to the ISO 19139 XML format. This
          translator is provided for backwards compatibility to support existing models
          and Python scripts. It has some known limitations with exporting metadata to the
          ISO 19139 XML format. Use the ARCGIS2ISO19139.xml translator instead. Metadata
          is converted using the Esri Metadata Translator tool's translation engine and
          produces a log file containing messages produced by the translation engine.

          * FGDC2ESRI_ISO.xml—Translates content stored in the FGDC CSDGM XML format to
          the ArcGIS metadata format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab. This
          translator is used when you import FGDC-formatted metadata by running the Import
          Metadata tool with the FROM_FGDC type and when you upgrade metadata by running
          the Upgrade Metadata tool with the FGDC_TO_ARCGIS type. Metadata is converted
          using the Esri Metadata Translator tool's translation engine and produces a log
          file containing messages produced by the translation engine.

          * FGDC2ISO19139.xml—Translates content stored in the FGDC CSDGM XML format to
          the ISO 19139 XML format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab.
          Metadata is converted using the Esri Metadata Translator tool's translation
          engine and produces a log file containing messages produced by the translation
          engine.

          * ISO19139_2ESRI_ISO.xml—Translates content stored in the ISO 19139 XML format
          to the ArcGIS metadata format. This translator is used when you import ISO
          19139-formatted metadata by running the Import Metadata tool with the
          FROM_ISO_19139 type. Metadata is converted using the Esri Metadata Translator
          tool's translation engine and produces a log file containing messages produced
          by the translation engine.
      Output_Folder (Folder):
          An existing folder where the output XML files containing the converted metadata
          will be stored."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportMetadataMultiple_conversion(*gp_fixargs((Source_Metadata, Translator, Output_Folder), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportMetadata_conversion', None)
def ImportMetadata(Source_Metadata=None, Import_Type=None, Target_Metadata=None, Enable_automatic_updates=None):
    """ImportMetadata_conversion(Source_Metadata, Import_Type, Target_Metadata, Enable_automatic_updates)

        Imports metadata to the target item after converting the source item's metadata
        to ArcGIS metadata, if appropriate. The source and target may be ArcGIS items or
        stand-alone metadata XML files.This tool processes the source metadata before
        importing it and updates the
        target metadata after. Any intrinsic properties of the source item that were
        added automatically to its metadata by ArcGIS are removed along with any unique
        identifiers before converting the information to the ArcGIS metadata format, if
        necessary. After the imported information is saved, the target item's metadata
        is automatically updated with its intrinsic properties.This tool is useful for
        copying metadata from one item to another when you start
        creating its metadata; the imported metadata acts as a template. Using another
        metadata document as a template can save time if two items share some
        information such as legal restrictions or a description of the project for which
        they were created.Existing metadata will be replaced by the imported metadata.

     INPUTS:
      Source_Metadata (Data Element / Layer):
          The item whose metadata will be imported or a stand-alone XML file that will be
          imported.If the source item is a stand-alone file, it must contain well-formed
          XML data.
      Import_Type (String):
          The format of the metadata that will be imported.

          * FROM_ARCGIS—The source metadata is ArcGIS metadata. The metadata won't be
          converted.

          * FROM_ESRIISO—The source metadata contains ESRI-ISO-formatted metadata; that
          is, it was created using the ISO metadata editor provided with ArcGIS Desktop
          9.3.1 and earlier releases. The source metadata will be converted to ArcGIS
          metadata when you run the tool.

          * FROM_FGDC—The source metadata is stored in the FGDC CSDGM metadata standard's
          XML format. The source metadata will be converted to ArcGIS metadata when you
          run the tool.

          * FROM_ISO_19139—The source metadata is formatted according to the ISO 19139
          metadata standard. The source metadata will be converted to ArcGIS metadata when
          you run the tool.
          By default, the FROM_ISO_19139 conversion will be performed.
      Target_Metadata (Data Element / Layer):
          The item to which the metadata will be imported or a stand-alone XML file that
          will be replaced.
      Enable_automatic_updates (Boolean):
          * ENABLED —Information in the imported metadata describing the item's properties
          will be modified to contain the actual item properties. For example, if the
          imported metadata includes the number of features contained by a feature class,
          this number will be updated in the item's metadata by the metadata
          synchronization process after the features have been edited in ArcGIS. Also,
          additional properties that were not present in the imported metadata and that
          can be synchronized for the item will be added. This is the default.

          * DISABLED— Imported information won't be modified. For example, the number of
          features contained by a feature class won't be updated in the item's metadata by
          the metadata synchronization process after the features have been edited in
          ArcGIS; the metadata will always contain the old, out-of-date number. Additional
          properties of the item that were not present in the imported metadata and that
          can be synchronized for the item will be added."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportMetadata_conversion(*gp_fixargs((Source_Metadata, Import_Type, Target_Metadata, Enable_automatic_updates), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MDPublisher_conversion', None)
def MDPublisher(source=None, publisher=None, url=None, service=None, user=None, password=None):
    """MDPublisher_conversion(source, publisher, {url}, {service}, {user}, {password})

        Publishes metadata to a metadata catalog such as an ArcIMS Metadata Service.The
        Metadata Publisher tool retrieves the source item's metadata, then a copy of
        this metadata document is passed to the Publisher specified in the tool. If the
        source item is a stand-alone XML file, a copy of the file itself will be passed
        to the Publisher. The Publisher uses information from the tool parameters and
        from the metadata document to create a request to publish the document to the
        specified metadata catalog.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be published, or a stand-alone XML file that will
          be published.
      publisher (File):
          An XML file that defines how the metadata will be published.
      url {String}:
          The URL of a Web Service that hosts the metadata catalog, if appropriate.For
          example, the URL of an ArcIMS Server that provides a Metadata Service.
      service {String}:
          The name of the service to which you want to publish, if appropriate.For
          example, for an ArcIMS Metadata Service this is the case-sensitive name of
          the Metadata Service.
      user {String}:
          The name used to access the metadata catalog when publishing documents, if
          appropriate.For example, when publishing documents to an ArcIMS Metadata Service
          you must
          log in to the service using a name that has been granted metadata_publisher
          privileges or a higher privilege.
      password {String}:
          The password you used to access the metadata catalog when publishing documents,
          if appropriate.For example, when publishing documents to an ArcIMS Metadata
          Service, this is
          the password required to log in with the specified User Name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MDPublisher_conversion(*gp_fixargs((source, publisher, url, service, user, password), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MetadataImporter_conversion', None)
def MetadataImporter(source=None, target=None):
    """MetadataImporter_conversion(source, target)

        Copies metadata from the source item to the target item. Metadata is retrieved
        from the source item and transferred to the target item without changing it. The
        source and target may be ArcGIS items or stand-alone metadata XML files.The
        source metadata should be ArcGIS metadata. If the imported information is
        not stored in the ArcGIS metadata format it must be upgraded to ArcGIS metadata
        before it will be automatically updated to contain the item's intrinsic
        properties.This tool is useful for saving changes made to your metadata with an
        XSLT
        stylesheet. For example, a model could update metadata using XSLT Transformation
        with a custom stylesheet, then use this tool to import the changes to the
        original ArcGIS item.Existing metadata will be replaced by the imported
        metadata.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be imported or a stand-alone XML file that will be
          imported.If the source item is a stand-alone file, it must contain well-formed
          XML data.
      target (Data Element / Layer):
          The item to which the metadata will be imported or a stand-alone XML file that
          will be replaced."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MetadataImporter_conversion(*gp_fixargs((source, target), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SynchronizeMetadata_conversion', None)
def SynchronizeMetadata(source=None, synctype=None):
    """SynchronizeMetadata_conversion(source, synctype)

        Automatically updates an ArcGIS item's metadata with the current properties of
        the item.For example, if the metadata describes the item as having one
        projection but the
        item's projection has changed since the last automatic update, the old
        projection information in the metadata will be replaced with the new projection
        information.The item's metadata must be stored in the ArcGIS metadata format;
        otherwise, the
        metadata will not be synchronized.If a property was set using ArcGIS Desktop
        9.3.1 or earlier to prevent ArcGIS
        from automatically updating this specific item's metadata with the item's
        properties, it will be ignored in the current release. ArcGIS metadata will
        always be synchronized with the item it descibes.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be synchronized.
      synctype (String):
          The type of synchronization that will take place.

          * ALWAYS—Properties of the source item are always added to or updated in its
          metadata. Metadata will be created if it doesn't already exist. This is the
          deault.

          * ACCESSED—Properties of the source item are added to or updated in its metadata
          when it is accessed. Metadata will be created if it doesn't already exist.

          * CREATED—Metadata will be created and properties of the source item will be
          added to it if the item doesn't already have metadata.

          * NOT_CREATED—Properties of the source item are added to or updated in existing
          metadata.

          * OVERWRITE—The same as "ALWAYS" except all information that can be recorded
          automatically in the metadata will be recorded. Any properties typed in by a
          person will be replaced with the item's actual properties.

          * SELECTIVE—The same as "OVERWRITE" except the title and the content type will
          not be overwritten with default values for the item. Used when metadata is
          upgraded to the ArcGIS 10.x metadata format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SynchronizeMetadata_conversion(*gp_fixargs((source, synctype), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('USGSMPTranslator_conversion', None)
def USGSMPTranslator(source=None, config=None, conversion=None, output=None, errors=None):
    """USGSMPTranslator_conversion(source, {config}, {conversion}, {output}, {errors})

        Uses the USGS metadata parser utility, known as mp, to export or validate FGDC
        metadata content. The mp utility is created and maintained by the USGS for
        managing metadata that follows the FGDC Content Standard for Digital Geospatial
        Metadata (CSDGM). A version of mp is provided with ArcGIS.This tool only uses
        metadata elements in an item's metadata or a stand-alone
        metadata XML file that follow the FGDC CSDGM metadata format. FGDC content may
        exist in an ArcGIS item's metadata. For example, if the metadata was created in
        ArcGIS Desktop 9.3.1 or earlier using the FGDC metadata editor or created in the
        current version of ArcGIS for Desktop using the FGDC metadata editor add-in, the
        item's metadata will include elements that follow the FGDC XML format. This tool
        only exports these FGDC XML metadata elements—the information displayed in the
        FGDC Metadata (read-only) section in the Description tab if you are using a
        metadata style that provides access to an item's complete metadata.If an item's
        metadata only contains information edited in the Description tab it
        won't contain any XML elements that can be exported using this tool. After
        selecting the FGDC CSDGM Metadata style you can export ArcGIS metadata to the
        FGDC XML format. Use this tool with the exported FGDC XML file to generate the
        HTML, text, and SGML files that are commonly associated with FGDC metadata.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be converted or a stand-alone XML file that will be
          converted.
      config {File}:
          A file that defines custom parameters that mp will consider when processing the
          metadata.To export metadata without using a configuration file, provide #
          instead of a
          file name.
      conversion {String}:
          The type of conversion that will take place.

          * NONE—No conversion will be performed.

          * XML—An XML file will be created as output.

          * HTML—An HTML file will be created as output.

          * TEXT—A text file will be created as output.

          * FAQ—An HTML file in FAQ format will be created as output.

          * SGML—An SGML file will be created as output.

          * DIF—A text file in DIF format will be created as output.
          By default, the "XML" conversion will be performed.

     OUTPUTS:
      output {File}:
          A file that will be created containing the converted metadata.The type of file
          created is defined by the conversion type.To check for problems in the FGDC
          metadata using mp and not produce a output
          file, provide # instead of a file name.
      errors {File}:
          A text file that will be created listing the warnings and errors that occurred
          during the conversion process.To export metadata without producing a log file,
          provide the pound sign (#)
          instead of a file name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.USGSMPTranslator_conversion(*gp_fixargs((source, config, conversion, output, errors), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpgradeMetadata_conversion', None)
def UpgradeMetadata(Source_Metadata=None, Upgrade_Type=None):
    """UpgradeMetadata_conversion(Source_Metadata, Upgrade_Type)

        Updates an ArcGIS item's metadata or a stand-alone XML file to the current
        ArcGIS metadata format.The current release of ArcGIS will only maintain
        information in the ArcGIS
        metadata format. For example, if an ArcGIS item has metadata in another format
        it must be upgraded to ArcGIS metadata before ArcGIS will automatically update
        it with the item's current properties; the item's properties are recorded in
        ArcGIS metadata elements.Upgrading metadata for the current release of ArcGIS
        will not change the
        existing metadata except to add ArcGIS metadata alongside the existing
        information. The existing metadata will remain unchanged.

     INPUTS:
      Source_Metadata (Data Element / Layer):
          The item whose metadata will be upgraded, or a stand-alone XML file that will be
          upgraded.
      Upgrade_Type (String):
          The type of conversion that will take place.

          * ESRIISO_TO_ARCGIS—Upgrades ESRI-ISO-format metadata. ESRI-ISO metadata is
          typically created with the ISO metadata editing wizard provided with ArcGIS
          Desktop 9.3.1 and earlier releases.

          * FGDC_TO_ARCGIS—Upgrades FGDC-format metadata. For example, FGDC metadata may
          have been created in ArcGIS Desktop 9.3.1 with the FGDC metadata editor. FGDC
          metadata may have been created outside ArcGIS.
          An upgrade type must be specified; otherwise, no conversion will be performed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeMetadata_conversion(*gp_fixargs((Source_Metadata, Upgrade_Type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ValidateMetadata_conversion', None)
def ValidateMetadata(Source_Metadata=None, Translator=None, Schema_URL=None, Namespace_URI=None, Output_File=None):
    """ValidateMetadata_conversion(Source_Metadata, Translator, Schema_URL, {Namespace_URI}, Output_File)

        Exports metadata to a standard metadata format then validates the exported
        file.ArcGIS metadata can't be directly validated against a metadata standard's
        XML
        schema. This tool validates ArcGIS metadata by first exporting it to an XML file
        that is formatted to follow a metadata standard's XML schema using Export
        Metadata, then validating the exported file using XML Schema Validation. Only
        use this tool to validate ArcGIS metadata, not a stand-alone XML file that is
        already formatted correctly for a metadata standard's XML format.Any validation
        errors and warnings will be reported in the tool's messages.

     INPUTS:
      Source_Metadata (Data Element / Layer):
          The item whose metadata will be validated or a stand-alone XML file that will be
          validated.
      Translator (File):
          An XML file that defines the conversion that will be performed.The translator
          files provided with ArcGIS for Desktop can be found in the
          <ArcGIS Installation Location>\Metadata\Translator folder. The following
          translators are provided:

          * ARCGIS2FGDC.xml—Translates content stored in the ArcGIS metadata format to the
          FGDC CSDGM XML format. This translator is used by default when you export
          metadata from the Description tab using the FGDC CSDGM Metadata style. Metadata
          is converted using an XSLT transformation and won't produce a log file.

          * ARCGIS2ISO19139.xml—Translates content stored in the ArcGIS metadata format to
          the ISO 19139 XML format. This translator is used by default when you export
          metadata from the Description tab using any of the ISO-based metadata styles. It
          is the preferred translator for exporting metadata to the ISO 19139 XML format.
          Metadata is converted using an XSLT transformation and won't produce a log file.

          * ESRI_ISO2ISO19139.xml—Translates content stored in either the ArcGIS metadata
          format or the ESRI-ISO metadata format to the ISO 19139 XML format. This
          translator is provided for backwards compatibility to support existing models
          and Python scripts. It has some known limitations with exporting metadata to the
          ISO 19139 XML format. Use the ARCGIS2ISO19139.xml translator instead. Metadata
          is converted using the Esri Metadata Translator tool's translation engine and
          produces a log file containing messages produced by the translation engine.

          * FGDC2ESRI_ISO.xml—Translates content stored in the FGDC CSDGM XML format to
          the ArcGIS metadata format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab. This
          translator is used when you import FGDC-formatted metadata by running the Import
          Metadata tool with the FROM_FGDC type and when you upgrade metadata by running
          the Upgrade Metadata tool with the FGDC_TO_ARCGIS type. Metadata is converted
          using the Esri Metadata Translator tool's translation engine and produces a log
          file containing messages produced by the translation engine.

          * FGDC2ISO19139.xml—Translates content stored in the FGDC CSDGM XML format to
          the ISO 19139 XML format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab.
          Metadata is converted using the Esri Metadata Translator tool's translation
          engine and produces a log file containing messages produced by the translation
          engine.

          * ISO19139_2ESRI_ISO.xml—Translates content stored in the ISO 19139 XML format
          to the ArcGIS metadata format. This translator is used when you import ISO
          19139-formatted metadata by running the Import Metadata tool with the
          FROM_ISO_19139 type. Metadata is converted using the Esri Metadata Translator
          tool's translation engine and produces a log file containing messages produced
          by the translation engine.
      Schema_URL (String):
          The XML Schema or XML DTD that describes the structure and content of a valid
          XML document.
      Namespace_URI {String}:
          The XML namespace that will be validated for an XML Schema, if appropriate, or
          the root element of the document for an XML DTD.If this value is inappropriate
          for the XML Schema being used, provide the pound
          sign (#) instead of a namespace URI.

     OUTPUTS:
      Output_File (File):
          A stand-alone XML file that will be created containing the converted metadata."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ValidateMetadata_conversion(*gp_fixargs((Source_Metadata, Translator, Schema_URL, Namespace_URI, Output_File), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ValidateMetadataMultiple_conversion', None)
def ValidateMetadataMultiple(Source_Metadata=None, Translator=None, Schema_URL=None, Namespace_URI=None, Output_Folder=None):
    """ValidateMetadataMultiple_conversion(Source_Metadata;Source_Metadata..., Translator, Schema_URL, {Namespace_URI}, Output_Folder)

        Exports metadata for many ArcGIS items to a designated folder, then validates
        the exported files. This tool is a model that uses Validate Metadata to validate
        metadata for many ArcGIS items.

     INPUTS:
      Source_Metadata (Data Element):
          The item whose metadata will be validated or a stand-alone XML file that will be
          validated.
      Translator (File):
          An XML file that defines the conversion that will be performed.The translator
          files provided with ArcGIS for Desktop can be found in the
          <ArcGIS Installation Location>\Metadata\Translator folder. The following
          translators are provided:

          * ARCGIS2FGDC.xml—Translates content stored in the ArcGIS metadata format to the
          FGDC CSDGM XML format. This translator is used by default when you export
          metadata from the Description tab using the FGDC CSDGM Metadata style. Metadata
          is converted using an XSLT transformation and won't produce a log file.

          * ARCGIS2ISO19139.xml—Translates content stored in the ArcGIS metadata format to
          the ISO 19139 XML format. This translator is used by default when you export
          metadata from the Description tab using any of the ISO-based metadata styles. It
          is the preferred translator for exporting metadata to the ISO 19139 XML format.
          Metadata is converted using an XSLT transformation and won't produce a log file.

          * ESRI_ISO2ISO19139.xml—Translates content stored in either the ArcGIS metadata
          format or the ESRI-ISO metadata format to the ISO 19139 XML format. This
          translator is provided for backwards compatibility to support existing models
          and Python scripts. It has some known limitations with exporting metadata to the
          ISO 19139 XML format. Use the ARCGIS2ISO19139.xml translator instead. Metadata
          is converted using the Esri Metadata Translator tool's translation engine and
          produces a log file containing messages produced by the translation engine.

          * FGDC2ESRI_ISO.xml—Translates content stored in the FGDC CSDGM XML format to
          the ArcGIS metadata format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab. This
          translator is used when you import FGDC-formatted metadata by running the Import
          Metadata tool with the FROM_FGDC type and when you upgrade metadata by running
          the Upgrade Metadata tool with the FGDC_TO_ARCGIS type. Metadata is converted
          using the Esri Metadata Translator tool's translation engine and produces a log
          file containing messages produced by the translation engine.

          * FGDC2ISO19139.xml—Translates content stored in the FGDC CSDGM XML format to
          the ISO 19139 XML format; that is, it translates metadata content that is
          visible under the FGDC Metadata (read-only) heading in the Description tab.
          Metadata is converted using the Esri Metadata Translator tool's translation
          engine and produces a log file containing messages produced by the translation
          engine.

          * ISO19139_2ESRI_ISO.xml—Translates content stored in the ISO 19139 XML format
          to the ArcGIS metadata format. This translator is used when you import ISO
          19139-formatted metadata by running the Import Metadata tool with the
          FROM_ISO_19139 type. Metadata is converted using the Esri Metadata Translator
          tool's translation engine and produces a log file containing messages produced
          by the translation engine.
      Schema_URL (String):
          An existing folder where the output XML files containing the converted metadata
          will be stored.
      Namespace_URI {String}:
          The XML Schema or XML DTD that describes the structure and content of a valid
          XML document.
      Output_Folder (Folder):
          The XML namespace that will be validated for an XML Schema, if appropriate, or
          the root element of the document for an XML DTD.If this value is inappropriate
          for the XML Schema being used, provide the pound
          sign (#) instead of a namespace URI."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ValidateMetadataMultiple_conversion(*gp_fixargs((Source_Metadata, Translator, Schema_URL, Namespace_URI, Output_Folder), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('XMLSchemaValidator_conversion', None)
def XMLSchemaValidator(source=None, schemaurl=None, nsuri=None):
    """XMLSchemaValidator_conversion(source, schemaurl, {nsuri})

        Uses the .NET 3.5 Framework's XML software to validate an ArcGIS item's
        metadata or any XML file. The XML is checked to see if it follows the structure
        and content rules outlined by an XML schema. Schemas written using the DTD or
        W3C XML Schema languages may be used with this tool.ArcGIS metadata is not
        formatted in a manner that can be directly validated
        against an XML schema. However, other metadata geoprocessing tools can export
        ArcGIS metadata to XML files that are formatted to follow a metadata standard's
        XML Schema or DTD; use this tool to validate the exported XML file or a stand-
        alone metadata XML file that is already formatted correctly for a metadata
        standard's XML schema.If the metadata or XML file is not valid for the specified
        XML Schema or DTD,
        the warnings or errors returned by the XML software will appear in the tool's
        messages.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be validated or a stand-alone XML file that will be
          validated.
      schemaurl (String):
          The XML Schema or XML DTD that describes the structure and content of a valid
          XML document.
      nsuri {String}:
          The XML namespace that will be validated for an XML Schema, if appropriate, or
          the root element of the document for an XML DTD.If this value is inappropriate
          for the XML Schema being used, provide the pound
          sign (#) instead of a namespace URI."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.XMLSchemaValidator_conversion(*gp_fixargs((source, schemaurl, nsuri), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('XSLTransform_conversion', None)
def XSLTransform(source=None, xslt=None, output=None, xsltparam=None):
    """XSLTransform_conversion(source, xslt, output, {xsltparam})

        Uses the .NET 3.5 XML software to transform an ArcGIS item's metadata or any XML
        file using an XSLT 1.0 stylesheet and save the result to an XML file.XSLT
        stylesheets can be used to perform a variety of modifications to ArcGIS
        metadata or an XML file. Several XSLT stylesheets are provided with ArcGIS for
        Desktop. They can be found in the <ArcGIS Installation
        Location>\Metadata\Stylesheets folder. These stylesheets are described in the
        tables below.The following stylesheets produce the HTML documents that are used
        to display
        information about an item in the Description tab. They extract content from an
        item's metadata and add HTML formatting instructions to it. These stylesheets
        import many XSLT templates from other files in the ArcGIS_Imports folder; the
        imported templates perform most of the work. If you are interested in creating
        custom stylesheets for display, you can learn more about these stylesheets by
        reading the documentation provided with the ArcGIS Metadata Toolkit.
        ArcGIS.xslDisplays an item's complete metadata content. It is referenced by all
        metadata
        styles except the default Item Description
        style.ArcGIS_ItemDescription.xslDisplays only a concise description of the item.
        It is referenced by the default
        Item Description metadata style.The following stylesheets, provided in the
        <ArcGIS Installation
        Location>\Metadata\Stylesheets\gpTools folder, take an item's metadata, process
        it, then save the resulting XML document to a new XML file. The goal of this
        operation might be to filter an item's metadata before using it outside of
        ArcGIS. Or, the goal might be to alter the item's metadata; in this case, the
        resulting XML file can be saved back to the original item as its metadata using
        the Metadata Importer tool. A model or script can be created that first runs
        this tool with a stylesheet to update the metadata content, then immediately
        saves the changes back to the item. The following stylesheets are provided with
        ArcGIS for Desktop to perform some well-defined metadata tasks.add unique
        identifier.xsltAdds or changes the unique identifier stored in the item's
        metadata. The
        identifier modified by this stylesheet is stored in the Esri PublishedDocID
        metadata element and is used to identify the document in a metadata catalog such
        as an ArcIMS Metadata Service or a Geoportal.exact copy of.xsltCreates an exact
        copy of the item's metadata as an XML file. For example, you
        might use this stylesheet to save a copy of a geodatabase item's metadata to a
        local file so it can be examined.generate metadata template.xsltCopies ArcGIS
        metadata content to a new XML file that can be imported to other
        items as a metadata template. Synchronized metadata content is excluded from the
        template and any empty elements are removed.remove empty elements.xslt Removes
        empty XML elements. After other stylesheets have been used to remove
        unwanted metadata content, empty XML elements may remain. Empty XML elements can
        cause problems if you later try to validate an item's metadata. For example, if
        an element is optional but empty, you will often receive an error message
        because the element has no value, whereas the metadata would be valid if the
        empty element was removed.remove entries from FGDC lineage.xsltRemoves process
        steps added to the FGDC-format lineage by ArcGIS Desktop 9.3.1.
        Process steps were added to the FGDC-format lineage when metadata was imported
        to an item and when the item was copied to a new location. This information is
        not added to an item's lineage using the current version of ArcGIS, and is not
        upgraded to the ArcGIS metadata format along with the rest of the item's
        lineage.remove FGDC required hints.xsltRemoves any FGDC-format metadata elements
        that contain the text REQUIRED. These
        text strings were added by ArcGIS Desktop 9.3.1 when FGDC-format metadata was
        created to indicate which metadata elements are required to create valid FGDC
        CSDGM metadata. However, these strings can cause problems if you later try to
        validate an item's metadata. When the default text is present, the element will
        be considered valid because it contains text, even though the text doesn't
        provide any information about the item. Default text strings are not added by
        the current version of ArcGIS, and these strings are not upgraded to the ArcGIS
        metadata format along with the rest of an item's metadata content.remove
        geoprocessing history.xsltRemoves an item's geoprocessing history. While all of
        the metadata geoprocessing
        tools are designed to preserve an item's geoprocessing history, over time, that
        history can grow so large that the item's metadata becomes difficult to handle
        as an XML document. In these circumstances it may be necessary to remove an
        item's geoprocessing history.remove local storage info.xsltRemoves any machine
        names that may exist in the item's metadata. Depending on
        where the machine name was found, the metadata element containing the
        information may be removed, or the machine name may be removed from a UNC path,
        or the element's value may be updated to identify the location as being
        withheld.remove pre94 metadata elements.xsltRemoves any ESRI-ISO format XML
        elements and any FGDC CSDGM-format XML elements
        from an item's metadata that are not included in the ArcGIS metadata
        format.remove synchronized elements.xsltRemoves any information that was added
        to an item's metadata by the ArcGIS
        metadata synchronization process.remove thumbnail.xsltRemoves an item's
        thumbnail. While all of the metadata geoprocessing tools are
        designed to preserve an item's thumbnail, in some circumstances you might want
        to remove the item's thumbnail. You can remove one item's thumbnail when you
        edit its metadata in the Description tab. With this script you could run a batch
        process to remove thumbnails from many items.remove unique
        identifiers.xsltRemoves all unique identifiers from an item's metadata,
        including all
        identifiers that may have been added by ArcGIS and any identifiers provided
        using a metadata editor. Identifiers should never be copied to another
        item._MPXML2.xslExtracts FGDC CSDGM format XML elements from the item's
        metadata, if they exist,
        and orders them correctly. The information extracted by this stylesheet is the
        content that appears under the FGDC Metadata (read-only) heading in the
        Description tab.Some of the stylesheets provided with ArcGIS for Desktop are
        used by the
        metadata geoprocessing tools to perform portions of the importing, exporting,
        and upgrading processes:

        * _MPXML2.xsl


        * merge imported metadata with existing.xslt


        * merge upgraded FGDC with existing.xslt


        * prep metadata for export.xslt


        * remove empty elements.xslt


        * remove FGDC required hints.xslt


        * remove synchronized elements.xslt


        * remove unique identifiers.xslt


        * upgrade ESRI-ISO to ArcGIS94.xslt
        You can create your own XSLT stylesheets to perform tasks using the provided
        stylesheets as examples. For example, you might write a stylesheet to:

        * Update addresses or phone numbers. Create a model that runs this process then
        uses the Metadata Importer tool to save the updated metadata to the original
        ArcGIS item.


        * Remove information that you do not want publicly available before exporting or
        publishing the metadata. Create a model that runs this process before running
        the Export Metadata or Metadata Publisher tools.


        * Export information to an HTML file so you can incorporate this information
        into a website. Create a script that runs this process periodically.
        XSLT stylesheets that modify ArcGIS metadata should not remove information in
        the Esri and Binary metadata elements except if the output XML will be used
        outside of ArcGIS.

     INPUTS:
      source (Data Element / Layer):
          The item whose metadata will be converted or a stand-alone XML file that will be
          converted.
      xslt (File):
          A W3C-compliant XSLT 1.0 stylesheet file that defines the transformation that
          will be performed.Several stylesheets are provided with ArcGIS and are available
          in the <ArcGIS
          Installation Location>\Metadata\Stylesheets folder.
      xsltparam {String / File}:
          An XML file or string that will be passed to the XSLT stylesheet.To capture this
          parameter in the XSLT stylesheet, add <xsl:param name="gpparam"
          /> to the top of the XSLT stylesheet after the xsl:output element and before the
          first xsl:template element. See add unique identifier.xslt for an example.

     OUTPUTS:
      output (File):
          A file that will be created containing the converted metadata.The type of file
          created depends on the output method specified in the XSLT
          stylesheet."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.XSLTransform_conversion(*gp_fixargs((source, xslt, output, xsltparam), True)))
        return retval
    except Exception, e:
        raise e


# To CAD toolset
@gptooldoc('AddCADFields_conversion', None)
def AddCADFields(input_table=None, Entities=None, LayerProps=None, TextProps=None, DocProps=None, XDataProps=None):
    """AddCADFields_conversion(input_table, Entities, {LayerProps}, {TextProps}, {DocProps}, {XDataProps})

        Adds several reserved CAD fields in one step. Fields created by this tool are
        used by the Export To CAD tool to generate CAD entities with specific
        properties.  After executing this tool, you must calculate or type the
        appropriate field values.

     INPUTS:
      input_table (Table View):
          Input table, feature class, or shapefile that will have the CAD-specific fields
          added to it
      Entities (Boolean):
          Adds the list of CAD-specific Entity property fields to the input table

          * ADD_ENTITY_PROPERTIES—Adds the list of CAD-specific Entity property fields to
          the input table

          * NO_ENTITY_PROPERTIES—Does not add the list of CAD-specific Entity property
          fields to the input table
      LayerProps {Boolean}:
          Adds the list of CAD-specific Layer property fields to the input table

          * ADD_LAYER_PROPERTIES—Adds the list of CAD-specific Layer property fields to
          the input table

          * NO_LAYER_PROPERTIES—Does not add the list of CAD-specific Layer property
          fields to the input table
      TextProps {Boolean}:
          Adds the list of CAD-specific Text property fields to the input table

          * ADD_TEXT_PROPERTIES—Adds the list of CAD-specific Text property fields to the
          input table

          * NO_TEXT_PROPERTIES—Does not add the list of CAD-specific Text property fields
          to the input table
      DocProps {Boolean}:
          Adds the list of CAD-specific Document property fields to the input table

          * ADD_DOCUMENT_PROPERTIES—Adds the list of CAD-specific Document property fields
          to the input table

          * NO_DOCUMENT_PROPERTIES—Does not add the list of CAD-specific Document property
          fields to the input table
      XDataProps {Boolean}:
          Adds the list of CAD-specific XData property fields to the input table

          * ADD_XDATA_PROPERTIES—Adds the list of CAD-specific XData property fields to
          the input table

          * NO_XDATA_PROPERTIES—Does not add the list of CAD-specific XData property
          fields to the input table"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddCADFields_conversion(*gp_fixargs((input_table, Entities, LayerProps, TextProps, DocProps, XDataProps), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportCAD_conversion', None)
def ExportCAD(in_features=None, Output_Type=None, Output_File=None, Ignore_FileNames=None, Append_To_Existing=None, Seed_File=None):
    """ExportCAD_conversion(in_features;in_features..., Output_Type, Output_File, {Ignore_FileNames}, {Append_To_Existing}, {Seed_File})

        Creates one or more CAD drawings based on the values contained in one or more
        input feature classes or feature layers and supporting tables.

     INPUTS:
      in_features (Feature Layer):
          A collection of feature classes and/or feature layers whose geometry will be
          exported to one or more CAD files.
      Output_Type (String):
          The CAD platform and file version of the output files. This value overrides any
          output_type values contained in the keyname column or alias column CADFile_type.
          Types include DGN_V8, DWG_R14, DWG_R2000, DWG_R2004, DWG_R2005, DWG_R2007,
          DWG_R2010, DXF_R14, DXF_R2000, DXF_R2004, DXF_R2005, DXF_R2007, and DXF_R2010.
      Ignore_FileNames {Boolean}:
          Allows the function to ignore or use the paths in the DrawingPathName. This
          allows the function to output CAD entities to specific drawings or ignore this
          and add to one CAD file.

          * IGNORE_FILENAMES_IN_TABLES—Ignores the paths in the document entity fields and
          allows the output of all entities to a single CAD file.

          * USE_FILENAMES_IN_TABLES—Allows the paths in the document entity fields to be
          used and have each entity's path used so that each CAD part will be written to a
          separate file. This is the default.
      Append_To_Existing {Boolean}:
          Allows the output to append to an existing CAD file. This lets you add
          information to a CAD file on disk.

          * APPEND_TO_EXISTING_FILES—Allows the output file content to be added to an
          existing output CAD file. The existing CAD file content will not be lost.

          * OVERWRITE_EXISTING_FILES—The output file content will overwrite the existing
          CAD file content. This is the default.
      Seed_File {CAD Drawing Dataset}:
          An existing CAD drawing whose contents and document and layer properties will be
          used for all new output CAD files. The CAD platform and format version of the
          seed file overrides the value specified by the Output_Type parameter. If
          appending to existing CAD files, the seed drawing is ignored.

     OUTPUTS:
      Output_File (CAD Drawing Dataset):
          The path of the desired output CAD drawing file. This name overrides any drawing
          name information included in the input features columns or alias columns named
          DrawingPathName."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportCAD_conversion(*gp_fixargs((in_features, Output_Type, Output_File, Ignore_FileNames, Append_To_Existing, Seed_File), True)))
        return retval
    except Exception, e:
        raise e


# To Collada toolset
@gptooldoc('MultipatchToCollada_conversion', None)
def MultipatchToCollada(in_features=None, output_folder=None, prepend_source=None, field_name=None):
    """MultipatchToCollada_conversion(in_features, output_folder, {prepend_source}, {field_name})

        Converts one or more multipatch features into a collection of COLLADA (.dae)
        files and referenced texture image files in an output folder. The inputs can be
        a layer or a feature class.

     INPUTS:
      in_features (Feature Layer):
          The multipatch features to be exported.
      prepend_source {Boolean}:
          Prepend the file names of the output COLLADA files with the name of the source
          feature layer.

          * PREPEND_SOURCE_NAME—Prepend the file names.

          * PREPEND_NONE—Do not prepend the file names. This is the default.
      field_name {Field}:
          The feature attribute to use as the output COLLADA file name for each exported
          feature. If no field is specified, the feature's Object ID is used.

     OUTPUTS:
      output_folder (Folder):
          The destination folder where the output COLLADA files and texture image files
          will be placed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MultipatchToCollada_conversion(*gp_fixargs((in_features, output_folder, prepend_source, field_name), True)))
        return retval
    except Exception, e:
        raise e


# To Coverage toolset
@gptooldoc('FeatureclassToCoverage_conversion', None)
def FeatureclassToCoverage(in_features=None, out_cover=None, cluster_tolerance=None, precision=None):
    """FeatureclassToCoverage_conversion(in_features;in_features..., out_cover, {cluster_tolerance}, {precision})

        Creates a single ArcInfo Workstation coverage from one or more input feature
        classes or layers.

     INPUTS:
      in_features (Value Table):
          The input feature classes or layers used to create a single ArcInfo Workstation
          coverage, including the type of features of which the coverage will be composed.

          * POINT

          * LABEL

          * NODE

          * ARC

          * ROUTE

          * POLYGON

          * REGION

          * ANNO
      cluster_tolerance {Linear unit}:
          The minimum distance separating all feature coordinates (nodes and vertices) as
          well as the distance a coordinate can move in X or Y (or both). You can set the
          value to be higher for data that has less coordinate accuracy and lower for
          datasets with extremely high accuracy.
      precision {Boolean}:
          The precision of the output coverage.

          * DOUBLE— The out_cover will have double precison. This is the default.

          * SINGLE—The out_cover will have single precision.

     OUTPUTS:
      out_cover (Coverage):
          The output coverage to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureclassToCoverage_conversion(*gp_fixargs((in_features, out_cover, cluster_tolerance, precision), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportFromE00_conversion', None)
def ImportFromE00(Input_interchange_file=None, Output_folder=None, Output_name=None):
    """ImportFromE00_conversion(Input_interchange_file, Output_folder, Output_name)

        Imports an ArcInfo Workstation interchange file (.e00).  An interchange file is
        used to transport coverages, INFO tables, text files such as AML macros, and
        other ArcInfo files. For coverages, grids, and tins, it contains all
        information, including appropriate INFO table information. Interchange files are
        designated with the .e00 file suffix. This is the ArcView GIS version of the
        utility for importing .e00 files.

     INPUTS:
      Input_interchange_file (File):
          ArcInfo Workstation interchange file to convert. The name of this file cannot
          contain spaces.
      Output_folder (Folder):
          The location in which the output will be created.
      Output_name (String):
          The name of the output. This string cannot contain any spaces. If this output
          already exists, the tool will not overwrite it, even if the geoprocessing
          overwrite output setting is set to true."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportFromE00_conversion(*gp_fixargs((Input_interchange_file, Output_folder, Output_name), True)))
        return retval
    except Exception, e:
        raise e


# To Geodatabase toolset
@gptooldoc('CADToGeodatabase_conversion', None)
def CADToGeodatabase(input_cad_datasets=None, out_gdb_path=None, out_dataset_name=None, reference_scale=None, spatial_reference=None):
    """CADToGeodatabase_conversion(input_cad_datasets;input_cad_datasets..., out_gdb_path, out_dataset_name, reference_scale, {spatial_reference})

        Reads a CAD dataset and creates feature classes of the drawing. The feature
        classes are written to a geodatabase feature dataset.

     INPUTS:
      input_cad_datasets (CAD Drawing Dataset):
          The collection of CAD files to convert to geodatabase features.
      out_gdb_path (Workspace):
          The ArcSDE, file, or personal geodatabase where the Output Feature Dataset will
          be created. The target geodatabase must already exist.
      out_dataset_name (String):
          The name of the feature dataset to be created.
      reference_scale (Double):
          Enter the scale to use as a reference for the annotation. This sets the scale
          to which all symbol and text sizes in the annotation will be made relative.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. If you wish to control
          other aspects of the spatial reference (i.e., the xy, z, m domains, resolutions,
          tolerances), use the relevant environments."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CADToGeodatabase_conversion(*gp_fixargs((input_cad_datasets, out_gdb_path, out_dataset_name, reference_scale, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CopyRuntimeGdbToFileGdb_conversion', None)
def CopyRuntimeGdbToFileGdb(in_file=None, out_file=None):
    """CopyRuntimeGdbToFileGdb_conversion(in_file, out_file)

        Copies the contents of a Runtime geodatabase into a new file geodatabase.

     INPUTS:
      in_file (File):
          Runtime geodatabase that will be copied to a file geodatabase.

     OUTPUTS:
      out_file (File):
          The output file geodatabase name and location. For example:
          c:/temp/outputGeodatabases/copiedFGDB.gdb."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyRuntimeGdbToFileGdb_conversion(*gp_fixargs((in_file, out_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureClassToFeatureClass_conversion', None)
def FeatureClassToFeatureClass(in_features=None, out_path=None, out_name=None, where_clause=None, field_mapping=None, config_keyword=None):
    """FeatureClassToFeatureClass_conversion(in_features, out_path, out_name, {where_clause}, {field_mapping}, {config_keyword})

        Converts a shapefile, coverage feature class, or geodatabase feature class to a
        shapefile or geodatabase feature class.

     INPUTS:
      in_features (Feature Layer):
          The feature class or feature layer that will be converted.
      out_path (Workspace / Feature Dataset):
          The location in which the output feature class will be created. This can be
          either a geodatabase or a folder. If the output location is a folder, the output
          will be a shapefile.
      out_name (String):
          The name of the output feature class.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS.
      field_mapping {Field Mappings}:
          The fields and field contents chosen from the input feature class. You can add,
          rename, or delete output fields as well as set properties such as data type and
          merge rule.Learn more about choosing and setting the output fields.You can use
          the ArcPy FieldMappings class to define this parameter.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for geodatabases in file and
          enterprise geodatabases. Personal geodatabases do not use configuration
          keywords."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureClassToFeatureClass_conversion(*gp_fixargs((in_features, out_path, out_name, where_clause, field_mapping, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureClassToGeodatabase_conversion', None)
def FeatureClassToGeodatabase(Input_Features=None, Output_Geodatabase=None):
    """FeatureClassToGeodatabase_conversion(Input_Features;Input_Features..., Output_Geodatabase)

        Converts one or more feature classes or feature layers to geodatabase feature
        classes.

     INPUTS:
      Input_Features (Feature Layer):
          One or more feature classes or feature layers to be imported into a file,
          personal, or enterprise geodatabase.
      Output_Geodatabase (Workspace / Feature Dataset):
          The output or destination geodatabase. This can be a file, personal, or
          enterprise geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureClassToGeodatabase_conversion(*gp_fixargs((Input_Features, Output_Geodatabase), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportCADAnnotation_conversion', None)
def ImportCADAnnotation(input_features=None, output_featureclass=None, reference_scale=None, use_levels=None, match_symbols_from_first_input=None, require_symbol_from_table=None, feature_linked=None, linked_feature_class=None, create_annotation_when_feature_added=None, update_annotation_when_feature_modified=None):
    """ImportCADAnnotation_conversion(input_features;input_features..., output_featureclass, reference_scale, {use_levels}, {match_symbols_from_first_input}, {require_symbol_from_table}, {feature_linked}, {linked_feature_class}, {create_annotation_when_feature_added}, {update_annotation_when_feature_modified})

        Converts a collection of CAD annotation features to geodatabase annotation. You
        can convert each level to individual annotation classes or merge them into a
        single class. Also, if you choose map layers as input, the level and font
        overrides will be honored.

     INPUTS:
      input_features (Feature Layer):
          The CAD annotation features that you want to convert to geodatabase annotation.
          If you choose a CAD annotation layer in ArcMap, the following properties of that
          layer will be honored during the conversion:

          * Visible drawing layers. Only those layers that are turned on for drawing will
          be converted.

          * Substitution of font and color properties for the text symbol.

          * Selection. Only the selected features will be converted.

          * Definition Query. Only visible features that match the definition query will
          be converted.
      reference_scale (Double):
          Enter the scale to use as a reference for the annotation. This sets the scale to
          which all symbol and text sizes in the annotation will be made relative.
      use_levels {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether all CAD drawing layers or levels will
          be converted to annotation
          classes within the feature class.

          * CLASSES_FROM_LEVELS—Each CAD drawing level or layer will be converted to an
          annotation class within the Output Feature Class. This is the default.

          * ONE_CLASS_ONLY—All CAD drawing levels or layers will be converted to a single
          annotation class within the Output Feature Class.
      match_symbols_from_first_input {Boolean}:
          If you are converting CAD annotation from more than one drawing file and need to
          substitute the font properties for a symbol and apply that to all the input
          features, you can use this option.

          * MATCH_FIRST_INPUT—Match the symbols from the first input layer and have them
          apply to all layers.

          * NO_MATCH—Each drawing file retains its own font properties. This is the
          default.
      require_symbol_from_table {Boolean}:
          Specify if the output annotation features will reference a symbol stored in the
          symbol collection for the feature class.

          * NO_SYMBOL_REQUIRED—The output annotation features will not reference a symbol
          stored in the symbol collection for the feature class. This is the default.

          * REQUIRE_SYMBOL—The output annotation features will reference a symbol stored
          in the symbol collection for the feature class.
      feature_linked {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Choose whether the output annotation feature class
          will be linked to the
          features in another feature class. The feature-linked option will not be
          available with an ArcGIS for Desktop Basic license.

          * FEATURE_LINKED—The output annotation feature class will be linked to the
          features in another feature class.

          * STANDARD—The output annotation feature class will not be linked to the
          features in another feature class. This is the default.
      linked_feature_class {Feature Layer}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.The feature class to which you are linking annotation
          features. The feature
          class must be a point, line, or polygon feature class. If converting annotation
          into a desktop, workgroup, or enterprise geodatabase, the link feature class
          must not be registered as versioned.This option is only available if you choose
          FEATURE_LINKED for the previous
          parameter.
      create_annotation_when_feature_added {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether new annotation will be generated when
          you add new features to
          the feature class to which this annotation feature class is linked.This option
          is only available if you choose FEATURE_LINKED for the Feature-
          linked parameter and specify a Linked Feature Class.

          * AUTO_CREATE—The ArcMap Editor will automatically generate a new piece of
          annotation when you add new features to the feature class to which this
          annotation feature class is linked. This is the default.

          * NO_AUTO_CREATE—The ArcMap Editor will not automatically generate a new piece
          of annotation when you add new features to the feature class to which this
          annotation feature class is linked.
      update_annotation_when_feature_modified {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether to automatically update the placement
          of annotation when you
          edit features in the feature class to which this annotation feature class is
          linked.This option is only available if you choose FEATURE_LINKED for the
          Feature-
          linked parameter and specify a Linked Feature Class.

          * AUTO_UPDATE—The annotation will be repositioned according to the modified
          feature shape. This is the default.

          * NO_AUTO_UPDATE—The annotation will remain in its original position.

     OUTPUTS:
      output_featureclass (Feature Class):
          The geodatabase annotation feature class to which you want to convert CAD
          annotation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportCADAnnotation_conversion(*gp_fixargs((input_features, output_featureclass, reference_scale, use_levels, match_symbols_from_first_input, require_symbol_from_table, feature_linked, linked_feature_class, create_annotation_when_feature_added, update_annotation_when_feature_modified), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportCoverageAnnotation_conversion', None)
def ImportCoverageAnnotation(input_features=None, output_featureclass=None, reference_scale=None, use_levels=None, match_symbols_from_first_input=None, require_symbol_from_table=None, feature_linked=None, linked_feature_class=None, create_annotation_when_feature_added=None, update_annotation_when_feature_modified=None):
    """ImportCoverageAnnotation_conversion(input_features;input_features..., output_featureclass, reference_scale, {use_levels}, {match_symbols_from_first_input}, {require_symbol_from_table}, {feature_linked}, {linked_feature_class}, {create_annotation_when_feature_added}, {update_annotation_when_feature_modified})

        Converts a collection of coverage annotation features to geodatabase annotation.
        You can convert each level to individual annotation classes or merge them into a
        single class. Also, if you choose map layers as input, the level and font
        overrides will be honored.

     INPUTS:
      input_features (Feature Layer):
          The coverage annotation features that you want to convert to geodatabase
          annotation. If you choose a coverage annotation layer in ArcMap, the following
          properties of that layer will be honored during the conversion:

          * Visible drawing levels. Only those levels that are turned on for drawing will
          be converted.

          * Substitution of font and color properties for the text symbol.

          * Selection. Only the selected features will be converted.

          * Definition query. Only visible features that match the definition query will
          be converted.
      reference_scale (Double):
          Enter the scale to use as a reference for the annotation. This sets the scale to
          which all symbol and text sizes in the annotation will be based.
      use_levels {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether all coverage annotation drawing levels
          will be converted to
          annotation classes within the feature class.

          * CLASSES_FROM_LEVELS—Each coverage annotation drawing level will be converted
          to an annotation class, within the output feature class. This is the default.

          * ONE_CLASS_ONLY—All coverage annotation drawing levels will be converted to a
          single annotation class within the output feature class.
      match_symbols_from_first_input {Boolean}:
          If you are converting coverage annotation from more than one coverage or
          annotation subclass and need to substitute the font properties for a symbol and
          apply them to all the input features, you can use this option.

          * MATCH_FIRST_INPUT—Match the symbols from the first input layer and have them
          apply to all layers.

          * NO_MATCH—Each drawing file retains its own font properties. This is the
          default.
      require_symbol_from_table {Boolean}:
          Specify whether the output annotation features must reference a symbol stored in
          the symbol collection for the feature class.

          * NO_SYMBOL_REQUIRED—Any type of annotation (including graphics) may be stored
          in the annotation feature class. This is the default.

          * REQUIRE_SYMBOL—The annotation must reference one of the predefined symbols in
          the collection; the symbol cannot be stored inline.
      feature_linked {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Choose whether the output annotation feature class
          will be linked to the
          features in another feature class.

          * FEATURE_LINKED—The output annotation feature class will be linked to the
          features in another feature class.

          * STANDARD—The output annotation feature class will not be linked to the
          features in another feature class. This is the default.
      linked_feature_class {Feature Layer}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.The feature class to which you are linking annotation
          features. This option is
          only available if you choose FEATURE_LINKED for the feature_linked parameter.
      create_annotation_when_feature_added {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether new annotation will be generated when
          you add new features to
          the feature class to which this annotation feature class is linked.This option
          is only available if you choose FEATURE_LINKED for the
          feature_linked parameter and specify a value for the linked_feature_class
          parameter.

          * AUTO_CREATE—When editing in ArcMap, a new piece of annotation will be
          automatically generated when you add new features to the feature class to which
          this annotation feature class is linked. This is the default.

          * NO_AUTO_CREATE—When editing in ArcMap, a new piece of annotation will not be
          automatically generated when you add new features to the feature class to which
          this annotation feature class is linked.
      update_annotation_when_feature_modified {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specify whether the ArcMap Editor will automatically
          update the placement of
          annotation when you edit features in the feature class to which this annotation
          feature class is linked.This option is only available if you choose
          FEATURE_LINKED for the
          feature_linked parameter and specify a value for the linked_feature_class
          parameter.

          * AUTO_UPDATE—The annotation will be repositioned according to the modified
          feature shape. This is the default.

          * NO_AUTO_UPDATE—The annotation will remain in its original position.

     OUTPUTS:
      output_featureclass (Feature Class):
          Browse into an existing geodatabase and type in the name of the new annotation
          feature class to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportCoverageAnnotation_conversion(*gp_fixargs((input_features, output_featureclass, reference_scale, use_levels, match_symbols_from_first_input, require_symbol_from_table, feature_linked, linked_feature_class, create_annotation_when_feature_added, update_annotation_when_feature_modified), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToGeodatabase_conversion', None)
def RasterToGeodatabase(Input_Rasters=None, Output_Geodatabase=None, Configuration_Keyword=None):
    """RasterToGeodatabase_conversion(Input_Rasters;Input_Rasters..., Output_Geodatabase, {Configuration_Keyword})

        Loads multiple raster datasets into a geodatabase or raster catalog.If this tool
        is used to load raster datasets into a raster catalog, then you
        need to run the Calculate Default Spatial Grid Index tool after the loading is
        completed.

     INPUTS:
      Input_Rasters (Raster Dataset):
          Input raster dataset(s).
      Output_Geodatabase (Workspace / Raster Catalog):
          The path and name of a geodatabase or raster catalog.
      Configuration_Keyword {String}:
          Specifies the storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database
          administrator.Personal geodatabases do not use configuration keywords."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToGeodatabase_conversion(*gp_fixargs((Input_Rasters, Output_Geodatabase, Configuration_Keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToGeodatabase_conversion', None)
def TableToGeodatabase(Input_Table=None, Output_Geodatabase=None):
    """TableToGeodatabase_conversion(Input_Table;Input_Table..., Output_Geodatabase)

        Converts one or more tables to geodatabase tables in an output geodatabase. The
        inputs can be dBASE, INFO, VPF, OLE DB tables, geodatabase tables, or table
        views.

     INPUTS:
      Input_Table (Table View):
          The list of tables to be converted to geodatabase tables. Input tables can be
          INFO, dBASE, OLE DB, geodatabase tables, or table views.
      Output_Geodatabase (Workspace):
          The destination geodatabase where the tables will be placed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToGeodatabase_conversion(*gp_fixargs((Input_Table, Output_Geodatabase), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToTable_conversion', None)
def TableToTable(in_rows=None, out_path=None, out_name=None, where_clause=None, field_mapping=None, config_keyword=None):
    """TableToTable_conversion(in_rows, out_path, out_name, {where_clause}, {field_mapping}, {config_keyword})

        Converts an input table to a dBASE or geodatabase table.

     INPUTS:
      in_rows (Table View / Raster Layer):
          The input table to be converted to a new table.
      out_path (Workspace / Feature Dataset):
          The destination where the output table will be written.
      out_name (String):
          The name of the output table. If the output location is a folder, convert the
          input rows to a dBASE table by
          specifying a name with the extension .dbf, or convert the input rows to an INFO
          table by specifying a name with no extension. If the output location is a
          geodatabase, convert the input rows to a geodatabase table by specifying a name
          with no extension.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records. Learn more about SQL query
          expressions
      field_mapping {Field Mappings}:
          The fields and field contents chosen from the input table. You can add, rename,
          or delete output fields as well as set properties such as data type and merge
          rule.Learn more about choosing and setting the output fields.You can use the
          ArcPy FieldMappings object for this parameter.
      config_keyword {String}:
          Specifies the default storage parameters (configurations) for geodatabases in a
          relational database management system (RDBMS). This setting is applicable only
          when using enterprise geodatabase tables.Configuration keywords are set by the
          database administrator."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToTable_conversion(*gp_fixargs((in_rows, out_path, out_name, where_clause, field_mapping, config_keyword), True)))
        return retval
    except Exception, e:
        raise e


# To KML toolset
@gptooldoc('LayerToKML_conversion', None)
def LayerToKML(layer=None, out_kmz_file=None, layer_output_scale=None, is_composite=None, boundary_box_extent=None, image_size=None, dpi_of_client=None, ignore_zvalue=None):
    """LayerToKML_conversion(layer, out_kmz_file, {layer_output_scale}, {is_composite}, {boundary_box_extent}, {image_size}, {dpi_of_client}, {ignore_zvalue})

        This tool converts a feature or raster layer into a KML file containing a
        translation of Esri geometries and symbology. This file is compressed using ZIP
        compression, has a .kmz extension, and can be read by any KML client including
        ArcGIS Explorer, ArcGlobe, and Google Earth.

     INPUTS:
      layer (Layer):
          The feature or raster layer or layer file (.lyr) to be converted to KML.
      layer_output_scale {Double}:
          The scale at which to export the layer. This parameter is used with any scale
          dependency, such as layer visibility or scale-dependent rendering. If the layer
          is not visible at the export scale, it will not be included in the created KML
          file. Any value, such as 0, can be used if there are no scale dependencies.If
          exporting a layer that is to be displayed as 3D vectors and the is_composite
          parameter is set to NO_COMPOSITE you can set this parameter to any value, as
          long as your features do not have any scale-dependent rendering.Only numeric
          characters should be entered; for example, enter 20000 as the
          scale, not 1:20000 or 20,000.
      is_composite {Boolean}:
          * COMPOSITE—The output KML file will be a single composite image representing
          the raster or vector features in the source layer. The raster is draped over the
          terrain as a KML GroundOverlay. Select this option to reduce the size of the
          output KMZ file. When you check this box, individual features and layers in the
          KML are not selectable.

          * NO_COMPOSITE—If your layer has vector features, they are preserved as KML
          vectors. (If your layer is a raster, you can choose either option for this
          parameter without any visual difference.)
      boundary_box_extent {Extent}:
          The geographic extent of the area to be exported. The extent rectangle bounds
          should be specified as a space-delimited string of WGS84 geographic coordinates
          in the form left lower right upper (xmin, ymin, xmax, ymax).
      image_size {Long}:
          Defines the vertical and horizontal resolution of any rasters in the output KML
          document. Use this parameter with the DPI parameter to control output image
          resolution.
      dpi_of_client {Long}:
          Defines the device resolution for any rasters in the output KML document. Use
          this parameter with the Image Size parameter to control output image resolution.
      ignore_zvalue {Boolean}:
          * ABSOLUTE—Use the Z-values of features when creating KML. The features will be
          drawn inside KML clients relative to sea level.

          * CLAMPED_TO_GROUND—Override Z-values in your features and create KML with the
          features clamped to the ground. The features will be draped over the terrain.
          This setting is used for features that do not have Z-values. This is the
          default.

     OUTPUTS:
      out_kmz_file (File):
          The KML file to write. This file is compressed and has a .kmz extension. It can
          be read by any KML client including ArcGIS Explorer, ArcGlobe, and Google Earth."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LayerToKML_conversion(*gp_fixargs((layer, out_kmz_file, layer_output_scale, is_composite, boundary_box_extent, image_size, dpi_of_client, ignore_zvalue), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MapToKML_conversion', None)
def MapToKML(in_map_document=None, data_frame=None, out_kmz_file=None, map_output_scale=None, is_composite=None, is_vector_to_raster=None, extent_to_export=None, image_size=None, dpi_of_client=None, ignore_zvalue=None):
    """MapToKML_conversion(in_map_document, data_frame, out_kmz_file, {map_output_scale}, {is_composite}, {is_vector_to_raster}, {extent_to_export}, {image_size}, {dpi_of_client}, {ignore_zvalue})

        This tool converts a map document into a KML file containing a translation of
        Esri geometries and symbology. This file is compressed using ZIP compression,
        will have a .kmz extension, and can be read by any KML client including ArcGIS
        Explorer, ArcGlobe, and Google Earth.

     INPUTS:
      in_map_document (ArcMap Document):
          The map document to convert to KML.
      data_frame (String):
          The data frame of the map document to convert to KML.
      map_output_scale {Double}:
          The scale at which to export each layer in the map. This parameter is important
          with any scale dependency, such as layer visibility or scale-dependent
          rendering. If the layer is not visible at the export scale, it will not be
          included in the created KML file. Any value, such as 1, can be used if there are
          no scale dependencies.If exporting a layer that is to be displayed as 3D vectors
          and the is_composite
          parameter is set to NO_COMPOSITE, you can set this parameter to any value, as
          long as your features do not have any scale-dependent rendering.Only numeric
          characters should be entered; for example, enter 20000 as the
          scale, not 1:20000 or 20,000.
      is_composite {Boolean}:
          * COMPOSITE—Directs the output KML file to contain only a single image that
          composites all the features in this map into a single raster image. The raster
          is draped over the terrain as a KML GroundOverlay. Select this option to reduce
          the size of the output KMZ file. When you check this box, individual features
          and layers in the KML are not selectable. Also, the next parameter,
          is_vector_to_raster, is ignored.

          * NO_COMPOSITE—Layers are returned separately in the KML. Whether the layers are
          returned all as rasters or as a mix of vectors and rasters is determined by the
          next parameter, is_vector_to_raster.
      is_vector_to_raster {Boolean}:
          * VECTOR_TO_RASTER—Converts each vector layer in the map into a separate raster
          image in the KML output. Normal raster layers are also added to the KML output.
          Each output KML raster layer is selectable, and its transparency can be adjusted
          in certain KML clients.

          * VECTOR_TO_VECTOR—Preserves vector layers in the map as KML vectors.
      extent_to_export {Extent}:
          The geographic extent of the area to be exported. The extent rectangle bounds
          should be specified as a space-delimited string of WGS84 geographic coordinates
          in the form left lower right upper (xmin, ymin, xmax, ymax).
      image_size {Long}:
          Size of returned image in pixels. Defines the vertical and horizontal resolution
          of any rasters in the output KML document. Use this parameter with the DPI
          parameter to control output image resolution.
      dpi_of_client {Long}:
          Defines the device resolution for any rasters in the output KML document.
          Typical screen resolution is 96 dpi. If the data inside your map supports a high
          resolution and your KML requires it, consider increasing the value. Use this
          parameter with the Image Size parameter to control output image resolution.
      ignore_zvalue {Boolean}:
          * ABSOLUTE—Use the Z-values of features when creating KML. The features will be
          drawn inside KML clients relative to sea level.

          * CLAMPED_TO_GROUND—Override Z-values in your features and create KML with the
          features clamped to the ground. The features will be draped over the terrain.
          This setting is used for features that do not have Z-values. This is the
          default.

     OUTPUTS:
      out_kmz_file (File):
          The KML file to write. This file is compressed and will have a .kmz extension.
          It can be read by any KML client including ArcGIS Explorer, ArcGlobe, and Google
          Earth."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MapToKML_conversion(*gp_fixargs((in_map_document, data_frame, out_kmz_file, map_output_scale, is_composite, is_vector_to_raster, extent_to_export, image_size, dpi_of_client, ignore_zvalue), True)))
        return retval
    except Exception, e:
        raise e


# To Raster toolset
@gptooldoc('ASCIIToRaster_conversion', None)
def ASCIIToRaster(in_ascii_file=None, out_raster=None, data_type=None):
    """ASCIIToRaster_conversion(in_ascii_file, out_raster, {data_type})

        Converts an ASCII file representing raster data to a raster dataset.

     INPUTS:
      in_ascii_file (File):
          The input ASCII file to be converted.
      data_type {String}:
          The data type of the output raster dataset.

          * INTEGER—An integer raster dataset will be created.

          * FLOAT—A floating-point raster dataset will be created.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ASCIIToRaster_conversion(*gp_fixargs((in_ascii_file, out_raster, data_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DEMToRaster_conversion', None)
def DEMToRaster(in_dem_file=None, out_raster=None, data_type=None, z_factor=None):
    """DEMToRaster_conversion(in_dem_file, out_raster, {data_type}, {z_factor})

        Converts a digital elevation model (DEM) in a United States Geological Survey
        (USGS) format to a raster dataset.

     INPUTS:
      in_dem_file (File):
          The input USGS DEM file. The DEM must be standard USGS 7.5 minute, 1 degree, or
          any other file in the USGS DEM format. The DEM may be in either fixed or
          variable record-length format.
      data_type {String}:
          Data type of the output raster dataset.

          * INTEGER—An integer raster dataset will be created.

          * FLOAT—A floating-point raster dataset will be created. This is the default.
      z_factor {Double}:
          The number of ground x,y units in one surface z unit.The z-factor adjusts the
          units of measure for the z units when they are
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

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DEMToRaster_conversion(*gp_fixargs((in_dem_file, out_raster, data_type, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureToRaster_conversion', None)
def FeatureToRaster(in_features=None, field=None, out_raster=None, cell_size=None):
    """FeatureToRaster_conversion(in_features, field, out_raster, {cell_size})

        Converts features to a raster dataset.

     INPUTS:
      in_features (Composite Geodataset):
          The input feature dataset to be converted to a raster dataset.
      field (Field):
          The field used to assign values to the output raster.It can be any field of the
          input feature dataset's attribute table.If the Shape field of a point or
          multipoint dataset contains z or m values, then
          either of these can be used.
      cell_size {Analysis Cell Size}:
          The cell size for the output raster dataset.The default cell size is the
          shortest of the width or height of the extent of
          the input feature dataset, in the output spatial reference, divided by 250.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureToRaster_conversion(*gp_fixargs((in_features, field, out_raster, cell_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FloatToRaster_conversion', None)
def FloatToRaster(in_float_file=None, out_raster=None):
    """FloatToRaster_conversion(in_float_file, out_raster)

        Converts a file of binary floating-point values representing raster data to a
        raster dataset.

     INPUTS:
      in_float_file (File):
          The input floating-point binary file. The file must have a .flt extension. There
          must be a header file in association
          with the floating-point binary file, with a .hdr extension.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FloatToRaster_conversion(*gp_fixargs((in_float_file, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LasDatasetToRaster_conversion', None)
def LasDatasetToRaster(in_las_dataset=None, out_raster=None, value_field=None, interpolation_type=None, data_type=None, sampling_type=None, sampling_value=None, z_factor=None):
    """LasDatasetToRaster_conversion(in_las_dataset, out_raster, {value_field}, {interpolation_type}, {data_type}, {sampling_type}, {sampling_value}, {z_factor})

        Creates a raster using elevation, intensity, or RGB values stored in the lidar
        files (*.las) referenced by the LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      value_field {String}:
          The lidar data that will be used to generate the raster output.

          *  ELEVATION—Elevation from the lidar files will be used to create the raster.
          This is the default.

          *  INTENSITY—Intensity information from the lidar files will be used to create
          the raster.

          * RGB—RGB values from the lidar points will be used to create 3-band imagery.
      interpolation_type {Interpolate}:
          The interpolation technique that will be used to determine the cell values of
          the output raster.The binning approach provides a Cell Assignment Method for
          determining each
          output cell using the points that fall within its extent, along with a Void Fill
          Method to determine the value of cells that do not contain any LAS points.Cell
          Assignment Methods

          * AVERAGE—Assigns the average value of all points in the cell. This is the
          default.

          * MINIMUM—Assigns the minimum value found in the points within the cell.

          * MAXIMUM—Assigns the maximum value found in the points within the cell.

          * IDW—Uses Inverse Distance Weighted interpolation to determine the cell value.

          * NEAREST—Uses Nearest Neighbor assignment to determine the cell value.
          Void Fill Methods

          * NONE—NoData is assigned to the cell.

          * SIMPLE—Averages the values from data cells immediately surrounding a NoData
          cell to eliminate small voids.

          * LINEAR—Triangulates across void areas and uses linear interpolation on the
          triangulated value to determine the cell value. This is the default.

          * NATURAL_NEIGHBOR—Uses natural neighbor interpolation to determine the cell
          value.
          The Triangulation interpolation methods derive cell values using a TIN based
          approach while also offering the opportunity to speed up processing time by
          thinning the sampling of LAS data using the Window Size technique.Triangulation
          Methods

          * Linear—Uses linear interpolation to determine cell values.

          * Natural Neighbors—Uses natural neighbor interpolation to determine cell value.
          Window Size Selection Methods

          * Maximum—The point with the highest value in each window size is maintained.
          This is the default.

          * Minimum—The point with the lowest value in each window size is maintained.

          * Closest To Mean—The point whose value is closest to the average of all point
          values in the window size is maintained.
      data_type {String}:
          The data type of the output raster can be defined by the following keywords:

          * FLOAT—Output raster will use 32-bit floating point, which supports values
          ranging from -3.402823466e+38 to 3.402823466e+38. This is the default.

          * INT—Output raster will use an appropriate integer bit depth. This option will
          round Z-values to the nearest whole number and write an integer to each raster
          cell value.
      sampling_type {String}:
          Specifies the method used for interpreting the Sampling Value to define the
          resolution of the output raster.

          * OBSERVATIONS—Defines the number of cells that divide the lengthiest side of
          the LAS dataset extent.

          * CELLSIZE—Defines the cell size of the output raster. This is the default.
      sampling_value {Double}:
          Specifies the value used in conjunction with the Sampling Type to define the
          resolution of the output raster.
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
        retval = convertArcObjectToPythonObject(gp.LasDatasetToRaster_conversion(*gp_fixargs((in_las_dataset, out_raster, value_field, interpolation_type, data_type, sampling_type, sampling_value, z_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MultipatchToRaster_conversion', None)
def MultipatchToRaster(in_multipatch_features=None, out_raster=None, cell_size=None):
    """MultipatchToRaster_conversion(in_multipatch_features, out_raster, {cell_size})

        Converts multipatch features to a raster dataset.

     INPUTS:
      in_multipatch_features (Composite Geodataset):
          The input multipatch features to be converted to a raster.
      cell_size {Analysis Cell Size}:
          The cell size for the output raster dataset.The default cell size is the
          shortest of the width or height of the extent of
          the input feature dataset, in the output spatial reference, divided by 250.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.It will be of floating point type.When
          not saving to a geodatabase, specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MultipatchToRaster_conversion(*gp_fixargs((in_multipatch_features, out_raster, cell_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PointToRaster_conversion', None)
def PointToRaster(in_features=None, value_field=None, out_rasterdataset=None, cell_assignment=None, priority_field=None, cellsize=None):
    """PointToRaster_conversion(in_features, value_field, out_rasterdataset, {cell_assignment}, {priority_field}, {cellsize})

        Converts point features to a raster dataset.

     INPUTS:
      in_features (Feature Layer):
          The point or multipoint input feature dataset to be converted to a raster.
      value_field (Field):
          The field used to assign values to the output raster.It can be any field of the
          input feature dataset's attribute table.If the Shape field of a point or
          multipoint dataset contains z or m values, then
          either of these can be used.
      cell_assignment {String}:
          The method to determine how the cell will be assigned a value when more than one
          feature falls within a cell.

          * MOST_FREQUENT—If there is more than one feature within the cell, the one with
          the most common attribute, in the Value field, is assigned to the cell. If they
          have the same number of common attributes, the one with the lowest FID is used.

          * SUM—The sum of the attributes of all the points within the cell (not valid for
          string data).

          * MEAN—The mean of the attributes of all the points within the cell (not valid
          for string data).

          * STANDARD_DEVIATION—The standard deviation of attributes of all the points
          within the cell. If there are less than two points in the cell, the cell is
          assigned NoData (not valid for string data).

          * MAXIMUM—The maximum value of the attributes of the points within the cell (not
          valid for string data).

          * MINIMUM—The minimum value of the attributes of the points within the cell (not
          valid for string data).

          * RANGE—The range of the attributes of the points within the cell (not valid for
          string data).

          * COUNT—The number of points within the cell.
      priority_field {Field}:
          This field is used when a feature should take preference over another feature
          with the same attribute.Priority field is only used with the MOST_FREQUENT cell
          assignment type option.
      cellsize {Analysis Cell Size}:
          The cell size for the output raster dataset.The default cell size is the
          shortest of the width or height of the extent of
          the input feature dataset, in the output spatial reference, divided by 250.

     OUTPUTS:
      out_rasterdataset (Raster Dataset / Raster Catalog):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PointToRaster_conversion(*gp_fixargs((in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PolygonToRaster_conversion', None)
def PolygonToRaster(in_features=None, value_field=None, out_rasterdataset=None, cell_assignment=None, priority_field=None, cellsize=None):
    """PolygonToRaster_conversion(in_features, value_field, out_rasterdataset, {cell_assignment}, {priority_field}, {cellsize})

        Converts polygon features to a raster dataset.

     INPUTS:
      in_features (Feature Layer):
          The polygon input feature dataset to be converted to a raster.
      value_field (Field):
          The field used to assign values to the output raster.It can be any field of the
          input feature dataset's attribute table.
      cell_assignment {String}:
          The method to determine how the cell will be assigned a value when more than one
          feature falls within a cell.

          * CELL_CENTER—The polygon that overlaps the center of the cell yields the
          attribute to assign to the cell.

          * MAXIMUM_AREA—The single feature with the largest area within the cell yields
          the attribute to assign to the cell.

          * MAXIMUM_COMBINED_AREA— If there is more than one feature in a cell with the
          same value, the areas of these features will be combined. The combined feature
          with the largest area within the cell will determine the value to assign to the
          cell.
      priority_field {Field}:
          This field is used to determine which feature should take preference over
          another feature that falls over a cell. When it is used, the feature with the
          largest positive priority is always selected for conversion irrespective of the
          Cell assignment type chosen.
      cellsize {Analysis Cell Size}:
          The cell size for the output raster dataset.The default cell size is the
          shortest of the width or height of the extent of
          the input feature dataset, in the output spatial reference, divided by 250.

     OUTPUTS:
      out_rasterdataset (Raster Dataset / Raster Catalog):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PolygonToRaster_conversion(*gp_fixargs((in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PolylineToRaster_conversion', None)
def PolylineToRaster(in_features=None, value_field=None, out_rasterdataset=None, cell_assignment=None, priority_field=None, cellsize=None):
    """PolylineToRaster_conversion(in_features, value_field, out_rasterdataset, {cell_assignment}, {priority_field}, {cellsize})

        Converts polyline features to a raster dataset.

     INPUTS:
      in_features (Feature Layer):
          The polyline input feature dataset to be converted to a raster.
      value_field (Field):
          The field used to assign values to the output raster.It can be any field of the
          input feature dataset's attribute table.
      cell_assignment {String}:
          The method to determine how the cell will be assigned a value when more than one
          feature falls within a cell.

          * MAXIMUM_LENGTH—The feature with the longest length that covers the cell will
          determine the value to assign to the cell.

          * MAXIMUM_COMBINED_LENGTH—If there is more than one feature in a cell with the
          same value, the lengths of these features will be combined. The combined feature
          with the longest length within the cell will determine the value to assign to
          the cell.
      priority_field {Field}:
          This field is used to determine which feature should take preference over
          another feature that falls over a cell. When it is used, the feature with the
          largest positive priority is always selected for conversion irrespective of the
          Cell assignment type chosen.
      cellsize {Analysis Cell Size}:
          The cell size for the output raster dataset.The default cell size is the
          shortest of the width or height of the extent of
          the input feature dataset, in the output spatial reference, divided by 250.

     OUTPUTS:
      out_rasterdataset (Raster Dataset / Raster Catalog):
          The output raster dataset to be created.When not saving to a geodatabase,
          specify .tif for a TIFF file format, .img for
          an ERDAS IMAGINE file format, or no extension for an Esri Grid raster format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PolylineToRaster_conversion(*gp_fixargs((in_features, value_field, out_rasterdataset, cell_assignment, priority_field, cellsize), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToOtherFormat_conversion', None)
def RasterToOtherFormat(Input_Rasters=None, Output_Workspace=None, Raster_Format=None):
    """RasterToOtherFormat_conversion(Input_Rasters;Input_Rasters..., Output_Workspace, {Raster_Format})

        Converts a raster dataset from one format to another.

     INPUTS:
      Input_Rasters (Raster Dataset):
          Select the raster dataset you want to convert.
      Output_Workspace (Workspace / Raster Catalog):
          Select the folder where you will save the raster dataset in its new format.
      Raster_Format {String}:
          Select the format of the new raster dataset.

          * BIL—Esri Band Interleaved by Line file.

          * BIP—Esri Band Interleaved by Pixel file.

          * BMP—Microsoft bitmap graphic raster dataset format.

          * BSQ—Esri Band Sequential file.

          * DAT—ENVI DAT file.

          * GIF—Graphic Interchange Format for raster datasets.

          * GRID—Esri Grid raster dataset format.

          * IMAGINE Image—ERDAS IMAGINE raster data format.

          * JP2000—JPEG 2000 raster dataset format.

          * JPEG—Joint Photographic Experts Group raster dataset format.

          * PNG—Portable Network Graphic raster dataset format.

          * TIFF—Tagged Image File Format for raster datasets."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToOtherFormat_conversion(*gp_fixargs((Input_Rasters, Output_Workspace, Raster_Format), True)))
        return retval
    except Exception, e:
        raise e


# To Shapefile toolset
@gptooldoc('FeatureClassToShapefile_conversion', None)
def FeatureClassToShapefile(Input_Features=None, Output_Folder=None):
    """FeatureClassToShapefile_conversion(Input_Features;Input_Features..., Output_Folder)

        Copies the features from one or more feature classes or layers to a folder of
        shapefiles.

     INPUTS:
      Input_Features (Feature Layer):
          The list of input feature classes or feature layers that will be converted and
          added to the output folder.
      Output_Folder (Folder):
          The folder where the shapefiles will be written."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureClassToShapefile_conversion(*gp_fixargs((Input_Features, Output_Folder), True)))
        return retval
    except Exception, e:
        raise e


# To dBASE toolset
@gptooldoc('TableToDBASE_conversion', None)
def TableToDBASE(Input_Table=None, Output_Folder=None):
    """TableToDBASE_conversion(Input_Table;Input_Table..., Output_Folder)

        Converts one or more tables to dBASE tables.

     INPUTS:
      Input_Table (Table View):
          The list of tables to be converted to dBASE.
      Output_Folder (Folder):
          The destination folder where the output dBASE tables will be placed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToDBASE_conversion(*gp_fixargs((Input_Table, Output_Folder), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject