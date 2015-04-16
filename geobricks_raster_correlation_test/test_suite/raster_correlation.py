import unittest
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation

raster_path1 = "../../test_data/geoserver_data_dir/data/workspace/wheat_actual_biomprod_201010_doukkala/wheat_actual_biomprod_201010_doukkala.geotiff"
raster_path2 = "../../test_data/geoserver_data_dir/data/workspace/wheat_potential_biomprod_201010_doukkala/wheat_potential_biomprod_201010_doukkala.geotiff"
bins = 300


class GeobricksTest(unittest.TestCase):

    def test_correlation(self):
        corr = get_correlation(raster_path1, raster_path2, bins)
        print corr["stats"]
        self.assertEqual(corr["stats"]["r_value"], 0.88488086004672395)


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()