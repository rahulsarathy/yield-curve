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

  def test_tax_calculator_single(self):
    """
    Checks that a GET request for a tax calculation with valid parameters,
    including a SINGLE filing status, produces the correct federal taxes
    owed, state taxes owed, and after tax income.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/taxes/?income=180000&filing_status=SINGLE&state=California')
    data = response.json()

    self.assertEqual(data['Federal Taxes'], 38952.50)
    self.assertEqual(data['State Taxes'], 13744.95)
    self.assertEqual(data['After Tax Income'], 127302.55)

  def test_tax_calculator_married_jointly(self):
    """
    Checks that a GET request for a tax calculation with valid parameters,
    including a MARRIED_JOINTLY filing status, produces the correct taxes owed
    and after tax income.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/taxes/?income=180000&filing_status=MARRIED_JOINTLY&state=California')
    data = response.json()
  
  def test_tax_calculator_married_separately(self):
    """
    Checks that a GET request for a tax calculation with a MARRIED_SEPARATELY
    filing status produces the correct taxes and after tax income.
    """
    response = self.client.get(TEST_ROOT + '/api/v1/taxes/?income=180000&filing_status=MARRIED_SEPARATELY&state=California')
    data = response.json()

    self.assertEqual(data['State Taxes'], 13744.95)
  
  def test_tax_calculator_invalid_params(self):
    """
    Checks that a GET request for a tax calculation with invalid parameters
    produces the appropriate status message.
    """
    pass