import unittest
import time
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation
from geobricks_raster_correlation.core.raster_correlation_core_gdal import get_correlation as get_correlation2

raster_path1 = "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/3857_display_only/CH4_Emissions_Burning_Savanna/CH4_GFED4BA_Emissions_Burning_Savanna_2003_3857.tif"
raster_path2 = "/home/vortex/Desktop/LAYERS/ghg/geodata_handedoverto_simonem/3857_display_only/CH4_Emissions_Burning_Savanna/CH4_GFED4BA_Emissions_Burning_Savanna_2003_3857.tif"
bins = 300


class GeobricksTest(unittest.TestCase):

    def test_correlation(self):
        start_time = time.time()
        corr = get_correlation(raster_path1, raster_path2, bins)
        print "rasterio) " + str(time.time() - start_time)
        # print corr["stats"]
        # self.assertEqual(corr["stats"]["r_value"], 0.88488086004672395)

    def test_correlation2(self):
        start_time = time.time()
        corr = get_correlation2(raster_path1, raster_path2, bins)
        # print corr["stats"]
        # self.assertEqual(corr["stats"]["r_value"], 0.88488086004672395)
        print "gdal) " + str(time.time() - start_time)


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()