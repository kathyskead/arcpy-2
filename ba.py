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
from __future__ import with_statement
from .arcobjects.arcobjectconversion import convertArcObjectToPythonObject
from .geoprocessing._base import gptooldoc, gp, gp_fixargs
"""This is an automatically generated module with Python interfaces for geoprocessing toolboxes (Business Analyst(ba)). Do not edit this file directly."""

@gptooldoc('BenchmarkReport_ba', None)
def BenchmarkReport(IN_IN_BDS_FEATURE_LAYER=None, IN_SELECTED_SUMMARIZATIONS=None, Layer_Area_ID_Field_Store_Name_Field_Area_Description_Field_Selection_Single_ID=None, IN_TA_FIELDS=None, IN_BENCHMARK_OPTIONS=None, IN_BENCHMARK_TA=None, InLayoutOptions=None, InSortTA=None, InSortTADescend=None, InSortTAField=None, OutFolder=None, NeedReportOutput=None, OutReportName=None, Benchmark_Report=None, NeedExcelOutput=None, NeedTableOutput=None):
    """BenchmarkReport_ba(IN_IN_BDS_FEATURE_LAYER, IN_SELECTED_SUMMARIZATIONS;IN_SELECTED_SUMMARIZATIONS..., Layer{Area ID Field}{Store Name Field}{Area Description Field}{Selection}{Single ID};Layer{Area ID Field}{Store Name Field}{Area Description Field}{Selection}{Single ID}..., {IN_TA_FIELDS;IN_TA_FIELDS...}, {NONE | USE_AVERAGE | USE_MEDIAN | USE_TRADE AREA}, {IN_BENCHMARK_TA}, {VARIABLES_IN_COLUMNS | VARIABLES_IN_ROWS}, {TRUE | FALSE}, {TRUE | FALSE}, {InSortTAField}, {OutFolder}, {CREATE_REPORT | DONT_CREATE_REPORT}, {OutReportName}, {Benchmark Report}, {CREATE_EXCEL | DONT_CREATE_EXCEL}, {CREATE_TABLE | DONT_CREATE_TABLE})
       
       A comparitive report that benchmarks 2 or more trade areas based on selected volumetric data (typically demographic data).
       
       INPUTS:
         IN_IN_BDS_FEATURE_LAYER (, Required): Input Data Layer
         IN_SELECTED_SUMMARIZATIONS (, Required): Input Summarizations
         Layer{Area ID Field}{Store Name Field}{Area Description Field}{Selection}{Single ID} (, Required): Trade Areas
         IN_TA_FIELDS (, Optional): Input Trade Area Fields
         IN_BENCHMARK_OPTIONS (, Optional): Benchmarking Preferences
         IN_BENCHMARK_TA (, Optional): Trade Area for Benchmark
         InSortTA (, Optional): Sort Trade Areas
         InSortTADescend (, Optional): Descending Sort Order
         InSortTAField (, Optional): By the Output Field
         NeedReportOutput (, Optional): Create Report
         OutReportName (, Optional): Report Name
         Benchmark Report (, Optional): Report Title
       OUTPUTS:
         InLayoutOptions (, Optional): Layout Options
         OutFolder (, Optional): Report Output Folder
         NeedExcelOutput (, Optional): Generate Excel Spreadsheet
         NeedTableOutput (, Optional): Generate Database Table"""
    with gp:
        return convertArcObjectToPythonObject(gp._gp.BenchmarkReport_ba(*gp_fixargs((IN_IN_BDS_FEATURE_LAYER, IN_SELECTED_SUMMARIZATIONS, Layer_Area_ID_Field_Store_Name_Field_Area_Description_Field_Selection_Single_ID, IN_TA_FIELDS, IN_BENCHMARK_OPTIONS, IN_BENCHMARK_TA, InLayoutOptions, InSortTA, InSortTADescend, InSortTAField, OutFolder, NeedReportOutput, OutReportName, Benchmark_Report, NeedExcelOutput, NeedTableOutput), True)))
@gptooldoc('MapSeriesReport_ba', None)
def MapSeriesReport(InputBoundaryLayer=None, All_Or_Single_Or_Selected=None, TitleFieldName=None, HideInactiveTAs=None, ByID_Or_ByName=None, Single_Site=None, CreateReport=None, ReportTitle=None, OutputFolder=None, ExportToImages=None, ImagesFormat=None, OutputFolderImages=None):
    """MapSeriesReport_ba(InputBoundaryLayer, ALL | SINGLE, TitleFieldName, true | false, {ID | NAME}, {Single_Site}, {true | false}, {ReportTitle}, {OutputFolder}, {true | false}, {JPG | BMP | GIF | EMF | PNG | TIFF}, {OutputFolderImages})
       
       Generates a series of maps based on one or more features of a trade area.
       
       INPUTS:
         InputBoundaryLayer (, Required): Boundary Layer
         All_Or_Single_Or_Selected (, Required): Features to use
         TitleFieldName (, Required): Field with titles for each map
         HideInactiveTAs (, Required): Hide all trade areas except for the current one on rendering image
         ByID_Or_ByName (, Optional): Select by
         Single_Site (, Optional): Feature
         CreateReport (, Optional): Create Report
         ReportTitle (, Optional): Report Title
         ImagesFormat (, Optional): Image format
       OUTPUTS:
         OutputFolder (, Optional): Report Output Path
         ExportToImages (, Optional): Export to images
         OutputFolderImages (, Optional): Output path for images"""
    with gp:
        return convertArcObjectToPythonObject(gp._gp.MapSeriesReport_ba(*gp_fixargs((InputBoundaryLayer, All_Or_Single_Or_Selected, TitleFieldName, HideInactiveTAs, ByID_Or_ByName, Single_Site, CreateReport, ReportTitle, OutputFolder, ExportToImages, ImagesFormat, OutputFolderImages), True)))
@gptooldoc('PCACustomerProspecting_ba', None)
def PCACustomerProspecting(InputBoundaryLayer=None, InputGeographyLevel=None, OutputFeatureClass=None, DMQFile=None, FSRankFeatNum=None, UserDefinedBoundVal=None):
    """PCACustomerProspecting_ba(InputBoundaryLayer, InputGeographyLevel, OutputFeatureClass, DMQFile, FSRankFeatNum, {UserDefinedBoundVal})
       
       Profiles demographic attributes of customer data based on a selected demographic or custom data layer using the Principal Component Analysis approach.
       
       INPUTS:
         InputBoundaryLayer (, Required): Analysis Extent
         InputGeographyLevel (, Required): Geography Level
         DMQFile (, Required): Input Demographic Query File
         FSRankFeatNum (, Required): Number of Features to Rank
         UserDefinedBoundVal (, Optional): Boundary PCA Eigenvalue
       OUTPUT:
         OutputFeatureClass (, Required): Output Feature Class"""
    with gp:
        return convertArcObjectToPythonObject(gp._gp.PCACustomerProspecting_ba(*gp_fixargs((InputBoundaryLayer, InputGeographyLevel, OutputFeatureClass, DMQFile, FSRankFeatNum, UserDefinedBoundVal), True)))
