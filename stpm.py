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
"""The Space Time Pattern Mining toolbox contains statistical tools for analyzing
data distributions and patterns in the context of both space and time. The
toolbox contains two tools: Create Space Time Cube and Emerging Hot Spot
Analysis."""
__all__ = ['CreateSpaceTimeCube', 'EmergingHotSpotAnalysis']
__alias__ = u'stpm'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('CreateSpaceTimeCube_stpm', None)
def CreateSpaceTimeCube(in_features=None, output_cube=None, time_field=None, template_cube=None, time_step_interval=None, time_step_alignment=None, reference_time=None, distance_interval=None):
    """CreateSpaceTimeCube_stpm(in_features, output_cube, time_field, {template_cube}, {time_step_interval}, {time_step_alignment}, {reference_time}, {distance_interval})

        Summarizes a set of points into a netCDF data structure by aggregating them
        into space-time bins. Within each bin, the points are counted. For all bin
        locations, the trend for counts over time are evaluated.

     INPUTS:
      in_features (Feature Layer):
          The input point feature class to be aggregated into space-time bins.
      time_field (Field):
          The field containing the date and time (timestamp) for each point. This field
          must be of type Date.
      template_cube {File}:
          A reference space-time cube used to define the output_cube extent of analysis,
          bin dimensions, and bin alignment.  The time_step_interval, distance_interval,
          and reference_time values are also obtained from the template cube.  This
          template cube must be a netCDF (.nc) file that has been created using this tool.
      time_step_interval {Time unit}:
          The number of seconds,  minutes, hours, days, weeks, or years that will
          represent a single time step. All points within the same Time Step Interval and
          Distance Interval will be aggregated. (When a Template Cube is provided, this
          parameter is disabled, and the Time Step Interval value is obtained from the
          template cube). Examples of valid entries for this parameter are 1 Weeks, 13
          Days, or 1 Years.
      time_step_alignment {String}:
          The basis for either starting or ending a time-step interval.  The range of
          timestamps associated with the points in the dataset creates a time extent
          ranging from the first time event to the last time event. If a template_cube is
          provided, this parameter is ignored and the time_step_alignment of the
          template_cube is used.

          * END_TIME—Time steps align to the last time event.

          * START_TIME—Time steps align to the first time event.

          * REFERENCE_TIME—Time steps align to a particular date/time that you specify. If
          all points in the input features have a timestamp larger than the reference time
          you provide, the time-step interval will begin with that reference time. If all
          points in the input features have a timestamp smaller than the reference time
          you provide, the time-step interval will end with that reference time. If the
          reference time you provide is in the middle of the time extent of your data, a
          time-step interval will be created starting with the reference time provided;
          additional intervals will be created both before and after the reference time
          until the full time extent of your data is covered.
      reference_time {Date}:
          The date/time to use to align the time-step intervals. If you want to bin your
          data weekly from Monday to Sunday, for example, you could set a reference time
          of Sunday at midnight to ensure bins break between Sunday and Monday at
          midnight.  (When a template_cube is provided, this parameter is ignored and the
          reference_time is based on the template_cube.)
      distance_interval {Linear unit}:
          The spatial extent of the bins used to aggregate the in_features. All points
          that fall within the same distance_interval and time_step_interval will be
          aggregated. (When a template_cube is provided, this parameter is ignored and the
          distance interval value will be based on the template_cube)

     OUTPUTS:
      output_cube (File):
          The output netCDF data cube that will be created to contain counts and
          summaries of the in_features point data."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateSpaceTimeCube_stpm(*gp_fixargs((in_features, output_cube, time_field, template_cube, time_step_interval, time_step_alignment, reference_time, distance_interval), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('EmergingHotSpotAnalysis_stpm', None)
def EmergingHotSpotAnalysis(in_cube=None, analysis_variable=None, output_features=None, neighborhood_distance=None, neighborhood_time_step=None, polygon_mask=None):
    """EmergingHotSpotAnalysis_stpm(in_cube, analysis_variable, output_features, {neighborhood_distance}, {neighborhood_time_step}, {polygon_mask})

        Identifies trends in the clustering of space-time point data, including new,
        intensifying, diminishing, and sporadic hot and cold spots.

     INPUTS:
      in_cube (File):
          The netCDF cube to be analyzed. This file must have an (.nc) extension and must
          have been created using the Create Space Time Cube tool.
      analysis_variable (String):
          The numeric variable in the netCDF file you want to analyze.
      neighborhood_distance {Linear unit}:
          The spatial extent of the analysis neighborhood. This value determines which
          features are analyzed together in order to assess local space-time clustering.
      neighborhood_time_step {Long}:
          The number of time-step intervals to include in the analysis neighborhood. This
          value determines which features are analyzed together in order to assess local
          space-time clustering.
      polygon_mask {Feature Layer}:
          A polygon feature layer with one or more polygons defining the analysis study
          area. You would use a polygon analysis mask to exclude a large lake from the
          analysis, for example. Bins defined in the Input Space Time Cube that fall
          outside of the mask will not be included in the analysis.

     OUTPUTS:
      output_features (Feature Class):
          The output feature class results. This feature class will be a two-dimensional
          map representation of the hot and cold spot trends in your data. It will show,
          for example, any new or intensifying hot spots."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.EmergingHotSpotAnalysis_stpm(*gp_fixargs((in_cube, analysis_variable, output_features, neighborhood_distance, neighborhood_time_step, polygon_mask), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject