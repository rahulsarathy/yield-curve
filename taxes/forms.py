from django import forms


FILING_STATUSES = (
  ('SINGLE', 'Single'),
  ('MARRIED_JOINTLY', 'Married Filing Jointly'),
  ('MARRIED_SEPARATELY', 'Married Filing Separately'),  
  ('HEAD_OF_HOUSEHOLD', 'Head of Household'),
  ('QUALIFYING_WIDOW', 'Qualifying Widow(er)'),
)

STATES = (
  ('Alabama', 'Alabama'),
  ('Arizona', 'Arizona'),
  ('California', 'California'),
)


class TaxForm(forms.Form):
  income = forms.IntegerField(label='Annual Gross Income (AGI)', widget=forms.NumberInput(attrs={'class': 'form-control mb-4'}))
  filing_status = forms.CharField(widget=forms.Select(choices=FILING_STATUSES, attrs={'class': 'form-control mb-4'}))
  state = forms.CharField(widget=forms.Select(choices=STATES, attrs={'class': 'form-control mb-4'}))
