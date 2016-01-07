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
"""The Tracking Analyst toolbox contains tools used to analyze temporal data and
prepare temporal data for use with the ArcGIS Tracking Analyst extension."""
__all__ = ['ConcatenateDateAndTimeFields', 'MakeTrackingLayer', 'TrackIntervalsToFeature', 'TrackIntervalsToLine']
__alias__ = u'ta'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('ConcatenateDateAndTimeFields_ta', None)
def ConcatenateDateAndTimeFields(Feature_Class=None, DateField=None, TimeField=None, OutputField=None):
    """ConcatenateDateAndTimeFields_ta(Feature_Class, DateField, TimeField, OutputField)

        Concatenates two separate date and time fields in a feature class or layer into
        a single field containing both the date and time.Tracking Analyst is designed to
        work with temporal data containing date and time
        information in a single field. If your data contains the date and time in two
        separate fields, this tool can be used to combine the information together into
        a new field that Tracking Analyst will understand.

     INPUTS:
      Feature_Class (Feature Layer):
          The input feature class or layer.
      DateField (Field):
          The text field in the input feature layer that contains date values.
      TimeField (Field):
          The text field in the input feature layer that contains time values.
      OutputField (String):
          The name of the new concatenated date/time field to be created and added to the
          input feature layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ConcatenateDateAndTimeFields_ta(*gp_fixargs((Feature_Class, DateField, TimeField, OutputField), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeTrackingLayer_ta', None)
def MakeTrackingLayer(in_features=None, out_layer=None, time_zone=None, adjusted_for_dst=None, storage_policy=None, start_time_field=None, time_field_format=None, locale_id=None, am_designator=None, pm_designator=None, track_id_field=None):
    """MakeTrackingLayer_ta(in_features, out_layer, time_zone, adjusted_for_dst, storage_policy, start_time_field, {time_field_format}, {locale_id}, {am_designator}, {pm_designator}, {track_id_field})

        This tool creates a tracking layer from a feature class or layer containing
        temporal data.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      time_zone (String):
          The time zone that the data in the input feature class was recorded in.  For a
          list of available time zones supported by your system, you can open the tool
          dialog box and expand this drop-down. When you enter the time zone as a
          parameter, you must use a non-localized string representation of the appropriate
          Microsoft Time Zone ID, and replace any spaces with underscore characters. For
          example, the appropriate string representation of the Pacific time zone in the
          United States is "Pacific_Standard_Time". "NO_TIME_ZONE" can be used to specify
          no time zone for the output tracking layer.
      adjusted_for_dst (Boolean):
          If you chose a time zone for your data, this parameter specifies whether the
          data values in the input time field were recorded with an adjustment for
          Daylight Saving Time.

          * ADJUSTED_FOR_DST—The data values in the input time field were recorded with an
          adjustment for Daylight Saving Time.

          * NOT_ADJUSTED_FOR_DST—The data values in the input time field were recorded
          without an adjustment for Daylight Saving Time.
      storage_policy (String):
          Determines the storage policy for the output tracking layer.

          * COPY_ALL_TO_MEMORY—The output tracking layer will be stored completely in
          memory.

          * KEEP_ON_DISK—The output tracking layer will use a disk-based storage system.
          This option should only be used when the input feature layer is very large.
      start_time_field (Field):
          The field in the input feature class or layer that contains date and time
          information. This tool requires date and time information to be contained in the
          same field, and the data type of the field must be Short, Long, Float, Double,
          Text, or Date.
      time_field_format {String}:
          If the data type of the time field is anything other than Date, this parameter
          determines the format that will be used to interpret data values in the time
          field. Some examples of formats are:

          * "yyyyMMdd" (standard format valid for Text or Numeric time fields)

          * "yyyy/MM/dd HH:mm:ss" (standard format valid only for Text time fields)

          * "MM-dd-yyyy hh:mm:ss tt" (custom format valid only for Text time fields)
          If the data type of the time field is Text, either a standard Esri text time
          format can be used or a custom format can be specified.  However, custom formats
          can not be used if you specified KEEP_ON_DISK for the storage policy. If the
          data type of the time field is numeric (Short, Long, Float, or Double), only
          standard Esri numeric time formats can be used.  If the data type of the time
          field is Date, this parameter is not needed.
      locale_id {Long}:
          If the data type of the time field is Text, this parameter determines which
          locale will be used to interpret data values in the time field.  For all time
          field data types other than Text, this parameter is not needed. If no locale is
          entered, the current locale of the operating system will be used. For a list of
          available locales supported by your system, open the tool dialog box and expand
          this drop-down. When entering the locale as a parameter, it is recommended to
          use only the locale ID (LCID) assigned by Microsoft, which can be entered as a
          long integer such as 1033. You can also enter the full string representation of
          the locale as a parameter, such as "01033-English_(United_States)", but you must
          replace spaces with underscore characters.
      am_designator {String}:
          If the time field data type is Text and the time format is a 12-hour clock
          representation including a time marker ("t" or "tt"), then this parameter
          determines the character ("t") or characters ("tt") that designate AM in the
          time field data values. If nothing is entered, then the default AM designator
          for the selected locale will be used. For all time field data types other than
          Text, this parameter is not needed.
      pm_designator {String}:
          If the time field data type is Text and the time format is a 12-hour clock
          representation including a time marker ("t" or "tt"), then this parameter
          determines the character ("t") or characters ("tt") that designate PM in the
          time field data values. If nothing is entered, then the default PM designator
          for the selected locale will be used. For all time field data types other than
          Text, this parameter is not needed.
      track_id_field {Field}:
          The field that contains data values that will be used to group features into
          tracks in the output tracking layer. The data type of the field can be Short,
          Long, Float, Double, Text, or OID.

     OUTPUTS:
      out_layer (Feature Layer):
          The name of the tracking layer to be created. The newly created tracking layer
          can be used as input to any geoprocessing tool that accepts a feature layer as
          input."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeTrackingLayer_ta(*gp_fixargs((in_features, out_layer, time_zone, adjusted_for_dst, storage_policy, start_time_field, time_field_format, locale_id, am_designator, pm_designator, track_id_field), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TrackIntervalsToFeature_ta', None)
def TrackIntervalsToFeature(in_features=None, time_field=None, track_id_field=None, calculation_method=None, time_field_format=None, locale_id=None, am_designator=None, pm_designator=None, distance_field_units=None, distance_field_name=None, duration_field_units=None, duration_field_name=None, speed_field_units=None, speed_field_name=None, course_field_units=None, course_field_name=None):
    """TrackIntervalsToFeature_ta(in_features, time_field, {track_id_field}, {calculation_method}, {time_field_format}, {locale_id}, {am_designator}, {pm_designator}, {distance_field_units}, {distance_field_name}, {duration_field_units}, {duration_field_name}, {speed_field_units}, {speed_field_name}, {course_field_units}, {course_field_name})

        Calculates values that are computed from the difference between successively
        ordered features in a track. New fields are added to the input feature class or
        layer to store the calculated values (distance, duration, speed, and course).

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      time_field (Field):
          The field in the input feature class or layer that contains date and time
          information. This tool requires date and time information to be contained in the
          same field, and the data type of the field must be Short, Long, Float, Double,
          Text, or Date.
      track_id_field {Field}:
          The field that contains data values which are used to group the input features
          into tracks. The data type of the field can be Short, Long, Float, Double, Text,
          or OID.
      calculation_method {String}:
          Specifies which interval is used to calculate values for each feature.

          * PREVIOUS_AND_CURRENT_FEATURE—Values are calculated using the interval between
          each feature and the previous feature in the track.

          * CURRENT_AND_NEXT_FEATURE—Values are calculated using the interval between each
          feature and the next feature in the track.
      time_field_format {String}:
          If the data type of the time field is anything other than Date, this parameter
          determines the format that will be used to interpret data values in the time
          field. Some examples of formats are:

          * "yyyyMMdd" (standard format valid for Text or Numeric time fields)

          * "yyyy/MM/dd HH:mm:ss" (standard format valid only for Text time fields)

          * "MM-dd-yyyy hh:mm:ss tt" (custom format valid only for Text time fields)
          If the data type of the time field is Text, either a standard Esri text time
          format can be used or a custom format can be specified.  However, custom formats
          cannot be used if you specified KEEP_ON_DISK for the storage policy. If the data
          type of the time field is numeric (Short, Long, Float, or Double), only standard
          Esri numeric time formats can be used.  If the data type of the time field is
          Date, this parameter is not needed.
      locale_id {Long}:
          If the data type of the time field is Text, this parameter determines which
          locale will be used to interpret data values in the time field.  For all time
          field data types other than Text, this parameter is not needed. If no locale is
          entered, the current locale of the operating system will be used. For a list of
          available locales supported by your system, open the tool dialog box and expand
          this drop-down list. When entering the locale as a parameter, it is recommended
          to use only the locale ID (LCID) assigned by Microsoft, which can be entered as
          a long integer such as 1033. You can also enter the full string representation
          of the locale as a parameter, such as "01033-English_(United_States)", but you
          must replace spaces with underscore characters.
      am_designator {String}:
          If the time field data type is Text and the time format is a 12-hour clock
          representation including a time marker ("t" or "tt"), then this parameter
          determines the character ("t") or characters ("tt") that designate AM in the
          time field data values. If nothing is entered, then the default AM designator
          for the selected locale will be used. For all time field data types other than
          Text, this parameter is not needed.
      pm_designator {String}:
          If the time field data type is Text and the time format is a 12-hour clock
          representation including a time marker ("t" or "tt"), then this parameter
          determines the character ("t") or characters ("tt") that designate PM in the
          time field data values. If nothing is entered, then the default PM designator
          for the selected locale will be used. For all time field data types other than
          Text, this parameter is not needed.
      distance_field_units {String}:
          Specifies the distance units that will be used in the output distance field.

          * INCHES—Inches

          * FEET—Feet

          * YARDS—Yards

          * MILES—Miles

          * NAUTICAL_MILES—Nautical Miles

          * MILLIMETERS—Millimeters

          * CENTIMETERS—Centimeters

          * METERS—Meters

          * KILOMETERS—Kilometers

          * DECIMETERS—Decimeters
      distance_field_name {String}:
          Specifies the name of the distance field that will be added to the input
          feature class or layer. If no field name is specified, a name will automatically
          be chosen.
      duration_field_units {String}:
          Specifies the time units that will be used in the output duration field.

          * MILLISECONDS—Milliseconds

          * SECONDS—Seconds

          * MINUTES—Minutes

          * HOURS—Hours

          * DAYS—Days

          * WEEKS—Weeks

          * MONTHS—Months

          * YEARS—Years
      duration_field_name {String}:
          Specifies the name of the duration field that will be added to the input
          feature class or layer. If no field name is specified, a name will automatically
          be chosen.
      speed_field_units {String}:
          Specifies the speed units that will be used in the output speed field.

          * MILES_PER_HOUR—Miles Per Hour

          * FEET_PER_HOUR—Feet Per Hour

          * KILOMETERS_PER_HOUR—Kilometers Per Hour

          * MILES_PER_SECOND—Miles Per Second

          * FEET_PER_SECOND—Feet Per Second

          * METERS_PER_SECOND—Meters Per Second

          * KNOTS—Knots
      speed_field_name {String}:
          Specifies the name of the speed field that will be added to the input feature
          class or layer. If no field name is specified, a name will automatically be
          chosen.
      course_field_units {String}:
          Specifies the course units that will be used in the output course field.

          * DEGREES—Degrees

          * RADIANS—Radians
      course_field_name {String}:
          Specifies the name of the course field that will be added to the input feature
          class or layer. If no field name is specified, a name will automatically be
          chosen."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TrackIntervalsToFeature_ta(*gp_fixargs((in_features, time_field, track_id_field, calculation_method, time_field_format, locale_id, am_designator, pm_designator, distance_field_units, distance_field_name, duration_field_units, duration_field_name, speed_field_units, speed_field_name, course_field_units, course_field_name), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TrackIntervalsToLine_ta', None)
def TrackIntervalsToLine(in_features=None, out_feature_class=None, time_field=None, track_id_field=None, time_field_format=None, locale_id=None, am_designator=None, pm_designator=None, distance_field_units=None, distance_field_name=None, duration_field_units=None, duration_field_name=None, speed_field_units=None, speed_field_name=None, course_field_units=None, course_field_name=None):
    """TrackIntervalsToLine_ta(in_features, out_feature_class, time_field, {track_id_field}, {time_field_format}, {locale_id}, {am_designator}, {pm_designator}, {distance_field_units}, {distance_field_name}, {duration_field_units}, {duration_field_name}, {speed_field_units}, {speed_field_name}, {course_field_units}, {course_field_name})

        Calculates values that are computed from the difference between successively
        ordered features in a track. A new line feature class is created to represent
        the track intervals and store the calculated values (distance, duration, speed,
        and course).

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer.
      time_field (Field):
          The field in the input feature class or layer that contains date and time
          information. This tool requires date and time information to be contained in the
          same field, and the data type of the field must be short, long, float, double,
          text, or date.
      track_id_field {Field}:
          The field that contains data values that are used to group the input features
          into tracks. The data type of the field can be short, long, float, double, text,
          or OID.
      time_field_format {String}:
          If the data type of the time field is anything other than date, this parameter
          determines the format that is used to interpret data values in the time field.
          Some examples of formats are as follows:

          * "yyyyMMdd" (standard format valid for text or numeric time fields)

          * "yyyy/MM/dd HH:mm:ss" (standard format valid only for text time fields)

          * "MM-dd-yyyy hh:mm:ss tt" (custom format valid only for text time fields)
          If the data type of the time field is text, either a standard Esri text time
          format can be used, or a custom format can be specified.  However, custom
          formats cannot be used if you specified KEEP_ON_DISK for the storage policy. If
          the data type of the time field is numeric (short, long, float, or double), only
          standard Esri numeric time formats can be used.  If the data type of the time
          field is date, this parameter is not needed.
      locale_id {Long}:
          If the data type of the time field is text, this parameter determines which
          locale is used to interpret data values in the time field.  For all time field
          data types other than text, this parameter is not needed. If no locale is
          entered, the current locale of the operating system is used. For a list of
          available locales supported by your system, open the tool dialog box and expand
          this drop-down list. When entering the locale as a parameter, it is recommended
          that you use only the locale ID (LCID) assigned by Microsoft, which can be
          entered as a long integer such as 1033. You can also enter the full string
          representation of the locale as a parameter, such as
          "01033-English_(United_States)", but you must replace spaces with underscore
          characters.
      am_designator {String}:
          If the time field data type is text and the time format is a 12-hour clock
          representation including a time marker (t or tt), this parameter determines the
          character (t) or characters (tt) that designate AM in the time field data
          values. If nothing is entered, the default AM designator for the selected locale
          is used. For all time field data types other than text, this parameter is not
          needed.
      pm_designator {String}:
          If the time field data type is text and the time format is a 12-hour clock
          representation including a time marker (t or tt), this parameter determines the
          character (t) or characters (tt) that designate PM in the time field data
          values. If nothing is entered, the default PM designator for the selected locale
          is used. For all time field data types other than text, this parameter is not
          needed.
      distance_field_units {String}:
          Specifies the distance units that will be used in the output distance field.

          * INCHES—Inches

          * FEET—Feet

          * YARDS—Yards

          * MILES—Miles

          * NAUTICAL_MILES—Nautical miles

          * MILLIMETERS—Millimeters

          * CENTIMETERS—Centimeters

          * METERS—Meters

          * KILOMETERS—Kilometers

          * DECIMETERS—Decimeters
      distance_field_name {String}:
          Specifies the name of the distance field that will be added to the input
          feature class or layer. If no field name is specified, a name is automatically
          chosen.
      duration_field_units {String}:
          Specifies the time units that will be used in the output duration field.

          * MILLISECONDS—Milliseconds

          * SECONDS—Seconds

          * MINUTES—Minutes

          * HOURS—Hours

          * DAYS—Days

          * WEEKS—Weeks

          * MONTHS—Months

          * YEARS—Years
      duration_field_name {String}:
          Specifies the name of the duration field that will be added to the input
          feature class or layer. If no field name is specified, a name is automatically
          chosen.
      speed_field_units {String}:
          Specifies the speed units that will be used in the output speed field.

          * MILES_PER_HOUR—Miles per hour

          * FEET_PER_HOUR—Feet per hour

          * KILOMETERS_PER_HOUR—Kilometers per hour

          * MILES_PER_SECOND—Miles per second

          * FEET_PER_SECOND—Feet per second

          * METERS_PER_SECOND—Meters per second

          * KNOTS—Knots
      speed_field_name {String}:
          Specifies the name of the speed field that will be added to the input feature
          class or layer. If no field name is specified, a name is automatically chosen.
      course_field_units {String}:
          Specifies the course units that will be used in the output course field.

          * DEGREES—Degrees

          * RADIANS—Radians
      course_field_name {String}:
          Specifies the name of the course field that will be added to the input feature
          class or layer. If no field name is specified, a name is automatically chosen.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output line feature class that will be created."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TrackIntervalsToLine_ta(*gp_fixargs((in_features, out_feature_class, time_field, track_id_field, time_field_format, locale_id, am_designator, pm_designator, distance_field_units, distance_field_name, duration_field_units, duration_field_name, speed_field_units, speed_field_name, course_field_units, course_field_name), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject