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
"""The Schematics toolbox contains tools that perform the most fundamental
schematic operations. With the tools in this toolbox, you can create, update,
and export diagrams or create schematic folders."""
__all__ = ['CreateDiagram', 'UpdateDiagram', 'UpdateDiagrams', 'CreateSchematicFolder', 'ConvertDiagram']
__alias__ = u'schematics'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('ConvertDiagram_schematics', None)
def ConvertDiagram(in_diagram=None, out_location=None, reuse_fc=None, export_related_attributes=None, container_geometry=None, config_keyword=None):
    """ConvertDiagram_schematics(in_diagram, out_location, {reuse_fc}, {export_related_attributes}, {container_geometry}, {config_keyword})

        Converts a schematic diagram to standard feature classes or shapefiles.
        Schematic diagrams are all stored in hidden feature classes that are specific
        to Schematics and need the rest of the schematic configuration tables and
        information to be useful. This tool allows you to share diagrams with other
        people without having to provide the entire schematic dataset, which includes
        all the diagrams and the configuration. If you plan to convert multiple
        diagrams, you can choose whether they will all be placed into the same set of
        standard feature classes or shapefiles or if each diagram will get its own set
        of feature classes or shapefiles.See the Code Sample section for a script tool
        sample that allows you to convert
        all diagrams contained in a schematic dataset or in a schematic folder.

     INPUTS:
      in_diagram (Schematic Layer):
          The schematic diagram layer to be converted.
      out_location (Workspace / Feature Dataset):
          Workspace or feature dataset in which the schematic diagram will be converted.
          This container must already exist.
      reuse_fc {Boolean}:
          Indicates whether the input schematic diagram layer will be converted in the
          same standard feature classes/shapefiles as the other diagrams based on the same
          diagram template.

          * REUSE_FC—Must be used to convert the specified diagram into the same standard
          feature classes/shapefiles as the other diagrams—based on the same diagram
          template—have already been or will be converted. In this case, depending on the
          chosen output location, the specified diagram is converted:

          * Into a feature dataset whose name corresponds to the diagram template name and
          each feature class name corresponding to the schematic feature class names.

          * Into a folder whose name corresponds to the diagram template name and each
          shapefile name corresponding to the schematic feature class names.
           This is the default.

          * NO_REUSE_FC—Converts the input diagram into a new feature dataset/folder whose
          name is the concatenation of the input diagram's diagram template name and the
          diagram name—each feature class/shapefile name being the concatenation of the
          schematic feature class name and diagram name.
      export_related_attributes {Boolean}:
          Indicates whether all the attributes stored in the real feature classes/object
          tables associated with the schematic feature classes will also be converted.

          * NO_RELATED_ATTRIBUTES—Each schematic feature contained in the input diagram is
          converted with only the attributes contained in its schematic feature class.
          This is the default.

          * EXPORT_RELATED_ATTRIBUTES—Each schematic feature contained in the input
          diagram is converted with the attributes contained in its schematic feature
          class and all the attributes related to its associated real feature.
          If no associated feature class/table is specified for a schematic feature class,
          no feature attributes can be converted.When using REUSE_FC and
          EXPORT_RELATED_ATTRIBUTES, the structure must already
          exist with the associated feature fields, so the related attributes are
          converted.
      container_geometry {String}:
          Indicates the geometry type of the features that will be created for the
          converted schematic containers contained in the input diagram.

          * POLYGON—Each container in the input diagram is converted as a polygon feature.
          This is the default.

          * POLYLINE—Each container in the input diagram is converted as a polyline
          feature.

          * POINT—Each container in the input diagram is converted as a point feature.
          When using the Reuse Existing Structure option and the structure already exists
          with POLYGON (POLYLINE or POINT) feature classes created for container schematic
          features, there is no way to change the feature class type to POLYLINE or POINT
          (POLYGON) for the next conversions.
      config_keyword {String}:
          The configuration keyword that determines the storage parameters of the table in
          a relational database management system (RDBMS). This is for enterprise,
          workgroup, or desktop geodatabase only."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConvertDiagram_schematics(*gp_fixargs((in_diagram, out_location, reuse_fc, export_related_attributes, container_geometry, config_keyword), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateDiagram_schematics', None)
def CreateDiagram(out_location=None, out_name=None, diagram_type=None, in_data=None, builder_options=None):
    """CreateDiagram_schematics(out_location, out_name, diagram_type, {in_data;in_data...}, {builder_options})

        Creates a schematic diagram.Depending on the schematic builder, diagram creation
        can be based on feature
        layers, feature classes, object tables, a network analysis layer, or XML data.

     INPUTS:
      out_location (Schematic Folder / Schematic Dataset):
          Schematic dataset or schematic folder in which the diagram will be created.
          This container must already exist.
      out_name (String):
          Name of the schematic diagram to be created.
      diagram_type (String):
          Schematic diagram template of the schematic diagram to be created.
      in_data {Table View / Data Element / Layer}:
          The input data to generate the diagram.The Input Data parameter specifies the
          elements on which the diagram generation
          will be based. It must be specified for most of the predefined schematic
          builders:

          * For diagram templates that work with the Standard builder configured to
          operate from a geometric network or network dataset, the Input Data parameter
          must at least reference a feature layer, feature class, or object table.

          * For diagram templates that work with the Network Dataset builder, the Input
          Data parameter must reference a unique network analysis layer. If the related
          network analysis is not performed, Schematics tries to perform it before using
          the solved analysis layer as input.

          * For diagram templates related to the XML builder, the Input Data parameter is
          optional when the data for the diagram generation is provided by an external
          component. But when no external component is defined for the builder properties,
          the Input Data must reference an XML file. In both cases, the input XML data
          must be built according to the XMLBuilderDiagram XML Schema file.

          * For diagram templates that work with the Standard builder configured to
          operate from custom queries, no input data is required.
          For diagram templates that work with the Standard builder when it is configured
          to operate from a geometric network or network dataset, XML builder, and Network
          Dataset builder, if no input data is specified, the diagram cannot be generated.
      builder_options {String}:
          The schematic builder creation parameters. These parameters are required only
          for diagrams based on the Network Dataset builder to specify whether nodes will
          be merged.

          * MERGE_NODES—Specifies the network element junctions, which are taken several
          times along the resultant route of a route analysis to be represented by a
          single schematic feature node in the generated schematic diagram. It also allows
          you to merge midspanjunction elements when they are at the same position in a
          service area analysis.

          * NO_MERGE_NODES—Specifies that no schematic feature node will be merged
          (default)."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateDiagram_schematics(*gp_fixargs((out_location, out_name, diagram_type, in_data, builder_options), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CreateSchematicFolder_schematics', None)
def CreateSchematicFolder(out_location=None, out_name=None):
    """CreateSchematicFolder_schematics(out_location, out_name)

        Creates a schematic folder in a schematic dataset or schematic folder.

     INPUTS:
      out_location (Schematic Folder / Schematic Dataset):
          The schematic dataset or schematic folder in which the folder will be created.
          This container must already exist.
      out_name (String):
          Name of the output schematic folder."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateSchematicFolder_schematics(*gp_fixargs((out_location, out_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateDiagram_schematics', None)
def UpdateDiagram(in_diagram=None, in_data=None, builder_options=None):
    """UpdateDiagram_schematics(in_diagram, {in_data;in_data...}, {builder_options})

        Updates a schematic diagram.Depending on the schematic builder, the diagram
        update can be based on feature
        layers, feature classes, object tables, a solved network analysis, or an XML
        file.

     INPUTS:
      in_diagram (Schematic Layer):
          The schematic diagram layer to be updated.
      in_data {Table View / Data Element / Layer}:
          The input data on which the diagram update will be based.The Input Data
          parameter is not required for all predefined builders; it's an
          optional parameter:

          * For diagram templates that work with the Standard builder configured to
          operate from custom queries, no input tables must be set.

          * For diagram templates that work with the XML builder, the Input Data parameter
          must reference an XML file.

          * For diagram templates that work with the Network Dataset builder, the input
          data must be specified. It must reference a unique network analysis layer. If
          the related network analysis is not performed, Schematics tries to perform it
          before using the solved analysis layer as input.

          * For diagram templates that work with the Standard builder configured to
          operate from a geometric network or a network dataset, when the Input Data
          parameter is not specified, the Update Diagram tool works from the initial set
          of network features/objects used to generate the diagram or from the updated
          geometric network trace result based on the trace parameters that persisted in
          the schematic database if the diagram was generated from a highlighted trace.
          When the Input Data parameter is specified, it must reference at least a feature
          layer, feature class, or object table so the update operates on this data
          according to the Builder Options value.
      builder_options {String}:
          The schematic builder update options. Update options are optional. They depend
          on the builder related to the diagram template that implements the specified
          schematic diagram:

          * Diagrams generated from custom queries (Standard builder): KEEP_MANUAL_MODIF,
          NO_KEEP_MANUAL_MODIF, or REFRESH.

          * Diagrams generated from XML data (XML builder): KEEP_MANUAL_MODIF or
          NO_KEEP_MANUAL_MODIF.

          * Diagrams generated from solver results on network datasets (Network Dataset
          builder): NO_MERGE_NODES;KEEP_MANUAL_MODIF, NO_MERGE_NODES;NO_KEEP_MANUAL_MODIF,
          MERGE_NODES;KEEP_MANUAL_MODIF or MERGE_NODES;NO_KEEP_MANUAL_MODIF.

          * Diagrams generated from features organized into a geometric network or a
          network dataset (Standard builder):

          * When the Input Data parameter is not specified—KEEP_MANUAL_MODIF,
          NO_KEEP_MANUAL_MODIF, or REFRESH

          * When the Input Data parameter is specified—REBUILD;KEEP_MANUAL_MODIF,
          REBUILD;NO_KEEP_MANUAL_MODIF, APPEND;KEEP_MANUAL_MODIF,
          APPEND;NO_KEEP_MANUAL_MODIF, APPEND_QUICK;KEEP_MANUAL_MODIF or
          APPEND_QUICK;NO_KEEP_MANUAL_MODIF


          * KEEP_MANUAL_MODIF—Default option for diagram based on the XML builder or on
          the Standard builder when no input data is set. Use it to synchronize the input
          diagram content either against the original selection/trace/query used to
          initially generate this diagram—Standard diagram—or from an updated version of
          the XML input data initially used to generate it—XML diagram—whereas the
          schematic features that may have been manually removed/reduced/reconnected are
          kept in the updated diagram.

          * NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the XML builder or
          on the Standard builder when no input data is set. Use it to synchronize the
          input diagram content either against the original selection/trace/query used to
          initially generate this diagram—Standard diagram—or from an updated version of
          the XML input data initially used to generate it—XML diagram—whereas the
          schematic features that may have been manually removed/reduced/reconnected are
          restored in the updated diagram.

          * REFRESH—Option available for diagrams based on the Standard builder when no
          input data is set. Use it to simply refresh the attributes for all schematic
          features in the input diagram to the current state of the related network
          features in the geometric network or network dataset feature classes.

          * REBUILD;KEEP_MANUAL_MODIF—Default option available for diagrams based on the
          Standard builder when input data is set. Use this option if you want the input
          diagram to be completely rebuilt according to the specified input feature
          layers, feature classes, or object tables, whereas the schematic features that
          may have been manually removed/reduced/reconnected are kept in the updated
          diagram.

          * REBUILD;NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Standard builder when input data is set. Use this option if you want the input
          diagram to be completely rebuilt according to the specified input feature
          layers, feature classes, or object tables, whereas the schematic features that
          may have been manually removed/reduced/reconnected are restored in the updated
          diagram.

          * APPEND;KEEP_MANUAL_MODIF—Option available for diagrams based on the Standard
          builder when input data is set. Use this option if you want to append schematic
          features associated with the specified input feature layers, feature classes, or
          object tables with a full synchronization of the input diagram content, whereas
          the schematic features that may have been manually removed/reduced/reconnected
          are kept in the updated diagram.

          * APPEND;NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Standard builder when input data is set. Use this option if you want to append
          schematic features associated with the specified input feature layers, feature
          classes, or object tables with a full synchronization of the input diagram
          content, whereas the schematic features that may have been manually
          removed/reduced/reconnected are restored in the updated diagram.

          * APPEND_QUICK;KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Standard builder when input data is set. Use this option if you want to append
          schematic features associated with the specified input feature layers, feature
          classes, or object tables with a partial synchronization of the input diagram
          content, whereas the schematic features that may have been manually
          removed/reduced/reconnected are kept in the updated diagram.

          * APPEND_QUICK;NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Standard builder when input data is set. Use this option if you want to append
          schematic features associated with the specified input feature layers, feature
          classes, or object tables with a partial synchronization of the input diagram
          content, whereas the schematic features that may have been manually
          removed/reduced/reconnected are restored in the updated diagram.

          * NO_MERGE_NODES;KEEP_MANUAL_MODIF—Default option for diagrams based on the
          Network Dataset builder. Use this option to update the input diagram from the
          specified solved network analysis layer without merging nodes that occur several
          times in this layer, whereas the schematic features that may have been manually
          removed/reduced/reconnected are kept in the updated diagram.

          * NO_MERGE_NODES;NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Network Dataset builder. Use this option to update the input diagram from the
          specified solved network analysis layer without merging nodes that occur several
          times in this layer, whereas the schematic features that may have been manually
          removed/reduced/reconnected are restored in the updated diagram.

          * MERGE_NODES;KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Network Dataset builder. Use it to update the input diagram from the specified
          solved network analysis layer and merge nodes that occur several times in this
          layer, whereas the schematic features that may have been manually
          removed/reduced/reconnected are kept in the updated diagram.

          * MERGE_NODES;NO_KEEP_MANUAL_MODIF—Option available for diagrams based on the
          Network Dataset builder. Use it to update the input diagram from the specified
          solved network analysis layer and merge nodes that occur several times in this
          layer, whereas the schematic features that may have been manually
          removed/reduced/reconnected are restored in the updated diagram."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateDiagram_schematics(*gp_fixargs((in_diagram, in_data, builder_options), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('UpdateDiagrams_schematics', None)
def UpdateDiagrams(in_container=None, builder_options=None, recursive=None, diagram_type=None, last_update_criteria=None):
    """UpdateDiagrams_schematics(in_container, {builder_options}, {recursive}, {diagram_type}, {last_update_criteria})

        Updates schematic diagrams stored in a schematic dataset or schematic folder.All
        diagrams or a subset of diagrams (for example, diagrams related to a
        specific diagram template or diagrams that have not been updated for a
        particular number of days) can be updated.Only diagrams based on the Standard
        builder—that is, diagrams built from
        features organized into a geometric network or network dataset and schematic
        diagrams built from custom queries—can be updated using this geoprocessing tool.
        Diagrams based on the Network Dataset builder and XML builder that require
        specific input data cannot be updated using this tool.If a diagram based on the
        XML or Network Dataset builder is detected during the
        execution, an error is displayed, and the process is stopped.

     INPUTS:
      in_container (Schematic Folder / Schematic Dataset):
          The schematic dataset or schematic folder in which the diagrams are stored. This
          container must already exist.
      builder_options {String}:
          The schematic builder update options. They are optional.

          * KEEP_MANUAL_MODIF—Default option. Use it if you want the schematic features
          that have been removed/reduced from the diagram not to reappear and the edited
          connections to be kept in the updated diagram. This is the default.

          * NO_KEEP_MANUAL_MODIF—Use it if you want the removed/reduced schematic features
          and reconnected schematic feature links to be restored after the update.

          * REFRESH—Use it to simply refresh the attributes for all schematic features in
          the input diagram to the current state of the related network features in the
          geometric network or network dataset feature classes.

          *  RESYNC_FROM_GUID—Use this particular option if you want to resynchronize the
          schematic related network feature/object information based on GUIDs. This option
          must be used to avoid errors or data corruption when diagrams are updated while
          user data has been dropped and reloaded since their generations. Note that when
          using this option, the process works on the GUIDs to try to reattach the
          schematic features in the diagrams to their expected related network
          features/objects, but the diagram contents are not updated when the process
          ends. Once the reattachment is done, the real update can be launched.
      recursive {Boolean}:
          * RECURSIVE—Search recursively in subfolders.

          * NO_RECURSIVE—Do not search recursively in subfolders.
      diagram_type {String}:
          The diagram template of the schematic diagram to update.
      last_update_criteria {Long}:
          The number of days between diagram updates. The default is zero (0), meaning all
          diagrams will be updated daily."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.UpdateDiagrams_schematics(*gp_fixargs((in_container, builder_options, recursive, diagram_type, last_update_criteria), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject