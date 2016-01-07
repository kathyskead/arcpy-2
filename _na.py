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
from arcgisscripting import na

__all__ = ['CheckIntersectingFeatures',
           'ListDirectionsLanguages',
           'ListDirectionsStyleNames',
           'GenerateDirectionsFeatures',
           'GetNAClassNames',
		   'GetTravelModes',
           'GetSolverProperties',
           'RouteSolverProperties',
           'ClosestFacilitySolverProperties',
           'ServiceAreaSolverProperties',
           'ODCostMatrixSolverProperties',
           'VehicleRoutingProblemSolverProperties',
           'LocationAllocationSolverProperties',
		   'TravelMode',
           'StreetDirectionsProperties',
           'NAClassFieldMap',
           'NAClassFieldMappings']

class ClosestFacilitySolverProperties(na.ClosestFacilitySolverProperties):
    """Provides access to analysis properties from a closest facility network
       analysis layer. The GetSolverProperties function is used to obtain a
       ClosestFacilitySolverProperties object from a closest facility network
       analysis layer."""
    pass

class LocationAllocationSolverProperties(na.LocationAllocationSolverProperties):
    """Provides access to analysis properties from a location-allocation network
       analysis layer. The GetSolverProperties function is used to obtain a
       LocationAllocationSolverProperties object from a location-allocation
       network analysis layer."""
    pass

class TravelMode(na.TravelMode):
    """Provides access to travel mode properties for
       configuring solver with a predefined named set of properties representing
	   a mode of travel."""
    pass
	
class StreetDirectionsProperties(na.StreetDirectionsProperties):
    """Provides access to direction configuration analysis properties for
       configuring street directions output."""
    pass
        
class NAClassFieldMappings(na.NAClassFieldMappings):
    """Provides  a Python dictionary of NAClassFieldMap objects that are used to
       map field names or set default values for the properties of a network
       analysis class within a network analysis layer. The dictionary keys are
       the network analysis class property names, and the values are the
       NAClassFieldMap objects."""
    pass

class NAClassFieldMap(na.NAClassFieldMap):
    """Provides the ability to map field names or set default values for the
       properties of a network analysis  class within a network analysis layer.
       The properties of the network analysis class  are used  as inputs by the
       solvers while performing  the network analyses."""
    pass

class ODCostMatrixSolverProperties(na.ODCostMatrixSolverProperties):
    """Provides access to analysis properties from an origin-destination (OD)
       cost matrix network analysis layer. The GetSolverProperties function is
       used to obtain an ODCostMatrixSolverProperties object from an OD cost
       matrix network analysis layer."""
    pass

class RouteSolverProperties(na.RouteSolverProperties):
    """Provides access to analysis properties from a route network analysis
       layer. The GetSolverProperties function is used to obtain a
       RouteSolverProperties object from a route network analysis layer."""
    pass

class ServiceAreaSolverProperties(na.ServiceAreaSolverProperties):
    """Provides access to analysis properties from a service area network
       analysis layer. The GetSolverProperties function is used to obtain a
       ServiceAreaSolverProperties object from a service area network analysis
       layer."""
    pass

class VehicleRoutingProblemSolverProperties(na.VehicleRoutingProblemSolverProperties):
    """Provides access to analysis properties from a vehicle routing problem
       Network Analyst layer. The GetSolverProperties function is used to obtain
       a VehicleRoutingProblemSolverProperties object from a vehicle routing
       problem Network Analyst layer."""
    pass

def CheckIntersectingFeatures(network_dataset_path, feature_layer, cutoff=5000):
    """CheckIntersectingFeatures(network_dataset_path, feature_layer, {cutoff})

       Returns a Boolean indicating whether the number of edge source features
       from the specified network dataset that are intersected by the features
       within the specified feature layer is less than or equal to the specified
       cutoff. The function is useful to restrict the number of features that
       can be loaded as line or polygon barriers into a network analysis layer.

         network_dataset_path(String):
       A variable that references the catalog path of the network dataset. Each
       edge source in this network dataset will be considered while performing
       the check. The catalog path of a  network dataset can be obtained from
       the dataSource property of a network dataset layer or a network analysis
       layer object. It can also be obtained from the catalogPath property of a
       network dataset Describe object.

         feature_layer(Layer):
       A variable that references the Layer object containing the features that
       are intersected with the edge sources. Any selection set or definition
       query present on the Layer object is honored and can be used to specify
       only a subset of features.

         cutoff{Long}:
       An integer value used as a cutoff while performing the check."""
    from arcgisscripting import na
    return na.CheckIntersectingFeatures(network_dataset_path, feature_layer, cutoff)

def ListDirectionsLanguages(network_dataset_path):
    """ListDirectionsLanguages(network_dataset_path)

       Returns a List of supported directions language names of the network dataset.

         network_dataset_path(String):
       A variable that references the catalog path of the network dataset. Each
       edge source in this network dataset will be considered while performing
       the check. The catalog path of a  network dataset can be obtained from
       the dataSource property of a network dataset layer or a network analysis
       layer object. It can also be obtained from the catalogPath property of a
       network dataset Describe object."""
    from arcgisscripting import na
    return na.ListDirectionsLanguages(network_dataset_path)

def ListDirectionsStyleNames(network_dataset_path):
    """ListDirectionsStyleNames(network_dataset_path)

       Returns a List of available directions style names of the network dataset.

         network_dataset_path(String):
       A variable that references the catalog path of the network dataset. Each
       edge source in this network dataset will be considered while performing
       the check. The catalog path of a  network dataset can be obtained from
       the dataSource property of a network dataset layer or a network analysis
       layer object. It can also be obtained from the catalogPath property of a
       network dataset Describe object."""
    from arcgisscripting import na
    return na.ListDirectionsStyleNames(network_dataset_path)

def GenerateDirectionsFeatures(network_analyst_layer, catalog_path="in_memory\\Directions",
	schema_only=False, configuration_keyword=None):
    """GenerateDirectionsFeatures(network_analyst_layer, {catalog_path}, {schema_only}, {configuration_keyword})

       Returns a String indicating the full catalog path of the generated directions feature class.
       
         network_analyst_layer(Layer):
       A variable that references a Layer object obtained from a network
       analysis layer. It can be derived from existing layers in a map document
       or by specifying the catalog path to the network analysis layer file as
       an argument to the Layer class. The isNetworkAnalystLayer property on the
       Layer object can be used to identify whether a given Layer object is a
       network analysis layer. The analysis layer solver type must be 'Route', 'VRP',
       or 'Closest Facility' because directions support is required. Also, the network 
       dataset used by the analysis layer must be configured for directions.
       
        catalog_path{String}:
      The catalog path to the output directions feature class.
                  
        schema_only{bool}
      Indicates whether to only generate an empty directions feature class or to also populate it with direction features.
                  
        configuration_keyword{String}
      The configuration keyword of the output directions feature class."""
    from arcgisscripting import na
    return na.GenerateDirectionsFeatures(network_analyst_layer, catalog_path, schema_only, configuration_keyword)

def GetNAClassNames(network_analyst_layer, naclass_edit_type='ANY', nalocation_type='ANY', shape_type='ANY'):
    """GetNAClassNames(network_analyst_layer, {naclass_edit_type},
       {nalocation_type}, {shape_type})

       Returns a dictionary of network analysis class names from the network
       analysis layer specified as argument. The dictionary keys are the network
       analysis class names, and the values are the layer names that reference
       the network analysis classes from the network analysis layer.
        The layer names are used as input in some geoprocessing tools such as
        Add Locations and Add Field To Analysis Layer .

         network_analyst_layer(Layer):
       A variable that references a Layer object obtained from a network
       analysis layer. It can be derived from existing layers in a map document
       or by specifying the catalog path to the network analysis layer file as
       an argument to the Layer class. The isNetworkAnalystLayer property on the
       Layer object can be used to identify whether a given Layer object is a
       network analysis layer.

         naclass_edit_type{String}:
       A string that specifies which network analysis classes are included in
       the output dictionary based on their edit mode in the network analysis
       layer. The argument value can be one of the following string keywords:

        * ANY:   Include all the classes from the network analysis layer. This
        is the default value.

        * INPUT:   Include only those classes that support an input mode in the
        network analysis layer. This option will also include classes that
        support both input and output modes.

        * OUTPUT:   Include only those classes that support an output mode in
        the network analysis layer. This option will also include classes that
        support both input and output modes.

         nalocation_type{String}:
       A string that specifies which network analysis classes are included in
       the output dictionary based on their support for location fields. The
       argument value can be one of the following string keywords:

        * ANY:   Include the classes from the network analysis layer
        irrespective of whether they do or do not support location fields. This
        is the default value.

        * LOCATION:   Include only those classes from the network analysis layer
        that support location fields or location ranges.

        * NOT_LOCATION:   Include only those classes from the network analysis
        layer that do not support location fields or location ranges.

         shape_type{String}:
       A string that specifies which network analysis classes are included in
       the output dictionary based on their shape type. The argument value can
       be one of the following string keywords:

        * ANY:   Include all shape type classes from the network analysis layer.
        This is the default value.

        * POINT:   Include only point classes from the network analysis layer.

        * LINE:   Include only line classes from the network analysis layer.

        * POLYGON:   Include only polygon classes from the network analysis
        layer.

        * NULL:   Include only tables from the network analysis layer."""
    from arcgisscripting import na
    return na.GetNAClassNames(network_analyst_layer, naclass_edit_type, nalocation_type, shape_type)

def GetTravelModes(network_dataset_path):
    """GetTravelModes(network_dataset_path)

       Returns a dictionary of travel modes from the specified network dataset.
	   The function is useful to apply override properties from a travel mode to a
	   solver settings object. The travel modes predefined in the network dataset
	   can be useful for quickly setting a group of related settings (a travel mode).

         network_dataset_path(String):
       A variable that references the catalog path of the network dataset. The
	   catalog path of a  network dataset can be obtained from the dataSource
	   property of a network dataset layer or a network analysis layer object.
	   It can also be obtained from the catalogPath property of a network dataset
	   Describe object."""
    from arcgisscripting import na
    return na.GetTravelModes(network_dataset_path)
	
def GetSolverProperties(network_analyst_layer):
    """GetSolverProperties(network_analyst_layer)

       Returns a Network Analyst solver properties object based on the type of
       the Network Analyst layer specified as the argument. The solver
       properties object is used to update the analysis properties for the
       layer.

         network_analyst_layer(Layer):
       A variable that references a layer object obtained from a Network Analyst
       layer. It can be derived from existing layers in a map document or by
       specifying the catalog path to the Network Analyst layer file as an
       argument to the Layer class. The isNetworkAnalystLayer property on the
       layer object can be used to identify whether a given layer object is a
       Network Analyst layer."""
    from arcgisscripting import na
    return na.GetSolverProperties(network_analyst_layer)

del na
