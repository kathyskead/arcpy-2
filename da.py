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
"Data Access Module"
from arcgisscripting import da

__all__ = [item for item in dir(da) if not item.startswith('_')]
del item

locals().update(da.__dict__)
del da
