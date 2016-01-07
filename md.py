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
"""The Multidimension toolbox contains tools that operate on netCDF data. You can
use these tools to make a netCDF raster layer, feature layer, or table view; to
convert to netCDF from a raster, feature, or table; and to select a dimension of
a netCDF layer or table."""
__all__ = ['MakeNetCDFRasterLayer', 'SelectByDimension', 'RasterToNetCDF', 'MakeNetCDFTableView', 'TableToNetCDF', 'MakeNetCDFFeatureLayer', 'FeatureToNetCDF']
__alias__ = u'md'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject

# Tools
@gptooldoc('FeatureToNetCDF_md', None)
def FeatureToNetCDF(in_features=None, fields_to_variables=None, out_netCDF_file=None, fields_to_dimensions=None):
    """FeatureToNetCDF_md(in_features, fields_to_variables;fields_to_variables..., out_netCDF_file, {fields_to_dimensions;fields_to_dimensions...})

        Converts a point feature class to a netCDF file.

     INPUTS:
      in_features (Feature Layer):
          The input point feature class.
      fields_to_variables (Value Table):
          The field or fields used to create variables in the netCDF file.Four special
          fields—Shape.X, Shape.Y, Shape.Z, and Shape.M—can be used for
          exporting x-coordinates or longitude, y-coordinates or latitude, Z values, and M
          values of input features, respectively.

          * field—A field in the input feature attribute table.

          * {variable}—The netCDF variable name.

          * {units}—The units of the data represented by the field.
      fields_to_dimensions {Value Table}:
          The field or fields used to create dimensions in the netCDF file.

          * field—A field in the input feature attribute table.

          * {dimension}—The netCDF dimension name.

          * {units}—The units of the data represented by the field.

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The filename must have a .nc extension."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.FeatureToNetCDF_md(*gp_fixargs((in_features, fields_to_variables, out_netCDF_file, fields_to_dimensions), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeNetCDFFeatureLayer_md', None)
def MakeNetCDFFeatureLayer(in_netCDF_file=None, variable=None, x_variable=None, y_variable=None, out_feature_layer=None, row_dimension=None, z_variable=None, m_variable=None, dimension_values=None, value_selection_method=None):
    """MakeNetCDFFeatureLayer_md(in_netCDF_file, variable;variable..., x_variable, y_variable, out_feature_layer, {row_dimension;row_dimension...}, {z_variable}, {m_variable}, {dimension_values;dimension_values...}, {value_selection_method})

        Makes a feature layer from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The netCDF variable, or variables, that will be added as fields in the feature
          attribute table.
      x_variable (String):
          A netCDF coordinate variable used to define the x, or longitude, coordinates of
          the output layer.
      y_variable (String):
          A netCDF coordinate variable used to define the y, or latitude, coordinates of
          the output layer.
      row_dimension {String}:
          The netCDF dimension, or dimensions, used to create features with unique values
          in the feature layer. The dimension or dimensions set here determine the number
          of features in the feature layer and the fields that will be presented in the
          feature layer's attribute table.For instance, if StationID is a dimension in the
          netCDF file and has 10 values,
          by setting StationID as the dimension to use, 10 features will be created (10
          rows will be created in the feature layer's attribute table). If StationID and
          time are used, and there are 3 time slices, 30 features will be created (30 rows
          will be created in the feature layer's attribute table). If you will be
          animating the netCDF feature layer, it is recommended, for efficiency reasons,
          to not set time as a row dimension. Time will still be available as a dimension
          that you can set to animate through, but the attribute table will not store this
          information.
      z_variable {String}:
          A netCDF variable used to specify elevation values (z-values) for features.
      m_variable {String}:
          A netCDF variable used to specify linear measurement values (m-values) for
          features.
      dimension_values {Value Table}:
          The value (such as 01/30/05) of the dimension (such as Time) or dimensions to
          use when displaying the variable in the output layer. By default, the first
          value of the dimension or dimensions will be used. This default value can also
          be altered on the netCDF tab of the Layer Properties dialog box.
      value_selection_method {String}:
          Specifies the dimension value selection method.

          * BY_VALUE— The input value is matched with the actual dimension value.

          * BY_INDEX— The input value is matched with the position or index of a dimension
          value. The index is 0 based, that is, the position starts at 0.

     OUTPUTS:
      out_feature_layer (Feature Layer):
          The name of the output feature layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeNetCDFFeatureLayer_md(*gp_fixargs((in_netCDF_file, variable, x_variable, y_variable, out_feature_layer, row_dimension, z_variable, m_variable, dimension_values, value_selection_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeNetCDFRasterLayer_md', None)
def MakeNetCDFRasterLayer(in_netCDF_file=None, variable=None, x_dimension=None, y_dimension=None, out_raster_layer=None, band_dimension=None, dimension_values=None, value_selection_method=None):
    """MakeNetCDFRasterLayer_md(in_netCDF_file, variable, x_dimension, y_dimension, out_raster_layer, {band_dimension}, {dimension_values;dimension_values...}, {value_selection_method})

        Makes a raster layer from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The variable of the netCDF file used to assign cell values to the output raster.
          This is the variable that will be displayed, such as temperature or rainfall.
      x_dimension (String):
          A netCDF dimension used to define the x, or longitude, coordinates of the output
          layer.
      y_dimension (String):
          A netCDF dimension used to define the y, or latitude, coordinates of the output
          layer.
      band_dimension {String}:
          A netCDF dimension used to create bands in the output raster. Set this dimension
          if a multiband raster layer is required. For instance, altitude might be set as
          the band dimension to create a multiband raster where each band represents
          temperature at that altitude.
      dimension_values {Value Table}:
          The value (such as 01/30/05) of the dimension (such as Time) or dimensions to
          use when displaying the variable in the output layer. By default, the first
          value of the dimension or dimensions will be used. This default value can also
          be altered on the netCDF tab of the Layer Properties dialog box.
      value_selection_method {String}:
          Specifies the dimension value selection method.

          * BY_VALUE— The input value is matched with the actual dimension value.

          * BY_INDEX— The input value is matched with the position or index of a dimension
          value. The index is 0 based, that is, the position starts at 0.

     OUTPUTS:
      out_raster_layer (Raster Layer):
          The name of the output raster layer."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeNetCDFRasterLayer_md(*gp_fixargs((in_netCDF_file, variable, x_dimension, y_dimension, out_raster_layer, band_dimension, dimension_values, value_selection_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('MakeNetCDFTableView_md', None)
def MakeNetCDFTableView(in_netCDF_file=None, variable=None, out_table_view=None, row_dimension=None, dimension_values=None, value_selection_method=None):
    """MakeNetCDFTableView_md(in_netCDF_file, variable;variable..., out_table_view, {row_dimension;row_dimension...}, {dimension_values;dimension_values...}, {value_selection_method})

        Makes a table view from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The netCDF variable, or variables, used to create fields in the table view.
      row_dimension {String}:
          The netCDF dimension, or dimensions, used to create fields populated with unique
          values in the table view. The dimension, or dimensions, set here determine the
          number of rows in the table view and the fields that will be present.For
          instance, if stationID is a dimension in the netCDF file and has 10 values,
          by setting stationID as the dimension to use, 10 rows will be created in the
          table view. If stationID and time are used and there are 3 time slices, 30 rows
          will be created in the table view.
      dimension_values {Value Table}:
          A set of dimension-value pairs used to specify a slice of a multidimensional
          variable.
      value_selection_method {String}:
          Specifies the dimension value selection method.

          * BY_VALUE— The input value is matched with the actual dimension value.

          * BY_INDEX— The input value is matched with the position or index of a dimension
          value. The index is 0 based, that is, the position starts at 0.

     OUTPUTS:
      out_table_view (Table View):
          The name of the output table view."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.MakeNetCDFTableView_md(*gp_fixargs((in_netCDF_file, variable, out_table_view, row_dimension, dimension_values, value_selection_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('RasterToNetCDF_md', None)
def RasterToNetCDF(in_raster=None, out_netCDF_file=None, variable=None, variable_units=None, x_dimension=None, y_dimension=None, band_dimension=None, fields_to_dimensions=None):
    """RasterToNetCDF_md(in_raster, out_netCDF_file, {variable}, {variable_units}, {x_dimension}, {y_dimension}, {band_dimension}, {fields_to_dimensions;fields_to_dimensions...})

        Converts a raster dataset to a netCDF file.

     INPUTS:
      in_raster (Raster Layer / Raster Catalog):
          The input raster dataset or raster catalog.
      variable {String}:
          The netCDF variable name that will be used in the output netCDF file. This
          variable will contain the values of cells in the input raster.
      variable_units {String}:
          The units of the data contained within the variable. The variable name is
          specified in the Variable parameter.
      x_dimension {String}:
          The netCDF dimension name used to specify x, or longitude, coordinates.
      y_dimension {String}:
          The netCDF dimension name used to specify y, or latitude, coordinates.
      band_dimension {String}:
          The netCDF dimension name used to specify bands.
      fields_to_dimensions {Value Table}:
          The field or fields used to create dimensions in the netCDF file.

          * field—A field in the input raster attribute table.

          * {dimension}—The netCDF dimension name.

          * {units}—The units of the data represented by the field.

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The filename must have a .nc extension."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.RasterToNetCDF_md(*gp_fixargs((in_raster, out_netCDF_file, variable, variable_units, x_dimension, y_dimension, band_dimension, fields_to_dimensions), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('SelectByDimension_md', None)
def SelectByDimension(in_layer_or_table=None, dimension_values=None, value_selection_method=None):
    """SelectByDimension_md(in_layer_or_table, {dimension_values;dimension_values...}, {value_selection_method})

        Updates the netCDF layer display or netCDF table view based on the dimension
        value.

     INPUTS:
      in_layer_or_table (Raster Layer / Feature Layer / Table View / Mosaic Layer):
          The input netCDF raster layer, netCDF feature layer, or netCDF table view.
      dimension_values {Value Table}:
          A set of dimension-value pairs used to specify a slice of a multidimensional
          variable.

          * dimension—A netCDF dimension.

          * {value}—A value of the dimension to specify a slice of a multidimensional
          variable.
      value_selection_method {String}:
          Specifies the dimension value selection method.

          * BY_VALUE— The input value is matched with the actual dimension value.

          * BY_INDEX— The input value is matched with the position or index of a dimension
          value. The index is 0 based, that is, the position starts at 0."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.SelectByDimension_md(*gp_fixargs((in_layer_or_table, dimension_values, value_selection_method), True)))
        return retval
    except Exception, e:
        raise e

@gptooldoc('TableToNetCDF_md', None)
def TableToNetCDF(in_table=None, fields_to_variables=None, out_netCDF_file=None, fields_to_dimensions=None):
    """TableToNetCDF_md(in_table, fields_to_variables;fields_to_variables..., out_netCDF_file, {fields_to_dimensions;fields_to_dimensions...})

        Converts a table to a netCDF file.

     INPUTS:
      in_table (Table View):
          The input table.
      fields_to_variables (Value Table):
          The field or fields used to create variables in the netCDF file.

          * field—A field in the input feature attribute table.

          * {variable}—The netCDF variable name.

          * {units}—The units of the data represented by the field.
      fields_to_dimensions {Value Table}:
          The field or fields used to create dimensions in the netCDF file.

          * field—A field in the input table.

          * {dimension}—The netCDF dimension name.

          * {units}—The units of the data represented by the field.

     OUTPUTS:
      out_netCDF_file (File):
          The output netCDF file. The filename must have a .nc extension."""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.TableToNetCDF_md(*gp_fixargs((in_table, fields_to_variables, out_netCDF_file, fields_to_dimensions), True)))
        return retval
    except Exception, e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject