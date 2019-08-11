from django import forms


class TaxForm(forms.Form):
  income = forms.IntegerField(label='Annual Gross Income (AGI)')
