from compound.calculator import monthly
from compound.forms import CompoundCalculatorForm
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view


THIRTY = 30


def compound_form(request):
  if request.method == 'POST':
    form = CompoundCalculatorForm(request.POST)
  else:
    form = CompoundCalculatorForm()
  return render(request, 'compound.html', {'form': form})

@api_view(['GET'])
def compound_calculator(request, format=None):
  initial = int(request.GET.get('initial_value'))
  contribution = int(request.GET.get('monthly_contribution'))
  growth = float(request.GET.get('annual_growth'))
  
  data = {}
  for yr in range(THIRTY + 1):
    value, contributions = monthly(initial, contribution, growth, yr)
    data[str(yr) + ' years'] = {  # data['x years'] = { ... }
      'Deposits': contributions,
      'Return': round(value - contributions, 2)
    }
  return JsonResponse(data)