Geobricks Raster Correlation
====================

The Geobricks Raster Correlation library provides an easy way correlate two raster of the same size, returning a json containing statistical outputs and frequencies information to be used directly with Highcharts JS library.

# Installation

The library is distributed through PyPi and can be installed by typing the following command in the console:
```
pip install GeobricksRasterCorrelation
```
# Examples

## Library usage

```python
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation

raster_path1 = "path_to_raster1.tif"
raster_path2 = "path_to_raster2.tif"
# Number of bins to be applied to the scatter chart
bins = 300
corr = get_correlation(raster_path1, raster_path2, bins)
print corr
```

The returned json contains:
 
 * in corr['stats'] the statistics: slope, p_value, std_err, intercept, r_value
 * in corr['series'] there are the series. The series output can be used directly as an input with Highcharts. 
