import unittest
import math
import numpy as np
from main.CONSTANTS import CONSTANTS
from main.Portfolio import Portfolio


# Input data for the unit test
returns_per_day = 78
in_sample_period = (0*returns_per_day, 50*returns_per_day)
out_of_sample_period = (0 * returns_per_day, 1 * returns_per_day)
returns_csv_directory = CONSTANTS['returns_data']
actual_out_of_sample_periods = (in_sample_period[1] + out_of_sample_period[0],
                                            in_sample_period[1] + out_of_sample_period[1])


class Test_Portfolio(unittest.TestCase):
    """
    The Unit Test tests the major function used in covariance matrix constructions and the predictor
    """

    def test_compute_empirical_covariance_matrix(self):
        """
        This Unit Test is to test if the empirical covariance matrix shape is as expected, the shape should be same as
        the number of assets * number of assets
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        expected_shape = (portfolio.get_number_of_assets(), portfolio.get_number_of_assets())
        portfolio.compute_empirical_covariance_matrix()
        self.assertEqual(portfolio._empirical_covariance_matrix.shape, expected_shape)


    def test_compute_clipped_covariance_matrix(self):
        """
        This Unit Test is to test if the clipped_covariance_matrix shape is as expected, the shape should be same as
        the number of assets * number of assets
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        expected_shape = (portfolio.get_number_of_assets(), portfolio.get_number_of_assets())
        portfolio.compute_clipped_covariance_matrix()
        self.assertEqual(portfolio._clipped_covariance_matrix.shape, expected_shape)


    def test_compute_optimal_shrinkage_covariance_matrix(self):
        """
        This Unit Test is to test if the optimal_shrinkage_covariance_matrix shape is as expected, the shape should be same as
        the number of assets * number of assets
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        expected_shape = (portfolio.get_number_of_assets(), portfolio.get_number_of_assets())
        portfolio.compute_optimal_shrinkage_covariance_matrix()
        self.assertEqual(portfolio._optimal_shrinkage_covariance_matrix.shape, expected_shape)


    def test_compute_exponential_weighted_covariance_matrix(self):
        """
        This Unit Test is to test if the exponentially_weighted_covariance_matrix shape is as expected, the shape should be same as
        the number of assets * number of assets
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        expected_shape = (portfolio.get_number_of_assets(), portfolio.get_number_of_assets())
        portfolio.compute_filtered_exponentially_weighted_covariance_matrix()
        self.assertEqual(portfolio._exponentially_weighted_covariance_matrix.shape, expected_shape)


    def test_minimum_variance_predictor(self):
        """
        This Unit Test is to test if the sum of all predictors are as expected, should be equal to the number of asset
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        self.assertEqual(sum(portfolio.minimum_variance_predictor())[0], portfolio.get_number_of_assets())


    def test_random_long_short_predictor(self):
        """
        This Unit Test is to test if the norm is as expected, should be equal to the square root of the number of asset
        """
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        self.assertAlmostEqual(np.linalg.norm(portfolio.random_long_short_predictor()), math.sqrt(portfolio.get_number_of_assets()), delta=0.01)


    def test_compute_bias_statistics_Zt(self):
        """
        This Unit Test is to test if the statistics_Zt is as expected, should be equal to 1
        """
        covariance_matrix_type = 'Empirical'
        portfolio = Portfolio(in_sample_period, actual_out_of_sample_periods, returns_csv_directory)
        portfolio.compute_empirical_covariance_matrix()
        portfolio.compute_inverse_covariance_matrix('Empirical')
        portfolio.compute_predictors('Minimum-variance')
        portfolio.compute_optimal_weights()
        self.assertAlmostEqual(portfolio.compute_bias_statistics_Zt(covariance_matrix_type), 1, delta=0.01)
        

if __name__ == "__main__":
    unittest.main()