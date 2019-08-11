from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from taxes.calculator import federal
from taxes.forms import TaxForm


def tax_form(request):
  if request.method == 'POST':
    form = TaxForm(request.POST)
  else:
    form = TaxForm()
  return render(request, 'taxes.html', {'form': form})

@api_view(['GET'])
def tax_calculator(request, format=None):
  income = int(request.GET.get('income'))
  taxes = federal(income)
  return JsonResponse({
    'After Tax Income': income - taxes,
    'Federal Taxes': taxes
  })
