from rest_framework.test import APITestCase


TEST_ROOT = 'http://localhost:8000'


class TaxCalculatorTests(APITestCase):
  def test_tax_calculator(self):
    """
    Checks that a GET request for a tax calculation with valid parameters
    produces the appropriate federal taxes owed and after tax income.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/taxes/?income=10000')
    data = response.json()

    self.assertEqual(data['Federal Taxes'], 1006)
    self.assertEqual(data['After Tax Income'], 8994)
