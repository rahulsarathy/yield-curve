import csv
from taxes.models import TaxBracket
from django.core.management.base import BaseCommand


class Command(BaseCommand):
  help = 'Builds all of the state and federal tax brackets from a given csv file.'

  def add_arguments(self, parser):
    parser.add_argument('brackets_file', type=str, help='The .csv file with all of the tax bracket data.')

  def handle(self, *args, **options):
    with open(kwargs['brackets_file']) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        bracket = TaxBracket()
        bracket.state = row['state']
        bracket.filing_status = row['filing_status']
        bracket.tax_type = row['tax_type']
        bracket.rate = float(row['rate'])
        bracket.minimum = int(row['minimum'])
        bracket.save()
