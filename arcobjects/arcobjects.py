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
from ._base import _BaseArcObject, passthrough_attr
from .arcobjectconversion import convertArcObjectToPythonObject
import mixins

'This is an automatically generated file. Do not edit directly.'

class ArcSDESQLExecute(mixins.ArcSDESQLExecuteMixin,_BaseArcObject):
    """The ArcSDESQLExecute class provides a means of executing SQL statements via
       an enterprise geodatabase connection."""
    transactionAutoCommit = passthrough_attr('transactionAutoCommit')
    def execute(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Execute(*gp_fixargs(args)))
    
    def startTransaction(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.StartTransaction(*gp_fixargs(args)))
    
    def rollbackTransaction(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RollbackTransaction(*gp_fixargs(args)))
    
    def commitTransaction(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CommitTransaction(*gp_fixargs(args)))
    

class Array(mixins.ArrayMixin,_BaseArcObject):
    """The array object can contain points and arrays and is used to construct
       geometry objects."""
    count = passthrough_attr('count')
    def add(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Add(*gp_fixargs(args)))
    
    def getObject(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetObject(*gp_fixargs(args)))
    
    def reset(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Reset(*gp_fixargs(args)))
    
    def next(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Next(*gp_fixargs(args)))
    
    def remove(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Remove(*gp_fixargs(args)))
    
    def removeAll(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveAll(*gp_fixargs(args)))
    
    def insert(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Insert(*gp_fixargs(args)))
    
    def replace(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Replace(*gp_fixargs(args)))
    
    def clone(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Clone(*gp_fixargs(args)))
    

class Cursor(mixins.CursorMixin,_BaseArcObject):
    """A cursor is a data access object that can be used either to iterate through
       the set of rows in a table or to insert new rows into a table. Cursors have
       three forms: search , insert , or update . Cursors are commonly used to
       read and update attributes."""
    def reset(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Reset(*gp_fixargs(args)))
    
    def next(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Next(*gp_fixargs(args)))
    
    def newRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.NewRow(*gp_fixargs(args)))
    
    def updateRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.UpdateRow(*gp_fixargs(args)))
    
    def insertRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.InsertRow(*gp_fixargs(args)))
    
    def deleteRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.DeleteRow(*gp_fixargs(args)))
    

class Extent(mixins.ExtentMixin,_BaseArcObject):
    """An extent is a rectangle specified by providing the coordinate of the lower
       left corner and the coordinate of the upper right corner in map units."""
    XMin = passthrough_attr('XMin')
    YMin = passthrough_attr('YMin')
    XMax = passthrough_attr('XMax')
    YMax = passthrough_attr('YMax')
    MMin = passthrough_attr('MMin')
    MMax = passthrough_attr('MMax')
    ZMin = passthrough_attr('ZMin')
    ZMax = passthrough_attr('ZMax')
    width = passthrough_attr('width')
    height = passthrough_attr('height')
    depth = passthrough_attr('depth')
    lowerLeft = passthrough_attr('lowerLeft')
    lowerRight = passthrough_attr('lowerRight')
    upperLeft = passthrough_attr('upperLeft')
    upperRight = passthrough_attr('upperRight')
    spatialReference = passthrough_attr('spatialReference')
    polygon = passthrough_attr('polygon')
    JSON = passthrough_attr('JSON')
    def contains(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Contains(*gp_fixargs([second_geometry])))
    
    def crosses(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Crosses(*gp_fixargs([second_geometry])))
    
    def disjoint(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Disjoint(*gp_fixargs([second_geometry])))
    
    def equals(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Equals(*gp_fixargs([second_geometry])))
    
    def overlaps(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Overlaps(*gp_fixargs([second_geometry])))
    
    def touches(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Touches(*gp_fixargs([second_geometry])))
    
    def within(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Within(*gp_fixargs([second_geometry])))
    
    def projectAs(self, spatial_reference, transformation_name=None):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ProjectAs(*gp_fixargs((spatial_reference, transformation_name))))
    

class FeatureSet(mixins.FeatureSetMixin,_BaseArcObject):
    """FeatureSet objects are a lightweight representation of a feature class.
       They are a special data element that contains not only schema, but also the
       data. The FeatureSet object is also how feature data is sent and received
       from the server."""
    JSON = passthrough_attr('JSON')
    def load(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Load(*gp_fixargs(args)))
    
    def save(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Save(*gp_fixargs(args)))
    

class Field(mixins.FieldMixin,_BaseArcObject):
    """The field object represents a column in a table. A field has many
       properties, the most obvious ones being its name and its type."""
    name = passthrough_attr('name')
    aliasName = passthrough_attr('aliasName')
    baseName = passthrough_attr('baseName')
    domain = passthrough_attr('domain')
    type = passthrough_attr('type')
    length = passthrough_attr('length')
    precision = passthrough_attr('precision')
    scale = passthrough_attr('scale')
    editable = passthrough_attr('editable')
    isNullable = passthrough_attr('isNullable')
    required = passthrough_attr('required')
    defaultValue = passthrough_attr('defaultValue')
    

class FieldInfo(mixins.FieldInfoMixin,_BaseArcObject):
    """Provides field info methods and properties for layer and table views."""
    count = passthrough_attr('count')
    def addField(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddField(*gp_fixargs(args)))
    
    def getFieldName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetFieldName(*gp_fixargs(args)))
    
    def getNewName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetNewName(*gp_fixargs(args)))
    
    def getSplitRule(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSplitRule(*gp_fixargs(args)))
    
    def getVisible(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetVisible(*gp_fixargs(args)))
    
    def setFieldName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetFieldName(*gp_fixargs(args)))
    
    def setNewName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetNewName(*gp_fixargs(args)))
    
    def setSplitRule(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetSplitRule(*gp_fixargs(args)))
    
    def setVisible(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetVisible(*gp_fixargs(args)))
    
    def removeField(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveField(*gp_fixargs(args)))
    
    def findFieldByName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.FindFieldByName(*gp_fixargs(args)))
    
    def findFieldByNewName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.FindFieldByNewName(*gp_fixargs(args)))
    
    def loadFromString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadFromString(*gp_fixargs(args)))
    
    def exportToString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ExportToString(*gp_fixargs(args)))
    

class FieldMap(mixins.FieldMapMixin,_BaseArcObject):
    """The FieldMap object provides a field definition and a list of input fields
       taken from a set of tables or feature classes."""
    mergeRule = passthrough_attr('mergeRule')
    outputField = passthrough_attr('outputField')
    joinDelimiter = passthrough_attr('joinDelimiter')
    inputFieldCount = passthrough_attr('inputFieldCount')
    def addInputField(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddInputField(*gp_fixargs(args)))
    
    def getInputTableName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetInputTableName(*gp_fixargs(args)))
    
    def getInputFieldName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetInputFieldName(*gp_fixargs(args)))
    
    def getStartTextPosition(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetStartTextPosition(*gp_fixargs(args)))
    
    def getEndTextPosition(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetEndTextPosition(*gp_fixargs(args)))
    
    def removeAll(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveAll(*gp_fixargs(args)))
    
    def removeInputField(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveInputField(*gp_fixargs(args)))
    
    def findInputFieldIndex(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.FindInputFieldIndex(*gp_fixargs(args)))
    
    def setStartTextPosition(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetStartTextPosition(*gp_fixargs(args)))
    
    def setEndTextPosition(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetEndTextPosition(*gp_fixargs(args)))
    

class FieldMappings(mixins.FieldMappingsMixin,_BaseArcObject):
    """The FieldMappings object is a collection of FieldMap objects and it is used
       as the parameter value for tools that perform field mapping, such as Merge."""
    fieldValidationWorkspace = passthrough_attr('fieldValidationWorkspace')
    fieldCount = passthrough_attr('fieldCount')
    fields = passthrough_attr('fields')
    fieldMappings = passthrough_attr('fieldMappings')
    def addTable(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddTable(*gp_fixargs(args)))
    
    def removeAll(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveAll(*gp_fixargs(args)))
    
    def addFieldMap(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddFieldMap(*gp_fixargs(args)))
    
    def getFieldMap(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetFieldMap(*gp_fixargs(args)))
    
    def replaceFieldMap(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ReplaceFieldMap(*gp_fixargs(args)))
    
    def removeFieldMap(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveFieldMap(*gp_fixargs(args)))
    
    def findFieldMapIndex(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.FindFieldMapIndex(*gp_fixargs(args)))
    
    def loadFromString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadFromString(*gp_fixargs(args)))
    
    def exportToString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ExportToString(*gp_fixargs(args)))
    

class Filter(_BaseArcObject):
    """The filter object allows you to specify the choices available for a
       parameter."""
    type = passthrough_attr('type')
    list = passthrough_attr('list')
    

class GeoProcessor(_BaseArcObject):
    messageCount = passthrough_attr('messageCount')
    maxSeverity = passthrough_attr('maxSeverity')
    parameterCount = passthrough_attr('parameterCount')
    toolbox = passthrough_attr('toolbox')
    overwriteOutput = passthrough_attr('overwriteOutput')
    logHistory = passthrough_attr('logHistory')
    scriptVersion = passthrough_attr('scriptVersion')
    severityLevel = passthrough_attr('severityLevel')
    def getInstallInfo(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetInstallInfo(*gp_fixargs(args)))
    
    def listInstallations(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListInstallations(*gp_fixargs(args)))
    
    def setProgressor(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetProgressor(*gp_fixargs(args)))
    
    def resetProgressor(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ResetProgressor(*gp_fixargs(args)))
    
    def setProgressorLabel(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetProgressorLabel(*gp_fixargs(args)))
    
    def setProgressorPosition(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetProgressorPosition(*gp_fixargs(args)))
    
    def resetEnvironments(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ResetEnvironments(*gp_fixargs(args)))
    
    def clearEnvironment(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ClearEnvironment(*gp_fixargs(args)))
    
    def getMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetMessage(*gp_fixargs(args)))
    
    def getSeverity(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSeverity(*gp_fixargs(args)))
    
    def getReturnCode(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetReturnCode(*gp_fixargs(args)))
    
    def getMessages(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetMessages(*gp_fixargs(args)))
    
    def addMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddMessage(*gp_fixargs(args)))
    
    def addIDMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddIDMessage(*gp_fixargs(args)))
    
    def getIDMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetIDMessage(*gp_fixargs(args)))
    
    def addError(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddError(*gp_fixargs(args)))
    
    def addWarning(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddWarning(*gp_fixargs(args)))
    
    def addReturnMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddReturnMessage(*gp_fixargs(args)))
    
    def setProduct(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetProduct(*gp_fixargs(args)))
    
    def checkProduct(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CheckProduct(*gp_fixargs(args)))
    
    def productInfo(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ProductInfo(*gp_fixargs(args)))
    
    def checkOutExtension(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CheckOutExtension(*gp_fixargs(args)))
    
    def checkInExtension(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CheckInExtension(*gp_fixargs(args)))
    
    def checkExtension(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CheckExtension(*gp_fixargs(args)))
    
    def getParameterAsText(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetParameterAsText(*gp_fixargs(args)))
    
    def setParameterAsText(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetParameterAsText(*gp_fixargs(args)))
    
    def getParameter(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetParameter(*gp_fixargs(args)))
    
    def setParameter(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetParameter(*gp_fixargs(args)))
    
    def copyParameter(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CopyParameter(*gp_fixargs(args)))
    
    def listFiles(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListFiles(*gp_fixargs(args)))
    
    def listTools(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListTools(*gp_fixargs(args)))
    
    def listEnvironments(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListEnvironments(*gp_fixargs(args)))
    
    def listToolboxes(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListToolboxes(*gp_fixargs(args)))
    
    def addToolbox(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddToolbox(*gp_fixargs(args)))
    
    def removeToolbox(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveToolbox(*gp_fixargs(args)))
    
    def getSystemEnvironment(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSystemEnvironment(*gp_fixargs(args)))
    
    def command(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Command(*gp_fixargs(args)))
    
    def usage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Usage(*gp_fixargs(args)))
    
    def exists(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Exists(*gp_fixargs(args)))
    
    def refreshCatalog(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RefreshCatalog(*gp_fixargs(args)))
    
    def refreshActiveView(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RefreshActiveView(*gp_fixargs(args)))
    
    def refreshTOC(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RefreshTOC(*gp_fixargs(args)))
    
    def listFeatureClasses(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListFeatureClasses(*gp_fixargs(args)))
    
    def listDatasets(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListDatasets(*gp_fixargs(args)))
    
    def listTables(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListTables(*gp_fixargs(args)))
    
    def listRasters(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListRasters(*gp_fixargs(args)))
    
    def listWorkspaces(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListWorkspaces(*gp_fixargs(args)))
    
    def listVersions(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListVersions(*gp_fixargs(args)))
    
    def listUsers(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListUsers(*gp_fixargs(args)))
    
    def disconnectUser(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.DisconnectUser(*gp_fixargs(args)))
    
    def listFields(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListFields(*gp_fixargs(args)))
    
    def listIndexes(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListIndexes(*gp_fixargs(args)))
    
    def searchCursor(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SearchCursor(*gp_fixargs(args)))
    
    def updateCursor(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.UpdateCursor(*gp_fixargs(args)))
    
    def insertCursor(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.InsertCursor(*gp_fixargs(args)))
    
    def describe(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Describe(*gp_fixargs(args)))
    
    def createObject(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateObject(*gp_fixargs(args)))
    
    def validateFieldName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ValidateFieldName(*gp_fixargs(args)))
    
    def validateTableName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ValidateTableName(*gp_fixargs(args)))
    
    def parseFieldName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ParseFieldName(*gp_fixargs(args)))
    
    def parseTableName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ParseTableName(*gp_fixargs(args)))
    
    def createScratchName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateScratchName(*gp_fixargs(args)))
    
    def createUniqueName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateUniqueName(*gp_fixargs(args)))
    
    def saveSettings(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SaveSettings(*gp_fixargs(args)))
    
    def loadSettings(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadSettings(*gp_fixargs(args)))
    
    def testSchemaLock(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.TestSchemaLock(*gp_fixargs(args)))
    
    def createRandomValueGenerator(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateRandomValueGenerator(*gp_fixargs(args)))
    
    def isSynchronous(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.IsSynchronous(*gp_fixargs(args)))
    
    def getParameterCount(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetParameterCount(*gp_fixargs(args)))
    
    def getParameterValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetParameterValue(*gp_fixargs(args)))
    
    def getParameterInfo(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetParameterInfo(*gp_fixargs(args)))
    
    def addFieldDelimiters(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddFieldDelimiters(*gp_fixargs(args)))
    
    def listPrinterNames(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListPrinterNames(*gp_fixargs(args)))
    
    def wildcardMatch(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.WildcardMatch(*gp_fixargs(args)))
    
    def alterAliasName(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AlterAliasName(*gp_fixargs(args)))
    
    def listSpatialReferences(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListSpatialReferences(*gp_fixargs(args)))
    
    def listTransformations(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListTransformations(*gp_fixargs(args)))
    
    def acceptConnections(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AcceptConnections(*gp_fixargs(args)))
    
    def logUsageMetering(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LogUsageMetering(*gp_fixargs(args)))
    
    def createGPSDDraft(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateGPSDDraft(*gp_fixargs(args)))
    
    def fromEsriJson(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.FromEsriJson(*gp_fixargs(args)))
    
    def listDataStoreItems(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListDataStoreItems(*gp_fixargs(args)))
    
    def validateDataStoreItem(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ValidateDataStoreItem(*gp_fixargs(args)))
    
    def removeDataStoreItem(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveDataStoreItem(*gp_fixargs(args)))
    
    def addDataStoreItem(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddDataStoreItem(*gp_fixargs(args)))
    
    def getSigninToken(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSigninToken(*gp_fixargs(args)))
    
    def getActivePortalURL(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetActivePortalURL(*gp_fixargs(args)))
    
    def listPortalURLs(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ListPortalURLs(*gp_fixargs(args)))
    

class Geometry(mixins.GeometrySpecializationMixin,_BaseArcObject):
    """Geometry objects define a spatial location and an associated geometric
       shape."""
    labelPoint = passthrough_attr('labelPoint')
    type = passthrough_attr('type')
    extent = passthrough_attr('extent')
    trueCentroid = passthrough_attr('trueCentroid')
    firstPoint = passthrough_attr('firstPoint')
    lastPoint = passthrough_attr('lastPoint')
    isMultipart = passthrough_attr('isMultipart')
    hullRectangle = passthrough_attr('hullRectangle')
    area = passthrough_attr('area')
    length = passthrough_attr('length')
    length3D = passthrough_attr('length3D')
    partCount = passthrough_attr('partCount')
    pointCount = passthrough_attr('pointCount')
    centroid = passthrough_attr('centroid')
    WKB = passthrough_attr('WKB')
    WKT = passthrough_attr('WKT')
    spatialReference = passthrough_attr('spatialReference')
    JSON = passthrough_attr('JSON')
    def getPart(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetPart(*gp_fixargs(args)))
    
    def contains(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Contains(*gp_fixargs([second_geometry])))
    
    def crosses(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Crosses(*gp_fixargs([second_geometry])))
    
    def disjoint(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Disjoint(*gp_fixargs([second_geometry])))
    
    def equals(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Equals(*gp_fixargs([second_geometry])))
    
    def overlaps(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Overlaps(*gp_fixargs([second_geometry])))
    
    def touches(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Touches(*gp_fixargs([second_geometry])))
    
    def within(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Within(*gp_fixargs([second_geometry])))
    
    def projectAs(self, spatial_reference, transformation_name=None):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ProjectAs(*gp_fixargs((spatial_reference, transformation_name))))
    
    def positionAlongLine(self, value, use_percentage=False):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.PositionAlongLine(*gp_fixargs((value, use_percentage))))
    
    def queryPointAndDistance(self, in_point, use_percentage=False):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.QueryPointAndDistance(*gp_fixargs((in_point, use_percentage))))
    
    def snapToLine(self, in_point):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SnapToLine(*gp_fixargs((in_point,))))
    
    def measureOnLine(self, in_point, use_percentage=False):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.MeasureOnLine(*gp_fixargs((in_point, use_percentage))))
    
    def generalize(self, distance):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Generalize(*gp_fixargs((distance,))))
    
    def getLength(self, method="GEODESIC", units=None):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetLength(*gp_fixargs((method, units))))
    
    def getArea(self, method="GEODESIC", units=None):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetArea(*gp_fixargs((method, units))))
    
    def segmentAlongLine(self, start_measure, end_measure, use_percentage=False):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SegmentAlongLine(*gp_fixargs((start_measure, end_measure, use_percentage))))
    
    def angleAndDistanceTo(self, other_geometry, method='GEODESIC'):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AngleAndDistanceTo(*gp_fixargs((other_geometry, method))))
    
    def pointFromAngleAndDistance(self, angle, distance, method='GEODESIC'):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.PointFromAngleAndDistance(*gp_fixargs((angle, distance, method))))
    
    def boundary(self):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Boundary())
    
    def buffer(self, distance):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Buffer(*gp_fixargs((distance,))))
    
    def clip(self, envelope):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Clip(*gp_fixargs((envelope,))))
    
    def convexHull(self):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ConvexHull())
    
    def difference(self, other):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Difference(*gp_fixargs((other,))))
    
    def intersect(self, other, dimension):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Intersect(*gp_fixargs((other, dimension))))
    
    def symmetricDifference(self, other):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SymmetricDifference(*gp_fixargs((other,))))
    
    def union(self, other):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Union(*gp_fixargs((other,))))
    
    def distanceTo(self, other):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.DistanceTo(*gp_fixargs((other,))))
    
    def densify(self, method, distance, deviation):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Densify(*gp_fixargs((method, distance, deviation))))
    
    def cut(self, other):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Cut(*gp_fixargs((other,))))
    

class Index(_BaseArcObject):
    """The Index object contains information about an index on a table. There are
       two types of indexes: spatial and attribute. Spatial indexes exist on the
       shape field of a feature class."""
    name = passthrough_attr('name')
    isAscending = passthrough_attr('isAscending')
    isUnique = passthrough_attr('isUnique')
    fields = passthrough_attr('fields')
    

class NetCDFFileProperties(mixins.NetCDFFilePropertiesMixin,_BaseArcObject):
    """The Network Common Data Form (netCDF) is a binary, self-describing,
       machine-independent file format for storing scientific data.
       
       Learn more about netCDF"""
    def getAttributeNames(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetAttributeNames(*gp_fixargs(args)))
    
    def getAttributeValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetAttributeValue(*gp_fixargs(args)))
    
    def getDimensionIndex(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetDimensionIndex(*gp_fixargs(args)))
    
    def getDimensions(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetDimensions(*gp_fixargs(args)))
    
    def getDimensionsByVariable(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetDimensionsByVariable(*gp_fixargs(args)))
    
    def getDimensionSize(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetDimensionSize(*gp_fixargs(args)))
    
    def getDimensionValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetDimensionValue(*gp_fixargs(args)))
    
    def getFieldType(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetFieldType(*gp_fixargs(args)))
    
    def getSpatialReference(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSpatialReference(*gp_fixargs(args)))
    
    def getVariables(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetVariables(*gp_fixargs(args)))
    
    def getVariablesByDimension(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetVariablesByDimension(*gp_fixargs(args)))
    

class Parameter(mixins.ParameterMixin,_BaseArcObject):
    """Every tool parameter has an associated parameter object with properties and
       methods that are useful in tool validation. Parameters are contained in a
       Python list."""
    name = passthrough_attr('name')
    displayName = passthrough_attr('displayName')
    direction = passthrough_attr('direction')
    datatype = passthrough_attr('datatype')
    parameterType = passthrough_attr('parameterType')
    parameterDependencies = passthrough_attr('parameterDependencies')
    enabled = passthrough_attr('enabled')
    value = passthrough_attr('value')
    defaultEnvironmentName = passthrough_attr('defaultEnvironmentName')
    altered = passthrough_attr('altered')
    hasBeenValidated = passthrough_attr('hasBeenValidated')
    category = passthrough_attr('category')
    schema = passthrough_attr('schema')
    filter = passthrough_attr('filter')
    filters = passthrough_attr('filters')
    symbology = passthrough_attr('symbology')
    message = passthrough_attr('message')
    multiValue = passthrough_attr('multiValue')
    columns = passthrough_attr('columns')
    valueAsText = passthrough_attr('valueAsText')
    values = passthrough_attr('values')
    def setErrorMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetErrorMessage(*gp_fixargs(args)))
    
    def setWarningMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetWarningMessage(*gp_fixargs(args)))
    
    def setIDMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetIDMessage(*gp_fixargs(args)))
    
    def clearMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ClearMessage(*gp_fixargs(args)))
    
    def hasError(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.HasError(*gp_fixargs(args)))
    
    def hasWarning(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.HasWarning(*gp_fixargs(args)))
    
    def isInputValueDerived(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.IsInputValueDerived(*gp_fixargs(args)))
    

class Point(mixins.PointMixin,_BaseArcObject):
    """The point object is used frequently with cursors. Point features return a
       single point object instead of an array of point objects. All other feature
       types—polygon, polyline, and multipoint—return an array of point
       objects or an array containing multiple arrays of point objects if the
       feature has multiple parts."""
    X = passthrough_attr('X')
    Y = passthrough_attr('Y')
    M = passthrough_attr('M')
    Z = passthrough_attr('Z')
    ID = passthrough_attr('ID')
    def clone(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Clone(*gp_fixargs(args)))
    
    def contains(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Contains(*gp_fixargs([second_geometry])))
    
    def crosses(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Crosses(*gp_fixargs([second_geometry])))
    
    def disjoint(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Disjoint(*gp_fixargs([second_geometry])))
    
    def equals(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Equals(*gp_fixargs([second_geometry])))
    
    def overlaps(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Overlaps(*gp_fixargs([second_geometry])))
    
    def touches(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Touches(*gp_fixargs([second_geometry])))
    
    def within(self, second_geometry):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Within(*gp_fixargs([second_geometry])))
    

class RandomNumberGenerator(_BaseArcObject):
    """Determines the type and seed that will be used to create random numbers
       between 0 and 1 for all tools that utilize random numbers, for example,
       CreateRandomRaster, CreateRandomPoints, and the ArcGIS.Rand() function.
       
       Returned from the randomGenerator environment."""
    def loadFromString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadFromString(*gp_fixargs(args)))
    
    def exportToString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ExportToString(*gp_fixargs(args)))
    

class RecordSet(mixins.RecordSetMixin,_BaseArcObject):
    """RecordSet objects are a lightweight representation of a table. They are a
       special data element that contains not only schema but also the data. The
       RecordSet object is also how tables are sent and received from the server."""
    JSON = passthrough_attr('JSON')
    def load(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Load(*gp_fixargs(args)))
    
    def save(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Save(*gp_fixargs(args)))
    

class Result(mixins.ResultMixin,_BaseArcObject):
    """A Result object is returned by geoprocessing tools."""
    status = passthrough_attr('status')
    resultID = passthrough_attr('resultID')
    messageCount = passthrough_attr('messageCount')
    maxSeverity = passthrough_attr('maxSeverity')
    outputCount = passthrough_attr('outputCount')
    inputCount = passthrough_attr('inputCount')
    def getMessage(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetMessage(*gp_fixargs(args)))
    
    def getMessages(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetMessages(*gp_fixargs(args)))
    
    def getSeverity(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetSeverity(*gp_fixargs(args)))
    
    def getOutput(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetOutput(*gp_fixargs(args)))
    
    def getInput(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetInput(*gp_fixargs(args)))
    
    def getMapImageURL(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetMapImageURL(*gp_fixargs(args)))
    
    def cancel(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Cancel(*gp_fixargs(args)))
    
    def saveToFile(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SaveToFile(*gp_fixargs(args)))
    

class Row(_BaseArcObject):
    """The Row object represents the row of a table. The Row object is returned
       from InsertCursor , SearchCursor , and UpdateCursor."""
    __passthrough_to_ao__ = True
    def setValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetValue(*gp_fixargs(args)))
    
    def getValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetValue(*gp_fixargs(args)))
    
    def setNull(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetNull(*gp_fixargs(args)))
    
    def isNull(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.IsNull(*gp_fixargs(args)))
    

class Schema(_BaseArcObject):
    """The schema of a dataset."""
    type = passthrough_attr('type')
    clone = passthrough_attr('clone')
    featureTypeRule = passthrough_attr('featureTypeRule')
    featureType = passthrough_attr('featureType')
    geometryTypeRule = passthrough_attr('geometryTypeRule')
    geometryType = passthrough_attr('geometryType')
    extentRule = passthrough_attr('extentRule')
    extent = passthrough_attr('extent')
    fieldsRule = passthrough_attr('fieldsRule')
    additionalFields = passthrough_attr('additionalFields')
    cellSizeRule = passthrough_attr('cellSizeRule')
    cellSize = passthrough_attr('cellSize')
    rasterRule = passthrough_attr('rasterRule')
    rasterFormatRule = passthrough_attr('rasterFormatRule')
    additionalChildren = passthrough_attr('additionalChildren')
    

class SpatialReference(mixins.SpatialReferenceMixin,_BaseArcObject):
    """Each part of the spatial reference has a number of properties (especially
       the coordinate system) that defines what map projection options are used to
       define horizontal coordinates."""
    type = passthrough_attr('type')
    name = passthrough_attr('name')
    alias = passthrough_attr('alias')
    abbreviation = passthrough_attr('abbreviation')
    remarks = passthrough_attr('remarks')
    factoryCode = passthrough_attr('factoryCode')
    PCSName = passthrough_attr('PCSName')
    PCSCode = passthrough_attr('PCSCode')
    GCSName = passthrough_attr('GCSName')
    GCSCode = passthrough_attr('GCSCode')
    spheroidName = passthrough_attr('spheroidName')
    spheroidCode = passthrough_attr('spheroidCode')
    projectionName = passthrough_attr('projectionName')
    projectionCode = passthrough_attr('projectionCode')
    datumName = passthrough_attr('datumName')
    datumCode = passthrough_attr('datumCode')
    primeMeridianName = passthrough_attr('primeMeridianName')
    primeMeridianCode = passthrough_attr('primeMeridianCode')
    angularUnitName = passthrough_attr('angularUnitName')
    angularUnitCode = passthrough_attr('angularUnitCode')
    linearUnitName = passthrough_attr('linearUnitName')
    linearUnitCode = passthrough_attr('linearUnitCode')
    hasXYPrecision = passthrough_attr('hasXYPrecision')
    hasZPrecision = passthrough_attr('hasZPrecision')
    hasMPrecision = passthrough_attr('hasMPrecision')
    falseOriginAndUnits = passthrough_attr('falseOriginAndUnits')
    ZFalseOriginAndUnits = passthrough_attr('ZFalseOriginAndUnits')
    MFalseOriginAndUnits = passthrough_attr('MFalseOriginAndUnits')
    domain = passthrough_attr('domain')
    ZDomain = passthrough_attr('ZDomain')
    MDomain = passthrough_attr('MDomain')
    usage = passthrough_attr('usage')
    centralMeridian = passthrough_attr('centralMeridian')
    centralMeridianInDegrees = passthrough_attr('centralMeridianInDegrees')
    longitudeOfOrigin = passthrough_attr('longitudeOfOrigin')
    latitudeOfOrigin = passthrough_attr('latitudeOfOrigin')
    latitudeOf1st = passthrough_attr('latitudeOf1st')
    latitudeOf2nd = passthrough_attr('latitudeOf2nd')
    falseEasting = passthrough_attr('falseEasting')
    falseNorthing = passthrough_attr('falseNorthing')
    centralParallel = passthrough_attr('centralParallel')
    standardParallel1 = passthrough_attr('standardParallel1')
    standardParallel2 = passthrough_attr('standardParallel2')
    longitudeOf1st = passthrough_attr('longitudeOf1st')
    longitudeOf2nd = passthrough_attr('longitudeOf2nd')
    scaleFactor = passthrough_attr('scaleFactor')
    azimuth = passthrough_attr('azimuth')
    semiMajorAxis = passthrough_attr('semiMajorAxis')
    semiMinorAxis = passthrough_attr('semiMinorAxis')
    flattening = passthrough_attr('flattening')
    longitude = passthrough_attr('longitude')
    radiansPerUnit = passthrough_attr('radiansPerUnit')
    metersPerUnit = passthrough_attr('metersPerUnit')
    GCS = passthrough_attr('GCS')
    isHighPrecision = passthrough_attr('isHighPrecision')
    XYTolerance = passthrough_attr('XYTolerance')
    MTolerance = passthrough_attr('MTolerance')
    ZTolerance = passthrough_attr('ZTolerance')
    XYResolution = passthrough_attr('XYResolution')
    MResolution = passthrough_attr('MResolution')
    ZResolution = passthrough_attr('ZResolution')
    classification = passthrough_attr('classification')
    def setFalseOriginAndUnits(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetFalseOriginAndUnits(*gp_fixargs(args)))
    
    def setZFalseOriginAndUnits(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetZFalseOriginAndUnits(*gp_fixargs(args)))
    
    def setMFalseOriginAndUnits(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetMFalseOriginAndUnits(*gp_fixargs(args)))
    
    def setDomain(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetDomain(*gp_fixargs(args)))
    
    def setZDomain(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetZDomain(*gp_fixargs(args)))
    
    def setMDomain(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetMDomain(*gp_fixargs(args)))
    
    def createFromFile(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.CreateFromFile(*gp_fixargs(args)))
    
    def create(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.Create(*gp_fixargs(args)))
    
    def loadFromString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadFromString(*gp_fixargs(args)))
    
    def exportToString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ExportToString(*gp_fixargs(args)))
    

class Value(_BaseArcObject):
    """The value object is returned from GetParameterInfo when used in a script
       tool's ToolValidator class."""
    value = passthrough_attr('value')
    isEmpty = passthrough_attr('isEmpty')
    

class ValueTable(mixins.ValueTableMixin,_BaseArcObject):
    """A value table is a flexible object that can be used as input for a
       multivalue parameter. It exists only during the lifetime of the
       geoprocessing object that created it."""
    rowCount = passthrough_attr('rowCount')
    columnCount = passthrough_attr('columnCount')
    def setColumns(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetColumns(*gp_fixargs(args)))
    
    def addRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.AddRow(*gp_fixargs(args)))
    
    def getRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetRow(*gp_fixargs(args)))
    
    def getValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetValue(*gp_fixargs(args)))
    
    def getTrueValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.GetTrueValue(*gp_fixargs(args)))
    
    def loadFromString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.LoadFromString(*gp_fixargs(args)))
    
    def exportToString(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.ExportToString(*gp_fixargs(args)))
    
    def removeRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.RemoveRow(*gp_fixargs(args)))
    
    def setRow(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetRow(*gp_fixargs(args)))
    
    def setValue(self, *args):
        from ..geoprocessing._base import gp_fixargs
        return convertArcObjectToPythonObject(self._arc_object.SetValue(*gp_fixargs(args)))
    