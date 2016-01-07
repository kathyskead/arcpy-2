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
"""The Spatial Statistics toolbox contains statistical tools for analyzing spatial
distributions, patterns, processes, and relationships. While there may be
similarities between spatial and nonspatial (traditional) statistics in terms of
concepts and objectives, spatial statistics are unique in that they were
developed specifically for use with geographic data. Unlike traditional
nonspatial statistical methods, they incorporate space (proximity, area,
connectivity, and/or other spatial relationships) directly into their
mathematics."""
__all__ = ['HighLowClustering', 'SpatialAutocorrelation', 'ClustersOutliers', 'HotSpots', 'CentralFeature', 'DirectionalMean', 'CalculateAreas', 'ExportXYv', 'MultiDistanceSpatialClustering', 'CalculateDistanceBand', 'AverageNearestNeighbor', 'DirectionalDistribution', 'MeanCenter', 'StandardDistance', 'CollectEvents', 'GeographicallyWeightedRegression', 'OrdinaryLeastSquares', 'GenerateSpatialWeightsMatrix', 'ConvertSpatialWeightsMatrixtoTable', 'GenerateNetworkSpatialWeights', 'HotSpotsRendered', 'MedianCenter', 'CountRenderer', 'ZRenderer', 'ClustersOutliersRendered', 'GroupingAnalysis', 'ExploratoryRegression', 'IncrementalSpatialAutocorrelation', 'CollectEventsRendered', 'OptimizedHotSpotAnalysis', 'SimilaritySearch']
__alias__ = u'stats'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Analyzing Patterns toolset
@gptooldoc('AverageNearestNeighbor_stats', None)
def AverageNearestNeighbor(Input_Feature_Class=None, Distance_Method=None, Generate_Report=None, Area=None):
    """AverageNearestNeighbor_stats(Input_Feature_Class, Distance_Method, {Generate_Report}, {Area})

        Calculates a nearest neighbor index based on the average distance from each
        feature to its nearest neighboring feature.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class, typically a point feature class, for which the average
          nearest neighbor distance will be calculated.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Generate_Report {Boolean}:
          * NO_REPORT—No graphical summary will be created. This is the default.

          * GENERATE_REPORT—A graphical summary will be created as an HTML file.
      Area {Double}:
          A numeric value representing the study area size. The default value is the area
          of the minimum enclosing rectangle that would encompass all features (or all
          selected features). Units should match those for the Output Coordinate System."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.AverageNearestNeighbor_stats(*gp_fixargs((Input_Feature_Class, Distance_Method, Generate_Report, Area), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('HighLowClustering_stats', None)
def HighLowClustering(Input_Feature_Class=None, Input_Field=None, Generate_Report=None, Conceptualization_of_Spatial_Relationships=None, Distance_Method=None, Standardization=None, Distance_Band_or_Threshold_Distance=None, Weights_Matrix_File=None):
    """HighLowClustering_stats(Input_Feature_Class, Input_Field, {Generate_Report}, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File})

        Measures the degree of clustering for either high values or low values using the
        Getis-Ord General G statistic.You can access the results of this tool (including
        the optional report file)
        from the Results window. If you disable background processing, results will also
        be written to the Progress dialog box.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which the General G statistic will be calculated.
      Input_Field (Field):
          The numeric field to be evaluated.
      Generate_Report {Boolean}:
          * NO_REPORT—No graphical summary will be created. This is the default.

          * GENERATE_REPORT—A graphical summary will be created as an HTML file.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are defined.

          * INVERSE_DISTANCE—Nearby neighboring features have a larger influence on the
          computations for a target feature than features that are far away.

          * INVERSE_DISTANCE_SQUARED—Same as INVERSE_DISTANCE except that the slope is
          sharper, so influence drops off more quickly, and only a target feature's
          closest neighbors will exert substantial influence on computations for that
          feature.

          * FIXED_DISTANCE_BAND—Each feature is analyzed within the context of neighboring
          features. Neighboring features inside the specified critical distance
          (Distance_Band_or_Threshold) receive a weight of one and exert influence on
          computations for the target feature. Neighboring features outside the critical
          distance receive a weight of zero and have no influence on a target feature's
          computations.

          * ZONE_OF_INDIFFERENCE—Features within the specified critical distance
          (Distance_Band_or_Threshold) of a target feature receive a weight of one and
          influence computations for that feature. Once the critical distance is exceeded,
          weights (and the influence a neighboring feature has on target feature
          computations) diminish with distance.

          * CONTIGUITY_EDGES_ONLY—Only neighboring polygon features that share a boundary
          or overlap will influence computations for the target polygon feature.

          * CONTIGUITY_EDGES_CORNERS—Polygon features that share a boundary, share a node,
          or overlap will influence computations for the target polygon feature.

          * GET_SPATIAL_WEIGHTS_FROM_FILE—Spatial relationships are defined by a specified
          spatial weights file. The path to the spatial weights file is specified by the
          Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Standardization (String):
          Row standardization is recommended whenever the distribution of your features is
          potentially biased due to sampling design or an imposed aggregation scheme.

          * NONE—No standardization of spatial weights is applied.

          * ROW—Spatial weights are standardized; each weight is divided by its row sum
          (the sum of the weights of all neighboring features).
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for the inverse distance and fixed distance options.
          Features outside the specified cutoff for a target feature are ignored in
          analyses for that feature. However, for ZONE_OF_INDIFFERENCE, the influence of
          features outside the given distance is reduced with distance, while those inside
          the distance threshold are equally considered. The distance value entered should
          match that of the output coordinate system.For the inverse distance
          conceptualizations of spatial relationships, a value of
          0 indicates that no threshold distance is applied; when this parameter is left
          blank, a default threshold value is computed and applied.  This default value is
          the Euclidean distance that ensures every feature has at least one neighbor.This
          parameter has no effect when polygon contiguity (CONTIGUITY_EDGES_ONLY or
          CONTIGUITY_EDGES_CORNERS) or GET_SPATIAL_WEIGHTS_FROM_FILE spatial
          conceptualizations are selected.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and potentially
          temporal, relationships among features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HighLowClustering_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Generate_Report, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, Distance_Band_or_Threshold_Distance, Weights_Matrix_File), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('IncrementalSpatialAutocorrelation_stats', None)
def IncrementalSpatialAutocorrelation(Input_Features=None, Input_Field=None, Number_of_Distance_Bands=None, Beginning_Distance=None, Distance_Increment=None, Distance_Method=None, Row_Standardization=None, Output_Table=None, Output_Report_File=None):
    """IncrementalSpatialAutocorrelation_stats(Input_Features, Input_Field, Number_of_Distance_Bands, {Beginning_Distance}, {Distance_Increment}, {Distance_Method}, {Row_Standardization}, {Output_Table}, {Output_Report_File})

        Measures spatial autocorrelation for a series of distances and optionally
        creates a line graph of those distances and their corresponding z-scores.
        Z-scores reflect the intensity of spatial clustering, and statistically
        significant peak z-scores indicate distances where spatial processes promoting
        clustering are most pronounced. These peak distances are often appropriate
        values to use for tools with a Distance Band or Distance Radius parameter.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class for which spatial autocorrelation will be measured over a
          series of distances.
      Input_Field (Field):
          The numeric field used in assessing spatial autocorrelation.
      Number_of_Distance_Bands (Long):
          The number of times to increment the neighborhood size and analyze the dataset
          for spatial autocorrelation. The starting point and size of the increment are
          specified in the Beginning_Distance and Distance_Increment parameters,
          respectively.
      Beginning_Distance {Double}:
          The distance at which to start the analysis of spatial autocorrelation and the
          distance from which to increment. The value entered for this parameter should be
          in the units of the Output Coordinate System environment setting.
      Distance_Increment {Double}:
          The distance to increase after each iteration. The distance used in the analysis
          starts at the Beginning_Distance and increases by the amount specified in the
          Distance_Increment. The value entered for this parameter should be in the units
          of the Output Coordinate System environment setting.
      Distance_Method {String}:
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN—The straight-line distance between two points (as the crow flies)

          * MANHATTAN—The distance between two points measured along axes at right angles
          (city block); calculated by summing the (absolute) difference between the x- and
          y-coordinates
      Row_Standardization {Boolean}:
          * NONE—No standardization of spatial weights is applied.

          * ROW—Spatial weights are standardized; each weight is divided by its row sum
          (the sum of the weights of all neighboring features).

     OUTPUTS:
      Output_Table {Table}:
          The table to be created with each distance band and associated z-score result.
      Output_Report_File {File}:
          The PDF file to be created containing a line graph summarizing results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.IncrementalSpatialAutocorrelation_stats(*gp_fixargs((Input_Features, Input_Field, Number_of_Distance_Bands, Beginning_Distance, Distance_Increment, Distance_Method, Row_Standardization, Output_Table, Output_Report_File), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MultiDistanceSpatialClustering_stats', None)
def MultiDistanceSpatialClustering(Input_Feature_Class=None, Output_Table=None, Number_of_Distance_Bands=None, Compute_Confidence_Envelope=None, Display_Results_Graphically=None, Weight_Field=None, Beginning_Distance=None, Distance_Increment=None, Boundary_Correction_Method=None, Study_Area_Method=None, Study_Area_Feature_Class=None):
    """MultiDistanceSpatialClustering_stats(Input_Feature_Class, Output_Table, Number_of_Distance_Bands, {Compute_Confidence_Envelope}, {Display_Results_Graphically}, {Weight_Field}, {Beginning_Distance}, {Distance_Increment}, {Boundary_Correction_Method}, {Study_Area_Method}, {Study_Area_Feature_Class})

        Determines whether features, or the values associated with features, exhibit
        statistically significant clustering or dispersion over a range of distances.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class upon which the analysis will be performed.
      Number_of_Distance_Bands (Long):
          The number of times to increment the neighborhood size and analyze the dataset
          for clustering. The starting point and size of the increment are specified in
          the Beginning_Distance and Distance_Increment parameters, respectively.
      Compute_Confidence_Envelope {String}:
          The confidence envelope is calculated by randomly placing feature points (or
          feature values) in the study area. The number of points/values randomly placed
          is equal to the number of points in the feature class. Each set of random
          placements is called a permutation and the confidence envelope is created from
          these permutations. This parameter allows you to select how many permutations
          you want to use to create the confidence envelope.

          * 0_PERMUTATIONS_-_NO_CONFIDENCE_ENVELOPE—Confidence envelopes are not created.

          * 9_PERMUTATIONS—Nine sets of points/values are randomly placed.

          * 99_PERMUTATIONS—99 sets of points/values are randomly placed.

          * 999_PERMUTATIONS—999 sets of points/values are randomly placed.
      Display_Results_Graphically {Boolean}:
          Specifies whether the tool will create a graph layer summarizing results.

          * NO_DISPLAY—No graphical summary will be created (default).

          * DISPLAY_IT—A graphical summary will be created as a graph layer.
      Weight_Field {Field}:
          A numeric field with weights representing the number of features/events at each
          location.
      Beginning_Distance {Double}:
          The distance at which to start the cluster analysis and the distance from which
          to increment. The value entered for this parameter should be in the units of the
          Output Coordinate System.
      Distance_Increment {Double}:
          The distance to increment during each iteration. The distance used in the
          analysis starts at the Beginning_Distance and increments by the amount specified
          in the Distance_Increment. The value entered for this parameter should be in the
          units of the Output Coordinate System environment setting.
      Boundary_Correction_Method {String}:
          Method to use to correct for underestimates in the number of neighbors for
          features near the edges of the study area.

          * NONE—No edge correction is applied. However, if the input feature class
          already has points that fall outside the study area boundaries, these will be
          used in neighborhood counts for features near boundaries.

          * SIMULATE_OUTER_BOUNDARY_VALUES—This method simulates points outside the study
          area so that the number of neighbors near edges is not underestimated. The
          simulated points are the "mirrors" of points near edges within the study area
          boundary.

          * REDUCE_ANALYSIS_AREA—This method shrinks the study area such that some points
          are found outside of the study area boundary. Points found outside the study
          area are used to calculate neighbor counts but are not used in the cluster
          analysis itself.

          * RIPLEY_EDGE_CORRECTION_FORMULA—For all the points (j) in the neighborhood of
          point i, this method checks to see if the edge of the study area is closer to i,
          or if j is closer to i. If j is closer, extra weight is given to the point j.
          This edge correction method is only appropriate for square or rectangular shaped
          study areas.
      Study_Area_Method {String}:
          Specifies the region to use for the study area. The K Function is sensitive to
          changes in study area size so careful selection of this value is important.

          * MINIMUM_ENCLOSING_RECTANGLE—Indicates that the smallest possible rectangle
          enclosing all of the points will be used.

          * USER_PROVIDED_STUDY_AREA_FEATURE_CLASS—Indicates that a feature class defining
          the study area will be provided in the Study Area Feature Class parameter.
      Study_Area_Feature_Class {Feature Layer}:
          Feature class that delineates the area over which the input feature class should
          be analyzed. Only specified if Study_Area_Method =
          "USER_PROVIDED_STUDY_AREA_FEATURE_CLASS" .

     OUTPUTS:
      Output_Table (Table):
          The table to which the results of the analysis will be written."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MultiDistanceSpatialClustering_stats(*gp_fixargs((Input_Feature_Class, Output_Table, Number_of_Distance_Bands, Compute_Confidence_Envelope, Display_Results_Graphically, Weight_Field, Beginning_Distance, Distance_Increment, Boundary_Correction_Method, Study_Area_Method, Study_Area_Feature_Class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SpatialAutocorrelation_stats', None)
def SpatialAutocorrelation(Input_Feature_Class=None, Input_Field=None, Generate_Report=None, Conceptualization_of_Spatial_Relationships=None, Distance_Method=None, Standardization=None, Distance_Band_or_Threshold_Distance=None, Weights_Matrix_File=None):
    """SpatialAutocorrelation_stats(Input_Feature_Class, Input_Field, {Generate_Report}, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File})

        Measures spatial autocorrelation based on feature locations and attribute values
        using the Global Moran's I statistic.You can access the results of this tool
        (including the optional report file)
        from the Results window. If you disable background processing, results will also
        be written to the Progress dialog box.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which spatial autocorrelation will be calculated.
      Input_Field (Field):
          The numeric field used in assessing spatial autocorrelation.
      Generate_Report {Boolean}:
          * NO_REPORT—No graphical summary will be created. This is the default.

          * GENERATE_REPORT—A graphical summary will be created as an HTML file.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are defined.

          * INVERSE_DISTANCE—Nearby neighboring features have a larger influence on the
          computations for a target feature than features that are far away.

          * INVERSE_DISTANCE_SQUARED—Same as INVERSE_DISTANCE except that the slope is
          sharper, so influence drops off more quickly, and only a target feature's
          closest neighbors will exert substantial influence on computations for that
          feature.

          * FIXED_DISTANCE_BAND—Each feature is analyzed within the context of neighboring
          features. Neighboring features inside the specified critical distance
          (Distance_Band_or_Threshold) receive a weight of one and exert influence on
          computations for the target feature. Neighboring features outside the critical
          distance receive a weight of zero and have no influence on a target feature's
          computations.

          * ZONE_OF_INDIFFERENCE—Features within the specified critical distance
          (Distance_Band_or_Threshold) of a target feature receive a weight of one and
          influence computations for that feature. Once the critical distance is exceeded,
          weights (and the influence a neighboring feature has on target feature
          computations) diminish with distance.

          * CONTIGUITY_EDGES_ONLY—Only neighboring polygon features that share a boundary
          or overlap will influence computations for the target polygon feature.

          * CONTIGUITY_EDGES_CORNERS—Polygon features that share a boundary, share a node,
          or overlap will influence computations for the target polygon feature.

          * GET_SPATIAL_WEIGHTS_FROM_FILE—Spatial relationships are defined by a specified
          spatial weights file. The path to the spatial weights file is specified by the
          Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Standardization (String):
          Row standardization is recommended whenever the distribution of your features is
          potentially biased due to sampling design or an imposed aggregation scheme.

          * NONE—No standardization of spatial weights is applied.

          * ROW—Spatial weights are standardized; each weight is divided by its row sum
          (the sum of the weights of all neighboring features).
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for the inverse distance and fixed distance options.
          Features outside the specified cutoff for a target feature are ignored in
          analyses for that feature. However, for ZONE_OF_INDIFFERENCE, the influence of
          features outside the given distance is reduced with distance, while those inside
          the distance threshold are equally considered. The distance value entered should
          match that of the output coordinate system.For the inverse distance
          conceptualizations of spatial relationships, a value of
          0 indicates that no threshold distance is applied; when this parameter is left
          blank, a default threshold value is computed and applied.  This default value is
          the Euclidean distance that ensures every feature has at least one neighbor.This
          parameter has no effect when polygon contiguity (CONTIGUITY_EDGES_ONLY or
          CONTIGUITY_EDGES_CORNERS) or GET_SPATIAL_WEIGHTS_FROM_FILE spatial
          conceptualizations are selected.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and potentially
          temporal, relationships among features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SpatialAutocorrelation_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Generate_Report, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, Distance_Band_or_Threshold_Distance, Weights_Matrix_File), True)))
        return retval
    except Exception, e:
        raise e


# Mapping Clusters toolset
@gptooldoc('ClustersOutliers_stats', None)
def ClustersOutliers(Input_Feature_Class=None, Input_Field=None, Output_Feature_Class=None, Conceptualization_of_Spatial_Relationships=None, Distance_Method=None, Standardization=None, Distance_Band_or_Threshold_Distance=None, Weights_Matrix_File=None, Apply_False_Discovery_Rate__FDR__Correction=None):
    """ClustersOutliers_stats(Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Weights_Matrix_File}, {Apply_False_Discovery_Rate__FDR__Correction})

        Given a set of weighted features, identifies statistically significant hot
        spots, cold spots, and spatial outliers using the Anselin Local Moran's I
        statistic.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which cluster/outlier analysis will be performed.
      Input_Field (Field):
          The numeric field to be evaluated.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are defined.

          * INVERSE_DISTANCE—Nearby neighboring features have a larger influence on the
          computations for a target feature than features that are far away.

          * INVERSE_DISTANCE_SQUARED—Same as INVERSE_DISTANCE except that the slope is
          sharper, so influence drops off more quickly, and only a target feature's
          closest neighbors will exert substantial influence on computations for that
          feature.

          * FIXED_DISTANCE_BAND—Each feature is analyzed within the context of neighboring
          features. Neighboring features inside the specified critical distance
          (Distance_Band_or_Threshold_Distance) receive a weight of one and exert
          influence on computations for the target feature. Neighboring features outside
          the critical distance receive a weight of zero and have no influence on a target
          feature's computations.

          * ZONE_OF_INDIFFERENCE—Features within the specified critical distance
          (Distance_Band_or_Threshold_Distance) of a target feature receive a weight of
          one and influence computations for that feature. Once the critical distance is
          exceeded, weights (and the influence a neighboring feature has on target feature
          computations) diminish with distance.

          * CONTIGUITY_EDGES_ONLY—Only neighboring polygon features that share a boundary
          or overlap will influence computations for the target polygon feature.

          * CONTIGUITY_EDGES_CORNERS—Polygon features that share a boundary, share a node,
          or overlap will influence computations for the target polygon feature.

          * GET_SPATIAL_WEIGHTS_FROM_FILE—Spatial relationships are defined by a specified
          spatial weights file. The path to the spatial weights file is specified by the
          Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Standardization (String):
          Row standardization is recommended whenever the distribution of your features is
          potentially biased due to sampling design or an imposed aggregation scheme.

          * NONE—No standardization of spatial weights is applied.

          * ROW—Spatial weights are standardized; each weight is divided by its row sum
          (the sum of the weights of all neighboring features).
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for Inverse Distance and Fixed Distance options.
          Features outside the specified cutoff for a target feature are ignored in
          analyses for that feature. However, for Zone of Indifference, the influence of
          features outside the given distance is reduced with distance, while those inside
          the distance threshold are equally considered. The distance value entered should
          match that of the output coordinate system.For the Inverse Distance
          conceptualizations of spatial relationships, a value of
          0 indicates that no threshold distance is applied; when this parameter is left
          blank, a default threshold value is computed and applied.  This default value is
          the Euclidean distance that ensures every feature has at least one neighbor.This
          parameter has no effect when Polygon Contiguity or Get Spatial Weights From
          File spatial conceptualizations are selected.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and potentially
          temporal, relationships among features.
      Apply_False_Discovery_Rate__FDR__Correction {Boolean}:
          * APPLY_FDR—Statistical significance will be based on the False Discovery Rate
          correction for a 95 percent confidence level.

          * NO_FDR—Features with p-values less than 0.05 will appear in the COType field
          reflecting statistically significant clusters or outliers at a 95 percent
          confidence level (default).

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class to receive the results fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ClustersOutliers_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, Distance_Band_or_Threshold_Distance, Weights_Matrix_File, Apply_False_Discovery_Rate__FDR__Correction), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GroupingAnalysis_stats', None)
def GroupingAnalysis(Input_Features=None, Unique_ID_Field=None, Output_Feature_Class=None, Number_of_Groups=None, Analysis_Fields=None, Spatial_Constraints=None, Distance_Method=None, Number_of_Neighbors=None, Weights_Matrix_File=None, Initialization_Method=None, Initialization_Field=None, Output_Report_File=None, Evaluate_Optimal_Number_of_Groups=None):
    """GroupingAnalysis_stats(Input_Features, Unique_ID_Field, Output_Feature_Class, Number_of_Groups, Analysis_Fields;Analysis_Fields..., Spatial_Constraints, {Distance_Method}, {Number_of_Neighbors}, {Weights_Matrix_File}, {Initialization_Method}, {Initialization_Field}, {Output_Report_File}, {Evaluate_Optimal_Number_of_Groups})

        Groups features based on feature attributes and optional spatial/temporal
        constraints.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class or feature layer for which you want to create groups.
      Unique_ID_Field (Field):
          An integer field containing a different value for every feature in the input
          feature class. If you don't have a Unique ID field, you can create one by adding
          an integer field to  your feature class table and calculating the field values
          to equal the FID or OBJECTID field.
      Number_of_Groups (Long):
          The number of groups to create. The Output Report parameter will be disabled for
          more than 15 groups.
      Analysis_Fields (Field):
          A list of fields you want to use to distinguish one group from another. The
          Output Report parameter will be disabled for more than 15 fields.
      Spatial_Constraints (String):
          Specifies if and how spatial relationships among features should constrain the
          groups created.

          * CONTIGUITY_EDGES_ONLY—Groups contain contiguous polygon features.  Only
          polygons that share an edge can be part of the same group.

          * CONTIGUITY_EDGES_CORNERS—Groups contain contiguous polygon features. Only
          polygons that share an edge or a vertex can be part of the same group.

          * DELAUNAY_TRIANGULATION—Features in the same group will have at least one
          natural neighbor in common with another feature in the group. Natural neighbor
          relationships are based on Delaunay Triangulation. Conceptually, Delaunay
          Triangulation creates a nonoverlapping mesh of triangles from feature centroids.
          Each feature is a triangle node and nodes that share edges are considered
          neighbors.

          * K_NEAREST_NEIGHBORS—Features in the same group will be near each other; each
          feature will be a neighbor of at least one other feature in the group. Neighbor
          relationships are based on the nearest K features where you specify an Integer
          value, K, for the Number_of_Neighbors parameter.

          * GET_SPATIAL_WEIGHTS_FROM_FILE—Spatial, and optionally temporal, relationships
          are defined by a spatial weights file (.swm). Create the spatial weights matrix
          file using the Generate Spatial Weights Matrix or Generate Network Spatial
          Weights tool.

          * NO_SPATIAL_CONSTRAINT—Features will be grouped using data space proximity
          only. Features do not have to be near each other in space or time to be part of
          the same group.
      Distance_Method {String}:
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN—The straight-line distance between two points (as the crow flies)

          * MANHATTAN—The distance between two points measured along axes at right angles
          (city block); calculated by summing the (absolute) difference between the x- and
          y-coordinates
      Number_of_Neighbors {Long}:
          This parameter may be specified whenever the Spatial_Constraints parameter is
          K_NEAREST_NEIGHBORS or one of the contiguity methods (CONTIGUITY_EDGES_ONLY or
          CONTIGUITY_EDGES_CORNERS). The default number of neighbors is 8 and cannot be
          smaller than 2 for K_NEAREST_NEIGHBORS. This value reflects the exact number of
          nearest neighbor candidates to consider when building groups. A feature will not
          be included in a group unless one of the other features in that group is a K
          nearest neighbor. The default for CONTIGUITY_EDGES_ONLY and
          CONTIGUITY_EDGES_CORNERS is 0. For the contiguity methods, this value reflects
          the minimum number of neighbor candidates to consider. Additional nearby
          neighbors for features with less than the Number_of_Neighbors specified will be
          based on feature centroid proximity.
      Weights_Matrix_File {File}:
          The path to a file containing spatial weights that define spatial relationships
          among features.
      Initialization_Method {String}:
          Specifies how initial seeds are obtained when the Spatial_Constraint parameter
          selected is NO_SPATIAL_CONSTRAINT. Seeds are used to grow groups. If you
          indicate you want three groups, for example, the analysis will begin with three
          seeds.

          * FIND_SEED_LOCATIONS—Seed features will be selected to optimize performance.

          * GET_SEEDS_FROM_FIELD—Nonzero entries in the Initialization Field will be used
          as starting points to grow groups.

          * USE_RANDOM_SEEDS—Initial seed features will be randomly selected.
      Initialization_Field {Field}:
          The numeric field identifying seed features. Features with a value of 1 for this
          field will be used to grow groups.
      Evaluate_Optimal_Number_of_Groups {Boolean}:
          * EVALUATE—Groupings from 2 to 15 will be evaluated.

          * DO_NOT_EVALUATE—No evaluation of the number of groups will be performed. This
          is the default.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The new output feature class created containing all features, the analysis
          fields specified, and a field indicating which group each feature belongs to.
      Output_Report_File {File}:
          The full path for the PDF report file to be created summarizing group
          characteristics. This report provides a number of graphs to help you compare the
          characteristics of each group. Creating the report file can add substantial
          processing time."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GroupingAnalysis_stats(*gp_fixargs((Input_Features, Unique_ID_Field, Output_Feature_Class, Number_of_Groups, Analysis_Fields, Spatial_Constraints, Distance_Method, Number_of_Neighbors, Weights_Matrix_File, Initialization_Method, Initialization_Field, Output_Report_File, Evaluate_Optimal_Number_of_Groups), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('HotSpots_stats', None)
def HotSpots(Input_Feature_Class=None, Input_Field=None, Output_Feature_Class=None, Conceptualization_of_Spatial_Relationships=None, Distance_Method=None, Standardization=None, Distance_Band_or_Threshold_Distance=None, Self_Potential_Field=None, Weights_Matrix_File=None, Apply_False_Discovery_Rate__FDR__Correction=None):
    """HotSpots_stats(Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, {Distance_Band_or_Threshold_Distance}, {Self_Potential_Field}, {Weights_Matrix_File}, {Apply_False_Discovery_Rate__FDR__Correction})

        Given a set of weighted features, identifies statistically significant hot spots
        and cold spots using the Getis-Ord Gi* statistic.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which hot spot analysis will be performed.
      Input_Field (Field):
          The numeric field (number of victims, crime rate, test scores, and so on) to be
          evaluated.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are defined.

          * INVERSE_DISTANCE—Nearby neighboring features have a larger influence on the
          computations for a target feature than features that are far away.

          * INVERSE_DISTANCE_SQUARED—Same as INVERSE_DISTANCE except that the slope is
          sharper, so influence drops off more quickly, and only a target feature's
          closest neighbors will exert substantial influence on computations for that
          feature.

          * FIXED_DISTANCE_BAND—Each feature is analyzed within the context of neighboring
          features. Neighboring features inside the specified critical distance
          (Distance_Band_or_Threshold) receive a weight of one and exert influence on
          computations for the target feature. Neighboring features outside the critical
          distance receive a weight of zero and have no influence on a target feature's
          computations.

          * ZONE_OF_INDIFFERENCE—Features within the specified critical distance
          (Distance_Band_or_Threshold) of a target feature receive a weight of one and
          influence computations for that feature. Once the critical distance is exceeded,
          weights (and the influence a neighboring feature has on target feature
          computations) diminish with distance.

          * CONTIGUITY_EDGES_ONLY—Only neighboring polygon features that share a boundary
          or overlap will influence computations for the target polygon feature.

          * CONTIGUITY_EDGES_CORNERS—Polygon features that share a boundary, share a node,
          or overlap will influence computations for the target polygon feature.

          * GET_SPATIAL_WEIGHTS_FROM_FILE—Spatial relationships are defined by a specified
          spatial weights file. The path to the spatial weights file is specified by the
          Weights_Matrix_File parameter.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Standardization (String):
          Row standardization has no impact on this tool: results from Hot Spot Analysis
          (the Getis-Ord Gi* statistic) would be identical with or without row
          standardization. The parameter is disabled; it remains as a tool parameter only
          to support backwards compatibility.

          * NONE—No standardization of spatial weights is applied.

          * ROW—No standardization of spatial weights is applied.
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a cutoff distance for the inverse distance and fixed distance options.
          Features outside the specified cutoff for a target feature are ignored in
          analyses for that feature. However, for ZONE_OF_INDIFFERENCE, the influence of
          features outside the given distance is reduced with distance, while those inside
          the distance threshold are equally considered. The distance value entered should
          match that of the output coordinate system.For the inverse distance
          conceptualizations of spatial relationships, a value of
          0 indicates that no threshold distance is applied; when this parameter is left
          blank, a default threshold value is computed and applied.  This default value is
          the Euclidean distance that ensures every feature has at least one neighbor.This
          parameter has no effect when polygon contiguity (CONTIGUITY_EDGES_ONLY or
          CONTIGUITY_EDGES_CORNERS) or GET_SPATIAL_WEIGHTS_FROM_FILE spatial
          conceptualizations are selected.
      Self_Potential_Field {Field}:
          The field representing self potential: the distance or weight between a feature
          and itself.
      Weights_Matrix_File {File}:
          The path to a file containing weights that define spatial, and potentially
          temporal, relationships among features.
      Apply_False_Discovery_Rate__FDR__Correction {Boolean}:
          * APPLY_FDR—Statistical significance will be based on the False Discovery Rate
          correction.

          * NO_FDR—Statistical significance will be based on the p-value and z-score
          fields (default).

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class to receive the z-score and p-value results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HotSpots_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Output_Feature_Class, Conceptualization_of_Spatial_Relationships, Distance_Method, Standardization, Distance_Band_or_Threshold_Distance, Self_Potential_Field, Weights_Matrix_File, Apply_False_Discovery_Rate__FDR__Correction), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('OptimizedHotSpotAnalysis_stats', None)
def OptimizedHotSpotAnalysis(Input_Features=None, Output_Features=None, Analysis_Field=None, Incident_Data_Aggregation_Method=None, Bounding_Polygons_Defining_Where_Incidents_Are_Possible=None, Polygons_For_Aggregating_Incidents_Into_Counts=None, Density_Surface=None):
    """OptimizedHotSpotAnalysis_stats(Input_Features, Output_Features, {Analysis_Field}, {Incident_Data_Aggregation_Method}, {Bounding_Polygons_Defining_Where_Incidents_Are_Possible}, {Polygons_For_Aggregating_Incidents_Into_Counts}, {Density_Surface})

        Given incident points or weighted features (points or polygons), creates a map
        of statistically significant hot and cold spots using the Getis-Ord Gi*
        statistic. It evaluates the characteristics of the input feature class to
        produce optimal results.

     INPUTS:
      Input_Features (Feature Layer):
          The point or polygon feature class for which hot spot analysis will be
          performed.
      Analysis_Field {Field}:
          The numeric field (number of incidents, crime rates, test scores, and so on) to
          be evaluated.
      Incident_Data_Aggregation_Method {String}:
          The aggregation method to use to create weighted features for analysis from
          incident point data.

          * COUNT_INCIDENTS_WITHIN_FISHNET_POLYGONS—A fishnet polygon mesh will overlay
          the incident point data and the number of incidents within each polygon cell
          will be counted. If no bounding polygon is provided in the
          Bounding_Polygons_Defining_Where_Incidents_Are_Possible parameter, only cells
          with at least one incident will be used in the analysis; otherwise, all cells
          within the bounding polygons will be analyzed.

          * COUNT_INCIDENTS_WITHIN_AGGREGATION_POLYGONS—You provide aggregation polygons
          to overlay the incident point data in the
          Polygons_For_Aggregating_Incidents_Into_Counts parameter. The incidents within
          each polygon are counted.

          * SNAP_NEARBY_INCIDENTS_TO_CREATE_WEIGHTED_POINTS—Nearby incidents will be
          aggregated together to create a single weighted point. The weight for each point
          is the number of aggregated incidents at that location.
      Bounding_Polygons_Defining_Where_Incidents_Are_Possible {Feature Layer}:
          A polygon feature class defining where the incident Input_Features could
          possibly occur.
      Polygons_For_Aggregating_Incidents_Into_Counts {Feature Layer}:
          The polygons to use to aggregate the incident Input_Features in order to get an
          incident count for each polygon feature.

     OUTPUTS:
      Output_Features (Feature Class):
          The output feature class to receive the z-score, p-value, and Gi_Bin results.
      Density_Surface {Raster Dataset}:
          The output density surface of point input features. This parameter is only
          enabled when Input_Features are points and you have the ArcGIS Spatial Analyst
          extension. The output surface created will be clipped to the raster analysis
          mask specified in your environment settings. If no raster mask is specified, the
          output raster layer will be clipped to a convex hull of the input features."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.OptimizedHotSpotAnalysis_stats(*gp_fixargs((Input_Features, Output_Features, Analysis_Field, Incident_Data_Aggregation_Method, Bounding_Polygons_Defining_Where_Incidents_Are_Possible, Polygons_For_Aggregating_Incidents_Into_Counts, Density_Surface), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SimilaritySearch_stats', None)
def SimilaritySearch(Input_Features_To_Match=None, Candidate_Features=None, Output_Features=None, Collapse_Output_To_Points=None, Most_Or_Least_Similar=None, Match_Method=None, Number_Of_Results=None, Attributes_Of_Interest=None, Fields_To_Append_To_Output=None):
    """SimilaritySearch_stats(Input_Features_To_Match, Candidate_Features, Output_Features, Collapse_Output_To_Points, Most_Or_Least_Similar, Match_Method, Number_Of_Results, Attributes_Of_Interest;Attributes_Of_Interest..., {Fields_To_Append_To_Output;Fields_To_Append_To_Output...})

        Identifies which candidate features are most similar or most dissimilar to one
        or more input features based on feature attributes.

     INPUTS:
      Input_Features_To_Match (Feature Layer):
          The layer (or a selection on a layer) containing the features you want to match;
          you are searching for other features that look like these features. When more
          than one feature is provided, matching is based on attribute averages.Tip: When
          your Input Features To Match and Candidate Features come from a single
          dataset

          * Select the reference features you want to match.

          * Right-click the layer and choose Selection followed by Create Layer From
          Selected Features. Use the new layer created for this parameter.

          * Right-click the layer again and choose Selection followed by Switch Selection
          to get the layer you will use for your Candidate Features.
      Candidate_Features (Feature Layer):
          The layer (or a selection on a layer) containing candidate matching features.
          The tool will look for features most like (or most dislike) the
          Input_Features_To_Match among these candidates.
      Collapse_Output_To_Points (Boolean):
          Specify whether you want the geometry for the Output_Features to be points or to
          match the geometry (lines or polygons) of the input features. This option is
          only available when the Input_Features_To_Match and the Candidate_Features are
          both lines or both polygons. Choosing COLLAPSE for large line or polygon
          datasets will improve tool performance.

          * COLLAPSE—The line and polygon features will be represented as feature
          centroids (points).

          * NO_COLLAPSE—The output geometry will match the line or polygon geometry of the
          input features. This is the default.
      Most_Or_Least_Similar (String):
          Choose whether you are interested in features that are most alike or most
          different to the Input_Features_To_Match.

          * MOST_SIMILAR—Find the features that are most alike.

          * LEAST_SIMILAR—Find the features that are most different.

          * BOTH—Find both the features that are most alike and the features that are most
          different.
      Match_Method (String):
          Choose whether matching should be based on values, ranks, or cosine
          relationships.

          * ATTRIBUTE_VALUES—Similarity or dissimilarity will be based on the sum of
          squared standardized attribute value differences for all the Attributes Of
          Interest.

          * RANKED_ATTRIBUTE_VALUES—Similarity or dissimilarity will be based on the sum
          of squared rank differences for all the Attributes Of Interest.

          * ATTRIBUTE_PROFILES—Similarity or dissimilarity will be computed as a function
          of cosine similarity for all the Attributes Of Interest.
      Number_Of_Results (Long):
          The number of solution matches to find. Entering zero or a number larger than
          the total number of  Candidate_Features will return rankings for all the
          candidate features.
      Attributes_Of_Interest (Field):
          A list of numeric attributes representing the matching criteria.
      Fields_To_Append_To_Output {Field}:
          An optional list of attributes to include with the Output_Features. You might
          want to include a name identifier, categorical field, or date field, for
          example. These fields are not used to determine similarity; they are only
          included in the Output_Features for your reference.

     OUTPUTS:
      Output_Features (Feature Class):
          The output feature class contains a record for each of the
          Input_Features_To_Match and for all the solution-matching features found."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SimilaritySearch_stats(*gp_fixargs((Input_Features_To_Match, Candidate_Features, Output_Features, Collapse_Output_To_Points, Most_Or_Least_Similar, Match_Method, Number_Of_Results, Attributes_Of_Interest, Fields_To_Append_To_Output), True)))
        return retval
    except Exception, e:
        raise e


# Measuring Geographic Distributions toolset
@gptooldoc('CentralFeature_stats', None)
def CentralFeature(Input_Feature_Class=None, Output_Feature_Class=None, Distance_Method=None, Weight_Field=None, Self_Potential_Weight_Field=None, Case_Field=None):
    """CentralFeature_stats(Input_Feature_Class, Output_Feature_Class, Distance_Method, {Weight_Field}, {Self_Potential_Weight_Field}, {Case_Field})

        Identifies the most centrally located feature in a point, line, or polygon
        feature class.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing a distribution of features from which to identify
          the most centrally located feature.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates
      Weight_Field {Field}:
          The numeric field used to weight distances in the origin-destination distance
          matrix.
      Self_Potential_Weight_Field {Field}:
          The field representing self-potential—the distance or weight between a feature
          and itself.
      Case_Field {Field}:
          Field used to group features for separate central feature computations. The case
          field can be of integer, date, or string type.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The feature class that will contain the most centrally located feature in the
          Input Feature Class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CentralFeature_stats(*gp_fixargs((Input_Feature_Class, Output_Feature_Class, Distance_Method, Weight_Field, Self_Potential_Weight_Field, Case_Field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DirectionalDistribution_stats', None)
def DirectionalDistribution(Input_Feature_Class=None, Output_Ellipse_Feature_Class=None, Ellipse_Size=None, Weight_Field=None, Case_Field=None):
    """DirectionalDistribution_stats(Input_Feature_Class, Output_Ellipse_Feature_Class, Ellipse_Size, {Weight_Field}, {Case_Field})

        Creates standard deviational ellipses to summarize the spatial characteristics
        of geographic features: central tendency, dispersion, and directional trends.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class containing a distribution of features for which the standard
          deviational ellipse will be calculated.
      Ellipse_Size (String):
          The size of output ellipses in standard deviations. The default ellipse size is
          1; valid choices are 1, 2, or 3 standard deviations.

          * 1_STANDARD_DEVIATION

          * 2_STANDARD_DEVIATIONS

          * 3_STANDARD_DEVIATIONS
      Weight_Field {Field}:
          The numeric field used to weight locations according to their relative
          importance.
      Case_Field {Field}:
          Field used to group features for separate directional distribution calculations.
          The case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Ellipse_Feature_Class (Feature Class):
          A polygon feature class that will contain the output ellipse feature."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DirectionalDistribution_stats(*gp_fixargs((Input_Feature_Class, Output_Ellipse_Feature_Class, Ellipse_Size, Weight_Field, Case_Field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('DirectionalMean_stats', None)
def DirectionalMean(Input_Feature_Class=None, Output_Feature_Class=None, Orientation_Only=None, Case_Field=None):
    """DirectionalMean_stats(Input_Feature_Class, Output_Feature_Class, Orientation_Only, {Case_Field})

        Identifies the mean direction, length, and geographic center for a set of lines.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing vectors for which the mean direction will be
          calculated.
      Orientation_Only (Boolean):
          * DIRECTION—The From and To nodes are utilized in calculating the mean
          (default).

          * ORIENTATION_ONLY—The From and To node information is ignored.
      Case_Field {Field}:
          Field used to group features for separate directional mean calculations. The
          case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A line feature class that will contain the features representing the mean
          directions of the input feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.DirectionalMean_stats(*gp_fixargs((Input_Feature_Class, Output_Feature_Class, Orientation_Only, Case_Field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MeanCenter_stats', None)
def MeanCenter(Input_Feature_Class=None, Output_Feature_Class=None, Weight_Field=None, Case_Field=None, Dimension_Field=None):
    """MeanCenter_stats(Input_Feature_Class, Output_Feature_Class, {Weight_Field}, {Case_Field}, {Dimension_Field})

        Identifies the geographic center (or the center of concentration) for a set of
        features.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class for which the mean center will be calculated.
      Weight_Field {Field}:
          The numeric field used to create a weighted mean center.
      Case_Field {Field}:
          Field used to group features for separate mean center calculations. The case
          field can be of integer, date, or string type.
      Dimension_Field {Field}:
          A numeric field containing attribute values from which an average value will be
          calculated.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A point feature class that will contain the features representing the mean
          centers of the input feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MeanCenter_stats(*gp_fixargs((Input_Feature_Class, Output_Feature_Class, Weight_Field, Case_Field, Dimension_Field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MedianCenter_stats', None)
def MedianCenter(Input_Feature_Class=None, Output_Feature_Class=None, Weight_Field=None, Case_Field=None, Attribute_Field=None):
    """MedianCenter_stats(Input_Feature_Class, Output_Feature_Class, {Weight_Field}, {Case_Field}, {Attribute_Field;Attribute_Field...})

        Identifies the location that minimizes overall Euclidean distance to the
        features in a dataset.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class for which the median center will be calculated.
      Weight_Field {Field}:
          The numeric field used to create a weighted median center.
      Case_Field {Field}:
          Field used to group features for separate median center calculations. The case
          field can be of integer, date, or string type.
      Attribute_Field {Field}:
          Numeric field(s) for which the data median value will be computed.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          A point feature class that will contain the features representing the median
          centers of the input feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MedianCenter_stats(*gp_fixargs((Input_Feature_Class, Output_Feature_Class, Weight_Field, Case_Field, Attribute_Field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('StandardDistance_stats', None)
def StandardDistance(Input_Feature_Class=None, Output_Standard_Distance_Feature_Class=None, Circle_Size=None, Weight_Field=None, Case_Field=None):
    """StandardDistance_stats(Input_Feature_Class, Output_Standard_Distance_Feature_Class, Circle_Size, {Weight_Field}, {Case_Field})

        Measures the degree to which features are concentrated or dispersed around the
        geometric mean center.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          A feature class containing a distribution of features for which the standard
          distance will be calculated.
      Circle_Size (String):
          The size of output circles in standard deviations. The default circle size is 1;
          valid choices are 1, 2, or 3 standard deviations.

          * 1_STANDARD_DEVIATION

          * 2_STANDARD_DEVIATIONS

          * 3_STANDARD_DEVIATIONS
      Weight_Field {Field}:
          The numeric field used to weight locations according to their relative
          importance.
      Case_Field {Field}:
          Field used to group features for separate standard distance calculations. The
          case field can be of integer, date, or string type.

     OUTPUTS:
      Output_Standard_Distance_Feature_Class (Feature Class):
          A polygon feature class that will contain a circle polygon for each input
          center. These circle polygons graphically portray the standard distance at each
          center point."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.StandardDistance_stats(*gp_fixargs((Input_Feature_Class, Output_Standard_Distance_Feature_Class, Circle_Size, Weight_Field, Case_Field), True)))
        return retval
    except Exception, e:
        raise e


# Modeling Spatial Relationships toolset
@gptooldoc('ExploratoryRegression_stats', None)
def ExploratoryRegression(Input_Features=None, Dependent_Variable=None, Candidate_Explanatory_Variables=None, Weights_Matrix_File=None, Output_Report_File=None, Output_Results_Table=None, Maximum_Number_of_Explanatory_Variables=None, Minimum_Number_of_Explanatory_Variables=None, Minimum_Acceptable_Adj_R_Squared=None, Maximum_Coefficient_p_value_Cutoff=None, Maximum_VIF_Value_Cutoff=None, Minimum_Acceptable_Jarque_Bera_p_value=None, Minimum_Acceptable_Spatial_Autocorrelation_p_value=None):
    """ExploratoryRegression_stats(Input_Features, Dependent_Variable, Candidate_Explanatory_Variables;Candidate_Explanatory_Variables..., {Weights_Matrix_File}, {Output_Report_File}, {Output_Results_Table}, {Maximum_Number_of_Explanatory_Variables}, {Minimum_Number_of_Explanatory_Variables}, {Minimum_Acceptable_Adj_R_Squared}, {Maximum_Coefficient_p_value_Cutoff}, {Maximum_VIF_Value_Cutoff}, {Minimum_Acceptable_Jarque_Bera_p_value}, {Minimum_Acceptable_Spatial_Autocorrelation_p_value})

        The Exploratory Regression tool evaluates all possible combinations of the
        input candidate explanatory variables, looking for OLS models that best explain
        the dependent variable within the context of user-specified criteria.You can
        access the results of this tool (including the optional report file)
        from the Results window. If you disable background processing, results will also
        be written to the Progress dialog box.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class or feature layer containing the dependent and candidate
          explanatory variables to analyze.
      Dependent_Variable (Field):
          The numeric field containing the observed values you want to model using OLS.
      Candidate_Explanatory_Variables (Field):
          A list of fields to try as OLS model explanatory variables.
      Weights_Matrix_File {File}:
          A file containing spatial weights that define the spatial relationships among
          your input features. This file is used to assess spatial autocorrelation among
          regression residuals. You can use the Generate Spatial Weights Matrix File tool
          to create this. When you do not provide a spatial weights matrix file, residuals
          are assessed for spatial autocorrelation based on each feature's 8 nearest
          neighbors.Note: The spatial weights matrix file is only used to analyze spatial
          structure
          in model residuals; it is not used to build or to calibrate any of the OLS
          models.
      Maximum_Number_of_Explanatory_Variables {Long}:
          All models with explanatory variables up to the value entered here will be
          assessed. If, for example, the Minimum_Number_of_Explanatory_Variables is 2 and
          the Maximum_Number_of_Explanatory_Variables is 3, the Exploratory Regression
          tool will try all models with every combination of two explanatory variables,
          and all models with every combination of three explanatory variables.
      Minimum_Number_of_Explanatory_Variables {Long}:
          This value represents the minimum number of explanatory variables for models
          evaluated. If, for example, the Minimum_Number_of_Explanatory_Variables is 2 and
          the Maximum_Number_of_Explanatory_Variables is 3, the Exploratory Regression
          tool will try all models with every combination of two explanatory variables,
          and all models with every combination of three explanatory variables.
      Minimum_Acceptable_Adj_R_Squared {Double}:
          This is the lowest Adjusted R-Squared value you consider a passing model. If a
          model passes all of your other search criteria, but has an Adjusted R-Squared
          value smaller than the value entered here, it will not show up as a Passing
          Model in the Output_Report_FileOutput Report File. Valid values for this
          parameter range from 0.0 to 1.0. The default value is 0.5, indicating that
          passing models will explain at least fifty percent of the variation in the
          dependent variable.
      Maximum_Coefficient_p_value_Cutoff {Double}:
          For each model evaluated, OLS computes explanatory variable coefficient
          p-values. The cutoff p-value you enter here represents the confidence level you
          require for all coefficients in the model in order to consider the model
          passing. Small p-values reflect a stronger confidence level. Valid values for
          this parameter range from 1.0 down to 0.0, but will most likely be 0.1, 0.05,
          0.01, 0.001, and so on. The default value is 0.05, indicating passing models
          will only contain explanatory variables whose coefficients are statistically at
          the 95 percent confidence level (p-values smaller than 0.05). To relax this
          default you would enter a larger p-value cutoff, such as 0.1. If you are getting
          lots of passing models, you will likely want to make this search criteria more
          stringent by decreasing the default p-value cutoff from 0.05 to 0.01 or smaller.
      Maximum_VIF_Value_Cutoff {Double}:
          This value reflects how much redundancy (multicollinearity) among model
          explanatory variables you will tolerate.  When the VIF (Variance Inflation
          Factor) value is higher than about 7.5, multicollinearity can make a model
          unstable; consequently, 7.5 is the default value here. If you want your passing
          models to have less redundancy, you would enter a smaller value, such as 5.0,
          for this parameter.
      Minimum_Acceptable_Jarque_Bera_p_value {Double}:
          The p-value returned by the Jarque-Bera diagnostic test indicates whether the
          model residuals are normally distributed. If the p-value is statistically
          significant (small),  the model residuals are not normal and the model is
          biased. Passing models should have large Jarque-Bera p-values. The default
          minimum acceptable p-value is 0.1. Only models returning p-values larger than
          this minimum will be considered passing. If you are having trouble finding
          unbiased passing models, and decide to relax this criterion, you might enter a
          smaller minimum p-value such as 0.05.
      Minimum_Acceptable_Spatial_Autocorrelation_p_value {Double}:
          For models that pass all of the other search criteria, the Exploratory
          Regression tool will check model residuals for spatial clustering using Global
          Moran's I. When the p-value for this diagnostic test is statistically
          significant (small), it indicates the model is very likely missing key
          explanatory variables (it isn't telling the whole story). Unfortunately, if you
          have spatial autocorrelation in your regression residuals, your model is
          misspecified, so you cannot trust your results. Passing models should have large
          p-values for this diagnostic test. The default minimum p-value is 0.1. Only
          models returning p-values larger than this minimum will be considered passing.
          If you are having trouble finding properly specified models because of this
          diagnostic test, and decide to relax this search criteria, you might enter a
          smaller minimum such as 0.05.

     OUTPUTS:
      Output_Report_File {File}:
          The report file contains tool results, including details about any models found
          that passed all the search criteria you entered. This output file also contains
          diagnostics to help you fix common regression problems in the case that you
          don't find any passing models.
      Output_Results_Table {Table}:
          The optional output table created containing the explanatory variables and
          diagnostics for all of the models within the Coefficient p-value and VIF value
          cutoffs."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExploratoryRegression_stats(*gp_fixargs((Input_Features, Dependent_Variable, Candidate_Explanatory_Variables, Weights_Matrix_File, Output_Report_File, Output_Results_Table, Maximum_Number_of_Explanatory_Variables, Minimum_Number_of_Explanatory_Variables, Minimum_Acceptable_Adj_R_Squared, Maximum_Coefficient_p_value_Cutoff, Maximum_VIF_Value_Cutoff, Minimum_Acceptable_Jarque_Bera_p_value, Minimum_Acceptable_Spatial_Autocorrelation_p_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateNetworkSpatialWeights_stats', None)
def GenerateNetworkSpatialWeights(Input_Feature_Class=None, Unique_ID_Field=None, Output_Spatial_Weights_Matrix_File=None, Input_Network=None, Impedance_Attribute=None, Impedance_Cutoff=None, Maximum_Number_of_Neighbors=None, Barriers=None, U_turn_Policy=None, Restrictions=None, Use_Hierarchy_in_Analysis=None, Search_Tolerance=None, Conceptualization_of_Spatial_Relationships=None, Exponent=None, Row_Standardization=None):
    """GenerateNetworkSpatialWeights_stats(Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Input_Network, Impedance_Attribute, {Impedance_Cutoff}, {Maximum_Number_of_Neighbors}, {Barriers}, {U_turn_Policy}, {Restrictions;Restrictions...}, {Use_Hierarchy_in_Analysis}, {Search_Tolerance}, {Conceptualization_of_Spatial_Relationships}, {Exponent}, {Row_Standardization})

        Constructs a spatial weights matrix file (.swm) using a Network dataset,
        defining feature spatial relationships in terms of the underlying network
        structure.

     INPUTS:
      Input_Feature_Class (Feature Class):
          The point feature class for which network spatial relationships among features
          will be assessed.
      Unique_ID_Field (Field):
          An integer field containing a different value for every feature in the input
          feature class. If you don't have a Unique ID field, you can create one by adding
          an integer field to  your feature class table and calculating the field values
          to equal the FID or OBJECTID field.
      Input_Network (Network Dataset Layer):
          The network dataset for which spatial relationships among features in the input
          feature class will be defined.
      Impedance_Attribute (String):
          The type of cost units to use as impedance in the analysis.
      Impedance_Cutoff {Double}:
          Specifies a cutoff value for INVERSE and FIXED conceptualizations of spatial
          relationships. Enter this value using the units specified by the
          Impedance_Attribute parameter.A value of zero indicates that no threshold is
          applied. When this parameter is
          left blank, a default threshold value is computed based on input feature class
          extent and the number of features.
      Maximum_Number_of_Neighbors {Long}:
          An integer reflecting the maximum number of neighbors to find for each feature.
      Barriers {Feature Layer}:
          The name of a point feature class with features representing blocked
          intersections, road closures, accident sites, or other locations where travel is
          blocked along the network.
      U-turn_Policy {String}:
          Specifies optional U-turn restrictions.

          * ALLOW_UTURNS—U-turns will be possible anywhere. This is the default.

          * NO_UTURNS—No U-turns will be allowed during navigation.

          * ALLOW_DEAD_ENDS_ONLY—U-turns will be possible only at the dead ends (that is,
          single-valent junctions).
      Restrictions {String}:
          A list of restrictions. Check the restrictions to be honored in spatial
          relationship computations.
      Use_Hierarchy_in_Analysis {Boolean}:
          Specifies whether or not to use a hierarchy in the analysis.

          * USE_HIERARCHY—Will use the network dataset's hierarchy attribute in a
          heuristic path algorithm to speed analysis.

          * NO_HIERARCHY—Will use an exact path algorithm instead. If there is no
          hierarchy attribute, this option does not affect analysis.
      Search_Tolerance {Linear unit}:
          The search threshold used to locate features in the Input_Feature_Class onto the
          network dataset. This parameter includes a search value and the units for the
          tolerance.
      Conceptualization_of_Spatial_Relationships {String}:
          Specifies how the weighting associated with each spatial relationship is
          specified.

          * INVERSE—Features farther away have a smaller weight than features nearby.

          * FIXED—Features within the Impendance_Cutoff are neighbors (weight of 1);
          features outside the Impendance_Cutoff are not weighted (weight of 0).
      Exponent {Double}:
          Parameter for the INVERSE Conceptualization_of_Spatial_Relationships
          calculation. Typical values are 1 or 2. Weights drop off quicker with distance
          as this exponent value increases.
      Row_Standardization {Boolean}:
          Row standardization is recommended whenever feature distribution is potentially
          biased due to sampling design or to an imposed aggregation scheme.

          * ROW_STANDARDIZATION—Spatial weights are standardized by row. Each weight is
          divided by its row sum.

          * NO_STANDARDIZATION—No standardization of spatial weights is applied.

     OUTPUTS:
      Output_Spatial_Weights_Matrix_File (File):
          The output network spatial weights matrix (.swm) file."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateNetworkSpatialWeights_stats(*gp_fixargs((Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Input_Network, Impedance_Attribute, Impedance_Cutoff, Maximum_Number_of_Neighbors, Barriers, U_turn_Policy, Restrictions, Use_Hierarchy_in_Analysis, Search_Tolerance, Conceptualization_of_Spatial_Relationships, Exponent, Row_Standardization), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GenerateSpatialWeightsMatrix_stats', None)
def GenerateSpatialWeightsMatrix(Input_Feature_Class=None, Unique_ID_Field=None, Output_Spatial_Weights_Matrix_File=None, Conceptualization_of_Spatial_Relationships=None, Distance_Method=None, Exponent=None, Threshold_Distance=None, Number_of_Neighbors=None, Row_Standardization=None, Input_Table=None, Date_Time_Field=None, Date_Time_Interval_Type=None, Date_Time_Interval_Value=None):
    """GenerateSpatialWeightsMatrix_stats(Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Conceptualization_of_Spatial_Relationships, {Distance_Method}, {Exponent}, {Threshold_Distance}, {Number_of_Neighbors}, {Row_Standardization}, {Input_Table}, {Date_Time_Field}, {Date_Time_Interval_Type}, {Date_Time_Interval_Value})

        Constructs a spatial weights matrix (.swm) file to represent the spatial
        relationships among features in a dataset.

     INPUTS:
      Input_Feature_Class (Feature Class):
          The feature class for which spatial relationships of features will be assessed.
      Unique_ID_Field (Field):
          An integer field containing a different value for every feature in the input
          feature class. If you don't have a Unique ID field, you can create one by adding
          an integer field to  your feature class table and calculating the field values
          to equal the FID or OBJECTID field.
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features are conceptualized.

          * INVERSE_DISTANCE—The impact of one feature on another feature decreases with
          distance.

          * FIXED_DISTANCE—Everything within a specified critical distance of each feature
          is included in the analysis; everything outside the critical distance is
          excluded.

          * K_NEAREST_NEIGHBORS—The closest k features are included in the analysis; k is
          a specified numeric parameter.

          * CONTIGUITY_EDGES_ONLY—Polygon features that share a boundary are neighbors.

          * CONTIGUITY_EDGES_CORNERS—Polygon features that share a boundary and/or share a
          node are neighbors.

          * DELAUNAY_TRIANGULATION—A mesh of nonoverlapping triangles is created from
          feature centroids; features associated with triangle nodes that share edges are
          neighbors.

          * SPACE_TIME_WINDOW—Features within a specified critical distance and specified
          time interval of each other are neighbors.

          * CONVERT_TABLE—Spatial relationships are defined in a table.
      Distance_Method {String}:
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN—The straight-line distance between two points (as the crow flies)

          * MANHATTAN—The distance between two points measured along axes at right angles
          (city block); calculated by summing the (absolute) difference between the x- and
          y-coordinates
      Exponent {Double}:
          Parameter for inverse distance calculation. Typical values are 1 or 2.
      Threshold_Distance {Double}:
          Specifies a cutoff distance for Inverse Distance and Fixed Distance
          conceptualizations of spatial relationships. Enter this value using the units
          specified in the environment output coordinate system. Defines the size of the
          Space window for the Space Time Window conceptualization of spatial
          relationships.A value of zero indicates that no threshold distance is applied.
          When this
          parameter is left blank, a default threshold value is computed based on output
          feature class extent and the number of features.
      Number_of_Neighbors {Long}:
          An integer reflecting either the minimum or the exact number of neighbors. For
          K_NEAREST_NEIGHBORS, each feature will have exactly this specified number of
          neighbors. For INVERSE_DISTANCE or FIXED_DISTANCE each feature will have at
          least this many neighbors (the threshold distance will be temporarily extended
          to ensure this many neighbors, if necessary). When one of the contiguity
          Conceptualizations of Spatial Relationships is selected, then each polygon will
          be assigned this minimum number of neighbors. For polygons with fewer than this
          number of contiguous neighbors, additional neighbors will be based on feature
          centroid proximity.
      Row_Standardization {Boolean}:
          Row standardization is recommended whenever feature distribution is potentially
          biased due to sampling design or to an imposed aggregation scheme.

          * ROW_STANDARDIZATION—Spatial weights are standardized by row. Each weight is
          divided by its row sum.

          * NO_STANDARDIZATION—No standardization of spatial weights is applied.
      Input_Table {Table}:
          A table containing numeric weights relating every feature to every other feature
          in the input feature class. Required fields are the Input Feature Class Unique
          ID field, NID (neighbor ID), and WEIGHT.
      Date_Time_Field {Field}:
          A date field with a timestamp for each feature.
      Date_Time_Interval_Type {String}:
          The units to use for measuring time.

          * SECONDS—Seconds

          * MINUTES—Minutes

          * HOURS—Hours

          * DAYS—Days

          * WEEKS—Weeks

          * MONTHS—30 Days

          * YEARS—Years
      Date_Time_Interval_Value {Long}:
          An Integer reflecting the number of time units comprising the time window.For
          example, if you select HOURS for the Date/Time Interval Type and 3 for the
          Date/Time Interval Value, the time window would be 3 hours; features within the
          specified space window and within the specified time window would be neighbors.

     OUTPUTS:
      Output_Spatial_Weights_Matrix_File (File):
          The full path for the spatial weights matrix file (.swm) you want to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateSpatialWeightsMatrix_stats(*gp_fixargs((Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Conceptualization_of_Spatial_Relationships, Distance_Method, Exponent, Threshold_Distance, Number_of_Neighbors, Row_Standardization, Input_Table, Date_Time_Field, Date_Time_Interval_Type, Date_Time_Interval_Value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('GeographicallyWeightedRegression_stats', None)
def GeographicallyWeightedRegression(in_features=None, dependent_field=None, explanatory_field=None, out_featureclass=None, kernel_type=None, bandwidth_method=None, distance=None, number_of_neighbors=None, weight_field=None, coefficient_raster_workspace=None, cell_size=None, in_prediction_locations=None, prediction_explanatory_field=None, out_prediction_featureclass=None):
    """GeographicallyWeightedRegression_stats(in_features, dependent_field, explanatory_field;explanatory_field..., out_featureclass, kernel_type, bandwidth_method, {distance}, {number_of_neighbors}, {weight_field}, {coefficient_raster_workspace}, {cell_size}, {in_prediction_locations}, {prediction_explanatory_field;prediction_explanatory_field...}, {out_prediction_featureclass})

        Performs Geographically Weighted Regression (GWR), a local form of linear
        regression used to model spatially varying relationships.

     INPUTS:
      in_features (Feature Layer):
          The feature class containing the dependent and independent variables.
      dependent_field (Field):
          The numeric field containing values for what you are trying to model.
      explanatory_field (Field):
          A list of fields representing independent explanatory variables in your
          regression model.
      kernel_type (String):
          Specifies if the kernel is constructed as a fixed distance, or if it is allowed
          to vary in extent as a function of feature density.

          * FIXED—The spatial context (the Gaussian kernel) used to solve each local
          regression analysis is a fixed distance.

          * ADAPTIVE —The spatial context (the Gaussian kernel) is a function of a
          specified number of neighbors. Where feature distribution is dense, the spatial
          context is smaller; where feature distribution is sparse, the spatial context is
          larger.
      bandwidth_method (String):
          Specifies how the extent of the kernel should be determined. When AICc or CV are
          selected, the tool will find the optimal distance or number of neighbors for
          you. Typically you will select either AICc or CV when you aren't sure what to
          use for the Distance or Number of neighbors parameter. Once the tool determines
          the optimal distance or number of neighbors, however, you would use the
          BANDWIDTH_PARAMETER option.

          * AICc—The extent of the kernel is determined using the Akaike Information
          Criterion (AICc).

          * CV—The extent of the kernel is determined using Cross Validation.

          * BANDWIDTH_PARAMETER—The extent of the kernel is determined by a fixed distance
          or a fixed number of neighbors. You must specify a value for either the Distance
          or Number of Neighbors parameters.
      distance {Double}:
          The distance whenever the kernel_type is FIXED and bandwidth_method is
          BANDWIDTH_PARAMETER.
      number_of_neighbors {Long}:
          The exact number of neighbors to include in the local bandwidth of the Gaussian
          kernel when kernel_type is ADAPTIVE and the bandwidth_method is
          BANDWIDTH_PARAMETER.
      weight_field {Field}:
          The numeric field containing a spatial weighting for individual features. This
          weight field allows some features to be more important in the model calibration
          process than others. Primarily useful when the number of samples taken at
          different locations varies, values for the dependent and independent variables
          are averaged, and places with more samples are more reliable (should be weighted
          higher). If you have an average of 25 different samples for one location, but an
          average of only 2 samples for another location, you can use the number of
          samples as your weight field so that locations with more samples have a larger
          influence on model calibration than locations with few samples.
      coefficient_raster_workspace {Workspace}:
          A full pathname to the workspace where all of the coefficient rasters will be
          created. When this workspace is provided, rasters are created for the intercept
          and every explanatory variable.
      cell_size {Analysis Cell Size}:
          The cell size (a number) or reference to the cell size (a pathname to a raster
          dataset) to use when creating the coefficient rasters.The default cell size is
          the shortest of the width or height of the extent
          specified in the geoprocessing environment output coordinate system, divided by
          250.
      in_prediction_locations {Feature Layer}:
          A feature class containing features representing locations where estimates
          should be computed. Each feature in this dataset should contain values for all
          of the explanatory variables specified; the dependent variable for these
          features will be estimated using the model calibrated for the input feature
          class data.
      prediction_explanatory_field {Field}:
          A list of fields representing explanatory variables in the Prediction locations
          feature class. These field names should be provided in the same order (a one-to-
          one correspondence) as those listed for the input feature class Explanatory
          variables parameter. If no prediction explanatory variables are given, the
          output prediction feature class will only contain computed coefficient values
          for each prediction location.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class to receive dependent variable estimates and residuals.
      out_prediction_featureclass {Feature Class}:
          The output feature class to receive dependent variable estimates for each
          feature in the Prediction locations feature class."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GeographicallyWeightedRegression_stats(*gp_fixargs((in_features, dependent_field, explanatory_field, out_featureclass, kernel_type, bandwidth_method, distance, number_of_neighbors, weight_field, coefficient_raster_workspace, cell_size, in_prediction_locations, prediction_explanatory_field, out_prediction_featureclass), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('OrdinaryLeastSquares_stats', None)
def OrdinaryLeastSquares(Input_Feature_Class=None, Unique_ID_Field=None, Output_Feature_Class=None, Dependent_Variable=None, Explanatory_Variables=None, Coefficient_Output_Table=None, Diagnostic_Output_Table=None, Output_Report_File=None):
    """OrdinaryLeastSquares_stats(Input_Feature_Class, Unique_ID_Field, Output_Feature_Class, Dependent_Variable, Explanatory_Variables;Explanatory_Variables..., {Coefficient_Output_Table}, {Diagnostic_Output_Table}, {Output_Report_File})

        Performs global Ordinary Least Squares (OLS) linear regression to generate
        predictions or to model a dependent variable in terms of its relationships to a
        set of explanatory variables.You can access the results of this tool (including
        the optional report file)
        from the Results window. If you disable background processing, results will also
        be written to the Progress dialog box.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class containing the dependent and independent variables for
          analysis.
      Unique_ID_Field (Field):
          An integer field containing a different value for every feature in the Input
          Feature Class.
      Dependent_Variable (Field):
          The numeric field containing values for what you are trying to model.
      Explanatory_Variables (Field):
          A list of fields representing explanatory variables in your regression model.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class to receive dependent variable estimates and residuals.
      Coefficient_Output_Table {Table}:
          The full path to an optional table that will receive model coefficients,
          standardized coefficients, standard errors, and probabilities for each
          explanatory variable.
      Diagnostic_Output_Table {Table}:
          The full path to an optional table that will receive model summary diagnostics.
      Output_Report_File {File}:
          The path to the optional PDF file you want the tool to create. This report file
          includes model diagnostics, graphs, and notes to help you interpret the OLS
          results."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.OrdinaryLeastSquares_stats(*gp_fixargs((Input_Feature_Class, Unique_ID_Field, Output_Feature_Class, Dependent_Variable, Explanatory_Variables, Coefficient_Output_Table, Diagnostic_Output_Table, Output_Report_File), True)))
        return retval
    except Exception, e:
        raise e


# Rendering toolset
@gptooldoc('ClustersOutliersRendered_stats', None)
def ClustersOutliersRendered(Input_Feature_Class=None, Input_Field=None, Output_Layer_File=None, Output_Feature_Class=None):
    """ClustersOutliersRendered_stats(Input_Feature_Class, Input_Field, Output_Layer_File, Output_Feature_Class)

        Given a set of weighted features, identifies hot spots, cold spots, and spatial
        outliers using the Anselin Local Moran's I statistic. It then applies cold-to-
        hot rendering to the z-score results.Due to new capabilities in ArcGIS that
        allow output from script and model tools
        to be associated with default rendering, this tool will be deprecated post
        ArcGIS 10.1.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which cluster analysis will be performed.
      Input_Field (Field):
          The field to be evaluated.

     OUTPUTS:
      Output_Layer_File (Layer File):
          The output layer file to store rendering information.
      Output_Feature_Class (Feature Class):
          The output feature class to receive the results field, z-score, p-value, and
          cluster type designation."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ClustersOutliersRendered_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Output_Layer_File, Output_Feature_Class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CollectEventsRendered_stats', None)
def CollectEventsRendered(Input_Incident_Features=None, Output_Layer=None, Output_Weighted_Point_Feature_Class=None):
    """CollectEventsRendered_stats(Input_Incident_Features, Output_Layer, Output_Weighted_Point_Feature_Class)

        Converts event data to weighted point data and then applies a graduated circle
        rendering to the resultant count field.Due to new capabilities in ArcGIS that
        allow output from script and model tools
        to be associated with default rendering, this tool will be deprecated post
        ArcGIS 10.1.

     INPUTS:
      Input_Incident_Features (Feature Layer):
          The features representing event or incident data.

     OUTPUTS:
      Output_Layer (Layer File):
          The layer file (.lyr) to store the graduate circle rendering information.
      Output_Weighted_Point_Feature_Class (Feature Class):
          The output feature class to contain the weighted point data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CollectEventsRendered_stats(*gp_fixargs((Input_Incident_Features, Output_Layer, Output_Weighted_Point_Feature_Class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CountRenderer_stats', None)
def CountRenderer(input_feature_class=None, field_to_render=None, output_layer_file=None, number_of_classes=None, symbol_color=None, maximum_field_value=None):
    """CountRenderer_stats(input_feature_class, field_to_render, output_layer_file, number_of_classes, symbol_color, {maximum_field_value})

        Applies graduated circle rendering to a numeric field in a feature class.

     INPUTS:
      input_feature_class (Feature Layer):
          The feature layer containing count data to be rendered.
      field_to_render (Field):
          The name of the field containing count data.
      number_of_classes (Long):
          The number of classes into which the input feature class will be classified.
      symbol_color (String):
          The color of the graduated circles.

          * MANGO

          * BRIGHT_RED

          * DARK_GREEN

          * GREEN

          * DARK_BLUE

          * BRIGHT_PINK

          * LIGHT_YELLOW

          * SKY_BLUE
      maximum_field_value {Double}:
          The maximum attribute value that will be rendered. Features with field values
          greater than this maximum value will not be drawn.

     OUTPUTS:
      output_layer_file (Layer File):
          The new output layer file containing rendering information. You must include the
          .lyr extension as part of the file name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CountRenderer_stats(*gp_fixargs((input_feature_class, field_to_render, output_layer_file, number_of_classes, symbol_color, maximum_field_value), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('HotSpotsRendered_stats', None)
def HotSpotsRendered(Input_Feature_Class=None, Input_Field=None, Output_Layer_File=None, Output_Feature_Class=None, Distance_Band_or_Threshold_Distance=None):
    """HotSpotsRendered_stats(Input_Feature_Class, Input_Field, Output_Layer_File, Output_Feature_Class, {Distance_Band_or_Threshold_Distance})

        Calculates the Getis-Ord Gi* statistic for hot spot analysis and then applies a
        cold-to-hot type of rendering to the output z-scores.Due to new capabilities in
        ArcGIS that allow output from script and model tools
        to be associated with default rendering, this tool will be deprecated post
        ArcGIS 10.1.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class for which hot spot analysis will be performed.
      Input_Field (Field):
          The numeric field (number of victims, jobs, incident severity, and so on) to be
          evaluated.
      Distance_Band_or_Threshold_Distance {Double}:
          Specifies a distance cutoff value. Features outside the specified Distance Band
          or Threshold Distance are ignored in the hot spot analysis. The value entered
          for this parameter should be in the units of the Input Feature Class' coordinate
          system. There is one exception: if the Output Coordinate System environment
          variable is set, the value entered for this parameter should be in the units of
          the coordinate system set in that environment. When this field is left blank, a
          default distance value will be computed and applied.

     OUTPUTS:
      Output_Layer_File (Layer File):
          The layer file to store the cold-to-hot rendering information. You must include
          the .lyr extension as part of the file name.
      Output_Feature_Class (Feature Class):
          The output feature class to receive the results fields."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.HotSpotsRendered_stats(*gp_fixargs((Input_Feature_Class, Input_Field, Output_Layer_File, Output_Feature_Class, Distance_Band_or_Threshold_Distance), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ZRenderer_stats', None)
def ZRenderer(input_feature_class=None, field_to_render=None, output_layer_file=None):
    """ZRenderer_stats(input_feature_class, field_to_render, output_layer_file)

        Applies a cold (blue) to hot (red) color rendering scheme for a field of
        z-scores.

     INPUTS:
      input_feature_class (Feature Layer):
          The feature class containing a field with standardized z-scores.
      field_to_render (Field):
          The name of the field containing the z-scores.

     OUTPUTS:
      output_layer_file (Layer File):
          The new output layer file to store rendering information. You must include the
          .lyr extension as part of the file name."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ZRenderer_stats(*gp_fixargs((input_feature_class, field_to_render, output_layer_file), True)))
        return retval
    except Exception, e:
        raise e


# Utilities toolset
@gptooldoc('CalculateAreas_stats', None)
def CalculateAreas(Input_Feature_Class=None, Output_Feature_Class=None):
    """CalculateAreas_stats(Input_Feature_Class, Output_Feature_Class)

        Calculates area values for each feature in a polygon feature class.Because there
        are easier and more efficient ways to get the area of features,
        the Calculate Areas tool will no longer be included with ArcGIS Pro. Use the
        Calculate Field tool or the Geometry Calculator instead of the Calculate Areas
        tool in your workflows and custom script or models tools.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The input polygon feature class.

     OUTPUTS:
      Output_Feature_Class (Feature Class):
          The output feature class. This feature class is a copy of the input feature
          class with field F_AREA added (or updated). The F_AREA field contains the
          polygon area."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateAreas_stats(*gp_fixargs((Input_Feature_Class, Output_Feature_Class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CalculateDistanceBand_stats', None)
def CalculateDistanceBand(Input_Features=None, Neighbors=None, Distance_Method=None):
    """CalculateDistanceBand_stats(Input_Features, Neighbors, Distance_Method)

        Returns the minimum, the maximum, and the average distance to the specified Nth
        nearest neighbor (N is an input parameter) for a set of features. Results are
        written as tool execution messages.

     INPUTS:
      Input_Features (Feature Layer):
          The feature class or layer used to calculate distance statistics.
      Neighbors (Long):
          The number of neighbors (N) to consider for each feature. This number should be
          any integer between one and the total number of features in the feature class. A
          list of distances between each feature and its Nth neighbor is compiled, and the
          maximum, minimum, and average distances are output to the Results window.
      Distance_Method (String):
          Specifies how distances are calculated from each feature to neighboring
          features.

          * EUCLIDEAN_DISTANCE—The straight-line distance between two points (as the crow
          flies)

          * MANHATTAN_DISTANCE—The distance between two points measured along axes at
          right angles (city block); calculated by summing the (absolute) difference
          between the x- and y-coordinates"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CalculateDistanceBand_stats(*gp_fixargs((Input_Features, Neighbors, Distance_Method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('CollectEvents_stats', None)
def CollectEvents(Input_Incident_Features=None, Output_Weighted_Point_Feature_Class=None):
    """CollectEvents_stats(Input_Incident_Features, Output_Weighted_Point_Feature_Class)

        Converts event data, such as crime or disease incidents, to weighted point data.

     INPUTS:
      Input_Incident_Features (Feature Layer):
          The features representing event or incident data.

     OUTPUTS:
      Output_Weighted_Point_Feature_Class (Feature Class):
          The output feature class to contain the weighted point data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CollectEvents_stats(*gp_fixargs((Input_Incident_Features, Output_Weighted_Point_Feature_Class), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ConvertSpatialWeightsMatrixtoTable_stats', None)
def ConvertSpatialWeightsMatrixtoTable(Input_Spatial_Weights_Matrix_File=None, Output_Table=None):
    """ConvertSpatialWeightsMatrixtoTable_stats(Input_Spatial_Weights_Matrix_File, Output_Table)

        Converts a binary spatial weights matrix file (.swm) to a table.

     INPUTS:
      Input_Spatial_Weights_Matrix_File (File):
          The full pathname for the spatial weights matrix file (.swm) you want to
          convert.

     OUTPUTS:
      Output_Table (Table):
          A full pathname to the table you want to create."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConvertSpatialWeightsMatrixtoTable_stats(*gp_fixargs((Input_Spatial_Weights_Matrix_File, Output_Table), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('ExportXYv_stats', None)
def ExportXYv(Input_Feature_Class=None, Value_Field=None, Delimiter=None, Output_ASCII_File=None, Add_Field_Names_to_Output=None):
    """ExportXYv_stats(Input_Feature_Class, Value_Field;Value_Field..., Delimiter, Output_ASCII_File, Add_Field_Names_to_Output)

        Exports feature class coordinates and attribute values to a space, comma, or
        semicolon-delimited ASCII text file.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class from which to export feature coordinates and attribute values.
      Value_Field (Field):
          The field or fields in the input feature class containing the values to export
          to an ASCII text file.
      Delimiter (String):
          Specifies how feature coordinates and attribute values will be separated in the
          output ASCII file.

          * SPACE—Feature coordinates and attribute values will be separated by a space in
          the output.

          * COMMA—Feature coordinates and attribute values will be separated by a comma in
          the output.

          * SEMI-COLON—Feature coordinates and attribute values will be separated by a
          semicolon in the output.
      Add_Field_Names_to_Output (Boolean):
          * NO_FIELD_NAMES—No field names will be included in the output text file
          (default).

          * ADD_FIELD_NAMES—Field names will be written to the output text file.

     OUTPUTS:
      Output_ASCII_File (File):
          The ASCII text file that will contain the feature coordinate and attribute
          values."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportXYv_stats(*gp_fixargs((Input_Feature_Class, Value_Field, Delimiter, Output_ASCII_File, Add_Field_Names_to_Output), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject