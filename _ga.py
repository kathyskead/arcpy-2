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
"""
Contains the implementation of the Neighborhood classes.
"""

__all__ = [
    "SearchNeighborhoodStandard",
    "SearchNeighborhoodSmooth",
    "SearchNeighborhoodStandardCircular",
    "SearchNeighborhoodSmoothCircular",
    "CrossValidationResult",
    "GeostatisticalDatasets"
    ]

from _base import _NamedAttrObject, _ValidateParameter
import gapy

#=======================================================================
class SearchNeighborhoodStandard(_NamedAttrObject):
    """The SearchNeighborhoodStandard class can be used to define the search
       neighborhood for IDW , Local Polynomial Interpolation , and Radial Basis
       Functions .  Search neighborhoods"""
    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Long:::",
        "Long:::",
        "String::ONE_SECTOR|FOUR_SECTORS|FOUR_SECTORS_SHIFTED|EIGHT_SECTORS:"
        ]

    def __init__(self,
                 majorSemiaxis=None,
                 minorSemiaxis=None,
                 angle = 0.,
                 nbrMax = 15,
                 nbrMin = 10,
                 sectorType = "ONE_SECTOR"):
        """SearchNeighborhoodStandard({majorSemiaxis}, {minorSemiaxis}, {angle},
           {nbrMax}, {nbrMin}, {sectorType})

             majorSemiaxis{Double}:
           The distance, in map units, specifying the length of the major semi
           axis of the ellipse within which data is selected from.

             minorSemiaxis{Double}:
           The distance, in map units, specifying the length of the minor semi
           axis of the ellipse within which data is selected from.

             angle{Double}:
           The angle of the search ellipse.

             nbrMax{Long}:
           Maximum number of neighbors, within the search ellipse, to use when
           making the prediction.

             nbrMin{Long}:
           Minimum number of neighbors, within the search ellipse, to use when
           making the prediction.

             sectorType{String}:
           The searching ellipse can be divided into 1, 4, 4 with an offset of
           45º, or 8 sectors."""
        self.majorSemiaxis = majorSemiaxis
        self.minorSemiaxis = minorSemiaxis
        self.angle = _ValidateParameter(angle, 0.)
        self.nbrMax = _ValidateParameter(nbrMax, 15)
        self.nbrMin = _ValidateParameter(nbrMin, 10)
        self.sectorType = _ValidateParameter(sectorType, "ONE_SECTOR")

SearchNeighborhoodStandard._add_attr("nbrType", "NBRTYPE", "Standard", True)
SearchNeighborhoodStandard._add_attr("majorSemiaxis", "S_MAJOR")
SearchNeighborhoodStandard._add_attr("minorSemiaxis", "S_MINOR")
SearchNeighborhoodStandard._add_attr("angle", "ANGLE")
SearchNeighborhoodStandard._add_attr("nbrMax", "NBR_MAX")
SearchNeighborhoodStandard._add_attr("nbrMin", "NBR_MIN")
SearchNeighborhoodStandard._add_attr("sectorType", "SECTOR_TYPE")

#=======================================================================
class SearchNeighborhoodSmooth(_NamedAttrObject):
    """The SearchNeighborhoodSmooth class can be used to define the search
       neighborhood for IDW , Local Polynomial Interpolation , and Radial Basis
       Functions (only when the INVERSE_MULTIQUADRIC_FUNCTION keyword is used).
       The smooth search neighborhood class accepts inputs for a minor and major
       axis, the size of search ellipse, the angle of the search ellipse, and a
       smoothing factor.  Smooth interpolation"""
    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Double:::",
        "Double:::"
        ]

    def __init__(self,
                 majorSemiaxis=None,
                 minorSemiaxis=None,
                 angle = 0.,
                 smoothFactor = 0.2):
        """SearchNeighborhoodSmooth({majorSemiaxis}, {minorSemiaxis}, {angle},
           {smoothFactor})

             majorSemiaxis{Double}:
           The distance, in map units, specifying the length of the major semi
           axis of the ellipse within which data is selected from.

             minorSemiaxis{Double}:
           The distance, in map units, specifying the length of the minor semi
           axis of the ellipse within which data is selected from.

             angle{Double}:
           The angle of the search ellipse.

             smoothFactor{Double}:
           Determines how much smoothing will be performed. 0 is no smoothing; 1
           is the maximum amount of smoothing."""
        self.majorSemiaxis = majorSemiaxis
        self.minorSemiaxis = minorSemiaxis
        self.angle = _ValidateParameter(angle, 0.)
        self.smoothFactor = _ValidateParameter(smoothFactor, 0.2)

SearchNeighborhoodSmooth._add_attr("nbrType", "NBRTYPE", "Smooth", True)
SearchNeighborhoodSmooth._add_attr("majorSemiaxis", "S_MAJOR")
SearchNeighborhoodSmooth._add_attr("minorSemiaxis", "S_MINOR")
SearchNeighborhoodSmooth._add_attr("angle", "ANGLE")
SearchNeighborhoodSmooth._add_attr("smoothFactor", "SMOOTH_FACTOR")

#=======================================================================
class SearchNeighborhoodStandardCircular(_NamedAttrObject):
    """The SearchNeighborhoodStandardCircular class can be used to define the
       search neighborhood for Empirical Bayesian Kriging , IDW , Local
       Polynomial Interpolation , and Radial Basis Functions .  Search
       neighborhoods"""
    __esri_toolinfo__ = [
        "Double:::",
        "Double:::",
        "Long:::",
        "Long:::",
        "String::ONE_SECTOR|FOUR_SECTORS|FOUR_SECTORS_SHIFTED|EIGHT_SECTORS:"
        ]

    def __init__(self,
                 radius = None,
                 angle = 0.,
                 nbrMax = 15,
                 nbrMin = 10,
                 sectorType = "ONE_SECTOR"):
        """SearchNeighborhoodStandardCircular({radius}, {angle}, {nbrMax},
           {nbrMin}, {sectorType})

             radius{Double}:
           The distance, in map units, specifying the length of the radius of
           the searching circle.

             angle{Double}:
           The angle of the search circle. This parameter will only affect the
           angle of the sectors.

             nbrMax{Long}:
           Maximum number of neighbors, within the search ellipse, to use when
           making the prediction.

             nbrMin{Long}:
           Minimum number of neighbors, within the search ellipse, to use when
           making the prediction.

             sectorType{String}:
           The searching ellipse can be divided into 1, 4, 4 with an offset of
           45º, or 8 sectors."""
        self.radius = radius
        self.angle = _ValidateParameter(angle, 0.)
        self.nbrMax = _ValidateParameter(nbrMax, 15)
        self.nbrMin = _ValidateParameter(nbrMin, 10)
        self.sectorType = _ValidateParameter(sectorType, "ONE_SECTOR")

SearchNeighborhoodStandardCircular._add_attr("nbrType", "NBRTYPE", "StandardCircular", True)
SearchNeighborhoodStandardCircular._add_attr("radius", "RADIUS")
SearchNeighborhoodStandardCircular._add_attr("angle", "ANGLE")
SearchNeighborhoodStandardCircular._add_attr("nbrMax", "NBR_MAX")
SearchNeighborhoodStandardCircular._add_attr("nbrMin", "NBR_MIN")
SearchNeighborhoodStandardCircular._add_attr("sectorType", "SECTOR_TYPE")

#=======================================================================
class SearchNeighborhoodSmoothCircular(_NamedAttrObject):
    """The SearchNeighborhoodSmoothCircular class can be used to define the
       search neighborhood for Empirical Bayesian Kriging , IDW , Local
       Polynomial Interpolation , and Radial Basis Functions (only when the
       INVERSE_MULTIQUADRIC_FUNCTION keyword is used). The class accepts inputs
       for the radius of the searching circle and a smoothing factor.  Smooth
       interpolation"""
    __esri_toolinfo__ = [
        "Double:::",
        "Double:::"
        ]

    def __init__(self,
                 radius=None,
                 smoothFactor = 0.2):
        """SearchNeighborhoodSmoothCircular({radius}, {smoothFactor})

             radius{Double}:
           The distance, in map units, specifying the length of the radius of
           the searching circle.

             smoothFactor{Double}:
           Determines how much smoothing will be performed. 0 is no smoothing; 1
           is the maximum amount of smoothing."""
        self.radius = radius
        self.smoothFactor = _ValidateParameter(smoothFactor, 0.2)

SearchNeighborhoodSmoothCircular._add_attr("nbrType", "NBRTYPE", "SmoothCircular", True)
SearchNeighborhoodSmoothCircular._add_attr("radius", "RADIUS")
SearchNeighborhoodSmoothCircular._add_attr("smoothFactor", "SMOOTH_FACTOR")

#=======================================================================
from arcpy.arcobjects import Result

class CrossValidationResult(Result):
    """The CrossValidationResult class is returned by the Cross Validation tool
       and contains access to the cross-validation results that can be generated
       for any geostatistical layer."""
    @property
    def count(self):
        return self.getOutput(1)

    @property
    def meanError(self):
        return self.getOutput(2)

    @property
    def rootMeanSquare(self):
        return self.getOutput(3)

    @property
    def averageStandard(self):
        return self.getOutput(4)

    @property
    def meanStandardized(self):
        return self.getOutput(5)

    @property
    def rootMeanSquareStandardized(self):
        return self.getOutput(6)

#=======================================================================
class GADatasets(object) :
    def __init__(self, info):
        self._info = info
        for row in info :
            for param in row :
                self.__dict__[param['name']] = param['value']

    def __str__(self):
        strRes = ""
        for row in self._info:
            for param in row:
                value = getattr(self, param['name'])
                #if value is not None and value != "" and value != "#":
                strRes += param['name'] + "='" + str(value) + "' "
                
            strRes = strRes.rstrip()            
            strRes += ';'
                
        return strRes[0:-1] #remove the last ';'

    def __repr__(self):
        strRes = ""
        for row in self._info:
            for param in row:
                value = getattr(self, param['name'])
                if value is not None and value != "" and value != "#":
                    if param['cmd'] != '' :
                        strRes += param['cmd'] + "=" + str(value) + " "
                    else :
                        strRes += str(value) + " "
            strRes = strRes.rstrip()            
            strRes += ';'
                
        return strRes[0:-1] #remove the last ';'

    @property
    def _arc_object(self):
        return self.__repr__()
    
#=======================================================================
def GeostatisticalDatasets(ga_model_source) :
    return GADatasets(gapy.GALayerInfo(ga_model_source))

GeostatisticalDatasets.__esri_toolinfo__ = [
            "GeostatisticalLayer:::",
            ]
