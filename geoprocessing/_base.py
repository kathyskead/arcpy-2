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
import arcgisscripting
import functools

"""Geoprocessing wrapper for the arcgisscripting library. Attempts to organize/make usage easier."""

__all__ = ['Geoprocessor', 'gp', 'env']

def gp_fixargs(args, strip_right_nones=False, string_results=True):
    """Adjusts arguments passed into a function to be arcgisscripting-friendly:
       pass in stringified result objects and unwrapped arc objects"""
    from ..arcobjects import Result, _BaseArcObject
    new_args = []
    for arg in args:
        if isinstance(arg, Result) and string_results:
            new_args.append(str(arg._arc_object))
        elif isinstance(arg, (tuple, list)):
            new_args.append(gp_fixargs(arg))
        elif isinstance(arg, _BaseArcObject):
            new_args.append(arg._arc_object)
        else:
            new_args.append(arg)
        del arg
    if strip_right_nones:
        while new_args and new_args[-1] is None:
            new_args.pop()
    del args
    return new_args

def passthrough_attr(prop):
    "Basic attribute passthrough for a wrapped Arc object -- allows for early binding."
    def get_(self):
        "Geoprocessor %s property" % prop
        return getattr(self._arc_object, prop)
    def set_(self, val):
        return setattr(self._arc_object, prop, val)
    return property(get_, set_)

class Geoprocessor(object):
    """Represents a geoprocessing object in ArcGIS"""
    def __init__(self):
        """Geoprocessor()"""
        self._gp = arcgisscripting.create(10.0)
    @property
    def _arc_object(self):
        return self._gp

    addToResults = passthrough_attr('addtoresults')
    messageCount = passthrough_attr('messagecount')
    maxSeverity = passthrough_attr('maxseverity')
    parameterCount = passthrough_attr('parametercount')
    toolbox = passthrough_attr('toolbox')
    overwriteOutput = passthrough_attr('overwriteoutput')
    logHistory = passthrough_attr('loghistory')
    scriptVersion = passthrough_attr('scriptversion')
    severityLevel = passthrough_attr('severitylevel')
    def getInstallInfo(self, *args):
        """GP function GetInstallInfo"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetInstallInfo(*gp_fixargs(args, True)))
    def listInstallations(self, *args):
        """GP function ListInstallations"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListInstallations(*gp_fixargs(args, True)))
    def setProgressor(self, *args):
        """GP function SetProgressor"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetProgressor(*gp_fixargs(args, True)))
    def resetProgressor(self, *args):
        """GP function ResetProgressor"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ResetProgressor(*gp_fixargs(args, True)))
    def setProgressorLabel(self, *args):
        """GP function SetProgressorLabel"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetProgressorLabel(*gp_fixargs(args, True)))
    def setProgressorPosition(self, *args):
        """GP function SetProgressorPosition"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetProgressorPosition(*gp_fixargs(args, True)))
    def resetEnvironments(self, *args):
        """GP function ResetEnvironments"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ResetEnvironments(*gp_fixargs(args, True)))
    def clearEnvironment(self, *args):
        """GP function ClearEnvironment"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ClearEnvironment(*gp_fixargs(args, True)))
    def getMessage(self, *args):
        """getMessage(index)

           Returns a specific message.

             index(Integer):
           The index position of the message."""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetMessage(*gp_fixargs(args, True)))
    def getSeverity(self, *args):
        """getSeverity(index)

           Returns the severity of a specific message.

             index(Integer):
           The message index position."""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetSeverity(*gp_fixargs(args, True)))
    def getReturnCode(self, *args):
        """GP function GetReturnCode"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetReturnCode(*gp_fixargs(args, True)))
    def getMessages(self, *args):
        """getMessages({severity})

           Returns messages.

             severity{Integer}:
           The type of messages to be returned: 0=message, 1=warning, 2=error. Not specifying a value returns all message types.

            * 0:   informational message

            * 1:   warning message

            * 2:   error message"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetMessages(*gp_fixargs(args, True)))
    def addMessage(self, *args):
        """GP function AddMessage"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddMessage(*gp_fixargs(args, True)))
    def addIDMessage(self, *args):
        """GP function AddIDMessage"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddIDMessage(*gp_fixargs(args, True)))
    def getIDMessage(self, *args):
        """GP function GetIDMessage"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetIDMessage(*gp_fixargs(args, True)))
    def addError(self, *args):
        """GP function AddError"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddError(*gp_fixargs(args, True)))
    def addWarning(self, *args):
        """GP function AddWarning"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddWarning(*gp_fixargs(args, True)))
    def addReturnMessage(self, *args):
        """GP function AddReturnMessage"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddReturnMessage(*gp_fixargs(args, True)))
    def setProduct(self, *args):
        """GP function SetProduct"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetProduct(*gp_fixargs(args, True)))
    def checkProduct(self, *args):
        """GP function CheckProduct"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CheckProduct(*gp_fixargs(args, True)))
    def productInfo(self, *args):
        """GP function ProductInfo"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ProductInfo(*gp_fixargs(args, True)))
    def checkOutExtension(self, *args):
        """GP function CheckoutExtension"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CheckoutExtension(*gp_fixargs(args, True)))
    def checkInExtension(self, *args):
        """GP function CheckinExtension"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CheckinExtension(*gp_fixargs(args, True)))
    def checkExtension(self, *args):
        """GP function CheckExtension"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CheckExtension(*gp_fixargs(args, True)))
    def listSpatialReferences(self, *args):
        """GP function ListSpatialReferences"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListSpatialReferences(*gp_fixargs(args, True)))
    def listTransformations(self, *args):
        """GP function ListTransformations"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListTransformations(*gp_fixargs(args, True)))
    def getParameterAsText(self, *args):
        """GP function GetParameterAsText"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetParameterAsText(*gp_fixargs(args, True)))
    def setParameterAsText(self, *args):
        """GP function SetParameterAsText"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetParameterAsText(*gp_fixargs(args, True)))
    def getParameter(self, *args):
        """GP function GetParameter"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetParameter(*gp_fixargs(args, True)))
    def setParameter(self, *args):
        """GP function SetParameter"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SetParameter(*gp_fixargs(args, True)))
    def copyParameter(self, *args):
        """GP function CopyParameter"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CopyParameter(*gp_fixargs(args, True)))
    def listFiles(self, *args):
        """GP function ListFiles"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListFiles(*gp_fixargs(args, True)))
    def listTools(self, *args):
        """GP function ListTools"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListTools(*gp_fixargs(args, True)))
    def listEnvironments(self, *args):
        """GP function ListEnvironments"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListEnvironments(*gp_fixargs(args, True)))
    def listToolboxes(self, *args):
        """GP function ListToolboxes"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListToolboxes(*gp_fixargs(args, True)))
    def addToolbox(self, *args):
        """GP function AddToolbox"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddToolbox(*gp_fixargs(args, True)))
    def removeToolbox(self, *args):
        """GP function RemoveToolbox"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.RemoveToolbox(*gp_fixargs(args, True)))
    def getSystemEnvironment(self, *args):
        """GP function GetSystemEnvironment"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetSystemEnvironment(*gp_fixargs(args, True)))
    def command(self, *args):
        """GP function Command"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.Command(*gp_fixargs(args, True)))
    def usage(self, *args):
        """GP function Usage"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.Usage(*gp_fixargs(args, True)))
    def exists(self, *args):
        """GP function Exists"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.Exists(*gp_fixargs(args, True)))
    def refreshCatalog(self, *args):
        """GP function RefreshCatalog"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.RefreshCatalog(*gp_fixargs(args, True)))
    def refreshGraphics(self, *args):
        """GP function RefreshGraphics"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.RefreshGraphics(*gp_fixargs(args, True)))
    def refreshContents(self, *args):
        """GP function RefreshContents"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.RefreshContents(*gp_fixargs(args, True)))
    def listFeatureClasses(self, *args):
        """GP function ListFeatureClasses"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListFeatureClasses(*gp_fixargs(args, True)))
    def listDatasets(self, *args):
        """GP function ListDatasets"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListDatasets(*gp_fixargs(args, True)))
    def listTables(self, *args):
        """GP function ListTables"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListTables(*gp_fixargs(args, True)))
    def listRasters(self, *args):
        """GP function ListRasters"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListRasters(*gp_fixargs(args, True)))
    def listWorkspaces(self, *args):
        """GP function ListWorkspaces"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListWorkspaces(*gp_fixargs(args, True)))
    def listVersions(self, *args):
        """GP function ListVersions"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListVersions(*gp_fixargs(args, True)))
    def listFields(self, *args):
        """GP function ListFields"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListFields(*gp_fixargs(args, True)))
    def listIndexes(self, *args):
        """GP function ListIndexes"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListIndexes(*gp_fixargs(args, True)))
    def listPrinterNames(self, *args):
        """GP function ListPrinterNames"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListPrinterNames(*gp_fixargs(args, True)))
    def searchCursor(self, *args):
        """GP function SearchCursor"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SearchCursor(*gp_fixargs(args, True)))
    def updateCursor(self, *args):
        """GP function UpdateCursor"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.UpdateCursor(*gp_fixargs(args, True)))
    def insertCursor(self, *args):
        """GP function InsertCursor"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.InsertCursor(*gp_fixargs(args, True)))
    def describe(self, *args):
        """GP function Describe"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.Describe(*gp_fixargs(args, True)))
    def createObject(self, *args):
        """GP function CreateObject"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CreateObject(*gp_fixargs(args, True)))
    def validateFieldName(self, *args):
        """GP function ValidateFieldName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ValidateFieldName(*gp_fixargs(args, True)))
    def validateTableName(self, *args):
        """GP function ValidateTableName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ValidateTableName(*gp_fixargs(args, True)))
    def parseFieldName(self, *args):
        """GP function ParseFieldName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ParseFieldName(*gp_fixargs(args, True)))
    def parseTableName(self, *args):
        """GP function ParseTableName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ParseTableName(*gp_fixargs(args, True)))
    def createScratchName(self, *args):
        """GP function CreateScratchName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CreateScratchName(*gp_fixargs(args, True)))
    def createUniqueName(self, *args):
        """GP function CreateUniqueName"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CreateUniqueName(*gp_fixargs(args, True)))
    def saveSettings(self, *args):
        """GP function SaveSettings"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.SaveSettings(*gp_fixargs(args, True)))
    def loadSettings(self, *args):
        """GP function LoadSettings"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.LoadSettings(*gp_fixargs(args, True)))
    def testSchemaLock(self, *args):
        """GP function TestSchemaLock"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.TestSchemaLock(*gp_fixargs(args, True)))
    def createRandomValueGenerator(self, *args):
        """GP function CreateRandomValueGenerator"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.CreateRandomValueGenerator(*gp_fixargs(args, True)))
    def isSynchronous(self, *args):
        """GP function IsSynchronous"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.IsSynchronous(*gp_fixargs(args, True)))
    def getParameterCount(self, *args):
        """GP function GetParameterCount"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetParameterCount(*gp_fixargs(args, True)))
    def getParameterValue(self, *args):
        """GP function GetParameterValue"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetParameterValue(*gp_fixargs(args, True)))
    def getParameterInfo(self, *args):
        """GP function GetParameterInfo"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.GetParameterInfo(*gp_fixargs(args, True)))
    def addFieldDelimiters(self, *args):
        """GP function AddFieldDelimiters"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.AddFieldDelimiters(*gp_fixargs(args, True)))
    def listPrinterNames(self, *args):
        """GP function ListPrinterNames"""
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        return convertArcObjectToPythonObject(
                    self._gp.ListPrinterNames(*gp_fixargs(args, True)))
    def getSystemToolboxesPath(self):
        return (arcgisscripting.getsystemtoolboxespath()
                if hasattr(arcgisscripting, 'getsystemtoolboxespath')
                else self._gp.GetSystemToolboxesPath())
    def getSystemToolboxesPaths(self):
        return (arcgisscripting.getsystemtoolboxespaths()
                if hasattr(arcgisscripting, 'getsystemtoolboxespaths')
                else self._gp.GetSystemToolboxesPaths())
    def getMyToolboxesPath(self):
        return (arcgisscripting.getmytoolboxespath()
                if hasattr(arcgisscripting, 'getmytoolboxespath')
                else self._gp.GetMyToolboxesPath())
    def wildcardMatch(self, wildcard, data):
        return self._gp.WildcardMatch(wildcard, data)
    def alterAliasName(self, table, alias):
        return self._gp.alterAliasName(table, alias)
    def acceptConnections(self, sde_workspace, accept_connections):
        return self._gp.AcceptConnections(sde_workspace, accept_connections)
    def logUsageMetering(self, code, task_name, num_objects=0, units=0.0):
        return self._gp.LogUsageMetering(code, task_name, num_objects, units)
    def createGPSDDraft(self, result, out_sddraft, service_name, server_type="ARCGIS_SERVER", connection_file_path="", copy_data_to_server=True, folder_name=None, summary=None, tags=None, executionType="Asynchronous", resultMapServer=False, showMessages="None", maximumRecords=1000, minInstances=1, maxInstances=2, maxUsageTime=600, maxWaitTime=60, maxIdleTime=1800):
        return self._gp.createGPSDDraft(result, out_sddraft, service_name, server_type, connection_file_path, copy_data_to_server, folder_name, summary, tags, executionType, resultMapServer, showMessages, maximumRecords, minInstances, maxInstances, maxUsageTime, maxWaitTime, maxIdleTime)
    def fromEsriJson(self, json):
        return self._gp.FromEsriJson(json)
    def listDataStoreItems(self, connection_file, datastore_type):
        return self._gp.listDataStoreItems(connection_file, datastore_type)
    def validateDataStoreItem(self, connection_file, datastore_type, connection_name):
        return self._gp.validateDataStoreItem(connection_file, datastore_type, connection_name)
    def removeDataStoreItem(self, connection_file, datastore_type, connection_name):
        return self._gp.removeDataStoreItem(connection_file, datastore_type, connection_name)
    def addDataStoreItem(self, connection_file, datastore_type, connection_name, server_path, client_path="", hostname=""):
        return self._gp.addDataStoreItem(connection_file, datastore_type, connection_name, server_path, client_path, hostname)
    def getSigninToken(self):
        return self._gp.getSigninToken()
    def getActivePortalURL(self):
        return self._gp.getActivePortalURL()
    def listPortalURLs(self):
        return self._gp.listPortalURLs()
    def __getattr__(self, attr):
        from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
        if attr == "__methods__":
            return []
        val = getattr(self._gp, attr)
        if callable(val):
            return lambda *args: val(*gp_fixargs(args, True))
        else:
            return convertArcObjectToPythonObject(val)

def gptooldoc(toolname, toolinfo=None):
    """Decorator for adding extra documentation strings to GP tool functions to
       help autocomplete."""
    def _params(fn):
        def fixcol(column):
            if isinstance(column, (list, tuple)):
                return '|'.join(fixcol(col) for col in column)
            elif isinstance(column, set):
                return '|'.join(fixcol(col) for col in sorted(column))
            else:
                return str(column)
        if toolname and isinstance(toolname, basestring):
            fn.__esri_toolname__ = toolname
        else:
            fn.__esri_toolinfo__ = [':'.join(fixcol(col)
                                             for col in cols)
                                    for cols in toolinfo]
        return fn
    return _params

def GPEnvironments(geoprocessor):
    def propfactory(env):
        def get_(self):
            return self[env]
        def set_(self, val):
            if hasattr(val, '_arc_object'):
                val = val._arc_object
            self[env] = val
        def del_(self):
            del self[env]
        return property(get_, set_, del_)
    class GPEnvironment(object):
        @apply
        def overwriteOutput():
            def get(self):
                return self._gp.OverwriteOutput
            def set(self, val):
                self._gp.OverwriteOutput = val
            return property(get, set)
        def __init__(self, gp):
            import weakref
            self._environments = set()
            self._gp = gp._gp
            self._refresh()
        def _refresh(self):
            envset = (set(env for env in self._gp.listEnvironments()))
            if envset == self._environments:
                return
            to_add = envset - self._environments
            to_delete = self._environments - envset
            # Sweep deleted environments
            for attr in to_delete:
                delattr(self.__class__, attr)
                self._environments.remove(attr)
            # Add new environments
            for environment in to_add:
                setattr(self.__class__, environment, propfactory(environment))
                self._environments.add(environment)
        def __iter__(self):
            for key in self._gp.listenvironments():
                yield key
        def keys(self):
            return self._gp.listenvironments()
        def values(self):
            return [v for k,v in self.items()]
        def iteritems(self):
            from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
            return ((k, convertArcObjectToPythonObject(getattr(self._gp, k)))
                    for k in self._gp.listEnvironments())
        def items(self):
            return tuple(self.iteritems())
        def __getitem__(self, item):
            from ..arcobjects.arcobjectconversion import convertArcObjectToPythonObject
            return convertArcObjectToPythonObject(getattr(self._gp, item))
        def __setitem__(self, item, value):
            # Force fetch
            need_refresh = item not in self._gp.listEnvironments()
            if hasattr(value, '_arc_object'):
                value = value._arc_object
            ret_ = setattr(self._gp, item, value)
            if need_refresh:
                self._refresh()
            return ret_
        def __delitem__(self, item):
            ret_ = self._gp.clearenvironment(item)
            self._refresh()
            return ret_
    return GPEnvironment(geoprocessor)

gp = Geoprocessor()
env = GPEnvironments(gp)
