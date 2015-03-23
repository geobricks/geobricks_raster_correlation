import numpy as np
import gdal
import time
from pysal.esda import mapclassify
from scipy.stats import linregress
from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import get_raster_path
from geobricks_raster_correlation.core.colors import get_colors

log = logger(__file__)


def get_correlation_json(obj):
    try:
        raster = obj["raster"]
        raster_path1 = get_raster_path(raster[0])
        raster_path2 = get_raster_path(raster[1])
        bins = 300
        intervals = 6
        color_ramp = 'Reds'
        if "stats" in obj:
            if "correlation" in obj["stats"]:
                o = obj["stats"]["correlation"]
                if "bins" in o: bins = o["bins"]
                if "intervals" in o: intervals = o["intervals"]
                if "color_ramp" in o: color_ramp = o["colorRamp"]

        return get_correlation(raster_path1, raster_path2, bins, intervals, color_ramp)
    except Exception, e:
        raise Exception(e)


def get_correlation(raster_path1, raster_path2, bins=300, intervals=6, color_ramp='Reds', reverse=False, min1=None, max1=None, min2=None, max2=None, band1=1, band2=1, classification_type="Jenks_Caspall"):

    ds1 = gdal.Open(raster_path1)
    ds2 = gdal.Open(raster_path2)

    if bins is None:
        bins = 300

    if _check_raster_equal_size(ds1, ds2):
        band1 = ds1.GetRasterBand(band1)
        array1 = np.array(band1.ReadAsArray()).flatten()
        nodata1 = band1.GetNoDataValue()

        band2 = ds2.GetRasterBand(band2)
        array2 = np.array(band2.ReadAsArray()).flatten()
        nodata2 = band2.GetNoDataValue()

        # min/max calulation
        # TODO: check if min and max are not passed and they have to be computed or not
        (min1_computed, max1_computed) = band1.ComputeRasterMinMax(0)
        (min2_computed, max2_computed) = band2.ComputeRasterMinMax(0)
        if min1 is None: min1 = min1_computed
        if max1 is None: max1 = max1_computed
        if min2 is None: min2 = min2_computed
        if max2 is None: max2 = max2_computed

        # this is useful? In theory should be enough the min1 and min2
        #if forced_min1 is None: forced_min1 = min1
        #if forced_min2 is None: forced_min2 = min2

        # Calculation of the frequencies
        statistics = compute_frequencies(array1, array2, min1, min2, max1, max2, nodata1, nodata2, bins)
        series = get_series(statistics["scatter"].values(), intervals, color_ramp, reverse, classification_type)

        result = dict()
        # probably not useful for the chart itself
        # result['min1'] = min1,
        # result['max1'] = max1,
        # result['min2'] = min2,
        # result['max2'] = max2,
        result["series"] = series
        result["stats"] = statistics["stats"]

        # is it useful to remove them from the memory?
        del ds1, ds2, array1, array2
        return result


def _check_raster_equal_size(ds1, ds2):
    rows1 = ds1.RasterYSize; cols1 = ds1.RasterXSize
    rows2 = ds2.RasterYSize; cols2 = ds2.RasterXSize
    if cols1 != cols2 or rows1 != rows2:
        return False
        log.error("%sx%s %sx%s" % (rows1, cols1, rows2, cols2))
        raise Exception("The rasters cannot be processed because they have different dimensions", 400)
    return True


def process_correlation(array1, array2, bins=300, add_stats=True, add_series=True):
    d = dict()
    try:
        # TODO: move it from here: calculation of the regression coeffient
        # TODO: add a boolean to check if it's need the computation of the coeffifcients
        if add_stats:
            slope, intercept, r_value, p_value, std_err = linregress(array1, array2)
            d["stats"] = {
                "slope": slope,
                "intercept": intercept,
                "r_value": r_value,
                "p_value": p_value,
                "std_err": std_err
            }
        if add_series:
            d["scatter"] = {}
            heatmap, xedges, yedges = np.histogram2d(array1, array2, bins)
            for x in range(0, len(xedges)-1):
                for y in range(0, len(yedges)-1):
                    if heatmap[x][y] > 0:
                        # print heatmap[x][y], xedges[x], yedges[y]
                        d["scatter"][str(xedges[x]) + "_" + str(yedges[y])] = {
                            "data": [xedges[x], yedges[y]],
                            "freq": heatmap[x][y]
                        }

        # print d
        log.info("Correlation computation End")
        return d
    except Exception, e:
        log.error(e)
        raise Exception(e, 400)


def compute_frequencies(array1, array2, min1, min2, max1, max2, nodata1=None, nodata2=None, bins=300):

    index1 = (array1 > min1) & (array1 <= max1) & (array1 != nodata1)
    index2 = (array1 > min2) & (array2 <= max2) & (array2 != nodata2)

    # merge array indexes
    compound_index = index1 & index2
    del index1, index2

    # it creates two arrays from the two original arrays
    array1 = array1[compound_index]
    array2 = array2[compound_index]

    # processing data
    d = process_correlation(array1, array2, bins)

    # is it useful?
    del array1, array2
    return d


# TODO: move it
def classify_values(values, k=5, classification_type="Jenks_Caspall"):
    # TODO: use a "switch" between the variuos classification types, Problem: they have different inputs and outputs (move to a classification file python file instead of here)
    start_time = time.time()
    #result = mapclassify.quantile(values, k)

    #print values
    #start_time = time.time()
    array = np.array(values)
    result = mapclassify.Jenks_Caspall_Forced(array, k)
    log.info("Classification done in %s seconds ---" % str(time.time() - start_time))
    #return result
    return result.bins


def get_series(values, intervals, color_ramp, reverse=False, classification_type="Jenks_Caspall"):
    classification_values = []
    for v in values:
        classification_values.append(float(v['freq']))

    classes = classify_values(classification_values, intervals, classification_type)

    # TODO: get colors
    colors = get_colors(color_ramp, intervals, reverse)

    # creating series
    series = []
    for color in colors:
        #print color
        series.append({
            "color": color,
            "data": []
        })

    #classes
    for v in values:
        freq = v['freq']
        for i in range(len(classes)):
            if freq <= classes[i]:
                series[i]['data'].append([float(v['data'][0]), float(v['data'][1])])
                break
    return series