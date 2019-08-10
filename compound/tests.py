from rest_framework import status
from rest_framework.test import APITestCase


TEST_ROOT = 'http://localhost:8000'


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
