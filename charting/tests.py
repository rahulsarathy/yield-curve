# Tests the functionality of the underlying API responsible for serving
# yield curve data.

import datetime
import requests
from charting.models import BondYield
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.test import APITestCase


# URL root for all test cases.
TEST_ROOT = 'http://localhost:8000'


class BondYieldTests(APITestCase):
  def setUp(self):
    """Arrange a small subset of bond yield data for testing purposes."""
    
    # Set up a testing client for verifying the behavior of GET requests.
    BondYield.objects.create(date=datetime.date(1995, 10, 18), two_year=5.6)
    BondYield.objects.create(date=datetime.date(1997, 11, 7), one_year=4.4, three_year=4.7)
    BondYield.objects.create(date=datetime.date(2019, 7, 3), one_month=2.1)

  def test_get_bond_yield_data(self):
    """
    Checks that a GET request for a valid series of bond yield data produces
    the appropriate records.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/bond_yield/20190703', format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['date'], '2019-07-03')
    self.assertAlmostEqual(response.data['one_month'], 2.1)

  def test_get_bond_yield_not_found(self):
    """
    Checks that a GET request for a nonexistent record of bond yield data
    returns a 404 not found error.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/bond_yield/20190704', format='json')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CompoundCalculatorTests(APITestCase):
  def test_compound_calculator(self):
    """
    Checks that a GET request for a compound calculation with valid parameters
    produces the appropriate 1 year, 10 year, and 30 year values.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/compound_calculator/?initial_value=1000&monthly_contribution=100&annual_growth=1.08')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    data = response.json()

    # At the start, the total deposits should be equal to the initial deposit,
    # and the total return should be 0.
    self.assertEqual(data['0 years']['Deposits'], 1000)
    self.assertEqual(data['0 years']['Return'], 0)

    # 1 year
    self.assertEqual(data['1 years']['Deposits'], 2200)
    self.assertEqual(data['1 years']['Return'], 123.39)

    # 10 years
    self.assertEqual(data['10 years']['Deposits'], 13000)
    self.assertEqual(data['10 years']['Return'], 7171.35)

    # 30 years
    self.assertEqual(data['30 years']['Deposits'], 37000)
    self.assertEqual(data['30 years']['Return'], 113917.72)
