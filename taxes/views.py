from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from taxes.calculator import marginal_tax
from taxes.forms import TaxForm
from taxes.models import TaxBracket


def tax_form(request):
  if request.method == 'POST':
    form = TaxForm(request.POST)
  else:
    form = TaxForm()
  return render(request, 'taxes.html', {'form': form})

@api_view(['GET'])
def tax_calculator(request, format=None):
  income = int(request.GET.get('income'))
  status = request.GET.get('filing_status')
  state = request.GET.get('state')
  # print('State:', state)
  # print('status:', status)
  # taxes = federal(income)

  minimums, rates = [], []
  brackets = TaxBracket.objects.filter(state=state, filing_status=status)
  for b in brackets:
    minimums.append(b.minimum)
    rates.append(b.rate)
  minimums.sort()
  rates.sort()
  # print(minimums)
  # print(rates)
  state_taxes = marginal_tax(rates, minimums, income)
  # print('State Taxes:', state_taxes)

  fed_min, fed_rates = [], []
  brackets = TaxBracket.objects.filter(state='United States', filing_status=status)
  for b in brackets:
    fed_min.append(b.minimum)
    fed_rates.append(b.rate)
  fed_min.sort()
  fed_rates.sort()
  fed_taxes = marginal_tax(fed_rates, fed_min, income)

  return JsonResponse({
    'After Tax Income': round(income - state_taxes - fed_taxes, 2),
    'Federal Taxes': fed_taxes,
    'State Taxes': state_taxes,
  })
