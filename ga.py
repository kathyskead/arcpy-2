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
"""With Geostatistical Analyst, you can easily create a continuous surface or map
from measurements stored in a point feature layer or raster layer or by using
polygon centroids. The sample points may be measurements such as elevation,
depth to the water table, or levels of pollution. Geostatistical Analyst
provides a comprehensive set of tools for creating surfaces that can be used to
visualize, analyze, and understand spatial phenomena."""
__all__ = ['GALayerToGrid', 'GACalculateZValue', 'GAGetModelParameter', 'GASetModelParameter', 'GANeighborhoodSelection', 'GAMovingWindowKriging', 'GASemivariogramSensitivity', 'GACreateGeostatisticalLayer', 'GALayerToContour', 'GALayerToPoints', 'GaussianGeostatisticalSimulations', 'SubsetFeatures', 'IDW', 'LocalPolynomialInterpolation', 'GlobalPolynomialInterpolation', 'CrossValidation', 'KernelInterpolationWithBarriers', 'DiffusionInterpolationWithBarriers', 'RadialBasisFunctions', 'CreateSpatiallyBalancedPoints', 'DensifySamplingNetwork', 'ExtractValuesToTable', 'EmpiricalBayesianKriging', 'ArealInterpolationLayerToPolygons']
__alias__ = u'ga'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
import _ga
from _ga import *
__all__ += _ga.__all__

# Interpolation toolset
@gptooldoc('DiffusionInterpolationWithBarriers_ga', None)
def DiffusionInterpolationWithBarriers(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, in_barrier_features=None, bandwidth=None, number_iterations=None, weight_field=None, in_additive_barrier_raster=None, in_cumulative_barrier_raster=None, in_flow_barrier_raster=None):
    """DiffusionInterpolationWithBarriers_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {in_barrier_features}, {bandwidth}, {number_iterations}, {weight_field}, {in_additive_barrier_raster}, {in_cumulative_barrier_raster}, {in_flow_barrier_raster})

        Interpolates a surface using a kernel that is based upon the heat equation and
        allows one to use raster and feature barriers to redefine distances between
        input points.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      in_barrier_features {Feature Layer}:
          Absolute barrier features using non-Euclidean distances rather than line-of-
          sight distances.
      bandwidth {Double}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and prediction
          variance decreases.
      number_iterations {Long}:
          The iteration count controls the accuracy of the numerical solution because the
          model solves the diffusion equation numerically. The larger this number, the
          more accurate the predictions, yet the longer the processing time. The more
          complex the barrier's geometry and the larger the bandwidth, the more iterations
          are required for accurate predictions.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more impact it has
          on the prediction. For coincident observations, assign the largest weight to the
          most reliable measurement.
      in_additive_barrier_raster {Raster Layer}:
          The travel distance from one raster cell to the next based on this
          formula:(average cost value in the neighboring cells) x (distance between cell
          centers)
      in_cumulative_barrier_raster {Raster Layer}:
          The travel distance from one raster cell to the next based on this
          formula:(difference between cost values in the neighboring cells) + (distance
          between
          cell centers)
      in_flow_barrier_raster {Raster Layer}:
          A flow barrier is used when interpolating data with preferential direction of
          data variation, based on this formula:Indicator (cost values in the to
          neighboring cell > cost values in the from
          neighboring cell) * (cost values in the to neighboring cell - cost values in the
          from neighboring cell) + (distance between cell centers),where indicator(true) =
          1 and indicator(false) = 0.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DiffusionInterpolationWithBarriers_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, bandwidth, number_iterations, weight_field, in_additive_barrier_raster, in_cumulative_barrier_raster, in_flow_barrier_raster), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EmpiricalBayesianKriging_ga', None)
def EmpiricalBayesianKriging(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, transformation_type=None, max_local_points=None, overlap_factor=None, number_semivariograms=None, search_neighborhood=None, output_type=None, quantile_value=None, threshold_type=None, probability_threshold=None, semivariogram_model_type=None):
    """EmpiricalBayesianKriging_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {transformation_type}, {max_local_points}, {overlap_factor}, {number_semivariograms}, {search_neighborhood}, {output_type}, {quantile_value}, {threshold_type}, {probability_threshold}, {semivariogram_model_type})

        Empirical Bayesian kriging is an interpolation method that accounts for the
        error in estimating the underlying semivariogram through repeated simulations.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      transformation_type {String}:
          Type of transformation to be applied to the input data.

          * NONE— Do not apply any transformation. This is the default.

          *  EMPIRICAL—Multiplicative Skewing transformation with Empirical base function.

          * LOGEMPIRICAL—Multiplicative Skewing transformation with Log Empirical base
          function. All data values must be positive.
      max_local_points {Long}:
          The input data will automatically be divided into groups that do not have more
          than this number of points.
      overlap_factor {Double}:
          A factor representing the degree of overlap between local models (also called
          subsets). Each input point can fall into several subsets, and the overlap factor
          specifies the average number of subsets that each point will fall into. A high
          value of the overlap factor makes the output surface smoother, but it also
          increases processing time. Typical values vary between 0.01 and 5.
      number_semivariograms {Long}:
          The number of simulated semivariograms.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output. Standard
          Circular is the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandardCircular and SearchNeighborhoodSmoothCircular.Standard
          Circular

          * radius—The length of the radius of the search circle.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Smooth Circular

          * radius—The length of the radius of the search circle.

          * smoothFactor—The Smooth Interpolation option creates an outer ellipse and an
          inner ellipse at a distance equal to the Major Semiaxis multiplied by the
          Smoothing factor. The points that fall outside the smallest ellipse but inside
          the largest ellipse are weighted using a sigmoidal function with a value between
          zero and one.
      output_type {String}:
          Surface type to store the interpolation results.

          *  PREDICTION—Prediction surfaces are produced from the interpolated values.

          *  PREDICTION_STANDARD_ERROR— Standard Error surfaces are produced from the
          standard errors of the interpolated values.

          *  PROBABILITY—Probability surface of values exceeding or not exceeding a
          certain threshold.

          *  QUANTILE—Quantile surface depicting the chance that a prediction is above a
          certain value.
      quantile_value {Double}:
          The quantile value for which the output raster will be generated.
      threshold_type {String}:
          Determines whether the probability values exceed the threshold value or not.

          *  EXCEED—Probability values exceed the threshold. This is the default.

          *  NOT_EXCEED— Probability values will not exceed the threshold.
      probability_threshold {Double}:
          The probability threshold value. If left empty, the median of the input data
          will be used.
      semivariogram_model_type {String}:
          The semivariogram model that will be used for the interpolation.

          *  POWER—Power semivariogram

          *  LINEAR— Linear semivariogram

          * THIN_PLATE_SPLINE—Thin Plate Spline semivariogram

          * EXPONENTIAL—Exponential semivariogram

          * EXPONENTIAL_DETRENDED—Exponential semivariogram with first order trend removal

          * WHITTLE—Whittle semivariogram

          * WHITTLE_DETRENDED—Whittle semivariogram with first order trend removal

          * K_BESSEL—K-Bessel semivariogram

          * K_BESSEL_DETRENDED—K-Bessel semivariogram with first order trend removal
           The available choices depend on the value of the transformation_type parameter.
          If the transformation type is set to , only the first three semivariograms are
          available. If the type is EMPIRICAL or LOGEMPIRICAL, the last six semivariograms
          are available.For more information about choosing an appropriate semivariogram
          for your data,
          see the topic What is Empirical Bayesian Kriging.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EmpiricalBayesianKriging_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, transformation_type, max_local_points, overlap_factor, number_semivariograms, search_neighborhood, output_type, quantile_value, threshold_type, probability_threshold, semivariogram_model_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GAMovingWindowKriging_ga', None)
def GAMovingWindowKriging(in_ga_model_source=None, in_datasets=None, in_locations=None, neighbors_max=None, out_featureclass=None, cell_size=None, out_surface_grid=None):
    """GAMovingWindowKriging_ga(in_ga_model_source, in_datasets;in_datasets..., in_locations, neighbors_max, out_featureclass, {cell_size}, {out_surface_grid})

        Recalculates the Range, Nugget, and Partial Sill semivariogram parameters based
        on a smaller neighborhood, moving through all location points.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      in_datasets (Geostatistical Value Table):
          A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited
          string of elements. Each element
          is comprised of the following components:

          * The catalog path and name to a dataset or the name of a layer in the current
          table of contents, followed by a space.

          * A sequence of field names, each field name separated by a space. In the case
          of a raster, the cell values will be used.
      in_locations (Feature Layer):
          Point locations where predictions will be performed.
      neighbors_max (Long):
          Number of neighbors to use in the moving window.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.

     OUTPUTS:
      out_featureclass (Feature Class):
          Feature class storing the results.
      out_surface_grid {Raster Dataset}:
          The prediction values in the output feature class are interpolated onto a raster
          using the Local polynomial interpolation method."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GAMovingWindowKriging_ga(*gp_fixargs((in_ga_model_source, in_datasets, in_locations, neighbors_max, out_featureclass, cell_size, out_surface_grid), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GlobalPolynomialInterpolation_ga', None)
def GlobalPolynomialInterpolation(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, power=None, weight_field=None):
    """GlobalPolynomialInterpolation_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {weight_field})

        Fits a smooth surface that is defined by a mathematical function (a polynomial)
        to the input sample points.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      power {Long}:
          The order of the polynomial.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more impact it has
          on the prediction. For coincident observations, assign the largest weight to the
          most reliable measurement.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GlobalPolynomialInterpolation_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, power, weight_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IDW_ga', None)
def IDW(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, power=None, search_neighborhood=None, weight_field=None):
    """IDW_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {search_neighborhood}, {weight_field})

        Uses the measured values surrounding the prediction location to predict a value
        for any unsampled location, based on the assumption that things that are close
        to one another are more alike than those that are farther apart.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      power {Double}:
          The exponent of distance that controls the significance of surrounding points on
          the interpolated value. A higher power results in less influence from distant
          points.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output. Standard is
          the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandard,
          SearchNeighborhoodSmooth, SearchNeighborhoodStandardCircular, and
          SearchNeighborhoodSmoothCircular.Standard

          * majorSemiaxis—The major semiaxis value of the searching neighborhood.

          * minorSemiaxis—The minor semiaxis value of the searching neighborhood.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Smooth

          * majorSemiaxis—The major semiaxis value of the searching neighborhood.

          * minorSemiaxis—The minor semiaxis value of the searching neighborhood.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * smoothFactor—The Smooth Interpolation option creates an outer ellipse and an
          inner ellipse at a distance equal to the Major Semiaxis multiplied by the
          Smoothing factor. The points that fall outside the smallest ellipse but inside
          the largest ellipse are weighted using a sigmoidal function with a value between
          zero and one.
          Standard Circular

          * radius—The length of the radius of the search circle.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Smooth Circular

          * radius—The length of the radius of the search circle.

          * smoothFactor—The Smooth Interpolation option creates an outer ellipse and an
          inner ellipse at a distance equal to the Major Semiaxis multiplied by the
          Smoothing factor. The points that fall outside the smallest ellipse but inside
          the largest ellipse are weighted using a sigmoidal function with a value between
          zero and one.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more impact it has
          on the prediction. For coincident observations, assign the largest weight to the
          most reliable measurement.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IDW_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, weight_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('KernelInterpolationWithBarriers_ga', None)
def KernelInterpolationWithBarriers(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, in_barrier_features=None, kernel_function=None, bandwidth=None, power=None, ridge=None, output_type=None):
    """KernelInterpolationWithBarriers_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {in_barrier_features}, {kernel_function}, {bandwidth}, {power}, {ridge}, {output_type})

        A moving window predictor that uses the shortest distance between points so that
        points on either side of the line barriers are connected.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      in_barrier_features {Feature Layer}:
          Absolute barrier features using non-Euclidean distances rather than line-of-
          sight distances.
      kernel_function {String}:
          The kernel function used in the simulation.

          *  EXPONENTIAL— The function grows or decays proportionally.

          *  GAUSSIAN— Bell-shaped function that falls off quickly toward plus/minus
          infinity.

          * QUARTIC— Fourth-order polynomial function.

          *  EPANECHNIKOV— A discontinuous parabolic function.

          *  POLYNOMIAL5— Fifth-order polynomial function.

          *  CONSTANT—An indicator function.
      bandwidth {Double}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and prediction
          variance decreases.
      power {Long}:
          Sets the order of the polynomial.
      ridge {Double}:
          Used for the numerical stabilization of the solution of the system of linear
          equations. It does not influence predictions in the case of regularly
          distributed data without barriers. Predictions for areas in which the data is
          located near the feature barrier or isolated by the barriers can be unstable and
          tend to require relatively large ridge parameter values.
      output_type {String}:
          Surface type to store the interpolation results.

          *  PREDICTION—Prediction surfaces are produced from the interpolated values.

          *  PREDICTION_STANDARD_ERROR— Standard Error surfaces are produced from the
          standard errors of the interpolated values.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.KernelInterpolationWithBarriers_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, in_barrier_features, kernel_function, bandwidth, power, ridge, output_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('LocalPolynomialInterpolation_ga', None)
def LocalPolynomialInterpolation(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, power=None, search_neighborhood=None, kernel_function=None, bandwidth=None, use_condition_number=None, condition_number=None, weight_field=None, output_type=None):
    """LocalPolynomialInterpolation_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {search_neighborhood}, {kernel_function}, {bandwidth}, {use_condition_number}, {condition_number}, {weight_field}, {output_type})

        Fits the specified order (zero, first, second, third, and so on) polynomial,
        each within specified overlapping neighborhoods, to produce an output surface.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      power {Long}:
          The order of the polynomial.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output. Standard is
          the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandard,
          SearchNeighborhoodSmooth, SearchNeighborhoodStandardCircular, and
          SearchNeighborhoodSmoothCircular.Standard

          * majorSemiaxis—The major semiaxis value of the searching neighborhood.

          * minorSemiaxis—The minor semiaxis value of the searching neighborhood.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Smooth

          * majorSemiaxis—The major semiaxis value of the searching neighborhood.

          * minorSemiaxis—The minor semiaxis value of the searching neighborhood.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * smoothFactor—The Smooth Interpolation option creates an outer ellipse and an
          inner ellipse at a distance equal to the Major Semiaxis multiplied by the
          Smoothing factor. The points that fall outside the smallest ellipse but inside
          the largest ellipse are weighted using a sigmoidal function with a value between
          zero and one.
          Standard Circular

          * radius—The length of the radius of the search circle.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Smooth Circular

          * radius—The length of the radius of the search circle.

          * smoothFactor—The Smooth Interpolation option creates an outer ellipse and an
          inner ellipse at a distance equal to the Major Semiaxis multiplied by the
          Smoothing factor. The points that fall outside the smallest ellipse but inside
          the largest ellipse are weighted using a sigmoidal function with a value between
          zero and one.
      kernel_function {String}:
          The kernel function used in the simulation.

          *  EXPONENTIAL— The function grows or decays proportionally.

          *  GAUSSIAN— Bell-shaped function that falls off quickly toward plus/minus
          infinity.

          * QUARTIC— Fourth-order polynomial function.

          *  EPANECHNIKOV— A discontinuous parabolic function.

          *  POLYNOMIAL5— Fifth-order polynomial function.

          *  CONSTANT—An indicator function.
      bandwidth {Double}:
          Option to control the creation of prediction and prediction standard errors
          where the predictions are unstable. This option is only available for
          polynomials of order 1, 2, and 3.

          * NO_USE_CONDITION_NUMBER—Prediction and prediction standard errors can be
          created where the predictions are unstable. This is the default.

          * USE_CONDITION_NUMBER—Prediction and prediction standard errors will not be
          created where the predictions are unstable.
      use_condition_number {Boolean}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and prediction
          variance decreases.
      condition_number {Double}:
          Every invertible square matrix has a condition number that indicates how
          inaccurate the solution to the linear equations can be with a small change in
          the matrix coefficients (it can be due to imprecise data). If the condition
          number is large, a small change in the matrix coefficients results in a large
          change in the solution vector.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more impact it has
          on the prediction. For coincident observations, assign the largest weight to the
          most reliable measurement.
      output_type {String}:
          Surface type to store the interpolation results.

          *  PREDICTION—Prediction surfaces are produced from the interpolated values.

          *  PREDICTION_STANDARD_ERROR— Standard Error surfaces are produced from the
          standard errors of the interpolated values.

          * CONDITION_NUMBER—The Spatial condition number surface indicates the stability
          of calculations at a particular location. The larger the condition number, the
          more unstable the prediction, so locations with large condition numbers may be
          prone to artifacts and erratic predicted values.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.LocalPolynomialInterpolation_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, power, search_neighborhood, kernel_function, bandwidth, use_condition_number, condition_number, weight_field, output_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RadialBasisFunctions_ga', None)
def RadialBasisFunctions(in_features=None, z_field=None, out_ga_layer=None, out_raster=None, cell_size=None, search_neighborhood=None, radial_basis_functions=None, small_scale_parameter=None):
    """RadialBasisFunctions_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {search_neighborhood}, {radial_basis_functions}, {small_scale_parameter})

        Uses one of five basis functions to interpolate a surfaces that passes through
        the input points exactly.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can be a
          numeric field or the Shape field if the input features contain z-values or
          m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output. Standard is
          the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandard and
          SearchNeighborhoodStandardCircular.Standard

          * majorSemiaxis—The major semiaxis value of the searching neighborhood.

          * minorSemiaxis—The minor semiaxis value of the searching neighborhood.

          * angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.

          Standard Circular

          * radius—The length of the radius of the search circle.

          * Angle—The angle of rotation for the axis (circle) or semimajor axis (ellipse)
          of the moving window.

          * nbrMax—The maximum number of neighbors that will be used to estimate the value
          at the unknown location.

          * nbrMin—The minimum number of neighbors that will be used to estimate the value
          at the unknown location.

          * sectorType—The geometry of the neighborhood.

          * ONE_SECTOR—Single ellipse.

          * FOUR_SECTORS—Ellipse divided into four sectors.

          * FOUR_SECTORS_SHIFTED—Ellipse divided into four sectors and shifted 45 degrees.

          * EIGHT_SECTORS—Ellipse divided into eight sectors.
      radial_basis_functions {String}:
          There are five radial basis functions available.

          * THIN_PLATE_SPLINE—Thin-plate spline function

          * SPLINE_WITH_TENSION— Spline with tension function

          * COMPLETELY_REGULARIZED_SPLINE— Completely regularized spline function

          * MULTIQUADRIC_FUNCTION— Multiquadric spline function

          * INVERSE_MULTIQUADRIC_FUNCTION—Inverse multiquadric spline function
      small_scale_parameter {Double}:
          Used to calculate the weights assigned to the points located in the moving
          window. Each of the radial basis functions has a parameter that controls the
          degree of small-scale variation of the surface. The (optimal) parameter is
          determined by finding the value that minimizes the root mean square prediction
          error (RMSPE).

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only if no
          output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RadialBasisFunctions_ga(*gp_fixargs((in_features, z_field, out_ga_layer, out_raster, cell_size, search_neighborhood, radial_basis_functions, small_scale_parameter), True)))
        return retval
    except Exception, e:
        raise e


# Sampling Network Design toolset
@gptooldoc('CreateSpatiallyBalancedPoints_ga', None)
def CreateSpatiallyBalancedPoints(in_probability_raster=None, number_output_points=None, out_feature_class=None):
    """CreateSpatiallyBalancedPoints_ga(in_probability_raster, number_output_points, out_feature_class)

        Generates a set of sample points based on inclusion probabilities, resulting in
        a spatially balanced sample design. This tool is generally used for designing a
        monitoring network by suggesting locations to take samples, and a preference for
        particular locations can be defined using an inclusion probability raster.

     INPUTS:
      in_probability_raster (Raster Layer / Mosaic Layer):
          This raster defines the inclusion probabilities for each location in the area of
          interest. The location values range from 0 (low inclusion probability) to 1
          (high inclusion probability).
      number_output_points (Long):
          Specify how many sample locations to generate.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class contains the selected sample locations and their
          inclusion probabilities."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateSpatiallyBalancedPoints_ga(*gp_fixargs((in_probability_raster, number_output_points, out_feature_class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DensifySamplingNetwork_ga', None)
def DensifySamplingNetwork(in_geostat_layer=None, number_output_points=None, out_feature_class=None, selection_criteria=None, threshold=None, in_weight_raster=None, in_candidate_point_features=None, inhibition_distance=None):
    """DensifySamplingNetwork_ga(in_geostat_layer, number_output_points, out_feature_class, {selection_criteria}, {threshold}, {in_weight_raster}, {in_candidate_point_features}, {inhibition_distance})

        Uses a predefined geostatistical kriging layer to determine where new monitoring
        stations should be built. It can also be used to determine which monitoring
        stations should be removed from an existing network.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          Input a geostatistical layer resulting from a Kriging model.
      number_output_points (Long):
          Specify how many sample locations to generate.
      selection_criteria {String}:
          Methods to densify a sampling network.

          *  STDERR—Standard error of prediction criteria

          *  STDERR_THRESHOLD—Standard error threshold criteria

          * QUARTILE_THRESHOLD — Lower quartile threshold criteria

          * QUARTILE_THRESHOLD_UPPER — Upper quartile threshold criteria
          The STERR option will give extra weight to locations where the standard error of
          prediction is large. The STDERR_THRESHOLD, QUARTILE_THRESHOLD, and
          QUARTILE_THRESHOLD_UPPER options are useful when there is a critical threshold
          value for the variable under study (such as the highest admissible ozone level).
          The STDERR_THRESHOLD option will give extra weight to locations whose values are
          close to the threshold. The QUARTILE_THRESHOLD option will give extra weight to
          locations that are least likely to exceed the critical threshold. The
          QUARTILE_THRESHOLD_UPPER option will give extra weight to locations that are
          most likely to exceed the critical threshold.The equations for each option
          are:Standard error of prediction = stderr
          Standard error threshold = stderr(s)(1 -
          2 · abs(prob[Z(s) > threshold] - 0.5))  Lower quartile threshold = (Z0.75(s) -
          Z0.25(s)) · (prob[Z(s) < threshold])  Upper quartile threshold = (Z0.75(s) -
          Z0.25(s)) · (prob[Z(s) > threshold])
      threshold {Double}:
          The threshold value used to densify the sampling network.This parameter is only
          applicable when STDERR_THRESHOLD, QUARTILE_THRESHOLD, or
          QUARTILE_THRESHOLD_UPPER selection criteria is used.
      in_weight_raster {Raster Layer}:
          A raster used to determine which locations to weight for preference.
      in_candidate_point_features {Feature Layer}:
          Sample locations to pick from.
      inhibition_distance {Linear unit}:
          Used to prevent any samples being placed within this distance from each other.

     OUTPUTS:
      out_feature_class (Feature Class):
          The name of the output feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DensifySamplingNetwork_ga(*gp_fixargs((in_geostat_layer, number_output_points, out_feature_class, selection_criteria, threshold, in_weight_raster, in_candidate_point_features, inhibition_distance), True)))
        return retval
    except Exception, e:
        raise e


# Simulation toolset
@gptooldoc('ExtractValuesToTable_ga', None)
def ExtractValuesToTable(in_features=None, in_rasters=None, out_table=None, out_raster_names_table=None, add_warning_field=None):
    """ExtractValuesToTable_ga(in_features, in_rasters;in_rasters..., out_table, {out_raster_names_table}, {add_warning_field})

        Extracts cell values from a set of rasters to a table, based on a point or
        polygon feature class.

     INPUTS:
      in_features (Feature Layer):
          The points or polygon features to be created.
      in_rasters (Raster Layer / Mosaic Layer):
          The rasters must all have the same extent, coordinate system, and cell size.
      add_warning_field {Boolean}:
          Records if input features are partially or completely covered by the Input
          rasters.

          * TRUE— Warning field is added to the output table and populated with a P when a
          feature is partially covered by raster values.

          * FALSE— Warning field is not added to the output table.

     OUTPUTS:
      out_table (Table):
          The output table contains a record for each point and each raster that has data.
          If polygon features are input, they are converted to points that coincide with
          the raster cell centers.
      out_raster_names_table {Table}:
          Saves the names of the Input rasters to disc."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExtractValuesToTable_ga(*gp_fixargs((in_features, in_rasters, out_table, out_raster_names_table, add_warning_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GaussianGeostatisticalSimulations_ga', None)
def GaussianGeostatisticalSimulations(in_geostat_layer=None, number_of_realizations=None, output_workspace=None, output_simulation_prefix=None, in_conditioning_features=None, conditioning_field=None, cell_size=None, in_bounding_dataset=None, save_simulated_rasters=None, quantile=None, threshold=None, in_stats_polygons=None, raster_stat_type=None, conditioning_measurement_error_field=None):
    """GaussianGeostatisticalSimulations_ga(in_geostat_layer, number_of_realizations, output_workspace, output_simulation_prefix, {in_conditioning_features}, {conditioning_field}, {cell_size}, {in_bounding_dataset}, {save_simulated_rasters}, {quantile}, {threshold}, {in_stats_polygons}, {raster_stat_type;raster_stat_type...}, {conditioning_measurement_error_field})

        Performs a conditional or unconditional geostatistical simulation based on a
        Simple Kriging model. The simulated rasters can be considered equally probable
        realizations of the kriging model.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          Input a geostatistical layer resulting from a Simple Kriging model.
      number_of_realizations (Long):
          The number of simulations to perform.
      output_workspace (Workspace):
          Stores all the simulation results. The workspace can be either a folder or a
          geodatabase.
      output_simulation_prefix (String):
          A one- to three-character alphanumeric prefix that is automatically added to the
          output dataset names.
      in_conditioning_features {Feature Layer}:
          The features used to condition the realizations. If left blank, unconditional
          realizations are produced.
      conditioning_field {Field}:
          The field used to condition the realizations. If left blank, unconditional
          realizations are produced.
      cell_size {Analysis Cell Size}:
          A field that specifies the measurement error for each input point in the
          conditioning features. For each conditioning feature, the value of this field
          should correspond to one standard deviation of the measured value of the
          feature. Use this field if the measurement error values are not the same at each
          sampling location.A common source of nonconstant measurement error is when the
          data is measured
          with different devices. One device might be more precise than another, which
          means that it will have a smaller measurement error. For example, one
          thermometer rounds to the nearest degree and another thermometer rounds to the
          nearest tenth of a degree. The variability of measurements is often provided by
          the manufacturer of the measuring device, or it may be known from empirical
          practice.Leave this parameter blank if there are no measurement error values or
          the
          measurement error values are unknown.
      in_bounding_dataset {Feature Layer}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      save_simulated_rasters {Boolean}:
          Limits the analysis to these features' bounding polygon. If point features are
          entered, then a convex hull polygon is automatically created. Realizations are
          then performed within that polygon. If bounding features are supplied, any
          features or rasters supplied in the Mask environment will be ignored.
      quantile {Double}:
          Specifies whether or not the simulated rasters are saved to disk.

          * TRUE—Indicates that the simulated rasters will be saved to disk.

          * FALSE—Indicates that the simulated rasters will not be saved to disk.
      threshold {Double}:
          The quantile value for which the output raster will be generated.
      in_stats_polygons {Feature Layer}:
          The threshold value for which the output raster will be generated, as the
          percentage of the number of times the set threshold was exceeded, on a cell-by-
          cell basis.
      raster_stat_type {String}:
          These polygons represent areas of interest for which summary statistics are
          calculated.If in_stats_polygons are provided, the output polygon feature class
          will be
          saved in the location defined by output_workspace, and it will have the same
          name as the input polygons, preceded by the output_simulation_prefix. For
          example, if the input statistical polygons were named myPolys and you entered
          aaa as the output prefix, then the output polygons will be named aaamyPolys and
          will be saved in the specified output workspace.
      conditioning_measurement_error_field {Field}:
          The simulated rasters are postprocessed on a cell-by-cell basis, and each
          selected statistics type is calculated and reported in an output raster.

          * MIN —Calculates the minimum (smallest value).

          * MAX —Calculates the maximum (largest value).

          * MEAN —Calculates the mean (average).

          * STDDEV —Calculates the standard deviation.

          * QUARTILE1 —Calculates the 25th quantile.

          * MEDIAN —Calculates the median.

          * QUARTILE3 —Calculates the 75th quantile.

          * QUANTILE —Calculates a user-specified quantile (0 < Q < 1).

          * P_THRSHLD —Calculates the percentage of the simulations where the cell value
          exceeds a user-specified threshold value."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GaussianGeostatisticalSimulations_ga(*gp_fixargs((in_geostat_layer, number_of_realizations, output_workspace, output_simulation_prefix, in_conditioning_features, conditioning_field, cell_size, in_bounding_dataset, save_simulated_rasters, quantile, threshold, in_stats_polygons, raster_stat_type, conditioning_measurement_error_field), True)))
        return retval
    except Exception, e:
        raise e


# Utilities toolset
@gptooldoc('CrossValidation_ga', None)
def CrossValidation(in_geostat_layer=None, out_point_feature_class=None):
    """CrossValidation_ga(in_geostat_layer, {out_point_feature_class})

        Removes one data location then predicts the associated data using the data at
        the rest of the locations.  The primary use for this tool is to compare the
        predicted value to the observed value in order to obtain useful information
        about some of your model parameters.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.

     OUTPUTS:
      out_point_feature_class {Feature Class}:
          Stores the cross-validation statistics at each location in the geostatistical
          layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CrossValidation_ga(*gp_fixargs((in_geostat_layer, out_point_feature_class), True)))
        from arcpy._ga import CrossValidationResult
        retval.__class__ = CrossValidationResult
        return retval
    except Exception, e:
        raise e

@gptooldoc('GANeighborhoodSelection_ga', None)
def GANeighborhoodSelection(in_dataset=None, out_layer=None, point_coord=None, neighbors_max=None, neighbors_min=None, minor_semiaxis=None, major_semiaxis=None, angle=None, shape_type=None):
    """GANeighborhoodSelection_ga(in_dataset, out_layer, point_coord, neighbors_max, neighbors_min, minor_semiaxis, major_semiaxis, angle, {shape_type})

        Creates a layer of points based on a user-defined neighborhood. For example, you
        might wish to create a selection of points in a circular
        neighborhood around a location defined by the Input point. The illustration
        above demonstrates that the output will be the 10 points, colored blue, that
        fall within the circle.

     INPUTS:
      in_dataset (Feature Layer):
          Points used to create a neighborhood selection.
      point_coord (Point):
          The neighborhood center's x,y coordinate.
      neighbors_max (Long):
          The number of points to use in each sector. If a sector has the required number
          of points, all points in that sector are used.
      neighbors_min (Long):
          The minimum number of points to use in each sector. If the minimum number of
          required points are not available in any given sector, the nearest available
          point outside the sector will be selected.
      minor_semiaxis (Double):
          Size of the minor semiaxis of the search neighborhood.
      major_semiaxis (Double):
          Size of the major semiaxis of the search neighborhood.
      angle (Double):
          The angle of rotation of the neighborhood axis.
      shape_type {String}:
          The geometry of the neighborhood.

          * ONE_SECTOR — Single ellipse

          * FOUR_SECTORS — Ellipse divided into four sectors

          * FOUR_SECTORS_SHIFTED — Ellipse divided into four sectors and shifted 45
          degrees

          * EIGHT_SECTORS — Ellipse divided into eight sectors

     OUTPUTS:
      out_layer (Feature Layer):
          Layer to store the neighborhood selection."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GANeighborhoodSelection_ga(*gp_fixargs((in_dataset, out_layer, point_coord, neighbors_max, neighbors_min, minor_semiaxis, major_semiaxis, angle, shape_type), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GASemivariogramSensitivity_ga', None)
def GASemivariogramSensitivity(in_ga_model_source=None, in_datasets=None, in_locations=None, nugget_span_percents=None, nugget_calc_times=None, partialsill_span_percents=None, partialsill_calc_times=None, range_span_percents=None, range_calc_times=None, minrange_span_percents=None, minrange_calc_times=None, out_table=None):
    """GASemivariogramSensitivity_ga(in_ga_model_source, in_datasets;in_datasets..., in_locations, {nugget_span_percents}, {nugget_calc_times}, {partialsill_span_percents}, {partialsill_calc_times}, {range_span_percents}, {range_calc_times}, {minrange_span_percents}, {minrange_calc_times}, out_table)

        This tool performs a sensitivity analysis on the predicted values and associated
        standard errors by changing the model's semivariogram parameters (the nugget,
        partial sill, and major/minor ranges) within a percentage of the original
        values. The tool takes a geostatistical model source in order to populate these
        initial values of the nugget, partial sill, and major/minor ranges. The tool's
        output is a table indicating which parameter values were used and what the
        resulting predicted and standard error values were. If there are large
        fluctuations in the output with small changes in the model's parameter values,
        then you cannot have much confidence in the output. On the other hand, if
        changes in the output are small, then you can be confident in the model's
        predictions and make decisions based on its output.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      in_datasets (Geostatistical Value Table):
          A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited
          string of elements. Each element
          is comprised of the following components:

          * The catalog path and name to a dataset or the name of a layer in the current
          table of contents, followed by a space.

          * A sequence of field names, each field name separated by a space. In the case
          of a raster, the cell values will be used.
      in_locations (Feature Layer):
          Point locations where the sensitivity analysis is performed.
      nugget_span_percents {Double}:
          The percentage subtracted and added to the Nugget parameter to create a range
          for a subsequent random Nugget parameter selection.
      nugget_calc_times {Long}:
          Number of random Nugget values randomly sampled from the Nugget span.
      partialsill_span_percents {Double}:
          Percentage subtracted from and added to the Partial Sill parameter to create a
          range for a random Partial Sill selection.
      partialsill_calc_times {Long}:
          Number of Partial Sill values randomly sampled from the Partial Sill span.
      range_span_percents {Double}:
          Percentage subtracted and added to the Major Range parameter to create a range
          for a random Major Range selection.
      range_calc_times {Long}:
          Number of Major Range values randomly sampled from the Major Range span.
      minrange_span_percents {Double}:
          Percentage subtracted and added to the Minor Range parameter to create a range
          for a random Minor Range selection.
      minrange_calc_times {Long}:
          Number of Minor Range values randomly sampled from the Minor Range span.If
          Anisotropy has been set in the input geostatistical model source, a value is
          required.

     OUTPUTS:
      out_table (Table):
          Table storing the sensitivity results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GASemivariogramSensitivity_ga(*gp_fixargs((in_ga_model_source, in_datasets, in_locations, nugget_span_percents, nugget_calc_times, partialsill_span_percents, partialsill_calc_times, range_span_percents, range_calc_times, minrange_span_percents, minrange_calc_times, out_table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SubsetFeatures_ga', None)
def SubsetFeatures(in_features=None, out_training_feature_class=None, out_test_feature_class=None, size_of_training_dataset=None, subset_size_units=None):
    """SubsetFeatures_ga(in_features, out_training_feature_class, {out_test_feature_class}, {size_of_training_dataset}, {subset_size_units})

        Divides the original dataset into two parts: one part to be used to model the
        spatial structure and produce a surface, the other to be used to compare and
        validate the output surface.

     INPUTS:
      in_features (Table View):
          Points, lines, polygon features, or table from which to create a subset.
      size_of_training_dataset {Double}:
          The size of the output training feature class, entered either as a percentage of
          the input features or as an absolute number of features.
      subset_size_units {Boolean}:
          Type of subset size.

          * PERCENTAGE_OF_INPUT— The percentage of the input features that will be in the
          training dataset.

          * ABSOLUTE_VALUE— The number of features that will be in the training dataset.

     OUTPUTS:
      out_training_feature_class (Feature Class / Table):
          The subset of training features to be created.
      out_test_feature_class {Feature Class / Table}:
          The subset of test features to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SubsetFeatures_ga(*gp_fixargs((in_features, out_training_feature_class, out_test_feature_class, size_of_training_dataset, subset_size_units), True)))
        return retval
    except Exception, e:
        raise e


# Working with Geostatistical Layers toolset
@gptooldoc('ArealInterpolationLayerToPolygons_ga', None)
def ArealInterpolationLayerToPolygons(in_areal_interpolation_layer=None, in_polygon_features=None, out_feature_class=None, append_all_fields=None):
    """ArealInterpolationLayerToPolygons_ga(in_areal_interpolation_layer, in_polygon_features, out_feature_class, {append_all_fields})

        Reaggregates the predictions of an Areal Interpolation layer to a new set of
        polygons.

     INPUTS:
      in_areal_interpolation_layer (Geostatistical Layer):
          Input geostatistical layer resulting from an Areal Interpolation model.
      in_polygon_features (Feature Layer):
          The polygons where predictions and standard errors will be aggregated.
      append_all_fields {Boolean}:
          Determines whether all fields will be copied from the input features to the
          output feature class.

          * ALL— All fields from the input features will be copied to the output feature
          class. This is the default.

          * FID_ONLY— Only the feature ID will be copied, and it will be named Source_ID
          on the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the aggregated predictions and standard
          errors for the new polygons."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ArealInterpolationLayerToPolygons_ga(*gp_fixargs((in_areal_interpolation_layer, in_polygon_features, out_feature_class, append_all_fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GACalculateZValue_ga', None)
def GACalculateZValue(in_geostat_layer=None, point_coord=None):
    """GACalculateZValue_ga(in_geostat_layer, point_coord)

        Uses the interpolation model in a geostatistical layer to predict a value at a
        single location.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      point_coord (Point):
          The x,y coordinate of the point for which the Z-value will be calculated."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GACalculateZValue_ga(*gp_fixargs((in_geostat_layer, point_coord), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GACreateGeostatisticalLayer_ga', None)
def GACreateGeostatisticalLayer(in_ga_model_source=None, in_datasets=None, out_layer=None):
    """GACreateGeostatisticalLayer_ga(in_ga_model_source, in_datasets;in_datasets..., out_layer)

        Creates a new geostatistical layer. An existing geostatistical layer or
        geostatistical model is required to populate the initial values for the new
        layer. The input to this tool can be created using the Geostatistical Wizard.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      in_datasets (Geostatistical Value Table):
          A GeostatisticalDatasets object.Alternatively, it can be a semicolon-delimited
          string of elements. Each element
          is comprised of the following components:

          * The catalog path and name to a dataset or the name of a layer in the current
          table of contents, followed by a space.

          * A sequence of field names, each field name separated by a space. In the case
          of a raster, the cell values will be used.

     OUTPUTS:
      out_layer (Geostatistical Layer):
          The geostatistical layer produced by the tool."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GACreateGeostatisticalLayer_ga(*gp_fixargs((in_ga_model_source, in_datasets, out_layer), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GAGetModelParameter_ga', None)
def GAGetModelParameter(in_ga_model_source=None, model_param_xpath=None):
    """GAGetModelParameter_ga(in_ga_model_source, model_param_xpath)

        Gets model parameter value from an existing geostatistical model source.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      model_param_xpath (String):
          XML path to the required model parameter."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GAGetModelParameter_ga(*gp_fixargs((in_ga_model_source, model_param_xpath), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GALayerToContour_ga', None)
def GALayerToContour(in_geostat_layer=None, contour_type=None, out_feature_class=None, contour_quality=None, classification_type=None, classes_count=None, classes_breaks=None):
    """GALayerToContour_ga(in_geostat_layer, contour_type, out_feature_class, {contour_quality}, {classification_type}, {classes_count}, {classes_breaks;classes_breaks...})

        Creates a feature class of contours from a geostatistical layer. The output
        feature class can be either a line feature class of contour lines or a polygon
        feature class of filled contours.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      contour_type (String):
          Type of contour to represent the geostatistical layer.

          * CONTOUR— The contour or isoline representation of the geostatistical layer.
          Displays the lines in either draft or presentation quality.

          * FILLED_CONTOUR—The polygon representation of the geostatistical layer. It
          assumes for the graphical display that the values between contour lines are the
          same for all locations within the polygon. Displays the lines in either draft or
          presentation quality.

          * SAME_AS_LAYER—Use the current renderer of the input geostatistical layer. If
          the geostatistical layer is not rendered as either contour or filled contour,
          this option will created filled contours. Similarly, if the geostatistical layer
          is rendered as both contour and filled contour, this option will create filled
          contours.
      contour_quality {String}:
          Determines the smoothness of contour line representation.

          * DRAFT— The default Draft quality presents a generalized version of isolines
          for faster display.

          * PRESENTATION—The Presentation option ensures more detailed isolines for the
          output feature class.
      classification_type {String}:
          Specifies how the contour breaks will be calculated.

          * GEOMETRIC_INTERVAL—Contour breaks are calculated based on geometric intervals.

          * EQUAL_INTERVAL—Contour breaks are calculated based on equal intervals.

          * QUANTILE—Contour breaks are calculated from quantiles of the input data.

          * MANUAL—Specify your own break values.
      classes_count {Long}:
          Specify the number of classes in the output feature class.If contour_type is
          set to output filled contour polygons, the number of polygons
          created will equal the value specified in this parameter. If it is set to output
          contour polylines, the number of polylines will be one less than the value
          specified in this parameter (because N class intervals define N-1 contour break
          values).This parameter does not apply if the classification_type is set to
          Manual.
      classes_breaks {Double}:
          The list of break values if the classification_type is set to Manual. The values
          should be passed as a list, and the values can be in any order.

          * For contour output, these are the values of the contour lines.

          * For filled contour, these are the upper limits of each class interval. Note
          that if the largest break value is less than the maximum of the geostatistical
          layer, the output feature class will not fill up the entire rectangular extent;
          all locations with predicted values above the largest break will not receive
          filled contours.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class will either be a polyline or a polygon, depending on
          the selected contour type."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GALayerToContour_ga(*gp_fixargs((in_geostat_layer, contour_type, out_feature_class, contour_quality, classification_type, classes_count, classes_breaks), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GALayerToGrid_ga', None)
def GALayerToGrid(in_geostat_layer=None, out_surface_grid=None, cell_size=None, points_per_block_horz=None, points_per_block_vert=None):
    """GALayerToGrid_ga(in_geostat_layer, out_surface_grid, {cell_size}, {points_per_block_horz}, {points_per_block_vert})

        Exports a Geostatistical layer to a raster.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created.This value can be
          explicitly set under Raster Analysis from the Environment
          Settings.If not set, it is the shorter of the width or the height of the extent
          of the
          input point features, in the input spatial reference, divided by 250.
      points_per_block_horz {Long}:
          The number of predictions for each cell in the horizontal direction for block
          interpolation.
      points_per_block_vert {Long}:
          The number of predictions for each cell in the vertical direction for block
          interpolation.

     OUTPUTS:
      out_surface_grid (Raster Dataset):
          The raster to be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GALayerToGrid_ga(*gp_fixargs((in_geostat_layer, out_surface_grid, cell_size, points_per_block_horz, points_per_block_vert), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GALayerToPoints_ga', None)
def GALayerToPoints(in_geostat_layer=None, in_locations=None, z_field=None, out_feature_class=None, append_all_fields=None):
    """GALayerToPoints_ga(in_geostat_layer, in_locations, {z_field}, out_feature_class, {append_all_fields})

        Exports a geostatistical layer to points. The tool can also be used to predict
        values at unmeasured locations or to validate predictions made at measured
        locations.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      in_locations (Feature Layer):
          Point locations where predictions or validations will be performed.
      z_field {Field}:
          If this field is left blank, predictions are made at the location points. If a
          field is selected, predictions are made at the location points and compared to
          their Z_value_field values and a validation analysis is performed.
      append_all_fields {Boolean}:
          Determines whether all fields will be copied from the input features to the
          output feature class.

          * ALL— All fields from the input features will be copied to the output feature
          class. This is the default.

          * FID_ONLY— Only the feature ID will be copied, and it will be named Source_ID
          on the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing either the predictions or the predictions
          and the validation results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GALayerToPoints_ga(*gp_fixargs((in_geostat_layer, in_locations, z_field, out_feature_class, append_all_fields), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GASetModelParameter_ga', None)
def GASetModelParameter(in_ga_model_source=None, model_param_xpath=None, in_param_value=None, out_ga_model=None):
    """GASetModelParameter_ga(in_ga_model_source, model_param_xpath, in_param_value, out_ga_model)

        Sets parameter values in an existing geostatistical model source.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      model_param_xpath (String):
          XML path to the required model parameter.
      in_param_value (String):
          Value for the parameter defined by the XML path.

     OUTPUTS:
      out_ga_model (File):
          Geostatistical model created with the parameter value defined in the XML path."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GASetModelParameter_ga(*gp_fixargs((in_ga_model_source, model_param_xpath, in_param_value, out_ga_model), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject