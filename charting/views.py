# -*- coding: utf-8 -*-
# Defines the handlers for all of the bond-curve charting pages.

from __future__ import unicode_literals
from charting.compound import monthly
from charting.forms import CompoundCalculatorForm
from charting.models import BondYield
from charting.serializers import BondYieldSerializer
from datetime import datetime
from django.http import Http404, JsonResponse
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


THIRTY = 30


class BondYieldData(APIView):
  def get_object(self, date):
    try:
      yield_date = datetime.strptime(str(date), '%Y%m%d')
      return BondYield.objects.get(date=yield_date)
    except BondYield.DoesNotExist:
      raise Http404
 
  def get(self, request, date, format=None):
    serializer = BondYieldSerializer(self.get_object(date))
    return Response(serializer.data)


def index(request):
  return render(request, 'index.html')

def yield_curve(request):
  """
  Renders the bond yield curve chart, along with the last time that the
  data was updated.
  """
  latest = BondYield.objects.latest('date')
  return render(request, 'yield.html', {'last_updated': latest.date})

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
