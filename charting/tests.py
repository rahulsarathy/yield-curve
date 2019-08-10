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
