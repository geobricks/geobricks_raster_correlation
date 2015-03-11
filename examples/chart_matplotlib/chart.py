from geobricks_raster_correlation.core.raster_correlation_core import get_correlation
from matplotlib import pyplot as plt
from matplotlib.pylab import polyfit, polyval

# input to your raster files
raster_path1 = "../../test_data/morocco/wheat_actual_biomprod_201010_doukkala.tif"
raster_path2 = "../../test_data/morocco/wheat_potential_biomprod_201010_doukkala.tif"

# Number of sampling bins
bins = 150

corr = get_correlation(raster_path1, raster_path2, bins)
x = []
y = []
colors = []
#print corr['series']
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