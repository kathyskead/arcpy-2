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
"""The Data Management toolbox provides a rich and varied collection of tools that
are used to develop, manage, and maintain feature classes, datasets, layers, and
raster data structures."""
__all__ = ['DeleteRows', 'CopyRows', 'CopyFeatures', 'Dissolve', 'MakeFeatureLayer', 'SaveToLayerFile', 'AddJoin', 'RemoveJoin', 'Copy', 'Delete', 'Rename', 'CreatePersonalGDB', 'CreateArcInfoWorkspace', 'CreateFolder', 'CreateFeatureDataset', 'PivotTable', 'CreateFeatureclass', 'CreateTable', 'MakeTableView', 'AddIndex', 'RemoveIndex', 'AddSpatialIndex', 'RemoveSpatialIndex', 'CreateDomain', 'DeleteDomain', 'AddCodedValueToDomain', 'DeleteCodedValueFromDomain', 'SetValueForRangeDomain', 'AssignDomainToField', 'RemoveDomainFromField', 'TableToDomain', 'DomainToTable', 'SelectData', 'AddXY', 'SelectLayerByAttribute', 'SelectLayerByLocation', 'CalculateDefaultGridIndex', 'GetCount', 'CreateVersion', 'DeleteVersion', 'RegisterAsVersioned', 'UnregisterAsVersioned', 'AlterVersion', 'Analyze', 'CreateRelationshipClass', 'TableToRelationshipClass', 'FeatureToPoint', 'FeatureVerticesToPoints', 'FeatureToLine', 'FeatureToPolygon', 'PolygonToLine', 'SplitLine', 'DefineProjection', 'Eliminate', 'RepairGeometry', 'CreateTopology', 'AddFeatureClassToTopology', 'RemoveFeatureClassFromTopology', 'AddRuleToTopology', 'RemoveRuleFromTopology', 'ValidateTopology', 'SetClusterTolerance', 'MakeQueryTable', 'MakeXYEventLayer', 'UpdateAnnotation', 'AppendAnnotation', 'MakeRasterLayer', 'Flip', 'Mirror', 'ProjectRaster', 'Rescale', 'Rotate', 'Shift', 'Warp', 'Append', 'DeleteFeatures', 'MakeRasterCatalogLayer', 'AddField', 'AssignDefaultToField', 'CalculateField', 'DeleteField', 'MultipartToSinglepart', 'Integrate', 'Merge', 'MergeBranch', 'FeatureCompare', 'FileCompare', 'RasterCompare', 'TableCompare', 'CreateCustomGeoTransformation', 'CreateFishnet', 'CreateFileGDB', 'UpgradeSpatialReference', 'Adjust3DZ', 'Compress', 'CompareReplicaSchema', 'CreateReplica', 'CreateReplicaFootPrints', 'CreateReplicaFromServer', 'ExportAcknowledgementMessage', 'ExportDataChangeMessage', 'ExportReplicaSchema', 'ImportMessage', 'ImportReplicaSchema', 'ReExportUnacknowledgedMessages', 'SynchronizeChanges', 'AddSubtype', 'RemoveSubtype', 'SetDefaultSubtype', 'SetSubtypeField', 'CalculateValue', 'CreateRandomPoints', 'AddColormap', 'BuildRasterAttributeTable', 'DeleteColormap', 'DeleteRasterAttributeTable', 'BuildPyramids', 'CalculateStatistics', 'GetRasterProperties', 'CopyRaster', 'CreateRandomRaster', 'CreateRasterDataset', 'Mosaic', 'WorkspaceToRasterDataset', 'CopyRasterCatalogItems', 'CreateRasterCatalog', 'DeleteRasterCatalogItems', 'WorkspaceToRasterCatalog', 'CreateOrthoCorrectedRasterDataset', 'CreatePansharpenedRasterDataset', 'Clip', 'CompositeBands', 'Resample', 'ExportRasterWorldFile', 'GetCellValue', 'RasterCatalogToRasterDataset', 'ExtractSubDataset', 'TINCompare', 'MakeImageServerLayer', 'MakeWCSLayer', 'ApplySymbologyFromLayer', 'ExportRasterCatalogPaths', 'RepairRasterCatalogPaths', 'MigrateStorage', 'MosaicToNewRaster', 'Dice', 'SplitLineAtPoint', 'UnsplitLine', 'SplitRaster', 'EliminatePolygonPart', 'MakeGraph', 'SaveGraph', 'PointsToLine', 'ChangeVersion', 'RegisterWithGeodatabase', 'UpgradeGDB', 'CalculateDefaultClusterTolerance', 'DeleteIdentical', 'FindIdentical', 'ConsolidateLayer', 'ConsolidateMap', 'PackageLayer', 'PackageMap', 'ChangePrivileges', 'CreateSpatialReference', 'RasterToDTED', 'BearingDistanceToLine', 'TableToEllipse', 'XYToLine', 'ConvertCoordinateNotation', 'CompressFileGeodatabaseData', 'UncompressFileGeodatabaseData', 'ExtractPackage', 'SharePackage', 'BuildPyramidsandStatistics', 'MakeMosaicLayer', 'MinimumBoundingGeometry', 'AddRastersToMosaicDataset', 'BuildBoundary', 'BuildFootprints', 'BuildOverviews', 'BuildSeamlines', 'CalculateCellSizeRanges', 'ColorBalanceMosaicDataset', 'ComputeDirtyArea', 'CreateMosaicDataset', 'CreateReferencedMosaicDataset', 'DefineMosaicDatasetNoData', 'DefineOverviews', 'GenerateExcludeArea', 'ImportMosaicDatasetGeometry', 'RemoveRastersFromMosaicDataset', 'SynchronizeMosaicDataset', 'CalculateEndTime', 'ConvertTimeField', 'ConvertTimeZone', 'TransposeFields', 'AddGlobalIDs', 'WarpFromFile', 'ExportXMLWorkspaceDocument', 'ImportXMLWorkspaceDocument', 'AlterMosaicDatasetSchema', 'AnalyzeMosaicDataset', 'Compact', 'ClearWorkspaceCache', 'AnalyzeDatasets', 'RebuildIndexes', 'CheckGeometry', 'ReconcileVersions', 'CreateArcSDEConnectionFile', 'AddEdgeEdgeConnectivityRuleToGeometricNetwork', 'AddEdgeJunctionConnectivityRuleToGeometricNetwork', 'CreateGeometricNetwork', 'RemoveConnectivityRuleFromGeometricNetwork', 'RemoveEmptyFeatureClassFromGeometricNetwork', 'TraceGeometricNetwork', 'AddAttachments', 'DisableAttachments', 'EnableAttachments', 'RemoveAttachments', 'ExportTopologyErrors', 'SetMosaicDatasetProperties', 'SetRasterProperties', 'MakeLasDatasetLayer', 'DownloadRasters', 'CreateEnterpriseGeodatabase', 'EnableEnterpriseGeodatabase', 'FeatureEnvelopeToPolygon', 'MakeQueryLayer', 'SetFlowDirection', 'CreateDatabaseConnection', 'DeleteMosaicDataset', 'CreateSpatialType', 'GenerateAttachmentMatchTable', 'ConsolidateLocator', 'PackageLocator', 'CreateDatabaseView', 'SortCodedValueDomain', 'DisableEditorTracking', 'EnableEditorTracking', 'TruncateTable', 'ConsolidateResult', 'PackageResult', 'UpgradeDataset', 'AddFilesToLasDataset', 'CreateLasDataset', 'LasDatasetStatistics', 'LasPointStatsAsRaster', 'RemoveFilesFromLasDataset', 'ExportMosaicDatasetPaths', 'RepairMosaicDatasetPaths', 'CreateDatabaseUser', 'JoinField', 'EditRasterFunction', 'BuildMosaicDatasetItemCache', 'CreateUnRegisteredFeatureclass', 'CreateUnRegisteredTable', 'BatchBuildPyramids', 'BatchCalculateStatistics', 'RecoverFileGDB', 'Sort', 'CreateMapTilePackage', 'MatchPhotosToRowsByTime', 'GeoTaggedPhotosToPoints', 'RegisterRaster', 'AddIncrementingIDField', 'CreateRole', 'ExportTileCache', 'GenerateTileCacheTilingScheme', 'ImportTileCache', 'ManageTileCache', 'DisableArchiving', 'EnableArchiving', 'MergeMosaicDatasetItems', 'SplitMosaicDatasetItems', 'ComputePansharpenWeights', 'DetectFeatureChanges', 'Project', 'BatchProject', 'AddGeometryAttributes', 'MigrateRelationshipClass', 'FindDisconnectedFeaturesInGeometricNetwork', 'ExportMosaicDatasetGeometry', 'ExportMosaicDatasetItems', 'CreateRuntimeContent', 'RebuildGeometricNetwork', 'VerifyAndRepairGeometricNetworkConnectivity', 'AddFieldConflictFilter', 'RemoveFieldConflictFilter', 'GenerateFgdbLicense', 'GenerateLicensedFgdb', 'AnalyzeControlPoints', 'AppendControlPoints', 'ApplyBlockAdjustment', 'ComputeBlockAdjustment', 'ComputeControlPoints', 'ComputeTiePoints', 'ExportGeodatabaseConfigurationKeywords', 'ImportGeodatabaseConfigurationKeywords', 'AlterField', 'GeodeticDensify', 'ConfigureGeodatabaseLogFileTables', 'CreateRasterType', 'DeleteSchemaGeodatabase', 'DiagnoseVersionMetadata', 'DiagnoseVersionTables', 'RepairVersionMetadata', 'RepairVersionTables', 'AnalyzeToolsForPro']

# Deprecated tools
__all__ += ['CreateVersionedView', 'ReconcileVersion']

__alias__ = u'management'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
import _management
from _management import *
__all__ += _management.__all__

# Archiving toolset
@gptooldoc('DisableArchiving_management', None)
def DisableArchiving(in_dataset=None, preserve_history=None):
    """DisableArchiving_management(in_dataset, {preserve_history})

        Disables archiving on a geodatabase feature class, table, or feature dataset.

     INPUTS:
      in_dataset (Table / Feature Class / Feature Dataset):
          Geodatabase feature class, table, or feature dataset for which archiving will
          be disabled.
      preserve_history {Boolean}:
          Determines if records that are not from the current moment will be deleted or
          preserved.If the table or feature class is versioned, the history table or
          feature will
          become available.For nonversioned data, a new table or feature class will be
          created that
          contains the history information. The name of the new dataset will be the same
          as the input with an _h appended.

          * PRESERVE—Records that are not from the current moment will be preserved. This
          is the default.

          * DELETE—Records that are not from the current moment will be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DisableArchiving_management(*gp_fixargs((in_dataset, preserve_history), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EnableArchiving_management', None)
def EnableArchiving(in_dataset=None):
    """EnableArchiving_management(in_dataset)

        Enables archiving on a table, feature layer, or feature dataset.

     INPUTS:
      in_dataset (Table / Feature Class / Feature Dataset):
          The name of the dataset on which to enable archiving."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EnableArchiving_management(*gp_fixargs((in_dataset,), True)))
        return retval
    except Exception, e:
        raise e


# Attachments toolset
@gptooldoc('AddAttachments_management', None)
def AddAttachments(in_dataset=None, in_join_field=None, in_match_table=None, in_match_join_field=None, in_match_path_field=None, in_working_folder=None):
    """AddAttachments_management(in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_path_field, {in_working_folder})

        Adds file attachments to the records of a geodatabase feature class or table.
        The attachments are stored internally in the geodatabase in a separate
        attachment table that maintains linkage to the target dataset. Attachments are
        added to the target dataset using a match table that dictates for each input
        record (or an attribute group of records) the path to a file to add as an
        attachment to that record.

     INPUTS:
      in_dataset (Table View):
          Geodatabase table or feature class to add attachments to. Attachments are not
          added directly to this table, but rather to a related attachment table that
          maintains linkage to the input dataset.The input dataset must be stored in a
          version 10.0 or later geodatabase, and the
          table must have attachments enabled.
      in_join_field (Field):
          Field from the Input Dataset that has values that match the values in the Match
          Join Field. Records that have join field values that match between the Input
          Dataset and the Match Table will have attachments added. This field can be an
          Object ID field or any other identifying attribute.
      in_match_table (Table View):
          Table that identifies which input records will have attachments added and the
          paths to those attachments.
      in_match_join_field (Field):
          Field from the match table that indicates which records in the Input Dataset
          will have specified attachments added. This field can have values that match
          Input Dataset Object IDs or some other identifying attribute.
      in_match_path_field (Field):
          Field from the match table that contains paths to the attachments to add to
          Input Dataset records.
      in_working_folder {Folder}:
          Folder or workspace where attachment files are centralized. By specifying a
          working folder, the paths in the Match Path Field can be the short names of
          files relative to the working folder. For example, if loading attachments with
          paths like C:\MyPictures\image1.jpg,
          C:\MyPictures\image2.jpg, set the Working Folder to C:\MyPictures, then paths in
          the Match Path Field can be the short names such as image1.jpg and image2.jpg,
          instead of the longer full paths."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddAttachments_management(*gp_fixargs((in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_path_field, in_working_folder), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DisableAttachments_management', None)
def DisableAttachments(in_dataset=None):
    """DisableAttachments_management(in_dataset)

        Disables attachments on a geodatabase feature class or table. Deletes the
        attachment relationship class and attachment table.

     INPUTS:
      in_dataset (Table View):
          Geodatabase table or feature class for which attachments will be disabled. The
          input must be in a version 10 or later geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DisableAttachments_management(*gp_fixargs((in_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EnableAttachments_management', None)
def EnableAttachments(in_dataset=None):
    """EnableAttachments_management(in_dataset)

        Enables attachments on a geodatabase feature class or table. Creates the
        necessary attachment relationship class and attachment table that will
        internally store attachment files.

     INPUTS:
      in_dataset (Table View):
          Geodatabase table or feature class for which attachments will be enabled. The
          input must be in a version 10 or later geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EnableAttachments_management(*gp_fixargs((in_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateAttachmentMatchTable_management', None)
def GenerateAttachmentMatchTable(in_dataset=None, in_folder=None, out_match_table=None, in_key_field=None, in_file_filter=None, in_use_relative_paths=None):
    """GenerateAttachmentMatchTable_management(in_dataset, in_folder, out_match_table, in_key_field, {in_file_filter}, {in_use_relative_paths})

        ArcGIS geoprocessing tool that creates a match table to be used with the Add
        Attachments and Remove Attachments tools.

     INPUTS:
      in_dataset (Table View):
          Input dataset that contains records that will have files attached.
      in_folder (Folder):
          Folder that contains files to attach.
      in_key_field (Field):
          The values in this field will match the names of the files in the input folder.
          The matching behavior will ignore file extensions, which allows multiple files
          with various file extensions to match with a single record in the input
          dataset.For example, if the input Key Field value is lot5986, a file on disk
          named
          lot5986.jpg would match with this record.
      in_file_filter {String}:
          This parameter is used to limit the files the tool considers for matching. If
          the file name does not meet the criteria in the file filter parameter it will
          not be processed and therefore will not show up in the output match table. Wild
          cards (*) can be used in this parameter for more flexible filtering options.
          Multiple semicolon-delimited filters can be used as well.For example, consider a
          directory that contains the following files: parcel.tif,
          parcel.doc, parcel.jpg, houses.jpg, and report.pdf.To limit the possible matches
          in this list to .jpg files, use *.jpg.To limit the possible matches in this list
          to .pdf and .doc files, use *.pdf;
          *.doc.To limit the possible matches in this list to files beginning with parcel,
          use
          parcel*.To limit the possible matches in this list to files that contain the
          text arc,
          use *arc*.
      in_use_relative_paths {Boolean}:
          Determines if the output match table field FILENAME will contain a full path to
          the dataset or only the file name.

          * RELATIVE—The output FILENAME field will contain relative paths. This is the
          default.

          * ABSOLUTE—The output FILENAME field will contain full paths to the data.

     OUTPUTS:
      out_match_table (Table):
          Table that will be generated which contains two columns: MATCHID and FILENAME."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateAttachmentMatchTable_management(*gp_fixargs((in_dataset, in_folder, out_match_table, in_key_field, in_file_filter, in_use_relative_paths), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveAttachments_management', None)
def RemoveAttachments(in_dataset=None, in_join_field=None, in_match_table=None, in_match_join_field=None, in_match_name_field=None):
    """RemoveAttachments_management(in_dataset, in_join_field, in_match_table, in_match_join_field, {in_match_name_field})

        Removes attachments from geodatabase feature class or table records. Since
        attachments are not actually stored in the input dataset, no changes will be
        made to that feature class or table, but rather to the related geodatabase table
        that stores the attachments and maintains linkage with the input dataset. A
        match table is used to identify which input records (or attribute groups of
        records) will have attachments removed.

     INPUTS:
      in_dataset (Table View):
          Geodatabase table or feature class from which to remove attachments.
          Attachments are not removed directly from this table, but rather from the
          related attachment table that stores the attachments. The Input Dataset must be
          in a version 10 or later geodatabase, and the table must have attachments
          enabled.
      in_join_field (Field):
          Field from the Input Dataset that has values which match the values in the
          Match Join Field. Records that have join field values that match between the
          Input Dataset and the Match Table will have attachments removed. This field can
          be an Object ID field or any other identifying attribute.
      in_match_table (Table View):
          Table that identifies which input records will have attachments removed.
      in_match_join_field (Field):
          Field from the match table that indicates which records in the Input Dataset
          will have specified attachments removed. This field can have values that match
          Input Dataset Object IDs or some other identifying attribute.
      in_match_name_field {Field}:
          Field from the match table that has the names of attachments to remove from
          Input Dataset records. If no name field is specified, all attachments will be
          removed from each record specified in the Match Join Field. If a name field is
          specified, but a record has a null or empty value in the name field, all
          attachments will be removed from that record. This field's values should be the
          short names of the attachment to remove, not the full paths to the files used to
          make the original attachments."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveAttachments_management(*gp_fixargs((in_dataset, in_join_field, in_match_table, in_match_join_field, in_match_name_field), True)))
        return retval
    except Exception, e:
        raise e


# Data Comparison toolset
@gptooldoc('DetectFeatureChanges_management', None)
def DetectFeatureChanges(update_features=None, base_features=None, out_feature_class=None, search_distance=None, match_fields=None, out_match_table=None, change_tolerance=None, compare_fields=None):
    """DetectFeatureChanges_management(update_features, base_features, out_feature_class, search_distance, {match_fields;match_fields...}, {out_match_table}, {change_tolerance}, {compare_fields;compare_fields...})

        Finds where the update line features spatially match the base line features and
        detects spatial changes, attribute changes, or both, as well as no change, and
        creates an output feature class containing matched update features with
        information about their changes, unmatched update features, and unmatched base
        features.

     INPUTS:
      update_features (Feature Layer):
          Line features to compare to the base features.
      base_features (Feature Layer):
          Line features to be compared with update features for change detection.
      search_distance (Linear unit):
          The distance used to search for match candidates. A distance must be specified
          and it must be greater than zero. You can choose a preferred unit; the default
          is the feature unit.
      match_fields {Value Table}:
          Lists of fields from update and base features. If specified, each pair of
          fields are checked for match candidates to help determine the right match.
      change_tolerance {Linear unit}:
          The distance used to determine if there is a spatial change.  All matched
          update features and base features are checked against this tolerance. If any
          parts of an update feature or base feature falls outside the zone around the
          matched feature, it is considered a spatial change. A distance can be equal to
          or greater than zero. The default is 0. When a value greater than zero is
          specified, the output will include LEN_PCT and LEN_ABS fields. You can choose a
          preferred unit; the default is the feature unit.
      compare_fields {Value Table}:
          Fields to determine if there is an attribute change between matched update and
          base features.

     OUTPUTS:
      out_feature_class (Feature Class):
          Output line feature class with change information. The output contains all
          participating update features (matched and unmatched) and any unmatched base
          features.
      out_match_table {Table}:
          The output table containing complete feature matching information."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DetectFeatureChanges_management(*gp_fixargs((update_features, base_features, out_feature_class, search_distance, match_fields, out_match_table, change_tolerance, compare_fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureCompare_management', None)
def FeatureCompare(in_base_features=None, in_test_features=None, sort_field=None, compare_type=None, ignore_options=None, xy_tolerance=None, m_tolerance=None, z_tolerance=None, attribute_tolerances=None, omit_field=None, continue_compare=None, out_compare_file=None):
    """FeatureCompare_management(in_base_features, in_test_features, sort_field;sort_field..., {compare_type}, {ignore_options;ignore_options...}, {xy_tolerance}, {m_tolerance}, {z_tolerance}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...}, {continue_compare}, {out_compare_file})

        Compares two feature classes or layers and returns the comparison results.
        Feature Compare can report differences with geometry, tabular values, spatial
        reference, and field definitions.

     INPUTS:
      in_base_features (Feature Layer):
          The Input Base Features are compared with the Input Test Features. Input Base
          Features refers to data that you have declared valid. This base data has the
          correct geometry definitions, field definitions, and spatial reference.
      in_test_features (Feature Layer):
          The Input Test Features are compared against the Input Base Features. Input Test
          Features refers to data that you have made changes to by editing or compiling
          new features.
      sort_field (Value Table):
          The field or fields used to sort records in the Input Base Table and the Input
          Test Table. The records are sorted in ascending order. Sorting by a common field
          in both the Input Base Features and the Input Test Features ensures that you are
          comparing the same row from each input dataset.
      compare_type {String}:
          The comparision type. The default is All, which will compare all properties of
          the features being compared.

          * ALL —All properties of the feature classes will be compared. This is the
          default.

          * GEOMETRY_ONLY —Only the geometries of the feature classes will be compared.

          * ATTRIBUTES_ONLY —Only the attributes and their values will be compared.

          * SCHEMA_ONLY —Only the schema of the feature classes will be compared.

          * SPATIAL_REFERENCE_ONLY —Only the spatial references of the two feature classes
          will be compared.
      ignore_options {String}:
          These properties will not be compared during comparison.

          * IGNORE_M —Do not compare measure properties.

          * IGNORE_Z —Do not compare elevation properties.

          * IGNORE_POINTID —Do not compare point id properties.

          * IGNORE_EXTENSION_PROPERTIES —Do not compare extension properties.

          * IGNORE_SUBTYPES —Do not compare subtypes.

          * IGNORE_RELATIONSHIPCLASSES —Do not compare relationship classes.

          * IGNORE_REPRESENTATIONCLASSES —Do not compare representation classes.
      xy_tolerance {Linear unit}:
          The distance that determines the range in which features are considered equal.
          To minimize error, the value you choose for the compare tolerance should be as
          small as possible. By default, the compare tolerance is the XY Tolerance of the
          input base features.
      m_tolerance {Double}:
          The measure tolerance is the minimum distance between measures before they are
          considered equal.
      z_tolerance {Double}:
          The Z Tolerance is the minimum distance between Z coordinates before they are
          considered equal.
      attribute_tolerances {Value Table}:
          The numeric value that determines the range in which attribute values are
          considered equal. This only applies to numeric field types.
      omit_field {String}:
          The field or fields that will be omitted during comparison. The field
          definitions and the tabular values for these fields will be ignored.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the first
          mismatch.

          * NO_CONTINUE_COMPARE—Stops after encountering the first mismatch. This is the
          default.

          * CONTINUE_COMPARE—Compares other properties after encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences between the Input Base
          Features and the Input Test Features. This file is a comma-delimited text file
          that can be viewed and used as a table in ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureCompare_management(*gp_fixargs((in_base_features, in_test_features, sort_field, compare_type, ignore_options, xy_tolerance, m_tolerance, z_tolerance, attribute_tolerances, omit_field, continue_compare, out_compare_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FileCompare_management', None)
def FileCompare(in_base_file=None, in_test_file=None, file_type=None, continue_compare=None, out_compare_file=None):
    """FileCompare_management(in_base_file, in_test_file, {file_type}, {continue_compare}, {out_compare_file})

        Compares two files and returns the comparison results. File Compare can report
        differences between two ASCII files or two binary files.

     INPUTS:
      in_base_file (File):
          The Input Base File is compared with the Input Test File. The Input Base File
          refers to a file that you have declared valid. This base file has the correct
          content and information.
      in_test_file (File):
          The Input Test File is compared against the Input Base File. The Input Test File
          refers to a file that you have made changes to by editing or compiling new
          information.
      file_type {String}:
          The type of files being compared.

          * ASCII —Compare using ASCII characters. This is the default.

          * BINARY —Perform a binary compare.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the first
          mismatch.

          * NO_CONTINUE_COMPARE—Stops after encountering the first mismatch. This is the
          default.

          * CONTINUE_COMPARE—Compares other properties after encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences between the Input Base
          File and the Input Test File. This file is a comma-delimited text file which can
          be viewed and used as a table in ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FileCompare_management(*gp_fixargs((in_base_file, in_test_file, file_type, continue_compare, out_compare_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterCompare_management', None)
def RasterCompare(in_base_raster=None, in_test_raster=None, compare_type=None, ignore_option=None, continue_compare=None, out_compare_file=None, parameter_tolerances=None, attribute_tolerances=None, omit_field=None):
    """RasterCompare_management(in_base_raster, in_test_raster, {compare_type}, {ignore_option;ignore_option...}, {continue_compare}, {out_compare_file}, {parameter_tolerances;parameter_tolerances...}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...})

        Compares the properties of two raster datasets, two raster catalogs, or two
        mosaic dataset and then returns the comparison result.

     INPUTS:
      in_base_raster (Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The input raster that will be compared to the test raster.Valid inputs include a
          raster dataset, a raster catalog or a mosaic dataset.
      in_test_raster (Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The test raster that will be compared to the input base raster.Valid inputs
          include a raster dataset, a raster catalog or a mosaic dataset.
      compare_type {String}:
          The type of comparison.

          * RASTER_DATASET—Compares raster dataset properties.

          * GDB_RASTER_DATASET—Compares properties of raster datasets in a geodatabase.

          * GDB_RASTER_CATALOG—Compares properties of raster catalogs in a geodatabase.

          * MOSAIC_DATASET—Compares properties of mosaic datasets.
      ignore_option {String}:
          The properties specified will not be compared during comparison.Open the tool
          dialog to view a list of values for the Ignore Options parameter.
          Your Compare Type will determine which Ignore Options are valid.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the first
          mismatch.

          * NO_CONTINUE_COMPARE—Stop after encountering the first mismatch. This is the
          default.

          * CONTINUE_COMPARE—Compare other properties after encountering the first
          mismatch.
      parameter_tolerances {Value Table}:
          The Parameter Tolerance allows you to compare your parameter values with some
          leeway on accuracy. This allows you to account for any slight changes that might
          have occurred in processing your data.For a list of Parameter types, choose the
          parameters for which you would like to
          have a tolerance. For each parameter you will need a tolerance and tolerance
          type. The tolerance type is either the value of the tolerance or a fraction of
          it. When using the fraction type, the fraction is based on the base value;
          therefore, the tolerance value for comparison would be the fraction times the
          base value. For example, if your base value is 100 and you set the fraction
          tolerance to 0.00001, the compare tolerance will be 100 * 0.00001 = 0.001

          * All—This option will apply the same tolerance to the extent, pixel value,
          minimum pixel value, maximum pixel value, mean pixel value, and standard
          deviation pixel value.

          * Extent—The extent of the raster will have an allowable tolerance.

          * Pixel_Value—The pixel values of the raster will have an allowable tolerance.

          * Statistics_Minimum—The minimum pixel value of the raster will have an
          allowable tolerance.

          * Statistics_Maximum—The maximum pixel value of the raster will have an
          allowable tolerance.

          * Statistics_Mean—The mean pixel value of the raster will have an allowable
          tolerance.

          * Statistics_Standard_Deviation—The standard deviation pixel value of the raster
          will have an allowable tolerance.
      attribute_tolerances {Value Table}:
          The Attribute Tolerance allows you to compare your attribute values with some
          leeway on accuracy. This allows you to account for any slight changes that might
          have occurred in processing your data.Type the field name and tolerance value
          for each parameter for which you want to
          have a tolerance. The tolerance value is the actual value of the tolerance, not
          a fraction.
      omit_field {String}:
          These are the fields you would like to Omit in the comparison results. Type in
          the fields to omit in the comparison.When dealing with a raster catalog
          scenario, you are comparing attribute columns
          of the raster catalogs, not any attributes within the catalog items.

     OUTPUTS:
      out_compare_file {File}:
          The name and path of the text file which will contain the comparison results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterCompare_management(*gp_fixargs((in_base_raster, in_test_raster, compare_type, ignore_option, continue_compare, out_compare_file, parameter_tolerances, attribute_tolerances, omit_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TINCompare_management', None)
def TINCompare(in_base_tin=None, in_test_tin=None, compare_type=None, continue_compare=None, out_compare_file=None):
    """TINCompare_management(in_base_tin, in_test_tin, {compare_type}, {continue_compare}, {out_compare_file})

        Compares two TINs and returns the comparison results. TIN Compare can report
        differences with geometry, TIN node and triangle tags, and spatial reference.

     INPUTS:
      in_base_tin (TIN Layer):
          The Input Base Tin is compared with the Input Test Tin. Input Base Tin refers to
          data that you have declared valid. This base data has the correct geometry, tag
          values (if any), and spatial reference.
      in_test_tin (TIN Layer):
          The Input Test Tin is compared against the Input Base Tin.
      compare_type {String}:
          The comparison type.

          * ALL—This is the default.

          * PROPERTIES_ONLY—Refers to both geometry and TIN tag values, if any, that are
          assigned to nodes and triangles.

          * SPATIAL_REFERENCE_ONLY—Coordinate system information.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the first
          mismatch.

          * NO_CONTINUE_COMPARE—Stop after encountering the first mismatch. This is the
          default.

          * CONTINUE_COMPARE—Compare other properties after encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          The name and path of the text file which will contain the comparison results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TINCompare_management(*gp_fixargs((in_base_tin, in_test_tin, compare_type, continue_compare, out_compare_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableCompare_management', None)
def TableCompare(in_base_table=None, in_test_table=None, sort_field=None, compare_type=None, ignore_options=None, attribute_tolerances=None, omit_field=None, continue_compare=None, out_compare_file=None):
    """TableCompare_management(in_base_table, in_test_table, sort_field;sort_field..., {compare_type}, {ignore_options;ignore_options...}, {attribute_tolerances;attribute_tolerances...}, {omit_field;omit_field...}, {continue_compare}, {out_compare_file})

        Compares two tables or table views and returns the comparison results. This tool
        can report differences and similarities with tabular values and field
        definitions.

     INPUTS:
      in_base_table (Table View / Raster Layer):
          The Input Base Table is compared with the Input Test Table. The Input Base Table
          refers to tabular data that you have declared valid. This base data has the
          correct field definitions and attribute values.
      in_test_table (Table View / Raster Layer):
          The Input Test Table is compared against the Input Base Table. The Input Test
          Table refers to data that you have made changes to by editing or compiling new
          fields, new records, or new attribute values.
      sort_field (Value Table):
          The field or fields used to sort records in the Input Base Table and the Input
          Test Table. The records are sorted in ascending order. Sorting by a common field
          in both the Input Base Table and the Input Test Table ensures that you are
          comparing the same row from each input dataset.
      compare_type {String}:
          The comparison type. ALL is the default. The default will compare all properties
          of the tables being compared.

          * ALL —Compare all properties. This is the default.

          * ATTRIBUTES_ONLY —Only compare the attributes and their values.

          * SCHEMA_ONLY —Only compare the schema.
      ignore_options {String}:
          These properties will not be compared during comparison.

          * IGNORE_EXTENSION_PROPERTIES—Do not compare extension properties.

          * IGNORE_SUBTYPES—Do not compare subtypes.

          * IGNORE_RELATIONSHIPCLASSES—Do not compare Relationship classes.
      attribute_tolerances {Value Table}:
          The numeric value that determines the range in which attribute values are
          considered equal. This only applies to numeric field types.
      omit_field {String}:
          The field or fields that will be omitted during comparison. The field
          definitions and the tabular values for these fields will be ignored.
      continue_compare {Boolean}:
          Indicates whether to compare all properties after encountering the first
          mismatch.

          * NO_CONTINUE_COMPARE—Stop after encountering the first mismatch. This is the
          default.

          * CONTINUE_COMPARE—Compare other properties after encountering the first
          mismatch.

     OUTPUTS:
      out_compare_file {File}:
          This file will contain all similarities and differences between the Input Base
          Table and the Input Test Table. This file is a comma-delimited text file which
          can be viewed and used as a table in ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableCompare_management(*gp_fixargs((in_base_table, in_test_table, sort_field, compare_type, ignore_options, attribute_tolerances, omit_field, continue_compare, out_compare_file), True)))
        return retval
    except Exception, e:
        raise e


# Distributed Geodatabase toolset
@gptooldoc('AddGlobalIDs_management', None)
def AddGlobalIDs(in_datasets=None):
    """AddGlobalIDs_management(in_datasets;in_datasets...)

        Adds global IDs to a list of geodatabase feature classes, tables, and/or feature
        datasets.

     INPUTS:
      in_datasets (Layer / Table View / Dataset):
          A list of geodatabase classes, tables, and/or feature datasets to which global
          IDs will be added."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddGlobalIDs_management(*gp_fixargs((in_datasets,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CompareReplicaSchema_management', None)
def CompareReplicaSchema(in_geodatabase=None, in_source_file=None, output_replica_schema_changes_file=None):
    """CompareReplicaSchema_management(in_geodatabase, in_source_file, output_replica_schema_changes_file)

        Generates an XML that describes schema differences between a replica geodatabase
        and the relative replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase to which the replica schema will be compared.
          The geodatabase may be a local geodatabase or a geodata service.
      in_source_file (File):
          Specifies the file that contains the relative replica schema to use for the
          comparison.

     OUTPUTS:
      output_replica_schema_changes_file (File):
          Specifies the file to contain a description of the schema differences."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CompareReplicaSchema_management(*gp_fixargs((in_geodatabase, in_source_file, output_replica_schema_changes_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateReplica_management', None)
def CreateReplica(in_data=None, in_type=None, out_geodatabase=None, out_name=None, access_type=None, initial_data_sender=None, expand_feature_classes_and_tables=None, reuse_schema=None, get_related_data=None, geometry_features=None, archiving=None):
    """CreateReplica_management(in_data;in_data..., in_type, out_geodatabase, out_name, {access_type}, {initial_data_sender}, {expand_feature_classes_and_tables}, {reuse_schema}, {get_related_data}, {geometry_features}, archiving)

        Creates a replica to a personal, file, or SDE geodatabase from a specified list
        of feature classes, layers, datasets, and/or tables in an ArcSDE geodatabase.

     INPUTS:
      in_data (Layer / Table View / Dataset):
          The data to be replicated. This list consists of layers and tables referencing
          versioned, editable data from an ArcSDE geodatabase.
      in_type (String):
          The kind of replica to create.

          * TWO_WAY_REPLICA— Changes can be sent between child and parent replicas in both
          directions.

          * ONE_WAY_REPLICA—Changes are sent from the parent replica to the child replica
          only.

          * CHECK_OUT—Data is replicated, edited, and checked back in one time.

          * ONE_WAY_CHILD_TO_PARENT_REPLICA—Changes are sent from the child replica to the
          parent replica only.
      out_geodatabase (Workspace / GeoDataServer):
          The local geodatabase or geodata service that will host the child replica.
          Geodata services are used to represent remote geodatabases. The geodatabase can
          be an ArcSDE, file, or personal geodatabase. For two-way replicas the child
          geodatabase must be ArcSDE. For one-way and check-out replicas the geodatabase
          can be personal, file, or ArcSDE. Personal or file geodatabases must already
          exist before running this tool.
      out_name (String):
          The name that identifies the replica.
      access_type {String}:
          The type of access you want:

          * FULL—Supports complex types (topologies and geometric networks) and requires
          the data to be versioned.

          * SIMPLE—The data on the child is not versioned and must be simple. This allows
          the replica to be interoperable. Nonsimple features in the parent (for example,
          features in geometric networks and topologies) are converted to simple features
          (for example, point, line, and polygon feature classes).
      initial_data_sender {String}:
          Used by replication to determine which replica can send changes when in
          disconnected mode. If you are working in a connected mode, this parameter is
          inconsequential. This ensures that the relative replica doesn't send updates
          until the changes are first received from the initial data sender.

          * CHILD_DATA_SENDER

          * PARENT_DATA_SENDER
      expand_feature_classes_and_tables {String}:
          Specifies whether you will include expanded feature classes and tables, such as
          those found in geometric networks, topologies, or relationship classes.

          * USE_DEFAULTS—Adds the expanded feature classes and tables related to the
          feature classes and tables in the replica. The default for feature classes is to
          replicate all features; the default for tables is to replicate the schema only.
          If a spatial filter has been defined it will be applied to feature classes.

          * ADD_WITH_SCHEMA_ONLY—Adds only the schema for the expanded feature classes and
          tables.

          * ALL_ROWS—Adds all rows for expanded feature classes and tables.

          * DO_NOT_ADD—Doesn't add expanded feature classes and tables.
      reuse_schema {String}:
          Indicates whether to reuse a geodatabase that contains the schema of the data
          you want to replicate. This reduces the amount of time required to replicate the
          data. This option is only available for check-out replicas.

          * DO_NOT_REUSE—Do not reuse schema. This is the default.

          * REUSE—Reuse schema.
      get_related_data {String}:
          Specifies whether to replicate rows related to rows already in the replica. For
          example, consider a feature (f1) inside the replication filter and a related
          feature (f2) from another class outside the filter. Feature f2 is included in
          the replica if you choose to get related data.

          * DO_NOT_GET_RELATED—Do not replicate related rows.

          * GET_RELATED—Replicate related data. This is the default.
      geometry_features {Feature Layer}:
          The features used to define the area to replicate.
      archiving (Boolean):
          Specifies whether to use the archive class to track changes instead of using the
          versioning delta tables. This is only available for one-way replicas.

          * ARCHIVING—Uses archiving to track changes.

          * DO_NOT_USE_ARCHIVING—Does not use archiving to track changes. This is the
          default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateReplica_management(*gp_fixargs((in_data, in_type, out_geodatabase, out_name, access_type, initial_data_sender, expand_feature_classes_and_tables, reuse_schema, get_related_data, geometry_features, archiving), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateReplicaFootPrints_management', None)
def CreateReplicaFootPrints(in_workspace=None, out_workspace=None, output_featureclass_name=None):
    """CreateReplicaFootPrints_management(in_workspace, out_workspace, output_featureclass_name)

        Creates a feature class that contains the geometries for all the replicas in a
        geodatabase. Attributes in the feature class store the information from the
        replica manager.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the replicas from which you would like to create the
          replica footprint. The geodatabase must be a local geodatabase; it cannot be a
          geodata service.
      out_workspace (Workspace):
          The output geodatabase that will hold the replica footprints feature class once
          it is created. The geodatabase may be local or remote.
      output_featureclass_name (String):
          The name of the replica footprints feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateReplicaFootPrints_management(*gp_fixargs((in_workspace, out_workspace, output_featureclass_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateReplicaFromServer_management', None)
def CreateReplicaFromServer(in_geodataservice=None, datasets=None, in_type=None, out_geodatabase=None, out_name=None, access_type=None, initial_data_sender=None, expand_feature_classes_and_tables=None, reuse_schema=None, get_related_data=None, geometry_features=None, archiving=None):
    """CreateReplicaFromServer_management(in_geodataservice, datasets;datasets..., in_type, out_geodatabase, out_name, {access_type}, {initial_data_sender}, {expand_feature_classes_and_tables}, {reuse_schema}, {get_related_data}, {geometry_features}, archiving)

        Creates a replica using a specified list of feature classes, layers, feature
        datasets, and/or tables from a remote geodatabase using a geodata service
        published on ArcGIS for Server.

     INPUTS:
      in_geodataservice (GeoDataServer):
          The geodata service representing the geodatabase from which the replica will be
          created. The geodatabase referenced by the geodata service must be an ArcSDE
          geodatabase.
      datasets (String):
          The list of the feature datasets, stand-alone feature classes, tables, and
          stand-alone attributed relationship classes from the geodata service to
          replicate.
      in_type (String):
          The kind of replica to create.

          * TWO_WAY_REPLICA— Changes can be sent between child and parent replicas in both
          directions.

          * ONE_WAY_REPLICA—Changes are sent from the parent replica to the child replica
          only.

          * CHECK_OUT—Data is replicated, edited, and checked back in one time.

          * ONE_WAY_CHILD_TO_PARENT_REPLICA—Changes are sent from the child replica to the
          parent replica only.
      out_geodatabase (Workspace / GeoDataServer):
          The local geodatabase or geodata service that will host the child replica.
          Geodata services are used to represent remote geodatabases. The geodatabase can
          be an ArcSDE, file, or personal geodatabase. For two-way replicas the child
          geodatabase must be ArcSDE. For one-way and check-out replicas the geodatabase
          can be personal, file, or ArcSDE. Personal or file geodatabases must already
          exist before running this tool.
      out_name (String):
          The name that identifies the replica.
      access_type {String}:
          The type of access you want:

          * FULL—Supports complex types (topologies and geometric networks) and requires
          the data to be versioned.

          * SIMPLE—The data on the child is not versioned and must be simple. This allows
          the replica to be interoperable. Nonsimple features in the parent (for example,
          features in geometric networks and topologies) are converted to simple features
          (for example, point, line, and polygon feature classes).
      initial_data_sender {String}:
          Used by replication to determine which replica can send changes when in
          disconnected mode. If you are working in a connected mode, this parameter is
          inconsequential. This ensures that the relative replica doesn't send updates
          until the changes are first received from the initial data sender.

          * CHILD_DATA_SENDER

          * PARENT_DATA_SENDER
      expand_feature_classes_and_tables {String}:
          Specifies whether you will include expanded feature classes and tables, such as
          those found in geometric networks, topologies, or relationship classes.

          * USE_DEFAULTS—Adds the expanded feature classes and tables related to the
          feature classes and tables in the replica. The default for feature classes is to
          replicate all features; the default for tables is to replicate the schema only.
          If a spatial filter has been defined it will be applied to feature classes.

          * ADD_WITH_SCHEMA_ONLY—Adds only the schema for the expanded feature classes and
          tables.

          * ALL_ROWS—Adds all rows for expanded feature classes and tables.

          * DO_NOT_ADD—Doesn't add expanded feature classes and tables.
      reuse_schema {String}:
          Indicates whether to reuse a geodatabase that contains the schema of the data
          you want to replicate. This reduces the amount of time required to replicate the
          data. This option is only available for check-out replicas.

          * DO_NOT_REUSE—Do not reuse schema. This is the default.

          * REUSE—Reuse schema.
      get_related_data {String}:
          Specifies whether to replicate rows related to rows already in the replica. For
          example, consider a feature (f1) inside the replication filter and a related
          feature (f2) from another class outside the filter. Feature f2 is included in
          the replica if you choose to get related data.

          * DO_NOT_GET_RELATED—Do not replicate related rows.

          * GET_RELATED—Replicate related data. This is the default.
      geometry_features {Feature Layer}:
          The features used to define the area to replicate.
      archiving (Boolean):
          Specifies whether to use the archive class to track changes instead of using the
          versioning delta tables. This is only available for one-way replicas.

          * ARCHIVING—Uses archiving to track changes.

          * DO_NOT_USE_ARCHIVING—Does not use archiving to track changes. This is the
          default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateReplicaFromServer_management(*gp_fixargs((in_geodataservice, datasets, in_type, out_geodatabase, out_name, access_type, initial_data_sender, expand_feature_classes_and_tables, reuse_schema, get_related_data, geometry_features, archiving), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportAcknowledgementMessage_management', None)
def ExportAcknowledgementMessage(in_geodatabase=None, out_acknowledgement_file=None, in_replica=None):
    """ExportAcknowledgementMessage_management(in_geodatabase, out_acknowledgement_file, in_replica)

        Creates an output acknowledgement file to acknowledge the reception of
        previously received data change messages.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase from which to export the acknowledgement
          message. The geodatabase may be local or remote.
      in_replica (String):
          The replica from which the acknowledgement message will be exported.

     OUTPUTS:
      out_acknowledgement_file (File):
          Specifies the delta file to export to."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportAcknowledgementMessage_management(*gp_fixargs((in_geodatabase, out_acknowledgement_file, in_replica), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportDataChangeMessage_management', None)
def ExportDataChangeMessage(in_geodatabase=None, out_data_changes_file=None, in_replica=None, switch_to_receiver=None, include_unacknowledged_changes=None, include_new_changes=None):
    """ExportDataChangeMessage_management(in_geodatabase, out_data_changes_file, in_replica, switch_to_receiver, include_unacknowledged_changes, include_new_changes)

        Creates an output delta file containing updates from an input replica.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase from which to export the data change message.
          The geodatabase may be local or remote.
      in_replica (String):
          The replica containing updates to be exported.
      switch_to_receiver (Boolean):
          Indicates whether to change the role of the replica to that of a receiver. The
          receiver may not send replica updates until updates from the relative replica
          sender arrive.

          * DO_NOT_SWITCH—Do not switch replica role. This is the default.

          * SWITCH—Switch replica role from sender to receiver.
      include_unacknowledged_changes (Boolean):
          Indicates whether to include data changes that have been previously exported for
          which no acknowledgment message has been received.

          * NO_UNACKNOWLEDGED—Do not include data changes that have been previously sent.

          * UNACKNOWLEDGED—Include all of the data changes that have been previously
          exported for which no acknowledgment message has been sent. This is the default.
      include_new_changes (Boolean):
          Indicates whether to include all data changes created since the last exported
          data change message.

          * NO_NEW_CHANGES—Do not include data changes created since the last exported
          data change message.

          * NEW_CHANGES—Include data changes created since the last exported data change
          message. This is the default.

     OUTPUTS:
      out_data_changes_file (File):
          Specifies the delta file to export to."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportDataChangeMessage_management(*gp_fixargs((in_geodatabase, out_data_changes_file, in_replica, switch_to_receiver, include_unacknowledged_changes, include_new_changes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportReplicaSchema_management', None)
def ExportReplicaSchema(in_geodatabase=None, output_replica_schema_file=None, in_replica=None):
    """ExportReplicaSchema_management(in_geodatabase, output_replica_schema_file, in_replica)

        Creates a replica schema file with the schema of an input one- or two-way
        replica.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase from which to export the replica schema. The
          geodatabase may be local or remote.
      in_replica (String):
          The replica from which to export schema.

     OUTPUTS:
      output_replica_schema_file (File):
          Specifies the file in which to export schema."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportReplicaSchema_management(*gp_fixargs((in_geodatabase, output_replica_schema_file, in_replica), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportXMLWorkspaceDocument_management', None)
def ExportXMLWorkspaceDocument(in_data=None, out_file=None, export_type=None, storage_type=None, export_metadata=None):
    """ExportXMLWorkspaceDocument_management(in_data, out_file, {export_type}, {storage_type}, {export_metadata})

        Creates a readable XML document of the geodatabase contents. The XML Workspace
        Document is useful for sharing geodatabase schemas or copying
        geodatabase schemas from one type to another.

     INPUTS:
      in_data (Table / Feature Class / Feature Dataset / Raster Dataset / Workspace):
          The input datasets to be exported and represented in an XML workspace document.
          The input data can be a geodatabase, feature dataset, feature class, table,
          raster, or raster catalog.
      export_type {String}:
          Determines if the output XML workspace document will contain all of the data
          from the input (table and feature class records, including geometry) or only the
          schema.

          * DATA—Export both the schema and the data. This is the default.

          * SCHEMA_ONLY—Export the schema only.
      storage_type {String}:
          Determines how feature geometry is stored when data is exported from a feature
          class.

          * BINARY—Store geometry in a compressed base64 binary format. This binary format
          will produce a smaller XML workspace document. Use this option when the XML
          workspace document will be read by a custom program that uses ArcObjects. This
          is the default.

          * NORMALIZED—The geometry will be stored in an uncompressed format, resulting in
          a larger file. Use this option when the XML workspace document will be read by a
          custom program that does not use ArcObjects.
      export_metadata {Boolean}:
          Determines if metadata will be exported.

          * METADATA—If the input contains metadata, it will be exported. This is the
          default.

          * NO_METADATA—Do not export metadata.

     OUTPUTS:
      out_file (File):
          The XML workspace document file to be created. This can be an XML file (.xml)
          or a compressed ZIP file (.zip or .z)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportXMLWorkspaceDocument_management(*gp_fixargs((in_data, out_file, export_type, storage_type, export_metadata), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportMessage_management', None)
def ImportMessage(in_geodatabase=None, source_delta_file=None, output_acknowledgement_file=None, conflict_policy=None, conflict_definition=None, reconcile_with_parent_version=None):
    """ImportMessage_management(in_geodatabase, source_delta_file, {output_acknowledgement_file}, {conflict_policy}, {conflict_definition}, {reconcile_with_parent_version})

        Imports changes from a delta file into a replica geodatabase, or imports an
        acknowledgment message into a replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase to receive the imported message. The
          geodatabase may be local or remote.
      source_delta_file (Workspace / File):
          Specifies the file from which the message will be imported.
      conflict_policy {String}:
          Specifies how conflicts are resolved when they are encountered while importing a
          data change message.

          * MANUAL—Manually resolve conflicts in the versioning reconcile environment.

          * IN_FAVOR_OF_DATABASE—Conflicts automatically resolve in favor of the database
          receiving the changes.

          * IN_FAVOR_OF_IMPORTED_CHANGES—Conflicts automatically resolve in favor of the
          imported changes.
      conflict_definition {String}:
          Specifies how you would like to define conflicts:

          * BY_OBJECT—Detects conflicts by row.

          * BY_ATTRIBUTE—Detects conflicts by column.
      reconcile_with_parent_version {Boolean}:
          Indicates whether to automatically reconcile once data changes are sent to the
          parent replica if there are no conflicts present. This option is only available
          for check-out/check-in replicas.

          * DO_NOT_RECONCILE—Do not reconcile. This is the default.

          * RECONCILE—Reconcile.

     OUTPUTS:
      output_acknowledgement_file {File}:
          When importing data changes, this allows you to optionally export a message to
          acknowledge the import of a data change message. This option is ignored for
          anything other than a data change message."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportMessage_management(*gp_fixargs((in_geodatabase, source_delta_file, output_acknowledgement_file, conflict_policy, conflict_definition, reconcile_with_parent_version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportReplicaSchema_management', None)
def ImportReplicaSchema(in_geodatabase=None, in_source=None):
    """ImportReplicaSchema_management(in_geodatabase, in_source)

        Applies replica schema differences using an input replica geodatabase and XML
        schema file.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase to which the replica schema will be imported.
          The geodatabase may be a local geodatabase or a geodata service.
      in_source (File):
          Specifies the file which contains the replica schema to import."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportReplicaSchema_management(*gp_fixargs((in_geodatabase, in_source), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportXMLWorkspaceDocument_management', None)
def ImportXMLWorkspaceDocument(target_geodatabase=None, in_file=None, import_type=None, config_keyword=None):
    """ImportXMLWorkspaceDocument_management(target_geodatabase, in_file, {import_type}, {config_keyword})

        Imports the contents of an XML workspace document into an existing geodatabase.

     INPUTS:
      target_geodatabase (Workspace):
          The existing geodatabase where the contents of the XML workspace document will
          be imported.
      in_file (File):
          The input XML workspace document file containing geodatabase contents to be
          imported. This can be an XML file (.xml) or a compressed ZIP file (.zip or .z)
          containing the XML file.
      import_type {String}:
          Determines if both data (feature class and table records, including geometry)
          and schema are imported, or only schema is imported.

          * DATA—Import the data and schema. This is the default.

          * SCHEMA_ONLY—Import the schema only.
      config_keyword {String}:
          Geodatabase configuration keyword to be applied if the Target Geodatabase is an
          enterprise or file geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportXMLWorkspaceDocument_management(*gp_fixargs((target_geodatabase, in_file, import_type, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReExportUnacknowledgedMessages_management', None)
def ReExportUnacknowledgedMessages(in_geodatabase=None, output_delta_file=None, in_replica=None, in_export_option=None):
    """ReExportUnacknowledgedMessages_management(in_geodatabase, output_delta_file, in_replica, in_export_option)

        Creates an output delta file containing unacknowledged replica updates from a
        one-way or two-way replica geodatabase.

     INPUTS:
      in_geodatabase (Workspace / GeoDataServer):
          Specifies the replica geodatabase from which to reexport the unacknowledged
          messages. The geodatabase may be a local geodatabase or a geodata service.
      in_replica (String):
          The replica from which the unacknowledgment messages will be reexported.
      in_export_option (String):
          * ALL_UNACKNOWLEDGED—Reexports all changes for which there has been no
          acknowledgment message received.

          * MOST_RECENT—Reexports only those changes since the last set of exported
          changes was sent.

     OUTPUTS:
      output_delta_file (File):
          Specifies the delta file in which to reexport data changes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReExportUnacknowledgedMessages_management(*gp_fixargs((in_geodatabase, output_delta_file, in_replica, in_export_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SynchronizeChanges_management', None)
def SynchronizeChanges(geodatabase_1=None, in_replica=None, geodatabase_2=None, in_direction=None, conflict_policy=None, conflict_definition=None, reconcile=None):
    """SynchronizeChanges_management(geodatabase_1, in_replica, geodatabase_2, in_direction, conflict_policy, conflict_definition, reconcile)

        Synchronizes updates between two replica geodatabases in a direction specified
        by the user.

     INPUTS:
      geodatabase_1 (Workspace / GeoDataServer):
          The geodatabase hosting the replica to synchronize. The geodatabase may be local
          or remote.
      in_replica (String):
          A valid replica with a parent contained within one input geodatabase and a child
          in the other input geodatabase.
      geodatabase_2 (Workspace / GeoDataServer):
          The geodatabase hosting the relative replica. The geodatabase may be local or
          remote.
      in_direction (String):
          The direction in which you want changes to be sent: from geodatabase 1 to
          geodatabase 2, from geodatabase 2 to geodatabase 1, or to send changes in both
          directions. For check-out/check-in replicas or one-way replicas there is only
          one appropriate direction. If the replica is two-way then any of the three
          choices are available.

          * BOTH_DIRECTIONS—Changes will be synchronized in both directions.

          * FROM_GEODATABASE2_TO_1—Changes will be synchronized from Geodatabase 2 to
          Geodatabase 1.

          * FROM_GEODATABASE1_TO_2—Changes will be synchronized from Geodatabase 1 to
          Geodatabase 2.
      conflict_policy (String):
          Specifies how conflicts are resolved when they are encountered.

          * MANUAL—Manually resolve conflicts in the versioning reconcile environment.

          * IN_FAVOR_OF_GDB1—Conflicts resolve in favor of the Geodatabase 1.

          * IN_FAVOR_OF_GDB2—Conflicts resolve in favor of the Geodatabase 2.
      conflict_definition (String):
          Specifies how you would like to define conflicts:

          * BY_OBJECT—Detects conflicts by row

          * BY_ATTRIBUTE—Detects conflicts by column
      reconcile (Boolean):
          Indicates whether to automatically reconcile once data changes are sent to the
          parent replica if there are no conflicts present. This option is only available
          for check-out/check-in replicas.

          * DO_NOT_RECONCILE—Do not reconcile. This is the default.

          * RECONCILE—Reconcile."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SynchronizeChanges_management(*gp_fixargs((geodatabase_1, in_replica, geodatabase_2, in_direction, conflict_policy, conflict_definition, reconcile), True)))
        return retval
    except Exception, e:
        raise e


# Domains toolset
@gptooldoc('AddCodedValueToDomain_management', None)
def AddCodedValueToDomain(in_workspace=None, domain_name=None, code=None, code_description=None):
    """AddCodedValueToDomain_management(in_workspace, domain_name, code, code_description)

        Adds a value to a domain's coded value list.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be updated.
      domain_name (String):
          The name of the attribute domain that will have a value added to its coded value
          list.
      code (String):
          The value to be added to the specified domain's coded value list.
      code_description (String):
          A description of what the coded value represents."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddCodedValueToDomain_management(*gp_fixargs((in_workspace, domain_name, code, code_description), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AssignDomainToField_management', None)
def AssignDomainToField(in_table=None, field_name=None, domain_name=None, subtype_code=None):
    """AssignDomainToField_management(in_table, field_name, domain_name, {subtype_code;subtype_code...})

        Sets the domain for a particular field and, optionally, for a subtype. If no
        subtype is specified, the domain is only assigned to the specified field.

     INPUTS:
      in_table (Table View):
          The name of the table or feature class containing the field that will be
          assigned a domain.
      field_name (Field):
          The name of the field to be assigned a domain.
      domain_name (String):
          The name of a geodatabase domain to assign to the field name. Available domains
          will automatically be loaded.
      subtype_code {String}:
          The subtype code to be assigned a domain."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AssignDomainToField_management(*gp_fixargs((in_table, field_name, domain_name, subtype_code), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateDomain_management', None)
def CreateDomain(in_workspace=None, domain_name=None, domain_description=None, field_type=None, domain_type=None, split_policy=None, merge_policy=None):
    """CreateDomain_management(in_workspace, domain_name, {domain_description}, field_type, {domain_type}, {split_policy}, {merge_policy})

        Creates an attribute domain in the specified workspace.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase that will contain the new domain.
      domain_name (String):
          The name of the domain that will be created.
      domain_description {String}:
          The description of the domain that will be created.
      field_type (String):
          The type of attribute domain to create. Attribute domains are rules that
          describe the legal values of a field type. Specify a field type that matches the
          data type of the field to which the attribute domain will be assigned.

          * SHORT—Numeric values without fractional values within a specific range; coded
          values. This is the default value.

          * LONG—Numeric values without fractional values within a specific range.

          * FLOAT—Numeric values with fractional values within a specific range.

          * DOUBLE—Numeric values with fractional values within a specific range.

          * TEXT—Names or other textual qualities.

          * DATE—Date and/or time.
      domain_type {String}:
          The domain type to create:

          * CODED—Specifies a valid set of values for an attribute. For example, a coded
          value domain might specify valid pipe material values: CL—cast iron pipe,
          DL—ductile iron pipe, or ACP—asbestos concrete pipe. This is the default value.

          * RANGE—Specifies a valid range of values for a numeric attribute. For example,
          if distribution water mains have a pressure between 50 and 75 psi, then a range
          domain would specify these minimum and maximum values.
      split_policy {String}:
          The split policy of the created domain. The behavior of an attribute's values
          when a feature that is split is controlled by its split policy.

          * DEFAULT—The attributes of the two resulting features take on the default value
          of the attribute of the given feature class or subtype.

          * DUPLICATE—The attribute of the two resulting features takes on a copy of the
          original object's attribute value.

          * GEOMETRY_RATIO—The attributes of resulting features are a ratio of the
          original feature's value. The ratio is based on the proportion into which the
          original geometry is divided. If the geometry is divided equally, each new
          feature's attribute gets one-half the value of the original object's attribute.
          The geometry ratio policy only applies to range domains.
      merge_policy {String}:
          The merge policy of the created domain. When two features are merged into a
          single feature, merge policies control attribute values in the new feature.

          * DEFAULT—The attribute of the resulting feature takes on the default value of
          the attribute of the given feature class or subtype. This is the only merge
          policy that applies to nonnumeric fields and coded value domains.

          * SUM_VALUES—The attribute of the resulting feature takes on the sum of the
          values from the original feature's attribute. The sum values policy only applies
          to range domains.

          * AREA_WEIGHTED—The attribute of the resulting feature is the weighted average
          of the attribute values of the original features. This average is based on the
          original feature's geometry. The area weighted policy only applies to range
          domains."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateDomain_management(*gp_fixargs((in_workspace, domain_name, domain_description, field_type, domain_type, split_policy, merge_policy), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteCodedValueFromDomain_management', None)
def DeleteCodedValueFromDomain(in_workspace=None, domain_name=None, code=None):
    """DeleteCodedValueFromDomain_management(in_workspace, domain_name, code;code...)

        Removes a value from a coded value domain.

     INPUTS:
      in_workspace (Workspace):
          The workspace containing the domain to be updated.
      domain_name (String):
          The name of the coded value domain to be updated.
      code (String):
          The value(s) to be deleted from the specified domain."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteCodedValueFromDomain_management(*gp_fixargs((in_workspace, domain_name, code), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteDomain_management', None)
def DeleteDomain(in_workspace=None, domain_name=None):
    """DeleteDomain_management(in_workspace, domain_name)

        Deletes a domain from a workspace.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase that contains the domain to be deleted.
      domain_name (String):
          The name of the domain to be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteDomain_management(*gp_fixargs((in_workspace, domain_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DomainToTable_management', None)
def DomainToTable(in_workspace=None, domain_name=None, out_table=None, code_field=None, description_field=None, configuration_keyword=None):
    """DomainToTable_management(in_workspace, domain_name, out_table, code_field, description_field, {configuration_keyword})

        Creates a table from an attribute domain.

     INPUTS:
      in_workspace (Workspace):
          The workspace containing the attribute domain to be converted to a table.
      domain_name (String):
          The name of the existing attribute domain.
      code_field (String):
          The name of the field in the created table that will store code values.
      description_field (String):
          The name of the field in the created table that will store code value
          descriptions.
      configuration_keyword {String}:
          For geodatabase tables, the custom storage keywords for creating the table.

     OUTPUTS:
      out_table (Table):
          The table to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DomainToTable_management(*gp_fixargs((in_workspace, domain_name, out_table, code_field, description_field, configuration_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveDomainFromField_management', None)
def RemoveDomainFromField(in_table=None, field_name=None, subtype_code=None):
    """RemoveDomainFromField_management(in_table, field_name, {subtype_code;subtype_code...})

        Removes an attribute domain association from a feature class or table field.

     INPUTS:
      in_table (Table View):
          The input table containing the attribute domain that will be removed.
      field_name (Field):
          The field that will no longer be associated with an attribute domain.
      subtype_code {String}:
          The subtype code(s) that will no longer be associated with an attribute domain."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveDomainFromField_management(*gp_fixargs((in_table, field_name, subtype_code), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetValueForRangeDomain_management', None)
def SetValueForRangeDomain(in_workspace=None, domain_name=None, min_value=None, max_value=None):
    """SetValueForRangeDomain_management(in_workspace, domain_name, min_value, max_value)

        Sets the minimum and maximum values for an existing Range domain.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be updated.
      domain_name (String):
          The name of the range domain to be updated.
      min_value (String):
          The minimum value of the range domain.
      max_value (String):
          The maximum value of the range domain."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetValueForRangeDomain_management(*gp_fixargs((in_workspace, domain_name, min_value, max_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SortCodedValueDomain_management', None)
def SortCodedValueDomain(in_workspace=None, domain_name=None, sort_by=None, sort_order=None):
    """SortCodedValueDomain_management(in_workspace, domain_name, sort_by, sort_order)

        Sorts the code or description of a coded value domain in either ascending or
        descending order.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase containing the domain to be sorted. Must be a version 10.0
          geodatabase or later.
      domain_name (String):
          The name of the coded value domain to be sorted.
      sort_by (String):
          Specifies whether the code or description will be used to sort the domain.

          * CODE—Records are sorted based on the code value for the domain.

          * DESCRIPTION—Records are sorted based on the description value for the domain.
      sort_order (String):
          Specifies the direction the records will be sorted.

          * ASCENDING—Records are sorted from low value to high value.

          * DESCENDING—Records are sorted from high value to low value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SortCodedValueDomain_management(*gp_fixargs((in_workspace, domain_name, sort_by, sort_order), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToDomain_management', None)
def TableToDomain(in_table=None, code_field=None, description_field=None, in_workspace=None, domain_name=None, domain_description=None, update_option=None):
    """TableToDomain_management(in_table, code_field, description_field, in_workspace, domain_name, {domain_description}, {update_option})

        Creates or updates a coded value domain with values from a table.

     INPUTS:
      in_table (Table View):
          The database table from which to derive domain values.
      code_field (Field):
          The field in the database table from which to derive domain code values.
      description_field (Field):
          The field in the database table from which to derive domain description values.
      in_workspace (Workspace):
          The workspace that contains the domain to be created or updated.
      domain_name (String):
          The name of the domain to be created or updated.
      domain_description {String}:
          The description of the domain to be created or updated. Domain descriptions of
          existing domains are not updated.
      update_option {String}:
          If the domain already exists, specifies how the domain will be updated.

          * APPEND—Appends to the domain values from the database table.

          * REPLACE—Replaces the values in the domain with values from the database table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToDomain_management(*gp_fixargs((in_table, code_field, description_field, in_workspace, domain_name, domain_description, update_option), True)))
        return retval
    except Exception, e:
        raise e


# Feature Class toolset
@gptooldoc('AppendAnnotation_management', None)
def AppendAnnotation(input_features=None, output_featureclass=None, reference_scale=None, create_single_class=None, require_symbol_from_table=None, create_annotation_when_feature_added=None, update_annotation_when_feature_modified=None):
    """AppendAnnotation_management(input_features;input_features..., output_featureclass, reference_scale, {create_single_class}, {require_symbol_from_table}, {create_annotation_when_feature_added}, {update_annotation_when_feature_modified})

        Creates a new geodatabase annotation feature class or appends to an existing
        annotation feature class by combining annotation from multiple input geodatabase
        annotation feature classes into a single feature class with annotation classes.

     INPUTS:
      input_features (Feature Layer):
          Input annotation features that will form an annotation class in the output
          feature class.
      reference_scale (Double):
          Reference scale set in the output feature class. Input features created at a
          different reference scale will be transformed to match this output reference
          scale.
      create_single_class {Boolean}:
          Specifies how annotation features will be added to the output feature class.

          * ONE_CLASS_ONLY—All annotation features will be aggregated into one annotation
          class within the output feature class.

          * CREATE_CLASSES—Separate annotation classes will be created for each input
          annotation class within the output feature class.
      require_symbol_from_table {Boolean}:
          Specifies how symbols can be selected for newly created annotation features.

          * REQUIRE_SYMBOL—Restricts the creation of annotation features to the list of
          symbols in the symbol collection of the output feature class

          * NO_SYMBOL_REQUIRED—Allows annotation features to be created with any symbology
      create_annotation_when_feature_added {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specifies if feature-linked annotation is created when
          a feature is added.

          * AUTO_CREATE—Use the label engine to place feature-linked annotation when a
          linked feature is created.

          * NO_AUTO_CREATE—Do not place feature-linked annotation when a feature is
          created.
      update_annotation_when_feature_modified {Boolean}:
          This parameter is only available with ArcGIS for Desktop Standard and ArcGIS for
          Desktop Advanced licenses.Specifies if feature-linked annotation is updated when
          a linked feature changes.

          * AUTO_UPDATE—Use the label engine to update feature-linked annotation when a
          linked feature changes.

          * NO_AUTO_UPDATE—Do not update feature-linked annotation when a linked feature
          changes.

     OUTPUTS:
      output_featureclass (Feature Class):
          New annotation feature class that contains an annotation class for each input
          annotation feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AppendAnnotation_management(*gp_fixargs((input_features, output_featureclass, reference_scale, create_single_class, require_symbol_from_table, create_annotation_when_feature_added, update_annotation_when_feature_modified), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateDefaultClusterTolerance_management', None)
def CalculateDefaultClusterTolerance(in_features=None):
    """CalculateDefaultClusterTolerance_management(in_features)

        Calculates a default XY tolerance by examining the spatial reference and the
        extent of the feature class. With geodatabase feature classes, the value
        returned by this tool will be
        identical to the XY Tolerance property on a geodatabase feature class or
        dataset, or the cluster tolerance of a topology. With non-geodatabase feature
        classes such as coverage feature classes, shape files, or CAD feature classes,
        the value will be based on the default tolerance of the feature class' spatial
        reference.The terms XY Tolerance and Cluster Tolerance are synonymous. You will
        see the
        usage of Cluster Tolerance in topology, python script, and ArcGIS prior to the
        9.2 Release. The name of this tool (used in scripting) is
        CalculateDefaultClusterTolerance.XY tolerance is also available in scripting
        through the XYTolerance property of
        a SpatialReference object. A SpatialReference object can be created by
        describing a feature class.

     INPUTS:
      in_features (Feature Layer):
          The feature class for which the default XY tolerance will be calculated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateDefaultClusterTolerance_management(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateDefaultGridIndex_management', None)
def CalculateDefaultGridIndex(in_features=None):
    """CalculateDefaultGridIndex_management(in_features)

        Calculates a set of valid grid index values (spatial grid 1, 2, and 3) for the
        input features. Grid index values will be calculated even if the input features
        do not support spatial grid indexing.

     INPUTS:
      in_features (Feature Layer / Raster Catalog Layer):
          The features for which a valid spatial grid index will be calculated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateDefaultGridIndex_management(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateFeatureclass_management', None)
def CreateFeatureclass(out_path=None, out_name=None, geometry_type=None, template=None, has_m=None, has_z=None, spatial_reference=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None):
    """CreateFeatureclass_management(out_path, out_name, {geometry_type}, {template;template...}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Creates an empty feature class in an ArcSDE, file geodatabase, or personal
        geodatabase; in a folder it creates a shapefile.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The ArcSDE, file, or personal geodatabase, or the folder in which the output
          feature class will be created. This workspace must already exist.
      out_name (String):
          The name of the feature class to be created.
      geometry_type {String}:
          The geometry type of the feature class.

          * POINT —

          * MULTIPOINT —

          * POLYGON —

          * POLYLINE —
      template {Feature Layer}:
          The feature class used as a template to define the attribute schema of the
          feature class.
      has_m {String}:
          Determines if the feature class contains linear measurement values (m-values).

          * DISABLED—The output feature class will not have m-values.

          * ENABLED—The output feature class will have m-values.

          * SAME_AS_TEMPLATE—The output feature class will have m-values only if the
          Template has m-values.
      has_z {String}:
          Determines if the feature class contains elevation values (z-values).

          * DISABLED—The output feature class will not have z-values.

          * ENABLED—The output feature class will have z-values.

          * SAME_AS_TEMPLATE—The output feature class will have z-values only if the
          Template has z-values.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter.
          The spatial reference of the Template Feature Class has no effect on the output
          spatial reference. If you want your output to be in the coordinate system of the
          Template Feature Class, set the Coordinate System parameter to the spatial
          reference of the Template Feature Class.
      config_keyword {String}:
          The configuration keyword applies to ArcSDE data only. It determines the storage
          parameters of the database table.
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
          2."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateFeatureclass_management(*gp_fixargs((out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateFishnet_management', None)
def CreateFishnet(out_feature_class=None, origin_coord=None, y_axis_coord=None, cell_width=None, cell_height=None, number_rows=None, number_columns=None, corner_coord=None, labels=None, template=None, geometry_type=None):
    """CreateFishnet_management(out_feature_class, origin_coord, y_axis_coord, cell_width, cell_height, number_rows, number_columns, {corner_coord}, {labels}, {template}, {geometry_type})

        Creates a fishnet of rectangular cells. The output can be polyline or polygon
        features.

     INPUTS:
      origin_coord (Point):
          The starting pivot point of the fishnet.
      y_axis_coord (Point):
          The Y-axis coordinate is used to orient the fishnet. The fishnet is rotated by
          the same angle as defined by the line connecting the origin and the y-axis
          coordinate.
      cell_width (Double):
          Determines the width of each cell. If you want the width to be automatically
          calculated using the value in the Number of Rows parameter, leave this parameter
          empty or set the value to zero—the width will be calculated when the tool is
          run.
      cell_height (Double):
          Determines the height of each cell. If you want the height to be automatically
          calculated using the value in the Number of Columns parameter, leave this
          parameter empty or set the value to zero—the height will be calculated when the
          tool is run.
      number_rows (Long):
          Determines the number of rows the fishnet will have. If you want the number of
          rows to be automatically calculated using the value in the Cell Size Width
          parameter, leave this parameter empty or set the value to zero—the number of
          rows will be calculated when the tool is run.
      number_columns (Long):
          Determines the number of columns the fishnet will have.  If you want the number
          of columns to be automatically calculated using the value in the Cell Size
          Height parameter, leave this parameter empty or set the value to zero—the number
          of columns will be calculated when the tool is run.
      corner_coord {Point}:
          The opposite corner of the fishnet set by X-Coordinate and Y-Coordinate values.
      labels {Boolean}:
          Specifies whether or not a point feature class will be created containing label
          points at the center of each fishnet cell.

          * LABELS—A new feature class is created with label points. This is the default.

          * NO_LABELS—The label points feature class is not created.
      template {Extent}:
          Specify the extent of the fishnet. The extent can be entered by specifying the
          coordinates or using a template dataset.

          * Left—XMin value

          * Right—XMax value

          * Bottom—YMin value

          * Top—YMax value
      geometry_type {String}:
          Determines if the output fishnet cells will be polyline or polygon features.

          * POLYLINE—Output is a polyline feature class. Each cell is defined by four line
          features.

          * POLYGON—Output is a polygon feature class. Each cell is defined by one polygon
          feature.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the fishnet of rectangular cells."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateFishnet_management(*gp_fixargs((out_feature_class, origin_coord, y_axis_coord, cell_width, cell_height, number_rows, number_columns, corner_coord, labels, template, geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRandomPoints_management', None)
def CreateRandomPoints(out_path=None, out_name=None, constraining_feature_class=None, constraining_extent=None, number_of_points_or_field=None, minimum_allowed_distance=None, create_multipoint_output=None, multipoint_size=None):
    """CreateRandomPoints_management(out_path, out_name, {constraining_feature_class}, {constraining_extent}, {number_of_points_or_field}, {minimum_allowed_distance}, {create_multipoint_output}, {multipoint_size})

        Creates a specified number of random point features. Random points can be
        generated in an extent window, inside polygon features, on point features, or
        along line features.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The location or workspace in which the random points feature class will be
          created. This location or workspace must already exist.
      out_name (String):
          The name of the random points feature class to be created.
      constraining_feature_class {Feature Layer}:
          Random points will be generated inside or along the features in this feature
          class. The constraining feature class can be point, multipoint, line, or
          polygon. Points will be randomly placed inside polygon features, along line
          features, or at point feature locations. Each feature in this feature class will
          have the specified number of points generated inside it (for example, if you
          specify 100 points, and the constraining feature class has 5 features, 100
          random points will be generated in each feature, totaling 500 points).
      constraining_extent {Extent / Feature Layer / Raster Layer}:
          Random points will be generated inside the extent. The constraining extent will
          only be used if no constraining feature class is specified.
      number_of_points_or_field {Long / Field}:
          The number of points to be randomly generated.The number of points can be
          specified as a long integer number or as a field
          from the constraining features containing numeric values for how many random
          points to place within each feature. The field option is only valid for polygon
          or line constraining features. If the number of points is supplied as a long
          integer number, each feature in the constraining feature class will have that
          number of random points generated inside or along it.
      minimum_allowed_distance {Linear unit / Field}:
          The shortest distance allowed between any two randomly placed points. If a value
          of 1 Meter is specified, all random points will be farther than 1 meter away
          from the closest point.
      create_multipoint_output {Boolean}:
          Determines if the output feature class will be a multipart or single-part
          feature.

          * POINT—The output will be geometry type point (each point is a separate
          feature). This is the default.

          * MULTIPOINT—The output will be geometry type multipoint (all points are a
          single feature).
      multipoint_size {Long}:
          If create_multipoint_output is set to MULTIPOINT, specify the number of random
          points to be placed in each multipoint geometry. The default is 10."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRandomPoints_management(*gp_fixargs((out_path, out_name, constraining_feature_class, constraining_extent, number_of_points_or_field, minimum_allowed_distance, create_multipoint_output, multipoint_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateUnRegisteredFeatureclass_management', None)
def CreateUnRegisteredFeatureclass(out_path=None, out_name=None, geometry_type=None, template=None, has_m=None, has_z=None, spatial_reference=None, config_keyword=None):
    """CreateUnRegisteredFeatureclass_management(out_path, out_name, {geometry_type}, {template;template...}, {has_m}, {has_z}, {spatial_reference}, {config_keyword})

        This tool creates an empty feature class in a database or enterprise
        geodatabase. The feature class is not registered with the geodatabase.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The enterprise geodatabase or database in which the output feature class will be
          created.
      out_name (String):
          The name of the feature class to be created.
      geometry_type {String}:
          The geometry type of the feature class. Only relevant for those geometry types
          that store dimensionality metadata, such as ST_Geometry in PostgreSQL, PostGIS
          Geometry, and Oracle SDO_Geometry.

          * Point

          * Multipoint

          * Polyline

          * Polygon
      template {Feature Layer}:
          An existing feature class or layer to use as a template to define the attribute
          schema of the output feature class.
      has_m {String}:
          Determines if the feature class contains linear measurement values (m values).

          * DISABLED—The output feature class will not have m values. This is the default.

          * SAME_AS_TEMPLATE—The output feature class will have m values if the template
          has m values.

          * ENABLED—The output feature class will have m values.
      has_z {String}:
          Determines if the feature class contains elevation values (z values).

          * DISABLED—The output feature class will not have z values. This is the default.

          * SAME_AS_TEMPLATE—The output feature class will have z values if the template
          has z values.

          * ENABLED—The output feature class will have z values.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter.
      config_keyword {String}:
          Determines the storage parameters of the feature class in an enterprise
          geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateUnRegisteredFeatureclass_management(*gp_fixargs((out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Integrate_management', None)
def Integrate(in_features=None, cluster_tolerance=None):
    """Integrate_management(in_features;in_features..., {cluster_tolerance})

        Integrate is used to maintain the integrity of shared feature boundaries by
        making features coincident if they fall within the specified x,y tolerance.
        Features that fall within the specified x,y tolerance are considered identical
        or coincident.For example, suppose you specify an x,y tolerance of five units
        (such as feet or
        meters) and your data has a parcel boundary that should be shared with the
        adjacent parcel boundary but is four units away. After running this tool, the
        boundaries of the two parcels would be made coincident because they were within
        the x,y tolerance of five units.Integrate performs the following processing
        tasks:

        * Finds features that are within the given x,y tolerance.


        *  Inserts common coordinate vertices for features that fall within the given
        x,y tolerance and will add vertices where feature segments intersect.

     INPUTS:
      in_features (Value Table):
          The feature classes to be integrated. When the distance between features is
          small in comparison to the tolerance the vertices or points will be clustered
          (moved to be coincident). The feature class or layer with the lower rank will
          snap to the feature from the feature class or layer with the higher rank (with 1
          being a higher rank than 2). Note that features in the feature class with a rank
          of 1 may move when a large x,y tolerance is used.
      cluster_tolerance {Linear unit}:
          The distance that determines the range in which feature vertices are made
          coincident. To minimize undesired movement of vertices, the x,y tolerance should
          be fairly small. If no value is specified, the xy tolerance from the first
          dataset in the list of inputs will be used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Integrate_management(*gp_fixargs((in_features, cluster_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateAnnotation_management', None)
def UpdateAnnotation(in_features=None, update_values=None):
    """UpdateAnnotation_management(in_features, {update_values})

        Updates the input annotation feature class with text attribute fields and
        optionally populates the value of each new field for every feature in the
        feature class.

     INPUTS:
      in_features (Feature Layer):
          Input annotation feature class to which new fields will be added.
      update_values {Boolean}:
          Populates the value of each new field for every feature in the feature class.

          * POPULATE—Populates the value of each new field for every feature in the
          feature class.

          * DO_NOT_POPULATE—Do not populate a value for the fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateAnnotation_management(*gp_fixargs((in_features, update_values), True)))
        return retval
    except Exception, e:
        raise e


# Features toolset
@gptooldoc('AddGeometryAttributes_management', None)
def AddGeometryAttributes(Input_Features=None, Geometry_Properties=None, Length_Unit=None, Area_Unit=None, Coordinate_System=None):
    """AddGeometryAttributes_management(Input_Features, Geometry_Properties;Geometry_Properties..., {Length_Unit}, {Area_Unit}, {Coordinate_System})

        Adds new attribute fields to the input features representing the spatial or
        geometric characteristics and location of each feature, such as length or area
        and x-, y-, z-, and m-coordinates.

     INPUTS:
      Input_Features (Feature Layer):
          New attribute fields will be added to the input features to store properties
          such as length, area, or x-, y-, z-, and m-coordinates.
      Geometry_Properties (String):
          Determines the geometry or shape properties that will be calculated into new
          attribute fields.

          * AREA—Adds an attribute to store the area of each polygon feature.

          * AREA_GEODESIC—Adds an attribute to store the geodesic area of each polygon
          feature.

          * CENTROID—Adds attributes to store the centroid coordinates of each feature.

          * CENTROID_INSIDE—Adds attributes to store the coordinates of a central point
          inside or on each feature.

          * EXTENT—Adds attributes to store the extent coordinates of each feature.

          * LENGTH—Adds an attribute to store the length of each line feature.

          * LENGTH_GEODESIC—Adds an attribute to store the geodesic length of each line
          feature.

          * LENGTH_3D—Adds an attribute to store the 3D length of each line feature.

          * LINE_BEARING—Adds an attribute to store the start-to-end bearing of each line
          feature. Values range from 0 to 360, with 0 meaning north, 90 east, 180 south,
          270 west, and so on.

          * LINE_START_MID_END—Adds attributes to store the coordinates of the start, mid,
          and end points of each feature.

          * PART_COUNT—Adds an attribute to store the number of parts comprising each
          feature.

          * PERIMETER_LENGTH—Adds an attribute to store the length of the perimeter or
          border of each polygon feature.

          * PERIMETER_LENGTH_GEODESIC—Adds an attribute to store the geodesic length of
          the perimeter or border of each polygon feature.

          * POINT_COUNT—Adds an attribute to store the number of points or vertices
          comprising each feature.

          * POINT_X_Y_Z_M—Adds attributes to store the x-, y-, z-, and m-coordinates of
          each point feature.
      Length_Unit {String}:
          The unit in which to calculate length.

          * FEET_US—Length in feet (United States)

          * METERS—Length in meters

          * KILOMETERS—Length in kilometers

          * MILES_US—Length in miles (United States)

          * NAUTICAL_MILES—Length in nautical miles (United States)

          * YARDS—Length in yards (United States)
      Area_Unit {String}:
          The unit in which to calculate area.

          * ACRES—Area in acres

          * HECTARES—Area in hectares

          * SQUARE_MILES_US—Area in square miles (United States)

          * SQUARE_KILOMETERS—Area in square kilometers

          * SQUARE_METERS—Area in square meters

          * SQUARE_FEET_US—Area in square feet (United States)

          * SQUARE_YARDS—Area in square yards (United States)

          * SQUARE_NAUTICAL_MILES—Area in square nautical miles (United States)
      Coordinate_System {Coordinate System}:
          The coordinate system in which the coordinates, length, and area will be
          calculated. The coordinate system of the input features is used by default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddGeometryAttributes_management(*gp_fixargs((Input_Features, Geometry_Properties, Length_Unit, Area_Unit, Coordinate_System), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddXY_management', None)
def AddXY(in_features=None):
    """AddXY_management(in_features)

        Adds the fields POINT_X and POINT_Y to the point input features and calculates
        their values. It also appends the POINT_Z and POINT_M fields if the input
        features are Z- and M-enabled.

     INPUTS:
      in_features (Feature Layer):
          The point features whose x,y coordinates will be appended as POINT_X and POINT_Y
          fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddXY_management(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Adjust3DZ_management', None)
def Adjust3DZ(in_features=None, reverse_sign=None, adjust_value=None, from_units=None, to_units=None):
    """Adjust3DZ_management(in_features, {reverse_sign}, {adjust_value}, {from_units}, {to_units})

        Modifies Z-values of 3D features.

     INPUTS:
      in_features (Feature Layer):
          The 3D features whose Z values will be modified.
      reverse_sign {String}:
          Specifies whether features will be inverted along the Z-axis.

          * REVERSE—Inverts the sign of Z-values causing the feature to flip upside down.

          * NO_REVERSE—Maintains the sign of Z-values. This is the default.
      adjust_value {Double}:
          Uniformly adjusts all Z-values by the specified number.  Entering a negative
          number will decrease the Z-value, whereas a positive number will increase it.
      from_units {String}:
          The existing units of the Z-values. This parameter is used in conjunction with
          the Convert To Units parameter.

          * MILLIMETERS

          * CENTIMETERS

          * METERS

          * INCHES

          * FEET

          * YARDS

          * FATHOMS
      to_units {String}:
          The units that existing Z-values will be converted to.

          * MILLIMETERS

          * CENTIMETERS

          * METERS

          * INCHES

          * FEET

          * YARDS

          * FATHOMS"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Adjust3DZ_management(*gp_fixargs((in_features, reverse_sign, adjust_value, from_units, to_units), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BearingDistanceToLine_management', None)
def BearingDistanceToLine(in_table=None, out_featureclass=None, x_field=None, y_field=None, distance_field=None, distance_units=None, bearing_field=None, bearing_units=None, line_type=None, id_field=None, spatial_reference=None):
    """BearingDistanceToLine_management(in_table, out_featureclass, x_field, y_field, distance_field, distance_units, bearing_field, bearing_units, {line_type}, {id_field}, {spatial_reference})

        Creates a new feature class containing geodetic line features constructed based
        on the values in an x-coordinate field, y-coordinate field, bearing field, and
        distance field of a table.

     INPUTS:
      in_table (Table View):
          The input table that can be a text file, CSV file, Excel file, dBASE table, or
          geodatabase table.
      x_field (Field):
          A numerical field in the input table containing the x coordinates (or
          longitudes) of the starting points of lines to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      y_field (Field):
          A numerical field in the input table containing the y coordinates (or latitudes)
          of the starting points of lines to be positioned in the output coordinate system
          specified by the spatial_reference parameter.
      distance_field (Field):
          A numerical field in the input table containing the distances from the starting
          points for creating the output lines.
      distance_units (String):
          The units for the values in the distance_field.

          * METERS

          * KILOMETERS

          * MILES

          * NAUTICAL_MILES

          * FEET

          * US_SURVEY_FEET
      bearing_field (Field):
          A numerical field in the input table containing bearing angle values for the
          output line rotation. The angles are measured clockwise from North.
      bearing_units (String):
          The units of the values in the bearing_field.

          * DEGREES—Values in decimal degrees; this is the default.

          * MILS—Values in mils.

          * RADS—Values in radians.

          * GRADS—Values in gradians.
      line_type {String}:
          The type of geodetic line to construct.

          * GEODESIC— A type of geodetic line which most accurately represents the
          shortest distance between any two points on the surface of the earth. The
          mathematical definition of the geodesic line is quite lengthy and complex and
          therefore omitted here. This line type is the default.

          * GREAT_CIRCLE—A type of geodetic line which represents the path between any two
          points along the intersection of the surface of the earth and a plane that
          passes through the center of the earth. Depending on the output coordinate
          system specified by the Spatial Reference parameter, in a spheroid-based
          coordinate system, the line is a great elliptic; in a sphere-based coordinate
          system, the line is uniquely called a great circle—a circle of the largest
          radius on the spherical surface.

          * RHUMB_LINE—A type of geodetic line, also known as a loxodrome line, which
          represents a path between any two points on the surface of a spheroid defined by
          a constant azimuth from a pole. A rhumb line is shown as a straight line in the
          Mercator projection.

          * NORMAL_SECTION—A type of geodetic line which represents a path between any two
          points on the surface of a spheroid defined by the intersection of the spheroid
          surface and a plane that passes through the two points and is normal
          (perpendicular) to the spheroid surface at the starting point of the two points.
          Therefore, the normal section line from point A to point B is different from the
          one from point B to point A.
      id_field {Field}:
          A field in the input table; this field and the values are included in the
          output and can be used to join the output features with the records in the input
          table.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature class. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class containing densified geodetic lines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BearingDistanceToLine_management(*gp_fixargs((in_table, out_featureclass, x_field, y_field, distance_field, distance_units, bearing_field, bearing_units, line_type, id_field, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CheckGeometry_management', None)
def CheckGeometry(in_features=None, out_table=None):
    """CheckGeometry_management(in_features;in_features..., out_table)

        Generates a report of the geometry problems in a feature class.Valid input
        formats are shapefile and feature classes stored in a personal
        geodatabase or file geodatabase. SDE geodatabases automatically check the
        validity of each geometry when they are uploaded; therefore, the Check Geometry
        and Repair Geometry tools are not for use with SDE.For additional information on
        geometry problems, its impact on the software, and
        potential sources, see Checking and repairing geometries.

     INPUTS:
      in_features (Feature Layer):
          One or more feature classes or feature layers to check for geometry problems.
          Valid inputs are shapefile and feature classes stored in a personal geodatabase
          or file geodatabase.

     OUTPUTS:
      out_table (Table):
          The output table containing geometry problems discovered in the input features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CheckGeometry_management(*gp_fixargs((in_features, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CopyFeatures_management', None)
def CopyFeatures(in_features=None, out_feature_class=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None):
    """CopyFeatures_management(in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Copies features from the input feature class or layer to a new feature class. If
        the input is a layer which has a selection, only the selected features will be
        copied. If the input is a geodatabase feature class or shapefile, all features
        will be copied.

     INPUTS:
      in_features (Feature Layer / Raster Catalog Layer):
          The features to be copied.
      config_keyword {String}:
          Geodatabase configuration keyword to be applied if the output is an ArcSDE
          geodatabase or file geodatabase.
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
          2.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class which will be created and to which the features will be
          copied. If the output feature class already exists and the overwrite option is
          set to true, the output will be deleted first. If the output feature class
          already exists and the overwrite option is set to false, the operation will
          fail."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyFeatures_management(*gp_fixargs((in_features, out_feature_class, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteFeatures_management', None)
def DeleteFeatures(in_features=None):
    """DeleteFeatures_management(in_features)

        Deletes all or the selected subset of features from the input.If the input
        features are from a feature class or table, all rows will be
        deleted. If the input features are from a layer with no selection, all features
        will be deleted.

     INPUTS:
      in_features (Feature Layer):
          The feature class, shapefile, or layer containing features to be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteFeatures_management(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Dice_management', None)
def Dice(in_features=None, out_feature_class=None, vertex_limit=None):
    """Dice_management(in_features, out_feature_class, vertex_limit)

        Subdivides a feature into smaller features based on a specified vertex limit.
        This tool is intended as a way to subdivide extremely large features that cause
        issues with drawing, analysis, editing, and/or performance but are difficult to
        split up with standard editing and geoprocessing tools. This tool should not be
        used in any cases other than those where tools are failing to complete
        successfully due to the size of features.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or feature layer. The geometry type must be multipoint,
          line, or polygon.
      vertex_limit (Long):
          Features with geometries that exceed this vertex limit will be subdivided before
          being written to the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class of diced features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Dice_management(*gp_fixargs((in_features, out_feature_class, vertex_limit), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureEnvelopeToPolygon_management', None)
def FeatureEnvelopeToPolygon(in_features=None, out_feature_class=None, single_envelope=None):
    """FeatureEnvelopeToPolygon_management(in_features, out_feature_class, {single_envelope})

        Creates a feature class containing polygons, each of which represents the
        envelope of an input feature.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be multipoint, line, polygon, or annotation.
      single_envelope {Boolean}:
          Specifies whether to use one envelope for each entire multipart feature or one
          envelope per part of a multipart feature. This parameter will affect the results
          of multipart input features only.

          * SINGLEPART—Uses one envelope containing an entire multipart feature;
          therefore, the resulting polygon will be singlepart. This is the default.

          * MULTIPART— Uses one envelope for each part of a multipart feature; the
          resulting polygon of the multipart feature will remain multipart.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureEnvelopeToPolygon_management(*gp_fixargs((in_features, out_feature_class, single_envelope), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureToLine_management', None)
def FeatureToLine(in_features=None, out_feature_class=None, cluster_tolerance=None, attributes=None):
    """FeatureToLine_management(in_features;in_features..., out_feature_class, {cluster_tolerance}, {attributes})

        Creates a feature class containing lines generated by converting polygon
        boundaries to lines, or splitting line, polygon, or both features at their
        intersections.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon, or both.
      cluster_tolerance {Linear unit}:
          The minimum distance separating all feature coordinates, and the distance a
          coordinate can move in X, Y, or both during spatial computation. The default XY
          tolerance is set to 0.001 meter or its equivalent in feature units.
      attributes {Boolean}:
          Specifies whether to preserve or omit the input attributes in the output feature
          class.

          * ATTRIBUTES—Preserves the input attributes in the output features. This is the
          default.

          * NO_ATTRIBUTES—Omits the input attributes in the output features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureToLine_management(*gp_fixargs((in_features, out_feature_class, cluster_tolerance, attributes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureToPoint_management', None)
def FeatureToPoint(in_features=None, out_feature_class=None, point_location=None):
    """FeatureToPoint_management(in_features, out_feature_class, {point_location})

        Creates a feature class containing points generated from the representative
        locations of input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be multipoint, line, polygon, or annotation.
      point_location {Boolean}:
          Specifies whether to use representative centers of input features or locations
          contained by input features as the output point locations.

          * CENTROID—Uses the representative center of an input feature as its output
          point location. This is the default. This point location may not always be
          contained by the input feature.

          * INSIDE—Uses a location contained by an input feature as its output point
          location.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureToPoint_management(*gp_fixargs((in_features, out_feature_class, point_location), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureToPolygon_management', None)
def FeatureToPolygon(in_features=None, out_feature_class=None, cluster_tolerance=None, attributes=None, label_features=None):
    """FeatureToPolygon_management(in_features;in_features..., out_feature_class, {cluster_tolerance}, {attributes}, {label_features})

        Creates a feature class containing polygons generated from areas enclosed by
        input line or polygon features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon, or both.
      cluster_tolerance {Linear unit}:
          The minimum distance separating all feature coordinates, and the distance a
          coordinate can move in X, Y, or both during spatial computation. The default XY
          tolerance is set to 0.001 meter or its equivalent in feature units.
      attributes {Boolean}:
          Specifies whether to preserve the input attribute schema or the attribures from
          label features in the output feature class, or omit any input attributes in the
          output feature class. This parameter does not work. It will not be removed for
          backward compatibility of scripts or models. The output attribute schema and
          field values for certain input combinations may be produced as described in the
          usage notes; most of them are unintended.

          * ATTRIBUTES—Preserves the input attribute schema or the attribures from label
          features, if provided, in the output features. This is the default.

          * NO_ATTRIBUTES—Omits any input attributes in the output feature class.
      label_features {Feature Layer}:
          The optional input point features that hold the attributes to be transferred to
          the output polygon features.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureToPolygon_management(*gp_fixargs((in_features, out_feature_class, cluster_tolerance, attributes, label_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FeatureVerticesToPoints_management', None)
def FeatureVerticesToPoints(in_features=None, out_feature_class=None, point_location=None):
    """FeatureVerticesToPoints_management(in_features, out_feature_class, {point_location})

        Creates a feature class containing points generated from specified vertices or
        locations of the input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon.
      point_location {String}:
          Specifies where an output point will be created.

          * ALL—A point will be created at each input feature vertex. This is the default.

          * MID—A point will be created at the midpoint, not necessarily a vertex, of each
          input line or polygon boundary.

          * START—A point will be created at the start point (first vertex) of each input
          feature.

          * END—A point will be created at the end point (last vertex) of each input
          feature.

          * BOTH_ENDS—Two points will be created, one at the start point and another at
          the endpoint of each input feature.

          * DANGLE —A dangle point will be created for any start or end point of an input
          line, if that point is not connected to another line at any location along that
          line. This option does not apply to polygon input.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output point feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureVerticesToPoints_management(*gp_fixargs((in_features, out_feature_class, point_location), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GeodeticDensify_management', None)
def GeodeticDensify(in_features=None, out_feature_class=None, geodetic_type=None, distance=None):
    """GeodeticDensify_management(in_features, out_feature_class, geodetic_type, {distance})

        Creates new features by replacing input feature's segments with densified
        approximations of geodesic segments. Four type of geodesic segments can be
        constructed: Geodesic, Great Elliptic, Loxodrome, and Normal Section.

     INPUTS:
      in_features (Feature Layer):
          The input line or polygon features.
      geodetic_type (String):
          The type of geodetic segment to construct. Geodetic calculations are performed
          on the ellipsoid associated with the input data's coordinate system.

          * GEODESIC—The shortest distance between two points on the surface of the
          spheroid (ellipsoid).

          * LOXODROME—The line of equal azimuth (from a pole) connecting the two points.

          * GREAT_ELLIPTIC— The line made by the intersection of a plane that contains the
          center of the spheroid and the two points.

          * NORMAL_SECTION—The line made by the intersection of a plane that contains the
          center of the spheroid and is perpendicular to the surface at the first point.
      distance {Linear unit}:
          The distance between vertices along the output geodesic segment. The default
          value is 50 kilometers.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the densified geodesic features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeodeticDensify_management(*gp_fixargs((in_features, out_feature_class, geodetic_type, distance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MinimumBoundingGeometry_management', None)
def MinimumBoundingGeometry(in_features=None, out_feature_class=None, geometry_type=None, group_option=None, group_field=None, mbg_fields_option=None):
    """MinimumBoundingGeometry_management(in_features, out_feature_class, {geometry_type}, {group_option}, {group_field;group_field...}, {mbg_fields_option})

        Creates a feature class containing polygons which represent a specified minimum
        bounding geometry enclosing each input feature or each group of input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be point, multipoint, line, polygon, or multipatch.
      geometry_type {String}:
          Specifies what type of minimum bounding geometry the output polygons will
          represent.

          * RECTANGLE_BY_AREA—The rectangle of the smallest area enclosing an input
          feature. This is the default.

          * RECTANGLE_BY_WIDTH—The rectangle of the smallest width enclosing an input
          feature.

          * CONVEX_HULL—The smallest convex polygon enclosing an input feature.

          * CIRCLE—The smallest circle enclosing an input feature.

          * ENVELOPE—The envelope of an input feature.
          The CONVEX_HULL, CIRCLE, and ENVELOPE options are only available with an ArcGIS
          for Desktop Advanced license.
      group_option {String}:
          Specifies how the input features will be grouped; each group will be enclosed
          with one output polygon.

          * NONE—Input features will not be grouped. This is the default. This option is
          not available for point input.

          * ALL—All input features will be treated as one group.

          * LIST—Input features will be grouped based on their common values in the
          specified field or fields in the group field parameter.
      group_field {Field}:
          The field or fields in the input features that will be used to group features,
          when LIST is specified as group_option. At least one group field is required for
          LIST option. All features that have the same value in the specified field or
          fields will be treated as a group.
      mbg_fields_option {Boolean}:
          Specifies whether to add the geometric attributes in the output feature class or
          omit them in the output feature class.

          * NO_MBG_FIELDS—Omits any input attributes in the output feature class. This is
          the default.

          * MBG_FIELDS—Adds the geometric attributes in the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MinimumBoundingGeometry_management(*gp_fixargs((in_features, out_feature_class, geometry_type, group_option, group_field, mbg_fields_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MultipartToSinglepart_management', None)
def MultipartToSinglepart(in_features=None, out_feature_class=None):
    """MultipartToSinglepart_management(in_features, out_feature_class)

        Creates a feature class containing singlepart features generated by separating
        multipart input features.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be any feature type.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing features that vary with input feature type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MultipartToSinglepart_management(*gp_fixargs((in_features, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PointsToLine_management', None)
def PointsToLine(Input_Features=None, Output_Feature_Class=None, Line_Field=None, Sort_Field=None, Close_Line=None):
    """PointsToLine_management(Input_Features, Output_Feature_Class, {Line_Field}, {Sort_Field}, {Close_Line})

        Creates line features from points.

     INPUTS:
      Input_Features (Feature Layer):
          The point features to be converted into lines.
      Line_Field {Field}:
          Each feature in the output will be based on unique values in the Line Field.
      Sort_Field {Field}:
          By default, points used to create each output line feature will be used in the
          order they are found. If a different order is desired, specify a Sort Field.
      Close_Line {Boolean}:
          Specifies whether output line features should be closed.

          * CLOSE—An extra vertex will be added to ensure that every output line feature's
          end point will match up with its start point. Then polygons can be generated
          from the line feature class using the Feature To Polygon tool.

          * NO_CLOSE—No extra vertices will be added to close an output line feature. This
          is the default.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The line feature class which will be created from the input points."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PointsToLine_management(*gp_fixargs((Input_Features, Output_Feature_Class, Line_Field, Sort_Field, Close_Line), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PolygonToLine_management', None)
def PolygonToLine(in_features=None, out_feature_class=None, neighbor_option=None):
    """PolygonToLine_management(in_features, out_feature_class, {neighbor_option})

        Creates a feature class containing lines that are converted from polygon
        boundaries with or without considering neighboring polygons.

     INPUTS:
      in_features (Feature Layer):
          The input features that must be polygon.
      neighbor_option {Boolean}:
          Specifies whether or not to identify and store polygon neighboring information.

          *  IDENTIFY_NEIGHBORS—Polygon neighboring relationship will be identified and
          stored in the output. If different segments of a polygon share boundary with
          different polygons, the boundary will be split such that each uniquely shared
          segment will become a line with its two neighboring polygon FIDs stored in the
          output. This is the default.

          *  IGNORE_NEIGHBORS—Polygon neighboring relationship will be ignored; every
          polygon boundary will become a line feature with its original polygon feature ID
          stored in the output.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PolygonToLine_management(*gp_fixargs((in_features, out_feature_class, neighbor_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RepairGeometry_management', None)
def RepairGeometry(in_features=None, delete_null=None):
    """RepairGeometry_management(in_features, {delete_null})

        Inspects each feature in a feature class for geometry problems. Upon discovery
        of a geometry problem, a relevant fix will be applied, and a one-line
        description will be printed identifying the feature as well as the problem
        encountered. Valid inputs are shapefiles, personal, and file geodatabase feature
        classes.

     INPUTS:
      in_features (Feature Layer):
          The feature class or layer that will be repaired. Valid input features are
          shapefiles and personal and file geodatabase feature classes.
      delete_null {Boolean}:
          Specifies what action to take on null geometries.

          * DELETE_NULL — Features that have NULL geometry will be deleted from the input.
          This is the default.

          * KEEP_NULL — Features that have NULL geometry will not be deleted from the
          input."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RepairGeometry_management(*gp_fixargs((in_features, delete_null), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SplitLine_management', None)
def SplitLine(in_features=None, out_feature_class=None):
    """SplitLine_management(in_features, out_feature_class)

        Creates a feature class containing lines that are generated by splitting input
        lines or polygon boundaries at their vertices.

     INPUTS:
      in_features (Feature Layer):
          The input features that can be line or polygon.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SplitLine_management(*gp_fixargs((in_features, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SplitLineAtPoint_management', None)
def SplitLineAtPoint(in_features=None, point_features=None, out_feature_class=None, search_radius=None):
    """SplitLineAtPoint_management(in_features, point_features, out_feature_class, {search_radius})

        Splits line features based on intersection or proximity to point features.

     INPUTS:
      in_features (Feature Layer):
          The input line features to be split.
      point_features (Feature Layer):
          The input point features whose locations will be used to split the input lines.
      search_radius {Linear unit}:
          Used to split lines by their proximity to point features. Points within the
          search distance to an input line will be used to split those lines at the
          nearest location to the point along the line segment.

     OUTPUTS:
      out_feature_class (Feature Class):
          The new feature class that will be created containing the split lines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SplitLineAtPoint_management(*gp_fixargs((in_features, point_features, out_feature_class, search_radius), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToEllipse_management', None)
def TableToEllipse(in_table=None, out_featureclass=None, x_field=None, y_field=None, major_field=None, minor_field=None, distance_units=None, azimuth_field=None, azimuth_units=None, id_field=None, spatial_reference=None):
    """TableToEllipse_management(in_table, out_featureclass, x_field, y_field, major_field, minor_field, distance_units, {azimuth_field}, {azimuth_units}, {id_field}, {spatial_reference})

        Creates a new feature class containing geodetic ellipse features constructed
        based on the values in an x-coordinate field, y-coordinate field, major-axis
        field, minor-axis field, and azimuth field of a table.

     INPUTS:
      in_table (Table View):
          The input table that can be a text file, CSV file, Excel file, dBASE table, or
          geodatabase table.
      x_field (Field):
          A numerical field in the input table containing the x coordinates (or
          longitudes) of the center points of ellipses to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      y_field (Field):
          A numerical field in the input table containing the y coordinates (or
          latitudes) of the center points of ellipses to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      major_field (Field):
          A numerical field in the input table containing major axis lengths of the
          ellipses.
      minor_field (Field):
          A numerical field in the input table containing minor axis lengths of the
          ellipses.
      distance_units (String):
          The units for the values in Major Field and Minor Field.

          * METERS

          * KILOMETERS

          * MILES

          * NAUTICAL_MILES

          * FEET

          * US_SURVEY_FEET
      azimuth_field {Field}:
          A numerical field in the input table containing azimuth angle values for the
          major axis rotations of the output ellipses. The values are measured clockwise
          from North.
      azimuth_units {String}:
          The units of the values in the Azimuth Field.

          * DEGREES—Values in decimal degrees; this is the default.

          * MILS—Values in mils.

          * RADS—Values in radians.

          * GRADS—Values in gradians.
      id_field {Field}:
          A field in the input table; this field and the values are included in the
          output and can be used to join the output features with the records in the input
          table.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature class. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class containing geodetic ellipses as densified polylines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToEllipse_management(*gp_fixargs((in_table, out_featureclass, x_field, y_field, major_field, minor_field, distance_units, azimuth_field, azimuth_units, id_field, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UnsplitLine_management', None)
def UnsplitLine(in_features=None, out_feature_class=None, dissolve_field=None, statistics_fields=None):
    """UnsplitLine_management(in_features, out_feature_class, {dissolve_field;dissolve_field...}, {statistics_fields;statistics_fields...})

        Merges lines that have coincident endpoints and, optionally, common attribute
        values.

     INPUTS:
      in_features (Feature Layer):
          The line features to be aggregrated.
      dissolve_field {Field}:
          The field or fields on which to aggregate features.The Add Field button, which
          is used only in ModelBuilder, allows you to add
          expected fields so you can complete the dialog box and continue to build your
          model.
      statistics_fields {Value Table}:
          The fields and statistics with which to summarize attributes. Text attribute
          fields may be summarized using the statistics FIRST or LAST. Numeric attribute
          fields may be summarized using any statistic. Nulls are excluded from all
          statistical calculations.

          * FIRST—Finds the first record in the Input Features and uses its specified
          field value.

          * LAST—Finds the last record in the Input Features and uses its specified field
          value.

          * SUM—Adds the total value for the specified field.

          * MEAN—Calculates the average for the specified field.

          * MIN—Finds the smallest value for all records of the specified field.

          * MAX—Finds the largest value for all records of the specified field.

          * RANGE—Finds the range of values (MAX–MIN) for the specified field.

          * STD—Finds the standard deviation on values in the specified field.

          * COUNT—Finds the number of values included in statistical calculations. This
          counts each value except null values. To determine the number of null values in
          a field, use the COUNT statistic on the field in question, and a COUNT statistic
          on a different field which does not contain nulls (for example, the OID if
          present), then subtract the two values.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created that will contain the aggregated features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UnsplitLine_management(*gp_fixargs((in_features, out_feature_class, dissolve_field, statistics_fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('XYToLine_management', None)
def XYToLine(in_table=None, out_featureclass=None, startx_field=None, starty_field=None, endx_field=None, endy_field=None, line_type=None, id_field=None, spatial_reference=None):
    """XYToLine_management(in_table, out_featureclass, startx_field, starty_field, endx_field, endy_field, {line_type}, {id_field}, {spatial_reference})

        Creates a new feature class containing geodetic line features constructed based
        on the values in a start x-coordinate field, start y-coordinate field, end
        x-coordinate field, and end y-coordinate field of a table.

     INPUTS:
      in_table (Table View):
          The input table that can be a text file, CSV file, Excel file, dBASE table, or
          geodatabase table.
      startx_field (Field):
          A numerical field in the input table containing the x coordinates (or
          longitudes) of the starting points of lines to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      starty_field (Field):
          A numerical field in the input table containing the y coordinates (or latitudes)
          of the starting points of lines to be positioned in the output coordinate system
          specified by the spatial_reference parameter.
      endx_field (Field):
          A numerical field in the input table containing the x coordinates (or
          longitudes) of the ending points of lines to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      endy_field (Field):
          A numerical field in the input table containing the y coordinates (or
          latitudes) of the ending points of lines to be positioned in the output
          coordinate system specified by the spatial_reference parameter.
      line_type {String}:
          The type of geodetic line to construct.

          * GEODESIC— A type of geodetic line which most accurately represents the
          shortest distance between any two points on the surface of the earth. The
          mathematical definition of the geodesic line is quite lengthy and complex and
          therefore omitted here. This line type is the default.

          * GREAT_CIRCLE—A type of geodetic line which represents the path between any two
          points along the intersection of the surface of the earth and a plane that
          passes through the center of the earth. Depending on the output coordinate
          system specified by the Spatial Reference parameter, in a spheroid-based
          coordinate system, the line is a great elliptic; in a sphere-based coordinate
          system, the line is uniquely called a great circle—a circle of the largest
          radius on the spherical surface.

          * RHUMB_LINE—A type of geodetic line, also known as a loxodrome line, which
          represents a path between any two points on the surface of a spheroid defined by
          a constant azimuth from a pole. A rhumb line is shown as a straight line in the
          Mercator projection.

          * NORMAL_SECTION—A type of geodetic line which represents a path between any two
          points on the surface of a spheroid defined by the intersection of the spheroid
          surface and a plane that passes through the two points and is normal
          (perpendicular) to the spheroid surface at the starting point of the two points.
          Therefore, the normal section line from point A to point B is different from the
          one from point B to point A.
      id_field {Field}:
          A field in the input table; this field and the values are included in the
          output and can be used to join the output features with the records in the input
          table.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature class. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class containing densified geodetic lines."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.XYToLine_management(*gp_fixargs((in_table, out_featureclass, startx_field, starty_field, endx_field, endy_field, line_type, id_field, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e


# Fields toolset
@gptooldoc('AddField_management', None)
def AddField(in_table=None, field_name=None, field_type=None, field_precision=None, field_scale=None, field_length=None, field_alias=None, field_is_nullable=None, field_is_required=None, field_domain=None):
    """AddField_management(in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})

        Adds a new field to a table or the table of a feature class, feature layer,
        raster catalog, and/or rasters with attribute tables.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The input table to which the specified field will be added. The field will be
          added to the existing input table and will not create a new output table.Fields
          can be added to feature classes of ArcSDE, file or personal geodatabases,
          coverages, shapefiles, raster catalogs, stand-alone tables, rasters with
          attribute tables, and/or layers.
      field_name (String):
          The name of the field that will be added to the input table.
      field_type (String):
          The field type of the new field.

          * TEXT—Any string of characters.

          * FLOAT— Fractional numbers between -3.4E38 and 1.2E38.

          * DOUBLE— Fractional numbers between -2.2E308 and 1.8E308.

          * SHORT— Whole numbers between -32,768 and 32,767.

          * LONG— Whole numbers between -2,147,483,648 and 2,147,483,647.

          * DATE—Date and/or time.

          * BLOB—Long sequence of binary numbers. You need a custom loader or viewer or a
          third-party application to load items into a BLOB field or view the contents of
          a BLOB field.

          * RASTER—Raster images. All ArcGIS software-supported raster dataset formats can
          be stored, but it is highly recommended that only small images be used.

          * GUID—Globally unique identifier.
      field_precision {Long}:
          The number of digits that can be stored in the field. All digits are counted no
          matter what side of the decimal they are on.If the input table is a personal or
          file geodatabase the field precision value
          will be ignored.
      field_scale {Long}:
          The number of decimal places stored in a field. This parameter is only used in
          float and double data field types.If the input table is a personal or file
          geodatabase the field scale value will
          be ignored.
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

          * NULLABLE—The field will allow null values. This is the default.
      field_is_required {Boolean}:
          Specifies whether the field being created is a required field for the table;
          only supported for fields in a geodatabase.

          * NON_REQUIRED—The field is not a required field. This is the default.

          * REQUIRED—The field is a required field. Required fields are permanent and can
          not be deleted.
      field_domain {String}:
          Used to constrain the values allowed in any particular attribute for a table,
          feature class, or subtype in a geodatabase. You must specify the name of an
          existing domain for it to be applied to the field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddField_management(*gp_fixargs((in_table, field_name, field_type, field_precision, field_scale, field_length, field_alias, field_is_nullable, field_is_required, field_domain), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddIncrementingIDField_management', None)
def AddIncrementingIDField(in_table=None, field_name=None):
    """AddIncrementingIDField_management(in_table, {field_name})

        The Add Incrementing ID Field tool adds a database-maintained ID field to an
        existing table or feature class in an ALTIBASE, IBM DB2, Microsoft SQL Server,
        Oracle, or PostgreSQL database. A database-maintained ID field is required on
        all feature classes or tables you plan to edit through a feature service.

     INPUTS:
      in_table (Table View):
          The location and name of the table to which you want to add an ID field.
      field_name {String}:
          The name to be used for the ID field. If no input is provided, the name defaults
          to objectid."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddIncrementingIDField_management(*gp_fixargs((in_table, field_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AlterField_management', None)
def AlterField(in_table=None, field=None, new_field_name=None, new_field_alias=None, field_type=None, field_length=None, field_is_nullable=None, clear_field_alias=None):
    """AlterField_management(in_table, field, {new_field_name}, {new_field_alias}, {field_type}, {field_length}, {field_is_nullable}, {clear_field_alias})

        Rename fields and field aliases, or alter field properties.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          Input table or feature class that contains the field to alter.
      field (Field):
          The name of the field to alter. If the field is a required field
          (isRequired=true), only the field alias may be altered.
      new_field_name {String}:
          The new name for the field.
      new_field_alias {String}:
          The new field alias for the field.
      field_type {String}:
          The new field type for the field. Only applicable if the input table is empty
          (does not contain records).

          * TEXT—Any string of characters.

          * FLOAT— Fractional numbers between -3.4E38 and 1.2E38.

          * DOUBLE— Fractional numbers between -2.2E308 and 1.8E308.

          * SHORT— Whole numbers between -32,768 and 32,767.

          * LONG— Whole numbers between -2,147,483,648 and 2,147,483,647.

          * DATE—Date and/or time.

          * BLOB—Long sequence of binary numbers. You need a custom loader or viewer or a
          third-party application to load items into a BLOB field or view the contents of
          a BLOB field.

          * RASTER—Raster images. All ArcGIS software-supported raster dataset formats can
          be stored, but it is highly recommended that only small images be used.

          * GUID—Globally unique identifier.
      field_length {Long}:
          The new length of the field. This sets the maximum number of allowable
          characters for each record of the field. This option is only applicable on
          fields of type TEXT or BLOB. Only applicable if table is empty.
      field_is_nullable {Boolean}:
          Determines if the field can contain null values. Null values are only supported
          for fields in a geodatabase. Only applicable if the input table is empty (does
          not contain records).

          * NON_NULLABLE—The field will not allow null values.

          * NULLABLE—The field will allow null values. This is the default.
      clear_field_alias {Boolean}:
          Specify whether to clear the alias for the input field. The field alias
          parameter must be empty to clear the alias of the field.

          * TRUE—The field alias will be cleared (set to null).

          * FALSE—The field alias will not be cleared. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AlterField_management(*gp_fixargs((in_table, field, new_field_name, new_field_alias, field_type, field_length, field_is_nullable, clear_field_alias), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AssignDefaultToField_management', None)
def AssignDefaultToField(in_table=None, field_name=None, default_value=None, subtype_code=None, clear_value=None):
    """AssignDefaultToField_management(in_table, field_name, {default_value}, {subtype_code;subtype_code...}, {clear_value})

        This tool will create a default value for a specified field. Whenever a new row
        is added to the table or feature class, the specified field will be set to this
        default value.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          Input table or feature class that will have a default value added to one of its
          fields.
      field_name (Field):
          The field that will have the default value added to it each time a new row is
          added to the table or feature class.
      default_value {String}:
          The default value to be added to each new table or feature class. The value
          entered must match the data type of the field.
      subtype_code {String}:
          The subtypes that can participate in the default value.
      clear_value {Boolean}:
          Specify whether to clear the default value for either the field or the subtype.
          To clear the default value, the default_value parameter must be passed in as an
          empty string. To clear the default value for the subtype, you must also specify
          the subtype which is to be cleared.

          * TRUE—The default value will be cleared (set to null).

          * FALSE—The default value will not be cleared. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AssignDefaultToField_management(*gp_fixargs((in_table, field_name, default_value, subtype_code, clear_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateEndTime_management', None)
def CalculateEndTime(in_table=None, start_field=None, end_field=None, fields=None):
    """CalculateEndTime_management(in_table, start_field, end_field, {fields;fields...})

        Calculates the end time of features based on the time values stored in another
        field.In the illustration below, the end time values in the End_Time field are
        calculated using the time values in the Start_Time field. The end time value for
        a feature is equal to the start time of the next feature. However, for the last
        feature in the table, the end time value is calculated to be the same as the
        start time value of the feature.

     INPUTS:
      in_table (Table View):
          The feature class or table for which an End Time Field is calculated based on
          the Start Time Field specified.
      start_field (Field):
          The field containing values that will be used to calculate values for the End
          Time Field. The Start Time Field and the End Time Field must be of the same
          type. For example, if the Start Time Field is of type LONG, then the End Time
          Field should be of type LONG as well.
      end_field (Field):
          The field that will be populated with values based on the Start Time Field
          specified. The Start Time Field and the End Time Field must be of the same
          format.
      fields {Field}:
          The name of the field or fields that can be used to uniquely identify spatial
          entities. These fields are used to first sort based on entity type if there is
          more than one entity. For instance, for a feature class representing population
          values per state over time, the state name could be the unique value field (the
          entity). If population figures are per county, you would need to set the county
          name and state name as the unique value fields, since some county names are the
          same for different states. If there is only one entity, this parameter can be
          ignored."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateEndTime_management(*gp_fixargs((in_table, start_field, end_field, fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateField_management', None)
def CalculateField(in_table=None, field=None, expression=None, expression_type=None, code_block=None):
    """CalculateField_management(in_table, field, expression, {expression_type}, {code_block})

        Calculates the values of a field for a feature class, feature layer, or raster.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table containing the field that will be updated with the new calculation.
      field (Field):
          The field that will be updated with the new calculation.
      expression (SQL Expression):
          The simple calculation expression used to create a value that will populate the
          selected rows.
      expression_type {String}:
          Specify the type of expression that will be used.

          * VB—The expression will be written in a standard VB format. This is the
          default.

          * PYTHON—The expression will be written in a standard Python format. Use of
          geoprocessor methods and properties is the same as creating a 9.2 version
          geoprocessor.

          * PYTHON_9.3—The expression will be written in a standard Python format. Use of
          geoprocessor methods and properties is the same as creating a 9.3 version
          geoprocessor.
          Field calculations with a VB Expression type are not supported on 64-bit
          products, including ArcGIS Pro, ArcGIS for Desktop—Background Geoprocessing
          (64-bit) and ArcGIS for Server. To successfully use Calculate Field in these
          products, expressions should be converted to Python, or in the case of
          Background Geoprocessing (64-bit), background processing can alternatively be
          disabled.
      code_block {String}:
          Allows for a block of code to be entered for complex expressions."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateField_management(*gp_fixargs((in_table, field, expression, expression_type, code_block), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConvertTimeField_management', None)
def ConvertTimeField(in_table=None, input_time_field=None, input_time_format=None, output_time_field=None, output_time_type=None, output_time_format=None):
    """ConvertTimeField_management(in_table, input_time_field, input_time_format, output_time_field, {output_time_type}, {output_time_format})

        Converts time values stored in a string or numeric field to a date field. The
        tool can also be used to convert time values stored in string, numeric, or date
        fields into custom formats such as day of the week, month of the year, and so
        on.

     INPUTS:
      in_table (Table View):
          The layer or table that contains the field containing the time values that need
          to be converted.
      input_time_field (Field):
          The field containing the time values. May be of type short, long, float,
          double, text, or date.
      input_time_format (String):
          The format in which the time values were stored in the input time field.  Either
          a standard time format can be selected from the drop-down list, or a custom
          format can be entered. If the data type of the time field is numeric (Short,
          Long, Float, or Double), a list of standard numeric time formats is provided in
          the drop-down list. If the data type of the time field is string, a list of
          standard string time formats is provided in the drop-down list. For string
          fields, you can also choose to specify a custom time format. For example, the
          time values may have been stored in a string field in one of the standard
          formats such as yyyy/MM/dd HH:mm:ss or in a custom format such as dd/MM/yyyy
          HH:mm:ss. For the custom format, you can also specify the a.m., p.m.
          designator.If the data type of the time field is date, then no time format is
          required.
      output_time_field (String):
          The name of output field in which the converted time values will be stored.
      output_time_type {String}:
          The data type of the output time field.

          * DATE—Date and/or time.

          * TEXT—Any string of characters

          * LONG—Whole numbers between -2,147,483,648 and 2,147,483,647.

          * SHORT—Whole numbers between -32,768 and 32,767.

          * DOUBLE—Fractional numbers between -2.2E308 and 1.8E308.

          * FLOAT—Fractional numbers between -3.4E38 and 1.2E38.
      output_time_format {String}:
          The format in which the output time values will be saved. The list of output
          time formats depends on the output data type specified for the output time
          field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConvertTimeField_management(*gp_fixargs((in_table, input_time_field, input_time_format, output_time_field, output_time_type, output_time_format), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConvertTimeZone_management', None)
def ConvertTimeZone(in_table=None, input_time_field=None, input_time_zone=None, output_time_field=None, output_time_zone=None, input_dst=None, output_dst=None):
    """ConvertTimeZone_management(in_table, input_time_field, input_time_zone, output_time_field, output_time_zone, {input_dst}, {output_dst})

        Converts time values recorded in a date field from one time zone to another
        time zone.Converting time values from one time zone to another helps normalize
        temporal
        data from different time zones. This improves display and query performance for
        visualizing temporal data from different time zones using the Time Slider.

     INPUTS:
      in_table (Table View):
          The input feature class or table that contains the time stamps which will be
          transformed to a different time zone.
      input_time_field (Field):
          The input field that contains the time stamps which will be transformed to a
          different time zone.
      input_time_zone (String):
          The input time zone in which the time stamps were collected.
      output_time_field (String):
          The output field in which the time stamps transformed to the desired output
          time zone will be stored.
      output_time_zone (String):
          The time zone to which the time stamps will be transformed. By default, the
          output time zone is the same as the input time zone.
      input_dst {Boolean}:
          Indicates whether the time stamps were collected while observing Daylight Saving
          Time rules in the input time zone. When reading the time values to convert the
          time zone, the time values will be adjusted to account for the shift in time
          during Daylight Saving Time.By default, the  input time values are adjusted to
          account for the shift in time
          due to the Daylight Saving Time rules in the input time zone.

          * INPUT_ADJUSTED_FOR_DST—The input time values are adjusted for Daylight Saving
          Time.

          * INPUT_NOT_ADJUSTED_FOR_DST—The input time values are not adjusted for Daylight
          Saving Time.
      output_dst {Boolean}:
          Indicates whether the output time values will account for the shift in time due
          to the Daylight Saving Time rules observed in the output time zone.By default,
          the  output time values are adjusted to account for the shift in
          time due to the Daylight Saving Time rules observed in the output time zone.

          * OUTPUT_ADJUSTED_FOR_DST—The output time values will be adjusted for Daylight
          Saving Time in the out time zone.

          * OUTPUT_NOT_ADJUSTED_FOR_DST—The output time values will not be adjusted for
          Daylight Saving Time in the out time zone."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConvertTimeZone_management(*gp_fixargs((in_table, input_time_field, input_time_zone, output_time_field, output_time_zone, input_dst, output_dst), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteField_management', None)
def DeleteField(in_table=None, drop_field=None):
    """DeleteField_management(in_table, drop_field;drop_field...)

        This tool deletes one or more fields from a table, feature class, feature layer,
        or raster dataset.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table containing the fields to be deleted. The existing input table will be
          modified.
      drop_field (Field):
          The fields to be dropped from the input table. Only nonrequired fields may be
          deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteField_management(*gp_fixargs((in_table, drop_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DisableEditorTracking_management', None)
def DisableEditorTracking(in_dataset=None, creator=None, creation_date=None, last_editor=None, last_edit_date=None):
    """DisableEditorTracking_management(in_dataset, {creator}, {creation_date}, {last_editor}, {last_edit_date})

        Disables editor tracking on a feature class, table, mosaic dataset, or raster
        catalog.

     INPUTS:
      in_dataset (Dataset):
          The feature class, table, mosaic dataset, or raster catalog that will have
          editor tracking disabled.
      creator {Boolean}:
          Indicates whether to disable editor tracking for the creator field.

          * DISABLE_CREATOR—Editor tracking for the creator field will be disabled. This
          is the default.

          * NO_DISABLE_CREATOR—Editor tracking for the creator field will not be disabled.
      creation_date {Boolean}:
          Indicates whether to disable editor tracking for the creation date field.

          * DISABLE_CREATION_DATE—Editor tracking for the creation date field will be
          disabled. This is the default.

          * NO_DISABLE_CREATION_DATE—Editor tracking for the creation date field will not
          be disabled.
      last_editor {Boolean}:
          Indicates whether to disable editor tracking for the last editor field.

          * DISABLE_LAST_EDITOR—Editor tracking for the last editor field will be
          disabled. This is the default.

          * NO_DISABLE_LAST_EDITOR—Editor tracking for the last editor field will not be
          disabled.
      last_edit_date {Boolean}:
          Indicates whether to disable editor tracking for the last edit date field.

          * DISABLE_LAST_EDIT_DATE—Editor tracking for the last edit date field will be
          disabled. This is the default.

          * NO_DISABLE_LAST_EDIT_DATE—Editor tracking for the last edit date field will
          not be disabled."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DisableEditorTracking_management(*gp_fixargs((in_dataset, creator, creation_date, last_editor, last_edit_date), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EnableEditorTracking_management', None)
def EnableEditorTracking(in_dataset=None, creator_field=None, creation_date_field=None, last_editor_field=None, last_edit_date_field=None, add_fields=None, record_dates_in=None):
    """EnableEditorTracking_management(in_dataset, {creator_field}, {creation_date_field}, {last_editor_field}, {last_edit_date_field}, {add_fields}, {record_dates_in})

        Enables editor tracking for a feature class, table, mosaic dataset, or raster
        catalog.

     INPUTS:
      in_dataset (Dataset):
          The feature class, table, mosaic dataset, or raster catalog that will have
          editor tracking enabled.
      creator_field {String}:
          The name of the field that will store the names of users who created features
          or records. If this field already exists, it must be a String field.
      creation_date_field {String}:
          The name of the field that will store the dates features or records were
          created. If this field already exists, it must be a Date field.
      last_editor_field {String}:
          The name of the field that will store the names of users who last edited
          features or records. If this field already exists, it must be a String field.
      last_edit_date_field {String}:
          The name of the field that will store the dates features or records were last
          edited. If this field already exists, it must be a Date field.
      add_fields {Boolean}:
          Specifies whether to add fields if they don't already exist.

          * NO_ADD_FIELDS—Fields will not be added. Fields specified must already exist.
          This is the default.

          * ADD_FIELDS—Fields will be added if they don't already exist.
      record_dates_in {String}:
          The time created date and last edited date will be recorded in. The default is
          UTC (Coordinated Universal Time).

          * UTC—Record dates in UTC (Coordinated Universal Time). This is the default.

          * DATABASE_TIME—Record dates in the time zone in which the database is located."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EnableEditorTracking_management(*gp_fixargs((in_dataset, creator_field, creation_date_field, last_editor_field, last_edit_date_field, add_fields, record_dates_in), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TransposeFields_management', None)
def TransposeFields(in_table=None, in_field=None, out_table=None, in_transposed_field_name=None, in_value_field_name=None, attribute_fields=None):
    """TransposeFields_management(in_table, in_field;in_field..., out_table, in_transposed_field_name, in_value_field_name, {attribute_fields;attribute_fields...})

        Shifts data entered in fields or columns into rows in a table or feature
        class.This tool is useful when your table or feature class stores values in
        field
        names (such as Field1, Field2, Field3) and you want to transpose the field names
        and the corresponding data values in the fields into a row format.

     INPUTS:
      in_table (Table View):
          The input feature class or table for which the fields containing data values
          will be transposed.
      in_field (Value Table):
          The fields or columns containing data values in the input table that need to be
          transposed.Depending on your needs, you can select multiple fields that need to
          be
          transposed. By default, the value is the same as the field name. However, you
          can choose to specify your own value. For example, if the field names of the
          fields you want to transpose are Pop1991, Pop1992, and so on, by default, the
          values for these field will be the same ( Pop1991, Pop1992, and so forth).
          However, you can choose to specify your own values such as 1991 and 1992.
      in_transposed_field_name (String):
          The name of the field that will be created to store field name values of the
          fields that are selected to be transposed. Any valid field name can be used.
      in_value_field_name (String):
          The name of the value field that will be created to store the values from the
          input table. Any valid field name can be set, as long as it does not conflict
          with existing field names from the input table or feature class.
      attribute_fields {Field}:
          Attribute fields from the input table to be included in the output table. If you
          want to output a feature class, choose the Shape field.

     OUTPUTS:
      out_table (Table):
          The output feature class or table. The output feature class or table will
          contain the transposed field, a value field, and any number of attribute fields
          specified that need to be inherited from the input table.What is specified for
          out_table will be a table, unless the in_table value is a
          feature class and the Shape field is selected in the attribute_fields parameter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TransposeFields_management(*gp_fixargs((in_table, in_field, out_table, in_transposed_field_name, in_value_field_name, attribute_fields), True)))
        return retval
    except Exception, e:
        raise e


# File Geodatabase toolset
@gptooldoc('Compact_management', None)
def Compact(in_workspace=None):
    """Compact_management(in_workspace)

        Compacts a personal or file geodatabase. Compacting rearranges how the
        geodatabase is stored on disk, often reducing its size and improving
        performance.

     INPUTS:
      in_workspace (Workspace):
          The personal or file geodatabase to be compacted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Compact_management(*gp_fixargs((in_workspace,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CompressFileGeodatabaseData_management', None)
def CompressFileGeodatabaseData(in_data=None, lossless=None):
    """CompressFileGeodatabaseData_management(in_data, lossless)

        Compresses all the contents in a geodatabase, all the contents in a feature
        dataset, or an individual stand-alone feature class or table.

     INPUTS:
      in_data (Workspace / Feature Dataset / Table View / Raster Layer / Geometric Network):
          The geodatabase, feature dataset, feature class, or table to compress.
      lossless (Boolean):
          Indicates whether lossless compression will be used.

          * Lossless compression—Lossless compression will be used. This is the default.

          * Non-lossless compression—Lossless compression will not be used.
          This parameter is ignored for pre-10.0 file geodatabases."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CompressFileGeodatabaseData_management(*gp_fixargs((in_data, lossless), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateFgdbLicense_management', None)
def GenerateFgdbLicense(in_lic_def_file=None, out_lic_file=None, allow_export=None, exp_date=None):
    """GenerateFgdbLicense_management(in_lic_def_file, out_lic_file, {allow_export}, {exp_date})

        Generates a license file (.sdlic) for displaying the contents in a licensed file
        geodatabase created by the Generate Licensed File Geodatabase tool. The license
        file must be installed using ArcGIS Administrator.Licensing is not supported for
        geodatabases created earlier than version 10.1.

     INPUTS:
      in_lic_def_file (File):
          The license definition file (.licdef) created by the Generate Licensed File
          Geodatabase tool.
      allow_export {String}:
          Indicates whether the export of vector data is allowed.

          *  DENY_EXPORT—Vector data cannot be exported with the data license file
          (.sdlic) installed. This is the default.

          *  ALLOW_EXPORT— Vector data can be exported with the data license file (.sdlic)
          installed.
      exp_date {Date}:
          The expiration date of the data license file,  after which the file
          geodatabase’s contents can no longer be displayed. The default value is empty
          (blank), which means the data license file will never expire.

     OUTPUTS:
      out_lic_file (File):
          The license file (.sdlic) for distribution."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateFgdbLicense_management(*gp_fixargs((in_lic_def_file, out_lic_file, allow_export, exp_date), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateLicensedFgdb_management', None)
def GenerateLicensedFgdb(in_fgdb=None, out_fgdb=None, out_lic_def=None):
    """GenerateLicensedFgdb_management(in_fgdb, out_fgdb, out_lic_def)

        Generates a license definition file (.licdef) that defines and restricts the
        display of contents in a file geodatabase. The contents of the licensed file
        geodatabase can be viewed by creating a license file (*.sdlic) and installing it
        with ArcGIS Administrator. The license file is created using the Generate File
        Geodatabase License tool.Licensing is not supported for geodatabases created
        earlier than version 10.1.

     INPUTS:
      in_fgdb (Workspace):
          The unlicensed file geodatabase to make licensed.

     OUTPUTS:
      out_fgdb (Workspace):
          The name of and location to create the licensed file geodatabase.
      out_lic_def (File):
          The license definition file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateLicensedFgdb_management(*gp_fixargs((in_fgdb, out_fgdb, out_lic_def), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RecoverFileGDB_management', None)
def RecoverFileGDB(input_file_gdb=None, output_location=None, out_name=None):
    """RecoverFileGDB_management(input_file_gdb, output_location, out_name)

        Recovers data from a file geodatabase that has become corrupt.

     INPUTS:
      input_file_gdb (Workspace):
          Input corrupt file geodatabase.
      output_location (Folder):
          Output folder location for the recovered file geodatabase.
      out_name (String):
          Name for the output file geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RecoverFileGDB_management(*gp_fixargs((input_file_gdb, output_location, out_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UncompressFileGeodatabaseData_management', None)
def UncompressFileGeodatabaseData(in_data=None, config_keyword=None):
    """UncompressFileGeodatabaseData_management(in_data, {config_keyword})

        Uncompresses all the contents in a geodatabase, all the contents in a feature
        dataset, or an individual stand-alone feature class or table.

     INPUTS:
      in_data (Workspace / Feature Dataset / Table View / Raster Layer / Geometric Network):
          The geodatabase, feature dataset, feature class, or table to uncompress.
      config_keyword {String}:
          The configuration keyword defining how the data will store once uncompressed"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UncompressFileGeodatabaseData_management(*gp_fixargs((in_data, config_keyword), True)))
        return retval
    except Exception, e:
        raise e


# General toolset
@gptooldoc('AnalyzeToolsForPro_management', None)
def AnalyzeToolsForPro(input=None, report=None):
    """AnalyzeToolsForPro_management(input, {report})

        Analyzes Python scripts and custom geoprocessing tools and toolboxes for
        functionality that is not supported in ArcGIS Pro.There are differences between
        ArcGIS Pro and ArcGIS 10.x that may mean changes
        to some custom tools and scripts so they run successfully in ArcGIS Pro. These
        changes include geoprocessing tools and environments that are not supported in
        ArcGIS Pro, the replacement of the arcpy.mapping module with the arcpy.mp
        module, unsupported data formats (such as a personal geodatabase), and an
        upgrade to Python 3.4 from Python 2.7.

     INPUTS:
      input (File / String):
          The input can be a geoprocessing toolbox, Python file, or a tool name.If a tool
          name is specified, the tool will need to be loaded first using the
          arcpy.ImportToolbox function to be recognized. Tool names should include the
          toolbox alias.

     OUTPUTS:
      report {File}:
          An output text file that includes all issues."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AnalyzeToolsForPro_management(*gp_fixargs((input, report), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Append_management', None)
def Append(inputs=None, target=None, schema_type=None, field_mapping=None, subtype=None):
    """Append_management(inputs;inputs..., target, {schema_type}, {field_mapping}, {subtype})

        Appends multiple input datasets into an existing target dataset. Input datasets
        can be point, line, or polygon feature classes, tables, rasters, raster
        catalogs, annotation feature classes, or dimensions feature classes.To combine
        input datasets into a new output dataset, use the Merge tool.

     INPUTS:
      inputs (Table View / Raster Layer):
          The input datasets whose data will be appended into the target dataset. Input
          datasets can be point, line, or polygon feature classes, tables, rasters, raster
          catalogs, annotation feature classes, or dimensions feature classes. Each input
          dataset must match the data type of the target dataset.
      target (Table View / Raster Layer):
          The existing dataset that the input datasets' data will be appended into. Each
          input dataset must match the data type of the target dataset.
      schema_type {String}:
          Specifies if the schema (field definitions) of the input datasets must match the
          schema of the target dataset in order for data to be appended.

          * TEST—Input dataset schema (field definitions) must match the schema of the
          target dataset. An error will be returned if the schemas do not match.

          * NO_TEST—Input dataset schema (field definitions) do not have to match that of
          the target dataset. Any fields from the input datasets that do not match the
          fields of the target dataset will not be mapped to the target dataset unless the
          mapping is explicitly set in the Field Map control.
      field_mapping {Field Mappings}:
          Controls how the attribute information in input datasets' fields is transferred
          to the target dataset. This parameter can only be used if the Schema Type
          NO_TEST is specified.Because the input datasets' data is appended into an
          existing target dataset
          that has a predefined schema (field definitions), fields cannot be added or
          removed from the target dataset.Merge rules allow you to specify how values from
          two or more input fields are
          merged or combined into a single output value. There are several merge rules
          that determine how the output field is populated with values.

          * First—Use the input fields' first value.

          * Last—Use the input fields' last value.

          * Join—Concatenate (join) the input fields' values.

          * Sum—Calculate the total of the input fields' values.

          * Mean—Calculate the mean (average) of the input fields' values.

          * Median—Calculate the median (middle) of the input fields' values.

          * Mode—Use the value with the highest frequency.

          * Min—Use the minimum value of all input fields' values.

          * Max—Use the maximum value of all input fields' values.

          * Standard deviation—Use the standard deviation classification method on all
          input fields' values.

          * Count—Find the number of records included in the calculation.
      subtype {String}:
          A subtype description to assign that subtype to all new data that is appended to
          the target dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Append_management(*gp_fixargs((inputs, target, schema_type, field_mapping, subtype), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateValue_management', None)
def CalculateValue(expression=None, code_block=None, data_type=None):
    """CalculateValue_management(expression, {code_block}, {data_type})

        Calculate Value tool returns a value based on a specified Python expression.

     INPUTS:
      expression (SQL Expression):
          The Python expression to be evaluated.
      code_block {String}:
          Additional Python code. Code in the code block can be referenced in the
          Expression parameter.
      data_type {String}:
          The data type of the output returned from the Python expression. This parameter
          should be used in ModelBuilder to help chain Calculate Value with other tools."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateValue_management(*gp_fixargs((expression, code_block, data_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Copy_management', None)
def Copy(in_data=None, out_data=None, data_type=None):
    """Copy_management(in_data, out_data, {data_type})

        Copies input data on disk and pastes the output to the same or another location.
        The data type of the input and output data element is identical.

     INPUTS:
      in_data (Data Element):
          The data on disk to be copied to the same or another location.
      data_type {String}:
          The type of the data on disk to be copied. The only time you need to provide a
          value is when a geodatabase contains a feature dataset and a feature class with
          the same name. In this case, you need to select the data type, FeatureDataset or
          FeatureClass, of the item you want to copy.

     OUTPUTS:
      out_data (Data Element):
          The location and name of the output data. The file name extension of the output
          data must match the extension of the input data. For example, if you are copying
          a file geodatabase, your output data element must have .gdb as a suffix."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Copy_management(*gp_fixargs((in_data, out_data, data_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateDatabaseView_management', None)
def CreateDatabaseView(input_database=None, view_name=None, view_definition=None):
    """CreateDatabaseView_management(input_database, view_name, view_definition)

        Creates a view in a database based on an SQL expression.

     INPUTS:
      input_database (Workspace):
          The database that contains the tables or feature classes used to construct the
          view. This database is also where the view will be created.
      view_name (String):
          The name of the view that will be created in the database.
      view_definition (String):
          An SQL statement used to construct the view."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateDatabaseView_management(*gp_fixargs((input_database, view_name, view_definition), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Delete_management', None)
def Delete(in_data=None, data_type=None):
    """Delete_management(in_data, {data_type})

        Permanently deletes data from disk. All types of geographic data supported by
        ArcGIS, as well as toolboxes and workspaces (folders, geodatabases), can be
        deleted. If the specified item is a workspace, all contained items are also
        deleted.

     INPUTS:
      in_data (Data Element / Layer / Table View / Graph):
          The input data to be deleted.
      data_type {String}:
          Data type of the Input Data Element. Data type is displayed for informative
          purposes and cannot be changed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Delete_management(*gp_fixargs((in_data, data_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteIdentical_management', None)
def DeleteIdentical(in_dataset=None, fields=None, xy_tolerance=None, z_tolerance=None):
    """DeleteIdentical_management(in_dataset, fields;fields..., {xy_tolerance}, {z_tolerance})

        Deletes records in a feature class or table which have identical values in a
        list of fields. If the field Shape is selected, feature geometries are
        compared.The Find Identical tool can be used to report which records are
        considered
        identical without deleting the identical records.

     INPUTS:
      in_dataset (Table View):
          The table or feature class that will have its identical records deleted.
      fields (Field):
          The field or fields whose values will be compared to find identical records.
      xy_tolerance {Linear unit}:
          The xy tolerance that will be applied to each vertex when evaluating if there is
          an identical vertex in another feature.
      z_tolerance {Double}:
          The z tolerance that will be applied to each vertex when evaluating if there is
          an identical vertex in another feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteIdentical_management(*gp_fixargs((in_dataset, fields, xy_tolerance, z_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FindIdentical_management', None)
def FindIdentical(in_dataset=None, out_dataset=None, fields=None, xy_tolerance=None, z_tolerance=None, output_record_option=None):
    """FindIdentical_management(in_dataset, out_dataset, fields;fields..., {xy_tolerance}, {z_tolerance}, {output_record_option})

        Reports any records in a feature class or table that have identical values in a
        list of fields, and generates a table listing these identical records. If the
        field Shape is selected, feature geometries are compared.The Delete Identical
        tool can be used to find and delete identical records.

     INPUTS:
      in_dataset (Table View):
          The table or feature class for which identical records will be found.
      fields (Field):
          The field or fields whose values will be compared to find identical records.
      xy_tolerance {Linear unit}:
          The xy tolerance that will be applied to each vertex when evaluating if there is
          an identical vertex in another feature. This parameter is enabled only when
          Shape is selected as one of the fields.
      z_tolerance {Double}:
          The Z tolerance that will be applied to each vertex when evaluating if there is
          an identical vertex in another feature. This parameter is enabled only when
          Shape is selected as one of the fields.
      output_record_option {Boolean}:
          Choose if you want only duplicated records in the output table.

          * ALL—All input records will have corresponding records in the output table.
          This is the default.

          * ONLY_DUPLICATES—Only duplicate records will have corresponding records in the
          output table. The output will be empty if no duplicate is found.

     OUTPUTS:
      out_dataset (Table):
          The output table reporting identical records. The FEAT_SEQ field in the output
          table will have the same value for identical records."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FindIdentical_management(*gp_fixargs((in_dataset, out_dataset, fields, xy_tolerance, z_tolerance, output_record_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Merge_management', None)
def Merge(inputs=None, output=None, field_mappings=None):
    """Merge_management(inputs;inputs..., output, {field_mappings})

        Combines multiple input datasets of the same data type into a single, new output
        dataset. This tool can combine point, line, or polygon feature classes or
        tables.Use the Append tool to combine input datasets with an existing dataset.

     INPUTS:
      inputs (Table View):
          The input datasets that will be merged together into a new output dataset. Input
          datasets can be point, line, or polygon feature classes or tables. The input
          datasets must all be of the same type.
      field_mappings {Field Mappings}:
          Controls how the attribute fields from the input datasets are mapped and
          transferred to the output dataset.You can add, rename, or delete output fields
          as well as set properties, such as
          data type and merge rule.Merge rules allow you to specify how values from two or
          more input fields are
          merged or combined into a single output value. There are several merge rules
          that determine how the output field is populated with values.

          * First—Use the input fields' first value.

          * Last—Use the input fields' last value.

          * Join—Concatenate (join) the input fields' values.

          * Sum—Calculate the total of the input fields' values.

          * Mean—Calculate the mean (average) of the input fields' values.

          * Median—Calculate the median (middle) of the input fields' values.

          * Mode—Use the value with the highest frequency.

          * Min—Use the minimum value of all input fields' values.

          * Max—Use the maximum value of all input fields' values.

          * Standard deviation—Use the standard deviation classification method on all
          input fields' values.

          * Count—Find the number of records included in the calculation.
          You can use the ArcPy FieldMappings class to define this parameter.

     OUTPUTS:
      output (Feature Class / Table):
          The output dataset that will contain all combined input datasets."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Merge_management(*gp_fixargs((inputs, output, field_mappings), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MergeBranch_management', None)
def MergeBranch(in_values=None):
    """MergeBranch_management({in_values;in_values...})

        The Merge Branch tool merges two or more logical branches into a single
        output.Branching in a model is accomplished by creating a script tool that
        implements
        the necessary if-then-else logic. It is often the case when branching that you
        need to merge two branches into a single process. What this means is that if you
        test an input against a condition (examples: whether the data exists on the
        disk, whether the cell size is greater than 30 meters, whether the field value
        is 1), it will create two outputs: True, if the condition is true, and False, if
        the condition is false. If the condition is True, you want to run some processes
        and if the condition is False, you want different processes to run, as
        illustrated below.  At any point, only one of the branches will run depending on
        the condition and the input. The Merge Branch tool is used in such cases where
        it is not possible to say which branch will run and produce results. The output
        of both branches becomes the input for the Merge Branch tool. The tool looks at
        the inputs and passes the last output of a branch that has-been-run to the next
        tool. The Merge Branch tool allows any number of inputs and uses the multivalue
        parameter control.

     INPUTS:
      in_values {Any value}:
          List of values from different branches. The first ready-to-run state value in
          the list will be the output of the tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MergeBranch_management(*gp_fixargs((in_values,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Rename_management', None)
def Rename(in_data=None, out_data=None, data_type=None):
    """Rename_management(in_data, out_data, {data_type})

        Changes the name of a dataset. This includes a wide variety of data types, among
        them feature dataset, raster, table, and shapefile.

     INPUTS:
      in_data (Data Element):
          The input data to be renamed.
      data_type {String}:
          The type of the data to be renamed. The only time you need to provide a value is
          when a geodatabase contains a feature dataset and a feature class with the same
          name. In this case, you need to select the data type (feature dataset or feature
          class) of the item you want to rename.

     OUTPUTS:
      out_data (Data Element):
          The name for the output data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Rename_management(*gp_fixargs((in_data, out_data, data_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SelectData_management', None)
def SelectData(in_dataelement=None, out_dataelement=None):
    """SelectData_management(in_dataelement, {out_dataelement})

        The Select Data tool selects data in a parent data element such as a folder,
        geodatabase, feature dataset, or coverage.The tool allows access to the data
        stored inside a parent container, such as
        feature classes or tables inside a geodatabase.

     INPUTS:
      in_dataelement (Data Element / Composite Layer):
          The input data element can be a folder, geodatabase, feature dataset, or
          coverage.
      out_dataelement {String}:
          The child data element is contained by the input data element. Once the input
          data element is specified, the child data element control contains a drop-down
          list of the data elements contained in the input data element. For example, if
          the input is a feature dataset, all the feature classes within the feature
          dataset are included in the drop-down list. A single element is selected from
          this list."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SelectData_management(*gp_fixargs((in_dataelement, out_dataelement), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Sort_management', None)
def Sort(in_dataset=None, out_dataset=None, sort_field=None, spatial_sort_method=None):
    """Sort_management(in_dataset, out_dataset, sort_field;sort_field..., {spatial_sort_method})

        Reorders, in ascending or descending order, records in a feature class or table
        based on one or multiple fields. The reordered result is written to a new
        dataset.

     INPUTS:
      in_dataset (Table View):
          The input dataset whose records will be reordered based on the field values in
          the sort field(s).
      sort_field (Value Table):
          Specifies the field(s) whose values will be used to reorder the input records,
          and the direction the records will be sorted.

          * ASCENDING—Records are sorted from low value to high value.

          * DESCENDING—Records are sorted from high value to low value.
      spatial_sort_method {String}:
          Specifies how features are spatially sorted. Sort method is only enabled when
          the Shape field is selected as one of the sort fields.

          * UR—Sorting starts at upper right corner. This is the default.

          * UL—Sorting starts at upper left corner.

          * LR—Sorting starts at lower right corner.

          * LL—Sorting starts at lower left corner.

          * PEANO—Sorting uses a space filling curve algorithm, also known as a Peano
          curve.

     OUTPUTS:
      out_dataset (Feature Class / Table):
          The output feature class or table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Sort_management(*gp_fixargs((in_dataset, out_dataset, sort_field, spatial_sort_method), True)))
        return retval
    except Exception, e:
        raise e


# Generalization toolset
@gptooldoc('Dissolve_management', None)
def Dissolve(in_features=None, out_feature_class=None, dissolve_field=None, statistics_fields=None, multi_part=None, unsplit_lines=None):
    """Dissolve_management(in_features, out_feature_class, {dissolve_field;dissolve_field...}, {statistics_fields;statistics_fields...}, {multi_part}, {unsplit_lines})

        Aggregates features based on specified attributes.

     INPUTS:
      in_features (Feature Layer):
          The features to be aggregated.
      dissolve_field {Field}:
          The field or fields on which to aggregate features.The Add Field button, which
          is used only in ModelBuilder, allows you to add
          expected fields so you can complete the dialog box and continue to build your
          model.
      statistics_fields {Value Table}:
          The fields and statistics with which to summarize attributes. Text attribute
          fields may be summarized using the statistics FIRST or LAST. Numeric attribute
          fields may be summarized using any statistic. Nulls are excluded from all
          statistical calculations.

          * FIRST—Finds the first record in the Input Features and uses its specified
          field value.

          * LAST—Finds the last record in the Input Features and uses its specified field
          value.

          * SUM—Adds the total value for the specified field.

          * MEAN—Calculates the average for the specified field.

          * MIN—Finds the smallest value for all records of the specified field.

          * MAX—Finds the largest value for all records of the specified field.

          * RANGE—Finds the range of values (MAX–MIN) for the specified field.

          * STD—Finds the standard deviation on values in the specified field.

          * COUNT—Finds the number of values included in statistical calculations. This
          counts each value except null values. To determine the number of null values in
          a field, use the COUNT statistic on the field in question, and a COUNT statistic
          on a different field which does not contain nulls (for example, the OID if
          present), then subtract the two values.
      multi_part {Boolean}:
          Specifies whether multipart features are allowed in the output feature class.

          * MULTI_PART—Specifies multipart features are allowed. This is the default.

          * SINGLE_PART—Specifies multipart features are not allowed. Instead of creating
          multipart features, individual features will be created for each part.
      unsplit_lines {Boolean}:
          Controls how line features are dissolved.

          * DISSOLVE_LINES—Lines are dissolved into a single feature. This is the default.

          * UNSPLIT_LINES—Lines are only dissolved when two lines have an end vertex in
          common.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created that will contain the aggregated features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Dissolve_management(*gp_fixargs((in_features, out_feature_class, dissolve_field, statistics_fields, multi_part, unsplit_lines), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Eliminate_management', None)
def Eliminate(in_features=None, out_feature_class=None, selection=None, ex_where_clause=None, ex_features=None):
    """Eliminate_management(in_features, out_feature_class, {selection}, {ex_where_clause}, {ex_features})

        Eliminates polygons by merging them with neighboring polygons that have the
        largest area or the longest shared border. Eliminate is often used to remove
        small sliver polygons that are the result of overlay operations, such as
        Intersect or Union.

     INPUTS:
      in_features (Feature Layer):
          The layer whose polygons will be merged into neighboring polygons.
      selection {Boolean}:
          These options specify which method will be used for eliminating features.

          * LENGTH—Merges a selected polygon with a neighboring unselected polygon by
          dropping the shared border. The neighboring polygon is the one with the longest
          shared border. This is the default.

          * AREA—Merges a selected polygon with a neighboring unselected polygon by
          dropping the shared border. The neighboring polygon is the one with the largest
          area.
      ex_where_clause {SQL Expression}:
          An SQL expression used to identify features that will not be altered. For more
          information on SQL syntax see the help topic SQL reference for query expressions
          used in ArcGIS.
      ex_features {Feature Layer}:
          An input polyline or polygon feature class or layer that defines polygon
          boundaries, or portions thereof, that should not be eliminated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Eliminate_management(*gp_fixargs((in_features, out_feature_class, selection, ex_where_clause, ex_features), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EliminatePolygonPart_management', None)
def EliminatePolygonPart(in_features=None, out_feature_class=None, condition=None, part_area=None, part_area_percent=None, part_option=None):
    """EliminatePolygonPart_management(in_features, out_feature_class, {condition}, {part_area}, {part_area_percent}, {part_option})

        Creates a new output feature class containing the features from the input
        polygons with some parts or holes of a specified size deleted.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer whose features will be copied to the output
          feature class, with some parts or holes eliminated.
      condition {String}:
          Specify how the parts to be eliminated will be determined.

          * AREA—Parts with an area less than that specified will be eliminated.

          * PERCENT—Parts with a percent of the total outer area less than that specified
          will be eliminated.

          * AREA_AND_PERCENT—Parts with an area and percent less than that specified will
          be eliminated. Only if a polygon part meets both the area and percent criteria
          will it be deleted.

          * AREA_OR_PERCENT—Parts with an area or percent less than that specified will be
          eliminated. If a polygon part meets either the area or percent criteria, it will
          be deleted.
      part_area {Areal unit}:
          Eliminate parts smaller than this area.
      part_area_percent {Double}:
          Eliminate parts smaller than this percentage of a feature's total outer area.
      part_option {Boolean}:
          Determines what parts can be eliminated.

          * CONTAINED_ONLY—Only parts totally contained by other parts can be eliminated.
          This is the default.

          * ANY—Any parts can be eliminated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output polygon feature class containing the remaining parts."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EliminatePolygonPart_management(*gp_fixargs((in_features, out_feature_class, condition, part_area, part_area_percent, part_option), True)))
        return retval
    except Exception, e:
        raise e


# Geodatabase Administration toolset
@gptooldoc('AnalyzeDatasets_management', None)
def AnalyzeDatasets(input_database=None, include_system=None, in_datasets=None, analyze_base=None, analyze_delta=None, analyze_archive=None):
    """AnalyzeDatasets_management(input_database, include_system, {in_datasets;in_datasets...}, {analyze_base}, {analyze_delta}, {analyze_archive})

        Updates database statistics of base tables, delta tables, and archive tables,
        along with the statistics on those tables' indexes. This tool is used in
        enterprise geodatabases to help get optimal performance from the RDBMS's query
        optimizer. Stale statistics can lead to poor geodatabase performance.

     INPUTS:
      input_database (Workspace):
          The enterprise database that contains the data to be analyzed.
      include_system (Boolean):
          Indicates whether statistics will be gathered on the states and state lineages
          tables.You must be the geodatabase administrator for this option to be
          activated.This
          option only applies to geodatabases. If the input workspace is a database,
          this option will be ignored.

          * NO_SYSTEM—Statistics will not be gathered on the states and state lineages
          tables. This is the default.

          * SYSTEM—Statistics will be gathered on the states and state lineages tables.
      in_datasets {String}:
          Names of the datasets that will be analyzed. An individual dataset or a Python
          list of datasets is allowed. Dataset names use paths relative to the input
          workspace; full paths are not accepted as input.Note that the connected user
          must be the data owner for the datasets provided.
      analyze_base {Boolean}:
          Indicates whether the selected dataset base tables will be analyzed.This option
          only applies to geodatabases. If the input workspace is a database,
          this option will be ignored.

          * ANALYZE_BASE— Statistics will be gathered on the base tables for the selected
          datasets. This is the default.

          * NO_ANALYZE_BASE— Statistics will not be gathered for the base tables for the
          selected datasets.
      analyze_delta {Boolean}:
          Indicates whether the selected dataset delta tables will be analyzed.This
          option only applies to geodatabases. If the input workspace is a database,
          this option will be ignored.

          * ANALYZE_DELTA— Statistics will be gathered on the delta tables for the
          selected datasets. This is the default.

          * NO_ANALYZE_DELTA— Statistics will not be gathered for the delta tables for the
          selected datasets.
      analyze_archive {Boolean}:
          Indicates whether the selected dataset archive tables will be analyzed.This
          option only applies to geodatabases. If the input workspace is a database,
          this option will be ignored.

          * ANALYZE_ARCHIVE— Statistics will be gathered on the archive tables for the
          selected datasets. This is the default.

          * NO_ANALYZE_ARCHIVE— Statistics will not be gathered for the archive tables for
          the selected datasets."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AnalyzeDatasets_management(*gp_fixargs((input_database, include_system, in_datasets, analyze_base, analyze_delta, analyze_archive), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ChangePrivileges_management', None)
def ChangePrivileges(in_dataset=None, user=None, View=None, Edit=None):
    """ChangePrivileges_management(in_dataset;in_dataset..., user, {View}, {Edit})

        Establishes or changes user access privileges to the input ArcSDE datasets,
        stand-alone feature classes, or tables.

     INPUTS:
      in_dataset (Layer / Table View / Dataset / Address Locator):
          The datasets, feature classes, or tables whose access privileges will be
          changed.
      user (String):
          The database user name whose privileges are being modified.
      View {String}:
          Establishes the user's View privileges.

          * AS_IS —No change to the user's existing view privilege. If the user has view
          privileges, they will continue to have view privileges. If the user doesn't have
          view privileges, they will continue to not have view privileges.

          * GRANT—Allows user to view datasets.

          * REVOKE—Removes all user privileges to view datasets.
      Edit {String}:
          Establishes the user's Edit privileges.

          * AS_IS — No change to the user's existing edit privilege. If the user has edit
          privileges, they will continue to have edit privileges. If the user doesn't have
          edit privileges, they will continue to not have edit privileges. This is the
          default.

          * GRANT—Allows the user to edit the input datasets.

          * REVOKE—Removes the user's edit privileges. The user may still view the Input
          dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ChangePrivileges_management(*gp_fixargs((in_dataset, user, View, Edit), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Compress_management', None)
def Compress(in_workspace=None):
    """Compress_management(in_workspace)

        Compresses an enterprise geodatabase by removing states not referenced by a
        version and redundant rows.

     INPUTS:
      in_workspace (Workspace):
          Specify the database connection file that connects to the enterprise geodatabase
          to be compressed. Connect as the geodatabase administrator."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Compress_management(*gp_fixargs((in_workspace,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConfigureGeodatabaseLogFileTables_management', None)
def ConfigureGeodatabaseLogFileTables(input_database=None, log_file_type=None, log_file_pool_size=None, use_tempdb=None):
    """ConfigureGeodatabaseLogFileTables_management(input_database, log_file_type, {log_file_pool_size}, {use_tempdb})

        The Configure Geodatabase Log File Tables tool allows you to alter the type of
        log file tables used by an enterprise geodatabase to maintain lists of selected
        records in ArcGIS.

     INPUTS:
      input_database (Workspace):
          Provide a database connection (.sde file) to the enterprise geodatabase for
          which you want to change log file table configuration. The connection must be
          made as the geodatabase administrator.
      log_file_type (String):
          Specify the type of log file tables you want the geodatabase to use: either
          SESSION_LOG_FILE or SHARED_LOG_FILE.For information on log file table options,
          see the topic that applies to the
          database management system where your geodatabase is stored:
      log_file_pool_size {Long}:
          If you want the geodatabase to use a pool of session-based log file tables
          owned by the geodatabase administrator, specify the number of tables you want
          included in the pool.
      use_tempdb {Boolean}:
          Specify TRUE if your geodatabase is stored in SQL Server, and you want to use
          session-based log files created in SQL Server's TempDB. This is the default and
          recommended configuration for geodatabases in SQL Server. Specify FALSE if you
          do not want the log file tables created in TempDB."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConfigureGeodatabaseLogFileTables_management(*gp_fixargs((input_database, log_file_type, log_file_pool_size, use_tempdb), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateDatabaseUser_management', None)
def CreateDatabaseUser(input_database=None, user_authentication_type=None, user_name=None, user_password=None, role=None, tablespace_name=None):
    """CreateDatabaseUser_management(input_database, {user_authentication_type}, user_name, {user_password}, {role}, {tablespace_name})

        The Create Database User tool creates a database user with privileges
        sufficient to create data in the database.

     INPUTS:
      input_database (Workspace):
          Specify the connection file to a database or enterprise geodatabase in Oracle,
          PostgreSQL, or SQL Server. Be sure the connection file connects directly to the
          database (no ArcSDE service), and that the connection is made as a database
          administrator user. When connecting to Oracle, you must connect as the sys user.
      user_authentication_type {Boolean}:
          Use this only if an operating system login exists for which you want to create a
          database user. Only enabled for SQL Server and Oracle databases.

          * DATABASE_USER—Create a database-authenticated user. This is the default. If
          your database management system is not configured to allow database
          authentication, do not use this option.

          * OPERATING_SYSTEM_USER—Create an operating system-authenticated user. The
          corresponding login must already exist. If your database management system is
          not configured to allow operating system authentication, do not use this option.
      user_name (String):
          Type a name for the new database user.If you chose to create a database user
          for an operating system login, the user
          name must match the login name.
      user_password {Encrypted String}:
          Type a password for the new user. The password policy of the underlying
          database will be enforced.If you chose to create a database user for an
          operating system login, no input
          is required.
      role {String}:
          If you want to add the new user to an existing database role, type the name of
          the role.
      tablespace_name {String}:
          When creating a user in an Oracle database, type the name of the tablespace to
          be used as the default tablespace for the user. You can specify a preconfigured
          tablespace, or, if the tablespace does not already exist, it will be created in
          the Oracle default storage location with its size set to 400 MB. If no
          tablespace is specified, the user's default tablespace will be set to the Oracle
          default tablespace."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateDatabaseUser_management(*gp_fixargs((input_database, user_authentication_type, user_name, user_password, role, tablespace_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateEnterpriseGeodatabase_management', None)
def CreateEnterpriseGeodatabase(database_platform=None, instance_name=None, database_name=None, account_authentication=None, database_admin=None, database_admin_password=None, sde_schema=None, gdb_admin_name=None, gdb_admin_password=None, tablespace_name=None, authorization_file=None):
    """CreateEnterpriseGeodatabase_management(database_platform, instance_name, {database_name}, {account_authentication}, {database_admin}, {database_admin_password}, {sde_schema}, {gdb_admin_name}, {gdb_admin_password}, {tablespace_name}, authorization_file)

        The Create Enterprise Geodatabase tool creates a database, storage locations,
        and a database user to be used as the geodatabase administrator and owner of the
        geodatabase depending on the database management system (DBMS) used. It grants
        the geodatabase administrator privileges required to create a geodatabase, and
        then creates a geodatabase in the database.

     INPUTS:
      database_platform (String):
          Specify the type of database management system to which you will connect to
          create a geodatabase.

          * Oracle—Indicates you are connecting to an Oracle instance

          * PostgreSQL—Indicates you are connecting to a PostgreSQL database cluster

          * SQL_Server—Indicates you are connecting to a SQL Server instance
      instance_name (String):
          For SQL Server, provide the SQL Server instance name. Note that case-sensitive
          or binary collation SQL Server instances are not supported.For Oracle, provide
          either the TNS name or Oracle Easy Connection string.For PostgreSQL, provide the
          name of the server where PostgreSQL is installed.
      database_name {String}:
          This parameter is valid only for PostgreSQL and SQL Server DBMS types. Either
          type the name of an existing, preconfigured database, or type a name for a
          database to be created.If you let the tool create the database in SQL Server,
          the file sizes will
          either be the same as you have defined for the SQL Server model database or 500
          MB for the MDF file and 125 MB for the LDF file, whichever is greater. Both the
          MDF and LDF files will be created in the default SQL Server location on the
          database server.If you let the tool create the database in PostgreSQL, the
          template1 database
          will be used as the template for your database. Be aware that the database name
          will be passed to the PostgreSQL database cluster in lower case.
      account_authentication {Boolean}:
          Specify what type of authorization to use for the database connection.

          * OPERATING_SYSTEM_AUTH—The login information you provided when you logged in to
          the computer from which you are running the tool will be used to authenticate
          your database connection. If your DBMS is not configured to allow operating
          system authentication, authentication will fail.

          * DATABASE_AUTH—You must provide a valid database user name and password for
          authentication in the database. This is the default authentication method. If
          your DBMS is not configured to allow database authentication, authentication
          will fail.
      database_admin {String}:
          If you use database authentication, you must specify a database administrator
          user. For Oracle, the database administrator is sys. For Postgres, it is the
          postgres superuser. For SQL Server, it is a member of the sysadmin fixed server
          role.
      database_admin_password {Encrypted String}:
          Type the password for the database administrator. If you use database
          authentication, you must specify the database administrator user password.
      sde_schema {Boolean}:
          This parameter is only relevant for SQL Server and indicates whether the
          geodatabase is to be created in the schema of a user named sde or in the dbo
          schema in the database. If creating a dbo-schema geodatabase, you must connect
          as a user who is dbo in the SQL Server instance.

          * SDE_SCHEMA—The geodatabase repository is owned by and stored in the schema of
          a user named sde. This is the default.

          * DBO_SCHEMA—The geodatabase repository is stored in the dbo schema in the
          database.
      gdb_admin_name {String}:
          If you are using PostgreSQL, this value must be sde. If the sde login role does
          not exist, this tool creates it and grants it superuser status. It also creates
          an sde schema in the database. If the sde login role exists, this tool will
          grant it superuser status if it does not already have it.If you are using
          Oracle, the default value is sde. However, if you are creating
          a user-schema geodatabase inside a master sde geodatabase, specify the name of
          the user who will own the geodatabase. If the user does not exist in the DBMS,
          the Create Enterprise Geodatabase tool creates the user and grants it the
          privileges required to create and upgrade a geodatabase and kill user
          connections to the DBMS. If the user already exists, the tool will grant the
          required privileges to the user. If you are using SQL Server and specified an
          sde-schema geodatabase, this value
          must be sde. The tool will create an sde login, database user, and schema and
          grant it privileges to create a geodatabase and kill connections to the SQL
          Server instance. If you specified a dbo schema, do not provide a value for this
          parameter.
      gdb_admin_password {Encrypted String}:
          Provide the password for the geodatabase administrator user. If the geodatabase
          administrator user already exists in the DBMS, the password you type must match
          the existing password. If the geodatabase administrator user does not already
          exist, type a valid database password for the new user. The password must meet
          the password policy enforced by your DBMS.The password is a geoprocessing-
          encrypted string.
      tablespace_name {String}:
          This parameter is only valid for Oracle and PostgreSQL DBMS types. For Oracle,
          do one of the following:

          * Provide the name of an existing tablespace to be used as the default
          tablespace for the geodatabase administrator user.

          * Type a valid name and a 400 MB tablespace will be created in the Oracle
          default storage location and set as the geodatabase administrator's default
          tablespace.

          * Leave the tablespace blank, and tablespace SDE_TBS (400 MB) will be created
          and set as the default tablespace for the geodatabase administrator.
          For PostgreSQL, you must either provide the name of an existing tablespace to be
          used as the default tablespace for the database or leave this parameter blank.
          This tool does not create a tablespace in PostgreSQL. If you do not provide a
          value for this parameter, the database is created in the pg_default tablespace
          in PostgreSQL.
      authorization_file (File):
          Provide the path and file name of the keycodes file that was created when you
          authorized ArcGIS for Server Enterprise. This file is in the \\Program
          Files\ESRI\License<release#>\sysgen folder on Windows and
          /arcgis/server/framework/runtime/.wine/drive_c/Program
          Files/ESRI/License<release#>/sysgen directory on Linux. If you have not already
          done so, authorize ArcGIS for Server to create this file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateEnterpriseGeodatabase_management(*gp_fixargs((database_platform, instance_name, database_name, account_authentication, database_admin, database_admin_password, sde_schema, gdb_admin_name, gdb_admin_password, tablespace_name, authorization_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRasterType_management', None)
def CreateRasterType(input_database=None):
    """CreateRasterType_management(input_database)

        The Create Raster Type tool installs the ST_Raster data type in a geodatabase
        stored in Oracle, Microsoft SQL Server, or PostgreSQL.

     INPUTS:
      input_database (Workspace):
          Specify the database connection (.sde) file for the geodatabase in which you
          want to install the ST_Raster data type. You must connect as the geodatabase
          administrator."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRasterType_management(*gp_fixargs((input_database,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRole_management', None)
def CreateRole(input_database=None, role=None, grant_revoke=None, user_name=None):
    """CreateRole_management(input_database, role, {grant_revoke}, {user_name})

        The Create Role tool creates a database role and lets you add users to or
        remove users from the role.

     INPUTS:
      input_database (Workspace):
          Specify the connection file to a database or enterprise geodatabase. You must
          use a direct connection (not an ArcSDE service), and connect as a database
          administrator user.
      role (String):
          Type the name of the database role you want to create. If the role already
          exists, type the name of the role for which you want to add users or remove
          users.
      grant_revoke {String}:
          Specify whether to grant the role to a user or list of users or remove a user or
          list of users from the role.

          * GRANT—Grants the role to the specified user or users, thereby making them a
          member of the role

          * REVOKE—Revokes the role from the specified user or users, thereby removing
          them from the role
      user_name {String}:
          Type the name of the user for which you want to change role membership. To
          specify multiple users, type the user names separated by commas (no spaces)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRole_management(*gp_fixargs((input_database, role, grant_revoke, user_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteSchemaGeodatabase_management', None)
def DeleteSchemaGeodatabase(input_database=None):
    """DeleteSchemaGeodatabase_management(input_database)

        The Delete Schema Geodatabase tool deletes a schema geodatabase from an Oracle
        database.

     INPUTS:
      input_database (Workspace):
          Specify the database connection (.sde) file for the schema geodatabase you want
          to delete. You must connect as the schema owner."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteSchemaGeodatabase_management(*gp_fixargs((input_database,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DiagnoseVersionMetadata_management', None)
def DiagnoseVersionMetadata(input_database=None, out_log=None):
    """DiagnoseVersionMetadata_management(input_database, out_log)

        The Diagnose Version Metadata tool identifies inconsistencies within the
        versioning system tables of a versioned geodatabase.

     INPUTS:
      input_database (Workspace):
          Provide a database connection (.sde file) to the enterprise, workgroup, or
          desktop geodatabase you suspect contains inconsistencies in the versioning
          system tables.The connection must be made as the geodatabase administrator.

     OUTPUTS:
      out_log (File):
          Specify a log file name and location where the tool will create the file.The
          log file is an ASCII file containing a list of the system tables in the
          specified version that contain orphaned records, as well as the database
          connection file used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DiagnoseVersionMetadata_management(*gp_fixargs((input_database, out_log), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DiagnoseVersionTables_management', None)
def DiagnoseVersionTables(input_database=None, out_log=None, target_version=None, input_tables=None):
    """DiagnoseVersionTables_management(input_database, out_log, {target_version}, {input_tables;input_tables...})

        The Diagnose Version Tables tool identifies inconsistencies in the delta (A and
        D) tables of a versioned geodatabase.

     INPUTS:
      input_database (Workspace):
          Provide a database connection (.sde file) to the enterprise, workgroup, or
          desktop geodatabase in which you suspect delta table inconsistencies exist. The
          connection must be made as the geodatabase administrator.
      target_version {String}:
          Specify which geodatabase version to check for inconsistencies in the delta
          tables. If no version is specified, all versions are processed.
      input_tables {String}:
          Specify a single table or provide a text file containing a list of versioned
          tables whose associated delta tables you want to check for inconsistencies. Use
          fully-qualified table names in the text file, and place one table name per line.
          If no file is specified, all tables in the geodatabase are processed.

     OUTPUTS:
      out_log (File):
          Specify where to create the log file and include a name for the log file. The
          log file is an ASCII file containing a list of the tables in the specified
          version that contain orphaned records, as well as information about what
          connection file, geodatabase version, and tables for which the tool was run."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DiagnoseVersionTables_management(*gp_fixargs((input_database, out_log, target_version, input_tables), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EnableEnterpriseGeodatabase_management', None)
def EnableEnterpriseGeodatabase(input_database=None, authorization_file=None):
    """EnableEnterpriseGeodatabase_management(input_database, authorization_file)

        The Enable Enterprise Geodatabase tool creates geodatabase system tables,
        stored procedures, functions, and types in an existing enterprise database,
        thereby enabling geodatabase functionality in the database.

     INPUTS:
      input_database (Workspace):
          Provide the path and connection file name for the database in which geodatabase
          functionality is to be enabled. The connection must be made as a user that
          qualifies as a geodatabase administrator.
      authorization_file (File):
          Provide the path and file name of the keycodes file that was created when you
          authorized ArcGIS for Server Enterprise. This file is in the \\Program
          Files\ESRI\License<release#>\sysgen folder on Windows and
          /arcgis/server/framework/runtime/.wine/drive_c/Program
          Files/ESRI/License<release#>/sysgen directory on Linux. If you have not already
          done so, authorize ArcGIS for Server to create this file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EnableEnterpriseGeodatabase_management(*gp_fixargs((input_database, authorization_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportGeodatabaseConfigurationKeywords_management', None)
def ExportGeodatabaseConfigurationKeywords(input_database=None, out_file=None):
    """ExportGeodatabaseConfigurationKeywords_management(input_database, out_file)

        The Export Geodatabase Configuration Keywords tool exports the configuration
        keywords, parameters, and values from the specified enterprise geodatabase. You
        can edit the file to change parameter values or add custom configuration
        keywords and use the Import Geodatabase Configuration Keywords tool to import
        the edited file to the geodatabase.

     INPUTS:
      input_database (Workspace):
          The connection file for the enterprise geodatabase from which configuration
          keywords, parameters, and values will be exported. You must connect as the
          geodatabase administrator.

     OUTPUTS:
      out_file (File):
          The full path to and name of the ASCII text file to be created. The file will
          contain all the configuration keywords, parameters, and values from the
          enterprise geodatabase's DBTUNE (or SDE_DBTUNE) table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportGeodatabaseConfigurationKeywords_management(*gp_fixargs((input_database, out_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportGeodatabaseConfigurationKeywords_management', None)
def ImportGeodatabaseConfigurationKeywords(input_database=None, in_file=None):
    """ImportGeodatabaseConfigurationKeywords_management(input_database, in_file)

        The Import Geodatabase Configuration Keywords tool allows you to define data
        storage parameters for an enterprise geodatabase by importing a file containing
        configuration keywords, parameters, and values.

     INPUTS:
      input_database (Workspace):
          The connection file for the enterprise geodatabase into which the configuration
          file will be imported. You must connect as the geodatabase administrator.
      in_file (File):
          The path to and name of the ASCII text file containing configuration keywords,
          parameters, and values to be imported."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportGeodatabaseConfigurationKeywords_management(*gp_fixargs((input_database, in_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MigrateStorage_management', None)
def MigrateStorage(in_datasets=None, config_keyword=None):
    """MigrateStorage_management(in_datasets;in_datasets..., config_keyword)

        This tool is designed to change the data types used to store rasters in an
        enterprise geodatabase in Oracle, PostgreSQL, and SQL Server; geometries in
        geodatabases in Oracle and SQL Server; and BLOB objects in attribute columns in
        geodatabases in Oracle. This is done through the migration of raster, spatial,
        or BLOB objects using configuration keywords specified in the DBTUNE table.After
        migrating the data type, you must disconnect from and reconnect to the
        geodatabase to reload the column names. If you do not, subsequent actions
        executed on the newly migrated datasets may fail.

     INPUTS:
      in_datasets (Table View / Raster Layer / Feature Dataset):
          Datasets to be migrated.
      config_keyword (String):
          DBTUNE configuration keyword containing the appropriate parameter values for the
          migration."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MigrateStorage_management(*gp_fixargs((in_datasets, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RebuildIndexes_management', None)
def RebuildIndexes(input_database=None, include_system=None, in_datasets=None, delta_only=None):
    """RebuildIndexes_management(input_database, include_system, {in_datasets;in_datasets...}, {delta_only})

        This tool is used in databases and enterprise, workgroup, and desktop
        geodatabases to rebuild existing attribute or spatial indexes. In enterprise,
        workgroup, and desktop geodatabases, indexes can also be rebuilt on states and
        state_lineage geodatabase system tables and the delta tables of versioned
        datasets. Out-of-date indexes can lead to poor query performance.

     INPUTS:
      input_database (Workspace):
          The connection (.sde file) to the database or geodatabase that contains the
          data for which you want to rebuild indexes.
      include_system (Boolean):
          Indicates whether indexes will be rebuilt on the states and state lineages
          tables.You must connect as the geodatabase administrator in the connection file
          you
          specified for the input_database for this option to be executed
          successfully.This option only applies to geodatabases. This option is ignored if
          you connect
          to a database.

          * NO_SYSTEM— Indexes will not be rebuilt on the states and state lineages table.
          This is the default.

          * SYSTEM— Indexes will be rebuilt on the states and state lineages tables.
      in_datasets {String}:
          Names of the datasets that will have their indexes rebuilt. Dataset names use
          paths relative to the input_database; full paths are not accepted as input.
      delta_only {Boolean}:
          Indicates how the indexes will be rebuilt on the selected datasets. This option
          has no effect if in_datasets is empty.This option only applies to geodatabases.
          If the input workspace is a database,
          this option will be ignored.

          * ALL—Indexes will be rebuilt on all indexes for the selected datasets. This
          includes spatial indexes as well as user-created attribute indexes and any
          geodatabase-maintained indexes for the dataset.

          * ONLY_DELTAS—Indexes will only be rebuilt for the delta tables of the selected
          datasets. This option can be used for cases where the business tables for the
          selected datasets are not updated often and there is a high volume of edits in
          the delta tables. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RebuildIndexes_management(*gp_fixargs((input_database, include_system, in_datasets, delta_only), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RegisterWithGeodatabase_management', None)
def RegisterWithGeodatabase(in_dataset=None):
    """RegisterWithGeodatabase_management(in_dataset)

        Registers feature classes, tables, and raster layers that were created outside
        of the geodatabase with the geodatabase in order for them to fully participate
        in geodatabase functionality.

     INPUTS:
      in_dataset (Table View / Raster Layer):
          Feature classes, tables, or raster feature classes created outside of the
          geodatabase are supported."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RegisterWithGeodatabase_management(*gp_fixargs((in_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RepairVersionMetadata_management', None)
def RepairVersionMetadata(input_database=None, out_log=None):
    """RepairVersionMetadata_management(input_database, out_log)

        The Repair Version Metadata tool repairs inconsistencies within the versioning
        system tables of a versioned geodatabase.

     INPUTS:
      input_database (Workspace):
          Provide a database connection (.sde file) to the enterprise, workgroup, or
          desktop geodatabase for which you want to repair inconsistencies in the
          versioning system tables. The connection must be made as the geodatabase
          administrator.

     OUTPUTS:
      out_log (File):
          The output log file. The log file is an ASCII file containing the results of
          the repair operation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RepairVersionMetadata_management(*gp_fixargs((input_database, out_log), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RepairVersionTables_management', None)
def RepairVersionTables(input_database=None, out_log=None, target_version=None, input_tables=None):
    """RepairVersionTables_management(input_database, out_log, {target_version}, {input_tables;input_tables...})

        The Repair Version Tables tool repairs inconsistencies in the delta (A and D)
        tables of a versioned geodatabase.

     INPUTS:
      input_database (Workspace):
          Provide a database connection (.sde file) to the enterprise, workgroup, or
          desktop geodatabase in which delta table inconsistencies exist. The connection
          must be made as the geodatabase administrator.
      target_version {String}:
          Specify which geodatabase version to repair. If no version is specified, all
          versions are processed.
      input_tables {String}:
          Specify a single table or provide a text file containing a list of versioned
          tables whose associated delta tables you want to repair. Use fully-qualified
          table names in the text file, and place one table name per line. If no table or
          file is specified, all tables are processed.

     OUTPUTS:
      out_log (File):
          Specify the location where the log file will be written and include the name to
          use for the log file. The log file is an ASCII file containing the results of
          the repair operation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RepairVersionTables_management(*gp_fixargs((input_database, out_log, target_version, input_tables), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpgradeDataset_management', None)
def UpgradeDataset(in_dataset=None):
    """UpgradeDataset_management(in_dataset)

        Upgrades the schema of a mosaic dataset, network dataset, or parcel fabric to
        the current ArcGIS release. Upgrading the dataset allows the dataset to make use
        of new functionality available in the current software release.

     INPUTS:
      in_dataset (Parcel Fabric Layer / Mosaic Layer / Network Dataset Layer):
          Dataset that will be upgraded to the current ArcGIS client release."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeDataset_management(*gp_fixargs((in_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpgradeGDB_management', None)
def UpgradeGDB(input_workspace=None, input_prerequisite_check=None, input_upgradegdb_check=None):
    """UpgradeGDB_management(input_workspace, input_prerequisite_check, input_upgradegdb_check)

        Upgrades a geodatabase to the latest ArcGIS release to take advantage of new
        functionality.You must have the current release of ArcGIS for Desktop or ArcGIS
        for Server
        installed on the computer from which you will run the upgrade. For enterprise
        geodatabases, you must connect directly to the geodatabase to upgrade; you
        cannot connect through an ArcSDE service.

     INPUTS:
      input_workspace (Workspace):
          Specify the geodatabase to upgrade. When upgrading a desktop, workgroup, or
          enterprise geodatabase, specify a database connection file (.sde) that connects
          to the geodatabase as the geodatabase administrator.
      input_prerequisite_check (Boolean):
          Specify whether the prerequisite check is run prior to upgrading the
          geodatabase.

          * NO_ PREREQUISITE_CHECK—Prerequisite check is not run.

          * PREREQUISITE_CHECK—Prerequisite check is run. This is the default.
      input_upgradegdb_check (Boolean):
          Specify whether to upgrade the geodatabase or not.

          * NO_UPGRADE—The upgrade is not run.

          * UPGRADE—The upgrade  is run. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeGDB_management(*gp_fixargs((input_workspace, input_prerequisite_check, input_upgradegdb_check), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpgradeSpatialReference_management', None)
def UpgradeSpatialReference(input_dataset=None, xy_resolution=None, z_resolution=None, m_resolution=None):
    """UpgradeSpatialReference_management(input_dataset, {xy_resolution}, {z_resolution}, {m_resolution})

        Upgrades a low precision dataset's spatial reference to high precision.Input to
        this tool is a stand-alone feature class, feature dataset, or raster
        catalog which has a low resolution spatial reference and is stored in a current
        version personal or ArcSDE geodatabase. The origin and precision of the high
        precision spatial reference grid will mesh with the existing low precision grid.
        For each point of the original low precision spatial reference grid there is a
        point in the new high precision spatial reference grid. Coordinate values will
        not be affected by the upgrade.

     INPUTS:
      input_dataset (Feature Class / Feature Dataset / Raster Catalog):
          The input dataset whose spatial reference precision will be upgraded. Valid
          input is a feature class, feature dataset, or raster catalog with a low
          resolution spatial reference, stored in a 9.2 or current version personal or
          ArcSDE geodatabase.
      xy_resolution {Double}:
          The value to which the dataset's XY Resolution will be changed as part of the
          upgrade. The maximum value is the same as the dataset's current XY Resolution.
      z_resolution {Double}:
          The value to which the dataset's Z Resolution will be changed as part of the
          upgrade. The maximum value is the same as the dataset's current Z Resolution. By
          default, the resolution will be improved by a factor of 4.
      m_resolution {Double}:
          The value to which the dataset's M Resolution will be changed as part of the
          upgrade. The maximum value is the same as the dataset's current M Resolution. By
          default, the resolution will be improved by a factor of 4."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpgradeSpatialReference_management(*gp_fixargs((input_dataset, xy_resolution, z_resolution, m_resolution), True)))
        return retval
    except Exception, e:
        raise e


# Geometric Network toolset
@gptooldoc('AddEdgeEdgeConnectivityRuleToGeometricNetwork_management', None)
def AddEdgeEdgeConnectivityRuleToGeometricNetwork(in_geometric_network=None, in_from_edge_feature_class=None, from_edge_subtype=None, in_to_edge_feature_class=None, to_edge_subtype=None, in_junction_subtypes=None, default_junction_subtype=None):
    """AddEdgeEdgeConnectivityRuleToGeometricNetwork_management(in_geometric_network, in_from_edge_feature_class, from_edge_subtype, in_to_edge_feature_class, to_edge_subtype, in_junction_subtypes;in_junction_subtypes..., default_junction_subtype)

        Adds an edge-edge connectivity rule to a geometric network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network to which the connectivity rule will be added.
      in_from_edge_feature_class (String):
          The name of the from edge feature class.
      from_edge_subtype (String):
          The subtype description for the from edge feature class. If subtypes do not
          exist on the feature class, use the feature class name.
      in_to_edge_feature_class (String):
          The name of the to edge feature class.
      to_edge_subtype (String):
          The subtype description for the to edge feature class. If subtypes do not exist
          on the feature class, use the feature class name.
      in_junction_subtypes (String):
          The junction feature classes and subtypes through which these edge feature
          classes or subtypes will be permitted to connect.
      default_junction_subtype (String):
          Junction Subtype that will serve as the default junction subtype for the edge-
          edge connectivity rule."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddEdgeEdgeConnectivityRuleToGeometricNetwork_management(*gp_fixargs((in_geometric_network, in_from_edge_feature_class, from_edge_subtype, in_to_edge_feature_class, to_edge_subtype, in_junction_subtypes, default_junction_subtype), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddEdgeJunctionConnectivityRuleToGeometricNetwork_management', None)
def AddEdgeJunctionConnectivityRuleToGeometricNetwork(in_geometric_network=None, in_edge_feature_class=None, edge_subtype=None, in_junction_feature_class=None, junction_subtype=None, default_junction=None, edge_min=None, edge_max=None, junction_min=None, junction_max=None):
    """AddEdgeJunctionConnectivityRuleToGeometricNetwork_management(in_geometric_network, in_edge_feature_class, edge_subtype, in_junction_feature_class, junction_subtype, {default_junction}, {edge_min}, {edge_max}, {junction_min}, {junction_max})

        Adds an edge-junction connectivity rule to a geometric network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network to which the connectivity rule will be added.
      in_edge_feature_class (String):
          The name of the edge feature class.
      edge_subtype (String):
          The subtype description for the edge feature class. If subtypes do not exist on
          the feature class, use the feature class name.
      in_junction_feature_class (String):
          The name of the junction feature class.
      junction_subtype (String):
          The subtype description for the junction feature class. If subtypes do not exist
          on the feature class, use the feature class name.
      default_junction {Boolean}:
          Indicates if the junction specified in this rule will be created automatically
          at a dangling endpoint of an edge in the feature class specified as part of the
          rule.

          * DEFAULT—Create a junction at a dangling endpoint of edges for this rule.

          * NO_ DEFAULT—Do not create a junction at a dangling endpoint of edges for this
          rule. This is the default.
      edge_min {Long}:
          The minimum number of edges that can connect to each junction. If nothing is
          specified, then it will be valid to have any number of edges connected to a
          single junction for the feature class or subtype pair.
      edge_max {Long}:
          The maximum number of edges that can connect to each junction. If nothing is
          specified, then it will be valid to have any number of edges connected to a
          single junction for the feature class or subtype pair.
      junction_min {Long}:
          The minimum number of junctions that can connect to each edge. If nothing is
          specified, then it will be valid to have any number of junctions connected to a
          single edge for the feature class or subtype pair.
      junction_max {Long}:
          The maximum number of junctions that can connect to each edge. If nothing is
          specified, then it will be valid to have any number of junctions connected to a
          single edge for the feature class or subtype pair."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddEdgeJunctionConnectivityRuleToGeometricNetwork_management(*gp_fixargs((in_geometric_network, in_edge_feature_class, edge_subtype, in_junction_feature_class, junction_subtype, default_junction, edge_min, edge_max, junction_min, junction_max), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateGeometricNetwork_management', None)
def CreateGeometricNetwork(in_feature_dataset=None, out_name=None, in_source_feature_classes=None, snap_tolerance=None, weights=None, weight_associations=None, z_snap_tolerance=None, preserve_enabled_values=None):
    """CreateGeometricNetwork_management(in_feature_dataset, out_name, in_source_feature_classes;in_source_feature_classes..., {snap_tolerance}, {weights;weights...}, {weight_associations;weight_associations...}, {z_snap_tolerance}, {preserve_enabled_values})

        Creates a geometric network in a geodatabase using the specified feature
        classes, role for each feature class, and the specified weights with weight
        associations.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          The feature dataset in which the geometric network will be created. In an
          enterprise geodatabase, the feature dataset and feature classes that will
          participate in the geometric network cannot be versioned.
      out_name (String):
          The name of the geometric network to be created.
      in_source_feature_classes (Value Table):
          The input feature classes to be added to the geometric network and the role the
          feature class should play in the geometric network. Roles can be:

          *  SIMPLE_JUNCTION—The only option for point feature classes.

          *  SIMPLE_EDGE—Used for line feature classes and only allows resources to flow
          from one end of the edge and out the other end.

          *  COMPLEX_EDGE—Used for line feature classes and allows resources to be
          siphoned off along the length of the edge.
           For each simple junction feature class, whether it will participate in flow
          direction with Sources and Sinks.

          *  YES—Simple junction feature class will act as a source or a sink for
          establishing flow direction.

          *  NO—Simple junction feature class will not act as a source or a sink for
          establishing flow direction.
      snap_tolerance {Double}:
          The snapping tolerance to be set on the geometric network. The larger the value,
          the more likely vertices will be to snap together. The default value is empty,
          which means that no snapping will be performed during geometric network
          creation. The snapping performed during geometric network creation cannot be
          undone.
      weights {Value Table}:
          Weights are the cost of traveling along an edge in a network. For example, in a
          water network, a weight can be the length of the pipe. Indicate the weight name,
          weight type, and for bitgate weights, the size. The type of the weight
          determines which feature class fields can be associated with the weight. Types
          can be one of the following:

          *  Integer—Can be associated with fields of type Short Integer or Long Integer.

          *  Single—Can be associated with fields of type Float.

          *  Double—Can be associated with fields of type Float or Double.

          *  Bitgate—Can be associated with fields of type Short Integer or Long Integer.
          Only values from 0 to 31 are supported.
      weight_associations {Value Table}:
          Specifies the weight associations for each field and feature class.  When
          adding a new network weight, it must be associated with a field in a feature
          class which will provide the values to determine the weight for the features.
      z_snap_tolerance {Double}:
          The snapping tolerance to be set on the geometric network with z-coordinate
          based snapping. The larger the value, the more likely vertices will be to snap
          together. The default value is empty which means that no snapping will be
          performed during geometric network creation, and the geometric network will not
          support Zs. A value of zero indicates that no snapping will be performed during
          the geometric network creation, but the geometric network will support Zs.
      preserve_enabled_values {Boolean}:
          Specifies whether to preserve the values in any existing enabled fields or
          whether the values should be reset to their default value of True.

          *  PRESERVE_ENABLED—Valid values (either True or False) in the existing enabled
          fields are preserved. This is the default.

          * NO_PRESERVE_ENABLED— Valid values (either True or False) in the existing
          enabled fields are not preserved."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateGeometricNetwork_management(*gp_fixargs((in_feature_dataset, out_name, in_source_feature_classes, snap_tolerance, weights, weight_associations, z_snap_tolerance, preserve_enabled_values), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('FindDisconnectedFeaturesInGeometricNetwork_management', None)
def FindDisconnectedFeaturesInGeometricNetwork(in_layer=None, out_layer=None):
    """FindDisconnectedFeaturesInGeometricNetwork_management(in_layer, out_layer)

        Finds junctions not connected to edges for a simple junction feature layer.
        Finds edges not connected to any other edges for simple and complex edge feature
        layers.

     INPUTS:
      in_layer (Feature Layer):
          The feature layer in which to search for disconnected features.

     OUTPUTS:
      out_layer (Feature Layer):
          The output feature layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FindDisconnectedFeaturesInGeometricNetwork_management(*gp_fixargs((in_layer, out_layer), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RebuildGeometricNetwork_management', None)
def RebuildGeometricNetwork(geometric_network=None, out_log=None):
    """RebuildGeometricNetwork_management(geometric_network, out_log)

        Drops and re-creates the logical network index for the geometric network. If
        the geometric network is in an enterprise geodatabase and is versioned, the
        logical network will be rebuilt across all versions of the database. This tool
        will not change features in the network, no snapping will occur, and no orphan
        junction features will be created.

     INPUTS:
      geometric_network (Geometric Network):
          The geometric network to rebuild.

     OUTPUTS:
      out_log (File):
          A log file containing details about the progress of the tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RebuildGeometricNetwork_management(*gp_fixargs((geometric_network, out_log), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveConnectivityRuleFromGeometricNetwork_management', None)
def RemoveConnectivityRuleFromGeometricNetwork(in_geometric_network=None, in_connectivity_rules=None):
    """RemoveConnectivityRuleFromGeometricNetwork_management(in_geometric_network, in_connectivity_rules;in_connectivity_rules...)

        Removes a connectivity rule from the geometric network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network from which the connectivity rule will be removed.
      in_connectivity_rules (String):
          For Edge-Junction rules, the edge feature class with subtype and junction
          feature class with subtype. For Edge-Edge rules, the from edge feature class
          with subtype, the to edge feature class with subtype and junction with subtype."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveConnectivityRuleFromGeometricNetwork_management(*gp_fixargs((in_geometric_network, in_connectivity_rules), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveEmptyFeatureClassFromGeometricNetwork_management', None)
def RemoveEmptyFeatureClassFromGeometricNetwork(in_geometric_network=None, in_feature_class=None):
    """RemoveEmptyFeatureClassFromGeometricNetwork_management(in_geometric_network, in_feature_class)

        Removes an empty feature class from a geometric network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network from which the feature class will be removed.
      in_feature_class (String):
          The name of the feature class to remove."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveEmptyFeatureClassFromGeometricNetwork_management(*gp_fixargs((in_geometric_network, in_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetFlowDirection_management', None)
def SetFlowDirection(in_geometric_network=None, flow_option=None):
    """SetFlowDirection_management(in_geometric_network, flow_option)

        Sets the flow direction for a geometric network based on either the digitized
        direction or the source/sink settings in the geometric network.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network for which flow will be set.
      flow_option (String):
          Indicates method by which flow direction will be established; there is no
          default value.

          * WITH_DIGITIZED_DIRECTION—Establish flow direction along the digitized
          direction of edges.

          * AGAINST_DIGITIZED_DIRECTION—Establish flow direction against the digitized
          direction of edges.

          *  WITH_SOURCES_SINKS—Establish flow direction using sources and sinks.

          * RESET_FLOW_DIRECTION—Reset flow direction on all edges to be uninitialized."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetFlowDirection_management(*gp_fixargs((in_geometric_network, flow_option), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TraceGeometricNetwork_management', None)
def TraceGeometricNetwork(in_geometric_network=None, out_network_layer=None, in_flags=None, in_trace_task_type=None, in_barriers=None, in_junction_weight=None, in_edge_along_digitized_weight=None, in_edge_against_digitized_weight=None, in_disable_from_trace=None, in_trace_ends=None, in_trace_indeterminate_flow=None, in_junction_weight_filter=None, in_junction_weight_range=None, in_junction_weight_range_not=None, in_edge_along_digitized_weight_filter=None, in_edge_against_digitized_weight_filter=None, in_edge_weight_range=None, in_edge_weight_range_not=None):
    """TraceGeometricNetwork_management(in_geometric_network, out_network_layer, in_flags, in_trace_task_type, {in_barriers}, {in_junction_weight}, {in_edge_along_digitized_weight}, {in_edge_against_digitized_weight}, {in_disable_from_trace;in_disable_from_trace...}, {in_trace_ends}, {in_trace_indeterminate_flow}, {in_junction_weight_filter}, {in_junction_weight_range}, {in_junction_weight_range_not}, {in_edge_along_digitized_weight_filter}, {in_edge_against_digitized_weight_filter}, {in_edge_weight_range}, {in_edge_weight_range_not})

        Solves the specified network analysis problem based on the flags, barriers, and
        specified weight properties.

     INPUTS:
      in_geometric_network (Geometric Network):
          The geometric network on which the trace will be performed.
      in_flags (Feature Layer):
          Point features representing a set of flags that serve as starting points for
          the tracing operation. For example, if you are performing an upstream trace, you
          use a flag to specify where the upstream trace will begin. Flags can be placed
          anywhere along edges or junctions, but junctions will be considered first when
          both a junction and edge are found at the location.
      in_trace_task_type (String):
          Trace task to be performed on the specified geometric network.

          * FIND_COMMON_ANCESTORS— Find the common features that are upstream of a set of
          points in your network. Requires flow direction to be set on the geometric
          network.

          * FIND_CONNECTED—Find the features that are connected to a given point through
          your network.

          * FIND_LOOPS— Find loops within the network that are defined by determining for
          each connected feature, on which you placed a flag, the features that loop back
          on themselves (that is, can't be reached from more than one direction).

          * FIND_DISCONNECTED— Find all of the features that are not connected to a given
          point through your network.

          * FIND_PATH_UPSTREAM— Find an upstream path from a point in your network. The
          path found can be just one of a number of paths depending on whether or not your
          network contains loops. The flags you place on the network can be a mixture of
          edge flags and junction flags.  Requires a weight to be defined for the trace
          and flow direction to be set on the geometric network. When a weight is not
          specified, the shortest path is determined by the least number of features
          between the two points.

          * FIND_PATH— Find a path between two or more flags in the network. The path
          found can be just one of a number of paths between the flags depending on
          whether or not your network contains loops. The flags you place on the network
          must be either all edge flags or all junction flags.  When a weight is not
          specified, the shortest path is determined by the least number of features
          between the two points.

          * TRACE_DOWNSTREAM—Find all network features that lie downstream (with flow
          direction) of a given point in your network. Requires flow direction to be set
          on the geometric network.

          * FIND_UPSTREAM_ACCUMULATION— Determine the total cost of all network features
          that lie upstream of a given point in your network. Requires a weight be defined
          for the trace and flow direction to be set on the geometric network.

          * TRACE_UPSTREAM— Find all features that lie upstream (against flow direction)
          of a given point in your network. Requires flow direction to be set on the
          geometric network.
      in_barriers {Feature Layer}:
          Point features representing a set of barriers. Barriers define places in the
          network where traces cannot pass through. If you are only interested in tracing
          a particular part of your network, you can use barriers to isolate that part of
          the network. Barriers can be placed anywhere along edges or junctions, but
          junctions will be considered first when both a junction and edge are found at
          the location. The feature will be treated as disabled and will not be considered
          during the trace, unless you've set the in_trace_ends parameter to TRACE_ENDS to
          purposefully find features stopping the trace.
      in_junction_weight {String}:
          A junction weight that is used as a cost for traversing through any junction.
          The weight must already be defined for the given geometric network. This
          parameter is disabled or ignored when one of the following cost-independent
          trace task types is specified:

          * FIND_COMMON_ANCESTORS

          * FIND_CONNECTED

          * FIND_LOOPS

          * FIND_DISCONNECTED

          * TRACE_DOWNSTREAM

          * TRACE_UPSTREAM
      in_edge_along_digitized_weight {String}:
          An edge weight that is used as a cost for traversing through an edge along the
          digitized direction of that edge. The weight must already be defined for the
          given geometric network. This parameter is disabled or ignored when one of the
          following cost-independent trace task types is specified:

          * FIND_COMMON_ANCESTORS

          * FIND_CONNECTED

          * FIND_LOOPS

          * FIND_DISCONNECTED

          * TRACE_DOWNSTREAM

          * TRACE_UPSTREAM
      in_edge_against_digitized_weight {String}:
          An edge weight that is used as a cost for traversing through an edge against
          the digitized direction of that edge. The weight must already be defined for the
          given geometric network. This parameter is disabled or ignored when one of the
          following cost-independent trace task types is specified:

          * FIND_COMMON_ANCESTORS

          * FIND_CONNECTED

          * FIND_LOOPS

          * FIND_DISCONNECTED

          * TRACE_DOWNSTREAM

          * TRACE_UPSTREAM
      in_disable_from_trace {String}:
          List of feature classes that are disabled from participating in the trace.
          Specifying a feature class as disabled makes the trace operation treat all
          features in that feature class as either being disabled or as having a barrier
          placed on them. Use this option to exclude an entire feature class from
          consideration during a trace. For example, by disabling the switches layer in an
          electrical distribution network, setting the in_trace_ends parameter to
          TRACE_ENDS and tracing from a given point in the network, you can find the
          switches that need to be thrown to isolate this point from the network; these
          will be the features at which the trace operation is stopped.
      in_trace_ends {Boolean}:
          Indicates whether the trace should include all features or only those stopping
          the trace. Use this option when you need to determine which features are
          stopping a trace. In order to be returned from the trace operation with this
          option, features must fall into one of the following categories:

          * The feature is connected to only one other geometric network feature (dead
          ends).

          * The feature is disabled (including those in disabled feature classes).

          * The feature has a barrier placed on it.

          * TRACE_ENDS—Include those features stopping the trace.

          * NO_TRACE_ENDS—Include all features. This is the default.
      in_trace_indeterminate_flow {Boolean}:
          Indicates whether the trace should include all features or only those stopping
          the trace.

          * TRACE_INDETERMINATE_FLOW—Trace features that have indeterminate or
          uninitialized flow direction.

          * NO_TRACE_INDETERMINATE_FLOW—Do not trace features that have indeterminate or
          uninitialized flow direction. This is the default.
          Only honored when one flow-dependent trace task type is set:

          * FIND_PATH_UPSTREAM

          * TRACE_DOWNSTREAM

          * FIND_UPSTREAM_ACCUMULATION

          * TRACE_UPSTREAM
      in_junction_weight_filter {String}:
          The weight to use to create the junction weight filter, which is used to filter
          junction features during the trace.
      in_junction_weight_range {String}:
          Specifies valid or invalid ranges of weight values for network features that
          can be traced. It is disabled when a cost-independent trace task type is set. In
          order to create a weight filter, you must specify valid weight ranges for the
          features. A weight filter can be composed of a number of ranges. When you
          specify multiple weight ranges, delimit the ranges with commas. Low and high
          values in a range are separated by a hyphen. Ranges consisting of a single value
          do not contain a hyphen and are delimited with commas, for example,
          0-2,3,6,7-10.
      in_junction_weight_range_not {Boolean}:
          Applies the logical NOT operator to the specified junction weight ranges. By
          default, the junction weight ranges that you enter specify junction features
          that can be traced. By checking this option, you indicate that junction features
          with weights in the ranges you entered cannot be traced.

          * AS_IS —Weight ranges specify features that can be traced. This is the default.

          * NOT—Weight ranges specify features that cannot be traced.
      in_edge_along_digitized_weight_filter {String}:
          The weight to use to create the along-edge weight filter, which is used to
          filter edge features during the trace.
      in_edge_against_digitized_weight_filter {String}:
          The weight to use to create the against-edge weight filter, which is used to
          filter edge features during the trace.
      in_edge_weight_range {String}:
          Specifies valid or invalid ranges of weight values for network features that
          can be traced. It is disabled when a cost-independent trace task type is set. In
          order to create a weight filter, you must specify valid weight ranges for the
          features. A weight filter can be composed of a number of ranges. When you
          specify multiple weight ranges, you must delimit the ranges with commas. Low and
          high values in a range are separated by a hyphen. Ranges consisting of a single
          value do not contain a hyphen and are delimited with commas, for example,
          0-2,3,6,7-10.
      in_edge_weight_range_not {Boolean}:
          Applies the logical NOT operator to the specified edge weight ranges. By
          default, the edge weight ranges that you enter specify edge features that can be
          traced. By checking this option, you indicate that edge features with weights in
          the ranges you entered cannot be traced.

          * AS_IS —Weight ranges specify features that can be traced. This is the default.

          * NOT—Weight ranges specify features that cannot be traced.

     OUTPUTS:
      out_network_layer (Group Layer):
          The name of the group layer that will store the results of the trace as a
          selected set."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TraceGeometricNetwork_management(*gp_fixargs((in_geometric_network, out_network_layer, in_flags, in_trace_task_type, in_barriers, in_junction_weight, in_edge_along_digitized_weight, in_edge_against_digitized_weight, in_disable_from_trace, in_trace_ends, in_trace_indeterminate_flow, in_junction_weight_filter, in_junction_weight_range, in_junction_weight_range_not, in_edge_along_digitized_weight_filter, in_edge_against_digitized_weight_filter, in_edge_weight_range, in_edge_weight_range_not), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('VerifyAndRepairGeometricNetworkConnectivity_management', None)
def VerifyAndRepairGeometricNetworkConnectivity(geometric_network=None, out_log=None, verify_or_repair=None, exhaustive_check=None, extent=None):
    """VerifyAndRepairGeometricNetworkConnectivity_management(geometric_network, out_log, {verify_or_repair}, {exhaustive_check}, {extent})

        Detects and optionally repairs a variety of connectivity and geometry problems
        within geometric networks.

     INPUTS:
      geometric_network (Geometric Network):
          The geometric network to verify.
      verify_or_repair {Boolean}:
          Indicates whether connectivity errors will be repaired or not.

          * VERIFY_ONLY—  Run verification checks for the geometric network for
          connectivity errors but do not perform repair. This is the default.

          * VERIFY_AND_REPAIR—After completion of the verification checks, perform repair
          of the connectivity errors.
      exhaustive_check {Boolean}:
          Indicates whether an exhaustive check will be performed against the geometric
          network. The exhaustive check will increase the time the tool will take to
          complete. Therefore, it is recommended that it be run over a subset of the
          geometric network such as the extent of edits made within a version.

          * NO_EXHAUSTIVE_CHECK—Do not perform the exhaustive check. This is the default.

          * EXHAUSTIVE_CHECK —Perform the exhaustive check over the extent provided.
      extent {Extent}:
          The four coordinates defining the extent over which the exhaustive check will
          be run. The extent is specified as X-Minimum, Y-Minimum, X-Maximum, Y-Maximum.

     OUTPUTS:
      out_log (File):
          A log file containing details about the progress of the tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.VerifyAndRepairGeometricNetworkConnectivity_management(*gp_fixargs((geometric_network, out_log, verify_or_repair, exhaustive_check, extent), True)))
        return retval
    except Exception, e:
        raise e


# Graph toolset
@gptooldoc('MakeGraph_management', None)
def MakeGraph(in_graph_template_source=None, in_datasets=None, out_graph_name=None):
    """MakeGraph_management(in_graph_template_source, in_datasets, out_graph_name)

        Creates a graph as a visual output using a graph template or an existing graph.

     INPUTS:
      in_graph_template_source (Graph / File):
          The input graph template (.tee) or graph file (.grf).
      in_datasets (Graph Data Table):
          The input data for individual series in the graph. The input data varies based
          on the graph type. To facilitate populating the parameters used for creating the
          graph series from Python, you can use the Graph class.

     OUTPUTS:
      out_graph_name (Graph):
          The name of the graph to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeGraph_management(*gp_fixargs((in_graph_template_source, in_datasets, out_graph_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SaveGraph_management', None)
def SaveGraph(in_graph=None, out_graph_file=None, maintain_image_aspect=None, image_width=None, image_height=None):
    """SaveGraph_management(in_graph, out_graph_file, {maintain_image_aspect}, {image_width}, {image_height})

        Saves a graph to an image, vector, or graph file.

     INPUTS:
      in_graph (Graph / File):
          Input graph name or location.You can input the location of an existing graph
          file (*.grf).However, when you are using the tool in an ArcGIS application
          (ArcMap, ArcGlobe,
          or ArcScene), you can either input a graph present in the ArcGIS document or you
          can input the location of an existing graph file (*.grf).
      maintain_image_aspect {Boolean}:
          * MAINTAIN_ASPECT_RATIO—The aspect ratio of the output image will be preserved.

          * IGNORE_ASPECT_RATIO— The aspect ratio of the output image will not be
          preserved.
      image_width {Long}:
          The width of the output image in pixels.
      image_height {Long}:
          The height of the output image in pixels.

     OUTPUTS:
      out_graph_file (File):
          The output image, vector, or graph file.The supported image and vector formats
          are:

          * Windows Bitmap (.bmp)

          * GIF(.gif)

          * JPEG (.jpg)

          * Portable Network Graphic (.png)

          * Paintbrush (.pcx)

          * Scalable Vector Graphics (.svg)

          * Adobe Acrobat PDF (.pdf)

          * Encapsulated PostsScript (.eps)

          * Enhanced Metafile (.emf)

          * Windows Metafile (.wmf)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SaveGraph_management(*gp_fixargs((in_graph, out_graph_file, maintain_image_aspect, image_width, image_height), True)))
        return retval
    except Exception, e:
        raise e


# Indexes toolset
@gptooldoc('AddIndex_management', None)
def AddIndex(in_table=None, fields=None, index_name=None, unique=None, ascending=None):
    """AddIndex_management(in_table, fields;fields..., {index_name}, {unique}, {ascending})

        Adds an attribute index to an existing table, feature class, shapefile,
        coverage, or attributed relationship class.Attribute indexes are used by ArcGIS
        to quickly locate records that match an
        attribute query. For information on attribute indexes in geodatabases, see
        Creating attribute indexes.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table containing the fields to be indexed.
      fields (Field):
          The list of fields that will participate in the index. Any number of fields can
          be specified.
      index_name {String}:
          The name of the new index. An index name is necessary when adding an index to
          geodatabase feature classes and tables. For other types of input, the Index Name
          is ignored
      unique {Boolean}:
          Specifies whether the values in the index are unique.

          * NON_UNIQUE—All values in the index are not unique. This is the default.

          * UNIQUE—All values in the index are unique.
      ascending {Boolean}:
          Specifies whether values are indexed in ascending order.

          * NON_ASCENDING—Values are not indexed in ascending order. This is the default.

          * ASCENDING—Values are indexed in ascending order."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddIndex_management(*gp_fixargs((in_table, fields, index_name, unique, ascending), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddSpatialIndex_management', None)
def AddSpatialIndex(in_features=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None):
    """AddSpatialIndex_management(in_features, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Adds a spatial index to a shapefile, file geodatabase, or ArcSDE feature class.
        Use this tool to either add a spatial index to a shapefile or feature class that
        does not already have one or to rebuild an existing spatial index.

     INPUTS:
      in_features (Feature Layer / Raster Catalog Layer / Mosaic Layer):
          ArcSDE feature class, file geodatabase feature class, or shapefile to which a
          spatial index is to be added or rebuilt.
      spatial_grid_1 {Double}:
          The Spatial Grid 1, 2, and 3 parameters apply only to file geodatabase and
          certain ArcSDE geodatabase feature classes. If you are unfamiliar with setting
          grid sizes, leave these options as 0,0,0, and ArcGIS will compute optimal sizes
          for you.
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
        retval = convertArcObjectToPythonObject(gp.AddSpatialIndex_management(*gp_fixargs((in_features, spatial_grid_1, spatial_grid_2, spatial_grid_3), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveIndex_management', None)
def RemoveIndex(in_table=None, index_name=None):
    """RemoveIndex_management(in_table, index_name;index_name...)

        This tool deletes an attribute index from an existing table, feature class,
        shapefile, coverage, or attributed relationship class.Attribute indexes are used
        by ArcGIS to quickly locate records that match an
        attribute query.

     INPUTS:
      in_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table containing the index or indexes to be deleted. Table can refer to an
          actual table, a feature class attribute table, or an attributed relationship
          class.
      index_name (String):
          The name of the index or indexes to be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveIndex_management(*gp_fixargs((in_table, index_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveSpatialIndex_management', None)
def RemoveSpatialIndex(in_features=None):
    """RemoveSpatialIndex_management(in_features)

        Deletes the spatial index from a shapefile, file geodatabase feature class, or
        an ArcSDE feature class. The spatial index cannot be deleted from a personal
        geodatabase feature class.Spatial indexes are used by ArcGIS to quickly locate
        features that match a
        spatial query.

     INPUTS:
      in_features (Feature Layer / Raster Catalog Layer / Mosaic Layer):
          The features from which the spatial index will be removed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveSpatialIndex_management(*gp_fixargs((in_features,), True)))
        return retval
    except Exception, e:
        raise e


# Joins toolset
@gptooldoc('AddJoin_management', None)
def AddJoin(in_layer_or_view=None, in_field=None, join_table=None, join_field=None, join_type=None):
    """AddJoin_management(in_layer_or_view, in_field, join_table, join_field, {join_type})

        Joins a layer to another layer or table (where layer is a feature layer, table
        view, or raster layer with a raster attribute table) based on a common field.The
        records in the Join Table are matched to the records in the input Layer
        Name. A match is made when the input join field and output join field values are
        equal. This join is temporary.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The layer or table view to which the join table will be joined.
      in_field (Field):
          The field in the input layer or table view on which the join will be based.
      join_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table or table view to be joined to the input layer or table view.
      join_field (Field):
          The field in the join table that contains the values on which the join will be
          based.
      join_type {Boolean}:
          Specifies what will be done with records in the input that match a record in the
          join table.

          * KEEP_ALL—All records in the input layer or table view will be included in the
          output—also known as an outer join. This is the default.

          * KEEP_COMMON—Only those records in the input that match to a row in the join
          table will be present in the result—also known as an inner join."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddJoin_management(*gp_fixargs((in_layer_or_view, in_field, join_table, join_field, join_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('JoinField_management', None)
def JoinField(in_data=None, in_field=None, join_table=None, join_field=None, fields=None):
    """JoinField_management(in_data, in_field, join_table, join_field, {fields;fields...})

        Joins the contents of a table to another table based on a common attribute
        field. The input table is updated to contain the fields from the join table. You
        can select which fields from the join table will be added to the input table.The
        records in the Input Table are matched to the records in the Join Table
        based on the values of Input Join Field and the Output Join Field. Optionally,
        only desired fields can be selected from the Join Table and appended to the
        Input Table during the join.

     INPUTS:
      in_data (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table or feature class to which the join table will be joined.
      in_field (Field):
          The field in the input table on which the join will be based.
      join_table (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The table to be joined to the input table.
      join_field (Field):
          The field in the join table that contains the values on which the join will be
          based.
      fields {Field}:
          The fields from the join table to be included in the join."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.JoinField_management(*gp_fixargs((in_data, in_field, join_table, join_field, fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveJoin_management', None)
def RemoveJoin(in_layer_or_view=None, join_name=None):
    """RemoveJoin_management(in_layer_or_view, {join_name})

        Removes a join from a feature layer or table view.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Raster Catalog Layer / Mosaic Layer):
          The layer or table view from which the join will be removed.
      join_name {String}:
          The join to be removed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveJoin_management(*gp_fixargs((in_layer_or_view, join_name), True)))
        return retval
    except Exception, e:
        raise e


# LAS Dataset toolset
@gptooldoc('AddFilesToLasDataset_management', None)
def AddFilesToLasDataset(in_las_dataset=None, in_files=None, folder_recursion=None, in_surface_constraints=None):
    """AddFilesToLasDataset_management(in_las_dataset, {in_files;in_files...}, {folder_recursion}, {in_surface_constraints;in_surface_constraints...})

        Adds references for one or more LAS files and surface constraint features to a
        LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      in_files {Folder / File}:
          Input files can reference any combination of individual LAS files and folders
          containing LAS data.
      folder_recursion {Boolean}:
          Specifies whether lidar data residing in the subdirectories of an input folder
          would get added to the LAS dataset.

          *  NO_RECURSION —Only lidar files found in an input folder will be added to the
          LAS dataset. This is the default.

          * RECURSION—All LAS files residing in the subdirectories of an input folder will
          be added to the LAS dataset.
      in_surface_constraints {Value Table}:
          The feature classes that will be referenced by the LAS dataset. Each feature
          will need the following properties defined:in_feature_class—The feature class to
          be referenced by the LAS dataset.height_field—The field that specifies the
          source of elevation values for the
          features. Any numeric field in the feature's attribute table can be used. If the
          feature supports z-values, the feature geometry can be read by selecting the
          Shape.Z option. If no height is desired, specify the keyword <None> to create
          Z-less features whose elevation would be interpolated from the
          surface.SF_type—The surface feature type that defines how the feature geometry
          gets
          incorporated into the triangulation for the surface. Options with hard or soft
          designation refer to whether the feature edges represent distinct breaks in
          slope or a gradual change.

          * anchorpoints—Elevation points that never get thinned away. This option is only
          available for single-point feature geometry.

          * hardline or softline—Breaklines that enforce a height value.

          * hardclip or softclip—Polygon dataset that defines the boundary of the LAS
          dataset.

          * harderase or softerase—Polygon dataset that defines holes in the LAS dataset.

          * hardreplace or softreplace—Polygon dataset that defines areas of constant
          height."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddFilesToLasDataset_management(*gp_fixargs((in_las_dataset, in_files, folder_recursion, in_surface_constraints), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateLasDataset_management', None)
def CreateLasDataset(input=None, out_las_dataset=None, folder_recursion=None, in_surface_constraints=None, spatial_reference=None, compute_stats=None, relative_paths=None):
    """CreateLasDataset_management(input;input..., out_las_dataset, {folder_recursion}, {in_surface_constraints;in_surface_constraints...}, {spatial_reference}, {compute_stats}, {relative_paths})

        Creates a LAS dataset referencing one or more LAS files and optional surface
        constraint features.

     INPUTS:
      input (Folder / File):
          The LAS files and folders containing LAS files that will be referenced by the
          LAS dataset. This information can be supplied as a string containing all the
          input data or a list of strings containing specific data elements (for example,
          "lidar1.las; lidar2.las; folder1; folder2" or ["lidar1.las", "lidar2.las",
          "folder1", "folder2"]).See Understanding tool syntax for more information on
          specifying lists for
          input.
      folder_recursion {Boolean}:
          Specifies whether lidar data residing in the subdirectories of an input folder
          would get added to the LAS dataset.

          *  NO_RECURSION —Only lidar files found in an input folder will be added to the
          LAS dataset. This is the default.

          * RECURSION—All LAS files residing in the subdirectories of an input folder will
          be added to the LAS dataset.
      in_surface_constraints {Value Table}:
          The feature classes that will be referenced by the LAS dataset. Each feature
          will need the following properties defined:in_feature_class—The feature class to
          be referenced by the LAS dataset.height_field—The field that specifies the
          source of elevation values for the
          features. Any numeric field in the feature's attribute table can be used. If the
          feature supports z-values, the feature geometry can be read by selecting the
          Shape.Z option. If no height is desired, specify the keyword <None> to create
          Z-less features whose elevation would be interpolated from the
          surface.SF_type—The surface feature type that defines how the feature geometry
          gets
          incorporated into the triangulation for the surface. Options with hard or soft
          designation refer to whether the feature edges represent distinct breaks in
          slope or a gradual change.

          * anchorpoints—Elevation points that never get thinned away. This option is only
          available for single-point feature geometry.

          * hardline or softline—Breaklines that enforce a height value.

          * hardclip or softclip—Polygon dataset that defines the boundary of the LAS
          dataset.

          * harderase or softerase—Polygon dataset that defines holes in the LAS dataset.

          * hardreplace or softreplace—Polygon dataset that defines areas of constant
          height.
      spatial_reference {Coordinate System}:
          The spatial reference of the LAS dataset. If no spatial reference is explicitly
          assigned, the LAS dataset will use the coordinate system of the first input LAS
          file. If the input files do not contain any spatial reference information and
          the Input Coordinate System is not set, then the LAS dataset's coordinate system
          will be listed as unknown.
      compute_stats {Boolean}:
          Specifies whether statistics for the LAS files will be computed and a spatial
          index generated for the LAS dataset.  The presence of statistics allows the LAS
          dataset layer's filtering and symbology options to only show LAS attribute
          values that exist in the LAS files. A .lasx auxiliary file is created for each
          LAS file.

          * COMPUTE_STATS—Statistics will be computed.

          * NO_COMPUTE_STATS—Statistics will not be computed. This is the default.
      relative_paths {Boolean}:
          Specifies whether lidar files and surface constraint features will be referenced
          by the LAS dataset through relative or absolute paths. Using relative paths may
          be convenient for cases where the LAS dataset and its associated data will be
          relocated in the file system using the same relative location to one another.

          *  ABSOLUTE_PATHS —Absolute paths will be used for the data referenced by the
          LAS dataset. This is the default.

          * RELATIVE_PATHS—Relative paths will be used for the data referenced by the LAS
          dataset.

     OUTPUTS:
      out_las_dataset (LAS Dataset):
          The LAS dataset that will be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateLasDataset_management(*gp_fixargs((input, out_las_dataset, folder_recursion, in_surface_constraints, spatial_reference, compute_stats, relative_paths), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LasDatasetStatistics_management', None)
def LasDatasetStatistics(in_las_dataset=None, calculation_type=None, out_file=None, summary_level=None, delimiter=None, decimal_separator=None):
    """LasDatasetStatistics_management(in_las_dataset, {calculation_type}, {out_file}, {summary_level}, {delimiter}, {decimal_separator})

        Calculates or updates statistics for a LAS dataset and generates an optional
        statistics report.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      calculation_type {Boolean}:
          Specifies whether statistics will be calculated for all lidar files or only for
          those that do not have statistics:

          * SKIP_EXISTING_STATS—LAS files with up-to-date statistics will be skipped, and
          statistics will only be calculated for newly added LAS files or ones that were
          updated since the initial calculation. This is the default.

          * OVERWRITE_EXISTING_STATS—Statistics will be calculated for all LAS files,
          including ones that have up-to-date statistics. This is useful if the LAS files
          were modified in an external application that went undetected by ArcGIS.
      summary_level {String}:
          Specify the type of summary contained in the report.

          * DATASET—The report will summarize statistics for the entire LAS dataset. This
          is the default.

          * LAS_FILES—The report will summarize statistics for the LAS files referenced by
          the LAS dataset.
      delimiter {String}:
          The delimiter used to indicate the separation of entries in the columns of the
          text file table.

          * SPACE—A space will be used to delimit field values. This is the default.

          * COMMA—A comma will be used to delimit field values. This option is not
          applicable if the decimal separator is also a comma.
      decimal_separator {String}:
          The decimal character used in the text file to differentiate the integer of a
          number from its fractional part.

          * DECIMAL_POINT—A point is used as the decimal character. This is the default.

          * DECIMAL_COMMA—A comma is used as the decimal character.

     OUTPUTS:
      out_file {Text File}:
          The output text file that will contain the summary of the LAS dataset
          statistics."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LasDatasetStatistics_management(*gp_fixargs((in_las_dataset, calculation_type, out_file, summary_level, delimiter, decimal_separator), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LasPointStatsAsRaster_management', None)
def LasPointStatsAsRaster(in_las_dataset=None, out_raster=None, method=None, sampling_type=None, sampling_value=None):
    """LasPointStatsAsRaster_management(in_las_dataset, out_raster, {method}, {sampling_type}, {sampling_value})

        Creates a raster whose cell values reflect statistical information about
        measurements from LAS files referenced by a LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      method {String}:
          The type of statistics collected about the LAS points in each cell of the
          output raster.

          * PULSE_COUNT—The number of last return points.

          * POINT_COUNT—The number of points from all returns.

          * PREDOMINANT_LAST_RETURN—The most frequent last return value.

          * PREDOMINANT_CLASS—The most frequent class code.

          * INTENSITY_RANGE—The range of intensity values.

          * Z_RANGE—The range of elevation values.
      sampling_type {String}:
          Specifies the method used for interpreting the Sampling Value to define the
          resolution of the output raster.

          * OBSERVATIONS—Defines the number of cells that divide the lengthiest side of
          the LAS dataset extent.

          * CELLSIZE—Defines the cell size of the output raster. This is the default.
      sampling_value {Double}:
          Specifies the value used in conjunction with the Sampling Type to define the
          resolution of the output raster.

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
        retval = convertArcObjectToPythonObject(gp.LasPointStatsAsRaster_management(*gp_fixargs((in_las_dataset, out_raster, method, sampling_type, sampling_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveFilesFromLasDataset_management', None)
def RemoveFilesFromLasDataset(in_las_dataset=None, in_files=None, in_surface_constraints=None):
    """RemoveFilesFromLasDataset_management(in_las_dataset, {in_files;in_files...}, {in_surface_constraints;in_surface_constraints...})

        Removes one or more LAS files and surface constraint features from a LAS
        dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      in_files {Folder / File}:
          The LAS files or folders containing LAS files that will be removed from the LAS
          dataset.
      in_surface_constraints {String}:
          The name of the surface constraint features that will be removed from the LAS
          dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveFilesFromLasDataset_management(*gp_fixargs((in_las_dataset, in_files, in_surface_constraints), True)))
        return retval
    except Exception, e:
        raise e


# Layers and Table Views toolset
@gptooldoc('ApplySymbologyFromLayer_management', None)
def ApplySymbologyFromLayer(in_layer=None, in_symbology_layer=None):
    """ApplySymbologyFromLayer_management(in_layer, in_symbology_layer)

        This tool applies the symbology from a layer to the Input Layer. It can be
        applied to feature, raster, network analysis, TIN, and geostatistical  layer
        files or layers in the ArcMap table of contents. This tool is primarily for use
        in scripts or ModelBuilder.

     INPUTS:
      in_layer (Layer):
          The layer to which the symbology will be applied.
      in_symbology_layer (Layer):
          The symbology of this layer is applied to the Input Layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ApplySymbologyFromLayer_management(*gp_fixargs((in_layer, in_symbology_layer), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeFeatureLayer_management', None)
def MakeFeatureLayer(in_features=None, out_layer=None, where_clause=None, workspace=None, field_info=None):
    """MakeFeatureLayer_management(in_features, out_layer, {where_clause}, {workspace}, {field_info})

        Creates a feature layer from an input feature class or layer file. The layer
        that is created by the tool is temporary and will not persist after the session
        ends unless the layer is saved to disk or the map document is saved.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer from which to make the new layer. Complex
          feature classes, such as annotation and dimensions, are not valid inputs to this
          tool.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS.
      workspace {Workspace / Feature Dataset}:
          The input workspace used to validate the field names. If the input is a
          geodatabase table and the output workspace is a dBASE table, the field names may
          be truncated, since dBASE fields can only have names of ten characters or less.
          The new names may be reviewed and altered using the field information control.
      field_info {Field Info}:
          Can be used to review and alter the field names and hide a subset of fields in
          the output layer. A split policy can be specified. See the usages for more
          information.

     OUTPUTS:
      out_layer (Feature Layer):
          The name of the feature layer to be created. The newly created layer can be used
          as input to any geoprocessing tool that accepts a feature layer as input."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeFeatureLayer_management(*gp_fixargs((in_features, out_layer, where_clause, workspace, field_info), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeImageServerLayer_management', None)
def MakeImageServerLayer(in_image_service=None, out_imageserver_layer=None, template=None, band_index=None, mosaic_method=None, order_field=None, order_base_value=None, lock_rasterid=None, cell_size=None, where_clause=None, processing_template=None):
    """MakeImageServerLayer_management(in_image_service, out_imageserver_layer, {template}, {band_index;band_index...}, {mosaic_method}, {order_field}, {order_base_value}, {lock_rasterid}, {cell_size}, {where_clause}, {processing_template})

        Creates a temporary raster layer from an image service. The layer that is
        created will not persist after the session ends unless the document is saved.The
        input can also be a SOAP URL to an image server.

     INPUTS:
      in_image_service (Image Service / String):
          The name of the input image service, or the SOAP URL that references the image
          service.An example of a URL is:
          http://AGSServer:8399/arcgis/services/ISName/ImageServer
      template {Extent}:
          The output extent of the image layer.The output extent can be specified by
          defining the area to be clipped
          (X-Minimum, Y-Minimum, X-Maximum, and Y-Maximum) or by using the extent of an
          existing layer.
      band_index {Value Table}:
          Choose which bands to export for the layer. If no bands are specified, then all
          the bands will be used in the output.
      mosaic_method {String}:
          The mosaic method defines how the mosaic is created from different rasters.

          * SEAMLINE—Smooth transitions between images using seamlines.

          * NORTH_WEST—Display imagery that is closest to the northwest corner of the
          mosaic dataset boundary.

          * CLOSEST_TO_CENTER—Display imagery that is closest to the center of the screen.

          * LOCK_RASTER—Select specific raster datasets to display.

          * BY_ATTRIBUTE—Display and prioritize imagery based on a field in from the
          attribute table.

          * CLOSEST_TO_NADIR—Display the rasters with viewing angles closest to zero.

          * CLOSEST_TO_VIEWPOINT—Display imagery that is closest to a selected viewing
          angle.

          * NONE—Order rasters based on the ObjectID in the mosaic dataset attribute
          table.
      order_field {String}:
          The default field to use to order the rasters when the mosaic method is
          By_Attribute. The list of fields is defined as those in the service table that
          are of type metadata and are integer (for example, the values can represent
          dates or cloud cover percentage).
      order_base_value {String}:
          The images are sorted based on the difference between this input value and the
          attribute value in the specified field.
      lock_rasterid {String}:
          Raster ID or raster name to which the service should be locked, such that only
          the specified rasters are displayed. If left blank (undefined), it will be
          similar to the system default. Multiple IDs can be defined as a semicolon-
          delimited list.
      cell_size {Double}:
          The cell size for the output image service layer.
      where_clause {SQL Expression}:
          A query used to select a subset of items within an image service.
      processing_template {String}:
          Processing Template

     OUTPUTS:
      out_imageserver_layer (Raster Layer):
          The name of the output image layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeImageServerLayer_management(*gp_fixargs((in_image_service, out_imageserver_layer, template, band_index, mosaic_method, order_field, order_base_value, lock_rasterid, cell_size, where_clause, processing_template), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeLasDatasetLayer_management', None)
def MakeLasDatasetLayer(in_las_dataset=None, out_layer=None, class_code=None, return_values=None, no_flag=None, synthetic=None, keypoint=None, withheld=None, surface_constraints=None):
    """MakeLasDatasetLayer_management(in_las_dataset, out_layer, {class_code;class_code...}, {return_values;return_values...}, {no_flag}, {synthetic}, {keypoint}, {withheld}, {surface_constraints;surface_constraints...})

        Creates a LAS dataset layer that can apply filters to LAS points and control
        the enforcement of surface constraint features.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset to process.
      class_code {String}:
          Allows the filtering of LAS points by classification codes. The range of valid
          values will depend on the class codes supported by the version of LAS files
          referenced by the LAS dataset. All class codes will be selected by default.

          * 0—Never processed by a classification method.

          * 1—Processed by a classification method but could not be determined

          * 2—Bare earth measurements

          * 3—Vegetation whose height is considered to be low for the area

          * 4—Vegetation whose height is considered to be intermediate for the area

          * 5—Vegetation whose height is considered to be high for the area

          * 6—Structure with roof and walls

          * 7—Erroneous or undesirable data that is closer to the ground

          * 8—Reserved for later use, but used for model key points in LAS 1.1 - 1.3

          * 9—Water

          * 10—Railway tracks used by trains

          * 11—Road surfaces

          * 12—Reserved for later use, but used for overlap points in LAS 1.1 - 1.3

          * 13—Shielding around electrical wires

          * 14—Power lines

          * 15—A latice tower used to support an overhead power line

          * 16—A mechanical assembyl that joins an electrical circuit

          * 17—The surface of a bridge

          * 18—Erroneous or undesirable data that is far from the ground
      return_values {String}:
          Specifies the return values to be used for filtering LAS points. When nothing is
          specified, all returns are used.

          * Last Return

          * First of Many

          * Last of Many

          * Single Return

          * 1

          * 2

          * 3

          * 4

          * 5

          * 6

          * 7

          * 8
      no_flag {Boolean}:
          Indicates whether data points that do not have any classification flags
          assigned should be enabled for display and analysis.

          * INCLUDE_UNFLAGGED—Unflagged points will be displayed. This is the default.

          * EXCLUDE_UNFLAGGED—Unflagged points will not be displayed.
      synthetic {Boolean}:
          Indicates whether data points flagged as synthetic, or points that originated
          from a data source other than lidar, should be enabled for display and
          analysis..

          * INCLUDE_SYNTHETIC—Synthetic points will be displayed. This is the default.

          * EXCLUDE_SYNTHETIC—Synthetic points will not be displayed.
      keypoint {Boolean}:
          Indicates whether data points flagged as model key points, or significant
          measurements that should not be thinned away, should be enabled for display and
          analysis..

          * INCLUDE_KEYPOINT—Model key points will be displayed. This is the default.

          * EXCLUDE_KEYPOINT—Model key points will not be displayed.
      withheld {Boolean}:
          Indicates whether data points flagged as withheld, which typically represent
          unwanted noise measurements, should be enabled for display and analysis.

          * EXCLUDE_WITHHELD—Withheld points will not be displayed. This is the default.

          * INCLUDE_WITHHELD—Withheld points will be displayed.
      surface_constraints {String}:
          The name of the surface constraint features that will be enabled in the layer.
          All constraints are enabled by default.

     OUTPUTS:
      out_layer (LAS Dataset Layer):
          The name of the resulting LAS dataset layer. Any backslash or forward slash can
          be used to denote a group layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeLasDatasetLayer_management(*gp_fixargs((in_las_dataset, out_layer, class_code, return_values, no_flag, synthetic, keypoint, withheld, surface_constraints), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeMosaicLayer_management', None)
def MakeMosaicLayer(in_mosaic_dataset=None, out_mosaic_layer=None, where_clause=None, template=None, band_index=None, mosaic_method=None, order_field=None, order_base_value=None, lock_rasterid=None, sort_order=None, mosaic_operator=None, cell_size=None, processing_template=None):
    """MakeMosaicLayer_management(in_mosaic_dataset, out_mosaic_layer, {where_clause}, {template}, {band_index;band_index...}, {mosaic_method}, {order_field}, {order_base_value}, {lock_rasterid}, {sort_order}, {mosaic_operator}, {cell_size}, {processing_template})

        Creates a mosaic layer from an mosaic dataset or layer file. The layer that is
        created by the tool is temporary and will not persist after the session ends
        unless the layer is saved as a layer file or the map is saved.This tool can be
        used to make a layer so you can work with a specified subset of
        bands within a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The path and name of the input mosaic dataset.
      where_clause {SQL Expression}:
          A query statement using the fields and values of the mosaic dataset.
      template {Extent}:
          Using the min x, min y, max x, or max y, you can specify the extents of the
          output mosaic layer.
      band_index {Value Table}:
          Choose which bands to export for the layer. If no bands are specified, then all
          the bands will be used in the output.
      mosaic_method {String}:
          Choose the mosaic method. The mosaic method defines how the layer is created
          from different rasters within the mosaic dataset.

          * CLOSEST_TO_CENTER—Sorts rasters based on an order where rasters that have
          their center closest to the view center are placed on top.

          * NORTH_WEST—Sorts rasters based on an order where rasters that have their
          center closest to the northwest are placed on top.

          * LOCK_RASTER—Enables a user to lock the display of single or multiple rasters,
          based on an ID or name. When you choose this option, you need to specify the
          Lock Raster ID.

          * BY_ATTRIBUTE—Sorts rasters based on an attribute field and its difference from
          the base value. When this option is chosen, the order field and order base value
          parameters also need to be set.

          * CLOSEST_TO_NADIR—Sorts rasters based on an order where rasters that have their
          nadir position closest to the view center are placed on top. The nadir point can
          be different from the center point, especially in oblique imagery.

          * CLOSEST_TO_VIEWPOINT—Sorts rasters based on an order where the nadir position
          is closest to the user-defined viewpoint location and are placed on top.

          * SEAMLINE—Cuts the rasters using the predefined seamline shape for each raster
          using optional feathering along the seams. The ordering is predefined during
          seamline generation. The LAST mosaic operator is not valid with this mosaic
          method.
      order_field {String}:
          Choose the order field. When the mosaic method is BY_ATTRIBUTE, the default
          field to use when ordering rasters needs to be set. The list of fields is
          defined as those in the service table that are of type metadata.
      order_base_value {String}:
          The order base value. The images are sorted based on the difference between this
          value and the attribute value in the specified field.
      lock_rasterid {String}:
          The Raster ID or raster name to which the service should be locked and that only
          the specified rasters are displayed. If left undefined, it will be similar to
          system default. Multiple IDs can be defined as a semicolon-delimited list.
      sort_order {String}:
          Choose whether the sort order is ascending or descending.

          * ASCENDING—The sort order will be ascending. This is the default.

          * DESCENDING—The sort order will be descending.
      mosaic_operator {String}:
          Choose which mosaic operator to use. When two or more rasters all have the same
          sort priority, this parameter is used to further refine the sort order.

          * FIRST—The first raster in the list will be on top. This is the default.

          * LAST—The last raster in the list will be on top.

          * MIN—The raster with the lowest value will be on top.

          * MAX—The raster with the lowest value will be on top.

          * MEAN—The average pixel value will be on top.

          * BLEND—The output cell value will be a blend of values; this blend value relies
          on an algorithm that is weight based and dependent on the distance from the
          pixel to the edge within the overlapping area.
      cell_size {Double}:
          The cell size for the output mosaic layer.
      processing_template {String}:
          Processing Template

     OUTPUTS:
      out_mosaic_layer (Mosaic Layer):
          The name of the output mosaic layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeMosaicLayer_management(*gp_fixargs((in_mosaic_dataset, out_mosaic_layer, where_clause, template, band_index, mosaic_method, order_field, order_base_value, lock_rasterid, sort_order, mosaic_operator, cell_size, processing_template), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeQueryLayer_management', None)
def MakeQueryLayer(input_database=None, out_layer_name=None, query=None, oid_fields=None, shape_type=None, srid=None, spatial_reference=None):
    """MakeQueryLayer_management(input_database, out_layer_name, query, {oid_fields;oid_fields...}, {shape_type}, {srid}, {spatial_reference})

        Creates a query layer from a DBMS table based on an input SQL select statement.

     INPUTS:
      input_database (Workspace):
          The database connection file that contains the data to be queried.
      out_layer_name (String):
          Output name for the feature layer or table view to be created.
      query (String):
          SQL statement defining the select query to be issued to the database.
      oid_fields {String}:
          One or more fields from the SELECT statement SELECT list that can be used to
          generate a dynamic, unique row identifier.
      shape_type {String}:
          The shape type for the query layer. Only those records from the result set of
          the query that match the specified shape type will be used in the output query
          layer. Tool validation will attempt to set this property based on the first
          record in the result set. This can be changed before executing the tool if it is
          not the desired output shape type. This parameter is ignored if the result set
          of the query does not return a geometry field.

          * POINT—The output query layer will use point geometry.

          * MULTIPOINT—The output query layer will use multipoint geometry.

          * POLYGON—The output query layer will use polygon geometry.

          * POLYLINE—The output query layer will use polyline geometry.
      srid {String}:
          Sets the SRID (spatial reference identifier) value for queries that return
          geometry. Only those records from the result set of the query that match the
          specified SRID value will be used in the output query layer. Tool validation
          will attempt to set this property based on the first record in the result set.
          This can be changed before executing the tool if it is not the desired output
          SRID value. This parameter is ignored if the result set of the query does not
          return a geometry field.
      spatial_reference {Spatial Reference}:
          Sets the coordinate system that will be used by the output query layer. Tool
          validation will attempt to set this property based on the first record in the
          result set. This can be changed before executing the tool if it is not the
          desired output coordinate system. This parameter is ignored if the result set of
          the query does not return a geometry field."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeQueryLayer_management(*gp_fixargs((input_database, out_layer_name, query, oid_fields, shape_type, srid, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeQueryTable_management', None)
def MakeQueryTable(in_table=None, out_table=None, in_key_field_option=None, in_key_field=None, in_field=None, where_clause=None):
    """MakeQueryTable_management(in_table;in_table..., out_table, in_key_field_option, {in_key_field;in_key_field...}, {in_field;in_field...}, {where_clause})

        This tool applies an SQL query to a database and the results are represented in
        a layer or table view. The query can be used to join several tables or return a
        subset of columns or rows from the original data in the database.This tool
        accepts data from an ArcSDE geodatabase, a file geodatabase, a
        personal geodatabase, or an OLE DB connection.

     INPUTS:
      in_table (Table View / Raster Layer):
          The name of the table or tables to be used in the query. If several tables are
          listed, the Expression parameter can be used to define how they are to be
          joined.The input table can be from an ArcSDE geodatabase, a file geodatabase, a
          personal geodatabase, or an OLE DB connection.
      in_key_field_option (String):
          Indicates how an ObjectID field will be generated, if at all, for the query. The
          default is USE_KEY_FIELDS.

          * USE_KEY_FIELDS—This indicates that the fields chosen in the key fields list
          should be used to define the dynamic ObjectID column. If there are no fields
          chosen in the key fields list, the ADD VIRTUAL_KEY_FIELD option is automatically
          applied.

          * ADD_VIRTUAL_KEY_FIELD—This option indicates that no key fields have been
          chosen, but a dynamic ObjectID column is to be generated. This is done by
          copying the data to a local, system-managed workspace and adding a field with
          unique values to the copy. The layer or table view can then access the copy and
          use the added field as the key field.

          * NO_KEY_FIELD—This option indicates that no dynamic ObjectID column is to be
          generated. Choosing this option means that selections will not be supported for
          the table view. If there is already a column of type ObjectID in the fields
          list, it will be used as the ObjectID even if this option is chosen.
      in_key_field {Field}:
          Specifies a field or combination of fields that can be used to uniquely identify
          a row in the query. This parameter is used only when the USE_KEY_FIELDS option
          is set.The Add Field button, which is used only in ModelBuilder, allows you to
          add
          expected field(s) so you can complete the dialog and continue to build your
          model.
      in_field {Value Table}:
          The fields to include in the layer or table view. If an alias is set for a
          field, this is the name that appears. If no fields are specified, all fields
          from all tables are included.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS.

     OUTPUTS:
      out_table (Table View / Raster Layer):
          The name of the layer or table view that will be created by the tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeQueryTable_management(*gp_fixargs((in_table, out_table, in_key_field_option, in_key_field, in_field, where_clause), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeRasterCatalogLayer_management', None)
def MakeRasterCatalogLayer(in_raster_catalog=None, layer_name=None, where_clause=None, workspace=None, field_info=None):
    """MakeRasterCatalogLayer_management(in_raster_catalog, layer_name, {where_clause}, {workspace}, {field_info})

        Creates a raster catalog layer from an input raster catalog. The layer that is
        created by the tool is temporary and will not persist after the session ends
        unless the layer is saved to disk or the map document is saved.

     INPUTS:
      in_raster_catalog (Raster Catalog Layer):
          The raster catalog containing one or more raster catalog items (raster
          datasets).
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of raster catalog items.The syntax for
          the expression differs slightly depending on the data source. For
          example, if you're querying file or ArcSDE geodatabases, enclose field names in
          double quotes:"MY_FIELD"If you're querying personal geodatabases, enclose fields
          in square brackets:[MY_FIELD].
      workspace {Workspace}:
          The input workspace used to validate the field names. If the input is from a
          file or personal geodatabase and the output workspace is an ArcSDE geodatabase,
          the field names may be truncated, since some database fields can only have names
          with ten characters or less. The new names may be reviewed and altered using the
          Field Info parameter.
      field_info {Field Info}:
          Specifies which fields from the input table to rename and make visible in the
          output table view.

     OUTPUTS:
      layer_name (Raster Catalog Layer):
          Name of the temporary raster catalog layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeRasterCatalogLayer_management(*gp_fixargs((in_raster_catalog, layer_name, where_clause, workspace, field_info), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeRasterLayer_management', None)
def MakeRasterLayer(in_raster=None, out_rasterlayer=None, where_clause=None, envelope=None, band_index=None):
    """MakeRasterLayer_management(in_raster, out_rasterlayer, {where_clause}, {envelope}, {band_index;band_index...})

        Creates a raster layer from an input raster dataset or layer file. The layer
        that is created by the tool is temporary and will not persist after the session
        ends unless the layer is saved to disk or the map document is saved.This tool
        can be used to make a temporary layer, so you can work with a
        specified subset of bands within a raster dataset.

     INPUTS:
      in_raster (Composite Geodataset):
          The path and name of the input raster dataset.You can use a raster layer from a
          GeoPackage as the input. To reference a raster
          within a GeoPackage, type the name of the path, followed by the name of the
          GeoPackage and the name of the raster. For example,
          c:\data\sample.gpkg\raster_tile would be your input raster, where sample.gpkg is
          the name of the GeoPackage, and raster_tile is the raster dataset within the
          package.
      where_clause {SQL Expression}:
          A query statement using the fields and values of the raster dataset.
      envelope {Extent}:
          Specify the extent of the raster layer, using the minimum x, minimum y, maximum
          x, and maximum y.
      band_index {Value Table}:
          Choose which bands to export for the layer. If no bands are specified, then all
          the bands will be used in the output.

     OUTPUTS:
      out_rasterlayer (Raster Layer):
          The name of the layer to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeRasterLayer_management(*gp_fixargs((in_raster, out_rasterlayer, where_clause, envelope, band_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeTableView_management', None)
def MakeTableView(in_table=None, out_view=None, where_clause=None, workspace=None, field_info=None):
    """MakeTableView_management(in_table, out_view, {where_clause}, {workspace}, {field_info})

        Creates a table view from an input table or feature class. The table view that
        is created by the tool is temporary and will not persist after the session ends
        unless the document is saved.

     INPUTS:
      in_table (Table View / Raster Layer):
          The input table or feature class.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS.
      workspace {Workspace}:
          The input workspace used to validate the field names. If the input is a
          geodatabase table and the output workspace is a dBASE table, the field names may
          be truncated, since dBASE fields can only have names of ten characters or less.
          The new names may be reviewed and altered using the field information control.
      field_info {Field Info}:
          Specifies which fields from the input table to rename and make visible in the
          output table view.

     OUTPUTS:
      out_view (Table View / Raster Layer):
          The name of the table view to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeTableView_management(*gp_fixargs((in_table, out_view, where_clause, workspace, field_info), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeWCSLayer_management', None)
def MakeWCSLayer(in_wcs_coverage=None, out_wcs_layer=None, template=None, band_index=None):
    """MakeWCSLayer_management(in_wcs_coverage, out_wcs_layer, {template}, {band_index;band_index...})

        Creates a temporary raster layer from a WCS service.

     INPUTS:
      in_wcs_coverage (WCS Coverage / String):
          The name of the input WCS service, or the URL that references the WCS service.If
          a WCS server URL is used, the URL should include the coverage name and
          version information. If only URL is entered, the tool will automatically take
          the first coverage and use default version (1.0.0) to create the WCS layer.An
          example of a URL that includes the coverage name and version is below:http://Ser
          verName/arcgis/services/serviceName/ImageServer/WCSServer?coverage=ras
          terDRGs&version=1.1.1In this example,
          "http://ServerName/arcgis/services/serviceName/ImageServer/WCSServer?" is the
          URL. The coverage specified is "coverage=rasterDRGs", and the version is
          "&version=1.1.1".To get the coverage names on a WCS server, use the WCS
          GetCapabilities request.
          An example of WCS request is http://ServerName/arcgis/services/serviceName/Image
          Server/WCSServer?request=getcapabilities&service=wcs
      template {Extent}:
          The output extent of the WCS layer.The output extent can either be specified by
          defining the area to be clipped
          (X-Minimum, Y-Minimum, X-Maximum, and Y-Maximum) or by using the extent of an
          existing layer.
      band_index {Value Table}:
          Choose which bands to export for the layer. If no bands are specified, then all
          the bands will be used in the output.

     OUTPUTS:
      out_wcs_layer (Raster Layer):
          The name of the output WCS layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeWCSLayer_management(*gp_fixargs((in_wcs_coverage, out_wcs_layer, template, band_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeXYEventLayer_management', None)
def MakeXYEventLayer(table=None, in_x_field=None, in_y_field=None, out_layer=None, spatial_reference=None, in_z_field=None):
    """MakeXYEventLayer_management(table, in_x_field, in_y_field, out_layer, {spatial_reference}, {in_z_field})

        Creates a new point feature layer based on x- and y-coordinates defined in a
        source table. If the source table contains z-coordinates (elevation values),
        that field can also be specified in the creation of the event layer. The layer
        created by this tool is temporary.

     INPUTS:
      table (Table View):
          The table containing the X and Y coordinates that define the locations of the
          point features to create.
      in_x_field (Field):
          The field in the input table that contains the x-coordinates.
      in_y_field (Field):
          The field in the input table that contains the y-coordinates.
      spatial_reference {Spatial Reference}:
          The spatial reference of the coordinates in the X and Y Fields defined above.
          This will be the output event layer's spatial reference.
      in_z_field {Field}:
          The field in the input table that contains the z-coordinates.

     OUTPUTS:
      out_layer (Feature Layer):
          The name of the output point event layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeXYEventLayer_management(*gp_fixargs((table, in_x_field, in_y_field, out_layer, spatial_reference, in_z_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SaveToLayerFile_management', None)
def SaveToLayerFile(in_layer=None, out_layer=None, is_relative_path=None, version=None):
    """SaveToLayerFile_management(in_layer, out_layer, {is_relative_path}, {version})

        Creates an output layer file (.lyr) that references geographic data stored on
        disk.

     INPUTS:
      in_layer (Layer):
          The in-memory layer, layer file stored on disk, or feature layer in ArcMap to be
          saved to disk as a layer file (.lyr).
      is_relative_path {Boolean}:
          Determines if the output layer file (.lyr) will store a relative path to the
          source data stored on disk, or an absolute path.

          * ABSOLUTE—The output layer file will store an absolute path to the source data
          stored on disk. This is the default.

          * RELATIVE—The output layer file will store a relative path to the source data
          stored on disk. If the output layer file is moved, its source path will update
          to where the source data should be in relation to the new path.
      version {String}:
          The version of layer file the output will be saved as. The default is CURRENT.

          * CURRENT

          * 10.1

          * 10

          * 9.3

          * 9.2

          * 9.1

          * 9.0

          * 8.3

     OUTPUTS:
      out_layer (Layer File):
          The output layer file (.lyr) to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SaveToLayerFile_management(*gp_fixargs((in_layer, out_layer, is_relative_path, version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SelectLayerByAttribute_management', None)
def SelectLayerByAttribute(in_layer_or_view=None, selection_type=None, where_clause=None):
    """SelectLayerByAttribute_management(in_layer_or_view, {selection_type}, {where_clause})

        Adds, updates, or removes a selection on a layer or table view based on an
        attribute query.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The feature layer or table view to which the selection will be applied.The input
          can be a layer or table view in the ArcMap table of contents, or a
          layer or table view created in ArcCatalog or in scripts using the Make Feature
          Layer or Make Table View tools.
      selection_type {String}:
          Determines how the selection will be applied and what to do if a selection
          already exists.

          * NEW_SELECTION—The resulting selection replaces any existing selection. This is
          the default.

          * ADD_TO_SELECTION—The resulting selection is added to an existing selection if
          one exists. If no selection exists, this is the same as the NEW_SELECTION
          option.

          * REMOVE_FROM_SELECTION—The resulting selection is removed from an existing
          selection. If no selection exists, this option has no effect.

          * SUBSET_SELECTION—The resulting selection is combined with the existing
          selection. Only records that are common to both remain selected.

          * SWITCH_SELECTION—Switches the selection. All records that were selected are
          removed from the selection; all records that were not selected are added to the
          selection. The Expression is ignored when this option is specified.

          * CLEAR_SELECTION—Clears or removes any selection. The Expression is ignored
          when this option is specified.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records. For more information on
          SQL syntax see the help topic SQL reference for query expressions used in
          ArcGIS."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SelectLayerByAttribute_management(*gp_fixargs((in_layer_or_view, selection_type, where_clause), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SelectLayerByLocation_management', None)
def SelectLayerByLocation(in_layer=None, overlap_type=None, select_features=None, search_distance=None, selection_type=None, invert_spatial_relationship=None):
    """SelectLayerByLocation_management(in_layer, {overlap_type}, {select_features}, {search_distance}, {selection_type}, {invert_spatial_relationship})

        Selects features in a layer based on a spatial relationship to features in
        another layer.Each feature in the Input Feature Layer is evaluated against the
        features in the
        Selecting Features layer or feature class; if the specified Relationship is met,
        the input feature is selected.

     INPUTS:
      in_layer (Feature Layer / Raster Catalog Layer / Mosaic Layer):
          The layer containing the features that will be evaluated against the
          select_features. The selection will be applied to this layer.  The input cannot
          be the path to a feature class on disk.
      overlap_type {String}:
          The spatial relationship to be evaluated.

          * INTERSECT—The features in the input layer will be selected if they intersect a
          selecting feature. This is the default.

          * INTERSECT_3D —The features in the input layer will be selected if they
          intersect a selecting feature in three-dimensional space (x, y, and z).

          * WITHIN_A_DISTANCE—The features in the input layer will be selected if they are
          within a specified distance of a selecting feature. Specify a distance in the
          Search Distance parameter.

          * WITHIN_A_DISTANCE_3D—The features in the input layer will be selected if they
          are within a specified distance of a selecting feature in three-dimensional
          space. Specify a distance in the Search Distance parameter.

          * WITHIN_A_DISTANCE_GEODESIC—The features in the input layer will be selected if
          they are within a specified distance of a selecting feature. Distance between
          features will be calculated using a geodesic method which takes into account the
          curvature of the earth and correctly deals with data near and across the
          dateline and poles.

          * CONTAINS—The features in the input layer will be selected if they contain a
          selecting feature.

          * COMPLETELY_CONTAINS—The features in the input layer will be selected if they
          completely contain a selecting feature.

          * CONTAINS_CLEMENTINI—This spatial relationship yields the same results as
          COMPLETELY_CONTAINS with the following exception: if the selecting feature is
          entirely on the boundary of the input feature (no part is properly inside or
          outside), the feature will not be selected. Clementini defines the boundary
          polygon as the line separating inside and outside, the boundary of a line is
          defined as its end points, and the boundary of a point is always empty.

          * WITHIN—The features in the input layer will be selected if they are within a
          selecting feature.

          * COMPLETELY_WITHIN—The features in the input layer will be selected if they are
          completely within or contained by a selecting feature.

          * WITHIN_CLEMENTINI—The result will be identical to WITHIN with the exception
          that if the entirety of the feature in the input layer is on the boundary of the
          feature in the selecting layer, the feature will not be selected. Clementini
          defines the boundary polygon as the line separating inside and outside, the
          boundary of a line is defined as its end points, and the boundary of a point is
          always empty.

          * ARE_IDENTICAL_TO—The features in the input layer will be selected if they are
          identical (in geometry) to a selecting feature.

          * BOUNDARY_TOUCHES—The features in the input layer will be selected if they have
          a boundary that touches a selecting feature. When the inputs features are lines
          or polygons, the boundary of the input feature can only touch the boundary of
          the selecting feature, and no part of the input feature can cross the boundary
          of the selecting feature.

          * SHARE_A_LINE_SEGMENT_WITH—The features in the input layer will be selected if
          they share a line segment with a selecting feature. The input and selecting
          features must be line or polygon.

          * CROSSED_BY_THE_OUTLINE_OF—The features in the input layer will be selected if
          they are crossed by the outline of a selecting feature. The input and selecting
          features must be lines or polygons. If polygons are used for the input or
          selecting layer, the polygon's boundary (line) will be used. Lines that cross at
          a point will be selected, not lines that share a line segment.

          * HAVE_THEIR_CENTER_IN—The features in the input layer will be selected if their
          center falls within a selecting feature. The center of the feature is calculated
          as follows: for polygon and multipoint, the geometry's centroid is used, and for
          line input, the geometry's midpoint is used.
      select_features {Feature Layer}:
          The features in the input feature layer will be selected based on their
          relationship to the features from this layer or feature class.
      search_distance {Linear unit}:
          This parameter is only valid if the overlap_type parameter is set to one of the
          following: WITHIN_A_DISTANCE_GEODESIC, WITHIN_A_DISTANCE, WITHIN_A_DISTANCE_3D,
          INTERSECT, INTERSECT_3D, HAVE_THEIR_CENTER_IN, CONTAINS, or WITHIN.If the
          WITHIN_A_DISTANCE_GEODESIC option is used, a linear unit such as
          Kilometers or Miles should be used.
      selection_type {String}:
          Determines how the selection will be applied to the input and how to combine
          with an existing selection. Note that there is no option here to clear an
          existing selection. To clear a selection, use the CLEAR_SELECTION option on the
          Select Layer By Attribute tool.

          * NEW_SELECTION—The resulting selection replaces any existing selection. This is
          the default.

          * ADD_TO_SELECTION—The resulting selection is added to an existing selection, if
          one exists. If no selection exists, this is the same as the NEW_SELECTION
          option.

          * REMOVE_FROM_SELECTION—The resulting selection is removed from an existing
          selection. If no selection exists, the operation will have no effect.

          * SUBSET_SELECTION—The resulting selection is combined with the existing
          selection. Only records that are common to both remain selected.

          * SWITCH_SELECTION—Switches the selection. All records that were selected are
          removed from the selection, and all records that were not selected are added to
          the selection. The select_features and overlap_type parameters are ignored when
          this option is selected.
      invert_spatial_relationship {Boolean}:
          After the spatial relationship is evaluated, this option determines if the
          result should be used as is, or inverted. For example, this option can be used
          to quickly get a list of features that do not intersect or are not within a
          distance of features in another dataset.

          * NOT_INVERT—The result of the query will not be inverted. This is the default.

          * INVERT—The result of the query will be inverted. If a selection_type option is
          used, the inversion occurs before the selection is combined with existing
          selections."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SelectLayerByLocation_management(*gp_fixargs((in_layer, overlap_type, select_features, search_distance, selection_type, invert_spatial_relationship), True)))
        return retval
    except Exception, e:
        raise e


# Package toolset
@gptooldoc('ConsolidateLayer_management', None)
def ConsolidateLayer(in_layer=None, output_folder=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None, schema_only=None):
    """ConsolidateLayer_management(in_layer;in_layer..., output_folder, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only})

        Consolidates one or more layers by copying all referenced data sources into a
        single folder.

     INPUTS:
      in_layer (Layer):
          The input layers to be consolidated.
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.
      schema_only {Boolean}:
          Specifies whether only the schema of the input layers will be consolidated or
          packaged.

          * ALL — All features and records will be consolidated or packaged. This is the
          default.

          * SCHEMA_ONLY— Only the Schema of input layers will be consolidated or packaged.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the layer files and consolidated data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConsolidateLayer_management(*gp_fixargs((in_layer, output_folder, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConsolidateLocator_management', None)
def ConsolidateLocator(in_locator=None, output_folder=None, copy_arcsde_locator=None):
    """ConsolidateLocator_management(in_locator, output_folder, {copy_arcsde_locator})

        Consolidate a locator or composite locator by copying all locators into a
        single folder.

     INPUTS:
      in_locator (Address Locator):
          The input locator or composite locator that will be consolidated.
      copy_arcsde_locator {Boolean}:
          Specifies whether participating locators will be copied or their connection
          information will be preserved in the composite locator. This option only applies
          to composite locators.

          * COPY_ARCSDE—All participating locators, including locators in ArcSDE, will be
          copied to the consolidated folder or package. This is the default.

          * PRESERVE_ARCSDE— Connection information of the participating locators that are
          stored in ArcSDE will be preserved in the composite locator.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the locator or composite locator with its
          participating locators."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConsolidateLocator_management(*gp_fixargs((in_locator, output_folder, copy_arcsde_locator), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConsolidateMap_management', None)
def ConsolidateMap(in_map=None, output_folder=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None):
    """ConsolidateMap_management(in_map, output_folder, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde})

        Consolidates a map and all referenced data sources to a specified output
        folder.

     INPUTS:
      in_map (ArcMap Document):
          The map document (.mxd) to be consolidated.
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated map and data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConsolidateMap_management(*gp_fixargs((in_map, output_folder, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConsolidateResult_management', None)
def ConsolidateResult(in_result=None, output_folder=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None, schema_only=None):
    """ConsolidateResult_management(in_result;in_result..., output_folder, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only})

        Consolidates one or more geoprocessing results into a specified output folder.
        If the specified folder does not exist, a new folder will be created.

     INPUTS:
      in_result (File / String):
          The geoprocessing result to be consolidated.Results that are added as input can
          either be a result file (.rlt) or a result
          from the Results window.
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.
      schema_only {Boolean}:
          Specifies whether only the schema of input and output datasets will be
          consolidated or packaged.

          * ALL — All records for input and output datasets will be consolidated or
          packaged. This is the default.

          * SCHEMA_ONLY— Only the Schema of input and output datasets will be consolidated
          pr packaged.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated tools and data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConsolidateResult_management(*gp_fixargs((in_result, output_folder, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateMapTilePackage_management', None)
def CreateMapTilePackage(in_map=None, service_type=None, output_file=None, format_type=None, level_of_detail=None, service_file=None, summary=None, tags=None):
    """CreateMapTilePackage_management(in_map, service_type, output_file, format_type, level_of_detail, {service_file}, {summary}, {tags})

        Generates tiles from a map or basemap and packages the tiles to create a single
        compressed .tpk file.

     INPUTS:
      in_map (ArcMap Document):
          The map document from which tiles will be generated and packaged.
      service_type (Boolean):
          Determines whether the tiling scheme will be generated from an existing map
          service or if map tiles will be generated for ArcGIS Online, Bing maps, and
          Google Maps.

          * EXISTING —Tiling scheme from an existing map service will be used. You must
          specify a map service in the service_file parameter.Choose this option if your
          organization has created a tiling scheme for an existing service on your server
          and you want to match it. Matching tiling schemes ensures that your tiles will
          overlay correctly in your ArcGIS Runtime application.If you choose this option,
          your source map document should use the same coordinate system as the map whose
          tiling scheme you are importing.

          * ONLINE —The ArcGIS Online/Bing Maps/Google Maps tiling scheme is used. This is
          the default.The ArcGIS Online/Bing Maps/Google Maps tiling scheme allows you to
          overlay your cache tiles with tiles from these online mapping services. ArcGIS
          for Desktop includes this tiling scheme as a built-in option when loading a
          tiling scheme. When you choose this tiling scheme, the data frame of your source
          map document must use the WGS 1984 Web Mercator (Auxiliary Sphere) projected
          coordinate system.The ArcGIS Online/Bing Maps/Google Maps tiling scheme is
          required if you'll be overlaying your package with ArcGIS Online, Bing Maps, or
          Google Maps. One advantage of the ArcGIS Online/Bing Maps/Google Maps tiling
          scheme is that it is widely known in the web mapping world, so your tiles will
          match those of other organizations that have used this tiling scheme. Even if
          you don't plan to overlay any of these well-known map services, you may choose
          the tiling scheme for its interoperability potential.The ArcGIS Online/Bing
          Maps/Google Maps tiling scheme may contain scales that would be zoomed in too
          far to be of use to your map. Packaging for large scales can take up much time
          and disk storage space. For example, the largest scale in the tiling scheme is
          about 1:1,000. Packaging the entire continental United States at this scale can
          take weeks and require hundreds of gigabytes of storage. If you aren't prepared
          to package at this scale level, you should remove this scale level when you
          create the tile package.
      format_type (String):
          Specifies the format of the generated tiles.

          * PNG—Use PNG to automatically select the correct format (PNG 8, PNG 24, or PNG
          32) based on the specified Level of Detail. This is the default.

          * PNG8—Use PNG 8 for overlay services that need to have a transparent
          background, such as roads and boundaries. PNG 8 creates tiles of very small size
          on disk with no loss of information. Do not use PNG 8 if your map contains more
          than 256 colors. Imagery, hillshades, gradient fills, transparency, and
          antialiasing can easily push your map over 256 colors. Even symbols such as
          highway shields may have subtle antialiasing around the edges that unexpectedly
          adds colors to your map.

          * PNG24—You can use PNG 24 for overlay services, such as roads and boundaries,
          that have more than 256 colors (if fewer than 256 colors, use PNG 8).

          * PNG32—Use PNG 32 for overlay services, such as roads and boundaries, that have
          more than 256 colors. PNG 32 is an especially good choice for overlay services
          that have antialiasing enabled on lines or text. PNG 32 creates larger tiles on
          disk than PNG 24, but the tiles are fully supported in all browsers.

          * JPEG—Use this format for basemap services that have large color variation and
          do not need to have a transparent background. For example, raster imagery and
          very detailed vector basemaps tend to work well with JPEG. JPEG is a lossy image
          format. It attempts to selectively remove data without affecting the appearance
          of the image. This can cause very small tile sizes on disk, but if your map
          contains vector linework or labels, it may produce too much noise or blurry area
          around the lines. If this is the case, you can attempt to raise the compression
          value from the default of 75. A higher value, such as 90, may balance an
          acceptable quality of linework with the small tile size benefit of the JPEG.It's
          up to you to decide what image quality you consider acceptable. If you are
          willing to accept a minor amount of noise in the images, you may save large
          amounts of disk space by choosing JPEG. The smaller tile size also means the
          application can download the tiles faster.

          * MIXED—A mixed package uses JPEG in the center of the package with PNG 32 on
          the edge of the package. Use the mixed mode when you want to cleanly overlay
          raster packages on other layers.When a mixed package is created, PNG 32 tiles
          are created anywhere that transparency is detected (in other words, anywhere
          that the data frame background is visible). The rest of the tiles are built
          using JPEG. This keeps the average file size down while providing you with a
          clean overlay on top of other packages. If you do not use the mixed mode package
          in this scenario, you will see a nontransparent collar around the periphery of
          your image where it overlaps the other package.
      level_of_detail (Long):
          Specify the number of scale levels at which tiles will be generated for the
          package. Possible values are 1 through 20.
      service_file {MapServer / File}:
          Specifies the name of the map service or the XML files to use for the tiling
          scheme. This parameter is required only when the  service_type parameter is
          EXISTING.
      summary {String}:
          Adds summary information to the properties of the package.
      tags {String}:
          Adds tag information to the properties of the package. Multiple tags can be
          added separated by a comma or semicolon.

     OUTPUTS:
      output_file (File):
          The output map tile package."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateMapTilePackage_management(*gp_fixargs((in_map, service_type, output_file, format_type, level_of_detail, service_file, summary, tags), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRuntimeContent_management', None)
def CreateRuntimeContent(in_map=None, output_folder=None, in_basemap=None, in_locator=None, extent=None, options=None, optimize=None, service_type=None, format_type=None, level_of_detail=None, service_file=None):
    """CreateRuntimeContent_management(in_map, output_folder, {in_basemap}, {in_locator}, {extent}, {options;options...}, {optimize}, service_type, format_type, level_of_detail, {service_file})

        Consolidates feature layers, basemaps, network datasets, and locators from your
        map document into a single folder and prepares the folder for use within
        applications built with ArcGIS Runtime SDKs. This folder can then be provisioned
        to devices to use with applications that run offline (applications that can run
        disconnected from ArcGIS Server or ArcGIS Online).

     INPUTS:
      in_map (ArcMap Document):
          The input map document (.mxd) that will be consolidated into a single folder.
      in_basemap {String}:
          Input basemap layer that will be included in the Runtime content.Esri-provided
          basemaps such as Imagery, Streets, Topographic, and so on, are not
          supported.
      in_locator {Address Locator}:
          Input locator (.loc) that will be included in the Runtime content.There are a
          few restrictions on which locators can be added to the Runtime content:

          * The locator must be created with ArcGIS 10.0 or later.

          *  The locator cannot have an unknown coordinate system.

          *  The locator or any participating locator in a composite locator cannot be a
          geocoding service, including services from Portal for ArcGIS or ArcGIS Online.

          *  The locator cannot contain a custom plug-in in the locator style
          configuration.
          Only one locator can be added to your runtime content. Create a composite
          locator if you want to include multiple locators.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      options {String}:
          Options for determining which layers will be included in the Runtime content.

          * NETWORK_DATA— Use this option to include all network data that resides within
          your map document.

          * FEATURE_AND_TABULAR_DATA—Use this option to include all simple features,
          tables, and relationship classes that reside within your map document.
           If your map contains a network dataset or a network analysis layer, you have
          the option of including the network dataset in your Runtime content as a
          transportation network. When including a network, all feature layers the network
          references become part of the Runtime content. This may include layers that are
          not part of the map. For example, if you only have a network dataset layer in
          the map, your runtime content includes the streets, junctions, and turns feature
          classes associated with the network. For a network dataset to become a
          transportation network, there are a few
          restrictions to keep in mind:

          * The network dataset must be part of a geodatabase. This excludes networks that
          are in SDC or shapefile format.

          * The network dataset must be from ArcGIS 10.0 or later. If your network is from
          an earlier version, you can upgrade your geodatabase and your network.

          * The network dataset cannot have an unknown coordinate system.

          *  The network dataset cannot use any VB or Python script evaluators.

          *  The network dataset cannot use any custom COM evaluators.

          *  A network dataset that uses live traffic will be ported to a transportation
          network, but the live traffic components are excluded since they are not
          supported.
          When using Python, multiple values can be entered by using a Python list, for
          example, ["NETWORK_DATA", "FEATURE_AND_TABULAR_DATA"].
      optimize {Boolean}:
          Optimizes the Runtime content by reducing its size for portability to mobile
          devices.

          * OPTIMIZE_SIZE—Runtime content will be optimized for size. This is the default.

          * NON_OPTIMIZE_SIZE—Runtime content will not be optimized for size.
          Optimization includes deleting all fields that are not used in renderers,
          relates, or joins. OBECTID, SHAPE, and GlobalIDs are always maintained.
          Additionally, optimize will set the precision of the of the spatial reference to
          0.1 meters.
      service_type (Boolean):
          Determines whether the tiling scheme will be generated from an existing map
          service or if map tiles will be generated for ArcGIS Online, Bing Maps, and
          Google Maps.

          * EXISTING —Tiling scheme from an existing map service will be used. You must
          specify a map service in the service_file parameter.Choose this option if your
          organization has created a tiling scheme for an existing service on your server
          and you want to match it. Matching tiling schemes ensures that your tiles will
          overlay correctly in your ArcGIS Runtime application.If you choose this option,
          your source map document should use the same coordinate system as the map whose
          tiling scheme you are importing.

          * ONLINE —The ArcGIS Online/Bing Maps/Google Maps tiling scheme is used. This is
          the default.The ArcGIS Online/Bing Maps/Google Maps tiling scheme allows you to
          overlay your cache tiles with tiles from these online mapping services. ArcGIS
          for Desktop includes this tiling scheme as a built-in option when loading a
          tiling scheme. When you choose this tiling scheme, the data frame of your source
          map document must use the WGS 1984 Web Mercator (Auxiliary Sphere) projected
          coordinate system.The ArcGIS Online/Bing Maps/Google Maps tiling scheme is
          required if you'll be overlaying your package with ArcGIS Online, Bing Maps, or
          Google Maps. One advantage of the ArcGIS Online/Bing Maps/Google Maps tiling
          scheme is that it is widely known in the web mapping world, so your tiles will
          match those of other organizations that have used this tiling scheme. Even if
          you don't plan to overlay any of these well-known map services, you may choose
          the tiling scheme for its interoperability potential.The ArcGIS Online/Bing
          Maps/Google Maps tiling scheme may contain scales that would be zoomed in too
          far to be of use to your map. Packaging for large scales can take up much time
          and disk storage space. For example, the largest scale in the tiling scheme is
          about 1:1,000. Packaging the entire continental United States at this scale can
          take weeks and require hundreds of gigabytes of storage. If you aren't prepared
          to package at this scale level, you should remove this scale level when you
          create the tile package.
      format_type (String):
          Specifies the format of the generated tiles.

          * PNG—Use PNG to automatically select the correct format (PNG8, PNG24, or PNG32)
          based on the specified Level of Detail. This is the default.

          * PNG8—Use PNG 8 for overlay services that need to have a transparent
          background, such as roads and boundaries. PNG 8 creates tiles of very small size
          on disk with no loss of information. Do not use PNG 8 if your map contains more
          than 256 colors. Imagery, hillshades, gradient fills, transparency, and
          antialiasing can easily push your map over 256 colors. Even symbols such as
          highway shields may have subtle antialiasing around the edges that unexpectedly
          adds colors to your map.

          * PNG24—You can use PNG 24 for overlay services, such as roads and boundaries,
          that have more than 256 colors (if fewer than 256 colors, use PNG 8).

          * PNG32—Use PNG 32 for overlay services, such as roads and boundaries, that have
          more than 256 colors. PNG 32 is an especially good choice for overlay services
          that have antialiasing enabled on lines or text. PNG 32 creates larger tiles on
          disk than PNG 24, but the tiles are fully supported in all browsers.

          * JPEG—Use this format for basemap services that have large color variation and
          do not need to have a transparent background; for example, raster imagery and
          very detailed vector basemaps tend to work well with JPEG. JPEG is a lossy image
          format. It attempts to selectively remove data without affecting the appearance
          of the image. This can cause very small tile sizes on disk, but if your map
          contains vector line work or labels, it may produce too much noise or blurry
          area around the lines. If this is the case, you can attempt to raise the
          compression value from the default of 75. A higher value, such as 90, may
          balance an acceptable quality of line work with the small tile size benefit of
          the JPEG.It's up to you to decide what image quality you consider acceptable. If
          you are willing to accept a minor amount of noise in the images, you may save
          large amounts of disk space by choosing JPEG. The smaller tile size also means
          the application can download the tiles faster.

          * MIXED—A mixed package uses JPEG in the center of the package with PNG 32 on
          the edge of the package. Use the mixed mode when you want to cleanly overlay
          raster packages on other layers.When a mixed package is created, PNG 32 tiles
          are created anywhere that transparency is detected (in other words, anywhere
          that the data frame background is visible). The rest of the tiles are built
          using JPEG. This keeps the average file size down while providing you with a
          clean overlay on top of other packages. If you do not use the mixed mode package
          in this scenario, you will see a nontransparent collar around the periphery of
          your image where it overlaps the other package.
      level_of_detail (Long):
          Specify the number of scale levels at which tiles will be generated for the
          package. Possible values are 1 through 20.
      service_file {MapServer / File}:
          Specifies the name of the map service or the XML files to use for the tiling
          scheme. This parameter is required only when the  service_type parameter is
          EXISTING.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated data. This folder can then
          be deployed to mobile devices to be used within ArcGIS Runtime-based
          applications.The output folder and its Runtime content is not intended to be
          used outside of
          a Runtime application."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRuntimeContent_management(*gp_fixargs((in_map, output_folder, in_basemap, in_locator, extent, options, optimize, service_type, format_type, level_of_detail, service_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExtractPackage_management', None)
def ExtractPackage(in_package=None, output_folder=None):
    """ExtractPackage_management(in_package, output_folder)

        Extracts the contents of a package to a specified folder.  The output folder
        will be updated with the extracted contents of the input package.

     INPUTS:
      in_package (File):
          The input package that will be extracted.

     OUTPUTS:
      output_folder (Folder):
          The output folder to contain the contents of the package."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExtractPackage_management(*gp_fixargs((in_package, output_folder), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PackageLayer_management', None)
def PackageLayer(in_layer=None, output_file=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None, schema_only=None, version=None, additional_files=None, summary=None, tags=None):
    """PackageLayer_management(in_layer;in_layer..., output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only}, {version;version...}, {additional_files;additional_files...}, {summary}, {tags})

        Packages one or more layers and all referenced data sources to create a single
        compressed .lpk file.

     INPUTS:
      in_layer (Layer):
          The layers to package.
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.
      schema_only {Boolean}:
          Specifies whether only the schema of the input layers will be consolidated or
          packaged.

          * ALL — All features and records will be consolidated or packaged. This is the
          default.

          * SCHEMA_ONLY— Only the Schema of input layers will be consolidated or packaged.
      version {String}:
          Specifies the version of the geodatabases that will be created in the resulting
          package. Specifying a version allows packages to be shared with previous
          versions and supports backward compatibility.

          * ALL —         Package will contain  geodatabases and layer files compatible
          with all versions. (9.3.1 and higher)

          * CURRENT—      Package will contain geodatabases and layer files compatible
          with the version of the current release.

          * 10.3— Package will contain geodatabases and layer files compatible with
          version 10.3.

          * 10.1— Package will contain geodatabases and layer files compatible with
          version 10.1.

          * 10— Package will contain geodatabases and layer files compatible with version
          10.0.

          * 9.3.1—Pacakge will contain geodatabases and layer files compatible with
          version 9.3.1.
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
          The location and name of the output package file (.lpk) to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PackageLayer_management(*gp_fixargs((in_layer, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only, version, additional_files, summary, tags), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PackageLocator_management', None)
def PackageLocator(in_locator=None, output_file=None, copy_arcsde_locator=None, additional_files=None, summary=None, tags=None):
    """PackageLocator_management(in_locator, output_file, {copy_arcsde_locator}, {additional_files;additional_files...}, {summary}, {tags})

        Package a locator or composite locator to create a single compressed .gcpk
        file.

     INPUTS:
      in_locator (Address Locator):
          The locator or composite locator that will be packaged.
      copy_arcsde_locator {Boolean}:
          Specifies whether participating locators will be copied or their connection
          information will be preserved in the composite locator. This option only applies
          to composite locators.

          * COPY_ARCSDE—All participating locators, including locators in ArcSDE, will be
          copied to the consolidated folder or package. This is the default.

          * PRESERVE_ARCSDE— Connection information of the participating locators that are
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
        retval = convertArcObjectToPythonObject(gp.PackageLocator_management(*gp_fixargs((in_locator, output_file, copy_arcsde_locator, additional_files, summary, tags), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PackageMap_management', None)
def PackageMap(in_map=None, output_file=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None, arcgisruntime=None, reference_all_data=None, version=None, additional_files=None, summary=None, tags=None):
    """PackageMap_management(in_map, output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {arcgisruntime}, {reference_all_data}, {version;version...}, {additional_files;additional_files...}, {summary}, {tags})

        Packages a map document and all referenced data sources to create a single
        compressed .mpk file.

     INPUTS:
      in_map (ArcMap Document):
          The map document to be packaged.
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.
      arcgisruntime {Boolean}:
          Specifies whether the package will support ArcGIS Runtime.  To support ArcGIS
          Runtime, all data sources will be converted to a file geodatabase and a .msd
          will be created in the output package.

          * DESKTOP—Output package will not support ArcGIS Runtime. Unless otherwise
          specified, data sources will not be converted to a file geodatabase and a .msd
          will not be created.

          * RUNTIME— Output package will support ArcGIS Runtime.  All data sources will be
          converted to a file geodatabase and a .msd will be created in the output
          package.
      reference_all_data {Boolean}:
          Setting this option to REFERENCED will create a package that references the
          data needed rather than copying the data. This is valuable when trying to
          package large datasets that are available from a central location within an
          organization.

          * REFERENCED—Creates a package that references the data rather than copying the
          data.

          * NOT_REFERENCED—       Creates a package that contains all needed data. This is
          the default.
      version {String}:
          Specifies the version of the geodatabases that will be created in the resulting
          package. Specifying a version allows packages to be shared with previous
          versions of ArcGIS and supports backward compatibility.

          * ALL —         Package will contain geodatabases and a map document compatible
          with all versions. (10.0 and higher)

          * CURRENT—      Package will contain geodatabases and a map document compatible
          with the version of the current release.

          * 10.3—Package will contain geodatabases and a map document compatible with
          version 10.3.

          * 10.2—Package will contain geodatabases and a map document compatible with
          version 10.2.

          * 10.1—Package will contain geodatabases and a map document compatible with
          version 10.1.

          * 10—Package will contain geodatabases and a map document compatible with
          version 10.0.
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
          The output map package (.mpk)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PackageMap_management(*gp_fixargs((in_map, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, arcgisruntime, reference_all_data, version, additional_files, summary, tags), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PackageResult_management', None)
def PackageResult(in_result=None, output_file=None, convert_data=None, convert_arcsde_data=None, extent=None, apply_extent_to_arcsde=None, schema_only=None, arcgisruntime=None, additional_files=None, summary=None, tags=None, version=None):
    """PackageResult_management(in_result;in_result..., output_file, {convert_data}, {convert_arcsde_data}, {extent}, {apply_extent_to_arcsde}, {schema_only}, {arcgisruntime}, {additional_files;additional_files...}, {summary}, {tags}, {version;version...})

        Packages one or more geoprocessing results, including all tools and input and
        output datasets, into a single compressed file (.gpk).

     INPUTS:
      in_result (File / String):
          The result that will be packaged.The input can be either a result added by
          dragging and dropping directly from
          the Results window or by browsing to a result file (.rlt).
      convert_data {Boolean}:
          Specifies whether input layers will be converted into a file geodatabase or
          preserve their original format.

          * CONVERT — Data will be converted to a file geodatabase.  This parameter does
          not apply to enterprise geodatabase data sources. To convert
          enterprise geodatabase data, set convert_arcsde_data to CONVERT_ARCSDE.

          * PRESERVE —Data formats will be preserved when possible.  This is the default.
          The exception to this rule are formats that are not supported in a 64x
          environment (personal geodatabase (.mdb) data, VPF data, and tables based on
          Excel spreadsheets or OLEDB connections) and raster formats that ArcGIS cannot
          write out natively (ADRG, CADRG/ECRG, CIB, and RPF).
      convert_arcsde_data {Boolean}:
          Specifies whether input enterprise geodatabase layers will be converted into a
          file geodatabase or preserve their original format.

          * CONVERT_ARCSDE— Enterprise geodatabase data will be converted to a file
          geodatabase and included in the consolidated folder or package. This is the
          default.

          * PRESERVE_ARCSDE— Enterprise geodatabase data will be preserved and will be
          referenced in the consolidated folder or package.
      extent {Extent}:
          Specify the extent by manually entering the coordinates in the extent parameter
          using the format X-Min Y-Min X-Max Y-Max. To use the extent of a specific layer,
          specify the layer name.

          * MAXOF—Union of inputs

          * MINOF—Intersection of inputs

          * DISPLAY—Same extent as current display

          * <Layer>—Same extent as specified layer
      apply_extent_to_arcsde {Boolean}:
          Determines whether specified extent will be applied to all layers or only to
          enterprise geodatabase layers.

          * ALL — Specified extent is applied to all layers. This is the default.

          * ARCSDE_ONLY —Specified extent is applied to enterprise geodatabase layers
          only.
      schema_only {Boolean}:
          Specifies whether only the schema of input and output datasets will be
          consolidated or packaged.

          * ALL— All records for input and output datasets will be consolidated or
          packaged. This is the default.

          * SCHEMA_ONLY— Only the schema of input and output datasets will be consolidated
          or packaged.
      arcgisruntime {Boolean}:
          Specifies whether the package will support ArcGIS Runtime.  To support ArcGIS
          Runtime, all data sources will be converted to a file geodatabase and a Map
          Service Definition file (.msd) will be created in the package.

          * DESKTOP—Output package will not support ArcGIS Runtime.

          * RUNTIME— Output package will support ArcGIS Runtime.
      additional_files {File}:
          Adds additional files to a package. Additional files, such as .doc, .txt, .pdf,
          and so on, are used to provide more information about the contents and purpose
          of the package.
      summary {String}:
          Adds Summary information to the properties of the package.
      tags {String}:
          Adds Tag information to the properties of the package. Multiple tags can be
          added or separated by a comma or semicolon.
      version {String}:
          Specifies the version of the geodatabases that will be created in the resulting
          package. Specifying a version allows packages to be shared with previous
          versions of ArcGIS and supports backward compatibility.

          * ALL —         Package will contain geodatabases and a map document compatible
          with all versions. (10.0 and higher)

          * CURRENT—      Package will contain geodatabases and a map document compatible
          with the version of the current release.

          * 10.3—Package will contain geodatabases and a map document compatible with
          version 10.3.

          * 10.2—Package will contain geodatabases and a map document compatible with
          version 10.2.

          * 10.1—Package will contain geodatabases and a map document compatible with
          version 10.1.

          * 10—Package will contain geodatabases and a map document compatible with
          version 10.0.

     OUTPUTS:
      output_file (File):
          The name and location of the output package file (.gpk)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PackageResult_management(*gp_fixargs((in_result, output_file, convert_data, convert_arcsde_data, extent, apply_extent_to_arcsde, schema_only, arcgisruntime, additional_files, summary, tags, version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SharePackage_management', None)
def SharePackage(in_package=None, username=None, password=None, summary=None, tags=None, credits=None, public=None, groups=None):
    """SharePackage_management(in_package, username, password, summary, tags, {credits}, {public}, {groups;groups...})

        Shares a package by uploading to ArcGIS online. Signing in to ArcGIS Online or
        Portal for ArcGIS through ArcGIS for Desktop
        changed in the ArcGIS for Desktop 10.2 release. You must sign in to ArcGIS
        Online or Portal by clicking File                        Sign In before
        launching the tool, if you see <Not signed into ArcGIS.com> in the Username
        parameter. See Signing in to ArcGIS Online in ArcGIS for Desktop applications
        for more information.

     INPUTS:
      in_package (File):
          Input layer (.lpk), map (.mpk), geoprocessing (.gpk), map tile (.tpk), or
          address locator (.gcpk) package file.
      username (String):
          Esri Global Account user name. This parameter will have limited use from a
          Python script when sharing a package to a portal that uses OAUTH2
          authentication. See the usage notes for more information.
      password (Encrypted String):
          Esri Global Account password. This parameter will have limited use from a
          Python script when sharing a package to a portal that uses OAUTH2
          authentication. See the usage notes for more information.
      summary (String):
          Summary of package. The summary is displayed in the item information of the
          package on ArcGIS.com.
      tags (String):
          Tags used to describe and identify the package. Individual tags are separated
          using either a comma or semicolon.
      credits {String}:
          Credits for the package. This is generally the name of the organization that is
          given credit for authoring and providing the content for the package.
      public {Boolean}:
          Specifies whether input package will be shared and available to everybody.

          * EVERYBODY — Package will be shared with everybody.

          * MYGROUPS— Package will be shared with  package owner and any selected group.
          This is the default.
      groups {String}:
          List of groups to share package with."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SharePackage_management(*gp_fixargs((in_package, username, password, summary, tags, credits, public, groups), True)))
        return retval
    except Exception, e:
        raise e


# Photos toolset
@gptooldoc('GeoTaggedPhotosToPoints_management', None)
def GeoTaggedPhotosToPoints(Input_Folder=None, Output_Feature_Class=None, Invalid_Photos_Table=None, Include_Non_GeoTagged_Photos=None, Add_Photos_As_Attachments=None):
    """GeoTaggedPhotosToPoints_management(Input_Folder, Output_Feature_Class, {Invalid_Photos_Table}, {Include_Non_GeoTagged_Photos}, {Add_Photos_As_Attachments})

        Creates points from the x-, y-, and z-coordinates stored in geotagged photos.
        Optionally adds photo files to features in the output feature class as
        geodatabase attachments.

     INPUTS:
      Input_Folder (Folder):
          The folder where photo files are located. This folder is scanned recursively
          for photo files; any photos in the base level of the folder, as well as in any
          subfolders, will be added to the output.
      Include_Non-GeoTagged_Photos {Boolean}:
          Specifies if all photo files should be added as records to the output feature
          class or only those with valid GPS coordinates.

          * ALL_PHOTOS— All photo files will be added as records to the output feature
          class. If a photo file does not have GPS coordinate information, it will be
          added as a record with null geometry. This is the default.

          * ONLY_GEOTAGGED— Only photo files with valid GPS coordinate information will
          have records in the output feature class.
      Add_Photos_As_Attachments {Boolean}:
          Specifies if photo files will be added to the output feature class as
          geodatabase attachments. Adding attachments requires at minimum an ArcGIS for
          Desktop Standard license,
          and the output feature class must be in a version 10 or higher geodatabase.

          * ADD_ATTACHMENTS— Photo files will be added to the output feature class records
          as geodatabase attachments. Geodatabase attachments are copied internally to the
          geodatabase. This is the default.

          * NO_ATTACHMENTS— Photo files will not be added to the output feature class
          records as geodatabase attachments.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output point feature class.
      Invalid_Photos_Table {Table}:
          The optional output table that will list any photo files in the input folder
          with invalid Exif metadata or empty GPS coordinates.If no path is specified,
          this table will not be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeoTaggedPhotosToPoints_management(*gp_fixargs((Input_Folder, Output_Feature_Class, Invalid_Photos_Table, Include_Non_GeoTagged_Photos, Add_Photos_As_Attachments), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MatchPhotosToRowsByTime_management', None)
def MatchPhotosToRowsByTime(Input_Folder=None, Input_Table=None, Time_Field=None, Output_Table=None, Unmatched_Photos_Table=None, Add_Photos_As_Attachments=None, Time_Tolerance=None, Clock_Offset=None):
    """MatchPhotosToRowsByTime_management(Input_Folder, Input_Table, Time_Field, Output_Table, {Unmatched_Photos_Table}, {Add_Photos_As_Attachments}, {Time_Tolerance}, {Clock_Offset})

        Matches photo files to table or feature class rows according to the photo and
        row time stamps. The row with the time stamp closest to the capture time of a
        photo will be matched to that photo. Creates a new table containing the
        ObjectIDs from the input rows and their matching photo paths. Optionally adds
        matching photo files to the rows of the input table as geodatabase attachments.

     INPUTS:
      Input_Folder (Folder):
          The folder where photo files are located. This folder is scanned recursively
          for photo files; any photos in the base level of the folder, as well as in any
          subfolders, will be added to the output.
      Input_Table (Table View):
          The table or feature class whose rows will be matched with photo files. The
          input table will typically be a point feature class representing GPS recordings.
      Time_Field (Field):
          The date/time field from the input table that indicates when each row was
          captured or created. Must be a date field; cannot be a string or numeric field.
      Add_Photos_As_Attachments {Boolean}:
          Specifies if photo files will be added to the rows of the input table as
          geodatabase attachments. Adding attachments requires at minimum an ArcGIS for
          Desktop Standard license,
          and the output feature class must be in a version 10 or higher geodatabase.

          * ADD_ATTACHMENTS— Photo files will be added to the rows of the input table as
          geodatabase attachments. Geodatabase attachments are copied internally to the
          geodatabase. This is the default.

          * NO_ATTACHMENTS— Photo files will not be added to the rows of the input table
          as geodatabase attachments.
      Time_Tolerance {Double}:
          The maximum difference (in seconds) between the date/time of an input row and
          a photo file that will be matched. If an input row and a photo file have time
          stamps that are different by more than this tolerance, no match will occur. To
          match a photo file to a row with the closest time stamp, regardless of how large
          the date/time difference might be, set the tolerance to 0. The sign of this
          value (- or +) is irrelevant; the absolute value of the number specified will be
          used.Do not use this parameter to adjust for consistent shifts or offsets
          between the
          times recorded by the GPS and the digital camera. Use the Clock Offset
          parameter, or the Convert Time Zone tool to shift the time stamps of the input
          rows to match those of the photos.
      Clock_Offset {Double}:
          The difference (in seconds) between the internal clock of the digital camera
          used to capture the photos and the GPS unit. If the clock of the digital camera
          is behind the clock of the GPS unit, use a positive value; if the clock of the
          digital camera is ahead of the clock of the GPS unit, use a negative value.For
          example, if a photo with a time stamp of 11:35:17 should match a row with a
          time stamp of 11:35:32, use a Clock Offset of 15.

     OUTPUTS:
      Output_Table (Table):
          The output table containing the OBJECTIDs from the input table that match a
          photo, and the matching photo path. Only OBJECTIDs from the input table that are
          found to match a photo are included in the output table.
      Unmatched_Photos_Table {Table}:
          The optional output table that will list any photo files in the input folder
          with an invalid time stamp or any photos that cannot be matched because there is
          no input row within the time tolerance.If no path is specified, this table will
          not be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MatchPhotosToRowsByTime_management(*gp_fixargs((Input_Folder, Input_Table, Time_Field, Output_Table, Unmatched_Photos_Table, Add_Photos_As_Attachments, Time_Tolerance, Clock_Offset), True)))
        return retval
    except Exception, e:
        raise e


# Projections and Transformations toolset
@gptooldoc('BatchProject_management', None)
def BatchProject(Input_Feature_Class_or_Dataset=None, Output_Workspace=None, Output_Coordinate_System=None, Template_dataset=None, Transformation=None):
    """BatchProject_management(Input_Feature_Class_or_Dataset;Input_Feature_Class_or_Dataset..., Output_Workspace, {Output_Coordinate_System}, {Template_dataset}, {Transformation})

        Changes the coordinate system of a set of input feature classes or feature
        datasets to a common coordinate system. To change the coordinate system of a
        single feature class or dataset use the Project tool.

     INPUTS:
      Input_Feature_Class_or_Dataset (Geodataset):
          The input feature classes or feature datasets whose coordinates are to be
          converted.
      Output_Workspace (Workspace / Feature Dataset):
          The location of each new output feature class or feature dataset.
      Output_Coordinate_System {Coordinate System}:
          The coordinate system to be used to project the inputs. Valid values are a
          Spatial Reference object, a file with a .prj extension, or a
          string representation of a coordinate system.
      Template_dataset {Geodataset}:
          The feature class or the feature dataset used to specify the output coordinate
          system used for projection.
      Transformation {String}:
          Name of the geographic transformation to be applied to convert data between two
          geographic coordinate systems (datums)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BatchProject_management(*gp_fixargs((Input_Feature_Class_or_Dataset, Output_Workspace, Output_Coordinate_System, Template_dataset, Transformation), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConvertCoordinateNotation_management', None)
def ConvertCoordinateNotation(in_table=None, out_featureclass=None, x_field=None, y_field=None, input_coordinate_format=None, output_coordinate_format=None, id_field=None, spatial_reference=None, in_coor_system=None):
    """ConvertCoordinateNotation_management(in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, {id_field}, {spatial_reference}, {in_coor_system})

        Converts coordinate notations contained on one or two fields from one notation
        format to another.

     INPUTS:
      in_table (Table View):
          The table containing the fields with coordinate notations to convert.
      x_field (Field):
          A field from the input table containing the longitude value. For DD_2,
          DD_NUMERIC, DDM_2, and DMS_2, this is the longitude field.For DD_1, DDM_1, and
          DMS_1, this field contains both latitude and longitude
          values in a single string.For GARS, GEOREF, UTM_ZONES, UTM_BANDS, USNG, and
          MGRS, this field contains an
          alphanumeric system of notation in a single text field.The y_field parameter is
          ignored when one of the single-string formats is
          chosen.
      y_field (Field):
          A field from the input table containing the latitude value. For DD_2,
          DD_NUMERIC, DDM_2, and DMS_2, this is the longitude field.For DD_1, DDM_1, and
          DMS_1, this field contains both latitude and longitude
          values in a single string.For GARS, GEOREF, UTM_ZONES, UTM_BANDS, USNG, and
          MGRS, this field contains an
          alphanumeric system of notation in a single text field.This parameter is ignored
          when one of the single-string formats is chosen.
      input_coordinate_format (String):
          Coordinate format of the input fields. The default is DD_2.

          * DD_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DD_2—Longitude and latitude values are in two separate fields.

          * DDM_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DDM_2— Longitude and latitude values are in two separate fields.

          * DMS_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DMS_2—Longitude and latitude values are in two separate fields.

          * GARS—Global Area Reference System. Based on latitude and longitude, it divides
          and subdivides the world into cells.

          * GEOREF—World Geographic Reference System. A grid-based system that divides the
          world into 15-degree quadrangles and then subdivides into smaller quadrangles.

          * UTM_ZONES—The letter N or S after the UTM zone number designates only North or
          South hemisphere.

          * UTM_BANDS—The letter after the UTM zone number designates one of the 20
          latitude bands. N or S does not designate a hemisphere.

          * USNG—United States National Grid. Almost exactly the same as MGRS but uses
          North American Datum 1983 (NAD83) as its datum.

          * MGRS—Military Grid Reference System. Follows the UTM coordinates and divides
          the world into 6-degree longitude and 20 latitude bands, but MGRS then further
          subdivides the grid zones into smaller 100,000-meter grids. These 100,000-meter
          grids are then divided into 10,000-meter, 1,000-meter, 100-meter, 10-meter, and
          1-meter grids.

          * SHAPE—Only available when a point feature layer is selected as input. The
          coordinates of each point are used to define the output format.
          DD, DDM, DMS, and UTM are also valid keywords; they can be used just by typing
          in (on dialog) or passing the value in scripting. However, keywords with
          underscore and a qualifier tell more about the field values.
      output_coordinate_format (String):
          Coordinate format to which the input notations will be converted. The default
          is DD_2.

          * DD_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DD_2—Longitude and latitude values are in two separate fields.

          * DD_NUMERIC—Longitude and latitude values are in two separate fields of type
          Double. Values in the West and South are denoted by a minus sign, whereas in
          DD_2, the values are in text and N, S, E, and W are used to denote direction.

          * DDM_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DDM_2— Longitude and latitude values are in two separate fields.

          * DMS_1—Both longitude and latitude values are in a single field. Two values are
          separated by a space, a comma, or a slash.

          * DMS_2—Longitude and latitude values are in two separate fields.

          * GARS—Global Area Reference System. Based on latitude and longitude, it divides
          and subdivides the world into cells.

          * GEOREF—World Geographic Reference System. A grid-based system that divides the
          world into 15-degree quadrangles and then subdivides into smaller quadrangles.

          * UTM_ZONES—The letter N or S after the UTM zone number designates only North or
          South hemisphere.

          * UTM_BANDS—The letter after the UTM zone number designates one of the 20
          latitude bands. N or S does not designate a hemisphere.

          * USNG—United States National Grid. Almost exactly the same as MGRS but uses
          North American Datum 1983 (NAD83) as its datum.

          * MGRS—Military Grid Reference System. Follows the UTM coordinates and divides
          the world into 6-degree longitude and 20 latitude bands, but MGRS then further
          subdivides the grid zones into smaller 100,000-meter grids. These 100,000-meter
          grids are then divided into 10,000-meter, 1,000-meter, 100-meter, 10-meter, and
          1-meter grids.
          DD, DDM, DMS, and UTM are also valid keywords; they can be used just by typing
          in (on dialog) or passing the value in scripting. However, keywords with
          underscore and a qualifier tell more about the field values.
      id_field {Field}:
          This parameter is ignored as all nonsystem fields are transferred to output
          table.
      spatial_reference {Spatial Reference}:
          Spatial reference of the output feature class. The default is GCS_WGS_1984.The
          tool projects the output to the spatial reference specified. If the input
          and output coordinate systems are in a different datum, then a default
          transformation is used based on the coordinate systems of the input and the
          output and the extent of the data.
      in_coor_system {Coordinate System}:
          Spatial reference of the input data. If the input spatial reference cannot be
          obtained from the input table, the default of GCS_WGS_1984 is used.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class of points. The attribute table will contain all fields
          of the input table along with the fields containing converted values in the
          output format."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConvertCoordinateNotation_management(*gp_fixargs((in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, id_field, spatial_reference, in_coor_system), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateCustomGeoTransformation_management', None)
def CreateCustomGeoTransformation(geot_name=None, in_coor_system=None, out_coor_system=None, custom_geot=None):
    """CreateCustomGeoTransformation_management(geot_name, in_coor_system, out_coor_system, custom_geot)

        Creates a transformation method for converting data between two geographic
        coordinate systems or datums. The output of this tool can be used as a
        transformation method for any tool with a parameter that requires a geographic
        transformation.

     INPUTS:
      geot_name (String):
          Name of the custom transformation method. All custom geographic transformation
          files are saved with a .gtf extension and
          stored in the ESRI\<ArcGIS product>\ArcToolbox\CustomTransformations folder
          under the user's Application Data folder. The CustomTransformations folder is
          created by the tool if it does not exist. If the Application Data folder is
          read-only or hidden, the output is created in ArcToolbox\CustomTransformations
          under the user's temp folder. The location or name of the Application Data and
          temp folders is dependent on the operating system.

          * In any Windows operating system the Application Data folder is located at
          %appdata% and the user's Temp folder is located at %temp%. Entering%appdata% in
          a command window it will return the AppData file location. Entering %temp% will
          return the temp folder location.

          * In Unix systems, the tmp and Application Data folders are located in the
          user's home directory, under $HOME and $TMP, respectively. Typing /tmp in a
          terminal will return the location.
      in_coor_system (Coordinate System):
          The starting geographic coordinate system.
      custom_geot (String):
          Set the METHOD and PARAMETER values wrapped in a string for custom
          transformation GEOGTRAN. Set the name of the method from the available methods
          of Geocentric_Translation, Molodensky, Molodensky_Abridged, Position_Vector,
          Coordinate_Frame, Molodensky_Badekas, NADCON, HARN, NTV2, Longitude_Rotation,
          Unit_Change, and Geographic_2D_Offset. Each method has its own sets of
          parameters—you can edit the values of the parameters by entering text next to
          the name of the parameter within the whole string representation of the custom
          geographic transformation. See examples in the Python sample below.

     OUTPUTS:
      out_coor_system (Coordinate System):
          The final geographic coordinate system."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateCustomGeoTransformation_management(*gp_fixargs((geot_name, in_coor_system, out_coor_system, custom_geot), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateSpatialReference_management', None)
def CreateSpatialReference(spatial_reference=None, spatial_reference_template=None, xy_domain=None, z_domain=None, m_domain=None, template=None, expand_ratio=None):
    """CreateSpatialReference_management({spatial_reference}, {spatial_reference_template}, {xy_domain}, {z_domain}, {m_domain}, {template;template...}, {expand_ratio})

        Creates a spatial reference object for use in ModelBuilder.Use the
        SpatialReference class to create a spatial reference object to use in a
        script.

     INPUTS:
      spatial_reference {Spatial Reference}:
          Name of the the spatial reference object to be created.
      spatial_reference_template {Feature Layer / Raster Dataset / Raster Catalog Layer}:
          The feature class or layer to be used as a template to set the value for the
          spatial reference.
      xy_domain {Envelope}:
          Allowable coordinate range for x,y coordinates.
      z_domain {String}:
          Allowable coordinate range for z values.
      m_domain {String}:
          Allowable coordinate range for m values.
      template {Feature Layer}:
          Feature classes or layers that can be used to define the XY Domain.
      expand_ratio {Double}:
          Percentage by which the XY Domain will be expanded."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateSpatialReference_management(*gp_fixargs((spatial_reference, spatial_reference_template, xy_domain, z_domain, m_domain, template, expand_ratio), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DefineProjection_management', None)
def DefineProjection(in_dataset=None, coor_system=None):
    """DefineProjection_management(in_dataset, coor_system)

        This tool overwrites the coordinate system information (map projection and
        datum) stored with a dataset. The only use for this tool is for datsets that
        have an unknown or incorrect coordinate system defined.All geographic datasets
        have a coordinate system that is used throughout ArcGIS
        to display, measure, and transform geographic data. If the coordinate system for
        a dataset is unknown or incorrect, you can use this tool to specify the correct
        coordinate system.  You must know the correct coordinate system of the dataset
        before using this tool.

     INPUTS:
      in_dataset (Feature Layer / Geodataset):
          Dataset or feature class whose projection is to be defined.
      coor_system (Coordinate System):
          Valid values are a Spatial Reference object, a file with a .prj extension, or a
          string representation of a coordinate system."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DefineProjection_management(*gp_fixargs((in_dataset, coor_system), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Project_management', None)
def Project(in_dataset=None, out_dataset=None, out_coor_system=None, transform_method=None, in_coor_system=None, preserve_shape=None, max_deviation=None):
    """Project_management(in_dataset, out_dataset, out_coor_system, {transform_method;transform_method...}, {in_coor_system}, {preserve_shape}, {max_deviation})

        Projects spatial data from one coordinate system to another.

     INPUTS:
      in_dataset (Feature Layer / Feature Dataset):
          The feature class, feature layer, or feature dataset to be projected.
      out_coor_system (Coordinate System):
          Valid values are a Spatial Reference object, a file with a .prj extension, or a
          string representation of a coordinate system.
      transform_method {String}:
          This method can be used for converting data between two geographic coordinate
          systems or datums. This optional parameter may be required if the input and
          output coordinate systems have different datum.Transformations are bi-
          directional. For example, if converting data from WGS
          1984 to NAD 1927, you can pick a transformation called NAD_1927_to_WGS_1984_3,
          and the tool will apply it correctly. If no transformation is provided, a
          default transformation is used. This default transformation is suitable for
          general mapping applications but may not be suitable for applications that
          require precise locational accuracy.
      in_coor_system {Coordinate System}:
          The coordinate system of the input feature class or dataset. When the input has
          an unknown, or unspecified, coordinate system, this allows you to specify the
          data's coordinate system without having to modify the input data (which may not
          be possible if the input is in read-only format).
      preserve_shape {Boolean}:
          Adds vertices to the output lines or polygons so their projected shape is more
          accurate.

          * NO_PRESERVE_SHAPE—Does not add extra vertices to the output lines or polygons.
          This is the default.

          * PRESERVE_SHAPE—Adds extra vertices to the output lines or polygons, as needed,
          so their projected shape is more accurate.
      max_deviation {Linear unit}:
          Determines how far a projected line or polygon can deviate from its exact
          projected location when preserve_shape = "PRESERVE_SHAPE".   The default is 100
          times the XY tolerance of the spatial reference of the output dataset.

     OUTPUTS:
      out_dataset (Feature Class / Feature Dataset):
          The output dataset to which the results will be written."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Project_management(*gp_fixargs((in_dataset, out_dataset, out_coor_system, transform_method, in_coor_system, preserve_shape, max_deviation), True)))
        return retval
    except Exception, e:
        raise e


# Projections and Transformations\Raster toolset
@gptooldoc('Flip_management', None)
def Flip(in_raster=None, out_raster=None):
    """Flip_management(in_raster, out_raster)

        Reorients the raster by turning it over, from top to bottom, along the
        horizontal axis through the center of the raster. This may be useful to correct
        raster datasets that are upside down.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          Input raster dataset.

     OUTPUTS:
      out_raster (Raster Dataset):
          Output raster dataset.When storing the raster dataset in a file format, you need
          to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Flip_management(*gp_fixargs((in_raster, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Mirror_management', None)
def Mirror(in_raster=None, out_raster=None):
    """Mirror_management(in_raster, out_raster)

        Reorients the raster by flipping it, from left to right, along the vertical axis
        through the center of the raster.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          Input raster dataset.

     OUTPUTS:
      out_raster (Raster Dataset):
          Output raster dataset.When storing the raster dataset in a file format, you need
          to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Mirror_management(*gp_fixargs((in_raster, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ProjectRaster_management', None)
def ProjectRaster(in_raster=None, out_raster=None, out_coor_system=None, resampling_type=None, cell_size=None, geographic_transform=None, Registration_Point=None, in_coor_system=None):
    """ProjectRaster_management(in_raster, out_raster, out_coor_system, {resampling_type}, {cell_size}, {geographic_transform;geographic_transform...}, {Registration_Point}, {in_coor_system})

        Transforms the raster dataset from one projection to another.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster dataset.
      out_coor_system (Coordinate System):
          The coordinate system to which the input raster will be projected. The default
          value is set based on the Output Coordinate System environment setting.Valid
          values for this parameter are

          * A file with the .prj extension.

          * An existing feature class, feature dataset, raster catalog (basically anything
          with a coordinate system).

          * The string representation of a coordinate system. These lengthy strings can be
          generated by adding a coordinate system variable to ModelBuilder, setting the
          variable's value as desired, then exporting the model to a Python script.
      resampling_type {String}:
          The resampling algorithm to be used. The default is NEAREST.

          * NEAREST— The fastest resampling method; it minimizes changes to pixel values.
          Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY— Determines the value of each pixel based on the most popular value
          within a 3 by 3 window. Suitable for discrete data.
          The NEAREST and MAJORITY options are used for categorical data, such as a land-
          use classification. The NEAREST option is the default since it is the quickest
          and also because it will not change the cell values. Do not use either of these
          for continuous data, such as elevation surfaces.The BILINEAR option and the
          CUBIC option are most appropriate for continuous
          data. It is not recommended that either of these be used with categorical data
          because the cell values may be altered.
      cell_size {Cell Size XY}:
          The cell size for the new raster dataset.The default cell size is the cell size
          of the selected raster dataset.
      geographic_transform {String}:
          The transformation method used between two geographic systems or datums.The
          geographic transformation is optional when the input and output coordinate
          systems have the same datum. If the input and output datum are different, a
          geographic transformation needs to be specified.For information on each
          supported geographic (datum) transformations, see the
          geographic_transformations.pdf file to be found in the \Documentation folder of
          your ArcGIS installation.
      Registration_Point {Point}:
          The x and y coordinates (in the output space) used for pixel alignment.The
          registration point works similar to the concept of snap raster. Instead of
          snapping the output to an existing raster cell alignment, the registration point
          allows you to specify the origin point for anchoring the output cells. All
          output cells will be an interval of the cell size away from this point. This
          point does not have to be a corner coordinate or fall within the raster
          dataset.The Snap Raster environment setting will take priority over the
          Registration_Point parameter. Therefore, if you want to set the registration
          point, make sure that Snap Raster is not set.
      in_coor_system {Coordinate System}:
          The coordinate system of the input raster dataset.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset to be created.When storing the raster dataset in a
          file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ProjectRaster_management(*gp_fixargs((in_raster, out_raster, out_coor_system, resampling_type, cell_size, geographic_transform, Registration_Point, in_coor_system), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RegisterRaster_management', None)
def RegisterRaster(in_raster=None, register_mode=None, reference_raster=None, input_link_file=None, transformation_type=None, output_cpt_link_file=None, maximum_rms_value=None):
    """RegisterRaster_management(in_raster, register_mode, {reference_raster}, {input_link_file}, {transformation_type}, {output_cpt_link_file}, {maximum_rms_value})

        Automatically aligns a raster to a reference image or use control points. If the
        input dataset is a mosaic dataset, the tool will operate on each mosaic dataset
        item. To automatically register the image, the input raster and the reference
        raster must be in a relatively close geographic area. The tool will run faster
        if the raster datasets are closer to lining up. You may need to create a link
        file with a few links to get your input raster into the same map space.

     INPUTS:
      in_raster (Raster Dataset / Raster Layer / Mosaic Layer):
          The raster that you want to realign. Registering a mosaic dataset item will
          update that particular item within the mosaic dataset.A mosaic dataset item will
          have the path to the mosaic dataset followed by the
          Object ID of the item. For instance, the first item in the mosaic dataset would
          have the following path: .\mosaicDataset\objectid=1.
      register_mode (String):
          Choose the registration mode. You can either register the raster with a
          transformation, or you can reset the transformation.

          * REGISTER—Apply a geometric transformation to the input raster.

          * REGISTER_MS—Register the multispectral input to the panchromatic input. This
          is only used for mosaic datasets that have a misalignment between the two.

          * RESET— Remove the geometric transformation previously added by this tool.

          * CREATE_LINKS—Create a link file with automatically generated links.
      reference_raster {Raster Layer / Raster Dataset / Image Service / MapServer / WMS Map / Mosaic Layer / Internet Tiled Layer / Map Server Layer}:
          Choose the raster dataset that will align the input raster dataset. Leave this
          parameter empty if you want to register your multispectral mosaic dataset items
          to their associated panchromatic raster datasets.
      input_link_file {Text File}:
          The file that has the coordinates to link the input raster dataset with the
          reference. The input link table works with one mosaic item in the mosaic layer.
          The input must specify which item is being processed, either selecting the item
          or specifying the ObjectID in the input. Leave this parameter empty to register
          multispectral mosaic dataset items with the associated panchromatic raster
          datasets.
      transformation_type {String}:
          The method for shifting the raster dataset.

          * POLYORDER0— Uses a zero-order polynomial to shift your data. This is commonly
          used when your data is already georeferenced, but a small shift will better line
          up your data. Only one link is required to perform a zero-order polynomial
          shift.

          * POLYORDER1—A first-order polynomial (affine) fits a flat plane to the input
          points.

          * POLYORDER2—A second-order polynomial fits a somewhat more complicated surface
          to the input points.

          * POLYORDER3—A third-order polynomial fits a more complicated surface to the
          input points.

          * ADJUST— Combines a polynomial transformation and uses a triangulated irregular
          network (TIN) interpolation technique to optimize for both global and local
          accuracy.

          * SPLINE— Transforms the source control points precisely to the target control
          points. In the output, the control points will be accurate, but the raster
          pixels between the control points are not.

          * PROJECTIVE— Warps lines so they remain straight. In doing so, lines that were
          once parallel may no longer remain parallel. The projective transformation is
          especially useful for oblique imagery, scanned maps, and for some imagery
          products.
      maximum_rms_value {Double}:
          Set the amount of modeled error (in pixels) that you want in the output. The
          default is 0.5, and values below 0.3 are not recommended as this leads to
          overfitting.

     OUTPUTS:
      output_cpt_link_file {Text File}:
          If specified, a text file will be written containing the links created by this
          tool. This file can be used in the Warp From File tool. The output link table
          works with one mosaic dataset item in the mosaic layer. The input must specify
          which item is being processed, either selecting the item or specifying the
          ObjectID in the input."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RegisterRaster_management(*gp_fixargs((in_raster, register_mode, reference_raster, input_link_file, transformation_type, output_cpt_link_file, maximum_rms_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Rescale_management', None)
def Rescale(in_raster=None, out_raster=None, x_scale=None, y_scale=None):
    """Rescale_management(in_raster, out_raster, x_scale, y_scale)

        Resizes a raster by the specified x and y scale factors.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster.
      x_scale (Double):
          The factor in which to scale the cell size in the x direction.The factor must be
          greater than zero.
      y_scale (Double):
          The factor in which to scale the cell size in the y direction.The factor must be
          greater than zero.

     OUTPUTS:
      out_raster (Raster Dataset):
          Output raster dataset.When storing the raster dataset in a file format, you need
          to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Rescale_management(*gp_fixargs((in_raster, out_raster, x_scale, y_scale), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Rotate_management', None)
def Rotate(in_raster=None, out_raster=None, angle=None, pivot_point=None, resampling_type=None):
    """Rotate_management(in_raster, out_raster, angle, {pivot_point}, {resampling_type})

        Turn a raster dataset around a pivot point.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          Select the raster dataset to rotate.
      angle (Double):
          Specify a value between 0 and 360 degrees to rotate the raster by that amount
          in the clockwise direction. To rotate the raster in the counterclockwise
          direction, specify the angle as a negative value. The angle can be specified as
          an integer or a floating-point value.
      pivot_point {Point}:
          Select a point to rotate the raster around. If left blank, the lower left corner
          of the input raster dataset will serve as the pivot.
      resampling_type {String}:
          The resampling algorithm to be used. The default is NEAREST.

          * NEAREST— The fastest resampling method; it minimizes changes to pixel values.
          Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY— Determines the value of each pixel based on the most popular value
          within a 3 by 3 window. Suitable for discrete data.
          The NEAREST and MAJORITY options are used for categorical data, such as a land-
          use classification. The NEAREST option is the default since it is the quickest
          and also because it will not change the cell values. Do not use either of these
          for continuous data, such as elevation surfaces.The BILINEAR option and the
          CUBIC option are most appropriate for continuous
          data. It is not recommended that either of these be used with categorical data
          because the cell values may be altered.

     OUTPUTS:
      out_raster (Raster Dataset):
          Specify a name, location, and format for the dataset you are creating. When
          storing a raster dataset in a geodatabase, do not add a file extension to the
          name of the raster dataset. When storing your raster dataset to a JPEG file, a
          JPEG 2000 file, a TIFF file, or a geodatabase, you can specify a compression
          type and compression quality.When storing the raster dataset in a file format,
          you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Rotate_management(*gp_fixargs((in_raster, out_raster, angle, pivot_point, resampling_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Shift_management', None)
def Shift(in_raster=None, out_raster=None, x_value=None, y_value=None, in_snap_raster=None):
    """Shift_management(in_raster, out_raster, x_value, y_value, {in_snap_raster})

        Moves (slides) the raster to a new geographic location, based on x and y shift
        values. This tool is helpful if your raster dataset needs to be shifted to align
        with another data file.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The input raster dataset.
      x_value (Double):
          The value used to shift the x coordinates.
      y_value (Double):
          The value used to shift the y coordinates.
      in_snap_raster {Raster Layer}:
          The raster dataset used to align the cells of the output raster dataset.

     OUTPUTS:
      out_raster (Raster Dataset):
          Output raster dataset.When storing the raster dataset in a file format, you need
          to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Shift_management(*gp_fixargs((in_raster, out_raster, x_value, y_value, in_snap_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Warp_management', None)
def Warp(in_raster=None, source_control_points=None, target_control_points=None, out_raster=None, transformation_type=None, resampling_type=None):
    """Warp_management(in_raster, source_control_points;source_control_points..., target_control_points;target_control_points..., out_raster, {transformation_type}, {resampling_type})

        Transform a raster dataset using source and target control points. This is
        similar to georeferencing.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster that you want to transform.
      source_control_points (Point):
          The source points are the "from" coordinates of the links.
      target_control_points (Point):
          The target points are the "to" coordinates of the links.
      transformation_type {String}:
          Select a method for shifting the raster dataset.

          * POLYORDER0— Uses a zero-order polynomial to shift your data. This is commonly
          used when your data is already georeferenced, but a small shift will better line
          up your data. Only one link is required to perform a zero-order polynomial
          shift.

          * POLYORDER1—A first-order polynomial (affine) fits a flat plane to the input
          points.

          * POLYORDER2—A second-order polynomial fits a somewhat more complicated surface
          to the input points.

          * POLYORDER3—A third-order polynomial fits a more complicated surface to the
          input points.

          * ADJUST— Combines a polynomial transformation and uses a triangulated irregular
          network (TIN) interpolation technique to optimize for both global and local
          accuracy.

          * SPLINE— Transforms the source control points precisely to the target control
          points. In the output, the control points will be accurate, but the raster
          pixels between the control points are not.

          * PROJECTIVE— Warps lines so they remain straight. In doing so, lines that were
          once parallel may no longer remain parallel. The projective transformation is
          especially useful for oblique imagery, scanned maps, and for some imagery
          products.
      resampling_type {String}:
          The resampling algorithm to be used. The default is NEAREST.

          * NEAREST— The fastest resampling method; it minimizes changes to pixel values.
          Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY— Determines the value of each pixel based on the most popular value
          within a 3 by 3 window. Suitable for discrete data.
          The NEAREST and MAJORITY options are used for categorical data, such as a land-
          use classification. The NEAREST option is the default since it is the quickest
          and also because it will not change the cell values. Do not use either of these
          for continuous data, such as elevation surfaces.The BILINEAR option and the
          CUBIC option are most appropriate for continuous
          data. It is not recommended that either of these be used with categorical data
          because the cell values may be altered.

     OUTPUTS:
      out_raster (Raster Dataset):
          Specify a name, location and format for the dataset you are creating. When
          storing a raster dataset in a geodatabase, do not add a file extension to the
          name of the raster dataset. When storing your raster dataset to a JPEG file, a
          JPEG 2000 file, a TIFF file, or a geodatabase, you can specify a compression
          type and compression quality.When storing the raster dataset in a file format,
          you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Warp_management(*gp_fixargs((in_raster, source_control_points, target_control_points, out_raster, transformation_type, resampling_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('WarpFromFile_management', None)
def WarpFromFile(in_raster=None, out_raster=None, link_file=None, transformation_type=None, resampling_type=None):
    """WarpFromFile_management(in_raster, out_raster, link_file, {transformation_type}, {resampling_type})

        Transforms a raster dataset using a file containing source and target control
        points.

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The raster that you want to transform.
      link_file (Text File):
          The file containing the coordinates to warp the input raster.
      transformation_type {String}:
          Select a method for shifting the raster dataset.

          * POLYORDER0— Uses a zero-order polynomial to shift your data. This is commonly
          used when your data is already georeferenced, but a small shift will better line
          up your data. Only one link is required to perform a zero-order polynomial
          shift.

          * POLYORDER1—A first-order polynomial (affine) fits a flat plane to the input
          points.

          * POLYORDER2—A second-order polynomial fits a somewhat more complicated surface
          to the input points.

          * POLYORDER3—A third-order polynomial fits a more complicated surface to the
          input points.

          * ADJUST— Combines a polynomial transformation and uses a triangulated irregular
          network (TIN) interpolation technique to optimize for both global and local
          accuracy.

          * SPLINE— Transforms the source control points precisely to the target control
          points. In the output, the control points will be accurate, but the raster
          pixels between the control points are not.

          * PROJECTIVE— Warps lines so they remain straight. In doing so, lines that were
          once parallel may no longer remain parallel. The projective transformation is
          especially useful for oblique imagery, scanned maps, and for some imagery
          products.
      resampling_type {String}:
          Choose an appropriate technique based on the type of data you have.

          * NEAREST— The fastest resampling method; it minimizes changes to pixel values.
          Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY— Determines the value of each pixel based on the most popular value
          within a 3 by 3 window. Suitable for discrete data.
          The NEAREST and MAJORITY options are used for categorical data, such as a land-
          use classification. The NEAREST option is the default since it is the quickest
          and also because it will not change the cell values. Do not use either of these
          for continuous data, such as elevation surfaces.The BILINEAR option and the
          CUBIC option are most appropriate for continuous
          data. It is not recommended that either of these be used with categorical data
          because the cell values may be altered.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the dataset you are creating. When storing a
          raster dataset in a geodatabase, do not add a file extension to the name of the
          raster dataset. When storing your raster dataset to a JPEG file, a JPEG 2000
          file, a TIFF file, or a geodatabase, you can specify a compression type and
          compression quality using environment settings.

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.WarpFromFile_management(*gp_fixargs((in_raster, out_raster, link_file, transformation_type, resampling_type), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Mosaic Dataset toolset
@gptooldoc('AddRastersToMosaicDataset_management', None)
def AddRastersToMosaicDataset(in_mosaic_dataset=None, raster_type=None, input_path=None, update_cellsize_ranges=None, update_boundary=None, update_overviews=None, maximum_pyramid_levels=None, maximum_cell_size=None, minimum_dimension=None, spatial_reference=None, filter=None, sub_folder=None, duplicate_items_action=None, build_pyramids=None, calculate_statistics=None, build_thumbnails=None, operation_description=None, force_spatial_reference=None):
    """AddRastersToMosaicDataset_management(in_mosaic_dataset, raster_type, input_path;input_path..., {update_cellsize_ranges}, {update_boundary}, {update_overviews}, {maximum_pyramid_levels}, {maximum_cell_size}, {minimum_dimension}, {spatial_reference}, {filter}, {sub_folder}, {duplicate_items_action}, {build_pyramids}, {calculate_statistics}, {build_thumbnails}, {operation_description}, {force_spatial_reference})

        Adds raster datasets to a mosaic dataset from many sources, including a file,
        folder, table, or web service.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The path and name of the mosaic dataset to which the raster data will be added.
      raster_type (Raster Type):
          The raster type is specific for imagery products. It identifies metadata, such
          as georeferencing, acquisition date, and sensor type, along with a raster
          format. For a list of raster types, see the list of supported raster and image
          data
          formats.If you are using a LAS, LAS Dataset, or Terrain raster Type, an .art
          file must
          be used, where the cell size is specified.
      input_path (File / Workspace / WCS Coverage / Image Service / MapServer / WMS Map / Table View / Raster Layer / Mosaic Layer / Raster Catalog Layer / Terrain Layer / LAS Dataset Layer / Layer File):
          Path and name of the file, folder, raster dataset, mosaic dataset, table, or
          service.Not all input choices will be available. Those available will depend on
          the
          selected raster type.

          * Dataset—Allows you to select an ArcGIS geographic dataset, such as any raster
          or mosaic dataset in a geodatabase or a table.

          * Workspace—Allows you to select a folder containing multiple raster datasets.
          The folder can contain subfolders.This is affected by the Include Sub Folders
          and Input Data Filter parameters.

          * File—Allows you to select one or more raster datasets stored in a folder on
          disk, an image service definition (.ISDef) file, and a raster process definition
          (.RPDef) file. Also, the file list will ignore any files that do not correspond
          to the raster type being added. Do not use this with file formats that are
          raster datasets, such as TIFF or MrSID files—use Dataset.

          * Service—Allows you to select a WCS, map, or image service, or a web service
          layer file.
      update_cellsize_ranges {Boolean}:
          Calculates the cell size ranges of each raster in the mosaic dataset. These
          values are written to the attribute table within the minPS and maxPS columns.

          * UPDATE_CELL_SIZES—The cell size ranges will be calculated for all the rasters
          in the mosaic dataset. This is the default.

          * NO_CELL_SIZES—The cell size ranges will not be calculated.
      update_boundary {Boolean}:
          Generates or updates the boundary polygon of a mosaic dataset. By default, the
          boundary merges all the footprint polygons to create a single boundary
          representing the extent of the valid pixels.

          * UPDATE_BOUNDARY—The boundary will be generated or updated. This is the
          default.

          * NO_BOUNDARY—The boundary will not be generated or updated.
      update_overviews {Boolean}:
          Defines and generates overviews for a mosaic dataset.

          *  UPDATE_OVERVIEWS—Overviews will be defined and generated.

          * NO_OVERVIEWS—Overviews will not be defined or generated. This is the default.
      maximum_pyramid_levels {Long}:
          Defines the maximum number of pyramid levels that will be used in the mosaic
          dataset. For example, a value of 2 will use only the first two pyramid levels
          from the source raster. Leaving this blank or typing a value of -1 will build
          pyramids for all levels.This value can affect the display and the number of
          overviews that will be
          generated.
      maximum_cell_size {Double}:
          Defines the maximum pyramid cell size that will be used in the mosaic dataset.
      minimum_dimension {Long}:
          Defines the minimum dimensions of a raster pyramid that will be used in the
          mosaic dataset.
      spatial_reference {Spatial Reference}:
          The spatial reference system of the input data.This should be specified if the
          data does not have a coordinate system;
          otherwise, the coordinate system of the mosaic dataset will be used. This can
          also be used to override the coordinate system of the input data.
      filter {String}:
          A filter for the data being added to the mosaic dataset. You can use SQL
          expressions to create the data filter. The wildcards for the filter work on the
          full path to the input data.The following SQL statement will select the rows in
          which the following object
          IDs match.

          * OBJECTID IN (19745, 19680, 19681, 19744, 5932, 5931, 5889, 5890, 14551, 14552,
          14590, 14591)
          If you want to add only a TIFF image, add an asterisk before a file extension.

          * *.TIF
          If you want to add any image with the word sensor in the file path or the file
          name, add an asterisk before and after the word sensor.

          * *sensor2009*
          Or you can use PERL syntax to create a data filter.

          *  REGEX: .*1923.*|.*1922.*

          *  REGEX: .*192[34567].*|.*194.*|.*195.*
          The following PERL syntax with multiple lexical groupings as part of the
          expression is not supported.

          * REGEX: .*
          map_mean_.*(?:(?:[a-z0-9]*)_pptPct_(?:[0-9]|1[0-2]*?)_2[0-9]_*\w*).img
          Alternatively, you can use the following syntax.

          * REGEX: .*map_mean_*[a-z0-9]*_pptPct_([0-9]|1[0-2])_2[0-9]*_\w*.img
      sub_folder {Boolean}:
          Recursively explores subfolders.

          * SUBFOLDERS—All subfolders will be explored for data. This is the default.

          * NO_SUBFOLDERS—Only the top-level folder will be explored for data.
      duplicate_items_action {String}:
          A check will be performed to see if each raster has already been added, using
          the original path and file name. Choose which action to perform when a duplicate
          path and file name have been found.

          * ALLOW_DUPLICATES—All rasters will be added even if they already exist within
          the mosaic dataset. This is the default.

          * EXCLUDE_DUPLICATES—The duplicate raster will not be added.

          * OVERWRITE_DUPLICATES—The duplicate raster will overwrite the existing one.
      build_pyramids {Boolean}:
          Builds pyramids for each source raster.

          * NO_PYRAMIDS—Pyramids will not be generated. This is the default.

          * BUILD_PYRAMIDS—Pyramids will be generated.
      calculate_statistics {Boolean}:
          Calculates statistics for each source raster.

          * NO_STATISTICS—Statistics will not be generated. This is the default.

          * CALCULATE_STATISTICS—Statistics will be generated.
      build_thumbnails {Boolean}:
          Builds thumbnails for each source raster.

          * NO_THUMBNAILS—Thumbnails will not be generated. This is the default.

          * BUILD_THUMBNAILS—Thumbnails will be generated.
      operation_description {String}:
          A description you want used to represent this operation of adding raster data.
          It will be added to the raster type table which can be used as part of a search
          or as a reference at another time.
      force_spatial_reference {Boolean}:
          Use the coordinate system that is specified for all the rasters when loading
          data into the mosaic dataset.

          * NO_FORCE_SPATIAL_REFERENCE—Keep the coordinate system of each raster data when
          loading data. This is the default.

          * FORCE_SPATIAL_REFERENCE—Force the coordinate system specified in this tool for
          each raster when loading data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddRastersToMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, raster_type, input_path, update_cellsize_ranges, update_boundary, update_overviews, maximum_pyramid_levels, maximum_cell_size, minimum_dimension, spatial_reference, filter, sub_folder, duplicate_items_action, build_pyramids, calculate_statistics, build_thumbnails, operation_description, force_spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AlterMosaicDatasetSchema_management', None)
def AlterMosaicDatasetSchema(in_mosaic_dataset=None, side_tables=None, raster_type_names=None, editor_tracking=None):
    """AlterMosaicDatasetSchema_management(in_mosaic_dataset, {side_tables;side_tables...}, {raster_type_names;raster_type_names...}, {editor_tracking})

        Defines which editing operations nonowners have when editing a mosaic dataset in
        an enterprise geodatabase.This tool prevents schema-locking issues that can
        arise when a mosaic dataset is
        stored in an enterprise geodatabase. The owner of the geodatabase runs this tool
        to create any side tables and fields that may be needed by the user. The owner
        must also grant the proper permissions to allow users to insert, update, or
        delete records.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset on which to change permitted operations.
      side_tables {String}:
          The operations permissible for this mosaic dataset.

          * ANALYSIS—Choose this option if a nonowner is allowed to run the Analyze Mosaic
          Dataset tool on the mosaic dataset.

          * BOUNDARY—Choose this option if a nonowner is allowed to create or edit the
          boundary of the mosaic dataset. This is also required if a nonowner will add
          rasters outside of the existing boundary.

          * CACHE—Choose this option if a nonowner is allowed to create cache for the
          mosaic dataset.

          * COLOR_CORRECTION—Choose this option if a nonowner is allowed to color correct
          the mosaic dataset.

          * DEFINITION—Choose this option if a nonowner is allowed to add multidimensional
          data or a processing template to the mosaic dataset.

          * LEVELS—Choose this option if a nonowner is allowed to calculate cell size
          ranges or create seamlines for the mosaic dataset.

          * LOG—Choose this option if a nonowner is allowed to create a log table for the
          mosaic dataset.

          * OVERVIEW—Choose this option if a nonowner is allowed to create overviews for
          the mosaic dataset.

          * SEAMLINE—Choose this option if a nonowner is allowed to create seamlines for
          the mosaic dataset.

          * STEREO—Choose this option if a nonowner is allowed to define stereo pairs for
          the mosaic dataset.

          * VIEW—Choose this option if a nonowner is allowed to edit the image service.
          The editor_tracking parameter will be automatically enabled when VIEW is used,
          since the View table has to have editor tracking turned on.
      raster_type_names {String}:
          The raster types allowable for this mosaic dataset.

          * CADRG/ECRG—CADRG/ECRG raster type

          * CIB—CIB raster type

          * DTED—DTED raster type

          * DMCii—DMCii raster type

          * FORMOSAT-2—FORMOSAT-2 raster type

          * Frame Camera—Frame Camera raster type

          * GeoEye-1—GeoEye-1 raster type

          * GRIB—GRIB raster type

          * HDF—HDF raster type

          * HRE—HRE raster type

          * IKONOS—IKONOS raster type

          * KOMPSAT-2—KOMPSAT-2 raster type

          * LAS— LAS raster type

          * Landsat 1-5 MSS—Landsat 1-5 MSS raster type

          * Landsat 4-5 TM—Landsat 4-5 TM raster type

          * Landsat 7 ETM+—Landsat 7 ETM+ raster type

          * Landsat 8—Landsat 8 raster type

          * NITF—NITF raster type

          * NetCDF—NetCDF raster type

          * Pleiades-1—Pleiades-1 raster type

          * QuickBird—Quickbird raster type

          * RADARSAT-2—RADARSAT-2 raster type

          * RapidEye— RapidEye raster type

          * Raster Process Definition—Raster Process Definition raster type

          * SPOT 5—SPOT 5 raster type

          * SPOT 6—SPOT 6 raster type

          * WorldView-1—WorldView-1 raster type

          * WorldView-2— WorldView-2 raster type
          If you wish to use a custom raster type, enter the path of the custom raster
          type file.
      editor_tracking {Boolean}:
          Editor tracking can help you maintain accountability and enforce quality-
          control standards. For more information about Editor Tracking, see About
          tracking an editor's changes to data.

          * NO_EDITOR_TRACKING—Do not turn on editor tracking. This is the default.

          * EDITOR_TRACKING—Enables editor tracking for your mosaic dataset.
          If the VIEW keyword is used in the side_tables parameter, then editor tracking
          will automatically be enabled."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AlterMosaicDatasetSchema_management(*gp_fixargs((in_mosaic_dataset, side_tables, raster_type_names, editor_tracking), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AnalyzeMosaicDataset_management', None)
def AnalyzeMosaicDataset(in_mosaic_dataset=None, where_clause=None, checker_keywords=None):
    """AnalyzeMosaicDataset_management(in_mosaic_dataset, {where_clause}, {checker_keywords;checker_keywords...})

        Performs checks on a mosaic dataset for errors and possible improvements.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset you want to analyze.
      where_clause {SQL Expression}:
          An SQL statement that confines your analysis to specific raster datasets within
          this mosaic dataset.
      checker_keywords {String}:
          Choose which parts of the mosaic dataset you want to analyze for known issues.

          * FOOTPRINT— Analyze the footprint geometry of each selected mosaic dataset
          item. This is checked on by default.

          * FUNCTION— Analyze the function chains for each selected mosaic dataset item.

          * RASTER— Analyze the original raster datasets. This is checked on by default.

          * PATHS— Check for broken paths. This is checked on by default.

          * SOURCE_VALIDITY— Analyze potential problems with the source data associated
          with each mosaic dataset item in the selected mosaic dataset. This is a good way
          to detect issues that may arise during synchronization workflows.

          * STALE— Overviews are stale when the underlying source data has changed. Once
          the mosaic dataset is analyzed, you can select which items are stale by right-
          clicking on the error and choosing Select Associated Items on the context menu.

          * PYRAMIDS— Analyze the raster pyramids associated with each mosaic dataset item
          in the selected mosaic dataset. Test for disconnected auxiliary files which can
          occur when they are stored in a raster proxy location.

          * STATISTICS— Test for disconnected auxiliary statistics files if they are
          stored in the raster proxy location. Analyze the covariance matrix associated
          with the raster, when the Gram-Schmidt pan-sharpening method is enabled. Analyze
          the radiometric pixel depth of a mosaic dataset item against the pixel depth of
          the mosaic dataset.

          * PERFORMANCE— Factors that increase performance include compression during
          transmission and caching items with many raster functions.

          * INFORMATION— Generate an information log for the analysis."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AnalyzeMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, where_clause, checker_keywords), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildBoundary_management', None)
def BuildBoundary(in_mosaic_dataset=None, where_clause=None, append_to_existing=None, simplification_method=None):
    """BuildBoundary_management(in_mosaic_dataset, {where_clause}, {append_to_existing}, {simplification_method})

        Updates the extent of the boundary when adding new raster datasets to a mosaic
        dataset that extend beyond its previous coverage.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          Select the mosaic dataset where you want to recompute the boundary.
      where_clause {SQL Expression}:
          An SQL Query to compute a boundary for select raster datasets. Use this option
          in conjunction with setting the append_to_existing parameter to APPEND to save
          time when adding new raster datasets.
      append_to_existing {Boolean}:
          Set this to APPEND when adding new raster datasets to an existing mosaic
          dataset. Instead of calculating the entire boundary, APPEND will merge the
          boundary of the new raster datasets with the existing boundary.

          * OVERWRITE—Recompute the boundary in its entirety.

          * APPEND—Append the perimeter of footprints to the existing boundary. This can
          save time when adding additional raster data to the mosaic dataset, as the
          entire boundary will not be recalculated. If there are rasters selected, the
          boundary will be recalculated to include only the selected footprints. This is
          the default.
      simplification_method {String}:
          The simplification method reduces the number of vertices, since a dense boundary
          can affect performance. Choose which simplification method to use in order to
          simplify the boundary.

          * NONE—No simplification method will be implemented. This is the default.

          * CONVEX_HULL—The minimum bounding geometry of the mosaic dataset will be used
          to simplify the boundary. If there are any footprints that are disconnected,
          then a minimum bounding geometry for each continuous group of footprints will be
          used to simplify the boundary.

          * ENVELOPE—The envelope of the mosaic dataset will provide a simplified
          boundary. If there are any footprints that are disconnected, then an envelope
          for each continuous group of footprints will be used to simplify the boundary."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildBoundary_management(*gp_fixargs((in_mosaic_dataset, where_clause, append_to_existing, simplification_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildFootprints_management', None)
def BuildFootprints(in_mosaic_dataset=None, where_clause=None, reset_footprint=None, min_data_value=None, max_data_value=None, approx_num_vertices=None, shrink_distance=None, maintain_edges=None, skip_derived_images=None, update_boundary=None, request_size=None, min_region_size=None, simplification_method=None, edge_tolerance=None, max_sliver_size=None, min_thinness_ratio=None):
    """BuildFootprints_management(in_mosaic_dataset, {where_clause}, {reset_footprint}, {min_data_value}, {max_data_value}, {approx_num_vertices}, {shrink_distance}, {maintain_edges}, {skip_derived_images}, {update_boundary}, {request_size}, {min_region_size}, {simplification_method}, {edge_tolerance}, {max_sliver_size}, {min_thinness_ratio})

        Computes the extent of every raster in a mosaic dataset. This tool is used when
        you have added or removed raster datasets from a mosaic dataset and want to
        recompute the footprints.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that contains the raster datasets whose footprints you want
          to compute.
      where_clause {SQL Expression}:
          An SQL expression to select specific raster datasets within the mosaic dataset.
      reset_footprint {String / Boolean}:
          Refine the footprints using one of the following methods:

          * RADIOMETRY— Exclude pixels with a value outside of a defined range. This
          option is generally used to exclude border areas, which do not contain valid
          data. This is the default.

          * GEOMETRY— Restore the footprint to its original geometry.

          * COPY_TO_SIBLING— Replace the panchromatic footprint with the multispectral
          footprint when using a pan-sharpened raster type. This can occur when the
          panchromatic and multispectral images do not have identical geometries.

          * NONE—Do not redefine the footprints.
      min_data_value {Double}:
          Exclude pixels with a value less than this number.
      max_data_value {Double}:
          Exclude pixels with a value greater than this number.
      approx_num_vertices {Long}:
          Choose between 4 and 10,000. More vertices will improve accuracy but can extend
          processing time. A value of -1 will calculate all vertices. More vertices will
          increase accuracy but also the processing time.
      shrink_distance {Double}:
          Clip the footprint by this distance. This can eliminate artifacts from using
          lossy compression, which causes the edges of the image to overlap into NoData
          areas.Shrinking of the polygon is used to counteract effects of lossy
          compression,
          which causes edges of the image to overlap into NoData areas.
      maintain_edges {Boolean}:
          Use this parameter when using raster datasets that have been tiled and are butt
          joined (or line up along the seams with little to no overlap).

          * NO_MAINTAIN_EDGES—Remove the sheet edges from all of the footprints. This is
          the default.

          * MAINTAIN_EDGES—Maintain the footprints in their original state.
      skip_derived_images {Boolean}:
          Adjust the footprints of overviews.

          * SKIP_DERIVED_IMAGES—Do not adjust the footprints of overviews. This is the
          default.

          * NO_SKIP_DERIVED_IMAGES—Adjust the footprints of overviews and associated
          raster datasets.
      update_boundary {Boolean}:
          Update the boundary of the mosaic dataset if you have added or removed imagery
          that changes the extent.

          * UPDATE_BOUNDARY—Update the boundary. This is the default.

          * NO_BOUNDARY—Do not update the boundary.
      request_size {Long}:
          Set the resampled extent (in columns and rows) for the raster when building
          footprints. Greater image resolution provides more detail in the raster dataset
          but increases the processing time. A value of -1 will compute the footprint at
          the original resolution.
      min_region_size {Long}:
          Avoid small holes in your imagery when using pixel values to create a mask. For
          example, your imagery may have a range of values from 0–255, and to mask clouds,
          you've excluded values from 245–255, which may cause other, non-cloud pixels to
          be masked as well. If those areas are smaller than the number of pixels
          specified here, they will not be masked out.
      simplification_method {String}:
          Reduce the number of vertices in the footprint to improve performance.

          * NONE—Do not limit the number of vertices. This is the default.

          * CONVEX_HULL—Use the minimum bounding box to simplify the footprint.

          * ENVELOPE—Use the envelope of each mosaic dataset item to simplify the
          footprint.
      edge_tolerance {Double}:
          Snap the footprint to the sheet edge if it is within this tolerance. Units are
          the same as those in the mosaic dataset coordinate system. This is used when
          maintain_edges is set to MAINTAIN_EDGES.By default, the value is empty for which
          the tolerance is computed based on the
          pixel size corresponding to the requested resampled raster.A value of -1 will
          compute the tolerance using the average pixel size of the
          mosaic dataset.
      max_sliver_size {Long}:
          Identify all polygons that are smaller than the square of this value. The value
          is specified in pixels and is based on the request_size, not the spatial
          resolution of the source raster.Regions less than the (max_sliver_size)2 and
          also less than the
          min_thinness_ratio are considered slivers and will be removed.
      min_thinness_ratio {Double}:
          Define the thinness of slivers on a scale from 0–1.0, where 1.0 represents a
          circle and 0.0 represents a polygon that approaches a straight line. Polygons
          that are below both the max_sliver_size and min_thinness_ratio will be
          removed from the footprint."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildFootprints_management(*gp_fixargs((in_mosaic_dataset, where_clause, reset_footprint, min_data_value, max_data_value, approx_num_vertices, shrink_distance, maintain_edges, skip_derived_images, update_boundary, request_size, min_region_size, simplification_method, edge_tolerance, max_sliver_size, min_thinness_ratio), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildMosaicDatasetItemCache_management', None)
def BuildMosaicDatasetItemCache(in_mosaic_dataset=None, where_clause=None, define_cache=None, generate_cache=None, item_cache_folder=None, compression_method=None, compression_quality=None, max_allowed_rows=None, max_allowed_columns=None, request_size_type=None, request_size=None):
    """BuildMosaicDatasetItemCache_management(in_mosaic_dataset, {where_clause}, {define_cache}, {generate_cache}, {item_cache_folder}, {compression_method}, {compression_quality}, {max_allowed_rows}, {max_allowed_columns}, {request_size_type}, {request_size})

        Inserts the Cached Raster function as the final step in all function chains
        within a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to apply the cache function.
      where_clause {SQL Expression}:
          An SQL expression to select specific raster datasets within the mosaic dataset
          on which you want the item cache built.
      define_cache {Boolean}:
          Choose to define the mosaic dataset cache. A Cached Raster function will be
          inserted to the selected items. If an item already has a Cached Raster function,
          it will not add another one.

          * DEFINE_CACHE—The Cached Raster function will be added to the selected items.
          If an item already has this function, it will not add another one. This is the
          default.

          * NO_DEFINE_CACHE—No raster cache will be defined.
      generate_cache {Boolean}:
          Choose to generate the cache files based on the properties defined in the
          Cached Raster function, such as the location and the compression of the cache.

          * GENERATE_CACHE—Cache will be generated. This is the default.

          * NO_GENERATE_CACHE—Cache will not be generated.
      item_cache_folder {Workspace}:
          Choose to overwrite the default location to save your cache. If the mosaic
          dataset is inside of a file geodatabase, by default the cache is saved in a
          folder with the same name as the geodatabase and a .cache extension. If the
          mosaic dataset is inside of an enterprise geodatabase, by default the cache will
          be saved inside of that geodatabase. Once created, the cache will always save to
          the same location. To save the cache to a different location, you need to first
          use the Repair Mosaic Dataset tool to specify a new location, and then run this
          tool again. Once an item cache is created, regenerating an item cache to a
          different
          location is not possible by specifying a different cache path and rerunning this
          tool. It will still generate the item cache in the location where it was
          generated the first time. However, you can remove this function and insert a new
          one with the new path or use the Repair Mosaic Dataset tool to modify the cache
          path, then run this tool to generate the item cache in a different location.
      compression_method {String}:
          Choose how you want to compress your data for quicker transmission.

          * LOSSLESS— Retain the values of each pixel when generating cache. Lossless has
          a compression ratio of approximately 2:1

          * LOSSY— Appropriate when your imagery is only used as a backdrop. Lossy has the
          highest compression ratio (20:1), but groups similar pixel values to achieve
          higher compression.

          * NONE— Do not compress imagery. This will make your imagery slower to transmit,
          but faster to draw because it will not need to be decompressed when viewed.
      compression_quality {Long}:
          Set a compression quality when using the lossy method. The compression quality
          value is between 1 and 100 percent, with 100 compressing the least.
      max_allowed_rows {Long}:
          Limit the size of the cache dataset by number of rows. If value is more than
          the number of rows in the dataset, the cache will not generate.
      max_allowed_columns {Long}:
          Limit the size of the cache dataset by number of columns. If value is more than
          the number of columns in the dataset, the cache will not generate.
      request_size_type {String}:
          Resample the cache using one of these two methods:

          * PIXEL_SIZE_FACTOR— Set a scaling factor relative to the pixel size. To not
          resample the cache, choose PIXEL_SIZE_FACTOR and set the request_size parameter
          to 1.

          * PIXEL_SIZE— Specify a pixel size for the cached raster.
      request_size {Double}:
          Set a value to apply to the request_size_type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildMosaicDatasetItemCache_management(*gp_fixargs((in_mosaic_dataset, where_clause, define_cache, generate_cache, item_cache_folder, compression_method, compression_quality, max_allowed_rows, max_allowed_columns, request_size_type, request_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildOverviews_management', None)
def BuildOverviews(in_mosaic_dataset=None, where_clause=None, define_missing_tiles=None, generate_overviews=None, generate_missing_images=None, regenerate_stale_images=None):
    """BuildOverviews_management(in_mosaic_dataset, {where_clause}, {define_missing_tiles}, {generate_overviews}, {generate_missing_images}, {regenerate_stale_images})

        Defines and generates overviews on a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to build overviews.
      where_clause {SQL Expression}:
          An SQL statement to select specific rasters within the mosaic dataset. The
          selected rasters will have their overview built.
      define_missing_tiles {Boolean}:
          Identify where overviews are needed and define them.

          * DEFINE_MISSING_TILES—Automatically identify where overviews are needed and
          define them. This is the default.

          * NO_DEFINE_MISSING_TILES— Do not define new overviews.
      generate_overviews {Boolean}:
          Generate all overviews that need to be created or re-created. This includes
          missing overviews and stale overviews.

          * GENERATE_OVERVIEWS—Generate all overviews, including those that already exist.
          This is the default.

          * NO_GENERATE_OVERVIEWS—Generate only the overviews that have been defined but
          not yet generated.
      generate_missing_images {Boolean}:
          Use if overviews have been defined but not generated.

          * GENERATE_MISSING_IMAGES—Generate overviews that have been defined but not
          generated. This is the default.

          * IGNORE_MISSING_IMAGES— Do not generate overviews that have been defined but
          not generated.
      regenerate_stale_images {Boolean}:
          Overviews become stale when you change the underlying raster datasets or modify
          their properties.

          * REGENERATE_STALE_IMAGES—Identify and regenerate stale overviews. This is the
          default.

          * IGNORE_STALE_IMAGES— Do not regenerate stale overviews."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildOverviews_management(*gp_fixargs((in_mosaic_dataset, where_clause, define_missing_tiles, generate_overviews, generate_missing_images, regenerate_stale_images), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildSeamlines_management', None)
def BuildSeamlines(in_mosaic_dataset=None, cell_size=None, sort_method=None, sort_order=None, order_by_attribute=None, order_by_base_value=None, view_point=None, computation_method=None, blend_width=None, blend_type=None, request_size=None, request_size_type=None, blend_width_units=None, area_of_interest=None, where_clause=None, update_existing=None):
    """BuildSeamlines_management(in_mosaic_dataset, {cell_size;cell_size...}, {sort_method}, {sort_order}, {order_by_attribute}, {order_by_base_value}, {view_point}, {computation_method}, {blend_width}, {blend_type}, {request_size}, {request_size_type}, {blend_width_units}, {area_of_interest}, {where_clause}, {update_existing})

        Generate or update seamlines for your mosaic dataset. Seamlines are used to
        sort overlapping imagery and produce a smoother-looking mosaic.You can use this
        tool to do the following:

        * Generate seamlines for all items in the mosaic dataset.


        * Generate seamlines for items selected using a query or by an area of interest.


        * Update existing seamlines if items are added or removed from the mosaic
        dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          Select the mosaic dataset on which to build seamlines.
      cell_size {Double}:
          Generate seamlines for raster datasets that fall within the following range of
          spatial resolutions. You can leave this parameter empty and the tool will
          automatically create
          seamlines at the appropriate levels.The units for this parameter are the same as
          the spatial reference of the input
          mosaic dataset.
      sort_method {String}:
          Set a rule to determine which raster will be used to generate seamlines when
          images overlap.

          * NORTH_WEST— Select the raster datasets that have center points closest to the
          northwest corner of the boundary. This is the default.

          * CLOSEST_TO_VIEWPOINT— Select raster datasets based on a user-defined location
          and a nadir location for the raster datasets using the Viewpoint tool.

          * BY_ATTRIBUTE— Select raster datasets based on an attribute from the footprint
          attribute table. Commonly used attributes include acquisition date, cloud cover,
          or viewing angle.
      sort_order {Boolean}:
          Choose whether to sort the rasters in ascending order or descending order.

          * ASCENDING— Sort the rasters in ascending order. This is the default.

          * DESCENDING— Sort the rasters in descending order.
      order_by_attribute {Field}:
          Order the raster datasets based on this field when the sort method is
          BY_ATTRIBUTE. The default attribute is ObjectID.
      order_by_base_value {Variant}:
          Sort the rasters by their difference between this value and their value in the
          order_by_attribute field.
      view_point {Point}:
          Set the coordinate location to use when sort_method is CLOSEST_TO_VIEWPOINT.
      computation_method {String}:
          Choose how to build seamlines.

          * GEOMETRY— Generate seamlines for overlapping areas based on the intersection
          of footprints. Areas with no overlapping imagery will merge the footprints. This
          is the default.

          * RADIOMETRY— Generate seamlines based on the spectral patterns of features
          within the imagery.

          * COPY_FOOTPRINT—Generates seamlines directly from the footprints.

          * COPY_TO_SIBLING— Apply the seamlines from another mosaic dataset. The mosaic
          datasets have to be in the same group. For example, the extent of the
          panchromatic band does not always match the extent of the multispectral band.
          This option makes sure they share the same seamline.

          * EDGE_DETECTION— Generate seamlines over intersecting areas based on the edges
          of features in the area.
          The Sort Method parameter applies  to each computation method.
      blend_width {Double}:
          Blending (feathering) occurs along a seamline between pixels where there are
          overlapping rasters. The blend width defines how many pixels will be blended.If
          the blend width value is 10, and you use BOTH as the blend type, then 5
          pixels will be blended on the inside and outside of the seamline. If the value
          is 10, and the blend type is INSIDE, then 10 pixels will be blended on the
          inside of the seamline.
      blend_type {String}:
          Determine how to blend one image into another, over the seamlines. Options are
          to blend inside the seamlines, outside the seamlines, or both inside and
          outside.

          * BOTH— Blend using pixels on either side of the seamlines. For example, if the
          Blend Width is 10 pixels, then five pixels will be blended on the inside and
          outside of the seamline. This is the default.

          * INSIDE—Blend inside of the seamline.

          * OUTSIDE—Blend outside of the seamline.
      request_size {Long}:
          Specify the number of columns and rows for resampling. The maximum value is
          5,000. Increase or decrease this value based on the complexity of your raster
          data. Greater image resolution provides more detail in the raster dataset but
          also increases the processing time.
      request_size_type {String}:
          Set the units for the Request Size.

          * PIXELS—Modify the request size based on the pixel size.This is the default
          option and resamples the closest image based on the raster pixel size.

          * PIXELSIZE_FACTOR—Modify the request size by specifying a scaling factor. This
          option resamples the closest image by multiplying the raster pixel size (from
          cell size level table) with the pixel size factor.
      blend_width_units {String}:
          Specify the unit of measurement for blend width.

          * PIXELS—Measure using the number of pixels. This is the default.

          * GROUND_UNITS—Measure using the same units as the mosaic dataset.
      area_of_interest {Feature Set}:
          SQL expression to build seamlines on specific raster datasets within the mosaic
          dataset.
      where_clause {SQL Expression}:
          Build seamlines on all of the rasters that intersect this polygon. To select an
          area of interest, use an input feature class.
      update_existing {Boolean}:
          Update new seamlines and regenerate existing seamlines that are affected by the
          addition or deletion of the mosaic dataset items.

          * IGNORE_EXISTING—Regenerates seamlines for all items and ignores existing
          seamlines, if any. This is the default.

          *  UPDATE_EXISTING—Only update items without seamlines. If any new items overlap
          with the previously created seamlines, the existing seamlines may be affected.
          This parameter is ignored if seamlines do not exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildSeamlines_management(*gp_fixargs((in_mosaic_dataset, cell_size, sort_method, sort_order, order_by_attribute, order_by_base_value, view_point, computation_method, blend_width, blend_type, request_size, request_size_type, blend_width_units, area_of_interest, where_clause, update_existing), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateCellSizeRanges_management', None)
def CalculateCellSizeRanges(in_mosaic_dataset=None, where_clause=None, do_compute_min=None, do_compute_max=None, max_range_factor=None, cell_size_tolerance_factor=None, update_missing_only=None):
    """CalculateCellSizeRanges_management(in_mosaic_dataset, {where_clause}, {do_compute_min}, {do_compute_max}, {max_range_factor}, {cell_size_tolerance_factor}, {update_missing_only})

        Computes the visibility levels of raster datasets in a mosaic dataset based on
        the spatial resolution.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset to calculate the visibility levels for.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters in the mosaic dataset on which to
          calculate visibility levels. If no query is specified, all the mosaic dataset
          items will have their cell size ranges calculated.
      do_compute_min {Boolean}:
          Compute the minimum pixel size for each selected raster in the mosaic dataset.

          * MIN_CELL_SIZES—Compute the minimum pixel size. This is the default.

          * NO_MIN_CELL_SIZES—Do not compute the minimum pixel size.
      do_compute_max {Boolean}:
          Compute the maximum pixel size for each selected raster in the mosaic dataset.

          * MAX_CELL_SIZES—Compute the maximum pixel size. This is the default.

          * NO_MAX_CELL_SIZES—Do not compute the maximum pixel size.
      max_range_factor {Double}:
          Set a multiplication factor to apply to the native resolution. The default is
          10, meaning that an image with a resolution of 30 meters will be visible at a
          scale appropriate for 300 meters. The relationship between cell size and scale
          is as follows: Cell Size = Scale * 0.0254 / 96 Scale = Cell Size * 96 / 0.0254
      cell_size_tolerance_factor {Double}:
          Use this to group images with similar resolutions as the having the same
          nominal resolution. For example 1 m imagery and 0.9 m imagery can be grouped
          together by setting this factor to 0.1, because they are within 10% of each
          other.
      update_missing_only {Boolean}:
          Calculate only the missing cell size range values.

          * UPDATE_ALL—Calculate cell size minimum and maximum values for selected rasters
          within the mosaic dataset. This is the default.

          * UPDATE_MISSING_ONLY— Calculate cell size minimum and maximum values only if
          they do not exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateCellSizeRanges_management(*gp_fixargs((in_mosaic_dataset, where_clause, do_compute_min, do_compute_max, max_range_factor, cell_size_tolerance_factor, update_missing_only), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ColorBalanceMosaicDataset_management', None)
def ColorBalanceMosaicDataset(in_mosaic_dataset=None, balancing_method=None, color_surface_type=None, target_raster=None, exclude_raster=None, stretch_type=None, gamma=None, block_field=None):
    """ColorBalanceMosaicDataset_management(in_mosaic_dataset, {balancing_method}, {color_surface_type}, {target_raster}, {exclude_raster}, {stretch_type}, {gamma}, {block_field})

        Makes transitions from one image to an adjoining image appear seamless.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset you want to color balance.
      balancing_method {String}:
          The balancing algorithm to use.

          * DODGING—Change each pixel's value towards a target color. With this technique,
          you must also choose the type of target color surface, which affects the target
          color. Dodging tends to give the best result in most cases.

          * HISTOGRAM—Change each pixel's value according to its relationship with a
          target histogram. The target histogram can be derived from all of the rasters or
          you can specify a raster. This technique works well when all of the rasters have
          a similar histogram.

          * STANDARD_DEVIATION—Change each of the pixel's values according to its
          relationship with the histogram of the target raster, within one standard
          deviation. The standard deviation can be calculated from all of the rasters in
          the mosaic dataset or you can specify a target raster. This technique works best
          when all of the rasters have normal distributions.
      color_surface_type {String}:
          When using the Dodging balance method, each pixel needs a target color, which
          is determined by the surface type.

          * SINGLE_COLOR—Use when there are only a small number of raster datasets and a
          few different types of ground objects. If there are too many raster datasets or
          there are too many types of ground surfaces, then the output color may become
          blurred. All the pixels are altered towards a single color point—the mean
          (average) of all pixels.

          * COLOR_GRID— Use when you have a large number of raster datasets, or areas with
          a large number of diverse ground objects. Pixels are altered toward multiple
          target colors, which are distributed across the mosaic dataset.

          * FIRST_ORDER— This technique tends to create a smoother color change and uses
          less storage in the auxiliary table, but it may take longer to process compared
          to the color grid surface. All pixels are altered towards many points obtained
          from the two-dimensional polynomial slanted plane.

          * SECOND_ORDER— This technique tends to create a smoother color change and uses
          less storage in the auxiliary table, but it may take longer to process compared
          to the color grid surface. All input pixels are altered toward a set of multiple
          points obtained from the two-dimensional polynomial parabolic surface.

          * THIRD_ORDER— This technique tends to create a smoother color change and uses
          less storage in the auxiliary table, but it may take longer to process compared
          to the color grid surface. All input pixels are altered toward multiple points
          obtained from the cubic surface.
      target_raster {Raster Layer / Internet Tiled Layer / Map Server Layer}:
          The raster that you want to use to color balance the other images. The balance
          method and color surface type, if applicable, will be derived from this image.
      exclude_raster {Raster Layer}:
          Applies a mask before color balancing the mosaic dataset. Create the mask using
          the Generate Exclude Area tool.
      stretch_type {String}:
          Stretch the range of values before color balancing. Choose from one of the
          following options:

          * NONE— Use the original pixel values. This is the default.

          * ADAPTIVE— An adaptive prestretch will be applied before any processing takes
          place.

          * MINIMUM_MAXIMUM— Stretch the values between their actual minimum and maximum
          values.

          * STANDARD_DEVIATION— Stretch the values between the default number of standard
          deviations.
      gamma {Double}:
          Adjust the overall brightness of an image. A low value will minimize the
          contrast between moderate values by making them appear darker. Higher values
          increase thecontrast by making them appear brighter.
      block_field {String}:
          The name of the field within a mosaic dataset's attribute table used to
          identify items that should be considered one item when performing some
          calculations and operations."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ColorBalanceMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, balancing_method, color_surface_type, target_raster, exclude_raster, stretch_type, gamma, block_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ComputeDirtyArea_management', None)
def ComputeDirtyArea(in_mosaic_dataset=None, where_clause=None, timestamp=None, out_feature_class=None):
    """ComputeDirtyArea_management(in_mosaic_dataset, {where_clause}, timestamp, out_feature_class)

        Identifies areas within a mosaic dataset that have changed since a specified
        point in time. This is used commonly when a mosaic dataset is updated or
        synchronized, or when derived products, such as cache, need to be updated. This
        tool will enable you to limit such processes to only the areas that have
        changed.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to analyze for changes.
      where_clause {SQL Expression}:
          SQL expression to select specific rasters within the mosaic dataset on which to
          compute dirty areas.
      timestamp (String):
          Compute the areas that have changed since the input time.XML time syntax:

          * YYYY-MM-DDThh:mm:ss

          * YYYY-MM-DDThh:mm:ss.ssssZ

          * 2002-10-10T12:00:00.ssss-00:00

          * 2002-10-10T12:00:00+00:00
          Non-XML time syntax:

          * 2002/12/25 23:59:58.123

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the areas that have changed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ComputeDirtyArea_management(*gp_fixargs((in_mosaic_dataset, where_clause, timestamp, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateMosaicDataset_management', None)
def CreateMosaicDataset(in_workspace=None, in_mosaicdataset_name=None, coordinate_system=None, num_bands=None, pixel_type=None, product_definition=None, product_band_definitions=None):
    """CreateMosaicDataset_management(in_workspace, in_mosaicdataset_name, coordinate_system, {num_bands}, {pixel_type}, {product_definition}, {product_band_definitions;product_band_definitions...})

        Create an empty mosaic dataset in a geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The path to the geodatabase.
      in_mosaicdataset_name (String):
          Name the mosaic dataset you are creating.
      coordinate_system (Spatial Reference):
          The coordinate system for all of the items in the mosaic dataset.
      num_bands {Long}:
          The number of bands that the raster datasets in the mosaic dataset will have.
      pixel_type {String}:
          Set the bit depth, or radiometric resolution, of the mosaic dataset. If not
          defined, it will be taken from the first raster dataset.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      product_definition {String}:
          Select a template that is either specific to the type of imagery you are
          working with, or is generic. The generic options are as follows:

          * None—No band ordering is specified for the mosaic dataset. This is the
          default.

          * NATURAL_COLOR_RGB—Create a three-band mosaic dataset, with red, green, and
          blue wavelength ranges. This is designed for natural color imagery.

          * NATURAL_COLOR_RGBI—Create a four-band mosaic dataset, with red, green, blue
          and near infrared wavelength ranges.

          * FALSE_COLOR_IRG—Create a three-band mosaic dataset, with near infrared, red,
          and green wavelength ranges.

          * VECTOR_FIELD_UV—Create a mosaic dataset displaying two variables.

          * VECTOR_FIELD_MAGNITUDE_DIRECTION—Create a mosaic dataset displaying magnitude
          and direction.

          * DMCII_3BANDS—Create a three-band mosaic dataset using the DMCII wavelength
          ranges.

          * FORMOSAT-2_4BANDS—Create a four-band mosaic dataset using the FORMOSAT-2
          wavelength ranges.

          * GEOEYE-1_4BANDS—Create a four-band mosaic dataset using the GeoEye-1
          wavelength ranges.

          * IKONOS_4BANDS—Create a four-band mosaic dataset using the IKONOS wavelength
          ranges.

          * KOMPSAT-2_4BANDS—Create a four-band mosaic dataset using the KOMPSAT-2
          wavelength ranges.

          * LANDSAT_6BANDS—Create a six-band mosaic dataset using the Landsat 5 and 7
          wavelength ranges from the TM and ETM+ sensors.

          * LANDSAT_8BANDS—Create an 8-band mosaic dataset using the LANDSAT 8 wavelength
          ranges.

          * LANDSAT_MSS_4BANDS—Create a four-band mosaic dataset using the Landsat
          wavelength ranges from the MSS sensor.

          * PLEIADES-1_4BANDS—Create a four-band mosaic dataset using the PLEIADES-1
          wavelength ranges.

          * QUICKBIRD_4BANDS—Create a four-band mosaic dataset using the QuickBird
          wavelength ranges.

          * RAPIDEYE_5BANDS—Create a five-band mosaic dataset using the RapidEye
          wavelength ranges.

          * SPOT-5_4BANDS—Create a four-band mosaic dataset using the SPOT 5 wavelength
          ranges.

          * SPOT-6_4BANDS—Create a four-band mosaic dataset using the SPOT-6 wavelength
          ranges.

          * WORLDVIEW-2_8BANDS—Create an eight-band mosaic dataset using the WorldView-2
          wavelength ranges.

          * CUSTOM—Define the number of bands and the average wavelength for each band.
      product_band_definitions {Value Table}:
          Edit the product_definition by adjusting the wavelength ranges, changing the
          band order, and adding new bands when using the CUSTOM product definition."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateMosaicDataset_management(*gp_fixargs((in_workspace, in_mosaicdataset_name, coordinate_system, num_bands, pixel_type, product_definition, product_band_definitions), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateReferencedMosaicDataset_management', None)
def CreateReferencedMosaicDataset(in_dataset=None, out_mosaic_dataset=None, coordinate_system=None, number_of_bands=None, pixel_type=None, where_clause=None, in_template_dataset=None, extent=None, select_using_features=None, lod_field=None, minPS_field=None, maxPS_field=None, pixelSize=None, build_boundary=None):
    """CreateReferencedMosaicDataset_management(in_dataset, out_mosaic_dataset, {coordinate_system}, {number_of_bands}, {pixel_type}, {where_clause}, {in_template_dataset}, {extent}, {select_using_features}, {lod_field}, {minPS_field}, {maxPS_field}, {pixelSize}, {build_boundary})

        Creates a new mosaic dataset from an existing raster catalog, a selection set
        from a raster catalog, or a mosaic dataset.

     INPUTS:
      in_dataset (Raster Catalog Layer / Mosaic Dataset / Mosaic Layer):
          The input raster catalog or mosaic dataset.
      coordinate_system {Spatial Reference}:
          The projection for the output mosaic dataset.
      number_of_bands {Long}:
          The number of bands that the referenced mosaic dataset will have.
      pixel_type {String}:
          The bit depth, or radiometric resolution, of the mosaic dataset. If not defined,
          it will be taken from the first raster dataset.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      where_clause {SQL Expression}:
          An SQL expression to select raster datasets that will be included in the output
          mosaic dataset.
      in_template_dataset {Raster Layer / Feature Layer}:
          Selects raster datasets based on the extent of another image or feature class.
          Raster datasets that lay along the defined extent will be included in the mosaic
          dataset. To manually input the minimum and maximum coordinates for the extent,
          use the Extent parameter.
      extent {Envelope}:
          The minimum and maximum coordinates for the extent.
      select_using_features {Boolean}:
          Limit the extent to the shape or envelope when a feature class is specified in
          the in_template_dataset parameter.

          * SELECT_USING_FEATURES—Select using the shape of the feature. This is the
          default.

          * NO_SELECT_USING_FEATURES—Select using the extent of the data within the
          feature class.
      lod_field {Field}:
          A field in the raster catalog table defining the map scales at which the mosaic
          should be displayed; otherwise, a wire frame will be displayed.
      minPS_field {Field}:
          Specify a field from the footprint attribute table that defines the minimum
          cell size for displaying the mosaic dataset; otherwise, only a footprint will be
          displayed.
      maxPS_field {Field}:
          Specify a field from the footprint attribute table that defines the maximum
          cell size for displaying the mosaic dataset; otherwise, only a footprint will be
          displayed.
      pixelSize {Double}:
          Set a maximum cell size to display the mosaic, instead of specifying a field. If
          you zoom out beyond this cell size, only the footprint will be displayed.
      build_boundary {Boolean}:
          Rebuild the boundary. If the selection covers a smaller area than the source
          mosaic dataset, this is recommended.This is only available if the mosaic dataset
          is created within a geodatabase.

          * BUILD_BOUNDARY—The boundary will be generated or updated. This is the default.

          * NO_BOUNDARY— The boundary will not be generated.

     OUTPUTS:
      out_mosaic_dataset (Mosaic Dataset):
          The referenced mosaic dataset that you want to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateReferencedMosaicDataset_management(*gp_fixargs((in_dataset, out_mosaic_dataset, coordinate_system, number_of_bands, pixel_type, where_clause, in_template_dataset, extent, select_using_features, lod_field, minPS_field, maxPS_field, pixelSize, build_boundary), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DefineMosaicDatasetNoData_management', None)
def DefineMosaicDatasetNoData(in_mosaic_dataset=None, num_bands=None, bands_for_nodata_value=None, bands_for_valid_data_range=None, where_clause=None, Composite_nodata_value=None):
    """DefineMosaicDatasetNoData_management(in_mosaic_dataset, num_bands, {bands_for_nodata_value;bands_for_nodata_value...}, {bands_for_valid_data_range;bands_for_valid_data_range...}, {where_clause}, {Composite_nodata_value})

        Specifies one or more values to be represented as NoData.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset where you want to update the NoData values.
      num_bands (Long):
          The number of bands in the mosaic dataset.
      bands_for_nodata_value {Value Table}:
          Define values for each or all bands. Each band can have a unique NoData value
          defined, or the same value can be specified for all bands. If you want to define
          multiple NoData values for each band selection, use a space delimiter between
          each NoData value within the bands_for_nodata_value parameter.The Mask function
          inserted by this tool is inserted before the Composite Bands
          function in the function chain. Therefore, if the function chain for each raster
          within the mosaic dataset contains the Composite Bands function, or if your
          raster data was added with a raster type that adds the Composite Bands function
          to each raster’s function chain, then any value you specify will apply to all
          bands.
      bands_for_valid_data_range {Value Table}:
          Specify a range of values to display for each band. Values outside of this
          range will be classified as NoData. When working with composite bands, the range
          will apply to all bands.
      where_clause {SQL Expression}:
          An SQL statement to select specific raster in the mosaic dataset. Only the
          selected rasters will have their NoData values changed.
      Composite_nodata_value {Boolean}:
          Choose whether all bands must be NoData in order for the pixel to be classified
          as NoData.

          *  NO_COMPOSITE_NODATA—If any of the bands have pixels of NoData, then the pixel
          is classified as NoData. This is the default.

          *  COMPOSITE_NODATA—All of the bands must have pixels of NoData in order for the
          pixel to be classified as NoData."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DefineMosaicDatasetNoData_management(*gp_fixargs((in_mosaic_dataset, num_bands, bands_for_nodata_value, bands_for_valid_data_range, where_clause, Composite_nodata_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DefineOverviews_management', None)
def DefineOverviews(in_mosaic_dataset=None, overview_image_folder=None, in_template_dataset=None, extent=None, pixel_size=None, number_of_levels=None, tile_rows=None, tile_cols=None, overview_factor=None, force_overview_tiles=None, resampling_method=None, compression_method=None, compression_quality=None):
    """DefineOverviews_management(in_mosaic_dataset, {overview_image_folder}, {in_template_dataset}, {extent}, {pixel_size}, {number_of_levels}, {tile_rows}, {tile_cols}, {overview_factor}, {force_overview_tiles}, {resampling_method}, {compression_method}, {compression_quality})

        Lets you set how mosaic dataset overviews are generated. The settings you make
        with this tool are used by the Build Overviews tool.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to build overviews on.
      overview_image_folder {Workspace}:
          The folder or geodatabase to store the overviews.
      in_template_dataset {Raster Layer / Feature Layer}:
          A raster dataset or feature class to define the extent of the overviews.
      extent {Envelope}:
          Set the extent using minimum and maximum x and y coordinates. This is specified
          as space delimited in the following order: X-minimum
          X-maximum Y-minimum Y-maximum.The mosaic dataset boundary will determine the
          extent of the overviews if you do
          not define an extent.
      pixel_size {Double}:
          If you prefer not to use all the raster's pyramids, specify a base pixel size
          at which your overviews will be generated.The units for this parameter are the
          same as the spatial reference of the mosaic
          dataset.
      number_of_levels {Long}:
          Specify the number of levels of overviews that you want to generate overviews. A
          value of -1 will determine an optimal value for you.
      tile_rows {Long}:
          Set the number of rows (in pixels) for each tile.Larger values will result in
          fewer, larger individual overviews, and increase
          the likelihood that you will need to regenerate lower level overviews. A smaller
          value will result in more, smaller files.
      tile_cols {Long}:
          Set the number of columns (in pixels) for each tile.Larger values will result
          in fewer, larger individual overviews, and increase
          the likelihood that you will need to regenerate lower level overviews. A smaller
          value will result in more, smaller files.
      overview_factor {Long}:
          Set a ratio to determine the size of the next overview. For example, if the cell
          size of the first level is 10, and the overview factor is 3, then the next
          overview pixel size will be 30.
      force_overview_tiles {Boolean}:
          Generate overviews at all levels, or only above existing pyramid levels.

          * NO_FORCE_OVERVIEW_TILES—Create overviews above the raster pyramid levels. This
          is the default.

          * FORCE_OVERVIEW_TILES— Create overviews at all levels.
      resampling_method {String}:
          Choose an algorithm for aggregating pixel values in the overviews.

          * NEAREST— The fastest resampling method because it minimizes changes to pixel
          values. Suitable for discrete data, such as land cover. If the Key Metadata Data
          Type is thematic, then nearest neighbor will be the default.

          * BILINEAR—Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous
          data.This is the default, unless the Key Metadata Data Type is thematic.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image, but can create values
          outside of the range found in the source data. Suitable for continuous data.
      compression_method {String}:
          Define the type of data compression to store the overview images.

          * JPEG—A lossy compression. This is the default, unless the Key Metadata Data
          Type is thematic. This compression method is only valid if the mosaic dataset
          items adhere to JPEG specifications.

          * JPEG_YCbCr—A lossy compression using the luma (Y) and chroma (Cb and Cr) color
          space components.

          * None—No data compression.

          * LZW—A lossless compression. If the Key Metadata Data Type is thematic, then
          nearest neighbor will be the default.
      compression_quality {Long}:
          Choose a value from 1 - 100. Higher values generate better quality outputs, but
          they create larger files."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DefineOverviews_management(*gp_fixargs((in_mosaic_dataset, overview_image_folder, in_template_dataset, extent, pixel_size, number_of_levels, tile_rows, tile_cols, overview_factor, force_overview_tiles, resampling_method, compression_method, compression_quality), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteMosaicDataset_management', None)
def DeleteMosaicDataset(in_mosaic_dataset=None, delete_overview_images=None, delete_item_cache=None):
    """DeleteMosaicDataset_management(in_mosaic_dataset, {delete_overview_images}, {delete_item_cache})

        Deletes a mosaic dataset, its overviews, and its item cache from disk.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to delete.
      delete_overview_images {Boolean}:
          Delete all overviews associated with the mosaic dataset.

          *  DELETE_OVERVIEW_IMAGES —Delete the overviews associated with the mosaic
          dataset. This is the default.

          * NO_DELETE_OVERVIEW_IMAGES—Do not delete the overviews.
      delete_item_cache {Boolean}:
          Delete the item cache associated with the mosaic dataset.

          *  DELETE_ITEM_CACHE—Delete the item cache associated with the mosaic dataset.
          This is the default.

          * NO_DELETE_ITEM_CACHE—Do not delete the item cache."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, delete_overview_images, delete_item_cache), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EditRasterFunction_management', None)
def EditRasterFunction(in_mosaic_dataset=None, edit_mosaic_dataset_item=None, edit_options=None, function_chain_definition=None, location_function_name=None):
    """EditRasterFunction_management(in_mosaic_dataset, {edit_mosaic_dataset_item}, {edit_options}, {function_chain_definition}, {location_function_name})

        Adds, replaces, or removes a function chain in a mosaic dataset or a raster
        layer that contains a raster function.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer / Raster Layer):
          The mosaic dataset or a raster layer. If you use a raster layer, it must have a
          function applied.
      edit_mosaic_dataset_item {Boolean}:
          Determines if edits affect functions or the entire mosaic dataset.

          * EDIT_MOSAIC_DATASET—Edits affect the functions associated with the mosaic
          dataset. This is the default.

          * EDIT_MOSAIC_DATASET_ITEM—Edits affect the functions associated with all of the
          items within the mosaic dataset.
      edit_options {String}:
          Insert, replace, or remove a function chain.

          * INSERT—Insert the function chain above the Function Name of the existing
          chain. Specify the function chain in the location_function_name parameter. This
          is the default.

          * REPLACE—Replace the existing function chain with the function chain specified
          in this tool. Specify the function chain below in the location_function_name
          parameter.

          * REMOVE— Remove the function chain starting from the function specified in the
          location_function_name parameter.
      function_chain_definition {File}:
          Choose the function chain (rft.xml file) that you want to insert or replace.
      location_function_name {String}:
          Choose where to insert, replace, or remove the function chain within the
          existing function chain."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EditRasterFunction_management(*gp_fixargs((in_mosaic_dataset, edit_mosaic_dataset_item, edit_options, function_chain_definition, location_function_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportMosaicDatasetGeometry_management', None)
def ExportMosaicDatasetGeometry(in_mosaic_dataset=None, out_feature_class=None, where_clause=None, geometry_type=None):
    """ExportMosaicDatasetGeometry_management(in_mosaic_dataset, out_feature_class, {where_clause}, {geometry_type})

        Creates a feature class showing the footprints, boundary, seamlines or spatial
        resolutions of a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to export the geometry from.
      where_clause {SQL Expression}:
          An SQL expression to export specific rasters in the mosaic dataset.
      geometry_type {String}:
          The type of geometry to export.

          * FOOTPRINT— Create a feature class showing the footprints of each image.

          * BOUNDARY — Create a feature class showing the boundary of the mosaic dataset.

          * SEAMLINE— Create a feature class showing the seamlines.

          * LEVEL— Create a feature class based on cell size level of features in your
          mosaic dataset.

     OUTPUTS:
      out_feature_class (Feature Class):
          Name the feature class you are creating."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportMosaicDatasetGeometry_management(*gp_fixargs((in_mosaic_dataset, out_feature_class, where_clause, geometry_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportMosaicDatasetItems_management', None)
def ExportMosaicDatasetItems(in_mosaic_dataset=None, out_folder=None, out_base_name=None, where_clause=None, format=None, nodata_value=None, clip_type=None, template_dataset=None, cell_size=None):
    """ExportMosaicDatasetItems_management(in_mosaic_dataset, out_folder, {out_base_name}, {where_clause}, {format}, {nodata_value}, {clip_type}, {template_dataset}, {cell_size})

        Saves a copy of your processed images within a mosaic dataset to a specified
        folder and raster file format.There are two common workflows that use this tool:

        * Exporting each processed item of a mosaic dataset to a new file. This allows
        you to have each processed item as its own stand-alone file. Make sure that you
        set the appropriate NoData value for the exported items so there are no black
        borders.


        * Exporting each image within a time series mosaic dataset, based on an area of
        interest. This allows you to have only the area of interest from each of the
        time slices.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that has the images you want to save.
      out_folder (Folder):
          The folder where you want to save your images.
      out_base_name {String}:
          An SQL expression to save selected images in the mosaic dataset. For more
          information on SQL syntax, see SQL reference for query expressions used in
          ArcGIS.
      where_clause {SQL Expression}:
          Choose a prefix to name each item after it is copied. The prefix will be
          followed by the Object ID.If no base name is set, the text in the Name field of
          the mosaic dataset item
          will be used.
      format {String}:
          Choose a format for the downloaded raster datasets.

          * TIFF—Tagged Image File Format. This is the default.

          * BMP—Microsoft Bitmap.

          * ENVI—ENVI DAT.

          * Esri BIL—Esri Band Interleaved by Line.

          * Esri BIP—Esri Band Interleaved by Pixel.

          * Esri BSQ—Esri Band Sequential.

          * GIF—Graphic Interchange Format.

          * GRID—Esri Grid.

          * IMAGINE IMAGE—ERDAS IMAGINE.

          * JP2—JPEG 2000.

          * JPEG—Joint Photographic Experts Group.

          * PNG—Portable Network Graphics.
      nodata_value {String}:
          Set a value for pixels to be considered as NoData.If you choose to clip your
          output data, it is recommended that you specify a
          NoData value.
      clip_type {String}:
          Limit the extent of your raster dataset before you clip it. If you choose an
          extent or feature class that covers a larger area than your data, the output
          will have the larger extent.

          * NONE—Do not clip. This is the default.

          * EXTENT—Specify an extent to clip to.

          * FEATURE_CLASS—Specify a feature class to clip to.
      template_dataset {Extent}:
          Specify a feature class or a bounding box to limit the extent.
      cell_size {Point}:
          Define the spatial resolution by specifying the horizontal (x) and vertical (y)
          dimensions of the output cells.If not specified, the spatial resolution of the
          input will be used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportMosaicDatasetItems_management(*gp_fixargs((in_mosaic_dataset, out_folder, out_base_name, where_clause, format, nodata_value, clip_type, template_dataset, cell_size), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportMosaicDatasetPaths_management', None)
def ExportMosaicDatasetPaths(in_mosaic_dataset=None, out_table=None, where_clause=None, export_mode=None, types_of_paths=None):
    """ExportMosaicDatasetPaths_management(in_mosaic_dataset, out_table, {where_clause}, {export_mode}, {types_of_paths;types_of_paths...})

        Creates a table of the file path for each item in a mosaic dataset. You can
        specify whether the table contains all the file paths or just the ones that are
        broken.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the file paths to export.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters for export.
      export_mode {String}:
          Populate the table with either all of the paths, or only the broken paths.

          * ALL—Export all paths to the table. This is the default.

          * BROKEN—Export only broken paths to the table.
      types_of_paths {String}:
          Choose to export file paths from only the source raster, only the cache, or
          both. The default is to export all path types.

          * RASTER—Export file paths from rasters.

          * ITEM_CACHE—Export file paths from item cache.

     OUTPUTS:
      out_table (Table):
          The table to create. The table can be a geodatabase table or a .dbf file.The
          SourceOID field in the output table is derived from the OID of the row in
          the original mosaic dataset table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportMosaicDatasetPaths_management(*gp_fixargs((in_mosaic_dataset, out_table, where_clause, export_mode, types_of_paths), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateExcludeArea_management', None)
def GenerateExcludeArea(in_raster=None, out_raster=None, pixel_type=None, generate_method=None, max_red=None, max_green=None, max_blue=None, max_white=None, max_black=None, max_magenta=None, max_cyan=None, max_yellow=None, percentage_low=None, percentage_high=None):
    """GenerateExcludeArea_management(in_raster, out_raster, pixel_type, generate_method, {max_red}, {max_green}, {max_blue}, {max_white}, {max_black}, {max_magenta}, {max_cyan}, {max_yellow}, {percentage_low}, {percentage_high})

        Masks pixels based on their color or by clipping a range of values. The output
        of this tool is used as an input to the Color Balance Mosaic Dataset tool to
        eliminate areas such as clouds and water that can skew the statistics used to
        color balance multiple images.

     INPUTS:
      in_raster (Mosaic Dataset / Composite Layer / Raster Dataset / Raster Layer):
          The raster or mosaic dataset layer that you want to mask.
      pixel_type (String):
          Choose the pixel depth of your input raster dataset. 8-bit is the default
          value; however, raster datasets with a greater bit-depth will need to have the
          color mask and histogram values scaled accordingly.

          * 8_BIT—The input raster dataset has values from 0 to 255. This is the default.

          * 11_BIT—The input raster dataset has values from 0 to 2047.

          * 12_BIT—The input raster dataset has values from 0 to 4095.

          * 16_BIT—The input raster dataset has values from 0 to 65535.
      generate_method (String):
          Create your mask based on the color of the pixels or by clipping high and low
          values.

          * COLOR_MASK—Set the maximum color values to include in the output. This is the
          default.

          * HISTOGRAM_PERCENTAGE—Remove a percentage of high and low pixel values.
      max_red {Double}:
          The maximum red value to exclude. The default is 255.
      max_green {Double}:
          The maximum green value to exclude. The default is 255.
      max_blue {Double}:
          The maximum blue value to exclude. The default is 255.
      max_white {Double}:
          The maximum white value to exclude. The default is 255.
      max_black {Double}:
          The maximum black value to exclude. The default is 0.
      max_magenta {Double}:
          The maximum magenta value to exclude. The default is 255.
      max_cyan {Double}:
          The maximum cyan value to exclude. The default is 255.
      max_yellow {Double}:
          The maximum yellow value to exclude. The default is 255.
      percentage_low {Double}:
          Exclude this percentage of the lowest pixel values. The default is 0.
      percentage_high {Double}:
          Exclude this percentage of the highest pixel values. The default is 100.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the dataset you are creating. When storing a
          raster dataset in a geodatabase, do not add a file extension to the name of the
          raster dataset. When storing your raster dataset to a JPEG file, a JPEG 2000
          file, or a geodatabase, you can specify a Compression type and Compression
          Quality within the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateExcludeArea_management(*gp_fixargs((in_raster, out_raster, pixel_type, generate_method, max_red, max_green, max_blue, max_white, max_black, max_magenta, max_cyan, max_yellow, percentage_low, percentage_high), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportMosaicDatasetGeometry_management', None)
def ImportMosaicDatasetGeometry(in_mosaic_dataset=None, target_featureclass_type=None, target_join_field=None, input_featureclass=None, input_join_field=None):
    """ImportMosaicDatasetGeometry_management(in_mosaic_dataset, target_featureclass_type, target_join_field, input_featureclass, input_join_field)

        Modifies the geometry for the footprints, boundary, or seamlines in a mosaic
        dataset to match those in a feature class.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset whose geometries you want to edit
      target_featureclass_type (String):
          The geometry that you want to change.

          * FOOTPRINT—The footprint polygons in the mosaic dataset.

          * SEAMLINE—The seamline polygons in the mosaic dataset.

          * BOUNDARY—The boundary polygon in the mosaic dataset.
      target_join_field (Field):
          The field in the mosaic dataset to use as a basis for the join.
      input_featureclass (Feature Layer / Raster Catalog Layer):
          The feature class with the new geometry.
      input_join_field (Field):
          The field in the input feature class to use as a basis for the join."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportMosaicDatasetGeometry_management(*gp_fixargs((in_mosaic_dataset, target_featureclass_type, target_join_field, input_featureclass, input_join_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MergeMosaicDatasetItems_management', None)
def MergeMosaicDatasetItems(in_mosaic_dataset=None, where_clause=None, block_field=None, max_rows_per_merged_items=None):
    """MergeMosaicDatasetItems_management(in_mosaic_dataset, {where_clause}, {block_field}, {max_rows_per_merged_items})

        Groups multiple items in a mosaic dataset together as one item.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that has the items that you want to merge.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters to merge in the mosaic dataset.
      block_field {Field}:
          The field in the attribute table that you want to use to group images. Only
          date, numeric, and string fields can be specified as Block fields.
      max_rows_per_merged_items {Long}:
          Limits the number of items to merge. If the maximum is exceeded, the tool will
          create multiple merged items. The default is 1,000 rows."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MergeMosaicDatasetItems_management(*gp_fixargs((in_mosaic_dataset, where_clause, block_field, max_rows_per_merged_items), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveRastersFromMosaicDataset_management', None)
def RemoveRastersFromMosaicDataset(in_mosaic_dataset=None, where_clause=None, update_boundary=None, mark_overviews_items=None, delete_overview_images=None, delete_item_cache=None, remove_items=None, update_cellsize_ranges=None):
    """RemoveRastersFromMosaicDataset_management(in_mosaic_dataset, {where_clause}, {update_boundary}, {mark_overviews_items}, {delete_overview_images}, {delete_item_cache}, {remove_items}, {update_cellsize_ranges})

        Removes selected raster datasets from a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the rasters you want to remove
      where_clause {SQL Expression}:
          An SQL expression to select the raster datasets that you want removed from the
          mosaic dataset.There must be a selection or a query specified; otherwise, the
          tool will not
          run. If you want to delete all the records from the mosaic dataset, specify a
          query that would select all the rasters, such as "OBJECTID>=0".
      update_boundary {Boolean}:
          Updates the boundary polygon of a mosaic dataset. By default, the boundary
          merges all the footprint polygons to create a single boundary representing the
          extent of the valid pixels.

          * UPDATE_BOUNDARY—The boundary will be updated. This is the default.

          * NO_BOUNDARY— The boundary will not be updated.
      mark_overviews_items {Boolean}:
          When the rasters in a mosaic catalog have been removed, any overviews created
          using those rasters may no longer be accurate; therefore, they can be identified
          so they can be updated or removed if they are no longer needed.

          * MARK_OVERVIEW_ITEMS—The affected overviews will be identified. This is the
          default.

          * NO_MARK_OVERVIEW_ITEMS—The affected overviews will not be identified.
      delete_overview_images {Boolean}:
          Remove overviews associated with the selected rasters.

          * DELETE_OVERVIEW_IMAGES—Delete overviews associated with the slected rasters.
          This is the default.

          * NO_DELETE_OVERVIEW_IMAGES— Remove overviews associated with the selected
          rasters.
      delete_item_cache {Boolean}:
          Remove cache that is based on any source raster datasets that you are removing
          from the mosaic dataset.

          * DELETE_ITEM_CACHE—Remove the item and its corresponding cache. This is the
          default.

          * NO_DELETE_ITEM_CACHE—Keep the cache as part of the mosaic dataset.
      remove_items {Boolean}:
          Remove item, cache, overviews, and raster datasets. Or, remove only the cache
          and overviews, and keep the raster datasets.

          * REMOVE_MOSAICDATASET_ITEMS—Remove the item from the mosaic dataset. This is
          the default.

          * NO_REMOVE_MOSAICDATASET_ITEMS—Remove the item cache and any associated
          overviews, but not the item itself.
      update_cellsize_ranges {Boolean}:
          Update cell size ranges for the mosaic dataset. Choose this option if you are
          removing all of the imagery at a specific cell size.

          * UPDATE_CELL_SIZES—Update the cell size ranges. This is the default.

          * NO_CELL_SIZES—Do not update the cell size ranges."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveRastersFromMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, where_clause, update_boundary, mark_overviews_items, delete_overview_images, delete_item_cache, remove_items, update_cellsize_ranges), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RepairMosaicDatasetPaths_management', None)
def RepairMosaicDatasetPaths(in_mosaic_dataset=None, paths_list=None, where_clause=None):
    """RepairMosaicDatasetPaths_management(in_mosaic_dataset, paths_list;paths_list..., {where_clause})

        Resets paths to source imagery if you have moved or copied a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset with the broken paths.
      paths_list (Value Table):
          A list of the paths to remap. Include the current path stored in the mosaic
          dataset and the path to which it will be changed. You can enter an asterisk (*)
          as the original path if you wish to change all your paths.
      where_clause {SQL Expression}:
          An SQL expression to limit the repairs to selected rasters within the mosaic
          dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RepairMosaicDatasetPaths_management(*gp_fixargs((in_mosaic_dataset, paths_list, where_clause), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetMosaicDatasetProperties_management', None)
def SetMosaicDatasetProperties(in_mosaic_dataset=None, rows_maximum_imagesize=None, columns_maximum_imagesize=None, allowed_compressions=None, default_compression_type=None, JPEG_quality=None, LERC_Tolerance=None, resampling_type=None, clip_to_footprints=None, footprints_may_contain_nodata=None, clip_to_boundary=None, color_correction=None, allowed_mensuration_capabilities=None, default_mensuration_capabilities=None, allowed_mosaic_methods=None, default_mosaic_method=None, order_field=None, order_base=None, sorting_order=None, mosaic_operator=None, blend_width=None, view_point_x=None, view_point_y=None, max_num_per_mosaic=None, cell_size_tolerance=None, cell_size=None, metadata_level=None, transmission_fields=None, use_time=None, start_time_field=None, end_time_field=None, time_format=None, geographic_transform=None, max_num_of_download_items=None, max_num_of_records_returned=None, data_source_type=None, minimum_pixel_contribution=None, processing_templates=None, default_processing_template=None):
    """SetMosaicDatasetProperties_management(in_mosaic_dataset, {rows_maximum_imagesize}, {columns_maximum_imagesize}, {allowed_compressions;allowed_compressions...}, {default_compression_type}, {JPEG_quality}, {LERC_Tolerance}, {resampling_type}, {clip_to_footprints}, {footprints_may_contain_nodata}, {clip_to_boundary}, {color_correction}, {allowed_mensuration_capabilities;allowed_mensuration_capabilities...}, {default_mensuration_capabilities}, {allowed_mosaic_methods;allowed_mosaic_methods...}, {default_mosaic_method}, {order_field}, {order_base}, {sorting_order}, {mosaic_operator}, {blend_width}, {view_point_x}, {view_point_y}, {max_num_per_mosaic}, {cell_size_tolerance}, {cell_size}, {metadata_level}, {transmission_fields;transmission_fields...}, {use_time}, {start_time_field}, {end_time_field}, {time_format}, {geographic_transform;geographic_transform...}, {max_num_of_download_items}, {max_num_of_records_returned}, {data_source_type}, {minimum_pixel_contribution}, {processing_templates;processing_templates...}, {default_processing_template})

        Defines the defaults for displaying a mosaic dataset and serving it as an image
        service.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset whose properties need to be set.
      rows_maximum_imagesize {Long}:
          The maximum number of rows for the mosaicked image, generated by the mosaic
          dataset for each request. This can help control how much work your server has to
          do when clients see your imagery. A higher number will create a more detailed
          image, but will also increase the amount of time to process the mosaic dataset.
          It is possible to set the value too small, and the image may not display.
      columns_maximum_imagesize {Long}:
          The maximum number of columns for the mosaicked image, generated by the mosaic
          dataset for each request. This can help control how much work your server has to
          do when clients see your imagery. A higher number will create a more detailed
          image, but will also increase the amount of time to process the mosaic dataset.
          It is possible to set the value too small, and the image may not display.
      allowed_compressions {String}:
          Define the method of compression for transmitting the mosaicked image from the
          computer to the display (or from the server to the client).

          * None—No compression will be used.

          * JPEG— Compresses up to 8:1 and is suitable for backdrops

          * LZ77— Compresses approximately 2:1. Suitable for analysis.

          * LERC—Compresses between 10:1 and 20:1. Compresses fast and is suitable for
          serving raw imagery with high bit-depth (12-bit to 32-bit)
      default_compression_type {String}:
          Set the default compression type. The default compression must be in the
          allowed_compressions list or already set in the mosaic dataset's Allowed
          Compression Methods property.
      JPEG_quality {Long}:
          The compression quality when using JPEG. Compression quality ranges from 1 to
          100. A higher number means better image quality but less compression.
      LERC_Tolerance {Double}:
          Limits the per pixel error when using LERC compression. This value is specified
          in the units of the mosaic dataset. For example, if the error is 10 centimeters
          and the mosaic dataset is in meters, enter 0.1.
      resampling_type {String}:
          Determines how pixel values will be calculated when the dataset is displayed at
          small scales. Choose an appropriate technique based on the type of data you
          have.

          * NEAREST—The fastest resampling method, and it minimizes changes to pixel
          values. Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging, based on distance,
          the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC—Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image, but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY—Determines the value of each pixel based on the most popular value
          within a 3x3 window. Suitable for discrete data.
      clip_to_footprints {Boolean}:
          Often the raster dataset and its footprint have the same extent. If they
          differ, you can clip the raster dataset to the footprint.

          * NOT_CLIP—Do not clip the raster to the footprint. This is the default.

          * CLIP—Clip the rasters to the footprint.
      footprints_may_contain_nodata {Boolean}:
          Allow for pixels that have NoData values.

          *  FOOTPRINTS_MAY_CONTAIN_NODATA—Show pixels with NoData values. This is the
          default.

          *  FOOTPRINTS_DO_NOT_CONTAIN_NODATA—Do not show pixels with NoData values. Note
          that while you may see an improvement in performance, if your imagery does have
          NoData values, they will appear as holes in your mosaic dataset.
      clip_to_boundary {Boolean}:
          Often the mosaic dataset and its boundary have the same extent. If they differ,
          you can clip the mosaic dataset to the boundary.

          * CLIP— Clip the mosaicked image to the boundary. This is the default.

          * NOT_CLIP—Do not clip the mosaicked image to the boundary.
      color_correction {Boolean}:
          Enable color correction on the mosaic dataset.

          * NOT_APPLY—Keep color correction off. This is the default.

          * APPLY—Use the color correction that has been set up for the mosaic dataset.
      allowed_mensuration_capabilities {String}:
          Choose which measurements your viewers can perform on the mosaic dataset. The
          ability to perform vertical measurements is dependent on your imagery and may
          require a DEM.

          * None—No mensuration capabilities will be allowed.

          * Basic— Allow ground measurements such as distance, point, centroid, and area
          calculations.

          * Base-Top Height—Allow measurements from the base to the top of features.
          Rational polynomial coefficients must be imbedded within the imagery.

          * Base-Top Shadow Height—Allow measurements from the base of a feature to the
          top of its shadow. Sun azimuth and sun elevation information is required.

          * Top-Top Shadow Height—Allow measurements from the top of a feature to the top
          of its shadow. Sun azimuth, sun elevation, and rational polynomial coefficients
          are required.

          * 3D—A DEM must be available.
      default_mensuration_capabilities {String}:
          Choose the default mensuration capability for this mosaic dataset. The default
          must be set in the allowed_mensuration_capabilities parameter list or already
          set in the mosaic dataset's Mensuration Capabilities property.
      allowed_mosaic_methods {String}:
          Define the rules for displaying overlapping imagery.

          * None—Order rasters based on the ObjectID in the mosaic dataset attribute
          table.

          * Center—Display imagery that is closest to the center of the screen.

          * NorthWest—Display imagery that is closest to the northwest corner of the
          mosaic dataset boundary.

          * LockRaster—Select specific raster datasets to display.

          * ByAttribute—Display and prioritize imagery based on a field in from the
          attribute table.

          * Nadir—Display the rasters with viewing angles closest to zero.

          * Viewpoint—Display imagery that is closest to a selected viewing angle.

          * Seamline—Smooth transitions between images using seamlines.
      default_mosaic_method {String}:
          Choose the default mosaic method for this mosaic dataset. The default must be
          set in the allowed_mosaic_methods parameter list or already set in the mosaic
          dataset's Allowed Mosaic Methods property.
      order_field {String}:
          Choose the default field to use when ordering rasters using the ByAttribute
          mosaic method. The list of fields is defined as those in the attribute table
          that are of type metadata and are integer. This list can include, but is not
          limited to:

          * Name

          * MinPS

          * MaxPS

          * LowPS

          * HighPS

          * Tag

          * GroupName

          * ProductName

          * CenterX

          * CenterY

          * ZOrder

          * Shape_Length

          * Shape_Area
          If your field is a numeric or date field, then the order_base parameter needs to
          be set.This parameter is not needed if ByAttribute is not an allowed mosaic
          method.
      order_base {String}:
          Sort the rasters based on their difference from this value in the field selected
          in the order_field parameterIf you are using a Date attribute, then it needs to
          be in one of the following
          formats:

          * YYYY/MM/DD HH:mm:ss.s

          * YYYY/MM/DD HH:mm:ss

          * YYYY/MM/DD HH:mm

          * YYYY/MM/DD HH

          * YYYY/MM/DD

          * YYYY/MM

          * YYYY
           This parameter needs to be specified only if ByAttribute is specified for the
          allowed_mosaic_method parameter.
      sorting_order {Boolean}:
          Choose whether to sort your rasters in an ascending or descending order.

          * ASCENDING —Sort ascending. This is the default setting.

          * DESCENDING—Sort descending.
           This parameter needs to be specified only if ByAttribute is specified for the
          allowed_mosaic_method parameter.
      mosaic_operator {String}:
          Define rules for resolving overlapping pixels.

          * FIRST—Display the highest ranked image based on the mosaic method.

          * LAST—Display the lowest ranked image based on the mosaic method.

          * MIN—Display the lowest pixel values.

          * MAX—Display the highest pixel values.

          * MEAN—Use arithmetic mean to average overlapping pixels.

          * BLEND—Use a distance weighted algorithm to average overlapping pixels.

          * SUM—Add all of the overlapping pixel values.
      blend_width {Long}:
          Set the number of pixels over which to apply the BLEND mosaic_operator.
      view_point_x {Double}:
          When using the viewpoint mosaic method, you can horizontally shift the center of
          the image using this parameter. The units are the same as the spatial reference
          system.
      view_point_y {Double}:
          When using the viewpoint mosaic method, you can vertically shift the center of
          the image using this parameter. The units are the same as the spatial reference
          system.
      max_num_per_mosaic {Long}:
          Set the maximum number of raster datasets that can be displayed at a given time
          in a mosaic dataset.
      cell_size_tolerance {Double}:
          Consider images of similar spatial resolutions as having the same nominal
          resolution. For example, with a factor of 0.1, all images with cell sizes within
          10 percent of each other will be grouped together for tools and operations that
          use cell sizes.
      cell_size {Cell Size XY}:
          Set the cell size of the mosaic dataset using an existing raster dataset or
          specify its width (x) and height (y). If you specify the cell size, you can use
          a single value for a square cell size, or X and Y values for a rectangular cell
          size.
      metadata_level {String}:
          Set the level of metadata to expose from the server to a client when publishing
          the mosaic dataset.

          * FULL—Transmit metadata about processing applied at the mosaic dataset level as
          well as metadata related to the individual raster datasets.

          * NONE—No metadata will be exposed to the client.

          * BASIC—Transmit metadata related to individual raster datasets, such as the
          number of columns and rows, cell size, and spatial reference information.
      transmission_fields {String}:
          Limit the fields in the attribute table that clients can view. By default, the
          list includes:

          * Name

          * MinPS

          * MaxPS

          * LowPS

          * HighPS

          * Tag

          * GroupName

          * ProductName

          * CenterX

          * CenterY

          * ZOrder

          * Shape_Length

          * Shape_Area
      use_time {Boolean}:
          Enable animation through time on the mosaic dataset time aware. If time is
          activated, you need to specify the start and end fields, and the time format.

          * DISABLED —The mosaic dataset will not be time aware. This is the default.

          * ENABLED—The mosaic dataset will be time aware. This allows the client to use
          the Time Slider.
      start_time_field {String}:
          The field from the attribute table that shows the start time.
      end_time_field {String}:
          The field from the attribute table that shows the end time.
      time_format {String}:
          Select the format that represents time in the fields chosen above.

          * YYYY—Year

          * YYYYMM—Year and month

          * YYYY/MM—Year and month

          * YYYY-MM—Year and month

          * YYYYMMDD—Year, month, and day

          * YYYY/MM/DD—Year, month, and day

          * YYYY-MM-DD—Year, month, and day

          * YYYYMMDDhhmmss—Year, month, day, hour, minute, and seconds

          * YYYY/MM/DD hh:mm:ss—Year, month, day, hour, minute, and seconds

          * YYYY-MM-DD hh:mm:ss—Year, month, day, hour, minute, and seconds

          * YYYYMMDDhhmmss.s—Year, month, day, hour, minute, seconds, and fraction of
          seconds

          * YYYY/MM/DD hh:mm:ss.s—Year, month, day, hour, minute, seconds, and fraction of
          seconds

          * YYYY-MM-DD hh:mm:ss.s—Year, month, day, hour, minute, seconds, and fraction of
          seconds
      geographic_transform {String}:
          The geographic transformations to associate with this mosaic dataset.
      max_num_of_download_items {Long}:
          Limit the number of raster datasets that can be downloaded per request.
      max_num_of_records_returned {Long}:
          Limit the number of records that can be downloaded per request.
      data_source_type {String}:
          Define the type of imagery in the mosaic dataset.

          *  GENERIC—The mosaic dataset does not have a specified data type.

          * THEMATIC—Thematic data has discrete values, such as land cover.

          * PROCESSED—The mosaic dataset has been color adjusted.

          * ELEVATION—The mosaic dataset contains elevation data.

          * SCIENTIFIC—The mosaic dataset contains scientific data.

          * VECTOR_UV—The mosaic dataset has two variables.

          * VECTOR_MAGDIR—The mosaic dataset has magnitude and direction.
      minimum_pixel_contribution {Long}:
          Set the minimum number of pixels required for a mosaic dataset item to be
          considered significant enough to be used in the mosaic dataset. Because of
          overlapping imagery, you may have an item that is displaying a small sliver of
          its overall image. Skipping these mosaic dataset items will help the performance
          of the mosaic dataset.
      processing_templates {rft*|*xml}:
          Choose the function chains that you want to use to process a mosaic dataset or
          the mosaic dataset items, on-the-fly. You can add, remove, or reorder the
          function chains.All the template names that are added need to be unique.For
          information on how to work with function chains, refer to Editing function
          chain templates .
      default_processing_template {String}:
          Define the default function chain. The default function chain will be applied
          when the mosaic dataset is accessed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetMosaicDatasetProperties_management(*gp_fixargs((in_mosaic_dataset, rows_maximum_imagesize, columns_maximum_imagesize, allowed_compressions, default_compression_type, JPEG_quality, LERC_Tolerance, resampling_type, clip_to_footprints, footprints_may_contain_nodata, clip_to_boundary, color_correction, allowed_mensuration_capabilities, default_mensuration_capabilities, allowed_mosaic_methods, default_mosaic_method, order_field, order_base, sorting_order, mosaic_operator, blend_width, view_point_x, view_point_y, max_num_per_mosaic, cell_size_tolerance, cell_size, metadata_level, transmission_fields, use_time, start_time_field, end_time_field, time_format, geographic_transform, max_num_of_download_items, max_num_of_records_returned, data_source_type, minimum_pixel_contribution, processing_templates, default_processing_template), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SplitMosaicDatasetItems_management', None)
def SplitMosaicDatasetItems(in_mosaic_dataset=None, where_clause=None):
    """SplitMosaicDatasetItems_management(in_mosaic_dataset, {where_clause})

        Splits mosaic dataset items that were merged together using Merge Mosaic
        Dataset Items.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the items to split.
      where_clause {SQL Expression}:
          An SQL expresseion to select items to split.If the query does not contain any
          previously merged items, the tool will return
          an error."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SplitMosaicDatasetItems_management(*gp_fixargs((in_mosaic_dataset, where_clause), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SynchronizeMosaicDataset_management', None)
def SynchronizeMosaicDataset(in_mosaic_dataset=None, where_clause=None, new_items=None, sync_only_stale=None, update_cellsize_ranges=None, update_boundary=None, update_overviews=None, build_pyramids=None, calculate_statistics=None, build_thumbnails=None, build_item_cache=None, rebuild_raster=None, update_fields=None, fields_to_update=None, existing_items=None, broken_items=None, skip_existing_items=None, refresh_aggregate_info=None):
    """SynchronizeMosaicDataset_management(in_mosaic_dataset, {where_clause}, {new_items}, {sync_only_stale}, {update_cellsize_ranges}, {update_boundary}, {update_overviews}, {build_pyramids}, {calculate_statistics}, {build_thumbnails}, {build_item_cache}, {rebuild_raster}, {update_fields}, {fields_to_update;fields_to_update...}, {existing_items}, {broken_items}, {skip_existing_items}, {refresh_aggregate_info})

        Keeps your mosaic dataset up to date. In addition to syncing data, you can
        update overviews if the underlying imagery has been changed, generate new
        overviews and cache, and restore the original configuration of mosaic dataset
        items. You can also remove paths to source data with this tool. To repair paths,
        you need to use the Repair Mosaic Dataset Paths tool.Synchronization is a one-
        way operation: changes in the source data can be
        synchronized to the mosaic dataset’s attribute table, thereby updating the
        mosaic dataset's attribute table. Changes in the mosaic dataset's attribute
        table will not affect the source data.Changes made with the synchronization
        cannot be undone. You may want to create a
        backup copy if you've made modifications to your mosaic data that could be
        overwritten.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to synchronize.
      where_clause {SQL Expression}:
          An SQL expression to select which mosaic dataset items will be synchronized. If
          an expression is not provided, all dataset items will be updated.
      new_items {Boolean}:
          Choose whether to  include new items when synchronizing, and then specify which
          options to update the new items with.If you choose to use this option, the
          item's workspace will be searched for new
          data. When data is added to the mosaic dataset, it will use the same raster type
          as the other items within the same workspace.

          * NO_NEW_ITEMS—New items will not be added when synchronizing. This is the
          default.

          * UPDATE_WITH_NEW_ITEMS—Update the mosaic dataset with new items in the
          workspaces. Optionally, you can modify the existing items using
          OVERWRITE_EXISTING_ITEMS keyword in the skip_existing_items parameter.
      sync_only_stale {Boolean}:
          Choose whether to update mosaic dataset items where the underlying raster
          datasets have been modified due to synchronizing. For example, building pyramids
          or updating the georeferencing of the rasters will affect how the overviews are
          rendered.

          * SYNC_STALE—Only update the items where the underlying raster datasets have
          been modified. This is the default.

          * SYNC_ALL—Update all of the items in the mosaic dataset.
      update_cellsize_ranges {Boolean}:
          Choose whether to update the cell size ranges.

          * UPDATE_CELL_SIZES—Recalculate the cell size for the entire mosaic dataset, but
          only for items that have an invalid visibility. This is the default.

          * NO_CELL_SIZES— Do not recalculate the cell size ranges.
      update_boundary {Boolean}:
          Choose whether to update the boundary.

          * UPDATE_BOUNDARY— The boundary will be rebuilt after the mosaic dataset is
          synchronized. Use this option if syncing will change the extent of the mosaic
          dataset. This is the default.

          * NO_BOUNDARY— The boundary will not be rebuilt.
      update_overviews {Boolean}:
          Choose whether to update any obsolete overviews. The overview becomes obsolete
          if any underlying rasters have been modified due to synchronizing.

          * NO_OVERVIEWS— The overviews will not be rebuilt. This is the default.

          * UPDATE_OVERVIEWS— The affected overviews will be rebuilt after the mosaic
          dataset is synchronized.
      build_pyramids {Boolean}:
          Choose whether to build pyramids for the specified mosaic dataset items.
          Pyramids can be built for each raster item in the mosaic dataset. Pyramids can
          improve the speed at which each raster is displayed.

          * NO_PYRAMIDS—Pyramids will not be generated. This is the default.

          * BUILD_PYRAMIDS— Pyramids will be generated for all the raster items that were
          updated due to synchronization.
          Pyramids will not be built for items that were added due to synchronization.
      calculate_statistics {Boolean}:
          Choose whether to calculate statistics for the specified mosaic dataset items.
          Statistics are required for your mosaic dataset when performing certain tasks,
          such as applying a contrast stretch.

          * NO_STATISTICS—Statistics will not be calculated. This is the default.

          * CALCULATE_STATISTICS— Statistics will be calculated for the mosaic dataset
          items that were updated due to synchronization.
          Statistics will not be built for items that were added due to synchronization.
      build_thumbnails {Boolean}:
          Choose whether to build thumbnails for the specified mosaic dataset items.
          Thumbnails are small, highly resampled images that can be created for each
          raster item in the mosaic definition. Thumbnails can be accessed when the mosaic
          dataset is accessed as an image service and will display as part of the item
          description.

          * NO_THUMBNAILS—No thumbnails will be created or updated. This is the default.

          * BUILD_THUMBNAILS—Thumbnails will be generated or updated for all the raster
          items that were updated due to synchronization.
          Thumbnails will not be built for items that were added due to synchronization.
      build_item_cache {Boolean}:
          Choose whether to build a cache for the specified mosaic dataset items. A cache
          can be created when you've added data using the LAS, Terrain, or LAS Dataset
          raster types. Items can also be cached using the Cached Raster function.

          * NO_ITEM_CACHE—No cache will be created or updated. This is the default.

          *  BUILD_ITEM_CACHE—The cache will be generated or updated for all the raster
          items that were updated due to synchronization.
          The cache will not be built for items that were added due to synchronization.
      rebuild_raster {Boolean}:
          Choose whether to rebuild the raster items from the data source using the
          original raster type.

          * REBUILD_RASTER—Rebuild the rasters from the source data. You will lose any
          changes that you have performed on selected items in the mosaic dataset. This is
          the default.

          * NO_RASTER—Do not rebuild the rasters. Other primary fields are reset if the
          update_fields parameter is set to UPDATE_FIELDS.
          This will only affect items that will be synchronized. This parameter is not
          applicable if the new_items parameter has been set to UPDATE_WITH_NEW_ITEMS.
      update_fields {Boolean}:
          Choose whether to update the fields within the table. This will only affect
          items that will be synchronized.

          * UPDATE_FIELDS—Update the fields from the source files. This is the default.

          * NO_FIELDS—Do not reset the fields within the table from the source.
          If you choose to update the fields, you can control which fields are updates by
          specifying them in the fields_to_update parameter. If you have made edits to
          some of the fields, you may want to remove them in the fields_to_update
          parameter.
      fields_to_update {String}:
          Specify which fields should be updated.This parameter is only valid if the
          option for the update_fields parameter is
          set to UPDATE_FIELDS.If you have made edits to some of the fields, you may want
          to make sure they are
          not listed.The RASTER field can be refreshed, even if the REBUILD_RASTER is not
          specified.
          However, if REBUILD_RASTER is specified, the RASTER field is rebuilt, even if
          this field is not specified.
      existing_items {Boolean}:
          Choose whether you would like to update existing items within your mosaic
          dataset.If you choose this option, you can then choose which existing parameters
          you
          would like to update: sync_only_stale, build_pyramids, calculate_statistics,
          build_thumbnails, build_item_cache, update_fields, or fields_to_update.

          * UPDATE_EXISTING_ITEMS—Existing items will be updated with the parameters that
          you have chosen to update. This is the default.

          * IGNORE_EXISTING_ITEMS—Existing items will not be updated.
      broken_items {Boolean}:
          Choose whether you want to remove any broken links.Make sure that all your
          network connections are working properly—this tool will
          remove any items that cannot be accessed.

          * IGNORE_BROKEN_ITEMS—Items that have broken links will not be removed from the
          mosaic dataset. This is the default.

          * REMOVE_BROKEN_ITEMS—Items that have broken links will be removed from the
          mosaic dataset.
      skip_existing_items {Boolean}:
          If UPDATE_WITH_NEW_ITEMS is specified in the new_items parameter then you can
          also choose whether to skip or to update existing mosaic dataset items with the
          modified files from disk.

          *  SKIP_EXISTING_ITEMS—While adding new mosaic dataset items, the tool will not
          update existing mosaic dataset items. This is the default.

          * OVERWRITE_EXISTING_ITEMS—While adding new mosaic dataset items, the tool will
          update existing mosaic dataset items that correspond to modified files on disk.
      refresh_aggregate_info {Boolean}:
          Choose whether to re-include data that may have been removed from the mosaic
          dataset.

          *  NO_REFRESH_INFO—When synchronizing, do not include any rasters that may have
          been removed from the mosaic dataset. This is the default.

          * REFRESH_INFO—When synchronizing, include rasters that may have been removed
          from the mosaic dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SynchronizeMosaicDataset_management(*gp_fixargs((in_mosaic_dataset, where_clause, new_items, sync_only_stale, update_cellsize_ranges, update_boundary, update_overviews, build_pyramids, calculate_statistics, build_thumbnails, build_item_cache, rebuild_raster, update_fields, fields_to_update, existing_items, broken_items, skip_existing_items, refresh_aggregate_info), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Mosaic Dataset\Block Adjustment toolset
@gptooldoc('AnalyzeControlPoints_management', None)
def AnalyzeControlPoints(in_mosaic_dataset=None, in_control_points=None, out_coverage_table=None, out_overlap_table=None, in_mask_dataset=None, minimum_area=None):
    """AnalyzeControlPoints_management(in_mosaic_dataset, in_control_points, out_coverage_table, out_overlap_table, {in_mask_dataset}, {minimum_area})

        Analyzes the control point coverage and identifies the areas that need
        additional control points to improve the block adjust result. The tool will
        check each image and provide the following:

        * The number of control points for each image


        * The percentage of image covered by the control points (point distribution)


        * The overlap areas


        * The number of control points within overlap areas

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset against which to analyze the control points.
      in_control_points (Feature Layer):
          The input control point feature class.It is normally created from the Compute
          Tie Points or the Compute Control Points
          tool.
      in_mask_dataset {Feature Layer}:
          A polygon feature class used to exclude areas that you do not want in the
          analysis of the control points computation.A field with a name of mask can
          control the inclusion or exclusion of areas. A
          value of 1 indicates that the areas defined by the polygons (inside) will be
          excluded from the computation. A value of 2 indicates the defined polygons
          (inside) will be included in the computation while areas outside of the polygons
          will be excluded.
      minimum_area {Double}:
          Specify the minimum percent that the overlap area must be, in relation to the
          image. Areas that are lower than the specified percent threshold will be
          excluded from the analysis.You want to make sure you do not have areas that are
          too small; otherwise, you
          will have small slivers being analyzed.

     OUTPUTS:
      out_coverage_table (Feature Class):
          A polygon feature class output that contains the control point coverage and the
          percentage of the area within the corresponding image.
      out_overlap_table (Feature Class):
          A polygon feature class output that contains all the overlap areas between
          images."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AnalyzeControlPoints_management(*gp_fixargs((in_mosaic_dataset, in_control_points, out_coverage_table, out_overlap_table, in_mask_dataset, minimum_area), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AppendControlPoints_management', None)
def AppendControlPoints(in_master_control_points=None, in_input_control_points=None, in_z_field=None, in_tag_field=None, in_dem=None):
    """AppendControlPoints_management(in_master_control_points, in_input_control_points, {in_z_field}, {in_tag_field}, {in_dem})

        Combines control points to an existing control point table. The points to be
        appended are the results from either the Compute Tie Points
        tool, Compute Control Points tool, or a point feature class.

     INPUTS:
      in_master_control_points (Feature Class / Feature Layer):
          The input control point table. This is usually the output from the Compute Tie
          Points tool.
      in_input_control_points (Feature Class / Feature Layer):
          A point feature class that stores control points. It could be the control point
          table created from the Compute Control Points tool, the Compute Tie Points tool,
          or a point feature class that has ground control points.
      in_z_field {Field}:
          The field that stores the control point Z values.If both the Z Value Field Name
          and the Input DEM parameters are set, then the Z
          value field is used. If neither the Z Value Field Name nor Input DEM parameters
          are set, then the Z value is set to 0 for all ground control points and check
          points.
      in_tag_field {Field}:
          A field in the input control point table that has a unique value. This field
          will be added to the target control point table, where the tag field can be used
          to bring in identifiers associated with ground control points.
      in_dem {Raster Layer / Mosaic Layer / Raster Dataset / Mosaic Dataset}:
          A DEM to use to obtain the Z value for the control points in the input control
          point table.If both the Z Value Field Name and Input DEM parameters are  set,
          then the Z
          value field is used. If neither the Z Value Field Name nor Input DEM parameters
          are  set, then the Z value is set to 0 for all ground control points and check
          points."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AppendControlPoints_management(*gp_fixargs((in_master_control_points, in_input_control_points, in_z_field, in_tag_field, in_dem), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ApplyBlockAdjustment_management', None)
def ApplyBlockAdjustment(in_mosaic_dataset=None, adjustment_operation=None, input_solution_table=None, pan_to_ms_scaling_factor=None):
    """ApplyBlockAdjustment_management(in_mosaic_dataset, adjustment_operation, {input_solution_table}, {pan_to_ms_scaling_factor})

        Applies the geographic adjustments to the mosaic dataset items. This tool uses
        the solution file from the Compute Adjustments tool.This tool can also reset the
        geographic adjustments back to the original
        location.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset to adjust.
      adjustment_operation (String):
          Choose whether you want to adjust the mosaic dataset using the solution table,
          or if you want to reset the mosaic dataset so there are no adjustments applied.

          * ADJUST—Adjust the mosaic dataset using the input solution table.

          * RESET—Reset the mosaic dataset so there are no adjustments applied to it.
      input_solution_table {Table View}:
          Specify a solution table to use when adjusting your mosaic dataset; this is the
          output from the Compute Block Adjustments tool.
      pan_to_ms_scaling_factor {Double}:
          If your mosaic dataset contains pansharpened rasters, specify the scaling
          factor between the pansharpened resolution and the multispectral resolution."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ApplyBlockAdjustment_management(*gp_fixargs((in_mosaic_dataset, adjustment_operation, input_solution_table, pan_to_ms_scaling_factor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ComputeBlockAdjustment_management', None)
def ComputeBlockAdjustment(in_mosaic_dataset=None, in_control_points=None, transformation_type=None, out_solution_table=None, out_solution_point_table=None, maximum_residual_value=None, adjustment_options=None):
    """ComputeBlockAdjustment_management(in_mosaic_dataset, in_control_points, transformation_type, out_solution_table, {out_solution_point_table}, {maximum_residual_value}, {adjustment_options;adjustment_options...})

        This tool is used to compute the adjustments to the mosaic dataset. This tool
        will create a solution table that can be used to apply the actual adjustments.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be adjusted.
      in_control_points (Feature Layer):
          The control point table that includes tie points and ground control points.You
          can use the output from the Compute Tie Points tool, or a refined control
          point table edited by the Block Adjustment Window.
      transformation_type (String):
          Choose which type of transformation will be used when adjusting the mosaic
          dataset.

          * POLYORDER0—A zero-order polynomial is used in the block adjustment
          computation. This is commonly used when your data is in flat area.

          * POLYORDER1—A first-order polynomial (affine) is used in the block adjustment
          computation. This is the default.
      maximum_residual_value {Double}:
          A threshold that is used in block adjust computation. When polynomial
          transformation type is either POLYORDER0 or POLYORDER1, the units for this
          parameter will be in map units.The block adjustment computation is an iterative
          process. This value will
          control when the block adjustment iterations should stop. The iterations will
          continue till the residuals are below the maximum value, or when ten iterations
          have been completed—even if the residuals are above the maximum value specified.
          The default value is 0.7.The adjustment_options parameter also allows you to
          specify a maximum residual
          threshold value by setting a MaxResidualFactor. If both the
          maximum_residual_value and MaxResidualFactor are specified, the tool will ignore
          the MaxResidualFactor.
      adjustment_options {Value Table}:
          Additional options that can fine-tune the adjustment computation.

          * MinResidual —The minimum residual value, which is the lower threshold value.
          When polynomial transformation is either POLYORDER0 or POLYORDER1, the units
          will be in map units and default minimum residual will be 0. The minimum
          residual value and the maximum residual parameter are used in detecting and
          removing points that generate large errors from the block adjustment
          computation.

          * MaxResidualFactor —The maximum residual factor, is a factor used to generate
          maximum (upper threshold) residual. If maximum_residual_value parameter is not
          defined, it will use the MaxResidualFactor * RMS to calculate the upper
          threshold value.The minimum residual value and the maximum residual parameter
          are used in detecting and removing points that generate large errors from block
          adjustment computation.

          * _BAO—The output file that contains the output information from the
          triangulation engine.

          * _BAI  —The output file that contains the input information for the
          triangulation engine.

     OUTPUTS:
      out_solution_table (Table):
          The output solution table containing the adjustments.
      out_solution_point_table {Feature Class}:
          The output solution points table. This will be saved as a polygon feature
          class. This output can be quite large."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ComputeBlockAdjustment_management(*gp_fixargs((in_mosaic_dataset, in_control_points, transformation_type, out_solution_table, out_solution_point_table, maximum_residual_value, adjustment_options), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ComputeControlPoints_management', None)
def ComputeControlPoints(in_mosaic_dataset=None, in_reference_images=None, out_control_points=None, similarity=None, out_image_feature_points=None):
    """ComputeControlPoints_management(in_mosaic_dataset, in_reference_images, out_control_points, {similarity}, {out_image_feature_points})

        Computes the control points between the mosaic dataset and the reference image.
        The control points can then be used in conjunction with tie points to compute
        the adjustments for the mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be used to create control points.
      in_reference_images (Raster Layer / Raster Dataset / Image Service / MapServer / WMS Map / Mosaic Layer / Internet Tiled Layer / Map Server Layer):
          The reference images that will be used to create control points for your mosaic
          dataset. If you have multiple images, create a mosaic dataset from the images
          and use the mosaic dataset as the reference.
      similarity {String}:
          Choose the tolerance level for your control point matching.

          * LOW—The similarity tolerance for finding control points will be low. This
          option will produce the most control points, but some may have a higher level of
          error.

          * MEDIUM—The similarity tolerance for finding control points will be medium.

          * HIGH—The similarity tolerance for finding control points will be high. This
          option will produce the least number of control points, but each matching pair
          will have a lower level of error. This is the default.

     OUTPUTS:
      out_control_points (Feature Class):
          The output control point table. This table will contain the control points that
          were created.
      out_image_feature_points {Feature Class}:
          The output image feature points table. This will be saved as a polygon feature
          class. This output can be quite large."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ComputeControlPoints_management(*gp_fixargs((in_mosaic_dataset, in_reference_images, out_control_points, similarity, out_image_feature_points), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ComputeTiePoints_management', None)
def ComputeTiePoints(in_mosaic_dataset=None, out_control_points=None, similarity=None, in_mask_dataset=None, out_image_features=None):
    """ComputeTiePoints_management(in_mosaic_dataset, out_control_points, {similarity}, {in_mask_dataset}, {out_image_features})

        Computes the tie points between overlapped mosaic dataset items. The tie points
        can then be used to compute the adjustments for the mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The input mosaic dataset that will be used to create tie points.
      similarity {String}:
          Choose the tolerance level for your matching tie points.

          * LOW—The similarity tolerance for the matching pairs will be low. This option
          will produce the most matching pairs, but some of the matches may have a higher
          level of error.

          * MEDIUM—The similarity tolerance for the matching pairs will be medium. This is
          the default.

          * HIGH—The similarity tolerance for the matching pairs will be high. This option
          will produce the least number of matching pairs, but each matching pair will
          have a lower level of error.
      in_mask_dataset {Feature Layer}:
          A polygon feature class that is used to exclude areas that you do not want in
          the computation of control points.A field with a name of mask can control the
          inclusion or exclusion of areas. A
          value of 1 indicates that the areas defined by the polygons (inside) will be
          excluded from the computation. A value of 2 indicates the defined polygons
          (inside) will be included in the computation while areas outside of the polygons
          will be excluded.

     OUTPUTS:
      out_control_points (Feature Class):
          The output control point table. This table will contain the tie points created
          by this tool.
      out_image_features {Feature Class}:
          The output image feature points table. This will be saved as a polygon feature
          class. This output can be quite large."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ComputeTiePoints_management(*gp_fixargs((in_mosaic_dataset, out_control_points, similarity, in_mask_dataset, out_image_features), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Raster Catalog toolset
@gptooldoc('CopyRasterCatalogItems_management', None)
def CopyRasterCatalogItems(in_raster_catalog=None, out_raster_catalog=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None):
    """CopyRasterCatalogItems_management(in_raster_catalog, out_raster_catalog, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Makes a copy of a raster catalog, including all of its contents, or a subset of
        its contents if there is a selection.

     INPUTS:
      in_raster_catalog (Raster Catalog Layer):
          The name and location of the raster catalog to be copied.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database administrator.
      spatial_grid_1 {Double}:
          The Output Spatial Grid 1, 2, and 3 parameters apply only to file geodatabases
          and ArcSDE geodatabases. If you are unfamiliar with setting grid sizes, leave
          these options as 0,0,0 and ArcGIS will compute optimal sizes for you. For more
          information about this parameter, refer to the Add Spatial Index tool
          documentation.
      spatial_grid_2 {Double}:
          Cell size of the second spatial grid. Leave the size at 0 if you only want one
          grid. Otherwise, set the size to at least three times larger than Spatial Grid
          1.
      spatial_grid_3 {Double}:
          Cell size of the third spatial grid. Leave the size at 0 if you only want two
          grids. Otherwise, set the size to at least three times larger than Spatial Grid
          2.

     OUTPUTS:
      out_raster_catalog (Raster Catalog):
          The name and location of the output raster catalog.You can copy your output
          raster catalog to any type of geodatabase: personal,
          file, or ArcSDE."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyRasterCatalogItems_management(*gp_fixargs((in_raster_catalog, out_raster_catalog, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRasterCatalog_management', None)
def CreateRasterCatalog(out_path=None, out_name=None, raster_spatial_reference=None, spatial_reference=None, config_keyword=None, spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None, raster_management_type=None, template_raster_catalog=None):
    """CreateRasterCatalog_management(out_path, out_name, {raster_spatial_reference}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3}, {raster_management_type}, {template_raster_catalog;template_raster_catalog...})

        Creates an empty raster catalog in a geodatabase.

     INPUTS:
      out_path (Workspace):
          The geodatabase to contain the raster catalog. This can be any type of
          geodatabase: personal, file, or ArcSDE.
      out_name (String):
          The name of the raster catalog to be created.
      raster_spatial_reference {Coordinate System}:
          The coordinate system for the raster column in the raster catalog.The spatial
          reference of the raster column is used during data loading as

          * A default spatial reference for those raster datasets that have an unknown
          spatial reference

          * A target spatial reference if you choose to project your raster datasets that
          have different spatial references from the raster column
          The default value is the coordinate system set in the environment settings.
      spatial_reference {Spatial Reference}:
          The coordinate system for the geometry column.The spatial reference for the
          geometry column defines the spatial reference of
          the footprints of the raster datasets.The default value is the coordinate system
          set in the environment settings.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database administrator.
      spatial_grid_1 {Double}:
          The Output Spatial Grid 1, 2, and 3 parameters are used to compute a spatial
          index and only apply to  file geodatabases and ArcSDE geodatabases. If you are
          unfamiliar with setting grid sizes, leave these options as 0,0,0 and ArcGIS will
          compute optimal sizes for you.If you use the default spatial grid index (of
          zero), it is recommended that you
          load data using the Workspace To Raster Catalog tool. If that tool is used to
          load raster datasets, the spatial grid size will be automatically calculated. If
          another tool is used to load raster datasets into a raster catalog, the
          Calculate Default Spatial Grid Index tool needs to be used after the loading is
          completed. For more information about this parameter, refer to the Add Spatial
          Index tool
          documentation.
      spatial_grid_2 {Double}:
          Cell size of the second spatial grid. Leave the size at 0 if you only want one
          grid. Otherwise, set the size to at least three times larger than Spatial Grid
          1.
      spatial_grid_3 {Double}:
          Cell size of the third spatial grid. Leave the size at 0 if you only want two
          grids. Otherwise, set the size to at least three times larger than Spatial Grid
          2.
      raster_management_type {String}:
          Raster datasets within raster catalogs can be managed in two ways: managed or
          unmanaged (by the geodatabase).

          * MANAGED—With a managed raster catalog, the raster datasets inside the raster
          catalog will be physically stored within the geodatabase. When a row (or raster)
          is deleted from the catalog, it is deleted from the geodatabase.

          * UNMANAGED—With an unmanaged raster catalog, the raster catalog only contains
          links or pointers connecting a row to a raster dataset stored outside the
          geodatabase. All raster datasets loaded into an unmanaged raster catalog must be
          a file on disk.
      template_raster_catalog {Raster Catalog Layer}:
          If you want to base your new raster catalog on a template, you can specify a
          template raster catalog. The new raster catalog will then have the same fields
          as the template raster catalog."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRasterCatalog_management(*gp_fixargs((out_path, out_name, raster_spatial_reference, spatial_reference, config_keyword, spatial_grid_1, spatial_grid_2, spatial_grid_3, raster_management_type, template_raster_catalog), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteRasterCatalogItems_management', None)
def DeleteRasterCatalogItems(in_raster_catalog=None):
    """DeleteRasterCatalogItems_management(in_raster_catalog)

        Deletes raster catalog items, including all its contents, or a subset of its
        contents if there is a selection.

     INPUTS:
      in_raster_catalog (Raster Catalog Layer):
          The input raster catalog that will have its items deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteRasterCatalogItems_management(*gp_fixargs((in_raster_catalog,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportRasterCatalogPaths_management', None)
def ExportRasterCatalogPaths(in_raster_catalog=None, export_mode=None, out_table=None):
    """ExportRasterCatalogPaths_management(in_raster_catalog, export_mode, out_table)

        Creates a table listing the paths to the raster datasets contained in an
        unmanaged raster catalog or a mosaic dataset. The table can display all the file
        paths, or just the ones that are broken.

     INPUTS:
      in_raster_catalog (Mosaic Dataset / Raster Catalog Layer / Group Layer / Composite Layer):
          The input unmanaged raster catalog or mosaic dataset.
      export_mode (String):
          Choose what paths to output to the table. You can choose to output all the file
          paths, or just the ones that are broken.Choose the repair mode you would like to
          use.

          * BROKEN—This option will export only the broken paths to the table.

          * ALL—This option will export all the paths to the table.

     OUTPUTS:
      out_table (Table):
          The output table. This table can be created as a DBF file or within a
          geodatabase.The output table will have a field that lists the Source OID. This
          is the OID of
          the row in the original raster catalog table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportRasterCatalogPaths_management(*gp_fixargs((in_raster_catalog, export_mode, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RepairRasterCatalogPaths_management', None)
def RepairRasterCatalogPaths(in_raster_catalog=None, repair_mode=None, original_path=None, new_path=None):
    """RepairRasterCatalogPaths_management(in_raster_catalog, repair_mode, {original_path}, {new_path})

        Repairs broken file paths or deletes broken links within an unmanaged raster
        catalog or a mosaic dataset.

     INPUTS:
      in_raster_catalog (Raster Catalog Layer / Mosaic Dataset / Group Layer / Composite Layer):
          The unmanaged raster catalog or mosaic dataset to be repaired.
      repair_mode (String):
          Choose the repair mode you would like to use.

          * FIX—This option will allow you to fix the paths.

          * REMOVE—This option will remove any broken links that exist.
      original_path {String}:
          Type the original path that needs to be repaired. This is a required parameter
          if the FIX option was chosen.If you want to change all your paths to the new
          path, you are able to use the
          asterisk (*) as the original path.
      new_path {Folder}:
          Type the new path to use. This is a required parameter if the FIX option was
          chosen."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RepairRasterCatalogPaths_management(*gp_fixargs((in_raster_catalog, repair_mode, original_path, new_path), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('WorkspaceToRasterCatalog_management', None)
def WorkspaceToRasterCatalog(in_workspace=None, in_raster_catalog=None, include_subdirectories=None, project=None):
    """WorkspaceToRasterCatalog_management(in_workspace, in_raster_catalog, {include_subdirectories}, {project})

        Loads all the raster datasets stored in the same workspace into an existing
        raster catalog.

     INPUTS:
      in_workspace (Workspace):
          The workspace that contains all the raster datasets to be loaded into the raster
          catalog.
      in_raster_catalog (Raster Catalog):
          An existing raster catalog that will have all the raster datasets from the
          workspace loaded into it.
      include_subdirectories {Boolean}:
          Specify whether to include subdirectories.

          * NONE—Does not include subdirectories. This is the default.

          * INCLUDE_SUBDIRECTORIES—Includes all the raster datasets within the
          subdirectories when loading.
      project {Boolean}:
          Specify whether to project the raster datasets projected on the fly.

          * NONE—All raster datasets are loaded into the raster catalog with the original
          spatial reference of the raster dataset. This is the default.

          * PROJECT_ONFLY—All raster datasets will be projected on the fly (to the
          coordinate system specified in the raster column) when loaded into the raster
          catalog."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.WorkspaceToRasterCatalog_management(*gp_fixargs((in_workspace, in_raster_catalog, include_subdirectories, project), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Raster Dataset toolset
@gptooldoc('CopyRaster_management', None)
def CopyRaster(in_raster=None, out_rasterdataset=None, config_keyword=None, background_value=None, nodata_value=None, onebit_to_eightbit=None, colormap_to_RGB=None, pixel_type=None, scale_pixel_value=None, RGB_to_Colormap=None):
    """CopyRaster_management(in_raster, out_rasterdataset, {config_keyword}, {background_value}, {nodata_value}, {onebit_to_eightbit}, {colormap_to_RGB}, {pixel_type}, {scale_pixel_value}, {RGB_to_Colormap})

        Saves a copy of a raster dataset or converts a mosaic dataset into a single
        raster dataset.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset or mosaic dataset you want to copy.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database administrator.
      background_value {Double}:
          Use this option to remove the unwanted values created around the raster data.
          The value specified will be distinguished from other valuable data in the raster
          dataset. For example, a value of zero along the raster dataset's borders will be
          distinguished from zero values within the raster dataset.The pixel value
          specified will be set to NoData in the output raster dataset.For file-based
          rasters and geodatabase rasters, the Ignore Background Value must
          be set to the same value as NoData in order for the background value to be
          ignored. Enterprise and geodatabase rasters will work without this extra step.
      nodata_value {String}:
          All the pixels with the specified value will be set to NoData in the output
          raster dataset.
      onebit_to_eightbit {Boolean}:
          Choose whether the input 1-bit raster dataset will be converted to an 8-bit
          raster dataset. In this conversion the value 1 in the input raster dataset will
          be changed to 255 in the output raster dataset. This is useful when importing a
          1-bit raster dataset to a geodatabase. One-bit raster datasets have 8-bit
          pyramid layers when stored in a file system, but in a geodatabase, 1-bit raster
          datasets can only have 1-bit pyramid layers, which makes the display unpleasant.
          By converting the data to 8 bit in a geodatabase, the pyramid layers are built
          as 8 bit instead of 1 bit, resulting in a proper raster dataset in the display.

          * NONE—No conversion will be done. This is the default.

          * OneBitTo8Bit—The input raster will be converted.
      colormap_to_RGB {Boolean}:
          If the input raster dataset has a color map, the output raster dataset can be
          converted to a three-band output raster dataset. This is useful when mosaicking
          rasters with different color maps.

          * NONE—No conversion will occur. This is the default.

          * ColormapToRGB—The input dataset will be converted.
      pixel_type {String}:
          Set the bit depth, or radiometric resolution, of the raster or mosaic dataset.
          If not defined, it will be taken from the first raster dataset.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      scale_pixel_value {Boolean}:
          When the output is a different pixel type than the input (such as 16 bit to 8
          bit) you can choose to have the values scaled to fit into the new range;
          otherwise, the values that do not fit into the new pixel range will be
          discarded.If scaling up, such as 8 bit to 16 bit, the minimum and maximum of the
          8-bit
          values will be scaled to the minimum and maximum in the 16-bit range. If scaling
          down, such as 16 bit to 8 bit, the minimum and maximum of the 16-bit values will
          be scaled to the minimum and maximum in the 8-bit range.

          * NONE—The pixel values will remain the same and will not be scaled. Any values
          that do not fit within the value range will be discarded. This is the default.

          * ScalePixelValue—The pixel values will be scaled to the new pixel type. When
          you scale your pixel depth, your raster will display the same, but the values
          will be scaled to the new bit depth that was specified.
      RGB_to_Colormap {Boolean}:
          Convert an 8-bit, 3-band (RGB) raster dataset to a single-band raster dataset
          with a color map. This operation suppresses noise that is often found in scanned
          images and is ideal for screen captures, scanned maps, or scanned documents.
          This is not recommended for satellite or aerial imagery or thematic raster data.

          * NONE—Do not convert RGB

          * RGBToColormap—Convert to colormap

     OUTPUTS:
      out_rasterdataset (Raster Dataset / Raster Catalog):
          The name and format for the raster dataset you are creating.

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a compression type and compression quality."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyRaster_management(*gp_fixargs((in_raster, out_rasterdataset, config_keyword, background_value, nodata_value, onebit_to_eightbit, colormap_to_RGB, pixel_type, scale_pixel_value, RGB_to_Colormap), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRandomRaster_management', None)
def CreateRandomRaster(out_path=None, out_name=None, distribution=None, raster_extent=None, cellsize=None):
    """CreateRandomRaster_management(out_path, out_name, {distribution}, {raster_extent}, {cellsize})

        Create a raster dataset of random values with a distribution you can define.

     INPUTS:
      out_path (Workspace / Raster Catalog):
          Select a folder or geodatabase to store the raster dataset.
      out_name (String):
          Specify a name and, where necessary, extension for the output raster dataset.
          When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.To store the output as an Esri Grid raster or a
          raster dataset in a geodatabase,
          no file extension should be added to the name of the raster dataset. To store
          the raster dataset in one of the available file raster formats, specify a tif
          extension to output a TIFF raster, or .img for an ERDAS IMAGINE raster.When
          storing your raster dataset to a TIFF file, or a geodatabase raster, you
          can specify a compression type and compression quality.
      distribution {String}:
          Specify the random value distribution method to use.

          * UNIFORM {Minimum}, {Maximum}—A uniform distribution with the defined range.
          The default values are 0.0 for {Minimum} and 1.0 for {Maximum}. Both values are
          of type double.

          * INTEGER {Minimum}, {Maximum}—An integer distribution with the defined range.
          The default values are 1 for {Minimum} and 10 for {Maximum}. Both values are of
          type long.

          * NORMAL {Mean}, {Standard Deviation}—A normal distribution with a defined
          {Mean} and {Standard Deviation}. The default values are 0.0 for {Mean} and 1.0
          for {Standard Deviation}. Both values are of type double.

          * EXPONENTIAL {Mean}—An exponential distribution with a defined {Mean}. The
          default value is 1.0. The value is of type double.

          * POISSON {Mean}—A Poisson distribution with a defined {Mean}. The default value
          is 1.0. The value is of type double.

          * GAMMA {Alpha}, {Beta}—A gamma distribution with a defined {Alpha} and {Beta}.
          The default values are 1.0 for {Alpha} and 1.0 for {Beta}. Both values are of
          type double.

          * BINOMIAL {N}, {Probability}—A binomial distribution with a defined {N} and
          {Probability}. The {N} is of type long with a default of 10. The {Probability}
          is of type double with a default of 0.5.

          * GEOMETRIC {Probability}—A geometric distribution with a defined {Probability}.
          The default value is 0.5. The value is of type double.

          * NEGATIVE BINOMIAL {r}, {Probability}—A Pascal distribution with a defined {r}
          and {Probability}. The {r} is of type double with a default of 10.0. The
          {Probability} is of type double with a default of 0.5.
      raster_extent {Extent}:
          Set the extent of the output raster dataset.
      cellsize {Double}:
          Define the spatial resolution of the output raster dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRandomRaster_management(*gp_fixargs((out_path, out_name, distribution, raster_extent, cellsize), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateRasterDataset_management', None)
def CreateRasterDataset(out_path=None, out_name=None, cellsize=None, pixel_type=None, raster_spatial_reference=None, number_of_bands=None, config_keyword=None, pyramids=None, tile_size=None, compression=None, pyramid_origin=None):
    """CreateRasterDataset_management(out_path, out_name, {cellsize}, pixel_type, {raster_spatial_reference}, number_of_bands, {config_keyword}, {pyramids}, {tile_size}, {compression}, {pyramid_origin})

        Creates an empty raster dataset.

     INPUTS:
      out_path (Workspace / Raster Catalog):
          The output location to store the raster dataset.
      out_name (String):
          The name, location and format for the dataset you are creating.When storing the
          raster dataset in a file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings.
      cellsize {Double}:
          The cell size for the new raster dataset.
      pixel_type (String):
          The bit-depth (radiometric resolution) of the output raster dataset. If this is
          not specified, your raster dataset will be created with a default pixel type of
          8-bit unsigned integer.Not all data types are supported by all raster formats.
          Check the Supported
          raster dataset file formats help topic to be sure the format you are using will
          support the data type you need.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      raster_spatial_reference {Coordinate System}:
          The coordinate system for the output raster dataset.If this is not specified,
          the coordinate system set in the environment settings
          will be used.
      number_of_bands (Long):
          The number of bands that the output raster dataset will have.
      config_keyword {String}:
          Specifies the storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database administrator.
      pyramids {Pyramid}:
          Use this option to create pyramids.For Pyramid Levels, choose a number of -1 or
          higher. A value of 0 will not build
          any pyramids, and a value of -1 will automatically choose the correct number of
          pyramid layers to create.The Pyramid Resampling Technique defines how the data
          will be resampled when
          building the pyramids.

          * NEAREST—Nearest neighbor should be used for nominal data or raster datasets
          with color maps, such as land-use or pseudo color images.

          * BILINEAR—Bilinear interpolation is best used with continuous data, such as
          satellite imagery or aerial photography.

          * CUBIC—Cubic convolution is best used with continuous data, such as satellite
          imagery or aerial photography. It is similar to bilinear interpolation; however,
          it resamples the data using a larger matrix.
          The Pyramid Compression Type defines the method used when compressing the
          pyramids.

          * DEFAULT—This uses the compression that is normally used by the raster dataset
          format.

          * LZ77—A lossless compression. The values of the cells in the raster will not be
          changed.

          * JPEG—A lossy compression.

          * NONE—No data compression.
      tile_size {Tile Size}:
          The tile width controls the number of pixels you can store in each tile. This is
          specified as a number of pixels in x. The default tile width is 128.The tile
          height controls the number of pixels you can store in each tile. This
          is specified as a number of pixels in y. The default tile height is 128.Only
          geodatabases and enterprise geodatabases use tile size.
      compression {Compression}:
          Define the type of compression to store the raster dataset.

          * LZ77

          * JPEG—Lossy compression that uses the public JPEG compression algorithm. If you
          choose JPEG, you can also specify the compression quality. The valid compression
          quality value ranges are from 0 to 100. This compression can be used for JPEG
          files and TIFF files.

          * JPEG 2000—Lossy compression

          * PACKBITS—PackBits compression for TIFF files.

          * LZW—Lossless compression that preserves all raster cell values.

          * PackBits

          * RLE—Run-length encoding for IMG files.

          * CCITT GROUP 3—Lossless compression for 1-bit data.

          * CCITT GROUP 4—Lossless compression for 1-bit data.

          * CCITT (1D)—Lossless compression for 1-bit data.

          * NONE—No compression will occur. This is the default.
      pyramid_origin {Point}:
          This defines the type of data compression that will be used to store the raster
          dataset.

          * LZ77—Lossless.

          * JPEG—Lossy. Uses a compression quality setting.

          * JPEG 2000—Lossy. Uses a compression quality setting.

          * PackBits—Lossless. Only for TIFF format.

          * LZW—Lossless.

          * RLE—Lossless.

          * CCITT GROUP 3—Lossless. Only for TIFF format.

          * CCITT GROUP 4—Lossless. Only for TIFF format.

          * CCITT (1D)—Lossless. Only for TIFF format.

          * NONE—No data compression.
          The JPEG and JPEG 2000 compression quality can range from 1 to 100. A higher
          number means better image quality but less compression."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRasterDataset_management(*gp_fixargs((out_path, out_name, cellsize, pixel_type, raster_spatial_reference, number_of_bands, config_keyword, pyramids, tile_size, compression, pyramid_origin), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DownloadRasters_management', None)
def DownloadRasters(in_image_service=None, out_folder=None, where_clause=None, selection_feature=None, clipping=None, convert_rasters=None, format=None, compression_method=None, compression_quality=None, MAINTAIN_FOLDER=None):
    """DownloadRasters_management(in_image_service, out_folder, {where_clause}, {selection_feature}, {clipping}, {convert_rasters}, {format}, {compression_method}, {compression_quality}, {MAINTAIN_FOLDER})

        Downloads the source files from an image service or mosaic dataset.

     INPUTS:
      in_image_service (Image Service / String / Mosaic Layer / Raster Layer):
          The image service or mosaic dataset to download.
      out_folder (Folder):
          The destination for the image service or mosaic dataset.
      where_clause {SQL Expression}:
          An SQL expression to limit the download to raster datasets that satisfy the
          expression.
      selection_feature {Extent}:
          Limits the download to an extent of a feature class or bounding box. All raster
          datasets that intersect the extent will be downloaded.
      clipping {Boolean}:
          Specify if you want to clip the downloaded images based on the geometry of a
          feature. Any raster that intersects the clipping geometry will be clipped and
          then downloaded. This is useful when your area of interest is not a rectangle.
          When downloaded images are clipped, you need to specify an output format for the
          clipped images.

          * NO_CLIPPING —The files will be clipped based on the minimum bounding rectangle
          that has been specified. This is the default.

          * CLIPPING —The files will be clipped based on the geometry of the
          selection_feature.
      convert_rasters {Boolean}:
          Choose whether to always convert your rasters to the specified format, or to
          only convert when it is necessary.

          * CONVERT_AS_REQUIRED—Do not convert the raster datasets to a new format.

          * ALWAYS_CONVERT —Convert the downloaded raster datasets into another format.
      format {String}:
          Choose a output format for the downloaded raster datasets.

          * TIFF—Tagged Image File Format. This is the default.

          * BIL—Esri band interleaved by line.

          * BSQ—Esri band sequential.

          * BIP—Esri band interleaved by pixel.

          * BMP—Bitmap.

          * ENVI—ENVI DAT file.

          * IMAGINE Image—ERDAS IMAGINE.

          * JPEG—Joint Photographics Experts Group. If chosen, you can also specify the
          compression quality. The valid compression quality value ranges are from 0 to
          100.

          * GIF—Graphic interchange format.

          * JP2 —JPEG 2000. If chosen, you can also specify the compression quality. The
          valid compression quality value ranges are from 0 to 100.

          * PNG—Portable Network Graphics.
      compression_method {String}:
          Choose the compression method to use with the specified Output Format.

          * NONE—No compression will occur. This is the default.

          * JPEG—Lossy compression that uses the public JPEG compression algorithm. If you
          choose JPEG, you can also specify the compression quality. The valid compression
          quality value ranges are from 0 to 100. This compression can be used for JPEG
          files and TIFF files.

          * LZW—Lossless compression that preserves all raster cell values.

          * PACKBITS—PackBits compression for TIFF files.

          * RLE—Run-length encoding for IMG files.

          * CCITT_GROUP3—Lossless compression for 1-bit data.

          * CCITT_GROUP4—Lossless compression for 1-bit data.

          * CCITT_1D—Lossless compression for 1-bit data.
      compression_quality {Long}:
          Set a value from 1 - 100. Higher values will have better image quality, but less
          compression.
      MAINTAIN_FOLDER {Boolean}:
          Determines the folder structure of the downloaded rasters.

          * MAINTAIN_FOLDER—Replicate the hierarchical folder structure used to store the
          source raster datasets.

          * NO_MAINTAIN_FOLDER—Raster datasets will be downloaded into the out_folder as a
          flat folder structure."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DownloadRasters_management(*gp_fixargs((in_image_service, out_folder, where_clause, selection_feature, clipping, convert_rasters, format, compression_method, compression_quality, MAINTAIN_FOLDER), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Mosaic_management', None)
def Mosaic(inputs=None, target=None, mosaic_type=None, colormap=None, background_value=None, nodata_value=None, onebit_to_eightbit=None, mosaicking_tolerance=None, MatchingMethod=None):
    """Mosaic_management(inputs;inputs..., target, {mosaic_type}, {colormap}, {background_value}, {nodata_value}, {onebit_to_eightbit}, {mosaicking_tolerance}, {MatchingMethod})

        Merges multiple existing raster datasets into an existing raster dataset.

     INPUTS:
      inputs (Mosaic Dataset / Composite Layer / Raster Dataset / Raster Layer):
          The raster datasets you want to merge together.
      target (Raster Dataset):
          The raster to add the input rasters. This raster dataset must already exist. By
          default, the target raster is considered the first raster in the list of input
          raster datasets. You can create an empty raster using the Create Raster Dataset
          tool.
      mosaic_type {String}:
          The method used to mosaic overlapping areas.

          * FIRST—The output cell value of the overlapping areas will be the value from
          the first raster dataset mosaicked into that location.

          * LAST—The output cell value of the overlapping areas will be the value from the
          last raster dataset mosaicked into that location. This is the default.

          * BLEND—The output cell value of the overlapping areas will be a horizontally
          weighted calculation of the values of the cells in the overlapping area.

          * MEAN—The output cell value of the overlapping areas will be the average value
          of the overlapping cells.

          * MINIMUM—The output cell value of the overlapping areas will be the minimum
          value of the overlapping cells.

          * MAXIMUM—The output cell value of the overlapping areas will be the maximum
          value of the overlapping cells.

          * SUM—The output cell value of the overlapping areas will be the total sum of
          the overlapping cells.
      colormap {String}:
          The method used to choose which color map from the input rasters will be applied
          to the mosaic output.

          * FIRST—The color map from the first raster dataset in the list will be applied
          to the output raster mosaic. This is the default.

          * LAST—The color map from the last raster dataset in the list will be applied to
          the output raster mosaic.

          * MATCH—Will take all the color maps into consideration when mosaicking. If all
          possible values are already used (for the bit depth), it will attempt to match
          the value with the closest color that is available.

          * REJECT—Only the raster datasets that do not have a color map associated with
          them will be mosaicked.
      background_value {Double}:
          Use this option to remove the unwanted values created around the raster data.
          The value specified will be distinguished from other valuable data in the raster
          dataset. For example, a value of zero along the raster dataset's borders will be
          distinguished from zero values within the raster dataset.The pixel value
          specified will be set to NoData in the output raster dataset.For file-based
          rasters and geodatabase rasters, the Ignore Background Value must
          be set to the same value as NoData in order for the background value to be
          ignored. Enterprise geodatabase rasters will work without this extra step.
      nodata_value {Double}:
          All the pixels with the specified value will be set to NoData in the output
          raster dataset.
      onebit_to_eightbit {Boolean}:
          Choose whether the input 1-bit raster dataset will be converted to an 8-bit
          raster dataset. In this conversion the value 1 in the input raster dataset will
          be changed to 255 in the output raster dataset. This is useful when importing a
          1-bit raster dataset to a geodatabase. One-bit raster datasets have 8-bit
          pyramid layers when stored in a file system, but in a geodatabase, 1-bit raster
          datasets can only have 1-bit pyramid layers, which makes the display unpleasant.
          By converting the data to 8 bit in a geodatabase, the pyramid layers are built
          as 8 bit instead of 1 bit, resulting in a proper raster dataset in the display.

          * NONE—No conversion will be done. This is the default.

          * OneBitTo8Bit—The input raster will be converted.
      mosaicking_tolerance {Double}:
          When mosaicking takes place, the target and the source pixels do not always line
          up exactly. When there is a misalignment of pixels, a decision needs to be made
          whether resampling takes place or whether the data should be shifted. The
          mosaicking tolerance controls whether resampling of the pixels take place or if
          the pixels should be shifted.If the difference in pixel alignment (of the
          incoming dataset and the target
          dataset) is greater than the tolerance, resampling will take place. If the
          difference in pixel alignment (of the incoming dataset and the target dataset)
          is less than the tolerance, resampling will not take place (instead, a shift is
          performed).The unit of tolerance is a pixel, where the valid value range is 0 to
          0.5. A
          tolerance of 0.5 will guarantee a shift takes place. A tolerance of zero
          guarantees resampling, if there is a misalignment in pixels.For example, the
          source and target pixels have a misalignment of 0.25. If the
          mosaicking tolerance is set to 0.2, then resampling will take place since the
          pixel misalignment is greater than the tolerance. If the mosaicking tolerance is
          set to 0.3, then the pixels will be shifted.
      MatchingMethod {String}:
          Choose the color matching method to apply to the rasters.

          * NONE—This option will not use the color matching operation when mosaicking
          your raster datasets.

          * STATISTIC_MATCHING—This method will use descriptive statistics from the
          overlapping areas; the transformation will then be applied to the entire target
          dataset.

          * HISTOGRAM_MATCHING—This method will match the histogram from the reference
          overlap area to the source overlap area; the transformation will then be applied
          to the entire target dataset.

          * LINEARCORRELATION_MATCHING—This method will match overlapping pixels and
          interpolate the rest of the source dataset; pixels without a one-to-one
          relationship will use a weighted average."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Mosaic_management(*gp_fixargs((inputs, target, mosaic_type, colormap, background_value, nodata_value, onebit_to_eightbit, mosaicking_tolerance, MatchingMethod), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MosaicToNewRaster_management', None)
def MosaicToNewRaster(input_rasters=None, output_location=None, raster_dataset_name_with_extension=None, coordinate_system_for_the_raster=None, pixel_type=None, cellsize=None, number_of_bands=None, mosaic_method=None, mosaic_colormap_mode=None):
    """MosaicToNewRaster_management(input_rasters;input_rasters..., output_location, raster_dataset_name_with_extension, {coordinate_system_for_the_raster}, {pixel_type}, {cellsize}, number_of_bands, {mosaic_method}, {mosaic_colormap_mode})

        Merges multiple raster datasets into a new raster dataset.

     INPUTS:
      input_rasters (Mosaic Dataset / Composite Layer / Raster Dataset / Raster Layer):
          The raster datasets that you want to merge together. The inputs must have the
          same number of bands and same bit depth.
      output_location (Workspace / Raster Catalog):
          The path to contain the raster dataset. The path can be to a folder or
          geodatabase.
      raster_dataset_name_with_extension (String):
          The name of the dataset you are creating.When storing the raster dataset in a
          file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings.
      coordinate_system_for_the_raster {Coordinate System}:
          The coordinate system for the output raster dataset. If this is not specified,
          the Output Coordinate System environment setting will be used.
      pixel_type {String}:
          The bit depth, or radiometric resolution of the mosaic dataset.If you do not set
          the pixel type, the 8-bit default will be used and your output
          may be incorrect.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      cellsize {Double}:
          The cell size for the new raster dataset.
      number_of_bands (Long):
          The number of bands that the output raster will have.
      mosaic_method {String}:
          The method used to mosaic overlapping areas.

          * FIRST—The output cell value of the overlapping areas will be the value from
          the first raster dataset mosaicked into that location.

          * LAST—The output cell value of the overlapping areas will be the value from the
          last raster dataset mosaicked into that location. This is the default.

          * BLEND—The output cell value of the overlapping areas will be a horizontally
          weighted calculation of the values of the cells in the overlapping area.

          * MEAN—The output cell value of the overlapping areas will be the average value
          of the overlapping cells.

          * MINIMUM—The output cell value of the overlapping areas will be the minimum
          value of the overlapping cells.

          * MAXIMUM—The output cell value of the overlapping areas will be the maximum
          value of the overlapping cells.

          * SUM—The output cell value of the overlapping areas will be the total sum of
          the overlapping cells.
          For more information about each mosaic operator, refer to the Mosaic Operator
          help topic.
      mosaic_colormap_mode {String}:
          Applies when the input raster datasets have a colormap.The method used to choose
          which color map from the input rasters will be applied
          to the mosaic output.

          * FIRST—The color map from the first raster dataset in the list will be applied
          to the output raster mosaic. This is the default.

          * LAST—The color map from the last raster dataset in the list will be applied to
          the output raster mosaic.

          * MATCH—Will take all the color maps into consideration when mosaicking. If all
          possible values are already used (for the bit depth), it will attempt to match
          the value with the closest color that is available.

          * REJECT—Only the raster datasets that do not have a color map associated with
          them will be mosaicked."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MosaicToNewRaster_management(*gp_fixargs((input_rasters, output_location, raster_dataset_name_with_extension, coordinate_system_for_the_raster, pixel_type, cellsize, number_of_bands, mosaic_method, mosaic_colormap_mode), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterCatalogToRasterDataset_management', None)
def RasterCatalogToRasterDataset(in_raster_catalog=None, out_raster_dataset=None, where_clause=None, mosaic_type=None, colormap=None, order_by_field=None, ascending=None, pixel_type=None, ColorBalancing=None, MatchingMethod=None, ReferenceRaster=None, OID=None):
    """RasterCatalogToRasterDataset_management(in_raster_catalog, out_raster_dataset, {where_clause}, {mosaic_type}, {colormap}, {order_by_field}, {ascending}, {pixel_type}, {ColorBalancing}, {MatchingMethod}, {ReferenceRaster}, {OID})

        Mosaics the contents of a raster catalog into a new raster dataset.

     INPUTS:
      in_raster_catalog (Raster Catalog Layer):
          The raster catalog that will be mosaicked to a raster dataset.
      where_clause {SQL Expression}:
          Enter the appropriate SQL statement to select specific rows in the raster
          catalog.
      mosaic_type {String}:
          The method used to mosaic overlapping areas.

          * FIRST—The output cell value of the overlapping areas will be the value from
          the first raster dataset mosaicked into that location.

          * LAST—The output cell value of the overlapping areas will be the value from the
          last raster dataset mosaicked into that location. This is the default.

          * BLEND—The output cell value of the overlapping areas will be a horizontally
          weighted calculation of the values of the cells in the overlapping area.

          * MEAN—The output cell value of the overlapping areas will be the average value
          of the overlapping cells.

          * MINIMUM—The output cell value of the overlapping areas will be the minimum
          value of the overlapping cells.

          * MAXIMUM—The output cell value of the overlapping areas will be the maximum
          value of the overlapping cells.

          * SUM—The output cell value of the overlapping areas will be the total sum of
          the overlapping cells.
          For more information about each mosaic operator, refer to Mosaic Operator.
      colormap {String}:
          The method used to choose which color map from the input rasters will be applied
          to the mosaic output.

          * FIRST—The color map from the first raster dataset in the list will be applied
          to the output raster mosaic. This is the default.

          * LAST—The color map from the last raster dataset in the list will be applied to
          the output raster mosaic.

          * MATCH—Will take all the color maps into consideration when mosaicking. If all
          possible values are already used (for the bit depth), it will attempt to match
          the value with the closest color that is available.

          * REJECT—Only the raster datasets that do not have a color map associated with
          them will be mosaicked.
          For more information about each colormap mode, refer to Mosaic colormap mode.
      order_by_field {String}:
          Define the field by which to order the raster catalog items.
      ascending {Boolean}:
          Choose whether to use the ascending value of the Order By field. If the
          Ascending option is not used, the descending order will be used.

          * Ascending—The ascending order of the rows will be followed in the mosaic
          procedure. This is the default.

          * None—The descending order of the rows will be followed in the mosaic
          procedure.
      pixel_type {String}:
          Determines the bit depth of the output raster dataset. If left unspecified, the
          output bit depth will be the same as the input.There will be no rescaling of the
          raster values when a different pixel type is
          chosen. If the pixel type is demoted (lowered), the raster values outside the
          valid range for that pixel depth will be truncated and lost.

          * 1_BIT—A 1-bit unsigned integer. The values can be 0 or 1.

          * 2_BIT—A 2-bit unsigned integer. The values supported can be from 0 to 3.

          * 4_BIT—A 4-bit unsigned integer. The values supported can be from 0 to 15.

          * 8_BIT_UNSIGNED—An unsigned 8-bit data type. The values supported can be from 0
          to 255.

          * 8_BIT_SIGNED—A signed 8-bit data type. The values supported can be from -128
          to 127.

          * 16_BIT_UNSIGNED—A 16-bit unsigned data type. The values can range from 0 to
          65,535.

          * 16_BIT_SIGNED—A 16-bit signed data type. The values can range from -32,768 to
          32,767.

          * 32_BIT_UNSIGNED—A 32-bit unsigned data type. The values can range from 0 to
          4,294,967,295.

          * 32_BIT_SIGNED—A 32-bit signed data type. The values can range from
          -2,147,483,648 to 2,147,483,647.

          * 32_BIT_FLOAT—A 32-bit data type supporting decimals.

          * 64_BIT—A 64-bit data type supporting decimals.
      ColorBalancing {Boolean}:
          Choose whether or not to use a dodging technique to color correct the raster
          catalog items. All pixels in the raster catalog will be used to determine the
          gamma and contrast values for the color-balancing algorithm.

          * NONE—Color balancing will not be performed in the mosaic procedure. This is
          the default.

          * ColorBalancing—Color balancing will be performed in the mosaic procedure.
      MatchingMethod {String}:
          Choose the color matching method to apply to the rasters.

          * NONE—This option will not use the color matching operation when mosaicking
          your raster datasets.

          * STATISTICS_MATCHING—This method will match the statistical differences
          (minimum, maximum, and mean) between the reference overlap area and the source
          overlap area; the transformation will then be applied to the entire target
          dataset.

          * HISTOGRAM_MATCHING—This method will match the histogram from the reference
          overlap area with the source overlap area; the transformation will then be
          applied to the entire target.

          * LINEARCORRELATION_MATCHING—This method will match overlapped pixels and
          interpolate to the rest of the source; pixels that do not have a one-to-one
          relationship will use a weighted average.
      ReferenceRaster {String}:
          If color matching is applied, choose how to specify the reference raster.

          * CALCULATE_FROM_ALL—The system will calculate the best raster dataset to use,
          based on all the raster catalog items.

          * SPECIFY_OID—The user will type in the Object ID (OID) of the raster catalog
          item to use as the reference raster.

          * DEFINE_FROM_SELECTION—The system will calculate the best raster dataset to
          use, based on the raster catalog items that are selected.
      OID {Long}:
          The object ID (OID) of the reference raster. The OID is a unique key field in
          the raster catalog.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The name and extension of the output raster dataset mosaic.When storing the
          raster dataset in a file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
          When storing a raster dataset in a geodatabase, no file extension should be
          added to the name of the raster dataset.When storing your raster dataset to a
          JPEG file, a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterCatalogToRasterDataset_management(*gp_fixargs((in_raster_catalog, out_raster_dataset, where_clause, mosaic_type, colormap, order_by_field, ascending, pixel_type, ColorBalancing, MatchingMethod, ReferenceRaster, OID), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('WorkspaceToRasterDataset_management', None)
def WorkspaceToRasterDataset(in_workspace=None, in_raster_dataset=None, include_subdirectories=None, mosaic_type=None, colormap=None, background_value=None, nodata_value=None, onebit_to_eightbit=None, mosaicking_tolerance=None, MatchingMethod=None, colormap_to_RGB=None):
    """WorkspaceToRasterDataset_management(in_workspace, in_raster_dataset, {include_subdirectories}, {mosaic_type}, {colormap}, {background_value}, {nodata_value}, {onebit_to_eightbit}, {mosaicking_tolerance}, {MatchingMethod}, {colormap_to_RGB})

        Merges all of the raster datasets in a folder into one raster dataset.

     INPUTS:
      in_workspace (Workspace):
          The folder containing the raster datasets to merge.
      in_raster_dataset (Raster Dataset):
          An existing raster dataset in which to merge all of the raster datasets from the
          input workspace.
      include_subdirectories {Boolean}:
          Specify whether to include subdirectories.

          * NONE—Does not include subdirectories. This is the default.

          * INCLUDE_SUBDIRECTORIES—Includes all the raster datasets within the
          subdirectories when loading.
      mosaic_type {String}:
          The method used to mosaic overlapping areas.

          * FIRST—The output cell value of the overlapping areas will be the value from
          the first raster dataset mosaicked into that location.

          * LAST—The output cell value of the overlapping areas will be the value from the
          last raster dataset mosaicked into that location. This is the default.

          * BLEND—The output cell value of the overlapping areas will be a horizontally
          weighted calculation of the values of the cells in the overlapping area.

          * MEAN—The output cell value of the overlapping areas will be the average value
          of the overlapping cells.

          * MINIMUM—The output cell value of the overlapping areas will be the minimum
          value of the overlapping cells.

          * MAXIMUM—The output cell value of the overlapping areas will be the maximum
          value of the overlapping cells.

          * SUM—The output cell value of the overlapping areas will be the total sum of
          the overlapping cells.
      colormap {String}:
          The method used to choose which color map from the input rasters will be applied
          to the mosaic output.

          * FIRST—The color map from the first raster dataset in the list will be applied
          to the output raster mosaic. This is the default.

          * LAST—The color map from the last raster dataset in the list will be applied to
          the output raster mosaic.

          * MATCH—Will take all the color maps into consideration when mosaicking. If all
          possible values are already used (for the bit depth), it will attempt to match
          the value with the closest color that is available.

          * REJECT—Only the raster datasets that do not have a color map associated with
          them will be mosaicked.
      background_value {Double}:
          Use this option to remove the unwanted values created around the raster data.
          The value specified will be distinguished from other valuable data in the raster
          dataset. For example, a value of zero along the raster dataset's borders will be
          distinguished from zero values within the raster dataset.The pixel value
          specified will be set to NoData in the output raster dataset.For file-based
          rasters and personal geodatabase rasters, the Ignore Background
          Value must be set to the same value as NoData in order for the background value
          to be ignored. Enterprise and file geodatabase rasters will work without this
          extra step.
      nodata_value {Double}:
          All the pixels with the specified value will be set to NoData in the output
          raster dataset.
      onebit_to_eightbit {Boolean}:
          Choose whether the input 1-bit raster dataset will be converted to an 8-bit
          raster dataset. In this conversion the value 1 in the input raster dataset will
          be changed to 255 in the output raster dataset. This is useful when importing a
          1-bit raster dataset to a geodatabase. One-bit raster datasets have 8-bit
          pyramid layers when stored in a file system, but in a geodatabase, 1-bit raster
          datasets can only have 1-bit pyramid layers, which makes the display unpleasant.
          By converting the data to 8 bit in a geodatabase, the pyramid layers are built
          as 8 bit instead of 1 bit, resulting in a proper raster dataset in the display.

          * NONE—No conversion will be done. This is the default.

          * OneBitTo8Bit—The input raster will be converted.
      mosaicking_tolerance {Double}:
          When mosaicking takes place, the target and the source pixels do not always line
          up exactly. When there is a misalignment of pixels, a decision needs to be made
          whether resampling takes place or whether the data should be shifted. The
          mosaicking tolerance controls whether resampling of the pixels take place or if
          the pixels should be shifted.If the difference in pixel alignment (of the
          incoming dataset and the target
          dataset) is greater than the tolerance, resampling will take place. If the
          difference in pixel alignment (of the incoming dataset and the target dataset)
          is less than the tolerance, resampling will not take place (instead, a shift is
          performed).The unit of tolerance is a pixel, where the valid value range is 0 to
          0.5. A
          tolerance of 0.5 will guarantee a shift takes place. A tolerance of zero
          guarantees resampling, if there is a misalignment in pixels.For example, the
          source and target pixels have a misalignment of 0.25. If the
          mosaicking tolerance is set to 0.2, then resampling will take place since the
          pixel misalignment is greater than the tolerance. If the mosaicking tolerance is
          set to 0.3, then the pixels will be shifted.
      MatchingMethod {String}:
          The color matching method to apply to the rasters.

          * NONE—This option will not use the color matching operation when mosaicking
          your raster datasets.

          * STATISTIC_MATCHING—This method will use descriptive statistics from the
          overlapping areas; the transformation will then be applied to the entire target
          dataset.

          * HISTOGRAM_MATCHING—This method will match the histogram from the reference
          overlap area to the source overlap area; the transformation will then be applied
          to the entire target dataset.

          * LINEARCORRELATION_MATCHING—This method will match overlapping pixels and then
          interpolated the rest of the source dataset; pixels without a one-to-one
          relationship will use a weighted average.
      colormap_to_RGB {Boolean}:
          If the input raster dataset has a color map, the output raster dataset can be
          converted to a three-band output raster dataset. This is useful when mosaicking
          rasters with different color maps.

          * NONE—No conversion will occur. This is the default.

          * ColormapToRGB—The input dataset will be converted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.WorkspaceToRasterDataset_management(*gp_fixargs((in_workspace, in_raster_dataset, include_subdirectories, mosaic_type, colormap, background_value, nodata_value, onebit_to_eightbit, mosaicking_tolerance, MatchingMethod, colormap_to_RGB), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Raster Processing toolset
@gptooldoc('Clip_management', None)
def Clip(in_raster=None, rectangle=None, out_raster=None, in_template_dataset=None, nodata_value=None, clipping_geometry=None, maintain_clipping_extent=None):
    """Clip_management(in_raster, rectangle, out_raster, {in_template_dataset}, {nodata_value}, {clipping_geometry}, {maintain_clipping_extent})

        Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset, mosaic dataset, or image service that you want to clip.
      rectangle (Envelope):
          Four coordinates to define the extent of the bounding box used to clip the
          raster in this order: X-Minimum, Y-Minimum, X-Maximum, Y-Maximum.If the clip
          extent specified is not aligned with the input raster dataset, the
          Clip tool makes sure that the proper alignment is used. This may cause the
          output to have a slightly different extent than specified in the tool.
      in_template_dataset {Raster Layer / Feature Layer}:
          A raster dataset or feature class to use as the extent. The clip output includes
          any pixels that intersect the minimum bounding rectangle.If a feature class is
          used as the output extent and you want to clip the raster
          based on the polygon features, set the clipping_geometry parameter to
          ClippingGeometry.This option may promote the pixel depth of the output.
          Therefore, you need to make sure that the output format can support the proper
          pixel depth.
      nodata_value {String}:
          The value for pixels to be considered as NoData.
      clipping_geometry {Boolean}:
          Specify whether to clip your data to the minimum bounding rectangle, or to the
          geometry of the feature class.

          * NONE—Use the minimum bounding rectangle to clip the data. This is the default.

          * ClippingGeometry—Use the geometry of the specified feature class to clip the
          data. The pixel depth of the output may be increased, therefore, you need to
          make sure that the output format can support the proper pixel depth.
      maintain_clipping_extent {Boolean}:
          * MAINTAIN_EXTENT—Adjust the number of columns and rows, then resample pixels so
          as to exactly match the clipping extent specified.

          * NO_MAINTAIN_EXTENT—Maintain the cell alignment as the input raster and adjust
          the output extent accordingly.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the dataset you are creating. Make sure that
          it can support the necessary bit-depth.When storing the raster dataset in a file
          format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Clip_management(*gp_fixargs((in_raster, rectangle, out_raster, in_template_dataset, nodata_value, clipping_geometry, maintain_clipping_extent), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CompositeBands_management', None)
def CompositeBands(in_rasters=None, out_raster=None):
    """CompositeBands_management(in_rasters;in_rasters..., out_raster)

        Creates a single raster dataset from multiple bands.

     INPUTS:
      in_rasters (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster datasets that you want to use as the bands.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location and format for the raster dataset you are creating. Make sure
          that it can support the necessary bit-depth.When storing the raster dataset in a
          file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CompositeBands_management(*gp_fixargs((in_rasters, out_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ComputePansharpenWeights_management', None)
def ComputePansharpenWeights(in_raster=None, in_panchromatic_image=None, band_indexes=None):
    """ComputePansharpenWeights_management(in_raster, in_panchromatic_image, {band_indexes})

        Calculates an optimal set of pan-sharpened weights for new or custom sensor
        data.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          A multispectral raster that has a panchromatic band.
      in_panchromatic_image (Raster Layer):
          The panchromatic band associated with the multispectral raster.
      band_indexes {String}:
          The band order for the pansharpened weights.If a raster product is used as the
          in_raster parameter, the band order within
          the raster product template will be used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ComputePansharpenWeights_management(*gp_fixargs((in_raster, in_panchromatic_image, band_indexes), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateOrthoCorrectedRasterDataset_management', None)
def CreateOrthoCorrectedRasterDataset(in_raster=None, out_raster_dataset=None, Ortho_type=None, constant_elevation=None, in_DEM_raster=None, ZFactor=None, ZOffset=None, Geoid=None):
    """CreateOrthoCorrectedRasterDataset_management(in_raster, out_raster_dataset, Ortho_type, constant_elevation, {in_DEM_raster}, {ZFactor}, {ZOffset}, {Geoid})

        Incorporates elevation data and image metadata to accurately line up imagery.

     INPUTS:
      in_raster (Raster Layer):
          Select the raster dataset that you want to orthorectify. The raster must have
          rational polynomial coefficients (RPCs) in its metadata.
      Ortho_type (String):
          Use a Digital Elevation Model (DEM) or specify a value that represents the
          average elevation across your image.

          * CONSTANT_ELEVATION—Uses a specified elevation value.

          * DEM—Uses a specified digital elevation model raster.
      constant_elevation (Double):
          The constant elevation value to be used when the ortho_type parameter is
          CONSTANT_ELEVATION.If a DEM is used in the orthocorrection process, this value
          is not used.
      in_DEM_raster {Mosaic Layer / Raster Layer}:
          The digital elevation model raster to be used for orthorectification when the
          ortho_type parameter is DEM.
      ZFactor {Double}:
          The scaling factor used to convert the elevation values in the DEM.If your
          vertical units are in meters, the Z Factor should be set to 1. If your
          vertical units are in feet, the Z Factor should be set to 0.3048. If any other
          vertical units are used, use the Z Factor to scale the units to meters.
      ZOffset {Double}:
          The base value to be added to the elevation value in the DEM. This could be used
          to offset elevation values that do not start at sea level.
      Geoid {Boolean}:
          The geoid correction is required by RPCs that reference ellipsoidal heights.
          Most elevation datasets are referenced to sea level orthometric heights, so this
          correction would be required in these cases to convert to ellipsoidal heights.

          * NONE—No geoid correction is made. Use NONE only if your DEM is already
          expressed in ellipsoidal heights.

          * GEOID—A geoid correction will be made to convert orthometric heights to
          ellipsoidal heights (based on EGM96 geoid).

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          Specify a name, location and format for the dataset you are creating.When
          storing the raster dataset in a file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, or a
          geodatabase, you can specify a Compression Type type and Compression Quality
          within the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateOrthoCorrectedRasterDataset_management(*gp_fixargs((in_raster, out_raster_dataset, Ortho_type, constant_elevation, in_DEM_raster, ZFactor, ZOffset, Geoid), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreatePansharpenedRasterDataset_management', None)
def CreatePansharpenedRasterDataset(in_raster=None, red_channel=None, green_channel=None, blue_channel=None, infrared_channel=None, out_raster_dataset=None, in_panchromatic_image=None, pansharpening_type=None, red_weight=None, green_weight=None, blue_weight=None, infrared_weight=None, sensor=None):
    """CreatePansharpenedRasterDataset_management(in_raster, red_channel, green_channel, blue_channel, {infrared_channel}, out_raster_dataset, in_panchromatic_image, pansharpening_type, {red_weight}, {green_weight}, {blue_weight}, {infrared_weight}, {sensor})

        Fuses a high-resolution panchromatic raster dataset with a lower-resolution
        multiband raster dataset to create a red-green-blue (RGB) raster with the
        resolution of the panchromatic raster.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset that you want to pan-sharpen.
      red_channel (Long):
          The input raster band that you want to display with the red color channel.
      green_channel (Long):
          The input raster band that you want to display with the green color channel.
      blue_channel (Long):
          The input raster band that you want to display with the blue color channel.
      infrared_channel {Long}:
          The input raster band that you want to display with the infrared color channel.
      in_panchromatic_image (Raster Layer):
          The higher resolution panchromatic image.
      pansharpening_type (String):
          The algorithm to fuse the panchromatic and multispectral bands together.

          * IHS—Uses Intensity, Hue, and Saturation color space for data fusion.

          * BROVEY—Uses the Brovey algorithm based on spectral modeling for data fusion.

          * Esri—Uses the ESRI algorithm based on spectral modeling for data fusion.

          * SIMPLE_MEAN—Uses the averaged value between the red, green, and blue values
          and the panchromatic pixel value.

          * Gram-Schmidt—Uses the Gram-Schmidt spectral-sharpening algorithm to sharpen
          multispectral data.
          With the ArcGIS 10.0 release, the original Simple Mean keyword option was
          replaced with SIMPLE_MEAN. Older scripts and models may still use the old
          keyword, but for clarity it may be worthwhile to update your scripts to the new
          keyword.
      red_weight {Double}:
          A value from 0 to 1 to weight the red band.
      green_weight {Double}:
          A value from 0 to 1 to weight the green band.
      blue_weight {Double}:
          A value from 0 to 1 to weight the blue band.
      infrared_weight {Double}:
          A value from 0 to 1 to weight the infrared band.
      sensor {String}:
          When the Gram-Schmidt pan-sharpening method is chosen, you can also specify the
          sensor of the multiband raster input. Choosing the sensor type will set
          appropriate band weights.

          * UNKNOWN—An unknown or unlisted sensor.

          * GeoEye-1—The GeoEye-1 and OrbView-3 satellite sensors.

          * IKONOS—The IKONOS satellite sensor.

          * KOMPSAT-2—The KOMPSAT-2 satellite sensor.

          * Landsat 1-5 MSS—The Landsat MSS satellite sensors.

          * Landsat 7 ETM+—The Landsat 7 satellite sensor.

          * Landsat 8—The Landsat 8 satellite sensor.

          * Pleiades-1—The Pleiades-1 satellite sensor.

          * QuickBird—The QuickBird satellite sensor.

          * SPOT 5—The SPOT 5 satellite sensor.

          * SPOT 6—The SPOT 6 satellite sensor.

          * UltraCam—The UltraCam aerial sensor.

          * WorldView-2—The WorldView-2 satellite sensor.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The name, location and format for the dataset you are creating.When storing the
          raster dataset in a file format, you need to specify the file
          extension:

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file,
          or a geodatabase, you can specify a Compression Type and Compression Quality in
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreatePansharpenedRasterDataset_management(*gp_fixargs((in_raster, red_channel, green_channel, blue_channel, infrared_channel, out_raster_dataset, in_panchromatic_image, pansharpening_type, red_weight, green_weight, blue_weight, infrared_weight, sensor), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExtractSubDataset_management', None)
def ExtractSubDataset(in_raster=None, out_raster=None, subdataset_index=None):
    """ExtractSubDataset_management(in_raster, out_raster, {subdataset_index;subdataset_index...})

        Creates a new raster dataset from a selection of an HDF or NITF dataset.

     INPUTS:
      in_raster (Raster Layer):
          The HDF or NITF dataset that has the layers you want to extract.
      subdataset_index {Value Table}:
          The subdatasets that you want to extract.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format for the dataset you are creating.When storing the
          raster dataset in a file format, you need to specify the file
          extension:

          * .bil—ESRI BIL

          * .bip—ESRI BIP

          * .bmp—BMP

          * .bsq—ESRI BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE file

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension—ESRI GRID.
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset.When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, or a
          geodatabase, you can specify a Compression type and Compression Quality within
          the Environment Settings."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExtractSubDataset_management(*gp_fixargs((in_raster, out_raster, subdataset_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToDTED_management', None)
def RasterToDTED(in_raster=None, out_folder=None, dted_level=None, resampling_type=None):
    """RasterToDTED_management(in_raster, out_folder, dted_level, {resampling_type})

        Splits a raster dataset into separate files based on the DTED tiling structure.

     INPUTS:
      in_raster (Raster Layer):
          Select a single band raster dataset that represents elevation.
      out_folder (Folder):
          Select a destination where the folder structure and DTED files will be created.
      dted_level (String):
          Select an appropriate level based on the resolution of your elevation data.

          * DTED_0— 900 m

          * DTED_1— 90 m

          * DTED_2—30 m
      resampling_type {String}:
          Choose an appropriate technique based on the type of data you have.

          * NEAREST—The fastest resampling method, and it minimizes changes to pixel
          values. Suitable for discrete data, such as land cover.

          * BILINEAR—Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC—Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image, but can create values
          outside of the range found in the source data. Suitable for continuous data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToDTED_management(*gp_fixargs((in_raster, out_folder, dted_level, resampling_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('Resample_management', None)
def Resample(in_raster=None, out_raster=None, cell_size=None, resampling_type=None):
    """Resample_management(in_raster, out_raster, {cell_size}, {resampling_type})

        Change the spatial resolution of your raster dataset and set rules for
        aggregating or interpolating values across the new pixel sizes.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset for which you want to change the spatial resolution.
      cell_size {Cell Size XY}:
          The cell size of the new raster using an existing raster dataset or specify its
          width (x) and height (y).You can specify the cell size in 3 different ways:

          * Using a single number specifying a square cell size

          * Using two numbers that specify the X and Y cell size, which is space delimited

          * Using the path of a raster dataset from which the square cell size will be
          imported
      resampling_type {String}:
          Choose an appropriate technique based on the type of data you have.

          * NEAREST— The fastest resampling method; it minimizes changes to pixel values.
          Suitable for discrete data, such as land cover.

          * BILINEAR— Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC— Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY— Determines the value of each pixel based on the most popular value
          within a 3 by 3 window. Suitable for discrete data.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format for the dataset you are creating.

          * .bil—Esri BIL

          * .bip—Esri BIP

          * .bmp—BMP

          * .bsq—Esri BSQ

          * .dat—ENVI DAT

          * .gif—GIF

          * .img—ERDAS IMAGINE

          * .jpg—JPEG

          * .jp2—JPEG 2000

          * .png—PNG

          * .tif—TIFF

          * no extension for Esri Grid
           When storing a raster dataset in a geodatabase, do not add a file extension to
          the name of the raster dataset. When storing your raster dataset to a JPEG file,
          a JPEG 2000 file, a TIFF file, or a geodatabase, you can specify a compression
          type and compression quality."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Resample_management(*gp_fixargs((in_raster, out_raster, cell_size, resampling_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SplitRaster_management', None)
def SplitRaster(in_raster=None, out_folder=None, out_base_name=None, split_method=None, format=None, resampling_type=None, num_rasters=None, tile_size=None, overlap=None, units=None, cell_size=None, origin=None, split_polygon_feature_class=None, clip_type=None, template_extent=None, nodata_value=None):
    """SplitRaster_management(in_raster, out_folder, out_base_name, split_method, format, {resampling_type}, {num_rasters}, {tile_size}, {overlap}, {units}, {cell_size}, {origin}, {split_polygon_feature_class}, {clip_type}, {template_extent}, {nodata_value})

        Divides a raster dataset into smaller pieces, by tiles or features from a
        polygon.

     INPUTS:
      in_raster (Raster Layer):
          The raster to split.
      out_folder (Folder):
          The destination for the new raster datasets.
      out_base_name (String):
          The prefix for each of the raster datasets you will create. A number will be
          appended to each prefix, starting with 0.
      split_method (String):
          Determines how to split the raster dataset.

          * SIZE_OF_TILE—Specify the width and height of the tile.

          * NUMBER_OF_TILES— Specify the number of raster tiles to create by breaking the
          dataset into a number of columns and rows.

          *  POLYGON_FEATURES— Use the individual polygon geometries in a feature class to
          split the raster.
      format (String):
          The format for the output raster datasets.

          * TIFF—Tagged Image File Format. This is the default.

          * BMP—Microsoft Bitmap.

          * ENVI—ENVI DAT.

          * Esri BIL—Esri Band Interleaved by Line.

          * Esri BIP—Esri Band Interleaved by Pixel.

          * Esri BSQ—Esri Band Sequential.

          * GIF—Graphic Interchange Format.

          * GRID—Esri Grid.

          * IMAGINE IMAGE—ERDAS IMAGINE.

          * JP2—JPEG 2000.

          * JPEG—Joint Photographic Experts Group.

          * PNG—Portable Network Graphics.
      resampling_type {String}:
          Choose an appropriate technique based on the type of data you have.

          * NEAREST—The fastest resampling method, and it minimizes changes to pixel
          values. Suitable for discrete data, such as land cover.

          * BILINEAR—Calculates the value of each pixel by averaging (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for continuous data.

          * CUBIC—Calculates the value of each pixel by fitting a smooth curve based on
          the surrounding 16 pixels. Produces the smoothest image, but can create values
          outside of the range found in the source data. Suitable for continuous data.

          * MAJORITY—Determines the value of each pixel based on the most popular value
          within a 3x3 window. Suitable for discrete data.
      num_rasters {Point}:
          The number of rows (x) and columns (y) to split the raster dataset into. This is
          a point whose X and Y coordinates define number of rows and columns. The X
          coordinate is the number of rows and the Y coordinate is the number of columns.
      tile_size {Point}:
          The x and y dimensions of the output tiles. The default unit of measurement is
          in pixels. You can change this with the units parameter. This is a point whose X
          and Y coordinates define the dimensions of output tiles. The X coordinate is the
          horizontal dimension of the output and the Y coordinate is the vertical
          dimension of the output.
      overlap {Double}:
          The tiles do not have to line up perfectly; set the amount of overlap between
          tiles with this parameter. The default unit of measurement is in pixels. You can
          change this with the units parameter.
      units {String}:
          Set the units of measurement for the tile_size and the overlap parameters.

          * PIXELS—The unit is in pixels. This is the default.

          * METERS—The unit is in meters.

          * FEET—The unit is in feet.

          * DEGREES—The unit is in decimal degrees.

          * MILES—The unit is in miles.

          * KILOMETERS—The unit is in kilometers.
      cell_size {Point}:
          The spatial resolution of the output raster. If left blank, the output cell size
          will match the input raster. When you change the cell size values, the tile size
          is reset to the image size and the tile count is reset to 1.
      origin {Point}:
          Change the coordinates for the lower left origin point, where the tiling scheme
          will begin. If left blank, the lower left origin would be the same as the input
          raster.
      split_polygon_feature_class {Feature Layer}:
          A feature class that will be used to split the raster dataset.
      clip_type {String}:
          Limits the extent of your raster dataset before you split it.

          * NONE— Use the full extent of the input raster dataset.

          * EXTENT—Specify bounding box as your clipping boundary.

          * FEATURE_CLASS—Specify a feature class to clip the extent.
      template_extent {Extent}:
          An extent or a dataset used to define the clipping boundary. The dataset can be
          a raster or feature class.
      nodata_value {String}:
          All the pixels with the specified value will be set to NoData in the output
          raster dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SplitRaster_management(*gp_fixargs((in_raster, out_folder, out_base_name, split_method, format, resampling_type, num_rasters, tile_size, overlap, units, cell_size, origin, split_polygon_feature_class, clip_type, template_extent, nodata_value), True)))
        return retval
    except Exception, e:
        raise e


# Raster\Raster Properties toolset
@gptooldoc('AddColormap_management', None)
def AddColormap(in_raster=None, in_template_raster=None, input_CLR_file=None):
    """AddColormap_management(in_raster, {in_template_raster}, {input_CLR_file})

        Adds a new colormap or replaces an existing colormap on a raster dataset.

     INPUTS:
      in_raster (Raster Layer):
          The raster dataset to add or replace a color map.
      in_template_raster {Raster Layer}:
          A raster dataset that has a colormap that you want to apply to the input raster
          dataset. If this is entered the input_CLR_file parameter cannot be specified.
      input_CLR_file {File}:
          Specify a .clr or .act file to use as the colormap."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddColormap_management(*gp_fixargs((in_raster, in_template_raster, input_CLR_file), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BatchBuildPyramids_management', None)
def BatchBuildPyramids(Input_Raster_Datasets=None, Pyramid_levels=None, Skip_first_level=None, Pyramid_resampling_technique=None, Pyramid_compression_type=None, Compression_quality=None, Skip_Existing=None):
    """BatchBuildPyramids_management(Input_Raster_Datasets;Input_Raster_Datasets..., {Pyramid_levels}, {Skip_first_level}, {Pyramid_resampling_technique}, {Pyramid_compression_type}, {Compression_quality}, {Skip_Existing})

        Builds pyramids for multiple raster datasets.

     INPUTS:
      Input_Raster_Datasets (Raster Dataset):
          The raster datasets for which you want to build raster pyramids.Each input
          should have more than 1024 rows and 1024 columns.
      Pyramid_levels {Long}:
          Choose the number of reduced-resolution dataset layers that will be built. The
          default value is -1, which will build full pyramids. A value of 0 will result in
          no pyramid levels.
      Skip_first_level {Boolean}:
          Choose whether to skip the first pyramid level. Skipping the first level will
          take up slightly less disk space, but it will slow down performance at these
          scales.

          * NONE—The first pyramid level will be built. This is the default.

          * SKIP_FIRST—The first pyramid level will not be built.
      Pyramid_resampling_technique {String}:
          The resampling technique used to build your pyramids.

          * NEAREST—The nearest neighbor resampling method uses the value of the closest
          cell to assign a value to the output cell when resampling. This is the default.

          * BILINEAR—The bilinear interpolation resampling method determines the new value
          of a cell based on a weighted distance average of the four nearest input cell
          centers.

          * CUBIC—The Cubic convolution resampling method determines the new value of a
          cell based on fitting a smooth curve through the 16 nearest input cell centers.
      Pyramid_compression_type {String}:
          The compression type to use when building the raster pyramids.

          * DEFAULT—If the source data is compressed using a wavelet compression, it will
          build pyramids with the JPEG compression type; otherwise, LZ77 will be used.
          This is the default compression method.

          * LZ77—The LZ77 compression algorithm will be used to build the pyramids. LZ77
          can be used for any data type.

          * JPEG—The JPEG compression algorithm to build pyramids. Only data that adheres
          to the JPEG compression specification can use this compression type. If JPEG is
          chosen, you can then set the compression quality.

          * JPEG_YCbCr—A lossy compression using the luma (Y) and chroma (Cb and Cr) color
          space components.

          * NONE—No compression will be used when building pyramids.
      Compression_quality {Long}:
          The compression quality to use when pyramids are built with the JPEG
          compression method. The value must be between 0 and 100. The values closer to
          100 would produce a higher-quality image, but the compression ratio would be
          lower.
      Skip_Existing {Boolean}:
          Specify whether to build pyramids only where they are missing or regenerate them
          even if they exist.

          * OVERWRITE—Pyramids will be built even if they already exist. Therefore,
          existing pyramids will be overwritten. This is the default.

          *  SKIP_EXISTING—Pyramids will only be built if they do not exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BatchBuildPyramids_management(*gp_fixargs((Input_Raster_Datasets, Pyramid_levels, Skip_first_level, Pyramid_resampling_technique, Pyramid_compression_type, Compression_quality, Skip_Existing), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BatchCalculateStatistics_management', None)
def BatchCalculateStatistics(Input_Raster_Datasets=None, Number_of_columns_to_skip=None, Number_of_rows_to_skip=None, Ignore_values=None, Skip_Existing=None):
    """BatchCalculateStatistics_management(Input_Raster_Datasets;Input_Raster_Datasets..., {Number_of_columns_to_skip}, {Number_of_rows_to_skip}, {Ignore_values;Ignore_values...}, {Skip_Existing})

        Calculates statistics for multiple raster datasets.

     INPUTS:
      Input_Raster_Datasets (Raster Dataset):
          The input raster datasets.
      Number_of_columns_to_skip {Long}:
          The number of horizontal pixels between samples.The value must be greater than
          zero and less than or equal to the number of
          columns in the raster. The default is 1 or the last skip factor used.The skip
          factors for raster datasets stored in a file geodatabase or an ArcSDE
          geodatabase are different. First, if the x and y skip factors are different, the
          smaller skip factor will be used for both the x and y skip factors. Second, the
          skip factor is related to the pyramid level that most closely fits the skip
          factor chosen. If the skip factor value is not equal to the number of pixels in
          a pyramid layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      Number_of_rows_to_skip {Long}:
          The number of vertical pixels between samples.The value must be greater than
          zero and less than or equal to the number of rows
          in the raster. The default is 1 or the last y skip factor used.The skip factors
          for raster datasets stored in a file geodatabase or an ArcSDE
          geodatabase are different. First, if the x and y skip factors are different, the
          smaller skip factor will be used for both the x and y skip factors. Second, the
          skip factor is related to the pyramid level that most closely fits the skip
          factor chosen. If the skip factor value is not equal to the number of pixels in
          a pyramid layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      Ignore_values {Double}:
          The pixel values that are not to be included in the statistics calculation.The
          default is no value.
      Skip_Existing {Boolean}:
          Specify whether to calculate statistics only where they are missing or
          regenerate them even if they exist.

          * OVERWRITE—Statistics will be calculated even if they already exist; therefore,
          existing statistics will be overwritten. This is the default.

          *  SKIP_EXISTING—Statistics will only be calculated if they do not already
          exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BatchCalculateStatistics_management(*gp_fixargs((Input_Raster_Datasets, Number_of_columns_to_skip, Number_of_rows_to_skip, Ignore_values, Skip_Existing), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildPyramids_management', None)
def BuildPyramids(in_raster_dataset=None, pyramid_level=None, SKIP_FIRST=None, resample_technique=None, compression_type=None, compression_quality=None, skip_existing=None):
    """BuildPyramids_management(in_raster_dataset, {pyramid_level}, {SKIP_FIRST}, {resample_technique}, {compression_type}, {compression_quality}, {skip_existing})

        Builds raster pyramids for your raster dataset.This tool can also be used to
        delete pyramids. To delete pyramids, set the
        Pyramids Levels parameter to 0.

     INPUTS:
      in_raster_dataset (Raster Dataset / Raster Layer):
          The raster dataset for which you want to build pyramids.The input should have
          more than 1024 rows and 1024 columns.
      pyramid_level {Long}:
          Choose the number of reduced-resolution dataset layers that will be built. The
          default value is -1, which will build full pyramids. A value of 0 will result in
          no pyramid levels.To delete pyramids, set the number of levels to 0.The maximum
          number of pyramid levels you can specify is 29. Any value that is 30
          or higher will revert to a value of -1, which will create a full set of
          pyramids.
      SKIP_FIRST {Boolean}:
          Choose whether to skip the first pyramid level. Skipping the first level will
          take up slightly less disk space, but it will slow down performance at these
          scales.

          * NONE—The first pyramid level will be built. This is the default.

          * SKIP_FIRST—The first pyramid level will not be built.
      resample_technique {String}:
          The resampling technique used to build your pyramids.

          * NEAREST—The nearest neighbor resampling method uses the value of the closest
          cell to assign a value to the output cell when resampling. This is the default.

          * BILINEAR—The bilinear interpolation resampling method determines the new value
          of a cell based on a weighted distance average of the four nearest input cell
          centers.

          * CUBIC—The Cubic convolution resampling method determines the new value of a
          cell based on fitting a smooth curve through the 16 nearest input cell centers.
      compression_type {String}:
          The compression type to use when building the raster pyramids.

          * DEFAULT—If the source data is compressed using a wavelet compression, it will
          build pyramids with the JPEG compression type; otherwise, LZ77 will be used.
          This is the default compression method.

          * LZ77—The LZ77 compression algorithm will be used to build the pyramids. LZ77
          can be used for any data type.

          * JPEG—The JPEG compression algorithm to build pyramids. Only data that adheres
          to the JPEG compression specification can use this compression type. If JPEG is
          chosen, you can then set the compression quality.

          * JPEG_YCBCR—A lossy compression using the luma (Y) and chroma (Cb and Cr) color
          space components.

          * NONE—No compression will be used when building pyramids.
      compression_quality {Long}:
          The compression quality to use when pyramids are built with the JPEG
          compression method. The value must be between 0 and 100. The values closer to
          100 would produce a higher-quality image, but the compression ratio would be
          lower.
      skip_existing {Boolean}:
          Specify whether to build pyramids only when they are missing or regenerate them
          even if they exist.

          * OVERWRITE—Pyramids will be built even if they already exist; therefore,
          existing pyramids will be overwritten. This is the default.

          * SKIP_EXISTING—Pyramids will only be built if they do not already exist."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildPyramids_management(*gp_fixargs((in_raster_dataset, pyramid_level, SKIP_FIRST, resample_technique, compression_type, compression_quality, skip_existing), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildPyramidsandStatistics_management', None)
def BuildPyramidsandStatistics(in_workspace=None, include_subdirectories=None, build_pyramids=None, calculate_statistics=None, BUILD_ON_SOURCE=None, block_field=None, estimate_statistics=None, x_skip_factor=None, y_skip_factor=None, ignore_values=None, pyramid_level=None, SKIP_FIRST=None, resample_technique=None, compression_type=None, compression_quality=None, skip_existing=None):
    """BuildPyramidsandStatistics_management(in_workspace, {include_subdirectories}, {build_pyramids}, {calculate_statistics}, {BUILD_ON_SOURCE}, {block_field}, {estimate_statistics}, {x_skip_factor}, {y_skip_factor}, {ignore_values;ignore_values...}, {pyramid_level}, {SKIP_FIRST}, {resample_technique}, {compression_type}, {compression_quality}, {skip_existing})

        Traverses a folder structure, building pyramids and calculating statistics for
        all the raster datasets it contains. It can also build pyramids and calculate
        statistics for all the items in a mosaic dataset.

     INPUTS:
      in_workspace (Text File / Mosaic Dataset / Workspace / Raster Catalog Layer / Raster Dataset / Mosaic Layer):
          The workspace that contains all the raster datasets to be processed, a mosaic
          dataset or a raster catalog.If the workspace includes a raster catalog or mosaic
          dataset, then these items
          will not be included when the tool runs.
      include_subdirectories {Boolean}:
          Specify whether to include subdirectories.

          * NONE—Does not include subdirectories.

          * INCLUDE_SUBDIRECTORIES—Includes all the raster datasets within the
          subdirectories when loading. This is the default.
          Raster catalogs and mosaic datasets must be specified as the input workspace. If
          the workspace includes a raster catalog or mosaic dataset, then these items will
          not be included when the tool runs.
      build_pyramids {Boolean}:
          Specify whether to build pyramids.

          * NONE—Does not build pyramids.

          * BUILD_PYRAMIDS—Builds pyramids. This is the default.
      calculate_statistics {Boolean}:
          Specify whether to calculate statistics.

          * NONE—Does not calculate statistics.

          * CALCULATE_STATISTICS—Calculates statistics. This is the default.
      BUILD_ON_SOURCE {Boolean}:
          Specify whether to build pyramids and calculate statistics on the source raster
          datasets or calculate statistics on the raster items in a mosaic dataset. This
          option only applies to mosaic datasets.

          * NONE—Statistics will be calculated for each raster item in the mosaic dataset
          (on each row in the attribute table). Any functions added to the raster item
          will be applied before generating the statistics. This is the default.

          * BUILD_ON_SOURCE—Builds pyramids and calculates statistics on the source data
          of the mosaic dataset.
      block_field {String}:
          The name of the field within a mosaic dataset's attribute table used to
          identify items that should be considered one item when performing some
          calculations and operations.
      estimate_statistics {Boolean}:
          Specify whether to calculate statistics for the mosaic dataset (not for the
          rasters within it). The statistics are derived from the existing statistics that
          have been calculated for each raster in the mosaic dataset.

          * NONE—Statistics are not calculated for the mosaic dataset. This is the
          default.

          * ESTIMATE_STATISTICS —Statistics will be calculated for the mosaic dataset.
      x_skip_factor {Long}:
          The number of horizontal pixels between samples.The value must be greater than
          zero and less than or equal to the number of
          columns in the raster. The default is 1 or the last skip factor used.
      y_skip_factor {Long}:
          The number of vertical pixels between samples.The value must be greater than
          zero and less than or equal to the number of rows
          in the raster. The default is 1 or the last y skip factor used.
      ignore_values {Long}:
          The pixel values that are not to be included in the statistics calculation.The
          default is no value.
      pyramid_level {Long}:
          Choose the number of reduced-resolution dataset layers that will be built. The
          default value is -1, which will build full pyramids. A value of 0 will result in
          no pyramid levels.The maximum number of pyramid levels you can specify is 29.
          Any value that is 30
          or higher will create a full set of pyramids.
      SKIP_FIRST {Boolean}:
          Choose whether to skip the first pyramid level. Skipping the first level will
          take up slightly less disk space, but it will slow down performance at these
          scales.

          * NONE—The first pyramid level will be built. This is the default.

          * SKIP_FIRST—The first pyramid level will not be built.
      resample_technique {String}:
          The resampling technique used to build your pyramids.

          * NEAREST—The nearest neighbor resampling method uses the value of the closest
          cell to assign a value to the output cell when resampling. This is the default.

          * BILINEAR—The bilinear interpolation resampling method determines the new value
          of a cell based on a weighted distance average of the four nearest input cell
          centers.

          * CUBIC—The Cubic convolution resampling method determines the new value of a
          cell based on fitting a smooth curve through the 16 nearest input cell centers.
      compression_type {String}:
          The compression type to use when building the raster pyramids.

          * DEFAULT—If the source data is compressed using a wavelet compression, it will
          build pyramids with the JPEG compression type; otherwise, LZ77 will be used.
          This is the default compression method.

          * LZ77—The LZ77 compression algorithm will be used to build the pyramids. LZ77
          can be used for any data type.

          * JPEG—The JPEG compression algorithm to build pyramids. Only data that adheres
          to the JPEG compression specification can use this compression type. If JPEG is
          chosen, you can then set the compression quality.

          * JPEG_YCBCR—A lossy compression using the luma (Y) and chroma (Cb and Cr) color
          space components.

          * NONE—No compression will be used when building pyramids.
      compression_quality {Long}:
          The compression quality to use when pyramids are built with the JPEG
          compression method. The value must be between 0 and 100. The values closer to
          100 would produce a higher-quality image, but the compression ratio would be
          lower.
      skip_existing {Boolean}:
          Specify whether to calculate statistics only where they are missing or
          regenerate them even if they exist.

          * SKIP_EXISTING—Statistics will only be calculated if they do not already exist.
          This is the default.

          * OVERWRITE—Statistics will be calculated even if they already exist. Therefore,
          existing statistics will be overwritten."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildPyramidsandStatistics_management(*gp_fixargs((in_workspace, include_subdirectories, build_pyramids, calculate_statistics, BUILD_ON_SOURCE, block_field, estimate_statistics, x_skip_factor, y_skip_factor, ignore_values, pyramid_level, SKIP_FIRST, resample_technique, compression_type, compression_quality, skip_existing), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('BuildRasterAttributeTable_management', None)
def BuildRasterAttributeTable(in_raster=None, overwrite=None):
    """BuildRasterAttributeTable_management(in_raster, {overwrite})

        Create or update a table with information about the classes in your raster
        datasets. This is used primarily with discrete data.

     INPUTS:
      in_raster (Raster Layer):
          Select a single band raster dataset that you want to add a table to. This tool
          will not run if the pixel type is floating point or double precision.
      overwrite {Boolean}:
          This allows you to overwrite or append columns and rows to an existing raster
          attribute table.

          * NONE—Existing raster attribute tables will not be overwritten, and any edits
          will be appended to the current table. This is the default.

          * OVERWRITE—Delete the existing raster attribute tables and create a new raster
          attribute table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.BuildRasterAttributeTable_management(*gp_fixargs((in_raster, overwrite), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateStatistics_management', None)
def CalculateStatistics(in_raster_dataset=None, x_skip_factor=None, y_skip_factor=None, ignore_values=None, skip_existing=None, area_of_interest=None):
    """CalculateStatistics_management(in_raster_dataset, {x_skip_factor}, {y_skip_factor}, {ignore_values;ignore_values...}, {skip_existing}, {area_of_interest})

        Calculates statistics for a raster dataset or mosaic dataset.Statistics are
        required for your raster and mosaic datasets to perform certain
        tasks, such as applying a contrast stretch or classifying your data.

     INPUTS:
      in_raster_dataset (Mosaic Dataset / Mosaic Layer / Raster Dataset):
          The input raster dataset or mosaic dataset.
      x_skip_factor {Long}:
          The number of horizontal pixels between samples.The value must be greater than
          zero and less than or equal to the number of
          columns in the raster. The default is 1 or the last skip factor used.The skip
          factors for raster datasets stored in a file geodatabase or an ArcSDE
          geodatabase are different. First, if the x and y skip factors are different, the
          smaller skip factor will be used for both the x and y skip factors. Second, the
          skip factor is related to the pyramid level that most closely fits the skip
          factor chosen. If the skip factor value is not equal to the number of pixels in
          a pyramid layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      y_skip_factor {Long}:
          The number of vertical pixels between samples.The value must be greater than
          zero and less than or equal to the number of rows
          in the raster. The default is 1 or the last y skip factor used.The skip factors
          for raster datasets stored in a file geodatabase or an ArcSDE
          geodatabase are different. First, if the x and y skip factors are different, the
          smaller skip factor will be used for both the x and y skip factors. Second, the
          skip factor is related to the pyramid level that most closely fits the skip
          factor chosen. If the skip factor value is not equal to the number of pixels in
          a pyramid layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      ignore_values {Long}:
          The pixel values that are not to be included in the statistics calculation.The
          default is no value, or the last ignore values used.
      skip_existing {Boolean}:
          Specify whether to calculate statistics only where they are missing or
          regenerate them even if they exist.

          * OVERWRITE—Statistics will be calculated even if they already exist; therefore,
          existing statistics will be overwritten. This is the default.

          *  SKIP_EXISTING—Statistics will only be calculated if they do not already
          exist.
      area_of_interest {Feature Set}:
          Specify a feature class that represents area in the dataset from where you want
          the statistics to be calculated, so they are not generated from the entire
          dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateStatistics_management(*gp_fixargs((in_raster_dataset, x_skip_factor, y_skip_factor, ignore_values, skip_existing, area_of_interest), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteColormap_management', None)
def DeleteColormap(in_raster=None):
    """DeleteColormap_management(in_raster)

        Removes the color map associated with a raster dataset.

     INPUTS:
      in_raster (Raster Layer):
          The raster dataset that containing the colormap you want to remove."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteColormap_management(*gp_fixargs((in_raster,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteRasterAttributeTable_management', None)
def DeleteRasterAttributeTable(in_raster=None):
    """DeleteRasterAttributeTable_management(in_raster)

        Removes the raster attribute table associated with a raster dataset.

     INPUTS:
      in_raster (Raster Layer):
          The raster dataset containing the attribute table you want to remove."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteRasterAttributeTable_management(*gp_fixargs((in_raster,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportRasterWorldFile_management', None)
def ExportRasterWorldFile(in_raster_dataset=None):
    """ExportRasterWorldFile_management(in_raster_dataset)

        Creates a world file based on the pixel size and the location of the upper left
        pixel.

     INPUTS:
      in_raster_dataset (Raster Dataset):
          The raster dataset from which you want to create the world file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportRasterWorldFile_management(*gp_fixargs((in_raster_dataset,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GetCellValue_management', None)
def GetCellValue(in_raster=None, location_point=None, band_index=None):
    """GetCellValue_management(in_raster, location_point, {band_index;band_index...})

        Retrieves the value of a given pixel using its x, y coordinates.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Layer):
          The raster that you want to query.
      location_point (Point):
          The X and Y coordinates of the pixel location.
      band_index {Value Table}:
          Specify the bands that you want to query. Leave blank to query all bands in a
          multiband dataset."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GetCellValue_management(*gp_fixargs((in_raster, location_point, band_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GetRasterProperties_management', None)
def GetRasterProperties(in_raster=None, property_type=None, band_index=None):
    """GetRasterProperties_management(in_raster, {property_type}, {band_index})

        Retrieves information from the metadata and descriptive statistics about a
        raster dataset.

     INPUTS:
      in_raster (Composite Geodataset):
          The raster containing the properties to retrieve.
      property_type {String}:
          The property to be obtained from the input raster.

          * MINIMUM—Smallest value of all cells in the input raster.

          * MAXIMUM—Largest value of all cells in the input raster.

          * MEAN—Average of all cells in the input raster.

          * STD—Standard deviation of all cells in the input raster.

          * UNIQUEVALUECOUNT—Number of unique values in the input raster.

          * TOP—Top or YMax value of the extent.

          * LEFT—Left or XMin value of the extent.

          * RIGHT—Right or XMax value of the extent.

          * BOTTOM—Bottom or YMin value of the extent.

          * CELLSIZEX—Cell size in the x-direction.

          * CELLSIZEY—Cell size in the y-direction.

          * VALUETYPE—Type of the cell value in the input raster:

          * 0 = 1-bit

          * 1 = 2-bit

          * 2 = 4-bit

          * 3 = 8-bit unsigned integer

          * 4 = 8-bit signed integer

          * 5 = 16-bit unsigned integer

          * 6 = 16-bit signed integer

          * 7 = 32-bit unsigned integer

          * 8 = 32-bit signed integer

          * 9 = 32-bit floating point

          * 10 = 64-bit double precision

          * 11 = 8-bit complex

          * 12 = 16-bit complex

          * 13 = 32-bit complex

          * 14 = 64-bit complex


          * COLUMNCOUNT—Number of columns in the input raster.

          * ROWCOUNT—Number of rows in the input raster.

          * BANDCOUNT—Number of bands in the input raster.

          * ANYNODATA—Returns whether there is NoData in the raster.

          * ALLNODATA—Returns whether all the pixels are NoData. This is the same as
          ISNULL.

          * SENSORNAME—Name of the sensor.

          * PRODUCTNAME—Product name related to the sensor.

          * ACQUSITIONDATE—Date that the data was captured.

          * SOURCETYPE—Source type.

          * CLOUDCOVER—Amount of cloud cover as a percentage.

          * SUNAZIMUTH—Sun azimuth, in degrees.

          * SUNELEVATION—Sun elevation, in degrees.

          * SENSORAZIMUTH—Sensor azimuth, in degrees.

          * SENSORELEVATION—Sensor elevation, in degrees.

          * OFFNADIR—Off-nadir angle, in degrees.

          * WAVELENGTH—Wavelength range of the band, in nanometers.
      band_index {String}:
          Choose the band name from which to get the properties. If no band is chosen,
          then the first band will be used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GetRasterProperties_management(*gp_fixargs((in_raster, property_type, band_index), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetRasterProperties_management', None)
def SetRasterProperties(in_raster=None, data_type=None, statistics=None, stats_file=None, nodata=None, key_properties=None):
    """SetRasterProperties_management(in_raster, {data_type}, {statistics;statistics...}, {stats_file}, {nodata;nodata...}, {key_properties;key_properties...})

        Sets the data type, statistics, and NoData values on a raster or mosaic dataset.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer):
          The raster or mosaic dataset whose properties you want to set.
      data_type {String}:
          The type of imagery in the mosaic dataset.

          * GENERIC— The mosaic dataset does not have a specified data type.

          * ELEVATION— The mosaic dataset contains elevation data.

          * THEMATIC—Thematic data has discrete values, such as land cover.

          * PROCESSED—The mosaic dataset has been color balanced.

          * SCIENTIFIC—The data has scientific information, and will be displayed with the
          blue to red color ramp, by default.

          * VECTOR_UV—The data is a two band raster that contains a U and a V component of
          vector field data.

          * VECTOR_MAGDIR—The data is a two band raster that contains the magnitude and
          direction of vector field data.
      statistics {Value Table}:
          Specify the bands and values for the minimum, maximum, mean, and standard
          deviation.
      stats_file {File}:
          An .xml file that contains the statistics. To create this file, export the
          statistics from another raster or mosaic dataset.
      nodata {Value Table}:
          Specify the NoData value for each band. Each band can have a unique NoData
          value defined, or the same value can be specified for all bands. If you want to
          define multiple NoData values for each band selection, use a space delimiter
          between each NoData value within the bands_for_nodata_value parameter.
      key_properties {Value Table}:
          The natively supported properties are as follows. Your data may have additional
          properties not included in this list. All properties are case insensitive.

          * Footprint

          * AcquisitionDate

          * CloudCover

          * SensorName

          * ProductName

          * SunAzimuth

          * SunElevation

          * SensorAzimuth

          * SensorElevation

          * OffNadir

          * VerticalAccuracy

          * BlockName

          * Variable

          * Dimensions

          * StdZ

          * StdTime

          * StdPressure

          * StdTemperature

          * StdZ_max

          * StdTime_Max

          * StdPressure_Max

          * StdTemperature_Max

          * Segmented

          * PerspectiveX

          * PerspectiveY

          * PerspectiveZ

          * WavelengthMin

          * WavelengthMax

          * BandName

          * SolarIrradiance

          * RadianceGain

          * RadianceBias

          * SourceBandIndex

          * RefelctanceGain

          * ReflectanceBias

          * ThermalConstant_K1

          * ThermalConstant_K2

          * ParentRasterType

          * ParentTemplate

          * DatasetTag

          * LowCellSize

          * HighCellSize

          * MinCellSize

          * MaxCellSize

          * FlowDirection"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetRasterProperties_management(*gp_fixargs((in_raster, data_type, statistics, stats_file, nodata, key_properties), True)))
        return retval
    except Exception, e:
        raise e


# Relationship Classes toolset
@gptooldoc('CreateRelationshipClass_management', None)
def CreateRelationshipClass(origin_table=None, destination_table=None, out_relationship_class=None, relationship_type=None, forward_label=None, backward_label=None, message_direction=None, cardinality=None, attributed=None, origin_primary_key=None, origin_foreign_key=None, destination_primary_key=None, destination_foreign_key=None):
    """CreateRelationshipClass_management(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, attributed, origin_primary_key, origin_foreign_key, {destination_primary_key}, {destination_foreign_key})

        This tool creates a relationship class to store an association between fields or
        features in the origin table and the destination table.

     INPUTS:
      origin_table (Table View):
          The table or feature class that is associated to the destination table.
      destination_table (Table View):
          The table that is associated to the origin table.
      relationship_type (String):
          The type of relationship to create between the origin and destination tables.

          * SIMPLE—A relationship between independent objects (parent to parent). This is
          the default.

          * COMPOSITE—A relationship between dependent objects where the lifetime of one
          object controls the lifetime of the related object (parent to child).
      forward_label (String):
          A name to uniquely identify the relationship when navigating from the origin
          table to the destination table.
      backward_label (String):
          A name to uniquely identify the relationship when navigating from the
          destination table to the origin table.
      message_direction (String):
          The direction in which messages are passed between the origin and destination
          tables. For example, in a relationship between poles and transformers, when the
          pole is deleted, it sends a message to its related transformer objects informing
          them it was deleted.

          * FORWARD—Messages are passed from the origin to the destination table.

          * BACK—Messages are passed from the destination to the origin table.

          * BOTH—Messages are passed from the origin to the destination table and from the
          destination to the origin table.

          * NONE—No messages passed. This is the default.
      cardinality (String):
          Determines how many relationships exist between rows or features in the origin
          and rows or features in the destination table.

          * ONE_TO_ONE—Each row or feature in the origin table can be related to zero or
          one row or feature in the destination table. This is the default.

          * ONE_TO_MANY—Each row or feature in the origin table can be related to one or
          several rows or features in the destination table.

          * MANY_TO_MANY—Several fields or features in the origin table can be related to
          one or several rows or features in the destination table.
      attributed (Boolean):
          Specifies if the relationship will have attributes.

          * NONE—Indicates the relationship class will not have attributes. This is the
          default.

          * ATTRIBUTED—Indicates the relationship class will have attributes.
      origin_primary_key (String):
          The field in the origin table, typically the OID field, that links it to the
          Origin Foreign Key field in the relationship class table.
      origin_foreign_key (String):
          The field in the relationship class table that links it to the Origin Primary
          Key field in the origin table.
      destination_primary_key {String}:
          The field in the destination table, typically the OID field, that links it to
          the Destination Foreign Key field in the relationship class table.
      destination_foreign_key {String}:
          The field in the relationship class table that links it to the Destination
          Primary Key field in the destination table.

     OUTPUTS:
      out_relationship_class (Relationship Class):
          The relationship class that is created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateRelationshipClass_management(*gp_fixargs((origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, attributed, origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MigrateRelationshipClass_management', None)
def MigrateRelationshipClass(in_relationship_class=None):
    """MigrateRelationshipClass_management(in_relationship_class)

        Migrates an ObjectID-based relationship class to a GlobalID-based relationship
        class.

     INPUTS:
      in_relationship_class (Relationship Class):
          ObjectID-based relationship class that will be migrated to a GlobalID-based
          relationship class. The origin and destination feature classes or tables must
          already have GlobalIDs."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MigrateRelationshipClass_management(*gp_fixargs((in_relationship_class,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToRelationshipClass_management', None)
def TableToRelationshipClass(origin_table=None, destination_table=None, out_relationship_class=None, relationship_type=None, forward_label=None, backward_label=None, message_direction=None, cardinality=None, relationship_table=None, attribute_fields=None, origin_primary_key=None, origin_foreign_key=None, destination_primary_key=None, destination_foreign_key=None):
    """TableToRelationshipClass_management(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, relationship_table, attribute_fields;attribute_fields..., origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key)

        Creates an attributed relationship class from the origin, destination, and
        relationship tables.

     INPUTS:
      origin_table (Table View):
          The table or feature class that will be associated to the destination table.
      destination_table (Table View):
          The table or feature class that will be associated to the origin table.
      relationship_type (String):
          The type of association to create between the origin and destination tables.

          * SIMPLE—An association where each object is independent of each other (a
          parent-to-parent relationship). This is the default.

          * COMPOSITE—An association where the lifetime of one object controls the
          lifetime of its related object (a parent-child relationship).
      forward_label (String):
          A label describing the relationship as it is traversed from the origin
          table/feature class to the destination table/feature class.
      backward_label (String):
          A label describing the relationship as it is traversed from the destination
          table/feature class to the origin table/feature class.
      message_direction (String):
          The direction messages will be propagated between the objects in the
          relationship. For example, in a relationship between poles and transformers,
          when the pole is deleted, it sends a message to its related transformer objects
          informing them it was deleted.

          * NONE—No messages propagated. This is the default.

          * FORWARD—Messages propagated from the origin to the destination.

          * BACKWARD—Messages propagated from the destination to the origin.

          * BOTH—Messages propagated from the origin to the destination and from the
          destination to the origin.
      cardinality (String):
          The cardinality of the relationship between the origin and destination.

          * ONE_TO_ONE—Each object of the origin table/feature class can be related to
          zero or one object of the destination table/feature class. This is the default.

          * ONE_TO_MANY—Each object of the origin table/feature class can be related to
          multiple objects in the destination table/feature class.

          * MANY_TO_MANY—Multiple objects of the origin table/feature class can be related
          to multiple objects in the destination table/feature class.
      relationship_table (Table View):
          The table containing attributes that will be added to the relationship class.
      attribute_fields (Field):
          The fields containing attribute values that will be added to the relationship
          class.
      origin_primary_key (String):
          The field in the origin table that will be used to create the relationship.
          Generally, this is the object identifier field.
      origin_foreign_key (String):
          The name of the Foreign Key field in the relationship table that refers to the
          Primary Key field in the origin table/feature class.
      destination_primary_key (String):
          The field in the destination table that will be used to create the relationship.
          Generally, this is the object identifier field.
      destination_foreign_key (String):
          The field in the relationship table that refers to the Primary Key field in the
          destination table.

     OUTPUTS:
      out_relationship_class (Relationship Class):
          The relationship class that will be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToRelationshipClass_management(*gp_fixargs((origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, relationship_table, attribute_fields, origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key), True)))
        return retval
    except Exception, e:
        raise e


# Subtypes toolset
@gptooldoc('AddSubtype_management', None)
def AddSubtype(in_table=None, subtype_code=None, subtype_description=None):
    """AddSubtype_management(in_table, subtype_code, subtype_description)

        Adds a new subtype to the subtypes in the input table.

     INPUTS:
      in_table (Table View):
          The feature class or table containing the subtype definition to be updated
      subtype_code (Long):
          A unique integer value for the subtype to be added
      subtype_description (String):
          A description of the subtype code"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddSubtype_management(*gp_fixargs((in_table, subtype_code, subtype_description), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveSubtype_management', None)
def RemoveSubtype(in_table=None, subtype_code=None):
    """RemoveSubtype_management(in_table, subtype_code;subtype_code...)

        Removes a subtype from the input table using its code.

     INPUTS:
      in_table (Table View):
          The feature class or table containing the subtype definition.
      subtype_code (String):
          The code used to remove a subtype from the input table or feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveSubtype_management(*gp_fixargs((in_table, subtype_code), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetDefaultSubtype_management', None)
def SetDefaultSubtype(in_table=None, subtype_code=None):
    """SetDefaultSubtype_management(in_table, subtype_code)

        Sets the default value or code for the input table's subtype.

     INPUTS:
      in_table (Table View):
          The input table or feature class whose subtype default value will be set.
      subtype_code (Long):
          The unique default value for a subtype."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetDefaultSubtype_management(*gp_fixargs((in_table, subtype_code), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetSubtypeField_management', None)
def SetSubtypeField(in_table=None, field=None, clear_value=None):
    """SetSubtypeField_management(in_table, {field}, {clear_value})

        Defines the field in the input table or feature class that stores the subtype
        codes.

     INPUTS:
      in_table (Table View):
          The input table or feature class which contains the field to set as a subtype
          field.
      field {Field}:
          An integer field that will store the subtype codes.
      clear_value {Boolean}:
          Specifies whether to clear the subtype field.

          * TRUE—The subtype field will be cleared (set to null).

          * FALSE—The subtype field will not be cleared. This is the default."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetSubtypeField_management(*gp_fixargs((in_table, field, clear_value), True)))
        return retval
    except Exception, e:
        raise e


# Table toolset
@gptooldoc('Analyze_management', None)
def Analyze(in_dataset=None, components=None):
    """Analyze_management(in_dataset, components;components...)

        Updates database statistics of business tables, feature tables, and delta
        tables, along with the statistics of those tables' indexes.

     INPUTS:
      in_dataset (Layer / Table View / Dataset):
          The table or feature class to be analyzed.
      components (String):
          The component type to be analyzed.

          * BUSINESS—Updates business rules statistics.

          * FEATURE—Updates feature statistics.

          * RASTER—Updates statistics on raster tables.

          * ADDS—Updates statistics on added datasets.

          * DELETES—Updates statistics on deleted datasets."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.Analyze_management(*gp_fixargs((in_dataset, components), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CopyRows_management', None)
def CopyRows(in_rows=None, out_table=None, config_keyword=None):
    """CopyRows_management(in_rows, out_table, {config_keyword})

        Writes the rows from an input table, table view, feature class, or feature layer
        to a new table. If a selection is defined on a feature class or feature layer in
        ArcMap, only the selected rows are copied out.

     INPUTS:
      in_rows (Table View / Raster Layer):
          The rows from a feature class, layer, table, or table view to be copied.
      config_keyword {String}:
          The config keyword specifies the default storage parameters for an ArcSDE
          geodatabase.

     OUTPUTS:
      out_table (Table):
          The table to which the rows will be written. The output table can be saved in a
          dBASE, ArcSDE geodatabase, file geodatabase, or personal geodatabase, or as an
          INFO table.The table to which the rows will be written. The output table can be
          saved in a
          dBASE, ArcSDE geodatabase, file geodatabase, or personal geodatabase, or as an
          INFO table."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CopyRows_management(*gp_fixargs((in_rows, out_table, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateTable_management', None)
def CreateTable(out_path=None, out_name=None, template=None, config_keyword=None):
    """CreateTable_management(out_path, out_name, {template;template...}, {config_keyword})

        Creates an ArcSDE, file, or personal geodatabase table, or an INFO or dBASE
        table.

     INPUTS:
      out_path (Workspace):
          The ArcSDE, file, or personal geodatabase or workspace in which the output table
          will be created.
      out_name (String):
          The name of the table to be created.
      template {Table View}:
          A table whose attribute schema is used to define the output table. Fields in the
          template table(s) will be added to the output table.
      config_keyword {String}:
          The configuration keyword that determines the storage parameters of the table in
          an ArcSDE geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateTable_management(*gp_fixargs((out_path, out_name, template, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateUnRegisteredTable_management', None)
def CreateUnRegisteredTable(out_path=None, out_name=None, template=None, config_keyword=None):
    """CreateUnRegisteredTable_management(out_path, out_name, {template;template...}, {config_keyword})

        This tool creates an empty table in a database or enterprise geodatabase. The
        table is not registered with the geodatabase.

     INPUTS:
      out_path (Workspace):
          The enterprise geodatabase or database in which the output table will be
          created.
      out_name (String):
          The name of the table to be created.
      template {Table View}:
          A table or list of tables whose fields and attribute schema are used to define
          the fields in the output table.
      config_keyword {String}:
          Determines the storage parameters of the table in an enterprise geodatabase."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateUnRegisteredTable_management(*gp_fixargs((out_path, out_name, template, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteRows_management', None)
def DeleteRows(in_rows=None):
    """DeleteRows_management(in_rows)

        Deletes all or the selected subset of rows from the input.If the input rows are
        from a feature class or table, all rows will be deleted.
        If the input rows are from a layer or table view with no selection, all rows
        will be deleted.

     INPUTS:
      in_rows (Table View):
          The feature class, layer, table, or table view whose rows will be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteRows_management(*gp_fixargs((in_rows,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GetCount_management', None)
def GetCount(in_rows=None):
    """GetCount_management(in_rows)

        Returns the total number of rows for a feature class, table, layer, or raster.

     INPUTS:
      in_rows (Table View / Raster Layer):
          The input table view or raster layer. If a selection is defined on the input,
          the count of the selected rows is returned."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GetCount_management(*gp_fixargs((in_rows,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('PivotTable_management', None)
def PivotTable(in_table=None, fields=None, pivot_field=None, value_field=None, out_table=None):
    """PivotTable_management(in_table, fields;fields..., pivot_field, value_field, out_table)

        Creates a table from the input table by reducing redundancy in records and
        flattening one-to-many relationships.

     INPUTS:
      in_table (Table View):
          The table whose records will be pivoted.
      fields (Field):
          The fields that define records to be included in the output table.
      pivot_field (Field):
          The field whose record values are used to generate the field names in the output
          table.
      value_field (Field):
          The field whose values populate the pivoted fields in the output table.

     OUTPUTS:
      out_table (Table):
          The table to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.PivotTable_management(*gp_fixargs((in_table, fields, pivot_field, value_field, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TruncateTable_management', None)
def TruncateTable(in_table=None):
    """TruncateTable_management(in_table)

        Removes all rows from a database table or feature class using truncate
        procedures in the database.

     INPUTS:
      in_table (Table View):
          Input database table or feature class that will be truncated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TruncateTable_management(*gp_fixargs((in_table,), True)))
        return retval
    except Exception, e:
        raise e


# Tile Cache toolset
@gptooldoc('ExportTileCache_management', None)
def ExportTileCache(in_cache_source=None, in_target_cache_folder=None, in_target_cache_name=None, export_cache_type=None, storage_format_type=None, scales=None, area_of_interest=None):
    """ExportTileCache_management(in_cache_source, in_target_cache_folder, in_target_cache_name, {export_cache_type}, {storage_format_type}, {scales;scales...}, {area_of_interest})

        Exports tiles from an existing tile cache to a new tile cache or a tile
        package. The tiles can either be independently imported into other caches or
        they can be accessed from ArcGIS for Desktop or mobile devices as a raster
        dataset.

     INPUTS:
      in_cache_source (Raster Layer / Raster Dataset):
          An existing tile cache to be exported.
      in_target_cache_folder (Folder):
          The output folder into which the tile cache or tile package will be exported.
      in_target_cache_name (String):
          The name of the exported tile cache or tile package.
      export_cache_type {String}:
          Choose to export cache as a tile cache or a tile package. Tile packages are
          suitable for ArcGIS Runtime and ArcGIS Mobile deployments.

          * TILE_CACHE—A stand-alone cache raster dataset. This is the default.

          * TILE_PACKAGE—A single compressed file (.tpk) where the cache dataset is added
          as a layer and consolidated so that it can be shared easily. Usable in ArcMap as
          well as in ArcGIS Runtime and ArcGIS Mobile applications.
      storage_format_type {String}:
          Determines the storage format of tiles. The default storage format is COMPACT.

          * COMPACT—Group tiles into large files called bundles. This storage format is
          more efficient in terms of storage and mobility. This is the default.

          *  EXPLODED—Each tile is stored as an individual file.Note that this format
          cannot be used with tile packages.
      scales {Double}:
          A list of scale levels at which tiles will be exported.
      area_of_interest {Feature Set}:
          An area of interest that spatially constrains where tiles are exported from the
          cache.The area of interest can be a feature class or a feature that you draw on
          the
          map.This parameter is useful if you want to export irregularly shaped areas, as
          the
          tool clips the cache dataset at pixel resolution."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportTileCache_management(*gp_fixargs((in_cache_source, in_target_cache_folder, in_target_cache_name, export_cache_type, storage_format_type, scales, area_of_interest), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateTileCacheTilingScheme_management', None)
def GenerateTileCacheTilingScheme(in_dataset=None, out_tiling_scheme=None, tiling_scheme_generation_method=None, number_of_scales=None, predefined_tiling_scheme=None, scales=None, scales_type=None, tile_origin=None, dpi=None, tile_size=None, tile_format=None, tile_compression_quality=None, storage_format=None, lerc_error=None):
    """GenerateTileCacheTilingScheme_management(in_dataset, out_tiling_scheme, tiling_scheme_generation_method, number_of_scales, {predefined_tiling_scheme}, {scales;scales...}, {scales_type}, {tile_origin}, {dpi}, {tile_size}, {tile_format}, {tile_compression_quality}, {storage_format}, {lerc_error})

        Creates a tiling scheme file based on the information from the source dataset.
        The tiling scheme file will then be used in the Manage Tile Cache tool when
        creating cache tiles.This tool can be used to edit the properties of an existing
        tiling scheme, such
        as tile format, storage format, tile size, and so on. In addition, you can also
        use it to add new scale levels to an existing tiling scheme.

     INPUTS:
      in_dataset (Raster Layer / Mosaic Layer / ArcMap Document):
          The source to be used to generate the tiling scheme. It can be a raster
          dataset, a mosaic dataset, or a map.
      tiling_scheme_generation_method (String):
          Choose to use a new or predefined tiling scheme. You can define a new tiling
          scheme with this tool or browse to a predefined tiling scheme file (.xml).

          * NEW—Define a new tiling scheme using other parameters in this tool to define
          scale levels, image format, storage format, and so on. This is the default.

          * PREDEFINED—Use a tiling scheme .xml file that already exists on disk.
      number_of_scales (Long):
          The number of scale levels to be created in the tiling scheme.
      predefined_tiling_scheme {File}:
          Path to a predefined tiling scheme file (usually named conf.xml). This parameter
          is enabled only when the Predefined option is chosen as the tiling scheme
          generation method.
      scales {Value Table}:
          Scale levels to be included in the tiling scheme. By default, these are not
          represented as fractions. Instead, use 500 to represent a scale of 1:500, and so
          on. The value entered in the Number of Scales parameter generates a set of
          default scale levels.
      scales_type {Boolean}:
          Determines the units of the scales parameter.

          * CELL_SIZE—Indicates the values of the scales parameter are pixel sizes. This
          is the default.

          * SCALE—Indicates the values of the scales parameter are scale levels.
      tile_origin {Point}:
          The origin (upper left corner) of the tiling scheme in the coordinates of the
          spatial reference of the source dataset. The extent of the source dataset must
          be within (but does not need to coincide) this region.
      dpi {Long}:
          The dots per inch of the intended output device. If a DPI is chosen that does
          not match the resolution of the output device, typically a display monitor, the
          scale of the tile will appear incorrect. The default value is 96.
      tile_size {String}:
          The width and height of the cache tiles in pixels. The default is 256x256.For
          the best balance between performance and manageability, avoid deviating from
          widths of 256 or 512.

          *  128 x 128— Tile width and height of 128 pixels.

          * 256 x 256—Tile width and height of 256 pixels.

          * 512 x 512—Tile width and height of 512 pixels.

          * 1024 x 1024—Tile width and height of 1024 pixels.
      tile_format {String}:
          The file format for the tiles in the cache.

          *  PNG—Creates PNG format with varying bit depths. The bit depths are optimized
          according to the color variation and transparency values in each tile.

          * PNG8—A lossless, 8-bit color, image format that uses an indexed color palette
          and an alpha table. Each pixel stores a value (0 to 255) that is used to look up
          the color in the color palette and the transparency in the alpha table. 8-bit
          PNGs are similar to GIF images and provide the best support for a transparent
          background by most web browsers.

          * PNG24—A lossless, three-channel image format that supports large color
          variations (16 million colors) and has limited support for transparency. Each
          pixel contains three 8-bit color channels, and the file header contains the
          single color that represents the transparent background. The color representing
          the transparent background color can be set in the application. Versions of
          Internet Explorer less than version 7 do not support this type of transparency.
          Caches using PNG24 are significantly larger than those using PNG8 or JPEG, so
          will take more disk space and require greater bandwidth to serve clients.

          * PNG32—A lossless, four-channel image format that supports large color
          variations (16 million colors) and transparency. Each pixel contains three 8-bit
          color channels and one 8-bit alpha channel that represents the level of
          transparency for each pixel. While the PNG32 format allows for partially
          transparent pixels in the range from 0 to 255, the ArcGIS Server cache
          generation tool only writes fully transparent (0) or fully opaque (255) values
          in the transparency channel. Caches using PNG32 are significantly larger than
          the other supported formats, so will take more disk space and require greater
          bandwidth to serve clients.

          * JPEG—A lossy, three-channel image format that supports large color variations
          (16 million colors) but does not support transparency. Each pixel contains three
          8-bit color channels. Caches using JPEG provide control over output quality and
          size.

          * MIXED—Creates PNG 32 anywhere that transparency is detected (in other words,
          anyplace where the data frame background is visible), but creates JPEG for the
          remaining tiles. This keeps the average file size down while providing you with
          a clean overlay on top of other caches. This is the default.
      tile_compression_quality {Long}:
          Enter a value between 1 and 100 for the JPEG or MIXED compression quality. The
          default value is 75.Compression is supported only for MIXED and JPEG format.
          Choosing a higher value
          will result in higher-quality images, but the file sizes will be larger. Using a
          lower value will result in lower-quality images with smaller file sizes.
      storage_format {String}:
          Determines the storage format of tiles.

          * COMPACT—Group tiles into large files called bundles. This storage format is
          more efficient in terms of storage and mobility. This is the default.

          *  EXPLODED—Each tile is stored as an individual file.Note that this format
          cannot be used with tile packages.
      lerc_error {Double}:
          LERC Error

     OUTPUTS:
      out_tiling_scheme (File):
          Path and file to the output tiling scheme to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateTileCacheTilingScheme_management(*gp_fixargs((in_dataset, out_tiling_scheme, tiling_scheme_generation_method, number_of_scales, predefined_tiling_scheme, scales, scales_type, tile_origin, dpi, tile_size, tile_format, tile_compression_quality, storage_format, lerc_error), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ImportTileCache_management', None)
def ImportTileCache(in_cache_target=None, in_cache_source=None, scales=None, area_of_interest=None):
    """ImportTileCache_management(in_cache_target, in_cache_source, {scales;scales...}, {area_of_interest})

        Imports tiles from an existing tile cache or a tile package. The target cache
        must have the same tiling scheme, spatial reference, and storage format as the
        source tile cache.

     INPUTS:
      in_cache_target (Raster Layer):
          An existing tile cache to which the tiles will be imported.
      in_cache_source (Raster Layer / File):
          An existing tile cache or a tile package from which the tiles are imported.
      scales {Double}:
          A list of scale levels at which tiles will be imported.
      area_of_interest {Feature Set}:
          An area of interest will spatially constrain where tiles are imported into the
          cache.It can be a feature class, or it can be a feature that you interactively
          define
          in ArcMap.This parameter is useful if you want to import tiles for irregularly
          shaped
          areas."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ImportTileCache_management(*gp_fixargs((in_cache_target, in_cache_source, scales, area_of_interest), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ManageTileCache_management', None)
def ManageTileCache(in_cache_location=None, manage_mode=None, in_cache_name=None, in_datasource=None, tiling_scheme=None, import_tiling_scheme=None, scales=None, area_of_interest=None, max_cell_size=None, min_cached_scale=None, max_cached_scale=None):
    """ManageTileCache_management(in_cache_location, manage_mode, {in_cache_name}, {in_datasource}, {tiling_scheme}, {import_tiling_scheme}, {scales;scales...}, {area_of_interest}, {max_cell_size}, {min_cached_scale}, {max_cached_scale})

        Creates a tile cache or updates tiles in an existing tile cache. You can use
        this tool to create new tiles, replace missing tiles, overwrite outdated tiles,
        and delete tiles.

     INPUTS:
      in_cache_location (Raster Layer / Folder):
          The folder in which the cache dataset is created or the path to an existing tile
          cache.
      manage_mode (String):
          The mode for managing the cache.

          * RECREATE_ALL_TILES—Existing tiles will be replaced and new tiles will be added
          if the extent has changed or if layers have been added to a multilayer cache.

          *  RECREATE_EMPTY_TILES—Only tiles that are empty will be created. Existing
          tiles will be left unchanged.

          *  DELETE_TILES—Tiles will be deleted from the cache. The cache folder structure
          will not be deleted.
      in_cache_name {String}:
          Name of the cache dataset to be created inside  the cache location.
      in_datasource {Mosaic Layer / Raster Layer / ArcMap Document}:
          A raster dataset, mosaic dataset, or a map document.This parameter is not
          required when DELETE_TILES is specified in the manage_mode
          parameter.An ArcMap document (.mxd) cannot contain a map service or image
          service.
      tiling_scheme {String}:
          An optional parameter to specify tiling scheme.

          * ARCGISONLINE_SCHEME—Use the default ArcGIS Online tiling scheme.

          *  IMPORT_SCHEME—Import an existing tiling scheme.
      import_tiling_scheme {File / Image Service / MapServer}:
          Path to an existing scheme file (.xml) or imported from an existing image
          service or map service.
      scales {Double}:
          The scale levels at which you will create or delete tiles when running this
          tool, depending on the value of the manage_mode parameter. The pixel size is
          represented based on the spatial reference of the tiling scheme.

          * By default, only the scales within the min_cached_scale and max_cached_scale
          will be used when generating cache.

          * Altering the value of either min_cached_scale or max_cached_scale parameters
          will change which scales are used when generating cache.

          * Scales that exist but are not within the range of min_cached_scale or
          max_cached_scale are ignored when generating the cache.
      area_of_interest {Feature Set}:
          Defines an area of interest to constrain where tiles will be created or
          deleted.It can be a feature class, or it can be a feature that you interactively
          define
          in ArcMap.This parameter is useful if you want to manage tiles for irregularly
          shaped
          areas. It's also useful in situations where you want to precache some areas and
          leave less-visited areas uncached.
      max_cell_size {Double}:
          The value that defines the visibility of the data source for which the cache
          will be generated. By default, the value is empty.If the value is empty

          * For levels of cache that lie within the visibility ranges of the data source,
          the cache is generated from the data source.

          * For levels of cache that fall outside the visibility of the data source, the
          cache is generated from the previous level of cache.
          If the value is greater than zero

          * For levels with cell sizes smaller than or equal to Maximum Source Cell Size
          (max_cell_size), the cache is generated from the data source.

          * For levels with cell sizes greater than Maximum Source Cell Size
          (max_cell_size), the cache is generated from the previous level of cache.
          The unit of the Maximum Source Cell Size value should be the same as the unit of
          the cell size of the source dataset.
      min_cached_scale {Double}:
          The minimum scale at which you want to create tiles. This does not have to be
          the smallest scale in your tiling scheme. Your minimum cache scale will
          determine which scales are used when generating cache.
      max_cached_scale {Double}:
          The maximum scale at which you want to create tiles. This does not have to be
          the largest scale in your tiling scheme. The maximum cache scale will determine
          which scales are used when generating cache."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ManageTileCache_management(*gp_fixargs((in_cache_location, manage_mode, in_cache_name, in_datasource, tiling_scheme, import_tiling_scheme, scales, area_of_interest, max_cell_size, min_cached_scale, max_cached_scale), True)))
        return retval
    except Exception, e:
        raise e


# Topology toolset
@gptooldoc('AddFeatureClassToTopology_management', None)
def AddFeatureClassToTopology(in_topology=None, in_featureclass=None, xy_rank=None, z_rank=None):
    """AddFeatureClassToTopology_management(in_topology, in_featureclass, xy_rank, z_rank)

        Adds a feature class to a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology to which the feature class will participate.
      in_featureclass (Feature Layer):
          The feature class to add to the topology. The feature class must be in the same
          feature dataset as the topology.
      xy_rank (Long):
          The relative degree of positional accuracy associated with vertices of features
          in the feature class versus those in other feature classes participating in the
          topology. The feature class with the highest accuracy should get a higher rank
          (lower number, for example, 1) than a feature class which is known to be less
          accurate.
      z_rank (Long):
          Feature classes that are z-aware have elevation values embedded in their
          geometry for each vertex. By setting a z rank, you can influence how vertices
          with accurate z-values are snapped or clustered with vertices that contain less
          accurate z measurements."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddFeatureClassToTopology_management(*gp_fixargs((in_topology, in_featureclass, xy_rank, z_rank), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AddRuleToTopology_management', None)
def AddRuleToTopology(in_topology=None, rule_type=None, in_featureclass=None, subtype=None, in_featureclass2=None, subtype2=None):
    """AddRuleToTopology_management(in_topology, rule_type, in_featureclass, {subtype}, {in_featureclass2}, {subtype2})

        Adds a new rule to a topology.The rules you choose to add depend on the spatial
        relationships that you wish to
        monitor for the feature classes that participate in the topology.For a complete
        list and description of the available topology rules see
        Geodatabase topology rules and topology error fixes

     INPUTS:
      in_topology (Topology Layer):
          The topology to which the new rule will be added.
      rule_type (String):
          The topology rule to be added. For a complete list of the rules and what they
          do, see the tool's help page.
      in_featureclass (Feature Layer):
          The input or origin feature class.
      subtype {String}:
          The subtype for the input or origin feature class. Enter the subtype's
          description (not the code). If subtypes do not exist on the origin feature
          class, or you want the rule to be applied to all subtypes in the feature class
          leave this blank.
      in_featureclass2 {Feature Layer}:
          The destination feature class for the topology rule.
      subtype2 {String}:
          The subtype for the destination feature class. Enter the subtype's description
          (not the code). If subtypes do not exist on the origin feature class, or you
          want the rule to be applied to all subtypes in the feature class leave this
          blank."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddRuleToTopology_management(*gp_fixargs((in_topology, rule_type, in_featureclass, subtype, in_featureclass2, subtype2), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateTopology_management', None)
def CreateTopology(in_dataset=None, out_name=None, in_cluster_tolerance=None):
    """CreateTopology_management(in_dataset, out_name, {in_cluster_tolerance})

        Creates a topology. The topology will not contain any feature classes or
        rules.Use the Add Feature Class To Topology and the Add Rule To Topology tools
        to add
        feature classes and rules to the topology.

     INPUTS:
      in_dataset (Feature Dataset):
          The feature dataset in which the topology will be created.
      out_name (String):
          The name of the topology to be created. This name must be unique across the
          entire geodatabase.
      in_cluster_tolerance {Double}:
          The cluster tolerance to be set on the topology. The larger the value, the more
          likely vertices will be to cluster together."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateTopology_management(*gp_fixargs((in_dataset, out_name, in_cluster_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportTopologyErrors_management', None)
def ExportTopologyErrors(in_topology=None, out_path=None, out_basename=None):
    """ExportTopologyErrors_management(in_topology, out_path, out_basename)

        Exports the errors from a geodatabase topology to the target geodatabase. All
        information associated with the errors and exceptions, such as the features
        referenced by the error or exception, are exported. Once they are exported, the
        feature classes can be accessed using any license level of ArcGIS. The feature
        classes can be used with the Select by Location dialog box or the Select Layer
        By Location tool and can be shared with other users who do not have access to
        the topology itself.

     INPUTS:
      in_topology (Topology Layer):
          The topology from which the errors will be exported.
      out_path (Workspace / Feature Dataset):
          The output workspace to which the feature classes will be created. The default
          is the workspace where the topology is located.
      out_basename (String):
          Name to prepend to each output feature class. This allows you to specify unique
          output names when running multiple exports to the same workspace. The default is
          the topology name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportTopologyErrors_management(*gp_fixargs((in_topology, out_path, out_basename), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveFeatureClassFromTopology_management', None)
def RemoveFeatureClassFromTopology(in_topology=None, in_featureclass=None):
    """RemoveFeatureClassFromTopology_management(in_topology, in_featureclass)

        Removes a feature class from a topology.

     INPUTS:
      in_topology (Topology):
          The topology from which to remove the feature class.
      in_featureclass (String):
          The feature class to remove from the topology."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveFeatureClassFromTopology_management(*gp_fixargs((in_topology, in_featureclass), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveRuleFromTopology_management', None)
def RemoveRuleFromTopology(in_topology=None, in_rule=None):
    """RemoveRuleFromTopology_management(in_topology, in_rule)

        Removes a rule from a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology from which to remove a rule. This is the full path to the topology
          layer on disk, NOT the topology layer name in map.
      in_rule (String):
          The topology rule to remove from the topology."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveRuleFromTopology_management(*gp_fixargs((in_topology, in_rule), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SetClusterTolerance_management', None)
def SetClusterTolerance(in_topology=None, cluster_tolerance=None):
    """SetClusterTolerance_management(in_topology, cluster_tolerance)

        Sets the cluster tolerance of a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology for which you want to change the cluster tolerance. This is the
          full path to the topology, note the topology's name or the topology layer's name
          when in ArcMap.
      cluster_tolerance (Double):
          The value to be set as the cluster tolerance property of the selected topology.
          If you enter a value of zero, the default or minimum cluster tolerance will be
          applied to the topology."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SetClusterTolerance_management(*gp_fixargs((in_topology, cluster_tolerance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ValidateTopology_management', None)
def ValidateTopology(in_topology=None, visible_extent=None):
    """ValidateTopology_management(in_topology, {visible_extent})

        Validates a geodatabase topology.Validate Topology performs the following
        operations:

        * Cracking and clustering of feature vertices to find features that share
        geometry (have common coordinates)


        * Inserting common coordinate vertices into features that share geometry


        * Running a set of integrity checks to identify any violations of the rules that
        have been defined for the topology

     INPUTS:
      in_topology (Topology Layer):
          The geodatabase topology to be validated.
      visible_extent {Boolean}:
          In ArcMap, determines whether to use the current visible extent of the map or
          the full extent of the topology. If run in ArcCatalog or in a Python script, the
          entire extent of the topology will be validated regardless of this parameter
          setting.

          * Full_Extent—The entire extent of the topology will be validated. This is the
          default.

          * Visible_Extent—Only the current visible extent will be validated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ValidateTopology_management(*gp_fixargs((in_topology, visible_extent), True)))
        return retval
    except Exception, e:
        raise e


# Versions toolset
@gptooldoc('AddFieldConflictFilter_management', None)
def AddFieldConflictFilter(table=None, fields=None):
    """AddFieldConflictFilter_management(table, fields;fields...)

        Adds a field conflict filter for a given field in a geodatabase table or
        feature class. Field conflict filters can be applied to versioned tables or
        feature classes to
        prevent conflicts from being identified when the same attribute is updated in
        the parent and child versions. Field conflict filters only apply for reconciles
        in which conflicts are defined by attribute.

     INPUTS:
      table (Table View):
          Table or feature class containing the field or fields to be added as conflict
          filters.
      fields (Field):
          Field or list of fields to add as conflict filters."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AddFieldConflictFilter_management(*gp_fixargs((table, fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('AlterVersion_management', None)
def AlterVersion(in_workspace=None, in_version=None, name=None, description=None, access=None):
    """AlterVersion_management(in_workspace, in_version, {name}, {description}, {access})

        The Alter Version tool allows you to change the geodatabase version's name,
        description, and access permissions.

     INPUTS:
      in_workspace (Workspace):
          The database connection file to the enterprise, workgroup, or desktop
          geodatabase where the version to be altered is located. The default is to use
          the workspace defined in the Current Workspace environment.
      in_version (String):
          The name of the version to be altered.
      name {String}:
          If you are changing the version name, enter the new name for the version.
      description {String}:
          If you are changing the version description, enter the new description for the
          version.
      access {String}:
          Specify the access permission you want to set for the version. The following
          values are supported:

          * PRIVATE—Only the owner may view the version and modify available feature
          classes. This is the default.

          * PUBLIC— Any user may view the version and modify available feature classes.

          * PROTECTED—Any user may view the version, but only the owner may modify
          available feature classes."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AlterVersion_management(*gp_fixargs((in_workspace, in_version, name, description, access), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ChangeVersion_management', None)
def ChangeVersion(in_features=None, version_type=None, version_name=None, date=None):
    """ChangeVersion_management(in_features, version_type, {version_name}, {date})

        Each input feature layer or table view will have its workspace modified to
        connect to the requested version.

     INPUTS:
      in_features (Feature Layer / Table View):
          The feature layer or table view to connect to using the specified version.
      version_type (String):
          The type of version to change to.

          * TRANSACTIONAL—Connect to a defined state of the database.

          * HISTORICAL—Connect to a version representing a defined moment in time, often
          specified by a time or Historical Marker.
      version_name {String}:
          Name of the version to change to. Optional if using historical versions.
      date {Date}:
          Date of the historical version to change to."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ChangeVersion_management(*gp_fixargs((in_features, version_type, version_name, date), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateVersion_management', None)
def CreateVersion(in_workspace=None, parent_version=None, version_name=None, access_permission=None):
    """CreateVersion_management(in_workspace, parent_version, version_name, {access_permission})

        Creates a new version in the specified geodatabase.

     INPUTS:
      in_workspace (Workspace):
          The enterprise geodatabase that contains the parent version and will contain the
          new version.
      parent_version (String):
          The geodatabase, or version of a geodatabase, on which the new version will be
          based.
      version_name (String):
          The name of the version to be created.
      access_permission {String}:
          The permission access level for the version to protect it from being edited or
          viewed by users other than the owner.

          * PRIVATE—Only the owner or the geodatabase administrator may view the version
          and modify versioned data or the version itself.

          * PUBLIC—Any user may view the version. Any user who has been granted read/write
          (update, insert, and delete) permissions on datasets can modify datasets in the
          version.

          * PROTECTED—Any user may view the version, but only the owner or the geodatabase
          administrator may edit datasets in the version or the version itself."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateVersion_management(*gp_fixargs((in_workspace, parent_version, version_name, access_permission), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DeleteVersion_management', None)
def DeleteVersion(in_workspace=None, version_name=None):
    """DeleteVersion_management(in_workspace, version_name)

        The Delete Version tool deletes the specified version from the input enterprise,
        workgroup, or desktop geodatabase.

     INPUTS:
      in_workspace (Workspace):
          Provide the database connection file to the enterprise, workgroup, or desktop
          geodatabase containing the version to be deleted. The default is to use the
          workspace defined in the Current Workspace environment.
      version_name (String):
          Specify the name of the version to be deleted."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DeleteVersion_management(*gp_fixargs((in_workspace, version_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ReconcileVersions_management', None)
def ReconcileVersions(input_database=None, reconcile_mode=None, target_version=None, edit_versions=None, acquire_locks=None, abort_if_conflicts=None, conflict_definition=None, conflict_resolution=None, with_post=None, with_delete=None, out_log=None):
    """ReconcileVersions_management(input_database, reconcile_mode, {target_version}, {edit_versions;edit_versions...}, {acquire_locks}, {abort_if_conflicts}, {conflict_definition}, {conflict_resolution}, {with_post}, {with_delete}, {out_log})

        Reconciles a version or multiple versions against a target version.

     INPUTS:
      input_database (Workspace):
          The enterprise geodatabase that contains the versions to be reconciled. The
          default is to use the workspace defined in the environment.
      reconcile_mode (String):
          Determines which versions will be reconciled when the tool is executed.

          * ALL_VERSIONS—Reconciles edit versions with the target version. This is the
          default.

          * BLOCKING_VERSIONS—Reconciles versions that are blocking the target version
          from compressing. This option uses the recommended reconcile order.
      target_version {String}:
          Name of any version in the direct ancestry of the an edit version, such as the
          parent version or the default version. Typically contains edits from other
          versions that the user performing the
          reconcile would like to pull into their edit version.
      edit_versions {String}:
          Name of the edit version or versions to be reconciled with the selected target
          version. This can be an individual version name or a Python list of version
          names.
      acquire_locks {Boolean}:
          Determines whether feature locks will be acquired.

          * LOCK_ACQUIRED—Acquires locks during the reconcile process. This should be used
          when the intention is to post edits. It ensures that the target version is not
          modified in the time between the reconcile and post operations. This is the
          default.

          * NO_LOCK_ACQUIRED—No locks are acquired during the reconcile process. This
          allows multiple users to reconcile in parallel. It should be used when the edit
          version will not be posted to the target version because there is a possibility
          that the target version could be modified in the time between the reconcile and
          post operations.
      abort_if_conflicts {Boolean}:
          Determines if the reconcile process should be aborted if conflicts are found
          between the target version and the edit version.

          * NO_ABORT—Does not abort the reconcile if conflicts are found. This is the
          default.

          * ABORT_CONFLICTS—Aborts the reconcile if conflicts are found.
      conflict_definition {String}:
          Describes the conditions required for a conflict to occur:

          * BY_OBJECT—Any changes to the same row or feature in the parent and child
          versions will conflict during reconcile. This is the default.

          * BY_ATTRIBUTE—Only changes to the same attribute (column) of the same row or
          feature in the parent and child versions will be flagged as a conflict during
          reconcile. Changes to different attributes will not be considered a conflict
          during reconcile.
      conflict_resolution {String}:
          Describes the behavior if a conflict is detected:

          * FAVOR_TARGET_VERSION—For all conflicts, resolves in favor of the target
          version. This is the default.

          * FAVOR_EDIT_VERSION—For all conflicts, resolves in favor of the edit version.
      with_post {Boolean}:
          Posts the current edit session to the reconciled target version.

          * NO_POST—Current edit version will not be posted to the target version after
          the reconcile. This is the default.

          * POST—Current edit version will be posted to the target version after the
          reconcile.
      with_delete {Boolean}:
          * DELETE_VERSION—Current edit version that was reconciled will be deleted after
          being posted to the target version.

          * KEEP_VERSION—Current edit version that was reconciled will not be deleted.
          This is the default.

     OUTPUTS:
      out_log {File}:
          Specify a name and location to where the log file will be written. The log file
          is an ASCII file containing the contents of the geoprocessing messages."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReconcileVersions_management(*gp_fixargs((input_database, reconcile_mode, target_version, edit_versions, acquire_locks, abort_if_conflicts, conflict_definition, conflict_resolution, with_post, with_delete, out_log), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RegisterAsVersioned_management', None)
def RegisterAsVersioned(in_dataset=None, edit_to_base=None):
    """RegisterAsVersioned_management(in_dataset, {edit_to_base})

        Registers ArcSDE dataset as versioned.

     INPUTS:
      in_dataset (Table View / Feature Dataset):
          Name of the dataset to be registered as versioned.
      edit_to_base {Boolean}:
          Determines whether edits to the default version will be moved to the base
          tables.

          * NO_EDITS_TO_BASE—Dataset will not be versioned with the option to move edits
          to base. This is the default.

          * EDITS_TO_BASE—Dataset will be versioned with the option of moving edits to
          base."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RegisterAsVersioned_management(*gp_fixargs((in_dataset, edit_to_base), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RemoveFieldConflictFilter_management', None)
def RemoveFieldConflictFilter(table=None, fields=None):
    """RemoveFieldConflictFilter_management(table, fields;fields...)

        Removes a field conflict filter for a given field in a geodatabase table or
        feature class. Field conflict filters can be applied to versioned tables or
        feature classes to
        prevent conflicts from being identified when the same attribute is updated in
        the parent and child versions. Field conflict filters only apply for reconciles
        in which conflicts are defined by attribute.

     INPUTS:
      table (Table View):
          Table or feature class containing the field or fields to be removed as conflict
          filters.
      fields (Field):
          Field or list of fields to be removed as conflict filters."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RemoveFieldConflictFilter_management(*gp_fixargs((table, fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UnregisterAsVersioned_management', None)
def UnregisterAsVersioned(in_dataset=None, keep_edit=None, compress_default=None):
    """UnregisterAsVersioned_management(in_dataset, {keep_edit}, {compress_default})

        Unregisters an ArcSDE dataset as versioned.

     INPUTS:
      in_dataset (Table View / Feature Dataset):
          Name of the ArcSDE dataset to be unregistered as versioned.
      keep_edit {Boolean}:
          Specifies whether edits made of the version should be maintained.

          * KEEP_EDIT—If there are existing edits in the delta tables the tool will fail
          with an error message. Do not use this option if you intend to compress your
          edits from the Default version in the compress_default parameter. This is the
          default.

          * NO_KEEP_EDIT—If there are existing edits in the delta tables the tool will
          allow deletion of these edits.
      compress_default {Boolean}:
          Determines whether edits will be compressed and unused data will be removed.
          This option is ignored if the KEEP_EDIT keyword is used when specifying the
          keep_edit parameter.

          * COMPRESS_DEFAULT—Edits in the Default version are compressed to the base
          table. This is the default.

          * NO_COMPRESS_DEFAULT—Any edits remaining in the delta tables are not
          compressed."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UnregisterAsVersioned_management(*gp_fixargs((in_dataset, keep_edit, compress_default), True)))
        return retval
    except Exception, e:
        raise e


# Workspace toolset
@gptooldoc('ClearWorkspaceCache_management', None)
def ClearWorkspaceCache(in_data=None):
    """ClearWorkspaceCache_management({in_data})

        Clears any enterprise geodatabase workspaces from the enterprise geodatabase
        workspace cache.

     INPUTS:
      in_data {Data Element / Layer}:
          The enterprise geodatabase database connection file representing the enterprise
          geodatabase workspace to be removed from the cache. Specify the path to the
          enterprise geodatabase connection file that was used in running your
          geoprocessing tools in order to remove the specific enterprise geodatabase
          workspace from the cache. Passing no input parameter will clear all enterprise
          geodatabase workspaces from the cache."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ClearWorkspaceCache_management(*gp_fixargs((in_data,), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateArcInfoWorkspace_management', None)
def CreateArcInfoWorkspace(out_folder_path=None, out_name=None):
    """CreateArcInfoWorkspace_management(out_folder_path, out_name)

        Creates a workspace with an INFO subdirectory.

     INPUTS:
      out_folder_path (Folder):
          Location where the ArcInfo workspace will be created.
      out_name (String):
          Name of the ArcInfo workspace to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateArcInfoWorkspace_management(*gp_fixargs((out_folder_path, out_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateArcSDEConnectionFile_management', None)
def CreateArcSDEConnectionFile(out_folder_path=None, out_name=None, server=None, service=None, database=None, account_authentication=None, username=None, password=None, save_username_password=None, version=None, save_version_info=None):
    """CreateArcSDEConnectionFile_management(out_folder_path, out_name, server, service, {database}, {account_authentication}, {username}, {password}, {save_username_password}, {version}, {save_version_info})

        Creates a database connection file to connect to an enterprise geodatabase
        using an ArcSDE service.

     INPUTS:
      out_folder_path (Folder):
          The folder path where the .sde file will be stored.
      out_name (String):
          The name of the connection file. Use the .sde file extension.
      server (String):
          The name of the machine where the ArcSDE application server is installed.
      service (String):
          The ArcSDE service name or TCP port number.
      database {String}:
          The name of the database to connect to. Do not provide a database name when
          connecting to Oracle.
      account_authentication {Boolean}:
          * DATABASE_AUTH—Database Authentication. Uses an internal database user name and
          password to connect to the DBMS. You aren't required to type your user name and
          password to create a connection; however, if you don't, you will be prompted to
          enter them when a connection is established.

          * OPERATING_SYSTEM_AUTH—Use Operating system authentication. You do not need to
          type a user name and password. The connection will be made with the credentials
          used to log in to the operating system. If the login used for the operating
          system is not a valid geodatabase login, the connection will fail. Also note you
          cannot make an ArcSDE service connection using operating system authentication
          to a geodatabase stored in Oracle, DB2, or Informix.
      username {String}:
          Database user name to connect with when using Database Authentication.
      password {Encrypted String}:
          The database user password when using Database Authentication.
      save_username_password {Boolean}:
          * SAVE_USERNAME—Save the user name and password in the connection file.

          * DO_NOT_SAVE_USERNAME—Do not save the user name and password in the file. Every
          time you connect using the file, you will be prompted for a user name and
          password.
      version {String}:
          The geodatabase version to connect to. By default, connections are made to the
          DEFAULT version.
      save_version_info {Boolean}:
          * SAVE_VERSION—Save the version name in the connection file.

          * DO_NOT_SAVE_VERSION—Do not save the version name in the connection file.
          Without the version name being saved with the file, a connection to the DEFAULT
          version will be made the next time you access the connection file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateArcSDEConnectionFile_management(*gp_fixargs((out_folder_path, out_name, server, service, database, account_authentication, username, password, save_username_password, version, save_version_info), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateDatabaseConnection_management', None)
def CreateDatabaseConnection(out_folder_path=None, out_name=None, database_platform=None, instance=None, account_authentication=None, username=None, password=None, save_user_pass=None, database=None, schema=None, version_type=None, version=None, date=None):
    """CreateDatabaseConnection_management(out_folder_path, out_name, database_platform, instance, {account_authentication}, {username}, {password}, {save_user_pass}, {database}, {schema}, {version_type}, {version}, {date})

        Creates a connection file that can be used to connect to a database or an
        enterprise, workgroup, or desktop geodatabase.

     INPUTS:
      out_folder_path (Folder):
          The folder path where the database connection file (.sde file) will be stored.
      out_name (String):
          The name of the database connection file. The output file will have the
          extension .sde.
      database_platform (String):
          The database management system platform to which you will be connecting. The
          following are valid options:

          * SQL_SERVER—For connecting to Microsoft SQL Server

          * ORACLE—For connecting to Oracle

          * DB2—For connecting to IBM DB2 on Linux, UNIX, or Windows

          * DB2ZOS—For connecting to IBM DB2 on z/OS

          * INFORMIX—For connecting to IBM Informix

          * NETEZZA—For connecting to IBM Netezza

          * POSTGRESQL—For connecting to PostgreSQL

          * TERADATA—For connecting to Teradata

          * SAP_HANA—For connecting to SAP HANA

          * ALTIBASE—For connecting to ALTIBASE
      instance (String):
          The database server or instance to which you will connect.The value you specify
          for the database_platform parameter indicates the type of
          database to which you want to connect. The information you provide for the
          instance parameter will vary, depending the database platform you specified. See
          below for further information on what to provide for each database
          platform.

          * ALTIBASE—The ODBC data source name for the ALTIBASE database

          * DB2—The name of the cataloged DB2 database

          * DB2 for Z/OS—The name of the cataloged DB2 database

          * Informix—The Open Database Connectivity (ODBC) data source name for the
          Informix database

          * Oracle—Either the TNS name or the Oracle Easy Connection string to connect to
          the Oracle database

          * Netezza—The ODBC data source name for the Netezza database

          * PostgreSQL—The name of the server where PostgreSQL is installed

          * SAP HANA—The ODBC data source name for the SAP HANA database

          * SQL Server—The name of the SQL Server instance

          * Teradata—The ODBC data source name for the Teradata database
      account_authentication {Boolean}:
          * DATABASE_AUTH—Database Authentication. Uses an internal database user name and
          password to connect to the database. You aren't required to type your user name
          and password to create a connection; however, if you don't, you will be prompted
          to enter them when a connection is established.  If the connection file you are
          creating will provide ArcGIS services with access
          to the database or geodatabase, or if you want to use the Catalog search to
          locate data accessed through this connection file, you must type a user name and
          password.

          * OPERATING_SYSTEM_AUTH—Use operating system authentication. You do not need to
          type in a user name and password. The connection will be made with the user name
          and password used to log in to the operating system. If the login used for the
          operating system is not a valid geodatabase login, the connection will fail.
          Also note, if you are creating a connection to a geodatabase stored in Oracle,
          DB2, or Informix, you must use a direct connection to the database.
      username {String}:
          The database user name to connect with using Database Authentication.
      password {Encrypted String}:
          The database user password when using Database Authentication.
      save_user_pass {Boolean}:
          * SAVE_USERNAME—Save the user name and password in the connection file. This is
          the default. If the connection file you are creating will provide ArcGIS
          services with access to the database or geodatabase, or if you want to use the
          Catalog search to locate data accessed through this connection file, you must
          type a user name and password.

          * DO_NOT_SAVE_USERNAME—Do not save the user name and password in the file. Every
          time you attempt to connect using the file, you will be prompted for the user
          name and password.
      database {String}:
          The name of the database to which you will be connecting. This parameter only
          applies to PostgreSQL and SQL Server platforms.
      schema {String}:
          The user schema geodatabase to which you want to connect. This option only
          applies to Oracle databases that contain at least one user-schema geodatabase.
          The default value for this parameter is to use the SDE schema (master)
          geodatabase.
      version_type {String}:
          The type of version to which you want to connect.

          * TRANSACTIONAL—Use to connect to a transactional version.

          * HISTORICAL—Use to connect to an historical marker.

          * POINT_IN_TIME—Use to connect to a specific point in time. If POINT_IN_TIME is
          used, the Version Name parameter will be ignored.
           If TRANSACTIONAL or HISTORICAL is used, the date parameter will be ignored. If
          HISTORICAL is used and a name is not provided in the version_name parameter, the
          Default transactional version will be used. If POINT_IN_TIME is used and a date
          is not provided in the date parameter, the Default transactional version will be
          used.
      version {String}:
          The geodatabase transactional version or historical marker to connect to. The
          default option uses the Default transactional version.
      date {Date}:
          The value representing the date and time used to connect to the database. For
          working with archiving enabled data.Dates can be entered in the following
          formats:

          *  6/9/2011 4:20:15 PM

          *  6/9/2011 16:20:15

          *  6/9/2011

          *  4:20:15 PM

          * 16:20:15

          * If a time is entered without a date, the default date of December 30, 1899,
          will be used.

          * If a date is entered without a time, the default time of 12:00:00 AM will be
          used."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateDatabaseConnection_management(*gp_fixargs((out_folder_path, out_name, database_platform, instance, account_authentication, username, password, save_user_pass, database, schema, version_type, version, date), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateFeatureDataset_management', None)
def CreateFeatureDataset(out_dataset_path=None, out_name=None, spatial_reference=None):
    """CreateFeatureDataset_management(out_dataset_path, out_name, {spatial_reference})

        Creates a feature dataset in the output location—an existing enterprise, file,
        or personal geodatabase.

     INPUTS:
      out_dataset_path (Workspace):
          The enterprise, file geodatabase, or personal geodatabase in which the output
          feature dataset will be created.
      out_name (String):
          The name of the feature dataset to be created.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature dataset. You can specify the spatial
          reference in several ways:

          *  By entering the path to a .prj file, such as C:/workspace/watershed.prj.

          *  By referencing a feature class or feature dataset whose spatial reference you
          want to apply, such as C:/workspace/myproject.gdb/landuse/grassland.

          *  By defining a spatial reference object prior to using this tool, such as sr =
          arcpy.SpatialReference("C:/data/Africa/Carthage.prj"), which you then use as the
          spatial reference parameter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateFeatureDataset_management(*gp_fixargs((out_dataset_path, out_name, spatial_reference), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateFileGDB_management', None)
def CreateFileGDB(out_folder_path=None, out_name=None, out_version=None):
    """CreateFileGDB_management(out_folder_path, out_name, {out_version})

        Creates a file geodatabase in a folder.

     INPUTS:
      out_folder_path (Folder):
          The location (folder) where the file geodatabase will be created.
      out_name (String):
          The name of the file geodatabase to be created.
      out_version {String}:
          The ArcGIS version for the geodatabase to be created.

          * CURRENT—Creates a geodatabase compatible with the currently installed version
          of ArcGIS

          * 10.0  —Creates a geodatabase compatible with ArcGIS version 10

          * 9.3—Creates a geodatabase compatible with ArcGIS version 9.3

          * 9.2—Creates a geodatabase compatible with ArcGIS version 9.2"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateFileGDB_management(*gp_fixargs((out_folder_path, out_name, out_version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateFolder_management', None)
def CreateFolder(out_folder_path=None, out_name=None):
    """CreateFolder_management(out_folder_path, out_name)

        Creates a folder in the specified location.

     INPUTS:
      out_folder_path (Folder):
          The disk location where the folder is created.
      out_name (String):
          The folder to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateFolder_management(*gp_fixargs((out_folder_path, out_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreatePersonalGDB_management', None)
def CreatePersonalGDB(out_folder_path=None, out_name=None, out_version=None):
    """CreatePersonalGDB_management(out_folder_path, out_name, {out_version})

        Creates a personal geodatabase in a folder.

     INPUTS:
      out_folder_path (Folder):
          Location (folder) where the personal geodatabase will be created.
      out_name (String):
          Name of the geodatabase to be created.
      out_version {String}:
          The ArcGIS version for the geodatabase to be created.

          * CURRENT—Creates a geodatabase compatible with the currently installed version
          of ArcGIS

          * 10.0—Creates a geodatabase compatible with ArcGIS version 10

          * 9.3—Creates a geodatabase compatible with ArcGIS version 9.3

          * 9.2—Creates a geodatabase compatible with ArcGIS version 9.2

          * 9.1—Creates a geodatabase compatible with ArcGIS version 9.1"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreatePersonalGDB_management(*gp_fixargs((out_folder_path, out_name, out_version), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateSpatialType_management', None)
def CreateSpatialType(input_database=None, sde_user_password=None, tablespace_name=None, st_shape_library_path=None):
    """CreateSpatialType_management(input_database, sde_user_password, {tablespace_name}, {st_shape_library_path})

        The Create Spatial Type tool adds or upgrades the ST_Geometry SQL type,
        subtypes, and functions to an Oracle or PostgreSQL database. This allows you to
        use the ST_Geometry SQL type to store geometries in a database that does not
        contain a geodatabase. This tool also can be used to upgrade an existing
        ST_Geometry installation in an Oracle or PostgreSQL database.

     INPUTS:
      input_database (Workspace):
          The input_database is the database connection file (.sde) that connects to the
          Oracle or PostgreSQL database. You must connect as a database administrator
          user; in Oracle, you must connect as the sys user.
      sde_user_password (Encrypted String):
          The password for the sde database user. If the sde user does not exist in the
          database, it will be created and will use the password provided. The password
          policy of the underlying database will be enforced. If the sde user already
          exists in the database or database cluster, this password must match the
          existing password.
      tablespace_name {String}:
          For Oracle, you can provide the name for a tablespace to be set as the default
          tablespace for the sde user. If the tablespace does not already exist, it will
          be created in the Oracle default storage location. If a tablespace with the
          specified name already exists, it will be set as the sde user's default.
      st_shape_library_path {File}:
          For Oracle, provide the location on the Oracle server where you placed the
          st_shape library."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateSpatialType_management(*gp_fixargs((input_database, sde_user_password, tablespace_name, st_shape_library_path), True)))
        return retval
    except Exception, e:
        raise e



@gptooldoc('CreateVersionedView_management', None)
def CreateVersionedView(in_dataset=None, in_name=None):
    """CreateVersionedView_management(in_dataset, {in_name})

        Creates a versioned view on a table or feature class.

        As of the 10.2 release, this tool has been deprecated.

     INPUTS:
      in_dataset (Table View):
          Input table or feature class for which a versioned view will be created.
      in_name {String}:
          Name for the versioned view that is created. If nothing is specified the output
          versioned view name is the name of the table or feature class with _vw appended
          to the end."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateVersionedView_management(*gp_fixargs((in_dataset, in_name), True)))
        return retval
    except Exception as e:
        raise e


@gptooldoc('ReconcileVersion_management', None)
def ReconcileVersion(in_workspace=None, version_name=None, target_name=None, conflict_definition=None, conflict_resolution=None, aquired_locks=None, abort_if_conflicts=None, post=None):
    """ReconcileVersion_management(in_workspace, version_name, target_name, {conflict_definition}, {conflict_resolution}, {aquired_locks}, {abort_if_conflicts}, {post})

        Reconciles a version against another version in its lineage.

        This tool has been deprecated. Use the Reconcile Versions tool instead.

     INPUTS:
      in_workspace (Workspace):
          The ArcSDE geodatabase containing the reconcilable version. The default is to
          use the workspace defined in the environment.
      version_name (String):
          Name of the Edit Version to be reconciled with the Target Version.
      target_name (String):
          Name of any version in the direct ancestry of the Edit version, such as the
          parent version or the default version.
      conflict_definition {String}:
          Describes the conditions required for a conflict to occur:

          * BY_OBJECTâ€”Any changes to the same row or feature in the parent and child
          versions will conflict during reconcile. This is the default.

          * BY_ATTRIBUTEâ€”Only changes to the same attribute of the same row or feature in
          the parent and child versions will be flagged as a conflict during reconcile.
          Changes to different attributes will not be considered a conflict during
          reconcile.
      conflict_resolution {String}:
          Describes the behavior if a conflict is detected:

          * FAVOR_TARGET_VERSIONâ€”For all conflicts, resolves in favor of the target
          version. This is the default.

          * FAVOR_EDIT_VERSIONâ€”For all conflicts, resolves in favor of the edit version.
      aquired_locks {Boolean}:
          Determines whether feature locks will be acquired.

          * LOCK_ACQUIREDâ€”Acquires locks when there is no intention of posting the edit
          session. This is the default.

          * NO_LOCK_ACQUIREDâ€”No locks are acquired and the edit session will be posted to
          the target version.
      abort_if_conflicts {Boolean}:
          Determines if the reconcile process should be aborted if conflicts are found
          between the target version and the edit version.

          * NO_ABORTâ€”Does not abort the reconcile if conflicts are found. This is the
          default.

          * ABORT_CONFLICTSâ€”Aborts the reconcile if conflicts are found.
      post {Boolean}:
          Posts the current edit session to the reconciled target version.

          * NO_POSTâ€”Current edits will not be posted to the target version after the
          reconcile. This is the default.

          * POSTâ€”Current edits will be posted to the target version after the reconcile."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ReconcileVersion_management(*gp_fixargs((in_workspace, version_name, target_name, conflict_definition, conflict_resolution, aquired_locks, abort_if_conflicts, post), True)))
        return retval
    except Exception as e:
        raise e

# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject