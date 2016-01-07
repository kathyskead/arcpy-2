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
import datetime
try:
    from . import CompoundParameter
    from . import Utils
except:
    import CompoundParameter
    import Utils


__all__ = [
    "FuzzyGaussian",
    "FuzzyLarge",
    "FuzzyLinear",
    "FuzzyMSLarge",
    "FuzzyMSSmall",
    "FuzzyNear",
    "FuzzySmall",
    "HfBinary",
    "HfForward",
    "HfInverseLinear",
    "HfLinear",
    "HfTable",
    "KrigingModelOrdinary",
    "KrigingModelUniversal",
    "NbrAnnulus",
    "NbrCircle",
    "NbrIrregular",
    "NbrRectangle",
    "NbrWedge",
    "NbrWeight",
    "RadiusFixed",
    "RadiusVariable",
    "RemapRange",
    "RemapValue",
    "TimeMultipleDays",
    "TimeSpecialDays",
    "TimeWholeYear",
    "TimeWithinDay",
    "TopoBoundary",
    "TopoCliff",
    "TopoCoast",
    "TopoContour",
    "TopoExclusion",
    "TopoLake",
    "TopoPointElevation",
    "TopoSink",
    "TopoStream",
    "TfExponential",
    "TfGaussian",
    "TfLarge",
    "TfLinear",
    "TfLogarithm",
    "TfLogisticDecay",
    "TfLogisticGrowth",
    "TfMSLarge",
    "TfMSSmall",
    "TfNear",
    "TfPower",
    "TfSmall",
    "TfSymmetricLinear",
    "VfBinary",
    "VfCos",
    "VfCosSec",
    "VfInverseLinear",
    "VfLinear",
    "VfSec",
    "VfSecCos",
    "VfSymInverseLinear",
    "VfSymLinear",
    "VfTable",
    "WOTable",
    "WSTable"
]


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _FuzzyMembership(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class FuzzyGaussian(_FuzzyMembership):
    """
    FuzzyGaussian(midpoint, spread)

    Spatial Analyst (ArcPy) class that defines a FuzzyGaussian membership object.

    Arguments:
    midpoint -- The user-defined value with a fuzzy membership of 1.
    spread -- Defines the spread of the Gaussian function. The spread generally ranges from 0.01 to 1, with the larger the value results in a steeper distribution around the midpoint.

    Results:
    A FuzzyGaussian membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None):
        _FuzzyMembership.__init__(self, "GAUSSIAN")
        self.midpoint = midpoint
        self.spread = spread

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread])

FuzzyGaussian._addProperty("midpoint")
FuzzyGaussian._addProperty("spread", 0.1)


class FuzzyLarge(_FuzzyMembership):
    """
    FuzzyLarge(midpoint, spread)

    Spatial Analyst (ArcPy) class that defines a FuzzyLarge membership object.

    Arguments:
    midpoint -- The user-defined value with a fuzzy membership of 0.5.
    spread -- Defines the spread of the Large function. The spread generally ranges from 1 to 10, with the larger the value results in a steeper distribution from the midpoint.

    Results:
    A FuzzyLarge membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None):
        _FuzzyMembership.__init__(self, "LARGE")
        self.midpoint = midpoint
        self.spread = spread

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread])

FuzzyLarge._addProperty("midpoint")
FuzzyLarge._addProperty("spread", 5.0)


class FuzzyLinear(_FuzzyMembership):
    """
    FuzzyLinear(minimum, maximum)

    Spatial Analyst (ArcPy) class that defines a FuzzyLinear membership object.

    Arguments:
    minimum -- The value that will have a membership of 0. If the minimum value is less than the maximum , the linear function will have a positive slope. If the minimum value is greater than the maximum , the linear function will have a negative slope.
    maximum -- The value that will have a membership of 1. If the maximum value is greater than the minimum , the linear function will have a positive slope. If the maximum value is less than the minimum , the linear function will have a negative slope.

    Results:
    A FuzzyLinear membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            minimum=None,
            maximum=None):
        _FuzzyMembership.__init__(self, "LINEAR")
        self.minimum = minimum
        self.maximum = maximum

    def __str__(self):
        return self._toString([
            self._keyword,
            self.minimum,
            self.maximum])

    def __repr__(self):
        return self._toRepresentation([
            self.minimum,
            self.maximum])

FuzzyLinear._addProperty("minimum")
FuzzyLinear._addProperty("maximum")


class FuzzyMSLarge(_FuzzyMembership):
    """
    FuzzyMSLarge(meanMultiplier, STDMultiplier)

    Spatial Analyst (ArcPy) class that defines a FuzzyMSLarge membership object.

    Arguments:
    meanMultiplier -- The multiplier for the mean of the input values in the MSLarge function equation.
    STDMultiplier -- The multiplier for the standard deviation of the input values in the MSLarge function equation.

    Results:
    A FuzzyMSLarge membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            meanMultiplier=None,
            STDMultiplier=None):
        _FuzzyMembership.__init__(self, "MSLARGE")
        self.meanMultiplier = meanMultiplier
        self.STDMultiplier = STDMultiplier

    def __str__(self):
        return self._toString([
            self._keyword,
            self.meanMultiplier,
            self.STDMultiplier])

    def __repr__(self):
        return self._toRepresentation([
            self.meanMultiplier,
            self.STDMultiplier])

FuzzyMSLarge._addProperty("meanMultiplier", 1.0)
FuzzyMSLarge._addProperty("STDMultiplier", 1.0)


class FuzzyMSSmall(_FuzzyMembership):
    """
    FuzzyMSSmall(meanMultiplier, STDMultiplier)

    Spatial Analyst (ArcPy) class that defines a FuzzyMSSmall membership object.

    Arguments:
    meanMultiplier -- The multiplier for the mean of the input values in the MSLarge function equation.
    STDMultiplier -- The multiplier for the standard deviation of the input values in the MSLarge function equation.

    Results:
    A FuzzyMSSmall membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            meanMultiplier=None,
            STDMultiplier=None):
        _FuzzyMembership.__init__(self, "MSSMALL")
        self.meanMultiplier = meanMultiplier
        self.STDMultiplier = STDMultiplier

    def __str__(self):
        return self._toString([
            self._keyword,
            self.meanMultiplier,
            self.STDMultiplier])

    def __repr__(self):
        return self._toRepresentation([
            self.meanMultiplier,
            self.STDMultiplier])

FuzzyMSSmall._addProperty("meanMultiplier", 1.0)
FuzzyMSSmall._addProperty("STDMultiplier", 1.0)


class FuzzyNear(_FuzzyMembership):
    """
    FuzzyNear(midpoint, spread)

    Spatial Analyst (ArcPy) class that defines a FuzzyNear membership object.

    Arguments:
    midpoint -- The user-defined value with a fuzzy membership of 1.
    spread -- Defines the spread of the Near function. The spread generally ranges from 0.001 to 1 with the larger the value results in a steeper distribution from the midpoint.

    Results:
    A FuzzyNear membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None):
        _FuzzyMembership.__init__(self, "NEAR")
        self.midpoint = midpoint
        self.spread = spread

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread])

FuzzyNear._addProperty("midpoint")
FuzzyNear._addProperty("spread", 0.1)


class FuzzySmall(_FuzzyMembership):
    """
    FuzzySmall(midpoint, spread)

    Spatial Analyst (ArcPy) class that defines a FuzzySmall membership object.

    Arguments:
    midpoint -- The user-defined value with a fuzzy membership of 0.5.
    spread -- Defines the spread of the Small function. The spread generally ranges from 1 to 10, with the larger the value results in a steeper distribution from the midpoint.

    Results:
    A FuzzySmall membership object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None):
        _FuzzyMembership.__init__(self, "SMALL")
        self.midpoint = midpoint
        self.spread = spread

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread])

FuzzySmall._addProperty("midpoint")
FuzzySmall._addProperty("spread", 5.0)


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _HorizontalFactor(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class HfBinary(_HorizontalFactor):
    """
    HfBinary({zeroFactor}, {cutAngle})

    Spatial Analyst (ArcPy) class that defines a binary horizontal factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the binary function.
    cutAngle -- The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity.

    Results:
    An HfBinary horizontal factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            cutAngle=None):
        _HorizontalFactor.__init__(self, "BINARY")
        self.zeroFactor = zeroFactor
        self.cutAngle = cutAngle

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.cutAngle])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.cutAngle])

HfBinary._addProperty("zeroFactor", 1.0)
HfBinary._addProperty("cutAngle", 45.0)


class HfForward(_HorizontalFactor):
    """
    HfForward({zeroFactor}, {sideValue})

    Spatial Analyst (ArcPy) class that defines a forward horizontal factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the forward function.
    sideValue -- Identifies the HF value that will be assigned for HRMAs that are equal to or less than 45 degrees and less than 90 degrees. In the diagram above, the sideValue is assigned 1.

    Results:
    An HfForward horizontal factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            sideValue=None):
        _HorizontalFactor.__init__(self, "FORWARD")
        self.zeroFactor = zeroFactor
        self.sideValue = sideValue

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.sideValue])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.sideValue])

HfForward._addProperty("zeroFactor", 0.5)
HfForward._addProperty("sideValue", 1.0)


class HfLinear(_HorizontalFactor):
    """
    HfLinear({zeroFactor}, {cutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines a linear horizontal factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the linear function.
    cutAngle -- The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity.
    slope -- Identifies the slope of the straight line in the HRMA-HF coordinate system. Slope is specified as the rise over the run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 HF on the y axis / 30 degrees on the x axis).

    Results:
    An HfLinear horizontal factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            cutAngle=None,
            slope=None):
        _HorizontalFactor.__init__(self, "LINEAR")
        self.zeroFactor = zeroFactor
        self.cutAngle = cutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.cutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.cutAngle,
            self.slope])

HfLinear._addProperty("zeroFactor", 0.5)
HfLinear._addProperty("cutAngle", 181.0)
HfLinear._addProperty("slope", 0.011111)


class HfInverseLinear(_HorizontalFactor):
    """
    HfInverseLinear({zeroFactor}, {cutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines an inverse linear horizontal factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the inverse linear function.
    cutAngle -- The cutAngle establishes the HRMA degree threshold beyond which the HFs are set to infinity.
    slope -- Identifies the slope of the straight line in the HRMA-HF coordinate system. Slope is specified as the rise over the run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 HF on the y axis / 30 degrees on the x axis).

    Results:
    An HfBinary horizontal factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            cutAngle=None,
            slope=None):
        _HorizontalFactor.__init__(self, "INVERSE_LINEAR")
        self.zeroFactor = zeroFactor
        self.cutAngle = cutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.cutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.cutAngle,
            self.slope])

HfInverseLinear._addProperty("zeroFactor", 2.0)
HfInverseLinear._addProperty("cutAngle", 180.0)
HfInverseLinear._addProperty("slope", -0.011111)


class HfTable(_HorizontalFactor):
    """
    HfTable(inTable)

    Spatial Analyst (ArcPy) class that defines a table horizontal factor object.

    Arguments:
    inTable -- The inTable is an ASCII file with two columns on each line. The first column identifies the HRMA in degrees, and the second, the HF. Each line specifies a point. Two consecutive points produce a line segment in the HRMA-HF coordinate system. The angles must be input in ascending order. The HF factor for any HRMA angle less than the first (lowest) input value or larger than the last (largest) input value will be set to infinity. An infinite HF is represented by -1 in the ASCII file.

    Results:
    An HfTable horizontal factor object is returned.
    """

    __esri_toolinfo__ = [
        "File:::",
    ]

    def __init__(self,
            inTable):
        _HorizontalFactor.__init__(self, "TABLE")
        self.inTable = CompoundParameter._DataSetName(inTable)

    def __str__(self):
        return self._toString([
            self._keyword,
            self.inTable])

    def __repr__(self):
        return self._toRepresentation([
            self.inTable])

HfTable._addProperty("inTable")


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _KrigingModel(CompoundParameter._CompoundParameter):

    def __init__(self):
        CompoundParameter._CompoundParameter.__init__(self)


class KrigingModelOrdinary(_KrigingModel):
    """
    KrigingModelOrdinary({semivariogramType}, {lagSize}, {majorRange}, {partialSill}, {nugget})

    Spatial Analyst (ArcPy) class that defines a KrigingModelOrdinary object.

    Arguments:
    semivariogramType -- Semivariogram model to be used.
    lagSize -- The lag size to be used in model creation. The default is the output raster cell size.
    majorRange -- Represents a distance beyond which there is little or no correlation.
    partialSill -- The difference between the nugget and the sill.
    nugget -- Represents the error and variation at spatial scales too fine to detect. The nugget effect is seen as a discontinuity at the origin.

    Results:
    A KrigingModelOrdinary object is returned.
    """

    __esri_toolinfo__ = [
        "String::SPHERICAL|CIRCULAR|EXPONENTIAL|GAUSSIAN|LINEAR:",
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            semivariogramType=None,
            lagSize=None,
            majorRange=None,
            partialSill=None,
            nugget=None):
        _KrigingModel.__init__(self)
        self.semivariogramType = semivariogramType
        self.lagSize = lagSize
        self.majorRange = majorRange
        self.partialSill = partialSill
        self.nugget = nugget

    def __str__(self):
        return self._toString([
            self.semivariogramType,
            self.lagSize,
            self.majorRange,
            self.partialSill,
            self.nugget])

    def __repr__(self):
        return self._toRepresentation([
            self.semivariogramType,
            self.lagSize,
            self.majorRange,
            self.partialSill,
            self.nugget])

KrigingModelOrdinary._addProperty("semivariogramType", "SPHERICAL")
KrigingModelOrdinary._addProperty("lagSize")
KrigingModelOrdinary._addProperty("majorRange")
KrigingModelOrdinary._addProperty("partialSill")
KrigingModelOrdinary._addProperty("nugget")


class KrigingModelUniversal(_KrigingModel):
    """
    KrigingModelUniversal({semivariogramType}, {lagSize}, {majorRange}, {partialSill}, {nugget})

    Spatial Analyst (ArcPy) class that defines a KrigingModelUniversal object.

    Arguments:
    semivariogramType -- Semivariogram model to be used.
    lagSize -- The lag size to be used in model creation. The default is the output raster cell size.
    majorRange -- Represents a distance beyond which there is little or no correlation.
    partialSill -- The difference between the nugget and the sill.
    nugget -- Represents the error and variation at spatial scales too fine to detect. The nugget effect is seen as a discontinuity at the origin.

    Results:
    A KrigingModelUniversal object is returned.
    """

    __esri_toolinfo__ = [
        "String::LINEARDRIFT|QUADRATICDRIFT:",
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            semivariogramType=None,
            lagSize=None,
            majorRange=None,
            partialSill=None,
            nugget=None):
        _KrigingModel.__init__(self)
        self.semivariogramType = semivariogramType
        self.lagSize = lagSize
        self.majorRange = majorRange
        self.partialSill = partialSill
        self.nugget = nugget

    def __str__(self):
        return self._toString([
            self.semivariogramType,
            self.lagSize,
            self.majorRange,
            self.partialSill,
            self.nugget])

    def __repr__(self):
        return self._toRepresentation([
            self.semivariogramType,
            self.lagSize,
            self.majorRange,
            self.partialSill,
            self.nugget])

KrigingModelUniversal._addProperty("semivariogramType", "LINEARDRIFT")
KrigingModelUniversal._addProperty("lagSize")
KrigingModelUniversal._addProperty("majorRange")
KrigingModelUniversal._addProperty("partialSill")
KrigingModelUniversal._addProperty("nugget")


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _Neighborhood(CompoundParameter._CompoundParameter):
    """Base class for specialized neighborhood classes."""

    def __init__(self,
            keyword):
        """Creates a _Neighborhood object.

        keyword -- Keyword associated with the neighborhood.
        """
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class NbrAnnulus(_Neighborhood):
    """
    NbrAnnulus({innerRadius}, {outerRadius}, {units})

    Spatial Analyst (ArcPy) class that defines an annulus or donut-shaped neighborhood object.

    Arguments:
    innerRadius -- The inner radius of an annulus neighborhood.
    outerRadius -- The outer radius of an annulus neighborhood.
    units -- Defines the units of the neighborhood.

    Results:
    A NbrAnnulus neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "String::CELL|MAP:",
    ]

    def __init__(self,
            innerRadius=None,
            outerRadius=None,
            units=None):
        _Neighborhood.__init__(self, "ANNULUS")
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.units = units

    def __str__(self):
        return self._toString([
            self._keyword,
            self.innerRadius,
            self.outerRadius,
            self.units])

    def __repr__(self):
        return self._toRepresentation([
            self.innerRadius,
            self.outerRadius,
            self.units])

NbrAnnulus._addProperty("innerRadius", 1.0)
NbrAnnulus._addProperty("outerRadius", 3.0)
NbrAnnulus._addProperty("units", "CELL")


class NbrCircle(_Neighborhood):
    """
    NbrCircle({radius}, {units})

    Spatial Analyst (ArcPy) class that defines a circular-shaped neighborhood object.

    Arguments:
    radius -- The radius of the circle neighborhood.
    units -- Defines the units of the neighborhood.

    Results:
    A NbrCircle neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "String::CELL|MAP:",
    ]

    def __init__(self,
            radius=None,
            units=None):
        _Neighborhood.__init__(self, "CIRCLE")
        self.radius = radius
        self.units = units

    def __str__(self):
        return self._toString([
            self._keyword,
            self.radius,
            self.units])

    def __repr__(self):
        return self._toRepresentation([
            self.radius,
            self.units])

NbrCircle._addProperty("radius", 3.0)
NbrCircle._addProperty("units", "CELL")


class NbrIrregular(_Neighborhood):
    """
    NbrIrregular(inKernelFile)

    Spatial Analyst (ArcPy) class that defines an irregular neighborhood object.

    Arguments:
    inKernelFile -- The irregular inKernelFile is an ASCII text file that defines the shape of an irregular neighborhood. A value of 0 for a cell position indicates that the cell is not a member of the neighborhood, and a nonzero number at a corresponding cell's position indicates that the cell value be included as a member of the neighborhood.

    Results:
    A NbrIrregular neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "File:::",
    ]

    def __init__(self,
            inKernelFile):
        _Neighborhood.__init__(self, "IRREGULAR")
        self.inKernelFile = CompoundParameter._DataSetName(inKernelFile)

    def __str__(self):
        return self._toString([
            self._keyword,
            self.inKernelFile])

    def __repr__(self):
        return self._toRepresentation([
            self.inKernelFile])

NbrIrregular._addProperty("inKernelFile")


class NbrRectangle(_Neighborhood):
    """
    NbrRectangle({width}, {height}, {units})

    Spatial Analyst (ArcPy) class that defines a rectangular-shaped neighborhood object.

    Arguments:
    width -- The width of the rectangle neighborhood.
    height -- The height of the rectangle neighborhood.
    units -- Defines the units of the neighborhood.

    Results:
    A NbrRectangle neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "String::CELL|MAP:",
    ]

    def __init__(self,
            width=None,
            height=None,
            units=None):
        _Neighborhood.__init__(self, "RECTANGLE")
        self.width = width
        self.height = height
        self.units = units

    def __str__(self):
        return self._toString([
            self._keyword,
            self.width,
            self.height,
            self.units])

    def __repr__(self):
        return self._toRepresentation([
            self.width,
            self.height,
            self.units])

NbrRectangle._addProperty("width", 3.0)
NbrRectangle._addProperty("height", 3.0)
NbrRectangle._addProperty("units", "CELL")


class NbrWedge(_Neighborhood):
    """
    NbrWedge({radius}, {startAngle}, {endAngle}, {units})

    Spatial Analyst (ArcPy) class that defines a wedge or pie-shaped neighborhood object.

    Arguments:
    radius -- The radius is the distance from the corner of the wedge to the outer limit of the wedge. The radius is an integer or floating-point value.
    startAngle -- The startAngle is an integer or floating-point value from 0 to 360.
    endAngle -- The endAngle is an integer or floating-point value from 0 to 360.
    units -- Defines the units of the neighborhood.

    Results:
    A NbrWedge neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "String::CELL|MAP:",
    ]

    def __init__(self,
            radius=None,
            startAngle=None,
            endAngle=None,
            units=None):
        _Neighborhood.__init__(self, "WEDGE")
        self.radius = radius
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.units = units

    def __str__(self):
        return self._toString([
            self._keyword,
            self.radius,
            self.startAngle,
            self.endAngle,
            self.units])

    def __repr__(self):
        return self._toRepresentation([
            self.radius,
            self.startAngle,
            self.endAngle,
            self.units])

NbrWedge._addProperty("radius", 3.0)
NbrWedge._addProperty("startAngle", 0.0)
NbrWedge._addProperty("endAngle", 90.0)
NbrWedge._addProperty("units", "CELL")


class NbrWeight(_Neighborhood):
    """
    NbrWeight(inKernelFile)

    Spatial Analyst (ArcPy) class that defines a weighted table neighborhood object.

    Arguments:
    inKernelFile -- The inKernelFile is an ASCII text file that defines the shape of the neighborhood and the weight of each cell in that neighborhood. A value of 0 for a cell position indicates that the cell is not a member of the neighborhood, and a number at a corresponding cell's position indicates that the cell value be included as a member of the neighborhood. The nonzero value will also serve as the weight to multiply the corresponding cell value.

    Results:
    A NbrWeight neighborhood object is returned.
    """

    __esri_toolinfo__ = [
        "File:::",
    ]

    def __init__(self,
            inKernelFile):
        _Neighborhood.__init__(self, "WEIGHT")
        self.inKernelFile = inKernelFile

    def __str__(self):
        return self._toString([
            self._keyword,
            self.inKernelFile])

    def __repr__(self):
        return self._toRepresentation([
            self.inKernelFile])

NbrWeight._addProperty("inKernelFile")


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _Radius(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class RadiusVariable(_Radius):
    """
    RadiusVariable({numberOfPoints}, {maxDistance})

    Spatial Analyst (ArcPy) class that defines a variable radius object.

    Arguments:
    numberOfPoints -- The numberOfPoints is an integer value specifying the number of nearest input samplepoints to be used to perform the interpolation.
    maxDistance -- The maxDistance specifies the distance, in map units, by which to limit the search for the nearest input sample points. The default value is the length of the extent's diagonal.

    Results:
    A RadiusVariable object is returned.
    """

    __esri_toolinfo__ = [
        "Long:::",
        "Double:::",
    ]

    def __init__(self,
            numberOfPoints=None,
            maxDistance=None):
        _Radius.__init__(self, "VARIABLE")
        self.numberOfPoints = numberOfPoints
        self.maxDistance = maxDistance

    def __str__(self):
        return self._toString([
            self._keyword,
            self.numberOfPoints,
            self.maxDistance])

    def __repr__(self):
        return self._toRepresentation([
            self.numberOfPoints,
            self.maxDistance])

RadiusVariable._addProperty("numberOfPoints", 12)
RadiusVariable._addProperty("maxDistance")


class RadiusFixed(_Radius):
    """
    RadiusFixed({distance}, {minNumberOfPoints})

    Spatial Analyst (ArcPy) class that defines a fixed radius object.

    Arguments:
    distance -- The distance specifies the distance as a radius within which input sample points will be used to perform the interpolation. The value of the radius is expressed in map units. The default radius is five times the cell size of the output raster.
    minNumberOfPoints -- The minNumberOfPoints is an integer defining the minimum number of points to be used to perform theinterpolation.

    Results:
    A RadiusFixed object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Long:::",
    ]

    def __init__(self,
            distance=None,
            minNumberOfPoints=None):
        _Radius.__init__(self, "FIXED")
        self.distance = distance
        self.minNumberOfPoints = minNumberOfPoints

    def __str__(self):
        return self._toString([
            self._keyword,
            self.distance,
            self.minNumberOfPoints])

    def __repr__(self):
        return self._toRepresentation([
            self.distance,
            self.minNumberOfPoints])

RadiusFixed._addProperty("distance")
RadiusFixed._addProperty("minNumberOfPoints", 0)


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _Remap(CompoundParameter._CompoundParameter):

    def __init__(self,
            remapTable):
        CompoundParameter._CompoundParameter.__init__(self)
        self.remapTable = [list(record) for record in remapTable]

    def __repr__(self):
        return self._toRepresentation([self.remapTable])

    def __str__(self):
        return "; ".join(map(lambda record:
            " ".join([str(item) for item in record]), self.remapTable))

_Remap._addProperty("remapTable")


class RemapRange(_Remap):
    """
    RemapRange([[startValue, endValue, newValue],...])

    Spatial Analyst (ArcPy) class that defines a remap by range table object.

    Arguments:
    remapTable -- The remap table to be used to remap the old values (specified by ranges) to new values.

    Results:
    A remap by range table object is returned.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            remapTable):
        _Remap.__init__(self, remapTable)


class RemapValue(_Remap):
    """
    RemapValue([[oldValue, newValue],...])

    Spatial Analyst (ArcPy) class that defines a remap by value table object.

    Arguments:
    remapTable -- The remap table to be used to remap the old values to new values.

    Results:
    A remap by value table object is returned.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            remapTable):
        _Remap.__init__(self, remapTable)


import datetime
try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _Time(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class TimeWithinDay(_Time):
    """
    TimeWithinDay({day}, {startTime}, {endTime})

    Spatial Analyst (ArcPy) class that defines a time within day object.

    Arguments:
    day -- The day is a Julian day value from 1 to 365.
    startTime -- The startTime is the first hour to be used in the analysis. The hour is represented with a number from 0 to 24.
    endTime -- The endTime is the last hour to be used in the analysis. The hour is represented with a number from 0 to 24.

    Results:
    A time within day object is returned.
    """

    __esri_toolinfo__ = [
        "Long:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            day=None,
            startTime=None,
            endTime=None):
        _Time.__init__(self, "WITHINDAY")
        self.day = day
        self.startTime = startTime
        self.endTime = endTime

    def __str__(self):
        return self._toString([
            self._keyword,
            self.day,
            self.startTime,
            self.endTime])

    def __repr__(self):
        return self._toRepresentation([
            self.day,
            self.startTime,
            self.endTime])

TimeWithinDay._addProperty("day", 183)
TimeWithinDay._addProperty("startTime", 0.0)
TimeWithinDay._addProperty("endTime", 24.0)


class TimeSpecialDays(_Time):
    """
    TimeSpecialDays()

    Spatial Analyst (ArcPy) class that defines a time special days object.

    Results:
    """

    __esri_toolinfo__ = [
        
    ]

    def __init__(self):
        _Time.__init__(self, "SPECIALDAYS")

    def __str__(self):
        return self._toString([
            self._keyword])

    def __repr__(self):
        return self._toRepresentation([])


class TimeMultipleDays(_Time):
    """
    TimeMultipleDays({year}, {startDay}, {endDay})

    Spatial Analyst (ArcPy) class that defines a time multiple days object.

    Arguments:
    year -- The Julian year.
    startDay -- The startDay is the first Julian day in the analysis.
    endDay -- The endDay is the last Julian day in the analysis.

    Results:
    A time multiple days object is returned.
    """

    __esri_toolinfo__ = [
        "Long:::",
        "Long:::",
        "Long:::",
    ]

    def __init__(self,
            year=None,
            startDay=None,
            endDay=None):
        _Time.__init__(self, "MULTIDAYS")
        self.year = year
        self.startDay = startDay
        self.endDay = endDay

    def __str__(self):
        return self._toString([
            self._keyword,
            self.year,
            self.startDay,
            self.endDay])

    def __repr__(self):
        return self._toRepresentation([
            self.year,
            self.startDay,
            self.endDay])

TimeMultipleDays._addProperty("year", datetime.date.today().year)
TimeMultipleDays._addProperty("startDay", 5)
TimeMultipleDays._addProperty("endDay", 160)


class TimeWholeYear(_Time):
    """
    TimeWholeYear({year})

    Spatial Analyst (ArcPy) class that defines a time whole year object.

    Arguments:
    year -- The Julian year.

    Results:
    A time whole year object is returned.
    """

    __esri_toolinfo__ = [
        "Long:::",
    ]

    def __init__(self,
            year=None):
        _Time.__init__(self, "WHOLEYEAR")
        self.year = year

    def __str__(self):
        return self._toString([
            self._keyword,
            self.year])

    def __repr__(self):
        return self._toRepresentation([
            self.year])

TimeWholeYear._addProperty("year", datetime.date.today().year)


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _TopoInput(object):
    pass


class _TopoInputNestedList(_TopoInput, CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword,
            inFeatures):
        _TopoInput.__init__(self)
        CompoundParameter._CompoundParameter.__init__(self,
            keyword=keyword)
        assert self._keyword

        self.inFeatures = [list(record) for record in inFeatures]

    def __str__(self):
        return "; ".join(map(lambda record:
            " ".join(["'{0}'".format(str(record[0]))] +
                [str(item) for item in record[1:] + [self._keyword]]),
            self.inFeatures))

    def __repr__(self):
        return self._toRepresentation([self.inFeatures])

_TopoInputNestedList._addProperty("inFeatures")


class _TopoInputList(_TopoInput, CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword,
            inFeatures):
        _TopoInput.__init__(self)
        CompoundParameter._CompoundParameter.__init__(self,
            keyword=keyword)
        assert self._keyword

        self.inFeatures = list(inFeatures)

    def __str__(self):
        return "; ".join(["'%s' # %s" % (str(item), self._keyword) for item in
            self.inFeatures])

    def __repr__(self):
        return self._toRepresentation([self.inFeatures])

_TopoInputList._addProperty("inFeatures")


class TopoPointElevation(_TopoInputNestedList):
    """
    TopoPointElevation([[inFeature, {field}],...])

    Spatial Analyst (ArcPy) class that defines a topo point elevation object.

    Arguments:
    inFeatures -- The input point feature datasets.

    Results:
    A topo point elevation object is returned.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputNestedList.__init__(self, "POINTELEVATION", inFeatures)


class TopoContour(_TopoInputNestedList):
    """
    TopoContour([[inFeature, {field}],...])

    Spatial Analyst (ArcPy) class that defines a topo contour object.

    Arguments:
    inFeatures -- The input line feature datasets.

    Results:
    A topo contour object is returned.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputNestedList.__init__(self, "CONTOUR", inFeatures)


class TopoStream(_TopoInputList):
    """
    TopoStream([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo stream object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo stream object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "STREAM", inFeatures)


class TopoSink(_TopoInputNestedList):
    """
    TopoSink([[inFeature, {field}],...])

    Spatial Analyst (ArcPy) class that defines a topo sink object.

    Arguments:
    inFeatures -- The input point feature datasets.

    Results:
    A topo sink object is returned.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputNestedList.__init__(self, "SINK", inFeatures)


class TopoBoundary(_TopoInputList):
    """
    TopoBoundary([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo boundary object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo boundary object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "BOUNDARY", inFeatures)


class TopoLake(_TopoInputList):
    """
    TopoLake([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo lake object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo lake object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "LAKE", inFeatures)


class TopoCliff(_TopoInputList):
    """
    TopoCliff([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo cliff object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo cliff object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "CLIFF", inFeatures)


class TopoCoast(_TopoInputList):
    """
    TopoCoast([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo coast object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo boundary object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "COAST", inFeatures)


class TopoExclusion(_TopoInputList):
    """
    TopoExclusion([inFeature,...])

    Spatial Analyst (ArcPy) class that defines a topo exclusion object.

    Arguments:
    inFeatures -- The input feature datasets.

    Results:
    A topo exclusion object is returned.
    """

    __esri_toolinfo__ = [
        "String:::",
    ]

    def __init__(self,
            inFeatures):
        _TopoInputList.__init__(self, "EXCLUSION", inFeatures)


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _TransformationFunction(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class TfGaussian(_TransformationFunction):
    """
    TfGaussian({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Gaussian function object.

    Arguments:
    midpoint -- The user-defined value that defines the highest point of the Gaussian transformation function curve. If the midpoint value is between the lower and upper threshold, input cell locations with the corresponding value will receive the toScale evaluation scale value on the output raster.
    spread -- Defines the spread of the Gaussian functionthat controls the steepness of the decay of the function from themidpoint. The spread generally ranges from 0.01 to 1; thelarger the value results in a steeper decay from themidpoint.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Gaussian object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "GAUSSIAN")
        self.midpoint = midpoint
        self.spread = spread
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfGaussian._addProperty("midpoint")
TfGaussian._addProperty("spread")
TfGaussian._addProperty("lowerThreshold")
TfGaussian._addProperty("valueBelowThreshold")
TfGaussian._addProperty("upperThreshold")
TfGaussian._addProperty("valueAboveThreshold")


class TfNear(_TransformationFunction):
    """
    TfNear({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Near function object.

    Arguments:
    midpoint -- The user-defined value that defines the highest point of the Near transformation function curve. If the midpoint value is between the lower and upper threshold, input cell locations with the corresponding value will receive the toScale evaluation scale value on the output raster.
    spread -- Defines the spread of the Near functionthat controls the steepness of the decay of the function from themidpoint. The spread generally ranges from 0.001 to 1;the larger the value results in a steeper decay from themidpoint.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Near object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "NEAR")
        self.midpoint = midpoint
        self.spread = spread
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfNear._addProperty("midpoint")
TfNear._addProperty("spread")
TfNear._addProperty("lowerThreshold")
TfNear._addProperty("valueBelowThreshold")
TfNear._addProperty("upperThreshold")
TfNear._addProperty("valueAboveThreshold")


class TfLarge(_TransformationFunction):
    """
    TfLarge({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Large function object.

    Arguments:
    midpoint -- Defines the transition point of the transformation function where the curve becomes more convex for the values lesser than the midpoint and more concave for values greater than the midpoint. Shifting the midpoint less than the midpoint of the input data alters the transition point, resulting in an increase in the range of the larger values above the midpoint being more preferred, with the preference increasing at a faster rate.
    spread -- Defines the spread of the Large transformationfunction that controls how quickly the function values increase and decrease from themidpoint. The spread generally ranges from 1 to 10; thelarger the value results in a steeper distribution around themidpoint.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Large object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "LARGE")
        self.midpoint = midpoint
        self.spread = spread
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfLarge._addProperty("midpoint")
TfLarge._addProperty("spread", 5.0)
TfLarge._addProperty("lowerThreshold")
TfLarge._addProperty("valueBelowThreshold")
TfLarge._addProperty("upperThreshold")
TfLarge._addProperty("valueAboveThreshold")


class TfSmall(_TransformationFunction):
    """
    TfSmall({midpoint}, {spread}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Small function object.

    Arguments:
    midpoint -- Defines the transition point of the transformation function where the curve becomes more concave for the values lesser than the midpoint and more convex for values greater than the midpoint. Shifting the midpoint greater than the midpoint of the input data alters the transition point, resulting in an increase in the range of the smaller values below the midpoint being more preferred, with the preference increasing at a slower rate.
    spread -- Defines the spread of the Small transformation functionthat controlshow quickly the function values increase and decrease from themidpoint. The spread generally ranges from 1 to 10; thelarger the value results in a steeper distribution aroundthe midpoint.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Small object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            midpoint=None,
            spread=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "SMALL")
        self.midpoint = midpoint
        self.spread = spread
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.midpoint,
            self.spread,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfSmall._addProperty("midpoint")
TfSmall._addProperty("spread", 5.0)
TfSmall._addProperty("lowerThreshold")
TfSmall._addProperty("valueBelowThreshold")
TfSmall._addProperty("upperThreshold")
TfSmall._addProperty("valueAboveThreshold")


class TfMSLarge(_TransformationFunction):
    """
    TfMSLarge(meanMultiplier, STDMultiplier, lowerThreshold, valueBelowThreshold, upperThreshold, valueAboveThreshold)

    Spatial Analyst (ArcPy) class that defines an MSLarge function object.

    Arguments:
    meanMultiplier -- The multiplier for the mean of the input values in the MSLarge function equation.
    STDMultiplier -- The multiplier for the standard deviation of the input values in the MSLarge function equation.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function MSLarge object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            meanMultiplier=None,
            STDMultiplier=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "MSLARGE")
        self.meanMultiplier = meanMultiplier
        self.STDMultiplier = STDMultiplier
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.meanMultiplier,
            self.STDMultiplier,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.meanMultiplier,
            self.STDMultiplier,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfMSLarge._addProperty("meanMultiplier", 1.0)
TfMSLarge._addProperty("STDMultiplier", 1.0)
TfMSLarge._addProperty("lowerThreshold")
TfMSLarge._addProperty("valueBelowThreshold")
TfMSLarge._addProperty("upperThreshold")
TfMSLarge._addProperty("valueAboveThreshold")


class TfMSSmall(_TransformationFunction):
    """
    TfMSSmall({meanMultiplier}, {STDMultiplier}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines an MSSmall function object.

    Arguments:
    meanMultiplier -- The multiplier for the mean of the input values in the MSSmall function equation.
    STDMultiplier -- The multiplier for the standard deviation of the input values in the MSSmall function equation.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function MSSmall object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            meanMultiplier=None,
            STDMultiplier=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "MSSMALL")
        self.meanMultiplier = meanMultiplier
        self.STDMultiplier = STDMultiplier
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.meanMultiplier,
            self.STDMultiplier,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.meanMultiplier,
            self.STDMultiplier,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfMSSmall._addProperty("meanMultiplier", 1.0)
TfMSSmall._addProperty("STDMultiplier", 1.0)
TfMSSmall._addProperty("lowerThreshold")
TfMSSmall._addProperty("valueBelowThreshold")
TfMSSmall._addProperty("upperThreshold")
TfMSSmall._addProperty("valueAboveThreshold")


class TfLinear(_TransformationFunction):
    """
    TfLinear({minimum}, {maximum}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Linear function object.

    Arguments:
    minimum -- One of two points the Linear transformation function must pass through. If the minimum value is less than the maximum , the linear function will have a positive slope. If the minimum value is greater than the maximum , the linear function will have a negative slope.
    maximum -- One of two points the Linear function mustpass through. If the maximum value is greater than the minimum , the linear function will have a positive slope. If the maximum value is less than the minimum , the linear function will have a negative slope.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Linear object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            minimum=None,
            maximum=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "LINEAR")
        self.minimum = minimum
        self.maximum = maximum
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.minimum,
            self.maximum,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.minimum,
            self.maximum,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfLinear._addProperty("minimum")
TfLinear._addProperty("maximum")
TfLinear._addProperty("lowerThreshold")
TfLinear._addProperty("valueBelowThreshold")
TfLinear._addProperty("upperThreshold")
TfLinear._addProperty("valueAboveThreshold")


class TfSymmetricLinear(_TransformationFunction):
    """
    TfSymmetricLinear({minimum}, {maximum}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a SymmetricLinear function object.

    Arguments:
    minimum -- The starting point for the Symmetric Lineartransformation function. The point of inflection to mirror thefunction is determined by the midpoint of the minimum and maximum. Ifthe minimum value is less than the maximum , the linear function will have a positive slope. If the minimum value is greater than the maximum , the linear function will be a negative slope.
    maximum -- The ending point for the Symmetric Lineartransformation function. The point of inflection to mirror thefunction is determined by the midpoint of the minimum and maximum. If the minimum value is less than the maximum , the linear function will have a positive slope. If the minimum value is greater than the maximum , the linear function will have a negative slope.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function SymmetricLinear object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            minimum=None,
            maximum=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "SYMMETRICLINEAR")
        self.minimum = minimum
        self.maximum = maximum
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.minimum,
            self.maximum,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.minimum,
            self.maximum,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfSymmetricLinear._addProperty("minimum")
TfSymmetricLinear._addProperty("maximum")
TfSymmetricLinear._addProperty("lowerThreshold")
TfSymmetricLinear._addProperty("valueBelowThreshold")
TfSymmetricLinear._addProperty("upperThreshold")
TfSymmetricLinear._addProperty("valueAboveThreshold")


class TfExponential(_TransformationFunction):
    """
    TfExponential({shift}, {baseFactor}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines an Exponential function object.

    Arguments:
    shift -- Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.
    baseFactor -- A multiplier that controls how steep the Exponential function increases. The larger the multiplier, the steeper the curve will be at the larger input values. There is a close connection between the base factor and the base of the Exponential function. A baseFactor of 1 equals the natural exponential (e x ).
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Exponential object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            shift=None,
            baseFactor=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "EXPONENTIAL")
        self.shift = shift
        self.baseFactor = baseFactor
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.shift,
            self.baseFactor,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.shift,
            self.baseFactor,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfExponential._addProperty("shift")
TfExponential._addProperty("baseFactor")
TfExponential._addProperty("lowerThreshold")
TfExponential._addProperty("valueBelowThreshold")
TfExponential._addProperty("upperThreshold")
TfExponential._addProperty("valueAboveThreshold")


class TfLogarithm(_TransformationFunction):
    """
    TfLogarithm({shift}, {factor}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Logarithm function object.

    Arguments:
    shift -- Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.
    factor -- The multiplier to apply to the shifted input values. The factor alters the rise of the Logarithm curve.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Logarithm object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            shift=None,
            factor=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "LOGARITHM")
        self.shift = shift
        self.factor = factor
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.shift,
            self.factor,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.shift,
            self.factor,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfLogarithm._addProperty("shift")
TfLogarithm._addProperty("factor")
TfLogarithm._addProperty("lowerThreshold")
TfLogarithm._addProperty("valueBelowThreshold")
TfLogarithm._addProperty("upperThreshold")
TfLogarithm._addProperty("valueAboveThreshold")


class TfPower(_TransformationFunction):
    """
    TfPower({shift}, {exponent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a Power function object.

    Arguments:
    shift -- Defines how much each input value is to be shifted. The shift value is subtracted from the input value. The transformation function is applied to the shifted input value to determine the function value.
    exponent -- The power to raise the input values in the transformation function. As the exponent increases, the preference for the larger input values increases more rapidly.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function Power object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            shift=None,
            exponent=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "POWER")
        self.shift = shift
        self.exponent = exponent
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.shift,
            self.exponent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.shift,
            self.exponent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfPower._addProperty("shift")
TfPower._addProperty("exponent")
TfPower._addProperty("lowerThreshold")
TfPower._addProperty("valueBelowThreshold")
TfPower._addProperty("upperThreshold")
TfPower._addProperty("valueAboveThreshold")


class TfLogisticGrowth(_TransformationFunction):
    """
    TfLogisticGrowth({minimum}, {maximum}, {yInterceptPercent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a LogisticGrowth function object.

    Arguments:
    minimum -- The starting point for the LogisticGrowth transformation function.
    maximum -- The ending point for the LogisticGrowth transformation function.
    yInterceptPercent -- Determines the value range in the increasing portion of the logistic growth curve. The smaller the yInterceptPercent , the smaller the input value range will be in the growth section of the curve; however, the preference for the values will increase at a faster rate. A smaller yInterceptPercent results in a more pronounced logistic growth curve.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function LogisticGrowth object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            minimum=None,
            maximum=None,
            yInterceptPercent=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "LOGISTICGROWTH")
        self.minimum = minimum
        self.maximum = maximum
        self.yInterceptPercent = yInterceptPercent
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.minimum,
            self.maximum,
            self.yInterceptPercent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.minimum,
            self.maximum,
            self.yInterceptPercent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfLogisticGrowth._addProperty("minimum")
TfLogisticGrowth._addProperty("maximum")
TfLogisticGrowth._addProperty("yInterceptPercent", 1.0)
TfLogisticGrowth._addProperty("lowerThreshold")
TfLogisticGrowth._addProperty("valueBelowThreshold")
TfLogisticGrowth._addProperty("upperThreshold")
TfLogisticGrowth._addProperty("valueAboveThreshold")


class TfLogisticDecay(_TransformationFunction):
    """
    TfLogisticDecay({minimum}, {maximum}, {yInterceptPercent}, {lowerThreshold}, {valueBelowThreshold}, {upperThreshold}, {valueAboveThreshold})

    Spatial Analyst (ArcPy) class that defines a LogisticDecay function object.

    Arguments:
    minimum -- The starting point for the LogisticDecay transformation function.
    maximum -- The ending point for the LogisticDecay transformation function.
    yInterceptPercent -- Determines the value range in the decreasing portion of the logistic decay curve. The greater the yInterceptPercent , the smaller the input value range will be in the decay section of the curve; however, the preference for the values will decrease at a faster rate. A larger yInterceptPercent results in a more pronounced logistic decay curve.
    lowerThreshold -- Defines the starting value at which to begin applying the specified transformation function. The input value corresponding to the lowerThreshold is assigned to the fromScale evaluation scale value on the output raster. Input values below the lowerThreshold are assigned to the valueBelowThreshold and are not considered in the function value range.
    valueBelowThreshold -- A user-specified value to assign output cell locations with input values below the lowerThreshold.
    upperThreshold -- Defines the ending value at which to stop applying the specified transformation function. The input value corresponding to the upperThreshold is assigned to the toScale evaluation scale value on the output raster. Input values above the upperThreshold are assigned to the valueAboveThreshold and are not considered in the function value range.
    valueAboveThreshold -- A user-specified value to assign output cell locations with input values above the upperThreshold.

    Results:
    A Transformation function LogisticDecay object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
        "Variant:::",
        "Double:::",
        "Variant:::",
    ]

    def __init__(self,
            minimum=None,
            maximum=None,
            yInterceptPercent=None,
            lowerThreshold=None,
            valueBelowThreshold=None,
            upperThreshold=None,
            valueAboveThreshold=None):
        _TransformationFunction.__init__(self, "LOGISTICDECAY")
        self.minimum = minimum
        self.maximum = maximum
        self.yInterceptPercent = yInterceptPercent
        self.lowerThreshold = lowerThreshold
        self.valueBelowThreshold = valueBelowThreshold
        self.upperThreshold = upperThreshold
        self.valueAboveThreshold = valueAboveThreshold

    def __str__(self):
        return self._toString([
            self._keyword,
            self.minimum,
            self.maximum,
            self.yInterceptPercent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

    def __repr__(self):
        return self._toRepresentation([
            self.minimum,
            self.maximum,
            self.yInterceptPercent,
            self.lowerThreshold,
            self.valueBelowThreshold,
            self.upperThreshold,
            self.valueAboveThreshold])

TfLogisticDecay._addProperty("minimum")
TfLogisticDecay._addProperty("maximum")
TfLogisticDecay._addProperty("yInterceptPercent", 99.0)
TfLogisticDecay._addProperty("lowerThreshold")
TfLogisticDecay._addProperty("valueBelowThreshold")
TfLogisticDecay._addProperty("upperThreshold")
TfLogisticDecay._addProperty("valueAboveThreshold")


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class _VerticalFactor(CompoundParameter._CompoundParameter):

    def __init__(self,
            keyword):
        CompoundParameter._CompoundParameter.__init__(self, keyword)


class VfBinary(_VerticalFactor):
    """
    VfBinary({zeroFactor}, {lowCutAngle}, {highCutAngle})

    Spatial Analyst (ArcPy) class that defines a binary vertical factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the binary function.
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.

    Results:
    A VfBinary vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            lowCutAngle=None,
            highCutAngle=None):
        _VerticalFactor.__init__(self, "BINARY")
        self.zeroFactor = zeroFactor
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle])

VfBinary._addProperty("zeroFactor", 1.0)
VfBinary._addProperty("lowCutAngle", -30.0)
VfBinary._addProperty("highCutAngle", 30.0)


class VfLinear(_VerticalFactor):
    """
    VfLinear({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines a linear vertical factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the linear function.
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    slope -- Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a 90-degree slope as 0.011111.

    Results:
    A VfLinear vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            lowCutAngle=None,
            highCutAngle=None,
            slope=None):
        _VerticalFactor.__init__(self, "LINEAR")
        self.zeroFactor = zeroFactor
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

VfLinear._addProperty("zeroFactor", 1.0)
VfLinear._addProperty("lowCutAngle", -90.0)
VfLinear._addProperty("highCutAngle", 90.0)
VfLinear._addProperty("slope", 0.011111)


class VfInverseLinear(_VerticalFactor):
    """
    VfInverseLinear({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines an inverse linear vertical factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the inverse linear function.
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    slope -- Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a -45-degree slope as -0.02222.

    Results:
    A VfInverseLinear vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            lowCutAngle=None,
            highCutAngle=None,
            slope=None):
        _VerticalFactor.__init__(self, "INVERSE_LINEAR")
        self.zeroFactor = zeroFactor
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

VfInverseLinear._addProperty("zeroFactor", 1.0)
VfInverseLinear._addProperty("lowCutAngle", -45.0)
VfInverseLinear._addProperty("highCutAngle", 45.0)
VfInverseLinear._addProperty("slope", -0.022222)


class VfSymLinear(_VerticalFactor):
    """
    VfSymLinear({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines a symmetrical linear vertical factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the symmetric linear function.
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    slope -- Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a 90-degree slope as 0.011111.

    Results:
    A VfSymLinear vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=1.0,
            lowCutAngle=-90.0,
            highCutAngle=90.0,
            slope=0.011111):
        _VerticalFactor.__init__(self, "SYM_LINEAR")
        self.zeroFactor = zeroFactor
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

VfSymLinear._addProperty("zeroFactor", 1.0)
VfSymLinear._addProperty("lowCutAngle", -90.0)
VfSymLinear._addProperty("highCutAngle", 90.0)
VfSymLinear._addProperty("slope", 0.011111)


class VfSymInverseLinear(_VerticalFactor):
    """
    VfSymInverseLinear({zeroFactor}, {lowCutAngle}, {highCutAngle}, {slope})

    Spatial Analyst (ArcPy) class that defines a symmetrical inverse linear vertical factor object.

    Arguments:
    zeroFactor -- The zeroFactor will be used to position the y-intercept of the symmetric inverse linear function.
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    slope -- Identifies the slope of the straight line in the VRMA-VF coordinate system. Slope is specified as the rise/run. For example, a 30-degree slope is 1/30, specified as 0.03333 (rise/run: 1 VF on the y axis / 30 degrees on the x axis); a -45-degree slope as -0.022222.

    Results:
    A VfSymInverseLinear vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            zeroFactor=None,
            lowCutAngle=None,
            highCutAngle=None,
            slope=None):
        _VerticalFactor.__init__(self, "SYM_INVERSE_LINEAR")
        self.zeroFactor = zeroFactor
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.slope = slope

    def __str__(self):
        return self._toString([
            self._keyword,
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

    def __repr__(self):
        return self._toRepresentation([
            self.zeroFactor,
            self.lowCutAngle,
            self.highCutAngle,
            self.slope])

VfSymInverseLinear._addProperty("zeroFactor", 1.0)
VfSymInverseLinear._addProperty("lowCutAngle", -45.0)
VfSymInverseLinear._addProperty("highCutAngle", 45.0)
VfSymInverseLinear._addProperty("slope", -0.022222)


class VfCos(_VerticalFactor):
    """
    VfCos({lowCutAngle}, highCutAngle, {cosPower})

    Spatial Analyst (ArcPy) class that defines a cosine vertical factor object.

    Arguments:
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    cosPower -- The power to which the values in the cosine VRMA function will be raised. The VF is determined by:

    Results:
    A VfCos vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            lowCutAngle=None,
            highCutAngle=None,
            cosPower=None):
        _VerticalFactor.__init__(self, "COS")
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.cosPower = cosPower

    def __str__(self):
        return self._toString([
            self._keyword,
            self.lowCutAngle,
            self.highCutAngle,
            self.cosPower])

    def __repr__(self):
        return self._toRepresentation([
            self.lowCutAngle,
            self.highCutAngle,
            self.cosPower])

VfCos._addProperty("lowCutAngle", -90.0)
VfCos._addProperty("highCutAngle", 90.0)
VfCos._addProperty("cosPower", 1.0)


class VfSec(_VerticalFactor):
    """
    VfSec({lowCutAngle}, {highCutAngle}, {secPower})

    Spatial Analyst (ArcPy) class that defines a secant vertical factor object.

    Arguments:
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    secPower -- The power to which the values in the secant VRMA function will be raised. The VF is determined by:

    Results:
    A VfSec vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            lowCutAngle=None,
            highCutAngle=None,
            secPower=None):
        _VerticalFactor.__init__(self, "SEC")
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.secPower = secPower

    def __str__(self):
        return self._toString([
            self._keyword,
            self.lowCutAngle,
            self.highCutAngle,
            self.secPower])

    def __repr__(self):
        return self._toRepresentation([
            self.lowCutAngle,
            self.highCutAngle,
            self.secPower])

VfSec._addProperty("lowCutAngle", -90.0)
VfSec._addProperty("highCutAngle", 90.0)
VfSec._addProperty("secPower", 1.0)


class VfCosSec(_VerticalFactor):
    """
    VfCosSec({lowCutAngle}, {highCutAngle}, {cosPower}, {secPower})

    Spatial Analyst (ArcPy) class that defines a cosine secant vertical factor object.

    Arguments:
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity.
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    cosPower -- The power to which the values in the cosine VRMA function will be raised. The VF is determined by:
    secPower -- The power to which the values in the secant VRMA function will be raised. The VF is determined by:

    Results:
    A VfCosSec vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            lowCutAngle=None,
            highCutAngle=None,
            cosPower=None,
            secPower=None):
        _VerticalFactor.__init__(self, "COS_SEC")
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.cosPower = cosPower
        self.secPower = secPower

    def __str__(self):
        return self._toString([
            self._keyword,
            self.lowCutAngle,
            self.highCutAngle,
            self.cosPower,
            self.secPower])

    def __repr__(self):
        return self._toRepresentation([
            self.lowCutAngle,
            self.highCutAngle,
            self.cosPower,
            self.secPower])

VfCosSec._addProperty("lowCutAngle", -90.0)
VfCosSec._addProperty("highCutAngle", 90.0)
VfCosSec._addProperty("cosPower", 1.0)
VfCosSec._addProperty("secPower", 1.0)


class VfSecCos(_VerticalFactor):
    """
    VfSecCos({lowCutAngle}, {highCutAngle}, {secPower}, {cosPower})

    Spatial Analyst (ArcPy) class that defines a secant cosine vertical factor object.

    Arguments:
    lowCutAngle -- The VRMA degree defining the lower threshold, below which (less than) the VFs are set to infinity
    highCutAngle -- The VRMA degree defining the upper threshold, beyond which (larger than) the VFs are set to infinity.
    secPower -- The power to which the values in the secant VRMA function will be raised. The VF is determined by:
    cosPower -- The power to which the values in the cosine VRMA function will be raised. The VF is determined by:

    Results:
    A VfSecCos vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::",
    ]

    def __init__(self,
            lowCutAngle=None,
            highCutAngle=None,
            secPower=None,
            cosPower=None):
        _VerticalFactor.__init__(self, "SEC_COS")
        self.lowCutAngle = lowCutAngle
        self.highCutAngle = highCutAngle
        self.secPower = secPower
        self.cosPower = cosPower

    def __str__(self):
        return self._toString([
            self._keyword,
            self.lowCutAngle,
            self.highCutAngle,
            self.secPower,
            self.cosPower])

    def __repr__(self):
        return self._toRepresentation([
            self.lowCutAngle,
            self.highCutAngle,
            self.secPower,
            self.cosPower])

VfSecCos._addProperty("lowCutAngle", -90.0)
VfSecCos._addProperty("highCutAngle", 90.0)
VfSecCos._addProperty("secPower", 1.0)
VfSecCos._addProperty("cosPower", 1.0)


class VfTable(_VerticalFactor):
    """
    VfTable(inTable)

    Spatial Analyst (ArcPy) class that defines a table vertical factor object.

    Arguments:
    inTable -- The inTable is an ASCII file with two columns on each line. The first column identifies the VRMA in degrees, and the second, the VF. Each line specifies a point. Two consecutive points produce a line segment in the VRMA-VF coordinate system.

    Results:
    A VfSymLinear vertical factor object is returned.
    """

    __esri_toolinfo__ = [
        "File:::",
    ]

    def __init__(self,
            inTable):
        _VerticalFactor.__init__(self, "TABLE")
        self.inTable = CompoundParameter._DataSetName(inTable)

    def __str__(self):
        return self._toString([
            self._keyword,
            self.inTable])

    def __repr__(self):
        return self._toRepresentation([
            self.inTable])

VfTable._addProperty("inTable")


try:
    from . import CompoundParameter
    from . import Utils

except (SystemError, ValueError):
    import CompoundParameter
    import Utils

class WOTable(CompoundParameter._CompoundParameter):
    """
    WOTable([[inRaster, influence, field, Remap],...], [from, to, by])

    Spatial Analyst (ArcPy) class that defines a weighted overlay table object.

    Arguments:
    weightedOverlayTable -- The table specifying the input rasters, their influence, the field to use, and the remap table identifying what the old values should be remapped to.
    evaluationScale -- The range and interval for the new values in which to remap the old values. The parameter is required for both the dialog box and scripting but it has no effect in scripting.

    Results:
    A WOTable object is returned defining the input rasters, the field identifying the input values, the remap of their values, the weight of each raster, and the evaluation scale.
    """

    __esri_toolinfo__ = [
        "List:::",
        "List:::",
    ]

    def __init__(self,
            weightedOverlayTable,
            evaluationScale):
        CompoundParameter._CompoundParameter.__init__(self)

        self.weightedOverlayTable = [list(record) for record in
            weightedOverlayTable]
        self.evaluationScale = list(evaluationScale)

    def __str__(self):
        strings = []

        for record in self.weightedOverlayTable:
            # Currently, it is relevant that single quotes are used around
            # strings. This is relevant for strings and class instances whos
            # string representation is used.
            string = " ".join(map(
                lambda item: not Utils.isNumerical(item) and
                    "'%s'" % (str(item)) or str(item), record[:-1]))
            string += " (%s)" % (str(record[-1]))
            strings.append(string)

        return "(%s); %s" % (
            "; ".join(strings),
            " ".join([str(item) for item in self.evaluationScale]))

    def __repr__(self):
        return self._toRepresentation([
            self.weightedOverlayTable,
            self.evaluationScale])

WOTable._addProperty("weightedOverlayTable")
WOTable._addProperty("evaluationScale")


try:
    from . import CompoundParameter
except (SystemError, ValueError):
    import CompoundParameter

class WSTable(CompoundParameter._CompoundParameter):
    """
    WSTable([[inRaster, field, weight],...])

    Spatial Analyst (ArcPy) class that defines a weighted sum table object.

    Arguments:
    weightedSumTable -- The table specifying the input rasters, the fields to use for the values for each raster, and the weight by which to multiply each raster.

    Results:
    A WSTable object is returned defining the input rasters, the field that will be used for each raster, and the weight each raster will have.
    """

    __esri_toolinfo__ = [
        "List:::",
    ]

    def __init__(self,
            weightedSumTable):
        CompoundParameter._CompoundParameter.__init__(self)
        self.weightedSumTable = [list(record) for record in weightedSumTable]

    def __str__(self):
        return "; ".join(map(lambda record:
            " ".join(["'{0}'".format(str(record[0]))] +
                [str(item) for item in record[1:]]), self.weightedSumTable))

    def __repr__(self):
        return self._toRepresentation([self.weightedSumTable])

WSTable._addProperty("weightedSumTable")
