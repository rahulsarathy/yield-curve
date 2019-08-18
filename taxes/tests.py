from rest_framework.test import APITestCase
from taxes.models import TaxBracket


TEST_ROOT = 'http://localhost:8000'


class TaxCalculatorTests(APITestCase):
  def setUp(self):
    """Set up the federal and California tax brackets for testing."""

    # Federal tax brackets
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.1, minimum=0)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.12, minimum=9700)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.22, minimum=39475)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.24, minimum=84200)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.32, minimum=160275)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.35, minimum=204100)
    TaxBracket.objects.create(state='United States', filing_status='SINGLE', tax_type='INCOME', rate=0.37, minimum=510300)

    # California tax brackets
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.01, minimum=0)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.02, minimum=8223)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.03, minimum=19495)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.04, minimum=30769)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.08, minimum=42711)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.093, minimum=53980)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.103, minimum=275738)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.113, minimum=330884)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.123, minimum=551473)
    TaxBracket.objects.create(state='California', filing_status='SINGLE', tax_type='INCOME', rate=0.133, minimum=1000000)

    # 46,"California","SINGLE","INCOME",0.01,0
    # 47,"California","SINGLE","INCOME",0.02,8223
    # 48,"California","SINGLE","INCOME",0.029999999999999,19495
    # 49,"California","SINGLE","INCOME",0.04,30769
    # 50,"California","SINGLE","INCOME",0.08,42711
    # 51,"California","SINGLE","INCOME",0.092999999999999,53980
    # 52,"California","SINGLE","INCOME",0.102999999999999,275738
    # 53,"California","SINGLE","INCOME",0.113,330884
    # 54,"California","SINGLE","INCOME",0.123,551473
    # 55,"California","SINGLE","INCOME",0.133,1000000

  def test_tax_calculator(self):
    """
    Checks that a GET request for a tax calculation with valid parameters
    produces the appropriate federal taxes owed and after tax income.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/taxes/?income=180000&filing_status=SINGLE&state=California')
    data = response.json()

    self.assertEqual(data['Federal Taxes'], 38952.50)
    self.assertEqual(data['State Taxes'], 13744.95)
    self.assertEqual(data['After Tax Income'], 127302.55)
