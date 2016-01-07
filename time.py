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
import datetime
import itertools
import locale
import re

__all__ = ['EsriTimeDelta', 'TimeZoneInfo', 'ListTimeZones',
           'ParseDateTimeString']

time_units = ["milliseconds", "seconds", "minutes", "hours",
              "days", "weeks", "months", "years", "decades",
              "centuries"]

class EsriTimeDelta(object):
    """EsriTimeDelta(interval, units)

       Creates an EsriTimeDelta object.

         interval(Double):
       The interval of the EsriTimeDelta .

         units(String):
       The units of the EsriTimeDelta . Valid units are milliseconds, seconds,
       minutes, hours, days, weeks, months, years, decades, and centuries."""
    def __init__(self, interval, units, other=None):
        """EsriTimeDelta(interval, units)

           Creates an EsriTimeDelta object.

             interval(Double):
           The interval of the EsriTimeDelta .

             units(String):
           The units of the EsriTimeDelta . Valid units are milliseconds,
           seconds, minutes, hours, days, weeks, months, years, decades, and
           centuries."""
        if not (isinstance(units, basestring) and
                units.lower() in time_units):
            raise ValueError(units)
        self.interval = interval
        self.units = units.lower()
        self.other = list(other or [])
    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__,
                                str(self))
    def __str__(self):
        stringself = "{} {}".format(self.interval, self.units)
        if self.other:
            stringself += (", " +
                           ", ".join(str(other)
                                        for other in self.other))
        return stringself
    def __neg__(self):
        return EsriTimeDelta(-self.interval,
                             self.units,
                             [-other for other in self.other]
                                    if self.other
                                    else None)
    def __add__(self, other):
        if isinstance(other, datetime.date):
            tzinfoobject = getattr(other, 'tzinfo', None)
            import arcgisscripting
            out_val = arcgisscripting._addTimeInterval(other,
                                                       self.interval,
                                                       self.units)
            if self.other:
                for other in self.other:
                    out_val += self.other
            if (not getattr(out_val, 'tzinfo', None)) and tzinfoobject:
                out_val = out_val.replace(tzinfo=tzinfoobject)
            return out_val
        elif isinstance(other, (int, float)):
            return EsriTimeDelta(self.interval + other,
                                 self.units,
                                 self.other)
        else:
            # Special case to do basic simplification of deltas
            if isinstance(other, EsriTimeDelta) and other.units == self.units:
                return EsriTimeDelta(self.interval + other.interval,
                                     self.units, (self.other or []) +_listDateTimeStringFormats
                                                 (other.other or []))
            return EsriTimeDelta(self.interval,
                                 self.units,
                                 (self.other or []) + [other])
    def __radd__(self, other):
        return self.__add__(other)
    def __sub__(self, other):
        return self + -other
    def __rsub__(self, other):
        return other + -self
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(type(other))
        return EsriTimeDelta(self.interval * other,
                             self.units,
                             self.other)
    def __rmul__(self, other):
        return self.__mul__(other)
    def __div__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(type(other))
        return EsriTimeDelta(self.interval / other,
                             self.units,
                             self.other)

class TimeZoneInfo(datetime.tzinfo):
    """TimeZoneInfo(time_zone_id)

       Creates a TimeZoneInfo object.

         time_zone_id(String):
       A valid time zone ID. A list of available time zone IDs can be obtained
       from the ListTimeZones function."""
    def __init__(self, tzid):
        """TimeZoneInfo(time_zone_id)

           Creates a TimeZoneInfo object.

             time_zone_id(String):
           A valid time zone ID. A list of available time zone IDs can be
           obtained from the ListTimeZones function."""
        super(TimeZoneInfo, self).__init__()
        import arcpy
        try:
            self._tzi = arcpy.CreateObject("TimeZoneInfo", tzid)
        except:
            raise ValueError("Invalid time zone ID.")
        self._generalinfo = self._tzi.generalInfo
        self._cache = {}
    def __repr__(self):
        return '<{}{}>'.format(self.name, '/{}'.format(self.DSTName)
                                                if self.DSTName and
                                                    self.DSTName != self.name
                                                       else '')
    def _foryear(self, year):
        assert isinstance(year, int)
        if year not in self._cache:
            if len(self._cache) > 100:
                self._cache.clear()
            self._cache[year] = self._tzi.forYear(year)
        return self._cache[year]
    @property
    def name(self):
        return self._generalinfo[0][0]
    @property
    def DSTName(self):
        return self._generalinfo[1][0]
    def _isdst(self, dt):
        ((std_start, std_bias),
         (dst_start, dst_bias)) = self._foryear(dt.year)
        if dt.tzinfo:
            std_start = std_start.replace(tzinfo=self)
            dst_start = dst_start.replace(tzinfo=self)
        if std_start == dst_start:
            return False
        elif std_start > dst_start:
            return dst_start <= dt < std_start
        else:
            return not (dst_start > dt >= std_start)
    def utcoffset(self, dt):
        """Return offset of local time from UTC, in minutes east of UTC."""
        ((std_start, std_bias),
         (dst_start, dst_bias)) = self._foryear(dt.year)
        return datetime.timedelta(minutes=std_bias)
    def dst(self, dt):
        """Return the daylight saving time (DST) adjustment, in minutes east
           of UTC, or None if DST information isn't known."""
        if self._isdst(dt):
            ((std_start, std_bias),
             (dst_start, dst_bias)) = self._foryear(dt.year)
            return datetime.timedelta(minutes=dst_bias)
        else:
            return datetime.timedelta(0)
    def tzname(self, dt):
        """TimeZoneInfo.tzname(dt)

           Returns the time zone name corresponding to the
           Python datetime
            object, dt, as a string.

             dt(DateTime):
           A reference to a Python datetime object."""
        if self._isdst(dt):
            return self.DSTName
        return self.name

def ListTimeZones():
    """ListTimeZones()

       Lists valid Time Zone IDs."""
    import arcgisscripting
    return arcgisscripting._listTimeZones()

# Map Microsoft date/time string format windows to be strptime-compatible
unit_map = {
        u'D': u"%d",
        u'Dd': u"%d",
        u'Ddd': u"%a",
        u'Dddd': u"%A",
        u'd': u"%d",
        u'dd': u"%d",
        u'ddd': u"%a",
        u'dddd': u"%A",
        u'M': u"%m",
        u'MM': u"%m",
        u'MMM': u"%b",
        u'MMMM': u"%B",
        u'y': u"%y",
        u'yy': u"%y",
        u'yyyy': u"%Y",
        u'h': u"%I",
        u'hh': u"%I",
        u'H': u"%H",
        u'HH': u"%H",
        u'm': u"%M",
        u'mm': u"%M",
        u's': u"%S",
        u'ss': u"%S",
        u't': u"%p",
        u'tt': u"%p"
}

unitpattern = re.compile(u"({})".format(u"|".join(
                                                reversed(
                                                    sorted(unit_map)))))

def FixDTString(dtstring):
    """FixDTString(dtstring)

       Rewrites a VBScript-style yyyy/mm/dd datetime format string
       into a strftime-compatible %Y-%M-%d type string"""
    new_string = u''
    patterns = unitpattern.findall(dtstring)
    for pattern in patterns:
        new_string += dtstring[:dtstring.find(pattern)]
        new_string += unit_map.get(pattern, pattern)
        dtstring = dtstring[dtstring.find(pattern) + len(pattern):]
    return new_string + dtstring

if locale.getlocale() == (None, None):
    locale.setlocale(locale.LC_ALL, '')

import arcgisscripting
ms_date_formats, ms_time_formats = arcgisscripting._listDateTimeStringFormats()
del arcgisscripting

python_date_formats = map(FixDTString, ms_date_formats) + [u'', u'%x']
python_time_formats = map(FixDTString, ms_time_formats) + [u'', u'%X']

def crossproduct(*args):
    if args:
        for item in args[0]:
            for subitem in crossproduct(*args[1:]):
                yield [item] + list(subitem)
    else:
        yield []

py_datetime_string_formats = [u' '.join(filter(bool, k))
                                    for k in itertools.chain(*([[u'%c']],
                                             crossproduct(python_date_formats,
                                                          python_time_formats))
                                                            )
                                    if any(k)
                             ]

def ParseDateTimeString(datetime_string):
    """ParseDateTimeString(dtstring)

       Try really hard to parse a string into a DateTime object"""
    parsed_dts = []
    for timestrf in py_datetime_string_formats:
        try:
            parsed_dts.append(
                    datetime.datetime.strptime(datetime_string,
                                               timestrf))
        except:
            pass
    if not parsed_dts:
        raise ValueError(datetime_string)
    elif len(parsed_dts) == 1:
        return parsed_dts[0]
    else:
        now = datetime.datetime.now()
        return min(parsed_dts, key=lambda x: abs(now - x))

def FormatDate(datetime_object, format_string):
    """FormatDate(datetime_object, format_string)

       Reformats a datetime object using a VBScript-style format
           string such as yyyy/mm/dd hh:mm"""
    if isinstance(datetime_object, basestring):
        datetime_object = ParseDateTimeString(datetime_object)
    return datetime_object.strftime(FixDTString(format_string))
