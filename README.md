Geobricks Raster Correlation
====================

The library provides an easy way correlate raster of the same size. It returns a json containing statistical outputs and frequencies information to be directly used with Highcharts JS library.

# Installation

## Dependencies

The library has different dependencies (see also requirements.txt) click, watchdog, flask, flask-cors, numpy, scipy, pysal, brewer2mpl, rasterio, GeobricksCommon

## On linux (ubuntu)

```bash
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get -y install python-numpy libgdal1h gdal-bin libgdal-dev
```

In case of compiling errors for numpy
```bash
sudo apt-get -y install libblas3gf libc6 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran python-all-dev libatlas-base-dev python-dev
```

In case of compiling errors for scipy
```bash
sudo apt-get -y install libblas-dev liblapack-dev
```

The library is distributed through PyPi and can be installed by typing the following command in the console:
```
sudo pip install GeobricksRasterCorrelation
```

**N.B.** Due to a well known PyPi issue it's not possible to install scipy and pysal through setup.py or requirements.txt 

In order to install pysal run the following command
```bash
sudo pip install pysal
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
