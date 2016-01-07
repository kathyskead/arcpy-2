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
"""
Contains the implementation of the graph classes.
"""

__all__ = [
    "Graph",
    "GraphTemplate"
    ]

from _base import _NamedAttrObject
from geoprocessing import gp
import arcgisscripting
from uuid import uuid1
import numpy



#======= SERIES =============
class _SeriesArea(_NamedAttrObject):
    def __init__(self,
                 bVertical,
                 dataSrc,
                 fieldY = None,
                 fieldX = None,
                 fieldLabel = None,
                 sortType = None
                 ):

        _SeriesArea._make_readwrite("aType")
        self.aType = ("area:vertical" if bVertical else "area:horizontal")
        _SeriesArea._make_readonly("aType")
        self.dataSrc = dataSrc
        self.fieldY = fieldY
        self.fieldX = fieldX
        self.fieldLabel = fieldLabel
        self.sortType = sortType

_SeriesArea._add_attr("aType", "SERIES")
_SeriesArea._add_attr("dataSrc", "DATA")
_SeriesArea._add_attr("fieldY", "Y")
_SeriesArea._add_attr("fieldX", "X")
_SeriesArea._add_attr("fieldLabel", "LABEL")
_SeriesArea._add_attr("sortType", "SORT")

#==============================
class _SeriesLine(_NamedAttrObject):
    def __init__(self,
                 bVertical,
                 dataSrc,
                 fieldY = None,
                 fieldX = None,
                 fieldLabel = None,
                 sortType = None
                 ):

        _SeriesLine._make_readwrite("aType")
        self.aType = ("line:vertical" if bVertical else "line:horizontal")
        _SeriesLine._make_readonly("aType")
        self.dataSrc = dataSrc
        self.fieldY = fieldY
        self.fieldX = fieldX
        self.fieldLabel = fieldLabel
        self.sortType = sortType

_SeriesLine._add_attr("aType", "SERIES")
_SeriesLine._add_attr("dataSrc", "DATA")
_SeriesLine._add_attr("fieldY", "Y")
_SeriesLine._add_attr("fieldX", "X")
_SeriesLine._add_attr("fieldLabel", "LABEL")
_SeriesLine._add_attr("sortType", "SORT")

#==============================
class _SeriesBar(_NamedAttrObject):
    def __init__(self,
                 bVertical,
                 dataSrc,
                 fieldY = None,
                 fieldX = None,
                 fieldLabel = None,
                 sortType = None
                 ):

        _SeriesBar._make_readwrite("aType")
        self.aType = ("bar:vertical" if bVertical else "bar:horizontal")
        _SeriesBar._make_readonly("aType")
        self.dataSrc = dataSrc
        self.fieldY = fieldY
        self.fieldX = fieldX
        self.fieldLabel = fieldLabel
        self.sortType = sortType

_SeriesBar._add_attr("aType", "SERIES")
_SeriesBar._add_attr("dataSrc", "DATA")
_SeriesBar._add_attr("fieldY", "Y")
_SeriesBar._add_attr("fieldX", "X")
_SeriesBar._add_attr("fieldLabel", "LABEL")
_SeriesBar._add_attr("sortType", "SORT")

#==============================
class _SeriesBarMinMax(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldYMax,
                 fieldYMin,
                 fieldX = None,
                 fieldLabel = None,
                 sortType = None
                 ):

        self.dataSrc = dataSrc
        self.fieldYMax = fieldYMax
        self.fieldYMin = fieldYMin
        self.fieldX = fieldX
        self.fieldLabel = fieldLabel
        self.sortType = sortType

_SeriesBarMinMax._add_attr("aType", "SERIES", "bar:minmax", True)
_SeriesBarMinMax._add_attr("dataSrc", "DATA")
_SeriesBarMinMax._add_attr("fieldYMax", "YMAX")
_SeriesBarMinMax._add_attr("fieldYMin", "YMIN")
_SeriesBarMinMax._add_attr("fieldX", "X")
_SeriesBarMinMax._add_attr("fieldLabel", "LABEL")
_SeriesBarMinMax._add_attr("sortType", "SORT")

#==============================
class _SeriesHistogram(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldValue,
                 countBin = None
                 ):

        self.dataSrc = dataSrc
        self.fieldValue = fieldValue
        self.countBin = countBin

_SeriesHistogram._add_attr("aType", "SERIES", "bar:histogram", True)
_SeriesHistogram._add_attr("dataSrc", "DATA")
_SeriesHistogram._add_attr("fieldValue", "VALUE")
_SeriesHistogram._add_attr("countBin", "BIN")

#==============================
class _SeriesScatterPlot(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldY,
                 fieldX = None,
                 fieldLabel = None
                 ):

        self.dataSrc = dataSrc
        self.fieldX = fieldX
        self.fieldY = fieldY
        self.fieldLabel = fieldLabel

_SeriesScatterPlot._add_attr("aType", "SERIES", "scatter_plot", True)
_SeriesScatterPlot._add_attr("dataSrc", "DATA")
_SeriesScatterPlot._add_attr("fieldX", "X")
_SeriesScatterPlot._add_attr("fieldY", "Y")
_SeriesScatterPlot._add_attr("fieldLabel", "LABEL")

#==============================
class _SeriesBoxPlot(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldValue,
                 ):

        self.dataSrc = dataSrc
        self.fieldValue = fieldValue

_SeriesBoxPlot._add_attr("aType", "SERIES", "box_plot", True)
_SeriesBoxPlot._add_attr("dataSrc", "DATA")
_SeriesBoxPlot._add_attr("fieldValue", "Value")

#==============================
class _SeriesBubble(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldRadius,
                 fieldY,
                 fieldX = None,
                 fieldLabel = None
                 ):

        self.dataSrc = dataSrc
        self.fieldRadius = fieldRadius
        self.fieldY = fieldY
        self.fieldX = fieldX
        self.fieldLabel = fieldLabel

_SeriesBubble._add_attr("aType", "SERIES", "bubble", True)
_SeriesBubble._add_attr("dataSrc", "DATA")
_SeriesBubble._add_attr("fieldRadius", "RADIUS")
_SeriesBubble._add_attr("fieldY", "Y")
_SeriesBubble._add_attr("fieldX", "X")
_SeriesBubble._add_attr("fieldLabel", "LABEL")

#==============================
class _SeriesPolar(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldRadius,
                 fieldAngle = None,
                 fieldLabel = None
                 ):

        self.dataSrc = dataSrc
        self.fieldRadius = fieldRadius
        self.fieldAngle = fieldAngle
        self.fieldLabel = fieldLabel

_SeriesPolar._add_attr("aType", "SERIES", "polar", True)
_SeriesPolar._add_attr("dataSrc", "DATA")
_SeriesPolar._add_attr("fieldRadius", "RADIUS")
_SeriesPolar._add_attr("fieldAngle", "ANGLE")
_SeriesPolar._add_attr("fieldLabel", "LABEL")

#==============================
class _SeriesPie(_NamedAttrObject):
    def __init__(self,
                 dataSrc,
                 fieldValue,
                 fieldSort = None,
                 fieldLabel = None,
                 sortType = None
                 ):

        self.dataSrc = dataSrc
        self.fieldValue = fieldValue
        self.fieldSort = fieldSort
        self.fieldLabel = fieldLabel
        self.sortType = sortType

_SeriesPie._add_attr("aType", "SERIES", "pie", True)
_SeriesPie._add_attr("dataSrc", "DATA")
_SeriesPie._add_attr("fieldValue", "VALUE")
_SeriesPie._add_attr("fieldSort", "SORT_FIELD")
_SeriesPie._add_attr("fieldLabel", "LABEL")
_SeriesPie._add_attr("sortType", "SORT")

#=======================================================================
#=======================================================================
#=======================================================================

#======= GENERAL =============
class _GraphPropsGeneral(_NamedAttrObject):
    def __init__(self,
                 title = None,
                 subtitle = None,
                 footer = None,
                 ):
        self.title = title
        self.subtitle = subtitle
        self.footer = footer

_GraphPropsGeneral._add_attr("aType", "GRAPH", "general", True)
_GraphPropsGeneral._add_attr("title", "TITLE")
_GraphPropsGeneral._add_attr("subtitle", "SUBTITLE")
_GraphPropsGeneral._add_attr("footer", "FOOTER")

#======= LEGEND =============
class _GraphPropsLegend(_NamedAttrObject):
    def __init__(self,
                 title = None
                 ):
        self.title = title

_GraphPropsLegend._add_attr("aType", "LEGEND", "general", True)
_GraphPropsLegend._add_attr("title", "TITLE")

#======= AXIS =============
class _GraphPropsAxis(_NamedAttrObject):
    def __init__(self,
                 type,
                 title = None
                 ):
        _GraphPropsAxis._make_readwrite("aType")
        self.aType = type
        _GraphPropsAxis._make_readonly("aType")
        self.title = title

_GraphPropsAxis._add_attr("aType", "AXIS")
_GraphPropsAxis._add_attr("title", "TITLE")

#=======================================================================
#=======================================================================
#=======================================================================

#======= GRAPH =============
from arcpy.geoprocessing._base import gptooldoc

class Graph(object):
    """The Graph class helps you in creating graphs of different types. Also,
       you can specify general graph properties such as the title, graph axes,
       and legend information."""
    def __init__(self):
        self.graphSeries = []
        self.graphAxis = [_GraphPropsAxis("left"), _GraphPropsAxis("right"), _GraphPropsAxis("bottom"), _GraphPropsAxis("top")]
        self.graphPropsGeneral = _GraphPropsGeneral()
        self.graphPropsLegend = _GraphPropsLegend()
        self._tempData = []
        self._scratch_workspace = None

    def __del__(self):
        for tempData in self._tempData :
            if tempData != None :
                gp.delete(tempData)
        if self._scratch_workspace != None :
            gp.delete(self._scratch_workspace)

    def __repr__(self):
        strRes = ""
        for series in self.graphSeries:
            if strRes != "":
                strRes += ";"
            strRes += str(series)

        strRes += ";"
        strRes += str(self.graphPropsGeneral)

        strRes += ";"
        strRes += str(self.graphPropsLegend)

        for axis in self.graphAxis:
            strRes += ";"
            strRes += str(axis)

        return strRes.rstrip()

    def __str__(self):
        return self.__repr__()

    @property
    def _arc_object(self):
        return str(self)

    #==============================================
    def addSeriesAreaVertical(self, dataSrc, fieldY, fieldX = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesAreaVertical(dataSrc, fieldY, {fieldX}, {fieldLabel},
           {sortType})

           Creates a new Vertical Area series that can be added to the graph.

           Learn more about Vertical Area graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldY(Field):
           The attribute field that will be used to plot value along the Y-axis
           of the Vertical Area graph.

             fieldX{Field}:
           The attribute field that will be used to plot value along the X-axis
           of the Vertical Area graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the vertical area in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the X-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesArea(True, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesAreaVertical.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesAreaHorizontal(self, dataSrc, fieldX, fieldY = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesAreaHorizontal(dataSrc, fieldX, {fieldY},
           {fieldLabel}, {sortType})

           Creates a new Horizontal Area series that can be added to the graph.

           Learn more about Horizontal Area graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldX(Field):
           The attribute field that will be used to plot value along the X-axis
           of the Horizontal Area graph.

             fieldY{Field}:
           The attribute field that will be used to plot value along the Y-axis
           of the Horizontal Area graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the horizontal area in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the Y-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesArea(False, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesAreaHorizontal.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesLineVertical(self, dataSrc, fieldY, fieldX = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesLineVertical(dataSrc, fieldY, {fieldX}, {fieldLabel},
           {sortType})

           Creates a new Vertical Line series that can be added to the graph.

           Learn more about Vertical Line graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldY(Field):
           The attribute field that will be used to plot value along the Y-axis
           of the Vertical Line graph.

             fieldX{Field}:
           The attribute field that will be used to plot value along the X-axis
           of the Vertical Line graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the vertical line in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the X-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesLine(True, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesLineVertical.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesLineHorizontal(self, dataSrc, fieldX, fieldY = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesLineHorizontal(dataSrc, fieldX, {fieldY},
           {fieldLabel}, {sortType})

           Creates a new Horizontal Line series that can be added to the graph.

           Learn more about Horizontal Line graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldX(Field):
           The attribute field that will be used to plot value along the X-axis
           of the Horizontal Line graph.

             fieldY{Field}:
           The attribute field that will be used to plot value along the Y-axis
           of the Horizontal Line graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the horizontal line in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the Y-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesLine(False, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesLineHorizontal.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesBarVertical(self, dataSrc, fieldY, fieldX = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesBarVertical(dataSrc, fieldY, {fieldX}, {fieldLabel},
           {sortType})

           Creates a new Vertical Bar series that can be added to the graph.

           Learn more about Vertical Bar graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldY(Field):
           The attribute field that will be used to plot values along the Y-axis
           of the Vertical Bar graph.

             fieldX{Field}:
           The attribute field that will be used to plot values along the X-axis
           of the Vertical Bar graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the vertical bars in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the X-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        if type(dataSrc) == numpy.ndarray :
            (dataSrc, fieldX, fieldY, fieldLabel) = self._NumpyToTable(dataSrc, [fieldX, fieldY, fieldLabel], ['fld_x', 'fld_y', 'fld_label'])

        self.graphSeries.append(_SeriesBar(True, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesBarVertical.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesBarHorizontal(self, dataSrc, fieldX, fieldY = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesBarHorizontal(dataSrc, fieldX, {fieldY}, {fieldLabel},
           {sortType})

           Creates a new Horizontal Bar series that can be added to the graph.

           Learn more about Horizontal Bar graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldX(Field):
           The attribute field that will be used to plot value along the X-axis
           of the Horizontal Bar graph.

             fieldY{Field}:
           The attribute field that will be used to plot value along the Y-axis
           of the Horizontal Bar graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the horizontal bars in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the Y-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table.  This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesBar(False, dataSrc, fieldY, fieldX, fieldLabel, sortType))

    addSeriesBarHorizontal.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesBarMinMax(self, dataSrc, fieldYMax, fieldYMin, fieldX = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesBarMinMax(dataSrc, fieldYMax, fieldYMin, {fieldX},
           {fieldLabel}, {sortType})

           Creates a new Bar Min and Max series that can be added to the graph.

           Learn more about Bar Min and Max graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldYMax(Field):
           The attribute field that will be used to plot the maximum value along
           the Y-axis of the Bar Min and Max graph.

             fieldYMin(Field):
           The attribute field that will be used to plot the minimum value along
           the Y-axis of the Bar Min and Max graph.

             fieldX{Field}:
           The attribute field that will be used to plot value along the X-axis
           of the Bar Min and Max graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           along the bars in the graph.

             sortType{String}:
           Specify how the data values in the attribute field used for defining
           the X-axis will be sorted.

            * VALUE:  Sort the  data values based on the order of values in the
            input layer or table. This is the default.

            * ASC:  Sort the data values in ascending order (lowest to highest).

            * DESC:  Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesBarMinMax(dataSrc, fieldYMax, fieldYMin, fieldX, fieldLabel, sortType))

    addSeriesBarMinMax.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::VALUE|ASC|DESC:"
            ]

    #==============================================
    def addSeriesHistogram(self, dataSrc, fieldValue, countBin = None):
        """Graph.addSeriesHistogram(dataSrc, fieldValue, countBin)

           Creates a new Histogram series that can be added to the graph.

           Learn more about Histogram graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldValue(Field):
           The attribute field used for displaying the frequency distribution in
           the bins of the histogram. The height of the bars in a Histogram
           represent a frequency count of the number of
           items falling into each bin.

             countBin(Integer):
           The number of bins in the histogram."""
        self.graphSeries.append(_SeriesHistogram(dataSrc, fieldValue, countBin))

    addSeriesHistogram.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Long:::"
            ]

    #==============================================
    def addSeriesScatterPlot(self, dataSrc, fieldY, fieldX = None, fieldLabel = None):
        """Graph.addSeriesScatterPlot(dataSrc, fieldY, {fieldX}, {fieldLabel})

           Creates a new Scatterplot  series that can be added to the graph.

           Learn more about Scatterplot graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldY(Field):
           The attribute field that will be used to plot values along the Y-axis
           of the Scatterplot graph.

             fieldX{Field}:
           The attribute field that will be used to plot values along the X-axis
           of the Scatterplot graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           in the graph."""
        self.graphSeries.append(_SeriesScatterPlot(dataSrc, fieldY, fieldX, fieldLabel))

    addSeriesScatterPlot.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1"
            ]

    #==============================================
    def addSeriesBoxPlot(self, dataSrc, fieldValue):
        """Graph.addSeriesBoxPlot(dataSrc, fieldValue)

           Creates a new Box Plot series that can be added to the graph.

           Learn more about Box Plot graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldValue(Field):
           The attribute field used for plotting the values in the Box Plot
           graph."""
        self.graphSeries.append(_SeriesBoxPlot(dataSrc, fieldValue))

    addSeriesBoxPlot.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1"
            ]

    #==============================================
    def addSeriesBubble(self, dataSrc, fieldRadius, fieldY, fieldX = None, fieldLabel = None):
        """Graph.addSeriesBubble(dataSrc, fieldRadius, fieldY, {fieldX},
           {fieldLabel})

           Creates a new Bubble  series that can be added to the graph.

           Learn more about Bubble graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldRadius(Field):
           The attribute field that defines the radius of the bubbles in the
           Bubble graph.

             fieldY(Field):
           The attribute field that will be used to plot values along the Y-axis
           of the Bubble graph.

             fieldX{Field}:
           The attribute field that will be used to plot values along the X-axis
           of the Bubble graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels for data points
           in the graph."""
        self.graphSeries.append(_SeriesBubble(dataSrc, fieldRadius, fieldY, fieldX, fieldLabel))

    addSeriesBubble.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1"
            ]

    #==============================================
    def addSeriesPolar(self, dataSrc, fieldRadius, fieldAngle = None, fieldLabel = None):
        """Graph.addSeriesPolar(dataSrc, fieldRadius, {fieldAngle},
           {fieldLabel})

           Creates a new Polar  series that can be added to the graph.

           Learn more about Polar graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldRadius(Field):
           The attribute field whose values are  graphed on the radial axis of
           the Polar graph.

             fieldAngle{Field}:
           The attribute field that supplies the angular position for each data
           point in the Polar graph.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels representing
           data values on  the graph."""
        self.graphSeries.append(_SeriesPolar(dataSrc, fieldRadius, fieldAngle, fieldLabel))

    addSeriesPolar.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1"
            ]

    #==============================================
    def addSeriesPie(self, dataSrc, fieldValue, fieldSort = None, fieldLabel = None, sortType = None):
        """Graph.addSeriesPie(dataSrc, fieldValue, fieldSort, {fieldLabel},
           {sortType})

           Creates a new Pie  series that can be added to the graph.

           Learn more about Pie graphs

             dataSrc(Layer):
           The layer or table containing the data values that will be used to
           create the graph.

             fieldValue(Field):
           The attribute field that will be used to plot values or wedges in the
           Pie graph.

             fieldSort(Field):
           The attribute field that will be used to sort the wedges in an
           ascending or descending order.

             fieldLabel{Field}:
           The attribute field that will be used to plot labels in the Pie
           graph.

             sortType{String}:
           Specify how the data values will be sorted in the attribute field
           used for sorting.

            * ASC: Sort the data values in ascending order (lowest to highest).
            This is the default.

            * DESC: Sort the data values in descending order (highest to
            lowest)."""
        self.graphSeries.append(_SeriesPie(dataSrc, fieldValue, fieldSort, fieldLabel, sortType))

    addSeriesPie.__esri_toolinfo__ = [
            "TableView|FeatureLayer|RasterLayer:::",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date::1",
            "Field:Short|Long|Float|Double|Date|Text::1",
            "String::ASC|DESC:"
            ]

    def _NumpyToTable(self, inArray, fldNdxList, nameList) :
        # create field names if input array has none
        names = list(inArray.dtype.names)
        if names == None :
            nFields = len(inArray[0])
            for i in range(0, nFields):
                if i in fldNdxList :
                    names.append(nameList[fldNdxList.index(i)])
                else :
                    names.append('fld_' + str(i))
            inArray.dtype.names = tuple(names)

        #create scratch workspace
        if self._scratch_workspace == None :
            ags = arcgisscripting.create()
            self._scratch_workspace = ags.CreateFileGDB_management(gp.getSystemEnvironment("TEMP") + '\\', str(uuid1()) + '.gdb')
            del ags

        #create temp table name
        inTempData = gp.CreateScratchName('grf', None, None, self._scratch_workspace)
        self._tempData.append(inTempData)

        #save input array to temp table
        tmpTable = arcgisscripting.da.NumPyArrayToTable(inArray, inTempData)
        del tmpTable

        #return tuple with temp table and field names
        retData = [inTempData]
        for iFld in fldNdxList :
            if iFld >= 0 and iFld < len(names) :
                retData.append(names[iFld])
            else :
                retData.append(None)

        return tuple(retData)


class GraphTemplate(object):
    templateName = None
    def __init__(self,
             templateName = None
             ):
        self.templateName = templateName
        if self.templateName == None :
            self.templateName = gp.GetInstallInfo()['InstallDir'] + 'GraphTemplates\\default.tee'

    def __repr__(self):
        return self.templateName

    def __str__(self):
        return self.__repr__()

    @property
    def _arc_object(self):
        return str(self)

