import unittest
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation

raster_path1 = "../test_data/morocco/wheat_actual_biomprod_201010_doukkala.tif"
raster_path2 = "../test_data/morocco/wheat_potential_biomprod_201010_doukkala.tif"
bins = 300


class GeobricksUnitTest(unittest.TestCase):

    def test_correlation(self):
        corr = get_correlation(raster_path1, raster_path2, 3)
        self.assertEqual(corr["stats"]["r_value"], 0.88488086004672395)
