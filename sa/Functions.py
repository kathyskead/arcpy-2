# -*- coding: utf-8 -*-
# COPYRIGHT 1995-2014 ESRI
#
# TRADE SECRETS: ESRI PROPRIETARY AND CONFIDENTIAL
# Unpublished material - all rights reserved under the
# Copyright Laws of the United States.
#
# For additional information, contact:
# Environmental Systems Research Institute, Inc.
# Attn: Contracts Dept
# 380 New York Street
# Redlands, California, USA 92373
#
# email: contracts@esri.com
#
# Warning: This module is automatically generated, changes will be overwritten.
from arcgisscripting import _wrapToolRaster, _wrapLocalFunctionRaster
import arcpy
from . import ParameterClasses
from . import Utils

try:
    unicode
except NameError:
    unicode = str


__all__ = [
    "Con",
    "Pick",
    "SetNull",
    "KernelDensity",
    "LineDensity",
    "PointDensity",
    "Corridor",
    "CostAllocation",
    "CostBackLink",
    "CostDistance",
    "CostPath",
    "EucAllocation",
    "EucDirection",
    "EucDistance",
    "PathAllocation",
    "PathBackLink",
    "PathDistance",
    "ExtractByAttributes",
    "ExtractByCircle",
    "ExtractByPoints",
    "ExtractByPolygon",
    "ExtractByRectangle",
    "ExtractValuesToPoints",
    "Sample",
    "Aggregate",
    "BoundaryClean",
    "Expand",
    "MajorityFilter",
    "Nibble",
    "RegionGroup",
    "Shrink",
    "Thin",
    "DarcyFlow",
    "DarcyVelocity",
    "ParticleTrack",
    "PorousPuff",
    "Basin",
    "Fill",
    "FlowAccumulation",
    "FlowDirection",
    "FlowLength",
    "Sink",
    "SnapPourPoint",
    "StreamLink",
    "StreamOrder",
    "StreamToFeature",
    "Watershed",
    "Idw",
    "Kriging",
    "NaturalNeighbor",
    "Spline",
    "TopoToRaster",
    "TopoToRasterByFile",
    "Trend",
    "CellStatistics",
    "Combine",
    "EqualToFrequency",
    "GreaterThanFrequency",
    "HighestPosition",
    "LessThanFrequency",
    "LowestPosition",
    "Popularity",
    "Rank",
    "Abs",
    "BitwiseAnd",
    "BitwiseLeftShift",
    "BitwiseNot",
    "BitwiseOr",
    "BitwiseRightShift",
    "BitwiseXOr",
    "Divide",
    "Exp",
    "Exp10",
    "Exp2",
    "Float",
    "Int",
    "Ln",
    "Log10",
    "Log2",
    "BooleanAnd",
    "BooleanNot",
    "BooleanOr",
    "BooleanXOr",
    "CombinatorialAnd",
    "CombinatorialOr",
    "CombinatorialXOr",
    "EqualTo",
    "GreaterThan",
    "GreaterThanEqual",
    "IsNull",
    "LessThan",
    "LessThanEqual",
    "NotEqual",
    "Test",
    "Minus",
    "Mod",
    "Negate",
    "Plus",
    "Power",
    "RoundDown",
    "RoundUp",
    "Square",
    "SquareRoot",
    "Times",
    "ACos",
    "ACosH",
    "ASin",
    "ASinH",
    "ATan",
    "ATan2",
    "ATanH",
    "Cos",
    "CosH",
    "Sin",
    "SinH",
    "Tan",
    "TanH",
    "BandCollectionStats",
    "ClassProbability",
    "CreateSignatures",
    "Dendrogram",
    "EditSignatures",
    "IsoCluster",
    "MLClassify",
    "PrincipalComponents",
    "BlockStatistics",
    "Filter",
    "FocalFlow",
    "FocalStatistics",
    "LineStatistics",
    "PointStatistics",
    "WeightedOverlay",
    "CreateConstantRaster",
    "CreateNormalRaster",
    "CreateRandomRaster",
    "Lookup",
    "ReclassByASCIIFile",
    "ReclassByTable",
    "Reclassify",
    "Slice",
    "Aspect",
    "Contour",
    "ContourList",
    "Hillshade",
    "ObserverPoints",
    "Slope",
    "Viewshed",
    "TabulateArea",
    "ZonalFill",
    "ZonalGeometry",
    "ZonalGeometryAsTable",
    "ZonalStatistics",
    "ZonalStatisticsAsTable",
    "AreaSolarRadiation",
    "PointsSolarRadiation",
    "SolarRadiationGraphics",
    "WeightedSum",
    "Diff",
    "InList",
    "Over",
    "ContourWithBarriers",
    "FuzzyMembership",
    "FuzzyOverlay",
    "IsoClusterUnsupervisedClassification",
    "ZonalHistogram",
    "CutFill",
    "ExtractByMask",
    "SplineWithBarriers",
    "Curvature",
    "ExtractMultiValuesToPoints",
    "Visibility",
    "RescaleByFunction",
    "Viewshed2",
    "ClassifyRaster",
    "ComputeSegmentAttributes",
    "SegmentMeanShift",
    "TrainMaximumLikelihoodClassifier",
    "TrainIsoClusterClassifier",
    "TrainSupportVectorMachineClassifier",
    "ApplyEnvironment",
    "FloatDivide",
    "FloorDivide"
]


def Con(
        in_conditional_raster,
        in_true_raster_or_constant,
        in_false_raster_or_constant="#",
        where_clause="#"):
    """Con(in_conditional_raster, in_true_raster_or_constant, {in_false_raster_or_constant}, {where_clause})

    Performs a conditional if/else evaluation on each of the input cells of an input raster.

    Arguments:
    in_conditional_raster -- Input raster representing the true or false result of the desired condition.
    in_true_raster_or_constant -- The input whose values will be used as the output cell values if the condition is true.
    in_false_raster_or_constant -- The input whose values will be used as the output cell values if the condition is false.
    where_clause -- A logical expression that determines which of the input cells are to be true or false.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_conditional_raster,
            in_true_raster_or_constant,
            in_false_raster_or_constant,
            where_clause):
        if Utils.useDefaultArgumentValue(where_clause):
            if Utils.useDefaultArgumentValue(in_false_raster_or_constant):
                return _wrapLocalFunctionRaster(u"Con_sa",
                    ["IfThen", in_conditional_raster, in_true_raster_or_constant])
            else:
                return _wrapLocalFunctionRaster(u"Con_sa",
                    ["IfThenElse", in_conditional_raster, in_true_raster_or_constant, in_false_raster_or_constant])
        out_raster = "#"
        result = arcpy.gp.Con_sa(
            in_conditional_raster,
            in_true_raster_or_constant,
            out_raster,
            in_false_raster_or_constant,
            where_clause)
        return _wrapToolRaster(u"Con_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_conditional_raster,
        in_true_raster_or_constant,
        in_false_raster_or_constant,
        where_clause)
Con.__esri_toolname__ = "Con_sa"
Con.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5"
]


def Pick(
        in_position_raster,
        in_rasters_or_constants):
    """Pick(in_position_raster, [in_raster_or_constant,...])

    The value from a position raster is used to determine from which raster in a list of input rasters the output cell value will be obtained.

    Arguments:
    in_position_raster -- Input raster defining the position of the raster to use for the output value.
    in_raster_or_constant -- The list of inputs from which the output value will be selected.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_position_raster,
            in_rasters_or_constants):
        out_raster = "#"
        result = arcpy.gp.Pick_sa(
            in_position_raster,
            in_rasters_or_constants,
            out_raster)
        return _wrapToolRaster(u"Pick_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_position_raster,
        in_rasters_or_constants)
Pick.__esri_toolname__ = "Pick_sa"
Pick.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def SetNull(
        in_conditional_raster,
        in_false_raster_or_constant,
        where_clause="#"):
    """SetNull(in_conditional_raster, in_false_raster_or_constant, {where_clause})

    Set Null sets identified cell locations to NoData based on a specified criteria.  It returns NoData if a conditional evaluation is true, and returns the value specified by another raster if it is false.

    Arguments:
    in_conditional_raster -- Input raster representing the true or false result of the desired condition.
    in_false_raster_or_constant -- The input whose values will be used as the output cell values if the condition is false.
    where_clause -- A logical expression that determines which of the input cells are to be true or false.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_conditional_raster,
            in_false_raster_or_constant,
            where_clause):
        if Utils.useDefaultArgumentValue(where_clause):
            return _wrapLocalFunctionRaster(u"SetNull_sa",
                ["SetNull", in_conditional_raster, in_false_raster_or_constant])
        out_raster = "#"
        result = arcpy.gp.SetNull_sa(
            in_conditional_raster,
            in_false_raster_or_constant,
            out_raster,
            where_clause)
        return _wrapToolRaster(u"SetNull_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_conditional_raster,
        in_false_raster_or_constant,
        where_clause)
SetNull.__esri_toolname__ = "SetNull_sa"
SetNull.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def KernelDensity(
        in_features,
        population_field,
        cell_size="#",
        search_radius="#",
        area_unit_scale_factor="#",
        out_cell_values="#",
        method="#"):
    """KernelDensity(in_features, population_field, {cell_size}, {search_radius}, {area_unit_scale_factor}, {out_cell_values}, {method})

    Calculates a magnitude-per-unit area from point or polyline features using a kernel function to fit a smoothly tapered surface to each point or polyline.

    Arguments:
    in_features -- The input features (point or line) for which to calculate the density.
    population_field -- Field denoting population values for each feature. The population
field is the count or quantity to be spread across the landscape to
create a continuous surface.
    cell_size -- The cell size for the output raster dataset.
    search_radius -- The search radius within which to calculate density. Units are based on the linear unit of the projection of the output spatial reference.
    area_unit_scale_factor -- The desired area units of the output density values.
    out_cell_values -- Determines what the values in the output raster represent.
    method -- Determines whether to use a shortest path on a spheroid (geodesic) or a flat earth (planar) method. It is strongly suggested to use the geodesic method with data stored in a coordinate system that is not appropriate for distance measurements (for example, Web Mercator or any geographic coordinate system) and any analysis that spans a large geographic area.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_features,
            population_field,
            cell_size,
            search_radius,
            area_unit_scale_factor,
            out_cell_values,
            method):
        out_raster = "#"
        result = arcpy.gp.KernelDensity_sa(
            in_features,
            population_field,
            out_raster,
            cell_size,
            search_radius,
            area_unit_scale_factor,
            out_cell_values,
            method)
        return _wrapToolRaster(u"KernelDensity_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_features,
        population_field,
        cell_size,
        search_radius,
        area_unit_scale_factor,
        out_cell_values,
        method)
KernelDensity.__esri_toolname__ = "KernelDensity_sa"
KernelDensity.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8"
]


def LineDensity(
        in_polyline_features,
        population_field,
        cell_size="#",
        search_radius="#",
        area_unit_scale_factor="#"):
    """LineDensity(in_polyline_features, population_field, {cell_size}, {search_radius}, {area_unit_scale_factor})

    Calculates a magnitude-per-unit area from polyline features that fall within a radius around each cell.

    Arguments:
    in_polyline_features -- The input line features for which to calculate the density.
    population_field -- Numeric field denoting population values (the number of times the line should be counted) for each polyline.
    cell_size -- The cell size for the output raster dataset.
    search_radius -- The search radius within which to calculate density. Units are based on the linear unit of the projection of the output spatial reference.
    area_unit_scale_factor -- The desired area units of the output density values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_polyline_features,
            population_field,
            cell_size,
            search_radius,
            area_unit_scale_factor):
        out_raster = "#"
        result = arcpy.gp.LineDensity_sa(
            in_polyline_features,
            population_field,
            out_raster,
            cell_size,
            search_radius,
            area_unit_scale_factor)
        return _wrapToolRaster(u"LineDensity_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_polyline_features,
        population_field,
        cell_size,
        search_radius,
        area_unit_scale_factor)
LineDensity.__esri_toolname__ = "LineDensity_sa"
LineDensity.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6"
]


def PointDensity(
        in_point_features,
        population_field,
        cell_size="#",
        neighborhood="#",
        area_unit_scale_factor="#"):
    """PointDensity(in_point_features, population_field, {cell_size}, {neighborhood}, {area_unit_scale_factor})

    Calculates a magnitude-per-unit area from point features that fall within a neighborhood around each cell.

    Arguments:
    in_point_features -- The input point features for which to calculate the density.
    population_field -- Field denoting population values for each point. The population
field is the count or quantity to be used in the calculation of a
continuous surface.
    cell_size -- The cell size for the output raster dataset.
    neighborhood -- Dictates the shape of the area around each cell used to calculate the density value.
    area_unit_scale_factor -- The desired area units of the output density values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            population_field,
            cell_size,
            neighborhood,
            area_unit_scale_factor):
        neighborhood = Utils.compoundParameterToString(neighborhood, ParameterClasses._Neighborhood)
        out_raster = "#"
        result = arcpy.gp.PointDensity_sa(
            in_point_features,
            population_field,
            out_raster,
            cell_size,
            neighborhood,
            area_unit_scale_factor)
        return _wrapToolRaster(u"PointDensity_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        population_field,
        cell_size,
        neighborhood,
        area_unit_scale_factor)
PointDensity.__esri_toolname__ = "PointDensity_sa"
PointDensity.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "Python::NbrAnnulus|NbrCircle|NbrRectangle|NbrWedge::",
    "::::6"
]


def Corridor(
        in_distance_raster1,
        in_distance_raster2):
    """Corridor(in_distance_raster1, in_distance_raster2)

    Calculates the sum of accumulative costs for two input accumulative cost rasters.

    Arguments:
    in_distance_raster1 -- The first input distance raster.
    in_distance_raster2 -- The second input distance raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_distance_raster1,
            in_distance_raster2):
        out_raster = "#"
        result = arcpy.gp.Corridor_sa(
            in_distance_raster1,
            in_distance_raster2,
            out_raster)
        return _wrapToolRaster(u"Corridor_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_distance_raster1,
        in_distance_raster2)
Corridor.__esri_toolname__ = "Corridor_sa"
Corridor.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def CostAllocation(
        in_source_data,
        in_cost_raster,
        maximum_distance="#",
        in_value_raster="#",
        source_field="#",
        out_distance_raster="#",
        out_backlink_raster="#"):
    """CostAllocation(in_source_data, in_cost_raster, {maximum_distance}, {in_value_raster}, {source_field}, {out_distance_raster}, {out_backlink_raster})

    Calculates for each cell its nearest source based on the least accumulative cost over a cost surface.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    in_value_raster -- The input integer raster that identifies the zone values that should be used for each input source location.
    source_field -- The field used to assign values to the source locations. It must be integer type.
    out_distance_raster -- The output cost distance raster.
    out_backlink_raster -- The output cost back-link raster.

    Results:
    out_allocation_raster -- Output allocation raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            maximum_distance,
            in_value_raster,
            source_field,
            out_distance_raster,
            out_backlink_raster):
        out_allocation_raster = "#"
        result = arcpy.gp.CostAllocation_sa(
            in_source_data,
            in_cost_raster,
            out_allocation_raster,
            maximum_distance,
            in_value_raster,
            source_field,
            out_distance_raster,
            out_backlink_raster)
        return _wrapToolRaster(u"CostAllocation_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        maximum_distance,
        in_value_raster,
        source_field,
        out_distance_raster,
        out_backlink_raster)
CostAllocation.__esri_toolname__ = "CostAllocation_sa"
CostAllocation.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8"
]


def CostBackLink(
        in_source_data,
        in_cost_raster,
        maximum_distance="#",
        out_distance_raster="#"):
    """CostBackLink(in_source_data, in_cost_raster, {maximum_distance}, {out_distance_raster})

    Defines the neighbor that is the next cell on the least accumulative cost path to the nearest source.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    out_distance_raster -- The output cost distance raster.

    Results:
    out_backlink_raster -- Output backlink raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            maximum_distance,
            out_distance_raster):
        out_backlink_raster = "#"
        result = arcpy.gp.CostBackLink_sa(
            in_source_data,
            in_cost_raster,
            out_backlink_raster,
            maximum_distance,
            out_distance_raster)
        return _wrapToolRaster(u"CostBackLink_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        maximum_distance,
        out_distance_raster)
CostBackLink.__esri_toolname__ = "CostBackLink_sa"
CostBackLink.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5"
]


def CostDistance(
        in_source_data,
        in_cost_raster,
        maximum_distance="#",
        out_backlink_raster="#"):
    """CostDistance(in_source_data, in_cost_raster, {maximum_distance}, {out_backlink_raster})

    Calculates the least accumulative cost distance for each cell to the nearest source over a cost surface.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    out_backlink_raster -- The output cost back-link raster.

    Results:
    out_distance_raster -- Output distance raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            maximum_distance,
            out_backlink_raster):
        out_distance_raster = "#"
        result = arcpy.gp.CostDistance_sa(
            in_source_data,
            in_cost_raster,
            out_distance_raster,
            maximum_distance,
            out_backlink_raster)
        return _wrapToolRaster(u"CostDistance_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        maximum_distance,
        out_backlink_raster)
CostDistance.__esri_toolname__ = "CostDistance_sa"
CostDistance.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5"
]


def CostPath(
        in_destination_data,
        in_cost_distance_raster,
        in_cost_backlink_raster,
        path_type="#",
        destination_field="#"):
    """CostPath(in_destination_data, in_cost_distance_raster, in_cost_backlink_raster, {path_type}, {destination_field})

    Calculates the least-cost path from a source to a destination.

    Arguments:
    in_destination_data -- A raster or feature dataset that identifies those cells from which the least-cost path is determined to the least costly source.
    in_cost_distance_raster -- The name of a cost distance raster to be used to determine the least-cost path from the destination locations to a source.
    in_cost_backlink_raster -- The name of a cost back link raster used to determine the path to return to a source via the least-cost path.
    path_type -- A keyword defining the manner in which the values and zones on the input destination data will be interpreted in the cost path calculations.
    destination_field -- The field used to obtain values for the destination locations.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_destination_data,
            in_cost_distance_raster,
            in_cost_backlink_raster,
            path_type,
            destination_field):
        out_raster = "#"
        result = arcpy.gp.CostPath_sa(
            in_destination_data,
            in_cost_distance_raster,
            in_cost_backlink_raster,
            out_raster,
            path_type,
            destination_field)
        return _wrapToolRaster(u"CostPath_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_destination_data,
        in_cost_distance_raster,
        in_cost_backlink_raster,
        path_type,
        destination_field)
CostPath.__esri_toolname__ = "CostPath_sa"
CostPath.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::5",
    "::::6"
]


def EucAllocation(
        in_source_data,
        maximum_distance="#",
        in_value_raster="#",
        cell_size="#",
        source_field="#",
        out_distance_raster="#",
        out_direction_raster="#"):
    """EucAllocation(in_source_data, {maximum_distance}, {in_value_raster}, {cell_size}, {source_field}, {out_distance_raster}, {out_direction_raster})

    Calculates, for each cell, the nearest source based on Euclidean distance.

    Arguments:
    in_source_data -- The input source locations.
    maximum_distance -- Defines the threshold that the accumulative distance values cannot exceed.
    in_value_raster -- The input integer raster that identifies the zone values that should be used for each input source location.
    cell_size -- The cell size at which the output raster will be created.
    source_field -- The field used to assign values to the source locations. It must be integer type.
    out_distance_raster -- The output Euclidean distance raster.
    out_direction_raster -- The output Euclidean direction raster.

    Results:
    out_allocation_raster -- Output allocation raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            maximum_distance,
            in_value_raster,
            cell_size,
            source_field,
            out_distance_raster,
            out_direction_raster):
        out_allocation_raster = "#"
        result = arcpy.gp.EucAllocation_sa(
            in_source_data,
            out_allocation_raster,
            maximum_distance,
            in_value_raster,
            cell_size,
            source_field,
            out_distance_raster,
            out_direction_raster)
        return _wrapToolRaster(u"EucAllocation_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        maximum_distance,
        in_value_raster,
        cell_size,
        source_field,
        out_distance_raster,
        out_direction_raster)
EucAllocation.__esri_toolname__ = "EucAllocation_sa"
EucAllocation.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8"
]


def EucDirection(
        in_source_data,
        maximum_distance="#",
        cell_size="#",
        out_distance_raster="#"):
    """EucDirection(in_source_data, {maximum_distance}, {cell_size}, {out_distance_raster})

    Calculates, for each cell, the direction, in degrees, to the nearest source.

    Arguments:
    in_source_data -- The input source locations.
    maximum_distance -- Defines the threshold that the accumulative distance values cannot exceed.
    cell_size -- The cell size at which the output raster will be created.
    out_distance_raster -- The output Euclidean distance raster.

    Results:
    out_direction_raster -- Output direction raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            maximum_distance,
            cell_size,
            out_distance_raster):
        out_direction_raster = "#"
        result = arcpy.gp.EucDirection_sa(
            in_source_data,
            out_direction_raster,
            maximum_distance,
            cell_size,
            out_distance_raster)
        return _wrapToolRaster(u"EucDirection_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        maximum_distance,
        cell_size,
        out_distance_raster)
EucDirection.__esri_toolname__ = "EucDirection_sa"
EucDirection.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5"
]


def EucDistance(
        in_source_data,
        maximum_distance="#",
        cell_size="#",
        out_direction_raster="#"):
    """EucDistance(in_source_data, {maximum_distance}, {cell_size}, {out_direction_raster})

    Calculates, for each cell, the Euclidean distance to the closest source.

    Arguments:
    in_source_data -- The input source locations.
    maximum_distance -- Defines the threshold that the accumulative distance values cannot exceed.
    cell_size -- The cell size at which the output raster will be created.
    out_direction_raster -- The output Euclidean direction raster.

    Results:
    out_distance_raster -- Output distance raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            maximum_distance,
            cell_size,
            out_direction_raster):
        out_distance_raster = "#"
        result = arcpy.gp.EucDistance_sa(
            in_source_data,
            out_distance_raster,
            maximum_distance,
            cell_size,
            out_direction_raster)
        return _wrapToolRaster(u"EucDistance_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        maximum_distance,
        cell_size,
        out_direction_raster)
EucDistance.__esri_toolname__ = "EucDistance_sa"
EucDistance.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5"
]


def PathAllocation(
        in_source_data,
        in_cost_raster="#",
        in_surface_raster="#",
        in_horizontal_raster="#",
        horizontal_factor="#",
        in_vertical_raster="#",
        vertical_factor="#",
        maximum_distance="#",
        in_value_raster="#",
        source_field="#",
        out_distance_raster="#",
        out_backlink_raster="#"):
    """PathAllocation(in_source_data, {in_cost_raster}, {in_surface_raster}, {in_horizontal_raster}, {horizontal_factor}, {in_vertical_raster}, {vertical_factor}, {maximum_distance}, {in_value_raster}, {source_field}, {out_distance_raster}, {out_backlink_raster})

    Calculates the nearest source for each cell based on the least accumulative cost over a cost surface, while accounting for surface distance and horizontal and vertical cost factors.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    in_surface_raster -- A raster defining the elevation values at each cell location.
    in_horizontal_raster -- A raster defining the horizontal direction at each cell.
    horizontal_factor -- The Horizontal Factor object defines the relationship between the horizontal cost factor and the horizontal relative moving angle.
    in_vertical_raster -- A raster defining the z-values for each cell location.
    vertical_factor -- The Vertical factor object defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA).
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    in_value_raster -- The input integer raster that identifies the zone values that should be used for each input source location.
    source_field -- The field used to assign values to the source locations. It must be integer type.
    out_distance_raster -- The output path distance raster.
    out_backlink_raster -- The output cost back-link raster.

    Results:
    out_allocation_raster -- Output allocation raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            in_value_raster,
            source_field,
            out_distance_raster,
            out_backlink_raster):
        horizontal_factor = Utils.compoundParameterToString(horizontal_factor, ParameterClasses._HorizontalFactor)
        vertical_factor = Utils.compoundParameterToString(vertical_factor, ParameterClasses._VerticalFactor)
        out_allocation_raster = "#"
        result = arcpy.gp.PathAllocation_sa(
            in_source_data,
            out_allocation_raster,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            in_value_raster,
            source_field,
            out_distance_raster,
            out_backlink_raster)
        return _wrapToolRaster(u"PathAllocation_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        in_surface_raster,
        in_horizontal_raster,
        horizontal_factor,
        in_vertical_raster,
        vertical_factor,
        maximum_distance,
        in_value_raster,
        source_field,
        out_distance_raster,
        out_backlink_raster)
PathAllocation.__esri_toolname__ = "PathAllocation_sa"
PathAllocation.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "Python::HfBinary|HfForward|HfInverseLinear|HfLinear|HfTable::",
    "::::7",
    "Python::VfBinary|VfCos|VfCosSec|VfInverseLinear|VfLinear|VfSec|VfSecCos|VfSymInverseLinear|VfSymLinear|VfTable::",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13"
]


def PathBackLink(
        in_source_data,
        in_cost_raster="#",
        in_surface_raster="#",
        in_horizontal_raster="#",
        horizontal_factor="#",
        in_vertical_raster="#",
        vertical_factor="#",
        maximum_distance="#",
        out_distance_raster="#"):
    """PathBackLink(in_source_data, {in_cost_raster}, {in_surface_raster}, {in_horizontal_raster}, {horizontal_factor}, {in_vertical_raster}, {vertical_factor}, {maximum_distance}, {out_distance_raster})

    Defines the neighbor that is the next cell on the least accumulative cost path to the nearest source, while accounting for surface distance and horizontal and vertical cost factors.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    in_surface_raster -- A raster defining the elevation values at each cell location.
    in_horizontal_raster -- A raster defining the horizontal direction at each cell.
    horizontal_factor -- The Horizontal Factor object defines the relationship between the horizontal cost factor and the horizontal relative moving angle.
    in_vertical_raster -- A raster defining the z-values for each cell location.
    vertical_factor -- The Vertical factor object defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA).
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    out_distance_raster -- The output path distance raster.

    Results:
    out_backlink_raster -- Output backlink raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            out_distance_raster):
        horizontal_factor = Utils.compoundParameterToString(horizontal_factor, ParameterClasses._HorizontalFactor)
        vertical_factor = Utils.compoundParameterToString(vertical_factor, ParameterClasses._VerticalFactor)
        out_backlink_raster = "#"
        result = arcpy.gp.PathBackLink_sa(
            in_source_data,
            out_backlink_raster,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            out_distance_raster)
        return _wrapToolRaster(u"PathBackLink_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        in_surface_raster,
        in_horizontal_raster,
        horizontal_factor,
        in_vertical_raster,
        vertical_factor,
        maximum_distance,
        out_distance_raster)
PathBackLink.__esri_toolname__ = "PathBackLink_sa"
PathBackLink.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "Python::HfBinary|HfForward|HfInverseLinear|HfLinear|HfTable::",
    "::::7",
    "Python::VfBinary|VfCos|VfCosSec|VfInverseLinear|VfLinear|VfSec|VfSecCos|VfSymInverseLinear|VfSymLinear|VfTable::",
    "::::9",
    "::::10"
]


def PathDistance(
        in_source_data,
        in_cost_raster="#",
        in_surface_raster="#",
        in_horizontal_raster="#",
        horizontal_factor="#",
        in_vertical_raster="#",
        vertical_factor="#",
        maximum_distance="#",
        out_backlink_raster="#"):
    """PathDistance(in_source_data, {in_cost_raster}, {in_surface_raster}, {in_horizontal_raster}, {horizontal_factor}, {in_vertical_raster}, {vertical_factor}, {maximum_distance}, {out_backlink_raster})

    Calculates, for each cell, the least accumulative cost distance to the nearest source, while accounting for surface distance and horizontal and vertical cost factors.

    Arguments:
    in_source_data -- The input source locations.
    in_cost_raster -- A raster defining the impedance or cost to move planimetrically through each cell.
    in_surface_raster -- A raster defining the elevation values at each cell location.
    in_horizontal_raster -- A raster defining the horizontal direction at each cell.
    horizontal_factor -- The Horizontal Factor object defines the relationship between the horizontal cost factor and the horizontal relative moving angle.
    in_vertical_raster -- A raster defining the z-values for each cell location.
    vertical_factor -- The Vertical factor object defines the relationship between the vertical cost factor and the vertical relative moving angle (VRMA).
    maximum_distance -- Defines the threshold that the accumulative cost values cannot exceed.
    out_backlink_raster -- The output cost back-link raster.

    Results:
    out_distance_raster -- Output distance raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_source_data,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            out_backlink_raster):
        horizontal_factor = Utils.compoundParameterToString(horizontal_factor, ParameterClasses._HorizontalFactor)
        vertical_factor = Utils.compoundParameterToString(vertical_factor, ParameterClasses._VerticalFactor)
        out_distance_raster = "#"
        result = arcpy.gp.PathDistance_sa(
            in_source_data,
            out_distance_raster,
            in_cost_raster,
            in_surface_raster,
            in_horizontal_raster,
            horizontal_factor,
            in_vertical_raster,
            vertical_factor,
            maximum_distance,
            out_backlink_raster)
        return _wrapToolRaster(u"PathDistance_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_source_data,
        in_cost_raster,
        in_surface_raster,
        in_horizontal_raster,
        horizontal_factor,
        in_vertical_raster,
        vertical_factor,
        maximum_distance,
        out_backlink_raster)
PathDistance.__esri_toolname__ = "PathDistance_sa"
PathDistance.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "Python::HfBinary|HfForward|HfInverseLinear|HfLinear|HfTable::",
    "::::7",
    "Python::VfBinary|VfCos|VfCosSec|VfInverseLinear|VfLinear|VfSec|VfSecCos|VfSymInverseLinear|VfSymLinear|VfTable::",
    "::::9",
    "::::10"
]


def ExtractByAttributes(
        in_raster,
        where_clause):
    """ExtractByAttributes(in_raster, where_clause)

    Extracts the cells of a raster based on a logical query.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    where_clause -- A logical expression that selects a subset of raster cells.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            where_clause):
        out_raster = "#"
        result = arcpy.gp.ExtractByAttributes_sa(
            in_raster,
            where_clause,
            out_raster)
        return _wrapToolRaster(u"ExtractByAttributes_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        where_clause)
ExtractByAttributes.__esri_toolname__ = "ExtractByAttributes_sa"
ExtractByAttributes.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ExtractByCircle(
        in_raster,
        center_point,
        radius,
        extraction_area="#"):
    """ExtractByCircle(in_raster, center_point, radius, {extraction_area})

    Extracts the cells of a raster based on a circle.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    center_point -- The Point class dictates the center coordinate (x,y) of the circle defining the area to be extracted.
    radius -- Radius of the circle defining the area to be extracted.
    extraction_area -- Identifies whether to extract cells inside or outside the input circle.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            center_point,
            radius,
            extraction_area):
        center_point = Utils.compoundParameterToString(center_point, arcpy.Point)
        out_raster = "#"
        result = arcpy.gp.ExtractByCircle_sa(
            in_raster,
            center_point,
            radius,
            out_raster,
            extraction_area)
        return _wrapToolRaster(u"ExtractByCircle_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        center_point,
        radius,
        extraction_area)
ExtractByCircle.__esri_toolname__ = "ExtractByCircle_sa"
ExtractByCircle.__esri_toolinfo__ = [
    "::::1",
    "Python::Point::",
    "::::3",
    "::::5"
]


def ExtractByPoints(
        in_raster,
        points,
        extraction_area="#"):
    """ExtractByPoints(in_raster, [point,...], {extraction_area})

    Extracts the cells of a raster based on a set of coordinate points.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    point -- A Python list of Point class objects denote the locations where values will be extracted from the raster.
    extraction_area -- Identifies whether to extract cells based on the specified point locations (inside) or outside the point locations (outside) .

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            points,
            extraction_area):
        points = Utils.multiValueCompoundParameterToString(points, arcpy.Point)
        out_raster = "#"
        result = arcpy.gp.ExtractByPoints_sa(
            in_raster,
            points,
            out_raster,
            extraction_area)
        return _wrapToolRaster(u"ExtractByPoints_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        points,
        extraction_area)
ExtractByPoints.__esri_toolname__ = "ExtractByPoints_sa"
ExtractByPoints.__esri_toolinfo__ = [
    "::::1",
    "Python::Point::",
    "::::4"
]


def ExtractByPolygon(
        in_raster,
        polygons,
        extraction_area="#"):
    """ExtractByPolygon(in_raster, [point,...], {extraction_area})

    Extracts the cells of a raster based on a polygon.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    point -- A polygon (or polygons) that defines the area of the input raster to be extracted.
    extraction_area -- Identifies whether to extract cells inside or outside the input polygon.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            polygons,
            extraction_area):
        polygons = Utils.multiValueCompoundParameterToString(polygons, arcpy.Point)
        out_raster = "#"
        result = arcpy.gp.ExtractByPolygon_sa(
            in_raster,
            polygons,
            out_raster,
            extraction_area)
        return _wrapToolRaster(u"ExtractByPolygon_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        polygons,
        extraction_area)
ExtractByPolygon.__esri_toolname__ = "ExtractByPolygon_sa"
ExtractByPolygon.__esri_toolinfo__ = [
    "::::1",
    "Python::Point::",
    "::::4"
]


def ExtractByRectangle(
        in_raster,
        extent,
        extraction_area="#"):
    """ExtractByRectangle(in_raster, extent, {extraction_area})

    Extracts the cells of a raster based on a rectangle.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    extent -- A rectangle that defines the area to be extracted.
    extraction_area -- Identifies whether to extract cells inside or outside the input rectangle.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            extent,
            extraction_area):
        extent = Utils.compoundParameterToString(extent, arcpy.Extent)
        out_raster = "#"
        result = arcpy.gp.ExtractByRectangle_sa(
            in_raster,
            extent,
            out_raster,
            extraction_area)
        return _wrapToolRaster(u"ExtractByRectangle_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        extent,
        extraction_area)
ExtractByRectangle.__esri_toolname__ = "ExtractByRectangle_sa"
ExtractByRectangle.__esri_toolinfo__ = [
    "::::1",
    "Python::Extent::",
    "::::4"
]


def ExtractValuesToPoints(
        in_point_features,
        in_raster,
        out_point_features,
        interpolate_values="#",
        add_attributes="#"):
    """ExtractValuesToPoints(in_point_features, in_raster, out_point_features, {interpolate_values}, {add_attributes})

    Extracts the cell values of a raster based on a set of point features and records the values in the attribute table of an output feature class.

    Arguments:
    in_point_features -- The input point features defining the locations from which you want to extract the raster cell values.
    in_raster -- The raster dataset whose values will be extracted.
    out_point_features -- The output point feature dataset containing the extracted raster values.
    interpolate_values -- Specifies whether or not interpolation will be used.
    add_attributes -- Determines if the raster attributes are written to the output point feature dataset."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_point_features,
            in_raster,
            out_point_features,
            interpolate_values,
            add_attributes):
        result = arcpy.gp.ExtractValuesToPoints_sa(
            in_point_features,
            in_raster,
            out_point_features,
            interpolate_values,
            add_attributes)
        return result
    return Wrapper(
        in_point_features,
        in_raster,
        out_point_features,
        interpolate_values,
        add_attributes)
ExtractValuesToPoints.__esri_toolname__ = "ExtractValuesToPoints_sa"
ExtractValuesToPoints.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def Sample(
        in_rasters,
        in_location_data,
        out_table,
        resampling_type="#",
        unique_id_field="#",
        process_as_multidimensional="#"):
    """Sample([in_raster,...], in_location_data, out_table, {resampling_type}, {unique_id_field}, {process_as_multidimensional})

    Creates a table that shows the values of cells from a raster, or set of rasters, for defined locations. The locations are defined by raster cells or by a set of points.

    Arguments:
    in_raster -- The list of rasters whose values will be sampled based on the input location data.
    in_location_data -- Data identifying positions at which you want a sample taken.
    out_table -- Output table holding the sampled cell values.
    resampling_type -- Resampling algorithm used when sampling a raster.
    unique_id_field -- A field containing a different value for every location or feature in the input location raster or point features.
    process_as_multidimensional -- Determines how the input rasters are processed."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_rasters,
            in_location_data,
            out_table,
            resampling_type,
            unique_id_field,
            process_as_multidimensional):
        result = arcpy.gp.Sample_sa(
            in_rasters,
            in_location_data,
            out_table,
            resampling_type,
            unique_id_field,
            process_as_multidimensional)
        return result
    return Wrapper(
        in_rasters,
        in_location_data,
        out_table,
        resampling_type,
        unique_id_field,
        process_as_multidimensional)
Sample.__esri_toolname__ = "Sample_sa"
Sample.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def Aggregate(
        in_raster,
        cell_factor,
        aggregation_type="#",
        extent_handling="#",
        ignore_nodata="#"):
    """Aggregate(in_raster, cell_factor, {aggregation_type}, {extent_handling}, {ignore_nodata})

    Generates a reduced-resolution version of a raster. Each output cell contains the Sum, Minimum, Maximum, Mean, or Median of the input cells that are encompassed by the extent of that cell.

    Arguments:
    in_raster -- The input raster to aggregate.
    cell_factor -- The factor by which to multiply the cell size of the input raster to obtain the desired resolution for the output raster.
    aggregation_type -- Establishes how the value for each output cell will be determined.
    extent_handling -- Defines how to handle the boundaries of the input raster when its rows or columns are not a multiple of the cell factor.
    ignore_nodata -- Denotes whether NoData values are ignored by the aggregation calculation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            cell_factor,
            aggregation_type,
            extent_handling,
            ignore_nodata):
        out_raster = "#"
        result = arcpy.gp.Aggregate_sa(
            in_raster,
            out_raster,
            cell_factor,
            aggregation_type,
            extent_handling,
            ignore_nodata)
        return _wrapToolRaster(u"Aggregate_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        cell_factor,
        aggregation_type,
        extent_handling,
        ignore_nodata)
Aggregate.__esri_toolname__ = "Aggregate_sa"
Aggregate.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def BoundaryClean(
        in_raster,
        sort_type="#",
        number_of_runs="#"):
    """BoundaryClean(in_raster, {sort_type}, {number_of_runs})

    Smooths the boundary between zones by expanding and shrinking it.

    Arguments:
    in_raster -- The input raster for which the boundary between zones will be smoothed.
    sort_type -- Specifies the type of sorting to use in the smoothing process.
    number_of_runs -- Specifies the number of directions in which the smoothing process will take place.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            sort_type,
            number_of_runs):
        out_raster = "#"
        result = arcpy.gp.BoundaryClean_sa(
            in_raster,
            out_raster,
            sort_type,
            number_of_runs)
        return _wrapToolRaster(u"BoundaryClean_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        sort_type,
        number_of_runs)
BoundaryClean.__esri_toolname__ = "BoundaryClean_sa"
BoundaryClean.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Expand(
        in_raster,
        number_cells,
        zone_values):
    """Expand(in_raster, number_cells, [zone_value,...])

    Expands specified zones of a raster by a specified number of cells.

    Arguments:
    in_raster -- The input raster for which the identified zones are to be expanded
    number_cells -- The number of cells to expand each specified zone by.
    zone_value -- The list of zone values to expand.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            number_cells,
            zone_values):
        out_raster = "#"
        result = arcpy.gp.Expand_sa(
            in_raster,
            out_raster,
            number_cells,
            zone_values)
        return _wrapToolRaster(u"Expand_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        number_cells,
        zone_values)
Expand.__esri_toolname__ = "Expand_sa"
Expand.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def MajorityFilter(
        in_raster,
        number_neighbors="#",
        majority_definition="#"):
    """MajorityFilter(in_raster, {number_neighbors}, {majority_definition})

    Replaces cells in a raster based on the majority of their contiguous neighboring cells.

    Arguments:
    in_raster -- The input raster to be filtered based on the majority of contiguous neighboring cells.
    number_neighbors -- Determines the number of neighboring cells to use in the kernel of the filter.
    majority_definition -- Specifies the number of contiguous (spatially connected) cells that must be of the same value before a replacement will occur.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            number_neighbors,
            majority_definition):
        out_raster = "#"
        result = arcpy.gp.MajorityFilter_sa(
            in_raster,
            out_raster,
            number_neighbors,
            majority_definition)
        return _wrapToolRaster(u"MajorityFilter_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        number_neighbors,
        majority_definition)
MajorityFilter.__esri_toolname__ = "MajorityFilter_sa"
MajorityFilter.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Nibble(
        in_raster,
        in_mask_raster,
        nibble_values="#"):
    """Nibble(in_raster, in_mask_raster, {nibble_values})

    Replaces cells of a raster corresponding to a mask with the values of the nearest neighbors.

    Arguments:
    in_raster -- The input raster that will be nibbled.
    in_mask_raster -- The raster used as the mask.
    nibble_values -- Keywords defining if NoData values in the input raster are allowed to nibble into the area defined by the mask raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_mask_raster,
            nibble_values):
        out_raster = "#"
        result = arcpy.gp.Nibble_sa(
            in_raster,
            in_mask_raster,
            out_raster,
            nibble_values)
        return _wrapToolRaster(u"Nibble_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_mask_raster,
        nibble_values)
Nibble.__esri_toolname__ = "Nibble_sa"
Nibble.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def RegionGroup(
        in_raster,
        number_neighbors="#",
        zone_connectivity="#",
        add_link="#",
        excluded_value="#"):
    """RegionGroup(in_raster, {number_neighbors}, {zone_connectivity}, {add_link}, {excluded_value})

    For each cell in the output, the identity of the connected region to which that cell belongs is recorded. A unique number is assigned to each region.

    Arguments:
    in_raster -- The input raster whose unique connected regions will be identified.
    number_neighbors -- The number of neighboring cells to use in evaluating connectivity between cells.
    zone_connectivity -- Defines which cell values should be considered when testing for connectivity.
    add_link -- Specifies whether a link field is added to the table of the output.
    excluded_value -- Identifies a value such that if a cell location contains the value, no spatial connectivity will be evaluated regardless how the number of neighbors is specified (FOUR or EIGHT).

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            number_neighbors,
            zone_connectivity,
            add_link,
            excluded_value):
        out_raster = "#"
        result = arcpy.gp.RegionGroup_sa(
            in_raster,
            out_raster,
            number_neighbors,
            zone_connectivity,
            add_link,
            excluded_value)
        return _wrapToolRaster(u"RegionGroup_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        number_neighbors,
        zone_connectivity,
        add_link,
        excluded_value)
RegionGroup.__esri_toolname__ = "RegionGroup_sa"
RegionGroup.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def Shrink(
        in_raster,
        number_cells,
        zone_values):
    """Shrink(in_raster, number_cells, [zone_value,...])

    Shrinks the selected zones by a specified number of cells by replacing them with the value of the cell that is most frequent in its neighborhood.

    Arguments:
    in_raster -- The input raster for which the identified zones are to be shrunk.
    number_cells -- The number of cells by which to shrink each specified zone.
    zone_value -- The list of zone values to shrink.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            number_cells,
            zone_values):
        out_raster = "#"
        result = arcpy.gp.Shrink_sa(
            in_raster,
            out_raster,
            number_cells,
            zone_values)
        return _wrapToolRaster(u"Shrink_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        number_cells,
        zone_values)
Shrink.__esri_toolname__ = "Shrink_sa"
Shrink.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Thin(
        in_raster,
        background_value="#",
        filter="#",
        corners="#",
        maximum_thickness="#"):
    """Thin(in_raster, {background_value}, {filter}, {corners}, {maximum_thickness})

    Thins rasterized linear features by reducing the number of cells representing the width of the features.

    Arguments:
    in_raster -- The input raster to be thinned.
    background_value -- Specifies the cell value that will identify the background cells. The linear features are formed from the foreground cells.
    filter -- Specifies whether a filter will be applied as the first phase of thinning.
    corners -- Specifies whether round or sharp turns will be made at turns or junctions.
    maximum_thickness -- The maximum thickness, in map units, of linear features in the input raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            background_value,
            filter,
            corners,
            maximum_thickness):
        out_raster = "#"
        result = arcpy.gp.Thin_sa(
            in_raster,
            out_raster,
            background_value,
            filter,
            corners,
            maximum_thickness)
        return _wrapToolRaster(u"Thin_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        background_value,
        filter,
        corners,
        maximum_thickness)
Thin.__esri_toolname__ = "Thin_sa"
Thin.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def DarcyFlow(
        in_head_raster,
        in_porosity_raster,
        in_thickness_raster,
        in_transmissivity_raster,
        out_direction_raster="#",
        out_magnitude_raster="#"):
    """DarcyFlow(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, {out_direction_raster}, {out_magnitude_raster})

    Calculates the groundwater volume balance residual and other outputs for steady flow in an aquifer.

    Arguments:
    in_head_raster -- The input raster where each cell value represents the groundwater head elevation at that location.
    in_porosity_raster -- The input raster where each cell value represents the effective formation porosity at that location.
    in_thickness_raster -- The input raster where each cell value represents the saturated thickness at that location.
    in_transmissivity_raster -- The input raster where each cell value represents the formation transmissivity at that location.
    out_direction_raster -- The  output flow direction raster.
    out_magnitude_raster -- An optional output raster where each cell value represents the magnitude of the seepage velocity vector (average linear velocity) at the center of the cell, calculated as the average value of the seepage velocity through the four faces of the cell.

    Results:
    out_volume_raster -- Output groundwater volume balance residual raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_head_raster,
            in_porosity_raster,
            in_thickness_raster,
            in_transmissivity_raster,
            out_direction_raster,
            out_magnitude_raster):
        out_volume_raster = "#"
        result = arcpy.gp.DarcyFlow_sa(
            in_head_raster,
            in_porosity_raster,
            in_thickness_raster,
            in_transmissivity_raster,
            out_volume_raster,
            out_direction_raster,
            out_magnitude_raster)
        return _wrapToolRaster(u"DarcyFlow_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_head_raster,
        in_porosity_raster,
        in_thickness_raster,
        in_transmissivity_raster,
        out_direction_raster,
        out_magnitude_raster)
DarcyFlow.__esri_toolname__ = "DarcyFlow_sa"
DarcyFlow.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::6",
    "::::7"
]


def DarcyVelocity(
        in_head_raster,
        in_porosity_raster,
        in_thickness_raster,
        in_transmissivity_raster,
        out_magnitude_raster):
    """DarcyVelocity(in_head_raster, in_porosity_raster, in_thickness_raster, in_transmissivity_raster, out_magnitude_raster)

    Calculates the groundwater seepage velocity vector (direction and magnitude) for steady flow in an aquifer.

    Arguments:
    in_head_raster -- The input raster where each cell value represents the groundwater head elevation at that location.
    in_porosity_raster -- The input raster where each cell value represents the effective formation porosity at that location.
    in_thickness_raster -- The input raster where each cell value represents the saturated thickness at that location.
    in_transmissivity_raster -- The input raster where each cell value represents the formation transmissivity at that location.
    out_magnitude_raster -- The  output flow direction raster.

    Results:
    out_direction_raster -- Output direction raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_head_raster,
            in_porosity_raster,
            in_thickness_raster,
            in_transmissivity_raster,
            out_magnitude_raster):
        out_direction_raster = "#"
        result = arcpy.gp.DarcyVelocity_sa(
            in_head_raster,
            in_porosity_raster,
            in_thickness_raster,
            in_transmissivity_raster,
            out_direction_raster,
            out_magnitude_raster)
        return _wrapToolRaster(u"DarcyVelocity_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_head_raster,
        in_porosity_raster,
        in_thickness_raster,
        in_transmissivity_raster,
        out_magnitude_raster)
DarcyVelocity.__esri_toolname__ = "DarcyVelocity_sa"
DarcyVelocity.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::6"
]


def ParticleTrack(
        in_direction_raster,
        in_magnitude_raster,
        source_point,
        out_track_file,
        step_length="#",
        tracking_time="#",
        out_track_polyline_features="#"):
    """ParticleTrack(in_direction_raster, in_magnitude_raster, source_point, out_track_file, {step_length}, {tracking_time}, {out_track_polyline_features})

    Calculates the path of a particle through a velocity field, returning an ASCII file of particle tracking data and, optionally, a feature class of track information.

    Arguments:
    in_direction_raster -- An input raster where each cell value represents the direction of the seepage velocity vector (average linear velocity) at the center of the cell.
    in_magnitude_raster -- An input raster where each cell value represents the magnitude of the seepage velocity vector (average linear velocity) at the center of the cell.
    source_point -- The location of the source point from which to begin the particle tracking.
    out_track_file -- The output ASCII text file that contains the particle tracking data.
    step_length -- The step length to be used for calculating the particle track.
    tracking_time -- Maximum elapsed time for particle tracking.
    out_track_polyline_features -- The optional output line feature class containing the particle track."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_direction_raster,
            in_magnitude_raster,
            source_point,
            out_track_file,
            step_length,
            tracking_time,
            out_track_polyline_features):
        source_point = Utils.compoundParameterToString(source_point, arcpy.Point)
        result = arcpy.gp.ParticleTrack_sa(
            in_direction_raster,
            in_magnitude_raster,
            source_point,
            out_track_file,
            step_length,
            tracking_time,
            out_track_polyline_features)
        return result
    return Wrapper(
        in_direction_raster,
        in_magnitude_raster,
        source_point,
        out_track_file,
        step_length,
        tracking_time,
        out_track_polyline_features)
ParticleTrack.__esri_toolname__ = "ParticleTrack_sa"
ParticleTrack.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "Python::Point::",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def PorousPuff(
        in_track_file,
        in_porosity_raster,
        in_thickness_raster,
        mass,
        dispersion_time="#",
        longitudinal_dispersivity="#",
        dispersivity_ratio="#",
        retardation_factor="#",
        decay_coefficient="#"):
    """PorousPuff(in_track_file, in_porosity_raster, in_thickness_raster, mass, {dispersion_time}, {longitudinal_dispersivity}, {dispersivity_ratio}, {retardation_factor}, {decay_coefficient})

    Calculates the time-dependent, two-dimensional concentration distribution in mass per volume of a solute introduced instantaneously and at a discrete point into a vertically mixed aquifer.

    Arguments:
    in_track_file -- The input particle track path file.
    in_porosity_raster -- The input raster where each cell value represents the effective formation porosity at that location.
    in_thickness_raster -- The input raster where each cell value represents the saturated thickness at that location.
    mass -- A value for the amount of mass released instantaneously at the source point, in units of mass.
    dispersion_time -- A value representing the time horizon for dispersion of the solute, in units of time.
    longitudinal_dispersivity -- A value representing the dispersivity parallel to the flow direction.
    dispersivity_ratio -- A value representing the ratio of longitudinal dispersivity over transverse dispersivity.
    retardation_factor -- A dimensionless value representing the retardation of the solute in the aquifer.
    decay_coefficient -- Decay coefficient for solutes undergoing first-order exponential decay (for example, radionuclides) in units of inverse time.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_track_file,
            in_porosity_raster,
            in_thickness_raster,
            mass,
            dispersion_time,
            longitudinal_dispersivity,
            dispersivity_ratio,
            retardation_factor,
            decay_coefficient):
        out_raster = "#"
        result = arcpy.gp.PorousPuff_sa(
            in_track_file,
            in_porosity_raster,
            in_thickness_raster,
            out_raster,
            mass,
            dispersion_time,
            longitudinal_dispersivity,
            dispersivity_ratio,
            retardation_factor,
            decay_coefficient)
        return _wrapToolRaster(u"PorousPuff_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_track_file,
        in_porosity_raster,
        in_thickness_raster,
        mass,
        dispersion_time,
        longitudinal_dispersivity,
        dispersivity_ratio,
        retardation_factor,
        decay_coefficient)
PorousPuff.__esri_toolname__ = "PorousPuff_sa"
PorousPuff.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::5",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10"
]


def Basin(
        in_flow_direction_raster):
    """Basin(in_flow_direction_raster)

    Creates a raster delineating all drainage basins.

    Arguments:
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_flow_direction_raster):
        out_raster = "#"
        result = arcpy.gp.Basin_sa(
            in_flow_direction_raster,
            out_raster)
        return _wrapToolRaster(u"Basin_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_flow_direction_raster)
Basin.__esri_toolname__ = "Basin_sa"
Basin.__esri_toolinfo__ = [
    "::::1"
]


def Fill(
        in_surface_raster,
        z_limit="#"):
    """Fill(in_surface_raster, {z_limit})

    Fills sinks in a surface raster to remove small imperfections in the data.

    Arguments:
    in_surface_raster -- The input raster representing a continuous surface.
    z_limit -- Maximum elevation difference between a sink and its pour point to be filled.

    Results:
    out_surface_raster -- Output surface raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_surface_raster,
            z_limit):
        out_surface_raster = "#"
        result = arcpy.gp.Fill_sa(
            in_surface_raster,
            out_surface_raster,
            z_limit)
        return _wrapToolRaster(u"Fill_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_surface_raster,
        z_limit)
Fill.__esri_toolname__ = "Fill_sa"
Fill.__esri_toolinfo__ = [
    "::::1",
    "::::3"
]


def FlowAccumulation(
        in_flow_direction_raster,
        in_weight_raster="#",
        data_type="#"):
    """FlowAccumulation(in_flow_direction_raster, {in_weight_raster}, {data_type})

    Creates a raster of accumulated flow into each cell. A weight factor can optionally be applied.

    Arguments:
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.
    in_weight_raster -- An optional input raster for applying a weight to each cell.
    data_type -- The output accumulation raster can be integer or floating point type.

    Results:
    out_accumulation_raster -- Output accumulation raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_flow_direction_raster,
            in_weight_raster,
            data_type):
        out_accumulation_raster = "#"
        result = arcpy.gp.FlowAccumulation_sa(
            in_flow_direction_raster,
            out_accumulation_raster,
            in_weight_raster,
            data_type)
        return _wrapToolRaster(u"FlowAccumulation_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_flow_direction_raster,
        in_weight_raster,
        data_type)
FlowAccumulation.__esri_toolname__ = "FlowAccumulation_sa"
FlowAccumulation.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def FlowDirection(
        in_surface_raster,
        force_flow="#",
        out_drop_raster="#"):
    """FlowDirection(in_surface_raster, {force_flow}, {out_drop_raster})

    Creates a raster of flow direction from each cell to its steepest downslope neighbor.

    Arguments:
    in_surface_raster -- The input raster representing a continuous surface.
    force_flow -- Specifies if edge cells will always flow outward or follow normal flow rules.
    out_drop_raster -- An optional output drop raster.

    Results:
    out_flow_direction_raster -- Output flow direction raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_surface_raster,
            force_flow,
            out_drop_raster):
        out_flow_direction_raster = "#"
        result = arcpy.gp.FlowDirection_sa(
            in_surface_raster,
            out_flow_direction_raster,
            force_flow,
            out_drop_raster)
        return _wrapToolRaster(u"FlowDirection_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_surface_raster,
        force_flow,
        out_drop_raster)
FlowDirection.__esri_toolname__ = "FlowDirection_sa"
FlowDirection.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def FlowLength(
        in_flow_direction_raster,
        direction_measurement="#",
        in_weight_raster="#"):
    """FlowLength(in_flow_direction_raster, {direction_measurement}, {in_weight_raster})

    Calculates the upstream or downstream distance, or weighted distance, along the flow path for each cell.

    Arguments:
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.
    direction_measurement -- The direction of measurement along the flow path.
    in_weight_raster -- An optional input raster for applying a weight to each cell.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_flow_direction_raster,
            direction_measurement,
            in_weight_raster):
        out_raster = "#"
        result = arcpy.gp.FlowLength_sa(
            in_flow_direction_raster,
            out_raster,
            direction_measurement,
            in_weight_raster)
        return _wrapToolRaster(u"FlowLength_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_flow_direction_raster,
        direction_measurement,
        in_weight_raster)
FlowLength.__esri_toolname__ = "FlowLength_sa"
FlowLength.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Sink(
        in_flow_direction_raster):
    """Sink(in_flow_direction_raster)

    Creates a raster identifying all sinks or areas of internal drainage.

    Arguments:
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_flow_direction_raster):
        out_raster = "#"
        result = arcpy.gp.Sink_sa(
            in_flow_direction_raster,
            out_raster)
        return _wrapToolRaster(u"Sink_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_flow_direction_raster)
Sink.__esri_toolname__ = "Sink_sa"
Sink.__esri_toolinfo__ = [
    "::::1"
]


def SnapPourPoint(
        in_pour_point_data,
        in_accumulation_raster,
        snap_distance,
        pour_point_field="#"):
    """SnapPourPoint(in_pour_point_data, in_accumulation_raster, snap_distance, {pour_point_field})

    Snaps pour points to the cell of highest flow accumulation within a specified distance.

    Arguments:
    in_pour_point_data -- The input pour point locations that are to be snapped.
    in_accumulation_raster -- The input flow accumulation raster.
    snap_distance -- Maximum distance, in map units, to search for a cell of higher accumulated flow.
    pour_point_field -- Field used to assign values to the pour point locations.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_pour_point_data,
            in_accumulation_raster,
            snap_distance,
            pour_point_field):
        out_raster = "#"
        result = arcpy.gp.SnapPourPoint_sa(
            in_pour_point_data,
            in_accumulation_raster,
            out_raster,
            snap_distance,
            pour_point_field)
        return _wrapToolRaster(u"SnapPourPoint_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_pour_point_data,
        in_accumulation_raster,
        snap_distance,
        pour_point_field)
SnapPourPoint.__esri_toolname__ = "SnapPourPoint_sa"
SnapPourPoint.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5"
]


def StreamLink(
        in_stream_raster,
        in_flow_direction_raster):
    """StreamLink(in_stream_raster, in_flow_direction_raster)

    Assigns unique values to sections of a raster linear network between intersections.

    Arguments:
    in_stream_raster -- An input raster that represents a linear stream network.
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_stream_raster,
            in_flow_direction_raster):
        out_raster = "#"
        result = arcpy.gp.StreamLink_sa(
            in_stream_raster,
            in_flow_direction_raster,
            out_raster)
        return _wrapToolRaster(u"StreamLink_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_stream_raster,
        in_flow_direction_raster)
StreamLink.__esri_toolname__ = "StreamLink_sa"
StreamLink.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def StreamOrder(
        in_stream_raster,
        in_flow_direction_raster,
        order_method="#"):
    """StreamOrder(in_stream_raster, in_flow_direction_raster, {order_method})

    Assigns a numeric order to segments of a raster representing branches of a linear network.

    Arguments:
    in_stream_raster -- An input raster that represents a linear stream network.
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.
    order_method -- The method used for assigning stream order.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_stream_raster,
            in_flow_direction_raster,
            order_method):
        out_raster = "#"
        result = arcpy.gp.StreamOrder_sa(
            in_stream_raster,
            in_flow_direction_raster,
            out_raster,
            order_method)
        return _wrapToolRaster(u"StreamOrder_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_stream_raster,
        in_flow_direction_raster,
        order_method)
StreamOrder.__esri_toolname__ = "StreamOrder_sa"
StreamOrder.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def StreamToFeature(
        in_stream_raster,
        in_flow_direction_raster,
        out_polyline_features,
        simplify="#"):
    """StreamToFeature(in_stream_raster, in_flow_direction_raster, out_polyline_features, {simplify})

    Converts a raster representing a linear network to features representing the linear network.

    Arguments:
    in_stream_raster -- An input raster that represents a linear stream network.
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.
    out_polyline_features -- Output feature class that will hold the converted streams.
    simplify -- Specifies whether weeding is used."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_stream_raster,
            in_flow_direction_raster,
            out_polyline_features,
            simplify):
        result = arcpy.gp.StreamToFeature_sa(
            in_stream_raster,
            in_flow_direction_raster,
            out_polyline_features,
            simplify)
        return result
    return Wrapper(
        in_stream_raster,
        in_flow_direction_raster,
        out_polyline_features,
        simplify)
StreamToFeature.__esri_toolname__ = "StreamToFeature_sa"
StreamToFeature.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4"
]


def Watershed(
        in_flow_direction_raster,
        in_pour_point_data,
        pour_point_field="#"):
    """Watershed(in_flow_direction_raster, in_pour_point_data, {pour_point_field})

    Determines the contributing area above a set of cells in a raster.

    Arguments:
    in_flow_direction_raster -- The input raster that shows the direction of flow out of each cell.
    in_pour_point_data -- The input pour point locations.
    pour_point_field -- Field used to assign values to the pour point locations.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_flow_direction_raster,
            in_pour_point_data,
            pour_point_field):
        out_raster = "#"
        result = arcpy.gp.Watershed_sa(
            in_flow_direction_raster,
            in_pour_point_data,
            out_raster,
            pour_point_field)
        return _wrapToolRaster(u"Watershed_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_flow_direction_raster,
        in_pour_point_data,
        pour_point_field)
Watershed.__esri_toolname__ = "Watershed_sa"
Watershed.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def Idw(
        in_point_features,
        z_field,
        cell_size="#",
        power="#",
        search_radius="#",
        in_barrier_polyline_features="#"):
    """Idw(in_point_features, z_field, {cell_size}, {power}, {search_radius}, {in_barrier_polyline_features})

    Interpolates a raster surface from points using an inverse distance weighted (IDW) technique.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    z_field -- The field that holds a height or magnitude value for each point.
    cell_size -- The cell size at which the output raster will be created.
    power -- The exponent of distance.
    search_radius -- The Radius class defines which of the input points will be used to interpolate the value for each cell in the output raster.
    in_barrier_polyline_features -- Polyline features to be used as a break or limit in searching for the input sample points.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            z_field,
            cell_size,
            power,
            search_radius,
            in_barrier_polyline_features):
        search_radius = Utils.compoundParameterToString(search_radius, ParameterClasses._Radius)
        out_raster = "#"
        result = arcpy.gp.Idw_sa(
            in_point_features,
            z_field,
            out_raster,
            cell_size,
            power,
            search_radius,
            in_barrier_polyline_features)
        return _wrapToolRaster(u"Idw_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        z_field,
        cell_size,
        power,
        search_radius,
        in_barrier_polyline_features)
Idw.__esri_toolname__ = "Idw_sa"
Idw.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "Python::RadiusFixed|RadiusVariable::",
    "::::7"
]


def Kriging(
        in_point_features,
        z_field,
        kriging_model,
        cell_size="#",
        search_radius="#",
        out_variance_prediction_raster="#"):
    """Kriging(in_point_features, z_field, kriging_model, {cell_size}, {search_radius}, {out_variance_prediction_raster})

    Interpolates a raster surface from points using kriging.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    z_field -- The field that holds a height or magnitude value for each point.
    kriging_model -- The KrigingModel class defines which kriging model is to  be used.
    cell_size -- The cell size at which the output raster will be created.
    search_radius -- The Radius class defines which of the input points will be used to interpolate the value for each cell in the output raster.
    out_variance_prediction_raster -- Optional output raster where each cell contains the predicted semi-variance values for that location.

    Results:
    out_surface_raster -- Output surface raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            z_field,
            kriging_model,
            cell_size,
            search_radius,
            out_variance_prediction_raster):
        kriging_model = Utils.compoundParameterToString(kriging_model, ParameterClasses._KrigingModel)
        search_radius = Utils.compoundParameterToString(search_radius, ParameterClasses._Radius)
        out_surface_raster = "#"
        result = arcpy.gp.Kriging_sa(
            in_point_features,
            z_field,
            out_surface_raster,
            kriging_model,
            cell_size,
            search_radius,
            out_variance_prediction_raster)
        return _wrapToolRaster(u"Kriging_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        z_field,
        kriging_model,
        cell_size,
        search_radius,
        out_variance_prediction_raster)
Kriging.__esri_toolname__ = "Kriging_sa"
Kriging.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "Python::KrigingModelOrdinary|KrigingModelUniversal::",
    "::::5",
    "Python::RadiusFixed|RadiusVariable::",
    "::::7"
]


def NaturalNeighbor(
        in_point_features,
        z_field,
        cell_size="#"):
    """NaturalNeighbor(in_point_features, z_field, {cell_size})

    Interpolates a raster surface from points using a natural neighbor technique.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    z_field -- The field that holds a height or magnitude value for each point.
    cell_size -- The cell size at which the output raster will be created.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            z_field,
            cell_size):
        out_raster = "#"
        result = arcpy.gp.NaturalNeighbor_sa(
            in_point_features,
            z_field,
            out_raster,
            cell_size)
        return _wrapToolRaster(u"NaturalNeighbor_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        z_field,
        cell_size)
NaturalNeighbor.__esri_toolname__ = "NaturalNeighbor_sa"
NaturalNeighbor.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def Spline(
        in_point_features,
        z_field,
        cell_size="#",
        spline_type="#",
        weight="#",
        number_points="#"):
    """Spline(in_point_features, z_field, {cell_size}, {spline_type}, {weight}, {number_points})

    Interpolates a raster surface from points using a two-dimensional minimum curvature spline technique.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    z_field -- The field that holds a height or magnitude value for each point.
    cell_size -- The cell size at which the output raster will be created.
    spline_type -- The type of spline to be used.
    weight -- Parameter influencing the character of the surface interpolation.
    number_points -- The number of points per region used for local approximation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            z_field,
            cell_size,
            spline_type,
            weight,
            number_points):
        out_raster = "#"
        result = arcpy.gp.Spline_sa(
            in_point_features,
            z_field,
            out_raster,
            cell_size,
            spline_type,
            weight,
            number_points)
        return _wrapToolRaster(u"Spline_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        z_field,
        cell_size,
        spline_type,
        weight,
        number_points)
Spline.__esri_toolname__ = "Spline_sa"
Spline.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def TopoToRaster(
        topo_input,
        cell_size="#",
        extent="#",
        Margin="#",
        minimum_z_value="#",
        maximum_z_value="#",
        enforce="#",
        data_type="#",
        maximum_iterations="#",
        roughness_penalty="#",
        discrete_error_factor="#",
        vertical_standard_error="#",
        tolerance_1="#",
        tolerance_2="#",
        out_stream_features="#",
        out_sink_features="#",
        out_diagnostic_file="#",
        out_parameter_file="#",
        profile_penalty="#",
        out_residual_feature="#",
        out_stream_cliff_error_feature="#",
        out_contour_error_feature="#"):
    """TopoToRaster(topo_input, {cell_size}, {extent}, {margin}, {minimum_z_value}, {maximum_z_value}, {enforce}, {data_type}, {maximum_iterations}, {roughness_penalty}, {discrete_error_factor}, {vertical_standard_error}, {tolerance_1}, {tolerance_2}, {out_stream_features}, {out_sink_features}, {out_diagnostic_file}, {out_parameter_file}, {profile_penalty}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

    Interpolates a hydrologically correct raster surface from point, line, and polygon data.

    Arguments:
    topo_input -- The Topo class specifies the input features containing the z-values to be interpolated into a surface raster.
    cell_size -- The cell size at which the output raster will be created.
    extent -- The Extent class determines the extent for the output raster dataset.
    margin -- Distance in cells to interpolate beyond the specified output extent and boundary.
    minimum_z_value -- The minimum z-value to be used in the interpolation.
    maximum_z_value -- The maximum z-value to be used in the interpolation.
    enforce -- The type of drainage enforcement to apply.
    data_type -- The dominant elevation data type of the input feature data.
    maximum_iterations -- The maximum number of interpolation iterations.
    roughness_penalty -- The integrated squared second derivative as a measure of roughness.
    discrete_error_factor -- The discrete error factor is used to adjust the amount of smoothing when converting the input data to a raster.
    vertical_standard_error -- The amount of random error in the z-values of the input data.
    tolerance_1 -- This tolerance reflects the accuracy and density of the elevation points in relation to surface drainage.
    tolerance_2 -- This tolerance prevents drainage clearance through unrealistically high barriers.
    out_stream_features -- The output line feature class of stream polyline features and ridge line features.
    out_sink_features -- The output point feature class of the remaining sink point features.
    out_diagnostic_file -- The output diagnostic file listing all inputs and parameters used and the number of sinks cleared at each resolution and iteration.
    out_parameter_file -- The output parameter file listing all inputs and parameters used, which can be used with Topo to Raster by File to run the interpolation again.
    profile_penalty -- The profile curvature roughness penalty is a locally adaptive penalty that can be used to partly replace total curvature.
    out_residual_feature -- The output point feature class of all the large elevation residuals as scaled by the local discretisation error.
    out_stream_cliff_error_feature -- The output point feature class of locations where possible stream and cliff errors occur.
    out_contour_error_feature -- The output point feature class of possible errors pertaining to the input contour data.

    Results:
    out_surface_raster -- Output surface raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            topo_input,
            cell_size,
            extent,
            Margin,
            minimum_z_value,
            maximum_z_value,
            enforce,
            data_type,
            maximum_iterations,
            roughness_penalty,
            discrete_error_factor,
            vertical_standard_error,
            tolerance_1,
            tolerance_2,
            out_stream_features,
            out_sink_features,
            out_diagnostic_file,
            out_parameter_file,
            profile_penalty,
            out_residual_feature,
            out_stream_cliff_error_feature,
            out_contour_error_feature):
        topo_input = Utils.multiValueCompoundParameterToString(topo_input, ParameterClasses._TopoInput)
        extent = Utils.compoundParameterToString(extent, arcpy.Extent)
        out_surface_raster = "#"
        result = arcpy.gp.TopoToRaster_sa(
            topo_input,
            out_surface_raster,
            cell_size,
            extent,
            Margin,
            minimum_z_value,
            maximum_z_value,
            enforce,
            data_type,
            maximum_iterations,
            roughness_penalty,
            discrete_error_factor,
            vertical_standard_error,
            tolerance_1,
            tolerance_2,
            out_stream_features,
            out_sink_features,
            out_diagnostic_file,
            out_parameter_file,
            profile_penalty,
            out_residual_feature,
            out_stream_cliff_error_feature,
            out_contour_error_feature)
        return _wrapToolRaster(u"TopoToRaster_sa", unicode(result.getOutput(0)))
    return Wrapper(
        topo_input,
        cell_size,
        extent,
        Margin,
        minimum_z_value,
        maximum_z_value,
        enforce,
        data_type,
        maximum_iterations,
        roughness_penalty,
        discrete_error_factor,
        vertical_standard_error,
        tolerance_1,
        tolerance_2,
        out_stream_features,
        out_sink_features,
        out_diagnostic_file,
        out_parameter_file,
        profile_penalty,
        out_residual_feature,
        out_stream_cliff_error_feature,
        out_contour_error_feature)
TopoToRaster.__esri_toolname__ = "TopoToRaster_sa"
TopoToRaster.__esri_toolinfo__ = [
    "Python::TopoBoundary|TopoCliff|TopoCoast|TopoContour|TopoExclusion|TopoLake|TopoPointElevation|TopoSink|TopoStream::",
    "::::3",
    "Python::Extent::",
    "::::5",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14",
    "::::15",
    "::::16",
    "::::17",
    "::::18",
    "::::19",
    "::::20",
    "::::21",
    "::::22",
    "::::23"
]


def TopoToRasterByFile(
        in_parameter_file,
        out_stream_features="#",
        out_sink_features="#",
        out_residual_feature="#",
        out_stream_cliff_error_feature="#",
        out_contour_error_feature="#"):
    """TopoToRasterByFile(in_parameter_file, {out_stream_features}, {out_sink_features}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

    Interpolates a hydrologically correct raster surface from point, line, and polygon data using parameters specified in a file.

    Arguments:
    in_parameter_file -- The input ASCII text file containing the inputs and parameters to use for the interpolation.
    out_stream_features -- Output feature class of stream polyline features.
    out_sink_features -- Output feature class of remaining sink point features.
    out_residual_feature -- The output point feature class of all the large elevation residuals as scaled by the local discretisation error.
    out_stream_cliff_error_feature -- The output point feature class of locations where possible stream and cliff errors occur.
    out_contour_error_feature -- The output point feature class of possible errors pertaining to the input contour data.

    Results:
    out_surface_raster -- Output surface raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_parameter_file,
            out_stream_features,
            out_sink_features,
            out_residual_feature,
            out_stream_cliff_error_feature,
            out_contour_error_feature):
        out_surface_raster = "#"
        result = arcpy.gp.TopoToRasterByFile_sa(
            in_parameter_file,
            out_surface_raster,
            out_stream_features,
            out_sink_features,
            out_residual_feature,
            out_stream_cliff_error_feature,
            out_contour_error_feature)
        return _wrapToolRaster(u"TopoToRasterByFile_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_parameter_file,
        out_stream_features,
        out_sink_features,
        out_residual_feature,
        out_stream_cliff_error_feature,
        out_contour_error_feature)
TopoToRasterByFile.__esri_toolname__ = "TopoToRasterByFile_sa"
TopoToRasterByFile.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def Trend(
        in_point_features,
        z_field,
        cell_size="#",
        order="#",
        regression_type="#",
        out_rms_file="#"):
    """Trend(in_point_features, z_field, {cell_size}, {order}, {regression_type}, {out_rms_file})

    Interpolates a raster surface from points using a trend technique.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    z_field -- The field that holds a height or magnitude value for each point.
    cell_size -- The cell size at which the output raster will be created.
    order -- The order of the polynomial.
    regression_type -- The type of regression to be performed.
    out_rms_file -- File name for the output text file that contains information about the RMS error and the Chi-Square of the interpolation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            z_field,
            cell_size,
            order,
            regression_type,
            out_rms_file):
        out_raster = "#"
        result = arcpy.gp.Trend_sa(
            in_point_features,
            z_field,
            out_raster,
            cell_size,
            order,
            regression_type,
            out_rms_file)
        return _wrapToolRaster(u"Trend_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        z_field,
        cell_size,
        order,
        regression_type,
        out_rms_file)
Trend.__esri_toolname__ = "Trend_sa"
Trend.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def CellStatistics(
        in_rasters_or_constants,
        statistics_type="#",
        ignore_nodata="#"):
    """CellStatistics([in_raster_or_constant,...], {statistics_type}, {ignore_nodata})

    Calculates a per-cell statistic from multiple rasters.

    Arguments:
    in_raster_or_constant -- A list of input rasters for which a statistic will be calculated for each cell within the Analysis window.
    statistics_type -- Statistic type to be calculated.
    ignore_nodata -- Denotes whether NoData values are ignored by the statistic calculation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rasters_or_constants,
            statistics_type,
            ignore_nodata):
        statisticsTypes = {
            "MAJORITY": "Majority",
            "MAXIMUM": "Max",
            "MEAN": "Mean",
            "MEDIAN": "Med",
            "MINIMUM": "Min",
            "MINORITY": "Minority",
            "RANGE": "Range",
            "STD": "Std",
            "SUM": "Sum",
            "VARIETY": "Variety"
        }
        if Utils.useDefaultArgumentValue(statistics_type):
            statistics_type = "MEAN"
        if not statistics_type in statisticsTypes:
            raise arcpy.ExecuteError("ERROR 000864: Overlay statistic: The input is not within the defined domain.\nERROR 000800: The value is not a member of MEAN | MAJORITY | MAXIMUM | MEDIAN | MINIMUM | MINORITY | RANGE | STD | SUM | VARIETY.\n")
        function = statisticsTypes[statistics_type]
        if Utils.useDefaultArgumentValue(ignore_nodata):
            ignore_nodata = "DATA"
        if ignore_nodata not in ["DATA", "NODATA"]:
            raise arcpy.ExecuteError("ERROR 000622: Failed to execute (CellStatistics). Parameters are not valid.\nERROR 000621: Input to parameter ignore_nodata not within domain.\n")
        if Utils.argumentValueEqualsString(ignore_nodata, "DATA"):
            function += "ContinueOnNoData"
        return _wrapLocalFunctionRaster(u"CellStatistics_sa",
            [function] + Utils.flattenLists(in_rasters_or_constants))
    return Wrapper(
        in_rasters_or_constants,
        statistics_type,
        ignore_nodata)
CellStatistics.__esri_toolname__ = "CellStatistics_sa"
CellStatistics.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Combine(
        in_rasters):
    """Combine([in_raster,...])

    Combines multiple rasters so that a unique output value is assigned to each unique combination of input values.

    Arguments:
    in_raster -- The list of input rasters to be combined.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.Combine_sa(
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"Combine_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_rasters)
Combine.__esri_toolname__ = "Combine_sa"
Combine.__esri_toolinfo__ = [
    "::::1"
]


def EqualToFrequency(
        in_value_raster,
        in_rasters):
    """EqualToFrequency(in_value_raster, [in_raster,...])

    Evaluates on a cell-by-cell basis the number of times the values in a set of rasters are equal to another raster.

    Arguments:
    in_value_raster -- For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has an equal value is counted.
    in_raster -- The list of rasters that will be compared against the value raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_value_raster,
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.EqualToFrequency_sa(
            in_value_raster,
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"EqualToFrequency_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_value_raster,
        in_rasters)
EqualToFrequency.__esri_toolname__ = "EqualToFrequency_sa"
EqualToFrequency.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def GreaterThanFrequency(
        in_value_raster,
        in_rasters):
    """GreaterThanFrequency(in_value_raster, [in_raster,...])

    Evaluates on a cell-by-cell basis the number of times a set of rasters is greater than another raster.

    Arguments:
    in_value_raster -- For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has a greater value is counted.
    in_raster -- The list of rasters that will be compared against the value raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_value_raster,
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.GreaterThanFrequency_sa(
            in_value_raster,
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"GreaterThanFrequency_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_value_raster,
        in_rasters)
GreaterThanFrequency.__esri_toolname__ = "GreaterThanFrequency_sa"
GreaterThanFrequency.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def HighestPosition(
        in_rasters_or_constants):
    """HighestPosition([in_raster_or_constant,...])

    Determines on a cell-by-cell basis the position of the raster with the maximum value in a set of rasters.

    Arguments:
    in_raster_or_constant -- The list of input rasters for which the position of the input with the highest value will be determined.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rasters_or_constants):
        out_raster = "#"
        result = arcpy.gp.HighestPosition_sa(
            in_rasters_or_constants,
            out_raster)
        return _wrapToolRaster(u"HighestPosition_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_rasters_or_constants)
HighestPosition.__esri_toolname__ = "HighestPosition_sa"
HighestPosition.__esri_toolinfo__ = [
    "::::1"
]


def LessThanFrequency(
        in_value_raster,
        in_rasters):
    """LessThanFrequency(in_value_raster, [in_raster,...])

    Evaluates on a cell-by-cell basis the number of times a set of rasters is less than another raster.

    Arguments:
    in_value_raster -- For each cell location in the input value raster, the number of occurrences (frequency) where a raster in the input list has a lesser value is counted.
    in_raster -- The list of rasters that will be compared against the value raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_value_raster,
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.LessThanFrequency_sa(
            in_value_raster,
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"LessThanFrequency_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_value_raster,
        in_rasters)
LessThanFrequency.__esri_toolname__ = "LessThanFrequency_sa"
LessThanFrequency.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def LowestPosition(
        in_rasters_or_constants):
    """LowestPosition([in_raster_or_constant,...])

    Determines on a cell-by-cell basis the position of the raster with the minimum value in a set of rasters.

    Arguments:
    in_raster_or_constant -- The list of input rasters for which the position of the input with the lowest value will be determined.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rasters_or_constants):
        out_raster = "#"
        result = arcpy.gp.LowestPosition_sa(
            in_rasters_or_constants,
            out_raster)
        return _wrapToolRaster(u"LowestPosition_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_rasters_or_constants)
LowestPosition.__esri_toolname__ = "LowestPosition_sa"
LowestPosition.__esri_toolinfo__ = [
    "::::1"
]


def Popularity(
        in_popularity_raster_or_constant,
        in_rasters):
    """Popularity(in_popularity_raster_or_constant, [in_raster,...])

    Determines the value in an argument list that is at a certain level of popularity on a cell-by-cell basis. The particular level of popularity (the number of occurrences of each value) is specified by the first argument.

    Arguments:
    in_popularity_raster_or_constant -- The input raster defining the popularity position to be returned.
    in_raster -- The list of input rasters used to evaluate the popularity of the values for each cell location.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_popularity_raster_or_constant,
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.Popularity_sa(
            in_popularity_raster_or_constant,
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"Popularity_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_popularity_raster_or_constant,
        in_rasters)
Popularity.__esri_toolname__ = "Popularity_sa"
Popularity.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Rank(
        in_rank_raster_or_constant,
        in_rasters):
    """Rank(in_rank_raster_or_constant, [in_raster,...])

    The values from the set of input rasters are ranked on a cell-by-cell basis, and which of these gets returned is determined by the value of the rank input raster.

    Arguments:
    in_rank_raster_or_constant -- The input raster that defines the rank position to be returned.
    in_raster -- The list of input rasters.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rank_raster_or_constant,
            in_rasters):
        out_raster = "#"
        result = arcpy.gp.Rank_sa(
            in_rank_raster_or_constant,
            in_rasters,
            out_raster)
        return _wrapToolRaster(u"Rank_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_rank_raster_or_constant,
        in_rasters)
Rank.__esri_toolname__ = "Rank_sa"
Rank.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Abs(
        in_raster_or_constant):
    """Abs(in_raster_or_constant)

    Calculates the absolute value of the cells in a raster.

    Arguments:
    in_raster_or_constant -- The input raster for which to calculate the absolute values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Abs_sa",
            ["Abs", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Abs.__esri_toolname__ = "Abs_sa"
Abs.__esri_toolinfo__ = [
    "::::1"
]


def BitwiseAnd(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BitwiseAnd(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Bitwise And operation on the binary values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this bitwise operation.
    in_raster_or_constant2 -- The second input to use in this bitwise operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BitwiseAnd_sa",
            ["BitwiseAnd", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BitwiseAnd.__esri_toolname__ = "BitwiseAnd_sa"
BitwiseAnd.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BitwiseLeftShift(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BitwiseLeftShift(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Bitwise Left Shift operation on the binary values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The input on which to perform the shift.
    in_raster_or_constant2 -- The input defining the number of positions to shift the bits.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BitwiseLeftShift_sa",
            ["BitwiseLeftShift", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BitwiseLeftShift.__esri_toolname__ = "BitwiseLeftShift_sa"
BitwiseLeftShift.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BitwiseNot(
        in_raster_or_constant):
    """BitwiseNot(in_raster_or_constant)

    Performs a Bitwise Not (complement) operation on the binary value of an input raster.

    Arguments:
    in_raster_or_constant -- The input raster on which to perform the Bitwise Not (complement) operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"BitwiseNot_sa",
            ["BitwiseNot", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
BitwiseNot.__esri_toolname__ = "BitwiseNot_sa"
BitwiseNot.__esri_toolinfo__ = [
    "::::1"
]


def BitwiseOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BitwiseOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Bitwise Or operation on the binary values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this bitwise operation.
    in_raster_or_constant2 -- The second input to use in this bitwise operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BitwiseOr_sa",
            ["BitwiseOr", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BitwiseOr.__esri_toolname__ = "BitwiseOr_sa"
BitwiseOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BitwiseRightShift(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BitwiseRightShift(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Bitwise Right Shift operation on the binary values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The input on which to perform the shift.
    in_raster_or_constant2 -- The input defining the number of positions to shift the bits.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BitwiseRightShift_sa",
            ["BitwiseRightShift", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BitwiseRightShift.__esri_toolname__ = "BitwiseRightShift_sa"
BitwiseRightShift.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BitwiseXOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BitwiseXOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Bitwise eXclusive Or operation on the binary values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this bitwise operation.
    in_raster_or_constant2 -- The second input to use in this bitwise operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BitwiseXOr_sa",
            ["BitwiseXOr", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BitwiseXOr.__esri_toolname__ = "BitwiseXOr_sa"
BitwiseXOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Divide(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Divide(in_raster_or_constant1, in_raster_or_constant2)

    Divides the values of two rasters on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input whose values will be divided by the second input.
    in_raster_or_constant2 -- The input whose values the first input are to be divided by.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Divide_sa",
            ["Divide", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Divide.__esri_toolname__ = "Divide_sa"
Divide.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Exp(
        in_raster_or_constant):
    """Exp(in_raster_or_constant)

    Calculates the base e exponential of the cells in a raster.

    Arguments:
    in_raster_or_constant -- The input values for which to find the base e exponential.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Exp_sa",
            ["Exp", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Exp.__esri_toolname__ = "Exp_sa"
Exp.__esri_toolinfo__ = [
    "::::1"
]


def Exp10(
        in_raster_or_constant):
    """Exp10(in_raster_or_constant)

    Calculates the base 10 exponential of the cells in a raster.

    Arguments:
    in_raster_or_constant -- The input values for which to find the base 10 exponential.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Exp10_sa",
            ["Exp10", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Exp10.__esri_toolname__ = "Exp10_sa"
Exp10.__esri_toolinfo__ = [
    "::::1"
]


def Exp2(
        in_raster_or_constant):
    """Exp2(in_raster_or_constant)

    Calculates the base 2 exponential of the cells in a raster.

    Arguments:
    in_raster_or_constant -- The input values for which to find the base 2 exponential.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Exp2_sa",
            ["Exp2", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Exp2.__esri_toolname__ = "Exp2_sa"
Exp2.__esri_toolinfo__ = [
    "::::1"
]


def Float(
        in_raster_or_constant):
    """Float(in_raster_or_constant)

    Converts each cell value of a raster into a floating-point representation.

    Arguments:
    in_raster_or_constant -- The input raster to be converted to floating point.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Float_sa",
            ["Float", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Float.__esri_toolname__ = "Float_sa"
Float.__esri_toolinfo__ = [
    "::::1"
]


def Int(
        in_raster_or_constant):
    """Int(in_raster_or_constant)

    Converts each cell value of a raster to an integer by truncation.

    Arguments:
    in_raster_or_constant -- The input raster to be converted to integer.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Int_sa",
            ["Int", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Int.__esri_toolname__ = "Int_sa"
Int.__esri_toolinfo__ = [
    "::::1"
]


def Ln(
        in_raster_or_constant):
    """Ln(in_raster_or_constant)

    Calculates the natural logarithm (base e) of cells in a raster.

    Arguments:
    in_raster_or_constant -- Input values for which to find the natural logarithm (Ln).

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Ln_sa",
            ["Ln", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Ln.__esri_toolname__ = "Ln_sa"
Ln.__esri_toolinfo__ = [
    "::::1"
]


def Log10(
        in_raster_or_constant):
    """Log10(in_raster_or_constant)

    Calculates the base 10 logarithm of cells in a raster.

    Arguments:
    in_raster_or_constant -- Input values for which to find the base 10 logarithm.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Log10_sa",
            ["Log10", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Log10.__esri_toolname__ = "Log10_sa"
Log10.__esri_toolinfo__ = [
    "::::1"
]


def Log2(
        in_raster_or_constant):
    """Log2(in_raster_or_constant)

    Calculates the base 2 logarithm of cells in a raster.

    Arguments:
    in_raster_or_constant -- Input values for which to find the base 2 logarithm.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Log2_sa",
            ["Log2", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Log2.__esri_toolname__ = "Log2_sa"
Log2.__esri_toolinfo__ = [
    "::::1"
]


def BooleanAnd(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BooleanAnd(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Boolean And operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this Boolean operation.
    in_raster_or_constant2 -- The second input to use in this Boolean operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BooleanAnd_sa",
            ["BooleanAnd", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BooleanAnd.__esri_toolname__ = "BooleanAnd_sa"
BooleanAnd.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BooleanNot(
        in_raster_or_constant):
    """BooleanNot(in_raster_or_constant)

    Performs a Boolean Not (complement) operation on the cell values of the input raster.

    Arguments:
    in_raster_or_constant -- The input to use in this Boolean operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"BooleanNot_sa",
            ["BooleanNot", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
BooleanNot.__esri_toolname__ = "BooleanNot_sa"
BooleanNot.__esri_toolinfo__ = [
    "::::1"
]


def BooleanOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BooleanOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Boolean Or operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this Boolean operation.
    in_raster_or_constant2 -- The second input to use in this Boolean operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BooleanOr_sa",
            ["BooleanOr", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BooleanOr.__esri_toolname__ = "BooleanOr_sa"
BooleanOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def BooleanXOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """BooleanXOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Boolean eXclusive Or operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this Boolean operation.
    in_raster_or_constant2 -- The second input to use in this Boolean operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"BooleanXOr_sa",
            ["BooleanXOr", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
BooleanXOr.__esri_toolname__ = "BooleanXOr_sa"
BooleanXOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def CombinatorialAnd(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """CombinatorialAnd(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Combinatorial And operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this combinatorial operation.
    in_raster_or_constant2 -- The second input to use in this combinatorial operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        out_raster = "#"
        result = arcpy.gp.CombinatorialAnd_sa(
            in_raster_or_constant1,
            in_raster_or_constant2,
            out_raster)
        return _wrapToolRaster(u"CombinatorialAnd_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
CombinatorialAnd.__esri_toolname__ = "CombinatorialAnd_sa"
CombinatorialAnd.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def CombinatorialOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """CombinatorialOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Combinatorial Or operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this combinatorial operation.
    in_raster_or_constant2 -- The second input to use in this combinatorial operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        out_raster = "#"
        result = arcpy.gp.CombinatorialOr_sa(
            in_raster_or_constant1,
            in_raster_or_constant2,
            out_raster)
        return _wrapToolRaster(u"CombinatorialOr_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
CombinatorialOr.__esri_toolname__ = "CombinatorialOr_sa"
CombinatorialOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def CombinatorialXOr(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """CombinatorialXOr(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Combinatorial eXclusive Or operation on the cell values of two input rasters.

    Arguments:
    in_raster_or_constant1 -- The first input to use in this combinatorial operation.
    in_raster_or_constant2 -- The second input to use in this combinatorial operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        out_raster = "#"
        result = arcpy.gp.CombinatorialXOr_sa(
            in_raster_or_constant1,
            in_raster_or_constant2,
            out_raster)
        return _wrapToolRaster(u"CombinatorialXOr_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
CombinatorialXOr.__esri_toolname__ = "CombinatorialXOr_sa"
CombinatorialXOr.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def EqualTo(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """EqualTo(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational equal-to operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input that will be compared to for equality by the second input.
    in_raster_or_constant2 -- The input that will be compared from for equality by the first input.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"EqualTo_sa",
            ["EqualTo", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
EqualTo.__esri_toolname__ = "EqualTo_sa"
EqualTo.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def GreaterThan(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """GreaterThan(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational greater-than operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input being tested to determine if it is greater than the second input.
    in_raster_or_constant2 -- The input against which the first input is tested to be greater than.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"GreaterThan_sa",
            ["GreaterThan", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
GreaterThan.__esri_toolname__ = "GreaterThan_sa"
GreaterThan.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def GreaterThanEqual(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """GreaterThanEqual(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational greater-than-or-equal-to operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input being tested to determine if it is greater than or equal to the second input.
    in_raster_or_constant2 -- The input against which the first input is tested to be greater than or equal to.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"GreaterThanEqual_sa",
            ["GreaterThanEqual", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
GreaterThanEqual.__esri_toolname__ = "GreaterThanEqual_sa"
GreaterThanEqual.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def IsNull(
        in_raster):
    """IsNull(in_raster)

    Determines which values from the input raster are NoData on a cell-by-cell basis.

    Arguments:
    in_raster -- The input raster being tested to identify the cells that are NoData (null).

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster):
        return _wrapLocalFunctionRaster(u"IsNull_sa",
            ["IsNull", in_raster])
    return Wrapper(
        in_raster)
IsNull.__esri_toolname__ = "IsNull_sa"
IsNull.__esri_toolinfo__ = [
    "::::1"
]


def LessThan(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """LessThan(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational less-than operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input being tested to determine if it is less than the second input.
    in_raster_or_constant2 -- The input against which the first input is tested to be less than.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"LessThan_sa",
            ["LessThan", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
LessThan.__esri_toolname__ = "LessThan_sa"
LessThan.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def LessThanEqual(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """LessThanEqual(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational less-than-or-equal-to operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input being tested to determine if it is less than or equal to the second input.
    in_raster_or_constant2 -- The input against which the first input is tested to be less than or equal to.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"LessThanEqual_sa",
            ["LessThanEqual", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
LessThanEqual.__esri_toolname__ = "LessThanEqual_sa"
LessThanEqual.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def NotEqual(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """NotEqual(in_raster_or_constant1, in_raster_or_constant2)

    Performs a Relational not-equal-to operation on two inputs on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input that will be compared to for inequality by the second input.
    in_raster_or_constant2 -- The input that will be compared from for inequality by the first input.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"NotEqual_sa",
            ["NotEqual", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
NotEqual.__esri_toolname__ = "NotEqual_sa"
NotEqual.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Test(
        in_raster,
        where_clause):
    """Test(in_raster, where_clause)

    Performs a Boolean evaluation of the input raster using a logical expression.

    Arguments:
    in_raster -- The input raster on which the Boolean evaluation is performed, based on a logical expression.
    where_clause -- The logical expression that will determine which input cells will return a value of true (1) and which will be false (0).

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            where_clause):
        out_raster = "#"
        result = arcpy.gp.Test_sa(
            in_raster,
            where_clause,
            out_raster)
        return _wrapToolRaster(u"Test_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        where_clause)
Test.__esri_toolname__ = "Test_sa"
Test.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Minus(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Minus(in_raster_or_constant1, in_raster_or_constant2)

    Subtracts the value of the second input raster from the value of the first input raster on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input from which to subtract the values in the second input.
    in_raster_or_constant2 -- The input values to subtract from the values in the first input.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Minus_sa",
            ["Minus", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Minus.__esri_toolname__ = "Minus_sa"
Minus.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Mod(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Mod(in_raster_or_constant1, in_raster_or_constant2)

    Finds the remainder (modulo) of the first raster when divided by the second raster on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The numerator input.
    in_raster_or_constant2 -- The denominator input.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Mod_sa",
            ["Mod", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Mod.__esri_toolname__ = "Mod_sa"
Mod.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Negate(
        in_raster_or_constant):
    """Negate(in_raster_or_constant)

    Changes the sign (multiplies by -1) of the cell values of the input raster on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant -- The input raster to be negated (multiplied by -1).

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Negate_sa",
            ["Negate", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Negate.__esri_toolname__ = "Negate_sa"
Negate.__esri_toolinfo__ = [
    "::::1"
]


def Plus(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Plus(in_raster_or_constant1, in_raster_or_constant2)

    Adds (sums) the values of two rasters on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input whose values will be added to.
    in_raster_or_constant2 -- The input whose values will be added to the first input.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Plus_sa",
            ["Plus", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Plus.__esri_toolname__ = "Plus_sa"
Plus.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Power(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Power(in_raster_or_constant1, in_raster_or_constant2)

    Raises the cell values in a raster to the power of the values found in another raster.

    Arguments:
    in_raster_or_constant1 -- The input values to be raised to the power defined by the second input.
    in_raster_or_constant2 -- The input that determines the power the values in the first input will be raised to.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Power_sa",
            ["Power", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Power.__esri_toolname__ = "Power_sa"
Power.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def RoundDown(
        in_raster_or_constant):
    """RoundDown(in_raster_or_constant)

    Returns the next lower integer value, just represented as a floating point, for each cell in a raster.

    Arguments:
    in_raster_or_constant -- The input values to be rounded down.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"RoundDown_sa",
            ["RoundDown", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
RoundDown.__esri_toolname__ = "RoundDown_sa"
RoundDown.__esri_toolinfo__ = [
    "::::1"
]


def RoundUp(
        in_raster_or_constant):
    """RoundUp(in_raster_or_constant)

    Returns the next higher integer value, just represented as a floating point, for each cell in a raster.

    Arguments:
    in_raster_or_constant -- The input values to be rounded up.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"RoundUp_sa",
            ["RoundUp", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
RoundUp.__esri_toolname__ = "RoundUp_sa"
RoundUp.__esri_toolinfo__ = [
    "::::1"
]


def Square(
        in_raster_or_constant):
    """Square(in_raster_or_constant)

    Calculates the square of the cell values in a raster.

    Arguments:
    in_raster_or_constant -- The input values to find the square of.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Square_sa",
            ["Square", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Square.__esri_toolname__ = "Square_sa"
Square.__esri_toolinfo__ = [
    "::::1"
]


def SquareRoot(
        in_raster_or_constant):
    """SquareRoot(in_raster_or_constant)

    Calculates the square root of the cell values in a raster.

    Arguments:
    in_raster_or_constant -- The input values to find the square root of.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"SquareRoot_sa",
            ["SquareRoot", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
SquareRoot.__esri_toolname__ = "SquareRoot_sa"
SquareRoot.__esri_toolinfo__ = [
    "::::1"
]


def Times(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Times(in_raster_or_constant1, in_raster_or_constant2)

    Multiplies the values of two rasters on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input containing the values to be multiplied.
    in_raster_or_constant2 -- The input containing the values by which the first input will be multiplied.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Times_sa",
            ["Times", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Times.__esri_toolname__ = "Times_sa"
Times.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ACos(
        in_raster_or_constant):
    """ACos(in_raster_or_constant)

    Calculates the inverse cosine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse cosine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ACos_sa",
            ["ACos", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ACos.__esri_toolname__ = "ACos_sa"
ACos.__esri_toolinfo__ = [
    "::::1"
]


def ACosH(
        in_raster_or_constant):
    """ACosH(in_raster_or_constant)

    Calculates the inverse hyperbolic cosine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse hyperbolic cosine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ACosH_sa",
            ["ACosH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ACosH.__esri_toolname__ = "ACosH_sa"
ACosH.__esri_toolinfo__ = [
    "::::1"
]


def ASin(
        in_raster_or_constant):
    """ASin(in_raster_or_constant)

    Calculates the inverse sine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse sine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ASin_sa",
            ["ASin", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ASin.__esri_toolname__ = "ASin_sa"
ASin.__esri_toolinfo__ = [
    "::::1"
]


def ASinH(
        in_raster_or_constant):
    """ASinH(in_raster_or_constant)

    Calculates the inverse hyperbolic sine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse hyperbolic sine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ASinH_sa",
            ["ASinH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ASinH.__esri_toolname__ = "ASinH_sa"
ASinH.__esri_toolinfo__ = [
    "::::1"
]


def ATan(
        in_raster_or_constant):
    """ATan(in_raster_or_constant)

    Calculates the inverse tangent of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse tangent values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ATan_sa",
            ["ATan", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ATan.__esri_toolname__ = "ATan_sa"
ATan.__esri_toolinfo__ = [
    "::::1"
]


def ATan2(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """ATan2(in_raster_or_constant1, in_raster_or_constant2)

    Calculates the inverse tangent (based on x,y) of cells in a raster.

    Arguments:
    in_raster_or_constant1 -- The input that specifies the numerator, or y value, to use when calculating the inverse tangent.
    in_raster_or_constant2 -- The input that specifies the denominator, or x value, to use when calculating the inverse tangent.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"ATan2_sa",
            ["ATan2", in_raster_or_constant1, in_raster_or_constant2])
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
ATan2.__esri_toolname__ = "ATan2_sa"
ATan2.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ATanH(
        in_raster_or_constant):
    """ATanH(in_raster_or_constant)

    Calculates the inverse hyperbolic tangent of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the inverse hyperbolic tangent values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"ATanH_sa",
            ["ATanH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
ATanH.__esri_toolname__ = "ATanH_sa"
ATanH.__esri_toolinfo__ = [
    "::::1"
]


def Cos(
        in_raster_or_constant):
    """Cos(in_raster_or_constant)

    Calculates the cosine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the cosine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Cos_sa",
            ["Cos", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Cos.__esri_toolname__ = "Cos_sa"
Cos.__esri_toolinfo__ = [
    "::::1"
]


def CosH(
        in_raster_or_constant):
    """CosH(in_raster_or_constant)

    Calculates the hyperbolic cosine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the hyperbolic cosine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"CosH_sa",
            ["CosH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
CosH.__esri_toolname__ = "CosH_sa"
CosH.__esri_toolinfo__ = [
    "::::1"
]


def Sin(
        in_raster_or_constant):
    """Sin(in_raster_or_constant)

    Calculates the sine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the sine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Sin_sa",
            ["Sin", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Sin.__esri_toolname__ = "Sin_sa"
Sin.__esri_toolinfo__ = [
    "::::1"
]


def SinH(
        in_raster_or_constant):
    """SinH(in_raster_or_constant)

    Calculates the hyperbolic sine of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the hyperbolic sine values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"SinH_sa",
            ["SinH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
SinH.__esri_toolname__ = "SinH_sa"
SinH.__esri_toolinfo__ = [
    "::::1"
]


def Tan(
        in_raster_or_constant):
    """Tan(in_raster_or_constant)

    Calculates the tangent of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input for which to calculate the tangent values.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"Tan_sa",
            ["Tan", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
Tan.__esri_toolname__ = "Tan_sa"
Tan.__esri_toolinfo__ = [
    "::::1"
]


def TanH(
        in_raster_or_constant):
    """TanH(in_raster_or_constant)

    Calculates the hyperbolic tangent of cells in a raster.

    Arguments:
    in_raster_or_constant -- The input to calculate the hyperbolic tangent values for.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant):
        return _wrapLocalFunctionRaster(u"TanH_sa",
            ["TanH", in_raster_or_constant])
    return Wrapper(
        in_raster_or_constant)
TanH.__esri_toolname__ = "TanH_sa"
TanH.__esri_toolinfo__ = [
    "::::1"
]


def BandCollectionStats(
        in_raster_bands,
        out_stat_file,
        compute_matrices="#"):
    """BandCollectionStats([in_raster_band,...], out_stat_file, {compute_matrices})

    Calculates the statistics for a set of raster bands.

    Arguments:
    in_raster_band -- The input raster bands.
    out_stat_file -- The output ASCII file containing the statistics.
    compute_matrices -- Specifies whether covariance and correlation matrices are calculated."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster_bands,
            out_stat_file,
            compute_matrices):
        result = arcpy.gp.BandCollectionStats_sa(
            in_raster_bands,
            out_stat_file,
            compute_matrices)
        return result
    return Wrapper(
        in_raster_bands,
        out_stat_file,
        compute_matrices)
BandCollectionStats.__esri_toolname__ = "BandCollectionStats_sa"
BandCollectionStats.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3"
]


def ClassProbability(
        in_raster_bands,
        in_signature_file,
        maximum_output_value="#",
        a_priori_probabilities="#",
        in_a_priori_file="#"):
    """ClassProbability([in_raster_band,...], in_signature_file, {maximum_output_value}, {a_priori_probabilities}, {in_a_priori_file})

    Creates a multiband raster of probability bands, with one band being created for each class represented in the input signature file.

    Arguments:
    in_raster_band -- The input raster bands.
    in_signature_file -- Input signature file whose class signatures are used to generate the a priori probability bands.
    maximum_output_value -- Factor for scaling the range of values in the output probability bands.
    a_priori_probabilities -- Specifies how a priori probabilities will be determined.
    in_a_priori_file -- A text file containing a priori probabilities for the input signature classes.

    Results:
    out_multiband_raster -- Output multiband raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_bands,
            in_signature_file,
            maximum_output_value,
            a_priori_probabilities,
            in_a_priori_file):
        out_multiband_raster = "#"
        result = arcpy.gp.ClassProbability_sa(
            in_raster_bands,
            in_signature_file,
            out_multiband_raster,
            maximum_output_value,
            a_priori_probabilities,
            in_a_priori_file)
        return _wrapToolRaster(u"ClassProbability_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_bands,
        in_signature_file,
        maximum_output_value,
        a_priori_probabilities,
        in_a_priori_file)
ClassProbability.__esri_toolname__ = "ClassProbability_sa"
ClassProbability.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6"
]


def CreateSignatures(
        in_raster_bands,
        in_sample_data,
        out_signature_file,
        compute_covariance="#",
        sample_field="#"):
    """CreateSignatures([in_raster_band,...], in_sample_data, out_signature_file, {compute_covariance}, {sample_field})

    Creates an ASCII signature file of classes defined by input sample data and a set of raster bands.

    Arguments:
    in_raster_band -- The input raster bands for which to create the signatures.
    in_sample_data -- The input delineating the set of class samples.
    out_signature_file -- The output signature file.
    compute_covariance -- Specifies whether covariance matrices in addition to the means are calculated.
    sample_field -- Field of the input raster or feature sample data to assign values to the sampled locations (classes)."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster_bands,
            in_sample_data,
            out_signature_file,
            compute_covariance,
            sample_field):
        result = arcpy.gp.CreateSignatures_sa(
            in_raster_bands,
            in_sample_data,
            out_signature_file,
            compute_covariance,
            sample_field)
        return result
    return Wrapper(
        in_raster_bands,
        in_sample_data,
        out_signature_file,
        compute_covariance,
        sample_field)
CreateSignatures.__esri_toolname__ = "CreateSignatures_sa"
CreateSignatures.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def Dendrogram(
        in_signature_file,
        out_dendrogram_file,
        distance_calculation="#",
        line_width="#"):
    """Dendrogram(in_signature_file, out_dendrogram_file, {distance_calculation}, {line_width})

    Constructs a tree diagram (dendrogram) showing attribute distances between sequentially merged classes in a signature file.

    Arguments:
    in_signature_file -- Input signature file whose class signatures are used to produce a dendrogram.
    out_dendrogram_file -- The output dendrogram ASCII file.
    distance_calculation -- Specifies the manner in which the distances between classes in multidimensional attribute space are defined.
    line_width -- Sets the width of the dendrogram in number of characters on a line."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_signature_file,
            out_dendrogram_file,
            distance_calculation,
            line_width):
        result = arcpy.gp.Dendrogram_sa(
            in_signature_file,
            out_dendrogram_file,
            distance_calculation,
            line_width)
        return result
    return Wrapper(
        in_signature_file,
        out_dendrogram_file,
        distance_calculation,
        line_width)
Dendrogram.__esri_toolname__ = "Dendrogram_sa"
Dendrogram.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4"
]


def EditSignatures(
        in_raster_bands,
        in_signature_file,
        in_signature_remap_file,
        out_signature_file,
        sample_interval="#"):
    """EditSignatures([in_raster_band,...], in_signature_file, in_signature_remap_file, out_signature_file, {sample_interval})

    Edits and updates a signature file by merging, renumbering, and deleting class signatures.

    Arguments:
    in_raster_band -- The input raster bands for which to edit the signatures.
    in_signature_file -- Input signature file whose class signatures are to be edited.
    in_signature_remap_file -- Input ASCII remap table containing the class IDs to be merged, renumbered, or deleted.
    out_signature_file -- The output signature file.
    sample_interval -- The interval to be used for sampling."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster_bands,
            in_signature_file,
            in_signature_remap_file,
            out_signature_file,
            sample_interval):
        result = arcpy.gp.EditSignatures_sa(
            in_raster_bands,
            in_signature_file,
            in_signature_remap_file,
            out_signature_file,
            sample_interval)
        return result
    return Wrapper(
        in_raster_bands,
        in_signature_file,
        in_signature_remap_file,
        out_signature_file,
        sample_interval)
EditSignatures.__esri_toolname__ = "EditSignatures_sa"
EditSignatures.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def IsoCluster(
        in_raster_bands,
        out_signature_file,
        number_classes,
        number_iterations="#",
        min_class_size="#",
        sample_interval="#"):
    """IsoCluster([in_raster_band,...], out_signature_file, number_classes, {number_iterations}, {min_class_size}, {sample_interval})

    Uses an isodata clustering algorithm to determine the characteristics of the natural groupings of cells in multidimensional attribute space and stores the results in an output ASCII signature file.

    Arguments:
    in_raster_band -- The input raster bands.
    out_signature_file -- The output signature file.
    number_classes -- Number of classes into which to group the cells.
    number_iterations -- Number of iterations of the clustering process to run.
    min_class_size -- Minimum number of cells in a valid class.
    sample_interval -- The interval to be used for sampling."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster_bands,
            out_signature_file,
            number_classes,
            number_iterations,
            min_class_size,
            sample_interval):
        result = arcpy.gp.IsoCluster_sa(
            in_raster_bands,
            out_signature_file,
            number_classes,
            number_iterations,
            min_class_size,
            sample_interval)
        return result
    return Wrapper(
        in_raster_bands,
        out_signature_file,
        number_classes,
        number_iterations,
        min_class_size,
        sample_interval)
IsoCluster.__esri_toolname__ = "IsoCluster_sa"
IsoCluster.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def MLClassify(
        in_raster_bands,
        in_signature_file,
        reject_fraction="#",
        a_priori_probabilities="#",
        in_a_priori_file="#",
        out_confidence_raster="#"):
    """MLClassify([in_raster_band,...], in_signature_file, {reject_fraction}, {a_priori_probabilities}, {in_a_priori_file}, {out_confidence_raster})

    Performs a maximum likelihood classification on a set of raster bands and creates a classified raster as output.

    Arguments:
    in_raster_band -- The input raster bands.
    in_signature_file -- The input signature file whose class signatures are used by the maximum likelihood classifier.
    reject_fraction -- The portion of cells that will remain unclassified due to the lowest possibility of correct assignments.
    a_priori_probabilities -- Specifies how a priori probabilities will be determined.
    in_a_priori_file -- A text file containing a priori probabilities for the input signature classes.
    out_confidence_raster -- Output confidence raster dataset showing the certainty of the classification in 14 levels of confidence, with the lowest values representing the highest reliability.

    Results:
    out_classified_raster -- Output classified raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_bands,
            in_signature_file,
            reject_fraction,
            a_priori_probabilities,
            in_a_priori_file,
            out_confidence_raster):
        out_classified_raster = "#"
        result = arcpy.gp.MLClassify_sa(
            in_raster_bands,
            in_signature_file,
            out_classified_raster,
            reject_fraction,
            a_priori_probabilities,
            in_a_priori_file,
            out_confidence_raster)
        return _wrapToolRaster(u"MLClassify_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_bands,
        in_signature_file,
        reject_fraction,
        a_priori_probabilities,
        in_a_priori_file,
        out_confidence_raster)
MLClassify.__esri_toolname__ = "MLClassify_sa"
MLClassify.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def PrincipalComponents(
        in_raster_bands,
        number_components="#",
        out_data_file="#"):
    """PrincipalComponents([in_raster_band,...], {number_components}, {out_data_file})

    Performs Principal Component Analysis (PCA) on a set of raster bands and generates a single multiband raster as output.

    Arguments:
    in_raster_band -- The input raster bands.
    number_components -- Number of principal components.
    out_data_file -- Output ASCII data file storing principal component parameters.

    Results:
    out_multiband_raster -- Output multiband raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_bands,
            number_components,
            out_data_file):
        out_multiband_raster = "#"
        result = arcpy.gp.PrincipalComponents_sa(
            in_raster_bands,
            out_multiband_raster,
            number_components,
            out_data_file)
        return _wrapToolRaster(u"PrincipalComponents_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_bands,
        number_components,
        out_data_file)
PrincipalComponents.__esri_toolname__ = "PrincipalComponents_sa"
PrincipalComponents.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def BlockStatistics(
        in_raster,
        neighborhood="#",
        statistics_type="#",
        ignore_nodata="#"):
    """BlockStatistics(in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})

    Partitions the input into non-overlapping blocks and calculates the statistic of the values within each block. The value is assigned to all of the cells in each block in the output.

    Arguments:
    in_raster -- The raster on which to perform the block statistics calculations.
    neighborhood -- The Neighborhood class dictates the shape of the area around each cell used to calculate the statistic.
    statistics_type -- The statistic type to be calculated.
    ignore_nodata -- Denotes whether NoData values are ignored by the statistic calculation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            neighborhood,
            statistics_type,
            ignore_nodata):
        neighborhood = Utils.compoundParameterToString(neighborhood, ParameterClasses._Neighborhood)
        out_raster = "#"
        result = arcpy.gp.BlockStatistics_sa(
            in_raster,
            out_raster,
            neighborhood,
            statistics_type,
            ignore_nodata)
        return _wrapToolRaster(u"BlockStatistics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        neighborhood,
        statistics_type,
        ignore_nodata)
BlockStatistics.__esri_toolname__ = "BlockStatistics_sa"
BlockStatistics.__esri_toolinfo__ = [
    "::::1",
    "Python::NbrAnnulus|NbrCircle|NbrIrregular|NbrRectangle|NbrWedge|NbrWeight::",
    "::::4",
    "::::5"
]


def Filter(
        in_raster,
        filter_type="#",
        ignore_nodata="#"):
    """Filter(in_raster, {filter_type}, {ignore_nodata})

    Performs either a smoothing (Low pass) or edge-enhancing (High pass) filter on a raster.

    Arguments:
    in_raster -- The input raster on which to perform the filter operation.
    filter_type -- The type of filter operation to perform.
    ignore_nodata -- Denotes whether NoData values are ignored by the filter calculation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            filter_type,
            ignore_nodata):
        out_raster = "#"
        result = arcpy.gp.Filter_sa(
            in_raster,
            out_raster,
            filter_type,
            ignore_nodata)
        return _wrapToolRaster(u"Filter_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        filter_type,
        ignore_nodata)
Filter.__esri_toolname__ = "Filter_sa"
Filter.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def FocalFlow(
        in_surface_raster,
        threshold_value="#"):
    """FocalFlow(in_surface_raster, {threshold_value})

    Determines the flow of the values in the input raster within each cell's immediate neighborhood.

    Arguments:
    in_surface_raster -- The input surface raster for which to calculate the focal flow.
    threshold_value -- Defines a value that constitutes the threshold, which must be equaled or exceeded before flow can occur.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_surface_raster,
            threshold_value):
        out_raster = "#"
        result = arcpy.gp.FocalFlow_sa(
            in_surface_raster,
            out_raster,
            threshold_value)
        return _wrapToolRaster(u"FocalFlow_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_surface_raster,
        threshold_value)
FocalFlow.__esri_toolname__ = "FocalFlow_sa"
FocalFlow.__esri_toolinfo__ = [
    "::::1",
    "::::3"
]


def FocalStatistics(
        in_raster,
        neighborhood="#",
        statistics_type="#",
        ignore_nodata="#"):
    """FocalStatistics(in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})

    Calculates for each input cell location a statistic of the values within a specified neighborhood around it.

    Arguments:
    in_raster -- The raster to perform the focal statistics calculations on.
    neighborhood -- The Neighborhood class dictates the shape of the area around each cell used to calculate the statistic.
    statistics_type -- The statistic type to be calculated.
    ignore_nodata -- Denotes whether NoData values are ignored by the statistic calculation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            neighborhood,
            statistics_type,
            ignore_nodata):
        neighborhood = Utils.compoundParameterToString(neighborhood, ParameterClasses._Neighborhood)
        out_raster = "#"
        result = arcpy.gp.FocalStatistics_sa(
            in_raster,
            out_raster,
            neighborhood,
            statistics_type,
            ignore_nodata)
        return _wrapToolRaster(u"FocalStatistics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        neighborhood,
        statistics_type,
        ignore_nodata)
FocalStatistics.__esri_toolname__ = "FocalStatistics_sa"
FocalStatistics.__esri_toolinfo__ = [
    "::::1",
    "Python::NbrAnnulus|NbrCircle|NbrIrregular|NbrRectangle|NbrWedge|NbrWeight::",
    "::::4",
    "::::5"
]


def LineStatistics(
        in_polyline_features,
        field,
        cell_size="#",
        search_radius="#",
        statistics_type="#"):
    """LineStatistics(in_polyline_features, field, {cell_size}, {search_radius}, {statistics_type})

    Calculates a statistic on the attributes of lines in a circular neighborhood around each output cell.

    Arguments:
    in_polyline_features -- The input polyline features for which to calculate the statistics  in a neighbourhood around each output cell.
    field -- The field that the specified statistic will be calculated for. It can be any numeric field of the input features.
    cell_size -- Cell size for output raster dataset.
    search_radius -- Search radius to calculate the desired statistic within, in map units.
    statistics_type -- The statistic type to be calculated.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_polyline_features,
            field,
            cell_size,
            search_radius,
            statistics_type):
        out_raster = "#"
        result = arcpy.gp.LineStatistics_sa(
            in_polyline_features,
            field,
            out_raster,
            cell_size,
            search_radius,
            statistics_type)
        return _wrapToolRaster(u"LineStatistics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_polyline_features,
        field,
        cell_size,
        search_radius,
        statistics_type)
LineStatistics.__esri_toolname__ = "LineStatistics_sa"
LineStatistics.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6"
]


def PointStatistics(
        in_point_features,
        field,
        cell_size="#",
        neighborhood="#",
        statistics_type="#"):
    """PointStatistics(in_point_features, field, {cell_size}, {neighborhood}, {statistics_type})

    Calculates a statistic on the points in a neighborhood around each output cell.

    Arguments:
    in_point_features -- The input point features for which to calculate the statistics in a neighborhood around each output cell.
    field -- The field that the specified statistic will be calculated for. It can be any numeric field of the input features.
    cell_size -- Cell size for output raster dataset.
    neighborhood -- The Neighborhood class dictates the shape of the area around each input point used to calculate the statistic.
    statistics_type -- The statistic type to be calculated.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            field,
            cell_size,
            neighborhood,
            statistics_type):
        neighborhood = Utils.compoundParameterToString(neighborhood, ParameterClasses._Neighborhood)
        out_raster = "#"
        result = arcpy.gp.PointStatistics_sa(
            in_point_features,
            field,
            out_raster,
            cell_size,
            neighborhood,
            statistics_type)
        return _wrapToolRaster(u"PointStatistics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        field,
        cell_size,
        neighborhood,
        statistics_type)
PointStatistics.__esri_toolname__ = "PointStatistics_sa"
PointStatistics.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "Python::NbrAnnulus|NbrCircle|NbrRectangle|NbrWedge::",
    "::::6"
]


def WeightedOverlay(
        in_weighted_overlay_table):
    """WeightedOverlay(in_weighted_overlay_table)

    Overlays several rasters using a common measurement scale and weights each according to its importance.

    Arguments:
    in_weighted_overlay_table -- The Weighted Overlay  tool allows the calculation of a multiple-criteria analysis between several rasters.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_weighted_overlay_table):
        in_weighted_overlay_table = Utils.compoundParameterToString(in_weighted_overlay_table, ParameterClasses.WOTable)
        out_raster = "#"
        result = arcpy.gp.WeightedOverlay_sa(
            in_weighted_overlay_table,
            out_raster)
        return _wrapToolRaster(u"WeightedOverlay_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_weighted_overlay_table)
WeightedOverlay.__esri_toolname__ = "WeightedOverlay_sa"
WeightedOverlay.__esri_toolinfo__ = [
    "Python::WOTable::"
]


def CreateConstantRaster(
        constant_value,
        data_type="#",
        cell_size="#",
        extent="#"):
    """CreateConstantRaster(constant_value, {data_type}, {cell_size}, {extent})

    Creates a raster of a constant value within the extent and cell size of the analysis window.

    Arguments:
    constant_value -- The constant value with which to populate all the cells in the output raster.
    data_type -- Data type of the output raster dataset.
    cell_size -- The cell size for the output raster dataset.
    extent -- The extent for the output raster dataset.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            constant_value,
            data_type,
            cell_size,
            extent):
        extent = Utils.compoundParameterToString(extent, arcpy.Extent)
        out_raster = "#"
        result = arcpy.gp.CreateConstantRaster_sa(
            out_raster,
            constant_value,
            data_type,
            cell_size,
            extent)
        return _wrapToolRaster(u"CreateConstantRaster_sa", unicode(result.getOutput(0)))
    return Wrapper(
        constant_value,
        data_type,
        cell_size,
        extent)
CreateConstantRaster.__esri_toolname__ = "CreateConstantRaster_sa"
CreateConstantRaster.__esri_toolinfo__ = [
    "::::2",
    "::::3",
    "::::4",
    "Python::Extent::"
]


def CreateNormalRaster(
        cell_size="#",
        extent="#"):
    """CreateNormalRaster({cell_size}, {extent})

    Creates a raster of random values with a normal (gaussian) distribution within the extent and cell size of the analysis window.

    Arguments:
    cell_size -- The cell size for the output raster dataset.
    extent -- The extent for the output raster dataset.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            cell_size,
            extent):
        extent = Utils.compoundParameterToString(extent, arcpy.Extent)
        out_raster = "#"
        result = arcpy.gp.CreateNormalRaster_sa(
            out_raster,
            cell_size,
            extent)
        return _wrapToolRaster(u"CreateNormalRaster_sa", unicode(result.getOutput(0)))
    return Wrapper(
        cell_size,
        extent)
CreateNormalRaster.__esri_toolname__ = "CreateNormalRaster_sa"
CreateNormalRaster.__esri_toolinfo__ = [
    "::::2",
    "Python::Extent::"
]


def CreateRandomRaster(
        seed_value="#",
        cell_size="#",
        extent="#"):
    """CreateRandomRaster({seed_value}, {cell_size}, {extent})

    Creates a raster of random floating point values between 0.0 and 1.0 within the extent and cell size of the analysis window.

    Arguments:
    seed_value -- A value to be used to reseed the random number generator.
    cell_size -- The cell size for the output raster dataset.
    extent -- The extent for the output raster dataset.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            seed_value,
            cell_size,
            extent):
        extent = Utils.compoundParameterToString(extent, arcpy.Extent)
        out_raster = "#"
        result = arcpy.gp.CreateRandomRaster_sa(
            out_raster,
            seed_value,
            cell_size,
            extent)
        return _wrapToolRaster(u"CreateRandomRaster_sa", unicode(result.getOutput(0)))
    return Wrapper(
        seed_value,
        cell_size,
        extent)
CreateRandomRaster.__esri_toolname__ = "CreateRandomRaster_sa"
CreateRandomRaster.__esri_toolinfo__ = [
    "::::2",
    "::::3",
    "Python::Extent::"
]


def Lookup(
        in_raster,
        lookup_field):
    """Lookup(in_raster, lookup_field)

    Creates a new raster by looking up values found in another field in the table of the input raster.

    Arguments:
    in_raster -- The input raster that contains a field from which to create a new raster.
    lookup_field -- Field containing the desired values for the new raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            lookup_field):
        out_raster = "#"
        result = arcpy.gp.Lookup_sa(
            in_raster,
            lookup_field,
            out_raster)
        return _wrapToolRaster(u"Lookup_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        lookup_field)
Lookup.__esri_toolname__ = "Lookup_sa"
Lookup.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ReclassByASCIIFile(
        in_raster,
        in_remap_file,
        missing_values="#"):
    """ReclassByASCIIFile(in_raster, in_remap_file, {missing_values})

    Reclassifies (or changes) the values of the input cells of a raster using an ASCII remap file.

    Arguments:
    in_raster -- The input raster to be reclassified.
    in_remap_file -- ASCII remap file defining the single values or ranges to be reclassified and the values they will become.
    missing_values -- Denotes whether missing values in the reclass file retain their value or get mapped to NoData.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_remap_file,
            missing_values):
        out_raster = "#"
        result = arcpy.gp.ReclassByASCIIFile_sa(
            in_raster,
            in_remap_file,
            out_raster,
            missing_values)
        return _wrapToolRaster(u"ReclassByASCIIFile_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_remap_file,
        missing_values)
ReclassByASCIIFile.__esri_toolname__ = "ReclassByASCIIFile_sa"
ReclassByASCIIFile.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def ReclassByTable(
        in_raster,
        in_remap_table,
        from_value_field,
        to_value_field,
        output_value_field,
        missing_values="#"):
    """ReclassByTable(in_raster, in_remap_table, from_value_field, to_value_field, output_value_field, {missing_values})

    Reclassifies (or changes) the values of the input cells of a raster using a remap table.

    Arguments:
    in_raster -- The input raster to be reclassified.
    in_remap_table -- Table holding fields defining value ranges to be reclassified and the values they will become.
    from_value_field -- Field holding the beginning value for each value range to be reclassified.
    to_value_field -- Field holding the ending value for each value range to be reclassified.
    output_value_field -- Field holding the integer values to which each range should be changed.
    missing_values -- Denotes whether missing values in the reclass table retain their value or get mapped to NoData.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_remap_table,
            from_value_field,
            to_value_field,
            output_value_field,
            missing_values):
        out_raster = "#"
        result = arcpy.gp.ReclassByTable_sa(
            in_raster,
            in_remap_table,
            from_value_field,
            to_value_field,
            output_value_field,
            out_raster,
            missing_values)
        return _wrapToolRaster(u"ReclassByTable_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_remap_table,
        from_value_field,
        to_value_field,
        output_value_field,
        missing_values)
ReclassByTable.__esri_toolname__ = "ReclassByTable_sa"
ReclassByTable.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::7"
]


def Reclassify(
        in_raster,
        reclass_field,
        remap,
        missing_values="#"):
    """Reclassify(in_raster, reclass_field, remap, {missing_values})

    Reclassifies (or changes) the values in a raster.

    Arguments:
    in_raster -- The input raster to be reclassified.
    reclass_field -- Field denoting the values that will be reclassified.
    remap -- The Remap object is used to specify how to  reclassify values of the input raster.
    missing_values -- Denotes whether missing values in the reclass table retain their value or get mapped to NoData.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            reclass_field,
            remap,
            missing_values):
        remap = Utils.compoundParameterToString(remap, ParameterClasses._Remap)
        out_raster = "#"
        result = arcpy.gp.Reclassify_sa(
            in_raster,
            reclass_field,
            remap,
            out_raster,
            missing_values)
        return _wrapToolRaster(u"Reclassify_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        reclass_field,
        remap,
        missing_values)
Reclassify.__esri_toolname__ = "Reclassify_sa"
Reclassify.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "Python::RemapRange|RemapValue::",
    "::::5"
]


def Slice(
        in_raster,
        number_zones,
        slice_type="#",
        base_output_zone="#"):
    """Slice(in_raster, number_zones, {slice_type}, {base_output_zone})

    Slices or reclassifies the range of values of the input cells into zones of equal interval, equal area, or by natural breaks.

    Arguments:
    in_raster -- The input raster to be reclassified.
    number_zones -- The number of zones  to reclassify the input raster into.
    slice_type -- The manner in which to slice the values in the input raster.
    base_output_zone -- Defines the lowest zone value on the output raster dataset.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            number_zones,
            slice_type,
            base_output_zone):
        out_raster = "#"
        result = arcpy.gp.Slice_sa(
            in_raster,
            out_raster,
            number_zones,
            slice_type,
            base_output_zone)
        return _wrapToolRaster(u"Slice_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        number_zones,
        slice_type,
        base_output_zone)
Slice.__esri_toolname__ = "Slice_sa"
Slice.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5"
]


def Aspect(
        in_raster):
    """Aspect(in_raster)

    Derives aspect from a raster surface. The aspect identifies the downslope direction of the maximum rate of change in value from each cell to its neighbors.

    Arguments:
    in_raster -- The input surface raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster):
        out_raster = "#"
        result = arcpy.gp.Aspect_sa(
            in_raster,
            out_raster)
        return _wrapToolRaster(u"Aspect_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster)
Aspect.__esri_toolname__ = "Aspect_sa"
Aspect.__esri_toolinfo__ = [
    "::::1"
]


def Contour(
        in_raster,
        out_polyline_features,
        contour_interval,
        base_contour="#",
        z_factor="#"):
    """Contour(in_raster, out_polyline_features, contour_interval, {base_contour}, {z_factor})

    Creates a line feature class of contours (isolines) from a raster surface.

    Arguments:
    in_raster -- The input surface raster.
    out_polyline_features -- The output contour polyline features.
    contour_interval -- The interval, or distance, between contour lines.
    base_contour -- The base contour value.
    z_factor -- The unit conversion factor used when generating
contours. The default value is 1."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            out_polyline_features,
            contour_interval,
            base_contour,
            z_factor):
        result = arcpy.gp.Contour_sa(
            in_raster,
            out_polyline_features,
            contour_interval,
            base_contour,
            z_factor)
        return result
    return Wrapper(
        in_raster,
        out_polyline_features,
        contour_interval,
        base_contour,
        z_factor)
Contour.__esri_toolname__ = "Contour_sa"
Contour.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def ContourList(
        in_raster,
        out_polyline_features,
        contour_values):
    """ContourList(in_raster, out_polyline_features, [contour_value,...])

    Creates a feature class of selected contour values from a raster surface.

    Arguments:
    in_raster -- The input surface raster.
    out_polyline_features -- The output contour polyline features.
    contour_value -- List of z-values for which to create contours."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            out_polyline_features,
            contour_values):
        result = arcpy.gp.ContourList_sa(
            in_raster,
            out_polyline_features,
            contour_values)
        return result
    return Wrapper(
        in_raster,
        out_polyline_features,
        contour_values)
ContourList.__esri_toolname__ = "ContourList_sa"
ContourList.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3"
]


def Hillshade(
        in_raster,
        azimuth="#",
        altitude="#",
        model_shadows="#",
        z_factor="#"):
    """Hillshade(in_raster, {azimuth}, {altitude}, {model_shadows}, {z_factor})

    Creates a shaded relief from a surface raster by considering the illumination source angle and shadows.

    Arguments:
    in_raster -- The input surface raster.
    azimuth -- Azimuth angle of the light source.
    altitude -- Altitude angle of the light source above the horizon.
    model_shadows -- Type of shaded relief to be generated.
    z_factor -- Number of ground x,y units in one surface z unit.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            azimuth,
            altitude,
            model_shadows,
            z_factor):
        out_raster = "#"
        result = arcpy.gp.Hillshade_sa(
            in_raster,
            out_raster,
            azimuth,
            altitude,
            model_shadows,
            z_factor)
        return _wrapToolRaster(u"Hillshade_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        azimuth,
        altitude,
        model_shadows,
        z_factor)
Hillshade.__esri_toolname__ = "Hillshade_sa"
Hillshade.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def ObserverPoints(
        in_raster,
        in_observer_point_features,
        z_factor="#",
        curvature_correction="#",
        refractivity_coefficient="#",
        out_agl_raster="#"):
    """ObserverPoints(in_raster, in_observer_point_features, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})

    Identifies which observer points are visible from each raster surface location.

    Arguments:
    in_raster -- The input surface raster.
    in_observer_point_features -- The point feature class that identifies the observer locations.
    z_factor -- Number of ground x,y units in one surface z unit.
    curvature_correction -- Allows correction for the earth's curvature.
    refractivity_coefficient -- Coefficient of the refraction of visible light in air.
    out_agl_raster -- The output above ground level (AGL) raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_observer_point_features,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            out_agl_raster):
        out_raster = "#"
        result = arcpy.gp.ObserverPoints_sa(
            in_raster,
            in_observer_point_features,
            out_raster,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            out_agl_raster)
        return _wrapToolRaster(u"ObserverPoints_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_observer_point_features,
        z_factor,
        curvature_correction,
        refractivity_coefficient,
        out_agl_raster)
ObserverPoints.__esri_toolname__ = "ObserverPoints_sa"
ObserverPoints.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def Slope(
        in_raster,
        output_measurement="#",
        z_factor="#"):
    """Slope(in_raster, {output_measurement}, {z_factor})

    Identifies the slope (gradient, or rate of maximum change in z-value) from each cell of a raster surface.

    Arguments:
    in_raster -- The input surface raster.
    output_measurement -- Determines the measurement units (degrees or percentages) of the output slope data.
    z_factor -- Number of ground x,y units in one surface z unit.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            output_measurement,
            z_factor):
        out_raster = "#"
        result = arcpy.gp.Slope_sa(
            in_raster,
            out_raster,
            output_measurement,
            z_factor)
        return _wrapToolRaster(u"Slope_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        output_measurement,
        z_factor)
Slope.__esri_toolname__ = "Slope_sa"
Slope.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def Viewshed(
        in_raster,
        in_observer_features,
        z_factor="#",
        curvature_correction="#",
        refractivity_coefficient="#",
        out_agl_raster="#"):
    """Viewshed(in_raster, in_observer_features, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {out_agl_raster})

    Determines the raster surface locations visible to a set of observer features.

    Arguments:
    in_raster -- The input surface raster.
    in_observer_features -- The feature class that identifies the observer locations.
    z_factor -- Number of ground x,y units in one surface z unit.
    curvature_correction -- Allows correction for the earth's curvature.
    refractivity_coefficient -- Coefficient of the refraction of visible light in air.
    out_agl_raster -- The output above ground level (AGL) raster.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_observer_features,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            out_agl_raster):
        out_raster = "#"
        result = arcpy.gp.Viewshed_sa(
            in_raster,
            in_observer_features,
            out_raster,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            out_agl_raster)
        return _wrapToolRaster(u"Viewshed_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_observer_features,
        z_factor,
        curvature_correction,
        refractivity_coefficient,
        out_agl_raster)
Viewshed.__esri_toolname__ = "Viewshed_sa"
Viewshed.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7"
]


def TabulateArea(
        in_zone_data,
        zone_field,
        in_class_data,
        class_field,
        out_table,
        processing_cell_size="#"):
    """TabulateArea(in_zone_data, zone_field, in_class_data, class_field, out_table, {processing_cell_size})

    Calculates cross-tabulated areas between two datasets and outputs a table.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    in_class_data -- The dataset that defines the classes that will have their area summarized within each zone.
    class_field -- The field that holds the class values.
    out_table -- Output table that will contain the summary of the area of each class in each zone.
    processing_cell_size -- The processing cell size for the zonal  operation."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            in_class_data,
            class_field,
            out_table,
            processing_cell_size):
        result = arcpy.gp.TabulateArea_sa(
            in_zone_data,
            zone_field,
            in_class_data,
            class_field,
            out_table,
            processing_cell_size)
        return result
    return Wrapper(
        in_zone_data,
        zone_field,
        in_class_data,
        class_field,
        out_table,
        processing_cell_size)
TabulateArea.__esri_toolname__ = "TabulateArea_sa"
TabulateArea.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def ZonalFill(
        in_zone_raster,
        in_weight_raster):
    """ZonalFill(in_zone_raster, in_weight_raster)

    Fills zones using the minimum cell value from a weight raster along the zone boundary.

    Arguments:
    in_zone_raster -- The input raster that defines the zones to be filled.
    in_weight_raster -- Weight, or value,  to be assigned to each zone.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_zone_raster,
            in_weight_raster):
        out_raster = "#"
        result = arcpy.gp.ZonalFill_sa(
            in_zone_raster,
            in_weight_raster,
            out_raster)
        return _wrapToolRaster(u"ZonalFill_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_zone_raster,
        in_weight_raster)
ZonalFill.__esri_toolname__ = "ZonalFill_sa"
ZonalFill.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ZonalGeometry(
        in_zone_data,
        zone_field,
        geometry_type="#",
        cell_size="#"):
    """ZonalGeometry(in_zone_data, zone_field, {geometry_type}, {cell_size})

    Calculates the specified geometry measure (area, perimeter, thickness, or the characteristics of ellipse) for each zone in a dataset.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    geometry_type -- Geometry type to be calculated.
    cell_size -- The processing cell size for the zonal  operation.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            geometry_type,
            cell_size):
        out_raster = "#"
        result = arcpy.gp.ZonalGeometry_sa(
            in_zone_data,
            zone_field,
            out_raster,
            geometry_type,
            cell_size)
        return _wrapToolRaster(u"ZonalGeometry_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_zone_data,
        zone_field,
        geometry_type,
        cell_size)
ZonalGeometry.__esri_toolname__ = "ZonalGeometry_sa"
ZonalGeometry.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5"
]


def ZonalGeometryAsTable(
        in_zone_data,
        zone_field,
        out_table,
        processing_cell_size="#"):
    """ZonalGeometryAsTable(in_zone_data, zone_field, out_table, {processing_cell_size})

    Calculates the geometry measures (area, perimeter, thickness, and the characteristics of ellipse) for each zone in a dataset and reports the results as a table.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    out_table -- Output table that will contain the summary of the values in each zone.
    processing_cell_size -- The processing cell size for the zonal  operation."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            out_table,
            processing_cell_size):
        result = arcpy.gp.ZonalGeometryAsTable_sa(
            in_zone_data,
            zone_field,
            out_table,
            processing_cell_size)
        return result
    return Wrapper(
        in_zone_data,
        zone_field,
        out_table,
        processing_cell_size)
ZonalGeometryAsTable.__esri_toolname__ = "ZonalGeometryAsTable_sa"
ZonalGeometryAsTable.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4"
]


def ZonalStatistics(
        in_zone_data,
        zone_field,
        in_value_raster,
        statistics_type="#",
        ignore_nodata="#"):
    """ZonalStatistics(in_zone_data, zone_field, in_value_raster, {statistics_type}, {ignore_nodata})

    Calculates statistics on values of a raster within the zones of another dataset.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    in_value_raster -- Raster that contains the values on which to calculate a statistic.
    statistics_type -- Statistic type to be calculated.
    ignore_nodata -- Denotes whether NoData values in the Value input will influence the results of the zone that they fall within.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            in_value_raster,
            statistics_type,
            ignore_nodata):
        out_raster = "#"
        result = arcpy.gp.ZonalStatistics_sa(
            in_zone_data,
            zone_field,
            in_value_raster,
            out_raster,
            statistics_type,
            ignore_nodata)
        return _wrapToolRaster(u"ZonalStatistics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_zone_data,
        zone_field,
        in_value_raster,
        statistics_type,
        ignore_nodata)
ZonalStatistics.__esri_toolname__ = "ZonalStatistics_sa"
ZonalStatistics.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::5",
    "::::6"
]


def ZonalStatisticsAsTable(
        in_zone_data,
        zone_field,
        in_value_raster,
        out_table,
        ignore_nodata="#",
        statistics_type="#"):
    """ZonalStatisticsAsTable(in_zone_data, zone_field, in_value_raster, out_table, {ignore_nodata}, {statistics_type})

    Summarizes the values of a raster within the zones of another dataset and reports the results to a table.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    in_value_raster -- Raster that contains the values on which to calculate a statistic.
    out_table -- Output table that will contain the summary of the values in each zone.
    ignore_nodata -- Denotes whether NoData values in the Value input will influence the results of the zone that they fall within.
    statistics_type -- Statistic type to be calculated."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            in_value_raster,
            out_table,
            ignore_nodata,
            statistics_type):
        result = arcpy.gp.ZonalStatisticsAsTable_sa(
            in_zone_data,
            zone_field,
            in_value_raster,
            out_table,
            ignore_nodata,
            statistics_type)
        return result
    return Wrapper(
        in_zone_data,
        zone_field,
        in_value_raster,
        out_table,
        ignore_nodata,
        statistics_type)
ZonalStatisticsAsTable.__esri_toolname__ = "ZonalStatisticsAsTable_sa"
ZonalStatisticsAsTable.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def AreaSolarRadiation(
        in_surface_raster,
        latitude="#",
        sky_size="#",
        time_configuration="#",
        day_interval="#",
        hour_interval="#",
        each_interval="#",
        z_factor="#",
        slope_aspect_input_type="#",
        calculation_directions="#",
        zenith_divisions="#",
        azimuth_divisions="#",
        diffuse_model_type="#",
        diffuse_proportion="#",
        transmittivity="#",
        out_direct_radiation_raster="#",
        out_diffuse_radiation_raster="#",
        out_direct_duration_raster="#"):
    """AreaSolarRadiation(in_surface_raster, {latitude}, {sky_size}, {time_configuration}, {day_interval}, {hour_interval}, {each_interval}, {z_factor}, {slope_aspect_input_type}, {calculation_directions}, {zenith_divisions}, {azimuth_divisions}, {diffuse_model_type}, {diffuse_proportion}, {transmittivity}, {out_direct_radiation_raster}, {out_diffuse_radiation_raster}, {out_direct_duration_raster})

    Derives incoming solar radiation from a raster surface.

    Arguments:
    in_surface_raster -- Input elevation surface raster.
    latitude -- The latitude for the site area. The units are decimal degrees, with positive values for the northern hemisphere and negative for the southern.
    sky_size -- The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.
    time_configuration -- Specifies the time configuration (period) used for calculating solar radiation.
    day_interval -- The time interval through the year (units: days) used for calculation of sky sectors for the sun map.
    hour_interval -- Time interval through the day (units: hours) used for calculation of sky sectors for sun maps.
    each_interval -- Specifies whether to calculate a single total insolation value for all locations or multiple values for the specified hour and day interval.
    z_factor -- The number of ground x,y units in one surface z unit.
    slope_aspect_input_type -- How slope and aspect information are derived for analysis.
    calculation_directions -- The number of azimuth directions used when calculating the viewshed.
    zenith_divisions -- The number of divisions used to create sky sectors in the sky map.
    azimuth_divisions -- The number of divisions used to create sky sectors in the sky map.
    diffuse_model_type -- Type of diffuse radiation model.
    diffuse_proportion -- The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.
    transmittivity -- The fraction of radiation that passes through the atmosphere (averaged over all wavelengths). Values range from 0 (no transmission) to 1 (all transmission).
    out_direct_radiation_raster -- The output raster representing the direct incoming solar radiation for each location.
    out_diffuse_radiation_raster -- The output raster representing the diffuse incoming solar radiation for each location.
    out_direct_duration_raster -- The output raster representing the duration of direct incoming solar radiation.

    Results:
    out_global_radiation_raster -- Output global radiation raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_surface_raster,
            latitude,
            sky_size,
            time_configuration,
            day_interval,
            hour_interval,
            each_interval,
            z_factor,
            slope_aspect_input_type,
            calculation_directions,
            zenith_divisions,
            azimuth_divisions,
            diffuse_model_type,
            diffuse_proportion,
            transmittivity,
            out_direct_radiation_raster,
            out_diffuse_radiation_raster,
            out_direct_duration_raster):
        time_configuration = Utils.compoundParameterToString(time_configuration, ParameterClasses._Time)
        out_global_radiation_raster = "#"
        result = arcpy.gp.AreaSolarRadiation_sa(
            in_surface_raster,
            out_global_radiation_raster,
            latitude,
            sky_size,
            time_configuration,
            day_interval,
            hour_interval,
            each_interval,
            z_factor,
            slope_aspect_input_type,
            calculation_directions,
            zenith_divisions,
            azimuth_divisions,
            diffuse_model_type,
            diffuse_proportion,
            transmittivity,
            out_direct_radiation_raster,
            out_diffuse_radiation_raster,
            out_direct_duration_raster)
        return _wrapToolRaster(u"AreaSolarRadiation_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_surface_raster,
        latitude,
        sky_size,
        time_configuration,
        day_interval,
        hour_interval,
        each_interval,
        z_factor,
        slope_aspect_input_type,
        calculation_directions,
        zenith_divisions,
        azimuth_divisions,
        diffuse_model_type,
        diffuse_proportion,
        transmittivity,
        out_direct_radiation_raster,
        out_diffuse_radiation_raster,
        out_direct_duration_raster)
AreaSolarRadiation.__esri_toolname__ = "AreaSolarRadiation_sa"
AreaSolarRadiation.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "Python::TimeMultipleDays|TimeSpecialDays|TimeWholeYear|TimeWithinDay::",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14",
    "::::15",
    "::::16",
    "::::17",
    "::::18",
    "::::19"
]


def PointsSolarRadiation(
        in_surface_raster,
        in_points_feature_or_table,
        out_global_radiation_features,
        height_offset="#",
        latitude="#",
        sky_size="#",
        time_configuration="#",
        day_interval="#",
        hour_interval="#",
        each_interval="#",
        z_factor="#",
        slope_aspect_input_type="#",
        calculation_directions="#",
        zenith_divisions="#",
        azimuth_divisions="#",
        diffuse_model_type="#",
        diffuse_proportion="#",
        transmittivity="#",
        out_direct_radiation_features="#",
        out_diffuse_radiation_features="#",
        out_direct_duration_features="#"):
    """PointsSolarRadiation(in_surface_raster, in_points_feature_or_table, out_global_radiation_features, {height_offset}, {latitude}, {sky_size}, {time_configuration}, {day_interval}, {hour_interval}, {each_interval}, {z_factor}, {slope_aspect_input_type}, {calculation_directions}, {zenith_divisions}, {azimuth_divisions}, {diffuse_model_type}, {diffuse_proportion}, {transmittivity}, {out_direct_radiation_features}, {out_diffuse_radiation_features}, {out_direct_duration_features})

    Derives incoming solar radiation for specific locations in a point feature class or location table.

    Arguments:
    in_surface_raster -- Input elevation surface raster.
    in_points_feature_or_table -- The input point feature class or table specifying the locations to analyze solar radiation.
    out_global_radiation_features -- The output feature class representing the global radiation or amount of incoming solar insolation (direct + diffuse) calculated for each location.
    height_offset -- The height (in meters) above the DEM surface for which calculations are to be performed.
    latitude -- The latitude for the site area. The units are decimal degrees, with positive values for the northern hemisphere and negative for the southern.
    sky_size -- The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.
    time_configuration -- Specifies the time configuration (period) used for calculating solar radiation.
    day_interval -- The time interval through the year (units: days) used for calculation of sky sectors for the sun map.
    hour_interval -- Time interval through the day (units: hours) used for calculation of sky sectors for sun maps.
    each_interval -- Specifies whether to calculate a single total insolation value for all locations or multiple values for the specified hour and day interval.
    z_factor -- The number of ground x,y units in one surface z unit.
    slope_aspect_input_type -- How slope and aspect information are derived for analysis.
    calculation_directions -- The number of azimuth directions used when calculating the viewshed.
    zenith_divisions -- The number of divisions used to create sky sectors in the sky map.
    azimuth_divisions -- The number of divisions used to create sky sectors in the sky map.
    diffuse_model_type -- Type of diffuse radiation model.
    diffuse_proportion -- The proportion of global normal radiation flux that is diffuse. Values range from 0 to 1.
    transmittivity -- The fraction of radiation that passes through the atmosphere (averaged over all wavelengths). Values range from 0 (no transmission) to 1 (all transmission).
    out_direct_radiation_features -- The output feature class representing the direct incoming solar radiation for each location.
    out_diffuse_radiation_features -- The output feature class representing the incoming solar radiation for each location that is diffuse.
    out_direct_duration_features -- The output feature class representing the duration of direct incoming solar radiation."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_surface_raster,
            in_points_feature_or_table,
            out_global_radiation_features,
            height_offset,
            latitude,
            sky_size,
            time_configuration,
            day_interval,
            hour_interval,
            each_interval,
            z_factor,
            slope_aspect_input_type,
            calculation_directions,
            zenith_divisions,
            azimuth_divisions,
            diffuse_model_type,
            diffuse_proportion,
            transmittivity,
            out_direct_radiation_features,
            out_diffuse_radiation_features,
            out_direct_duration_features):
        time_configuration = Utils.compoundParameterToString(time_configuration, ParameterClasses._Time)
        result = arcpy.gp.PointsSolarRadiation_sa(
            in_surface_raster,
            in_points_feature_or_table,
            out_global_radiation_features,
            height_offset,
            latitude,
            sky_size,
            time_configuration,
            day_interval,
            hour_interval,
            each_interval,
            z_factor,
            slope_aspect_input_type,
            calculation_directions,
            zenith_divisions,
            azimuth_divisions,
            diffuse_model_type,
            diffuse_proportion,
            transmittivity,
            out_direct_radiation_features,
            out_diffuse_radiation_features,
            out_direct_duration_features)
        return result
    return Wrapper(
        in_surface_raster,
        in_points_feature_or_table,
        out_global_radiation_features,
        height_offset,
        latitude,
        sky_size,
        time_configuration,
        day_interval,
        hour_interval,
        each_interval,
        z_factor,
        slope_aspect_input_type,
        calculation_directions,
        zenith_divisions,
        azimuth_divisions,
        diffuse_model_type,
        diffuse_proportion,
        transmittivity,
        out_direct_radiation_features,
        out_diffuse_radiation_features,
        out_direct_duration_features)
PointsSolarRadiation.__esri_toolname__ = "PointsSolarRadiation_sa"
PointsSolarRadiation.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "Python::TimeMultipleDays|TimeSpecialDays|TimeWholeYear|TimeWithinDay::",
    "::::8",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14",
    "::::15",
    "::::16",
    "::::17",
    "::::18",
    "::::19",
    "::::20",
    "::::21"
]


def SolarRadiationGraphics(
        in_surface_raster,
        in_points_feature_or_table="#",
        sky_size="#",
        height_offset="#",
        calculation_directions="#",
        latitude="#",
        time_configuration="#",
        day_interval="#",
        hour_interval="#",
        out_sunmap_raster="#",
        zenith_divisions="#",
        azimuth_divisions="#",
        out_skymap_raster="#"):
    """SolarRadiationGraphics(in_surface_raster, {in_points_feature_or_table}, {sky_size}, {height_offset}, {calculation_directions}, {latitude}, {time_configuration}, {day_interval}, {hour_interval}, {out_sunmap_raster}, {zenith_divisions}, {azimuth_divisions}, {out_skymap_raster})

    Derives raster representations of a hemispherical viewshed, sun map, and sky map, which are used in the calculation of direct, diffuse, and global solar radiation.

    Arguments:
    in_surface_raster -- Input elevation surface raster.
    in_points_feature_or_table -- The input point feature class or table specifying the locations to analyze solar radiation.
    sky_size -- The resolution or sky size for the viewshed, sky map, and sun map rasters. The units are cells.
    height_offset -- The height (in meters) above the DEM surface for which calculations are to be performed.
    calculation_directions -- The number of azimuth directions used when calculating the viewshed.
    latitude -- The latitude for the site area. The units are decimal degrees, with positive values for the northern hemisphere and negative for the southern.
    time_configuration -- Specifies the time configuration (period) used for calculating solar radiation.
    day_interval -- The time interval through the year (units: days) used for calculation of sky sectors for the sun map.
    hour_interval -- Time interval through the day (units: hours) used for calculation of sky sectors for sun maps.
    out_sunmap_raster -- The output sun map raster.
    zenith_divisions -- The number of divisions used to create sky sectors in the sky map.
    azimuth_divisions -- The number of divisions used to create sky sectors in the sky map.
    out_skymap_raster -- The output sky map raster.

    Results:
    out_viewshed_raster -- Output viewshed raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_surface_raster,
            in_points_feature_or_table,
            sky_size,
            height_offset,
            calculation_directions,
            latitude,
            time_configuration,
            day_interval,
            hour_interval,
            out_sunmap_raster,
            zenith_divisions,
            azimuth_divisions,
            out_skymap_raster):
        time_configuration = Utils.compoundParameterToString(time_configuration, ParameterClasses._Time)
        out_viewshed_raster = "#"
        result = arcpy.gp.SolarRadiationGraphics_sa(
            in_surface_raster,
            out_viewshed_raster,
            in_points_feature_or_table,
            sky_size,
            height_offset,
            calculation_directions,
            latitude,
            time_configuration,
            day_interval,
            hour_interval,
            out_sunmap_raster,
            zenith_divisions,
            azimuth_divisions,
            out_skymap_raster)
        return _wrapToolRaster(u"SolarRadiationGraphics_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_surface_raster,
        in_points_feature_or_table,
        sky_size,
        height_offset,
        calculation_directions,
        latitude,
        time_configuration,
        day_interval,
        hour_interval,
        out_sunmap_raster,
        zenith_divisions,
        azimuth_divisions,
        out_skymap_raster)
SolarRadiationGraphics.__esri_toolname__ = "SolarRadiationGraphics_sa"
SolarRadiationGraphics.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "Python::TimeMultipleDays|TimeSpecialDays|TimeWholeYear|TimeWithinDay::",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14"
]


def WeightedSum(
        in_weighted_sum_table):
    """WeightedSum(in_weighted_sum_table)

    Overlays several rasters, multiplying each by their given weight and summing them together.

    Arguments:
    in_weighted_sum_table -- TheWeighted Sum tool overlays several rasters, multiplying each by their given weight and summing them together.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_weighted_sum_table):
        in_weighted_sum_table = Utils.compoundParameterToString(in_weighted_sum_table, ParameterClasses.WSTable)
        out_raster = "#"
        result = arcpy.gp.WeightedSum_sa(
            in_weighted_sum_table,
            out_raster)
        return _wrapToolRaster(u"WeightedSum_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_weighted_sum_table)
WeightedSum.__esri_toolname__ = "WeightedSum_sa"
WeightedSum.__esri_toolinfo__ = [
    "Python::WSTable::"
]


def Diff(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Diff(in_raster_or_constant1, in_raster_or_constant2)

    Determines which values from the first input are logically different from the values of the second input on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant1 -- The input to which the second input will be compared.
    in_raster_or_constant2 -- The input to which the first input will be compared.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        out_raster = "#"
        result = arcpy.gp.Diff_sa(
            in_raster_or_constant1,
            in_raster_or_constant2,
            out_raster)
        return _wrapToolRaster(u"Diff_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Diff.__esri_toolname__ = "Diff_sa"
Diff.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def InList(
        in_raster_or_constant,
        in_raster_or_constants):
    """InList(in_raster_or_constant, [in_raster_or_constant,...])

    Determines which values from the first input are contained in a set of other inputs, on a cell-by-cell basis.

    Arguments:
    in_raster_or_constant -- The input raster whose values will be looked for in the input list.
    in_raster_or_constant -- A list of input rasters in which the cell values from the first input will be looked for.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant,
            in_raster_or_constants):
        out_raster = "#"
        result = arcpy.gp.InList_sa(
            in_raster_or_constant,
            in_raster_or_constants,
            out_raster)
        return _wrapToolRaster(u"InList_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant,
        in_raster_or_constants)
InList.__esri_toolname__ = "InList_sa"
InList.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def Over(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """Over(in_raster_or_constant1, in_raster_or_constant2)

    For the cell values in the first input that are not 0, the output value will be that of the first input. Where the cell values are 0, the output will be that of the second input raster.

    Arguments:
    in_raster_or_constant1 -- The input for which cell values of 0 will be replaced with the value from the second input.
    in_raster_or_constant2 -- The input whose value will be assigned to the output raster cells where the first input value is 0.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        out_raster = "#"
        result = arcpy.gp.Over_sa(
            in_raster_or_constant1,
            in_raster_or_constant2,
            out_raster)
        return _wrapToolRaster(u"Over_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)
Over.__esri_toolname__ = "Over_sa"
Over.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def ContourWithBarriers(
        in_raster,
        out_contour_feature_class,
        in_barrier_features="#",
        in_contour_type="#",
        in_contour_values_file="#",
        explicit_only="#",
        in_base_contour="#",
        in_contour_interval="#",
        in_indexed_contour_interval="#",
        in_explicit_contours="#",
        in_z_factor="#"):
    """ContourWithBarriers(in_raster, out_contour_feature_class, {in_barrier_features}, {in_contour_type}, {in_contour_values_file}, {explicit_only}, {in_base_contour}, {in_contour_interval}, {in_indexed_contour_interval}, {[in_explicit_contour,...]}, {in_z_factor})

    Creates contours from a raster surface. The inclusion of barrier features allows you to independently generate contours on either side of a barrier.

    Arguments:
    in_raster -- The input surface raster.
    out_contour_feature_class -- The output contour features.
    in_barrier_features -- The input barrier features.
    in_contour_type -- The type of contour to create.
    in_contour_values_file -- The base contour, contour interval, indexed contour interval, and explicit contour values can also be specified via a text file.
    explicit_only -- Only explicit contour values are used. Base contour, contour interval, and indexed contour intervals are not specified.
    in_base_contour -- The base contour value.
    in_contour_interval -- The interval, or distance, between contour lines.
    in_indexed_contour_interval -- Contours will also be generated for this interval and will be flagged accordingly in the output feature class.
    in_explicit_contour -- Explicit values at which to create contours.
    in_z_factor -- The unit conversion factor used when generating
contours. The default value is 1."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            out_contour_feature_class,
            in_barrier_features,
            in_contour_type,
            in_contour_values_file,
            explicit_only,
            in_base_contour,
            in_contour_interval,
            in_indexed_contour_interval,
            in_explicit_contours,
            in_z_factor):
        result = arcpy.gp.ContourWithBarriers_sa(
            in_raster,
            out_contour_feature_class,
            in_barrier_features,
            in_contour_type,
            in_contour_values_file,
            explicit_only,
            in_base_contour,
            in_contour_interval,
            in_indexed_contour_interval,
            in_explicit_contours,
            in_z_factor)
        return result
    return Wrapper(
        in_raster,
        out_contour_feature_class,
        in_barrier_features,
        in_contour_type,
        in_contour_values_file,
        explicit_only,
        in_base_contour,
        in_contour_interval,
        in_indexed_contour_interval,
        in_explicit_contours,
        in_z_factor)
ContourWithBarriers.__esri_toolname__ = "ContourWithBarriers_sa"
ContourWithBarriers.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10",
    "::::11"
]


def FuzzyMembership(
        in_raster,
        fuzzy_function="#",
        hedge="#"):
    """FuzzyMembership(in_raster, {fuzzy_function}, {hedge})

    Transforms  the input raster   into a 0 to 1 scale, indicating the strength of a membership in a set, based on a specified fuzzification algorithm.

    Arguments:
    in_raster -- The input raster whose values will be scaled from 0 to 1.
    fuzzy_function -- Specifies the algorithm used in fuzzification of the input raster.
    hedge -- Defining a hedge increases or decreases the fuzzy membership values which modify the meaning of a fuzzy set. Hedges are useful to help in controlling the criteria or important attributes.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            fuzzy_function,
            hedge):
        fuzzy_function = Utils.compoundParameterToString(fuzzy_function, ParameterClasses._FuzzyMembership)
        out_raster = "#"
        result = arcpy.gp.FuzzyMembership_sa(
            in_raster,
            out_raster,
            fuzzy_function,
            hedge)
        return _wrapToolRaster(u"FuzzyMembership_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        fuzzy_function,
        hedge)
FuzzyMembership.__esri_toolname__ = "FuzzyMembership_sa"
FuzzyMembership.__esri_toolinfo__ = [
    "::::1",
    "Python::FuzzyGaussian|FuzzyLarge|FuzzyLinear|FuzzyMSLarge|FuzzyMSSmall|FuzzyNear|FuzzySmall::",
    "::::4"
]


def FuzzyOverlay(
        in_rasters,
        overlay_type="#",
        gamma="#"):
    """FuzzyOverlay([in_raster,...], {overlay_type}, {gamma})

    Combine fuzzy membership rasters data together, based on selected overlay type.

    Arguments:
    in_raster -- A list of input membership rasters to be combined in the overlay.
    overlay_type -- Specifies the method used to combine two or more membership data.
    gamma -- The gamma value to be used.   This is only available when  the Overlay type is set to GAMMA.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_rasters,
            overlay_type,
            gamma):
        out_raster = "#"
        result = arcpy.gp.FuzzyOverlay_sa(
            in_rasters,
            out_raster,
            overlay_type,
            gamma)
        return _wrapToolRaster(u"FuzzyOverlay_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_rasters,
        overlay_type,
        gamma)
FuzzyOverlay.__esri_toolname__ = "FuzzyOverlay_sa"
FuzzyOverlay.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def IsoClusterUnsupervisedClassification(
        in_raster_bands,
        Number_of_classes,
        Minimum_class_size="#",
        Sample_interval="#",
        out_signature_file="#"):
    """IsoClusterUnsupervisedClassification([in_raster_band,...], number_of_classes, {minimum_class_size}, {sample_interval}, {out_signature_file})

    Performs unsupervised classification on a series of input raster bands using the Iso Cluster and Maximum Likelihood Classification tools.

    Arguments:
    in_raster_band -- The input raster bands.
    number_of_classes -- Number of classes into which to group the cells.
    minimum_class_size -- Minimum number of cells in a valid class.
    sample_interval -- The interval to be used for sampling.
    out_signature_file -- The output signature file.

    Results:
    Output_classified_raster -- Output classified raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster_bands,
            Number_of_classes,
            Minimum_class_size,
            Sample_interval,
            out_signature_file):
        Output_classified_raster = "#"
        result = arcpy.gp.IsoClusterUnsupervisedClassification_sa(
            in_raster_bands,
            Number_of_classes,
            Output_classified_raster,
            Minimum_class_size,
            Sample_interval,
            out_signature_file)
        return _wrapToolRaster(u"IsoClusterUnsupervisedClassification_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster_bands,
        Number_of_classes,
        Minimum_class_size,
        Sample_interval,
        out_signature_file)
IsoClusterUnsupervisedClassification.__esri_toolname__ = "IsoClusterUnsupervisedClassification_sa"
IsoClusterUnsupervisedClassification.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6"
]


def ZonalHistogram(
        in_zone_data,
        zone_field,
        in_value_raster,
        out_table,
        out_graph="#"):
    """ZonalHistogram(in_zone_data, zone_field, in_value_raster, out_table, {out_graph})

    Creates a table and a histogram graph that show the frequency distribution of cell values on the Value input for each unique Zone.

    Arguments:
    in_zone_data -- Dataset that defines the zones.
    zone_field -- Field that holds the values that define each zone.
    in_value_raster -- The raster values to create the histograms.
    out_table -- The output table file.
    out_graph -- The name of the output graph for display."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_zone_data,
            zone_field,
            in_value_raster,
            out_table,
            out_graph):
        result = arcpy.gp.ZonalHistogram_sa(
            in_zone_data,
            zone_field,
            in_value_raster,
            out_table,
            out_graph)
        return result
    return Wrapper(
        in_zone_data,
        zone_field,
        in_value_raster,
        out_table,
        out_graph)
ZonalHistogram.__esri_toolname__ = "ZonalHistogram_sa"
ZonalHistogram.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def CutFill(
        in_before_surface,
        in_after_surface,
        z_factor="#"):
    """CutFill(in_before_surface, in_after_surface, {z_factor})

    Calculates the volume change between two surfaces. This is typically used for cut and fill operations.

    Arguments:
    in_before_surface -- The input representing the surface before the cut or fill operation.
    in_after_surface -- The input representing the surface after the cut or fill operation.
    z_factor -- Number of ground x,y units in one surface z unit.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_before_surface,
            in_after_surface,
            z_factor):
        out_raster = "#"
        result = arcpy.gp.CutFill_sa(
            in_before_surface,
            in_after_surface,
            out_raster,
            z_factor)
        return _wrapToolRaster(u"CutFill_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_before_surface,
        in_after_surface,
        z_factor)
CutFill.__esri_toolname__ = "CutFill_sa"
CutFill.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def ExtractByMask(
        in_raster,
        in_mask_data):
    """ExtractByMask(in_raster, in_mask_data)

    Extracts the cells of a raster that correspond to the areas defined by a mask.

    Arguments:
    in_raster -- The input raster from which cells will be extracted.
    in_mask_data -- Input mask data defining areas to extract.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_mask_data):
        out_raster = "#"
        result = arcpy.gp.ExtractByMask_sa(
            in_raster,
            in_mask_data,
            out_raster)
        return _wrapToolRaster(u"ExtractByMask_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_mask_data)
ExtractByMask.__esri_toolname__ = "ExtractByMask_sa"
ExtractByMask.__esri_toolinfo__ = [
    "::::1",
    "::::2"
]


def SplineWithBarriers(
        in_point_features,
        Z_value_field,
        Input_barrier_features="#",
        cell_size="#",
        Smoothing_Factor="#"):
    """SplineWithBarriers(in_point_features, Z_value_field, {Input_barrier_features}, {cell_size}, {Smoothing_Factor})

    Interpolates a raster surface, using barriers, from points using a minimum curvature spline technique. The barriers are entered as either polygon or polyline features.

    Arguments:
    in_point_features -- The input point features containing the z-values to be interpolated into a surface raster.
    Z_value_field -- The field that holds a height or magnitude value for each point.
    Input_barrier_features -- The optional input barrier features to constrain the interpolation.
    cell_size -- The cell size at which the output raster will be created.
    Smoothing_Factor -- The parameter that influences the smoothing of the output surface.

    Results:
    Output_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_point_features,
            Z_value_field,
            Input_barrier_features,
            cell_size,
            Smoothing_Factor):
        Output_raster = "#"
        result = arcpy.gp.SplineWithBarriers_sa(
            in_point_features,
            Z_value_field,
            Input_barrier_features,
            cell_size,
            Output_raster,
            Smoothing_Factor)
        return _wrapToolRaster(u"SplineWithBarriers_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_point_features,
        Z_value_field,
        Input_barrier_features,
        cell_size,
        Smoothing_Factor)
SplineWithBarriers.__esri_toolname__ = "SplineWithBarriers_sa"
SplineWithBarriers.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::6"
]


def Curvature(
        in_raster,
        z_factor="#",
        out_profile_curve_raster="#",
        out_plan_curve_raster="#"):
    """Curvature(in_raster, {z_factor}, {out_profile_curve_raster}, {out_plan_curve_raster})

    Calculates the curvature of a raster surface, optionally including profile and plan curvature.

    Arguments:
    in_raster -- The input surface raster.
    z_factor -- Number of ground x,y units in one surface z unit.
    out_profile_curve_raster -- Output profile curve raster dataset.
    out_plan_curve_raster -- Output plan curve raster dataset.

    Results:
    out_curvature_raster -- Output curvature raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            z_factor,
            out_profile_curve_raster,
            out_plan_curve_raster):
        out_curvature_raster = "#"
        result = arcpy.gp.Curvature_sa(
            in_raster,
            out_curvature_raster,
            z_factor,
            out_profile_curve_raster,
            out_plan_curve_raster)
        return _wrapToolRaster(u"Curvature_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        z_factor,
        out_profile_curve_raster,
        out_plan_curve_raster)
Curvature.__esri_toolname__ = "Curvature_sa"
Curvature.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5"
]


def ExtractMultiValuesToPoints(
        in_point_features,
        in_rasters,
        bilinear_interpolate_values="#"):
    """ExtractMultiValuesToPoints(in_point_features, [[Raster, {Output Field Name}],...], {bilinear_interpolate_values})

    Extracts cell values at locations specified in a point feature class from one or more rasters and records the values to the attribute table of the point feature class.

    Arguments:
    in_point_features -- The input point features to which you want to add raster values.
    Raster, Output Field Name -- The input raster (or rasters) values you want to extract based on the input point feature location.
    bilinear_interpolate_values -- Specifies whether or not interpolation will be used."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_point_features,
            in_rasters,
            bilinear_interpolate_values):
        result = arcpy.gp.ExtractMultiValuesToPoints_sa(
            in_point_features,
            in_rasters,
            bilinear_interpolate_values)
        return result
    return Wrapper(
        in_point_features,
        in_rasters,
        bilinear_interpolate_values)
ExtractMultiValuesToPoints.__esri_toolname__ = "ExtractMultiValuesToPoints_sa"
ExtractMultiValuesToPoints.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3"
]


def Visibility(
        in_raster,
        in_observer_features,
        out_agl_raster="#",
        analysis_type="#",
        nonvisible_cell_value="#",
        z_factor="#",
        curvature_correction="#",
        refractivity_coefficient="#",
        surface_offset="#",
        observer_elevation="#",
        observer_offset="#",
        inner_radius="#",
        outer_radius="#",
        horizontal_start_angle="#",
        horizontal_end_angle="#",
        vertical_upper_angle="#",
        vertical_lower_angle="#"):
    """Visibility(in_raster, in_observer_features, {out_agl_raster}, {analysis_type}, {nonvisible_cell_value}, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {outer_radius}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle})

    Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location.

    Arguments:
    in_raster -- The input surface raster.
    in_observer_features -- The feature class that identifies the observer locations.
    out_agl_raster -- The output above-ground-level (AGL) raster.
    analysis_type -- The visibility analysis type.
    nonvisible_cell_value -- Value assigned to non-visible cells.
    z_factor -- Number of ground x,y units in one surface z unit.
    curvature_correction -- Allows correction for the earth's curvature.
    refractivity_coefficient -- Coefficient of the refraction of visible light in air.
    surface_offset -- This value indicates a vertical distance (in surface units) to be added to the z-value of each cell as it is considered for visibility. It should be a positive integer or floating point value.
    observer_elevation -- This value is used to define the surface elevations of the observer points or vertices.
    observer_offset -- This value indicates a vertical distance (in surface units) to be added to observer elevation.
It should be a positive integer or floating point value.
    inner_radius -- This value defines the start distance from which visibility is determined. Cells closer than this distance are not visible in the output, but can still block visibility of the cells between inner radius and outer radius.
It can be a positive or negative  integer or floating point value. If it is a positive value, then it is interpreted as three-dimensional, line-of-sight distance. If it is a negative value, then it is interpreted as  two-dimensional planimetric distance.
    outer_radius -- This value defines the maximum distance from which visibility is determined. Cells beyond this distance are excluded from the analysis. It can be a positive or negative  integer or floating point value. If it is a positive value, then it is interpreted as three-dimensional, line-of-sight distance. If it is a negative value, then it is interpreted as  two-dimensional planimetric distance.
    horizontal_start_angle -- This value defines the start angle of the horizontal scan range. The value should be specified in degrees from 0 to 360, with 0 oriented to north. The default value is 0.
    horizontal_end_angle -- This value defines the end angle of the horizontal scan range. The value should be specified in degrees from 0 to 360, with 0 oriented to north. The default value is 360.
    vertical_upper_angle -- This value defines the upper vertical angle limit of the scan above a horizontal plane.
The value should be specified in degrees from 0 to 90, which can be integer or floating point.
    vertical_lower_angle -- This value defines the lower vertical angle limit of the scan below a horizontal plane.
The value should be specified in degrees from -90 to 0, which can be integer or floating point.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_observer_features,
            out_agl_raster,
            analysis_type,
            nonvisible_cell_value,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            surface_offset,
            observer_elevation,
            observer_offset,
            inner_radius,
            outer_radius,
            horizontal_start_angle,
            horizontal_end_angle,
            vertical_upper_angle,
            vertical_lower_angle):
        out_raster = "#"
        result = arcpy.gp.Visibility_sa(
            in_raster,
            in_observer_features,
            out_raster,
            out_agl_raster,
            analysis_type,
            nonvisible_cell_value,
            z_factor,
            curvature_correction,
            refractivity_coefficient,
            surface_offset,
            observer_elevation,
            observer_offset,
            inner_radius,
            outer_radius,
            horizontal_start_angle,
            horizontal_end_angle,
            vertical_upper_angle,
            vertical_lower_angle)
        return _wrapToolRaster(u"Visibility_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_observer_features,
        out_agl_raster,
        analysis_type,
        nonvisible_cell_value,
        z_factor,
        curvature_correction,
        refractivity_coefficient,
        surface_offset,
        observer_elevation,
        observer_offset,
        inner_radius,
        outer_radius,
        horizontal_start_angle,
        horizontal_end_angle,
        vertical_upper_angle,
        vertical_lower_angle)
Visibility.__esri_toolname__ = "Visibility_sa"
Visibility.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14",
    "::::15",
    "::::16",
    "::::17",
    "::::18"
]


def RescaleByFunction(
        in_raster,
        transformation_function="#",
        from_scale="#",
        to_scale="#"):
    """RescaleByFunction(in_raster, {transformation_function}, {from_scale}, {to_scale})

    Rescales the input raster values by applying a selected transformation function and then transforming the resulting values onto a specified continuous evaluation scale.

    Arguments:
    in_raster -- The input raster to rescale.
    transformation_function -- Specifies the continuous function to transform the input
raster.
    from_scale -- The 
 starting value of the output evaluation scale.
    to_scale -- The 
 ending value of the output evaluation scale.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            transformation_function,
            from_scale,
            to_scale):
        transformation_function = Utils.compoundParameterToString(transformation_function, ParameterClasses._TransformationFunction)
        out_raster = "#"
        result = arcpy.gp.RescaleByFunction_sa(
            in_raster,
            out_raster,
            transformation_function,
            from_scale,
            to_scale)
        return _wrapToolRaster(u"RescaleByFunction_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        transformation_function,
        from_scale,
        to_scale)
RescaleByFunction.__esri_toolname__ = "RescaleByFunction_sa"
RescaleByFunction.__esri_toolinfo__ = [
    "::::1",
    "Python::TfExponential|TfGaussian|TfLarge|TfLinear|TfLogarithm|TfLogisticDecay|TfLogisticGrowth|TfMSLarge|TfMSSmall|TfNear|TfPower|TfSmall|TfSymmetricLinear::",
    "::::4",
    "::::5"
]


def Viewshed2(
        in_raster,
        in_observer_features,
        out_agl_raster="#",
        analysis_type="#",
        vertical_error="#",
        out_observer_region_relationship_table="#",
        refractivity_coefficient="#",
        surface_offset="#",
        observer_elevation="#",
        observer_offset="#",
        inner_radius="#",
        inner_radius_is_3d="#",
        outer_radius="#",
        outer_radius_is_3d="#",
        horizontal_start_angle="#",
        horizontal_end_angle="#",
        vertical_upper_angle="#",
        vertical_lower_angle="#",
        analysis_method="#"):
    """Viewshed2(in_raster, in_observer_features, {out_agl_raster}, {analysis_type}, {vertical_error}, {out_observer_region_relationship_table}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {inner_radius_is_3d}, {outer_radius}, {outer_radius_is_3d}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle}, {analysis_method})

    Determines the raster surface locations visible to a set of observer features, using geodesic methods.

    Arguments:
    in_raster -- The input surface raster. It can be an integer or a  floating-point raster.
    in_observer_features -- The input feature class that identifies the observer locations. It can be point, multipoint, or polyline features.
    out_agl_raster -- The output above ground level (AGL) raster.
    analysis_type -- Choose which type of visibility analysis you wish to perform, either determining how visible each cell is to the observers, or identifying for each surface location which observers are visible.
    vertical_error -- The amount of uncertainty (the Root-Mean-Square error, or RMSE) in the surface elevation values. It is a floating-point value representing the expected error of the input elevation values. When this parameter is assigned a value greater than 0, the output visibility raster will be floating point. In this case, each cell value on the output visibility raster represents the sum of probabilities that the cell is visible to any of the observers.
    out_observer_region_relationship_table -- The output table for identifying the regions that are visible to each observer. This table can be related to the input observer feature class and the output visibility raster for identifying the regions visible to given observers.
    refractivity_coefficient -- Coefficient of the refraction of visible light in air.
    surface_offset -- This value indicates a vertical distance (in surface units) to be added to the z-value of each target cell as it is considered for visibility. It should be a positive integer or floating-point value.
    observer_elevation -- This value is used to define the surface elevations of the observer points or vertices.
    observer_offset -- This value indicates a vertical distance (in surface units) to be added to observer elevation. It should be a positive integer or floating-point value.
    inner_radius -- This value defines the start (minimum) distance from which visibility is determined. Cells closer than this distance are considered not visible in the output but can still block visibility of the cells between the inner radius and the outer radius. The default value is 0.
    inner_radius_is_3d -- Type of distance for the inner radius parameter.
    outer_radius -- This value defines the maximum distance from which visibility is determined. Cells beyond this distance are excluded from the analysis.
    outer_radius_is_3d -- Type of distance for the outer radius parameter.
    horizontal_start_angle -- This value defines the start angle of the horizontal scan range. The value should be specified in degrees from 0 to 360.0, with 0 oriented to north. The default value is 0.
    horizontal_end_angle -- This value defines the end angle of the horizontal scan range. The value should be specified in degrees from 0 to 360.0, with 0 oriented to north. The default value is 360.0.
    vertical_upper_angle -- This value defines the upper vertical angle limit of the scan above a horizontal plane. The value should be specified in degrees from 0 to 90.0, which can be integer or floating point. The default value is 90.0.
    vertical_lower_angle -- This value defines the lower vertical angle limit of the scan below a horizontal plane. The value should be specified in degrees from -90.0 to 0, which can be integer or floating point. The default value is -90.0.
    analysis_method -- Choose the method by which the visibility will be calculated. This option allows you to trade some accuracy for increased performance.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_observer_features,
            out_agl_raster,
            analysis_type,
            vertical_error,
            out_observer_region_relationship_table,
            refractivity_coefficient,
            surface_offset,
            observer_elevation,
            observer_offset,
            inner_radius,
            inner_radius_is_3d,
            outer_radius,
            outer_radius_is_3d,
            horizontal_start_angle,
            horizontal_end_angle,
            vertical_upper_angle,
            vertical_lower_angle,
            analysis_method):
        out_raster = "#"
        result = arcpy.gp.Viewshed2_sa(
            in_raster,
            in_observer_features,
            out_raster,
            out_agl_raster,
            analysis_type,
            vertical_error,
            out_observer_region_relationship_table,
            refractivity_coefficient,
            surface_offset,
            observer_elevation,
            observer_offset,
            inner_radius,
            inner_radius_is_3d,
            outer_radius,
            outer_radius_is_3d,
            horizontal_start_angle,
            horizontal_end_angle,
            vertical_upper_angle,
            vertical_lower_angle,
            analysis_method)
        return _wrapToolRaster(u"Viewshed2_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_observer_features,
        out_agl_raster,
        analysis_type,
        vertical_error,
        out_observer_region_relationship_table,
        refractivity_coefficient,
        surface_offset,
        observer_elevation,
        observer_offset,
        inner_radius,
        inner_radius_is_3d,
        outer_radius,
        outer_radius_is_3d,
        horizontal_start_angle,
        horizontal_end_angle,
        vertical_upper_angle,
        vertical_lower_angle,
        analysis_method)
Viewshed2.__esri_toolname__ = "Viewshed2_sa"
Viewshed2.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8",
    "::::9",
    "::::10",
    "::::11",
    "::::12",
    "::::13",
    "::::14",
    "::::15",
    "::::16",
    "::::17",
    "::::18",
    "::::19",
    "::::20"
]


def ClassifyRaster(
        in_raster,
        in_classifier_definition,
        in_additional_raster="#"):
    """ClassifyRaster(in_raster, in_classifier_definition, {in_additional_raster})

    Classify a raster dataset based on an Esri Classifier Definition (.ecd) file and raster dataset inputs.

    Arguments:
    in_raster -- Select the raster dataset you want to classify.
    in_classifier_definition -- The input Esri Classifier Definition (.ecd) file containing the statistics on the chosen attributes for the classifier.
    in_additional_raster -- Optionally incorporate ancillary  raster datasets, such as a segmented image, a multispectral image,  or a DEM, to generate attributes and other required information for the classifier.  The raster datasets for this parameter must match those used to create the training .ecd file.

    Results:
    out_raster_dataset -- Output Classified Raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            in_classifier_definition,
            in_additional_raster):
        out_raster_dataset = "#"
        result = arcpy.gp.ClassifyRaster_sa(
            in_raster,
            in_classifier_definition,
            out_raster_dataset,
            in_additional_raster)
        return _wrapToolRaster(u"ClassifyRaster_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        in_classifier_definition,
        in_additional_raster)
ClassifyRaster.__esri_toolname__ = "ClassifyRaster_sa"
ClassifyRaster.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::4"
]


def ComputeSegmentAttributes(
        in_segmented_raster,
        in_additional_raster="#",
        used_attributes="#"):
    """ComputeSegmentAttributes(in_segmented_raster, {in_additional_raster}, {[used_attributes,...]})

    Compute a set of attributes associated with your segmented image. The input raster can be a single-band or 3-band, 8-bit segmented image.

    Arguments:
    in_segmented_raster -- The input segmented raster dataset, where all the pixels belonging to a segment have the same converged RGB color. Usually, it is an  8-bit, 3-band RGB raster, but it can also be a 1-band grayscale raster.
    in_additional_raster -- Optionally incorporate ancillary  raster datasets, such as a segmented image, a multispectral image,  or a DEM, to generate attributes and other required information for the classifier.  The raster datasets for this parameter must match those used to create the training .ecd file.
    used_attributes -- Specify the attributes to be included in the attribute table associated with the output raster.

    Results:
    out_index_raster_dataset -- Output Segment Index Raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_segmented_raster,
            in_additional_raster,
            used_attributes):
        out_index_raster_dataset = "#"
        result = arcpy.gp.ComputeSegmentAttributes_sa(
            in_segmented_raster,
            out_index_raster_dataset,
            in_additional_raster,
            used_attributes)
        return _wrapToolRaster(u"ComputeSegmentAttributes_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_segmented_raster,
        in_additional_raster,
        used_attributes)
ComputeSegmentAttributes.__esri_toolname__ = "ComputeSegmentAttributes_sa"
ComputeSegmentAttributes.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4"
]


def SegmentMeanShift(
        in_raster,
        spectral_detail="#",
        spatial_detail="#",
        min_segment_size="#",
        band_indexes="#"):
    """SegmentMeanShift(in_raster, {spectral_detail}, {spatial_detail}, {min_segment_size}, {band_indexes})

    Identify features or segments in your imagery by grouping adjacent pixels together that have similar spectral characteristics. You may control the amount of spatial and spectral smoothing to help derive features of interest.

    Arguments:
    in_raster -- Select the raster dataset you want to segment. This can be a multispectral or grayscale image.
    spectral_detail -- Set the level of importance given to the spectral differences of features in your imagery.
    spatial_detail -- Set the level of importance given to the proximity between features in your imagery.
    min_segment_size -- Merge segments smaller than this size with their best fitting neighbor segment.
    band_indexes -- Select the bands you want to use to segment your imagery separated by a space.

    Results:
    out_raster_dataset -- Output Raster Dataset"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def Wrapper(
            in_raster,
            spectral_detail,
            spatial_detail,
            min_segment_size,
            band_indexes):
        out_raster_dataset = "#"
        result = arcpy.gp.SegmentMeanShift_sa(
            in_raster,
            out_raster_dataset,
            spectral_detail,
            spatial_detail,
            min_segment_size,
            band_indexes)
        return _wrapToolRaster(u"SegmentMeanShift_sa", unicode(result.getOutput(0)))
    return Wrapper(
        in_raster,
        spectral_detail,
        spatial_detail,
        min_segment_size,
        band_indexes)
SegmentMeanShift.__esri_toolname__ = "SegmentMeanShift_sa"
SegmentMeanShift.__esri_toolinfo__ = [
    "::::1",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]


def TrainMaximumLikelihoodClassifier(
        in_raster,
        in_training_features,
        out_classifier_definition,
        in_additional_raster="#",
        used_attributes="#"):
    """TrainMaximumLikelihoodClassifier(in_raster, in_training_features, out_classifier_definition, {in_additional_raster}, {used_attributes})

    Generate an Esri classifier definition (.ecd) file using the Maximum Likelihood Classifier (MLC)  classification definition.

    Arguments:
    in_raster -- Select the raster dataset you want to classify.
    in_training_features -- Select the training sample file or layer that delineates your training sites.
    out_classifier_definition -- This is a JSON file that contains attribute information, statistics, hyperplane vectors and other information needed for the classifier.  A file with an .ecd extension is created.
    in_additional_raster -- Optionally incorporate ancillary raster datasets, such as a segmented image or DEM.
    used_attributes -- Specify the attributes to be included in the attribute table associated with the output raster."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            in_training_features,
            out_classifier_definition,
            in_additional_raster,
            used_attributes):
        result = arcpy.gp.TrainMaximumLikelihoodClassifier_sa(
            in_raster,
            in_training_features,
            out_classifier_definition,
            in_additional_raster,
            used_attributes)
        return result
    return Wrapper(
        in_raster,
        in_training_features,
        out_classifier_definition,
        in_additional_raster,
        used_attributes)
TrainMaximumLikelihoodClassifier.__esri_toolname__ = "TrainMaximumLikelihoodClassifier_sa"
TrainMaximumLikelihoodClassifier.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5"
]


def TrainIsoClusterClassifier(
        in_raster,
        max_classes,
        out_classifier_definition,
        in_additional_raster="#",
        max_iterations="#",
        min_samples_per_cluster="#",
        skip_factor="#",
        used_attributes="#"):
    """TrainIsoClusterClassifier(in_raster, max_classes, out_classifier_definition, {in_additional_raster}, {max_iterations}, {min_samples_per_cluster}, {skip_factor}, {used_attributes;used_attributes})

    Generate an Esri classifier definition (.ecd) file using the Iso Cluster classification definition.

    Arguments:
    in_raster -- Select the raster dataset you want to classify.
    max_classes -- Maximum number of desired classes to group pixels or segments.
    out_classifier_definition -- This is a JSON file that contains attribute information, statistics, hyperplane vectors and other information needed for the classifier.  A file with an .ecd extension is created.
    in_additional_raster -- Optionally incorporate ancillary raster datasets, such as a segmented image, a multispectral image,  or a DEM, to generate attributes and other required information for classification.
    max_iterations -- Maximum number of iterations for the clustering process to run.
    min_samples_per_cluster -- Minimum number of pixels or segments in a valid cluster or class.
    skip_factor -- Number of pixels to skip for a pixel image input. If a segmented image is an input, specify the number of segments to skip.
    used_attributes;used_attributes -- Specify the attributes to be included in the attribute table associated with the output raster."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            max_classes,
            out_classifier_definition,
            in_additional_raster,
            max_iterations,
            min_samples_per_cluster,
            skip_factor,
            used_attributes):
        result = arcpy.gp.TrainIsoClusterClassifier_sa(
            in_raster,
            max_classes,
            out_classifier_definition,
            in_additional_raster,
            max_iterations,
            min_samples_per_cluster,
            skip_factor,
            used_attributes)
        return result
    return Wrapper(
        in_raster,
        max_classes,
        out_classifier_definition,
        in_additional_raster,
        max_iterations,
        min_samples_per_cluster,
        skip_factor,
        used_attributes)
TrainIsoClusterClassifier.__esri_toolname__ = "TrainIsoClusterClassifier_sa"
TrainIsoClusterClassifier.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6",
    "::::7",
    "::::8"
]


def TrainSupportVectorMachineClassifier(
        in_raster,
        in_training_features,
        out_classifier_definition,
        in_additional_raster="#",
        max_samples_per_class="#",
        used_attributes="#"):
    """TrainSupportVectorMachineClassifier(in_raster, in_training_features, out_classifier_definition, {in_additional_raster}, {max_samples_per_class}, {used_attributes;used_attributes})

    Generate an Esri classifier definition (.ecd) file using the Support Vector Machine (SVM)  classification definition.

    Arguments:
    in_raster -- Select the raster dataset you want to classify.
    in_training_features -- The training sample feature class must have been created in ArcMap.  There is no method to create them in Python.
    out_classifier_definition -- This is a JSON file that contains attribute information, statistics, hyperplane vectors and other information needed for the classifier.  A file with an .ecd extension is created.
    in_additional_raster -- Optionally incorporate ancillary raster datasets, such as a segmented image, a multispectral image,  or a DEM, to generate attributes and other required information for classification.
    max_samples_per_class -- The maximum number of samples to use for defining each class.
    used_attributes;used_attributes -- Specify the attributes to be included in the attribute table associated with the output raster."""
    @Utils.StateSwapper(Utils.StateSwapper.NoSingleRasterResult)
    def Wrapper(
            in_raster,
            in_training_features,
            out_classifier_definition,
            in_additional_raster,
            max_samples_per_class,
            used_attributes):
        result = arcpy.gp.TrainSupportVectorMachineClassifier_sa(
            in_raster,
            in_training_features,
            out_classifier_definition,
            in_additional_raster,
            max_samples_per_class,
            used_attributes)
        return result
    return Wrapper(
        in_raster,
        in_training_features,
        out_classifier_definition,
        in_additional_raster,
        max_samples_per_class,
        used_attributes)
TrainSupportVectorMachineClassifier.__esri_toolname__ = "TrainSupportVectorMachineClassifier_sa"
TrainSupportVectorMachineClassifier.__esri_toolinfo__ = [
    "::::1",
    "::::2",
    "::::3",
    "::::4",
    "::::5",
    "::::6"
]

def ApplyEnvironment(
        in_raster):
    """ApplyEnvironment(in_raster)

    Creates a copy of in_raster with environment settings applied.

    Arguments:
    in_raster -- The input that will be copied.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def wrapper(in_raster):
        return _wrapLocalFunctionRaster(u"ApplyEnvironment",
            ["Copy", in_raster])
    return wrapper(
        in_raster)

def FloatDivide(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """FloatDivide(in_raster_or_constant1, in_raster_or_constant2)

    Divides the values of two rasters on a cell-by-cell basis. The result will
    be a true floating point division.

    Arguments:
    in_raster_or_constant1 -- The input whose values will be divided by the second input.
    in_raster_or_constant2 -- The input whose values the first input are to be divided by.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def wrapper(in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Divide_sa",
            ["FloatDivide", in_raster_or_constant1, in_raster_or_constant2])
    return wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)

def FloorDivide(
        in_raster_or_constant1,
        in_raster_or_constant2):
    """FloorDivide(in_raster_or_constant1, in_raster_or_constant2)

    Divides the values of two rasters on a cell-by-cell basis. The result will
    be a floored floating point division.

    Arguments:
    in_raster_or_constant1 -- The input whose values will be divided by the second input.
    in_raster_or_constant2 -- The input whose values the first input are to be divided by.

    Results:
    out_raster -- Output raster"""
    @Utils.StateSwapper(Utils.StateSwapper.SingleRasterResult)
    def wrapper(
            in_raster_or_constant1,
            in_raster_or_constant2):
        return _wrapLocalFunctionRaster(u"Divide_sa",
            ["FloorDivide", in_raster_or_constant1, in_raster_or_constant2])
    return wrapper(
        in_raster_or_constant1,
        in_raster_or_constant2)