# TODO(rsarathy): What does this do?

from __future__ import unicode_literals
from django.db import models


class BondYield(models.Model):
  date = models.DateField()
  one_month = models.FloatField(null=True)
  two_month = models.FloatField(null=True)
  three_month = models.FloatField(null=True)
  six_month = models.FloatField(null=True)
  one_year = models.FloatField(null=True)
  two_year = models.FloatField(null=True)
  three_year = models.FloatField(null=True)
  five_year = models.FloatField(null=True)
  seven_year = models.FloatField(null=True)
  ten_year = models.FloatField(null=True)
  twenty_year = models.FloatField(null=True)
  thirty_year = models.FloatField(null=True)
