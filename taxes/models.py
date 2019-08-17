from __future__ import unicode_literals
from django.db import models


class TaxBracket(models.Model):
  """
  Encapsulates information regarding a specific tax bracket, state or federal.
  """
  
  # The authority imposing the taxation, e.g. United States, California, etc.
  state = models.CharField(max_length=32)

  # The tax filing status, e.g. single, married filing jointly, etc.
  filing_status = models.CharField(max_length=64)

  # The type of tax levied, e.g. income, long term capital gains, etc.
  tax_type = models.CharField(max_length=16)

  # The percentage rate charged on the tax bracket.
  rate = models.FloatField()

  # The minimum dollar amount required to be placed within this tax bracket.
  minimum = models.IntegerField()
