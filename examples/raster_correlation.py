from geobricks_raster_correlation.core.raster_correlation_core import get_correlation

raster_path1 = "../test_data/morocco/wheat_actual_biomprod_201010_doukkala.tif"
raster_path2 = "../test_data/morocco/wheat_potential_biomprod_201010_doukkala.tif"
bins = 300
print get_correlation(raster_path1, raster_path2, bins)

# in output there will be
# "series" to be used in Highcharts or in any other chart engine
# and "stats" providing i.e.:
# {
#   'slope': 0.7796536375115416,
#   'p_value': 0.0,
#   'std_err': 0.00043888022938107468,
#   'intercept': 335.40514545887174,
#   'r_value': 0.88488086004672395
# }
