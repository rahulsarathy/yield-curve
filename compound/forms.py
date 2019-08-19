from django import forms


GROWTH_CHOICES = (
  (1.01, '1%'),
  (1.02, '2%'),
  (1.03, '3%'),
  (1.04, '4%'),
  (1.05, '5%'),
  (1.06, '6%'),
  (1.07, '7%'),
  (1.08, '8%'),
  (1.09, '9%'),
  (1.10, '10%')
)

class CompoundCalculatorForm(forms.Form):
  initial_value = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
  monthly_contribution = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control mb-4'}))
  annual_growth = forms.CharField(widget=forms.Select(choices=GROWTH_CHOICES, attrs={'class': 'form-control mb-4'}))
