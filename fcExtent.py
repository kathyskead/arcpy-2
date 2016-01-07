#--------------------------------------------------------------
# Purpose:     Creates a rectangle polygon feature class
#              around an existing feature class.
#
# Author:      
# Website:     
#
# Created:     04/28/2015
# Modified     
#
#--------------------------------------------------------------
import arcpy
from arcpy import env

env.overwriteOutput = True

# todo: get arg from inside arcmap toc fc
fc = r"c:\Temp\hotel.shp"
desc = arcpy.Describe(fc)
extent = desc.extent

pts = [arcpy.Point(extent.XMin, extent.YMin),
	   arcpy.Point(extent.XMax, extent.YMin),
	   arcpy.Point(extent.XMax, extent.YMax),
	   arcpy.Point(extent.XMin, extent.YMax)]

array = arcpy.Array(items = pts)
poly = arcpy.Polygon(array)

# todo: get arg for output fc.
arcpy.CopyFeatures_management(poly, r"%scratchgdb%\way1")


# Method for individual features using a cursor with extent XMin,
# YMin, XMax, and YMax, and arcpy.CreateFeatureClass().
import arcpy
from arcpy import env
env.overwriteOutput = True
fc = r"c:\States.shp"
out_fc = r"%scratchgdb%\way2"
if not arcpy.Exists(out_fc):
    arcpy.CreateFeatureclass_management(out_path="%scratchgdb%",
                                        out_name="way2", geometry_type="POLYGON",
                                        spatial_reference=arcpy.SpatialReference(4326))
icur = arcpy.da.InsertCursor(out_fc, "SHAPE@")
with arcpy.da.SearchCursor(fc, "SHAPE@") as rows:
    for row in rows:
        extent = row[0].extent
        pts = [arcpy.Point(extent.XMin, extent.YMin),
               arcpy.Point(extent.XMax, extent.YMin),
               arcpy.Point(extent.XMax, extent.YMax),
               arcpy.Point(extent.XMin, extent.YMax)]
        array = arcpy.Array(items=pts)
        poly = arcpy.Polygon(array)
        icur.insertRow([poly])
        del array
        del poly
        del pts
        del extent
        del row


# Method for individual features using a cursor and arcpy.CopyFeatures().
import arcpy
from arcpy import env
env.overwriteOutput = True
fc = r"c:\States.shp"
out_fc = r"%scratchgdb%\way3"
with arcpy.da.SearchCursor(fc, "SHAPE@") as rows:
    polys = []
    array = arcpy.Array()    
    for row in rows:
        extent = row[0].extent
        array.add(extent.lowerLeft)
        array.add(extent.lowerRight)
        array.add(extent.upperRight)
        array.add(extent.upperLeft)
        array.add(extent.lowerLeft)
        polys.append(arcpy.Polygon(array))
        array.removeAll()
        del row
    del array
    arcpy.CopyFeatures_management(polys, out_fc)
    del polys        