Raster Correlation
====================

The library provides an easy way correlate raster of the same size. It returns a json containing statistical outputs and frequencies information to be directly used with Highcharts JS or Matplotlib chart libraries.

# Installation

## Dependencies

The library has different dependencies (see also requirements.txt) click, watchdog, flask, flask-cors, numpy, scipy, pysal, brewer2mpl, rasterio, GeobricksCommon.

## On Ubuntu

```bash
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get install python-numpy libgdal1h gdal-bin libgdal-dev
```

In case of compiling errors for numpy
```bash
sudo apt-get install libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev python-dev
```

In case of compiling errors for scipy
```bash
sudo apt-get install libblas-dev liblapack-dev
```

## Installation

The library is distributed through PyPi and can be installed by typing the following commands in the console:
```
pip -r https://raw.githubusercontent.com/geobricks/geobricks_raster_correlation/master/requirements.txt

pip install GeobricksRasterCorrelation
```

**N.B.** Due to a well known PyPi issue it's not possible to install scipy and pysal through setup.py or requirements.txt 

In order to install pysal run the following command
```bash
pip install pysal
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

## Example with matplotlib

This example generate a correlation chart with matplotlib

```python
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation
from matplotlib import pyplot as plt
from matplotlib.pylab import polyfit, polyval

# input to your raster files
raster_path1 = "path_to_raster1.tif"
raster_path2 = "path_to_raster2.tif"

# Number of sampling bins
bins = 150

corr = get_correlation(raster_path1, raster_path2, bins)
x = []
y = []
colors = []
# print corr['series']
for serie in corr['series']:
    colors.append(serie['color'])
    for data in serie['data']:
        x.append(data[0])
        y.append(data[1])

# Adding regression line
(m, b) = polyfit(x, y, 1)
yp = polyval([m, b], x)
plt.plot(x, yp)

# plotting scatter
plt.scatter(x, y, c=colors)
plt.show()
```

The returned json:
 
 * corr['stats']  contains the statistics: slope, p_value, std_err, intercept, r_value
 * corr['series'] contains the output series that can be used directly as an Highcharts input or with Matplotlib.
