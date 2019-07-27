# -*- coding: utf-8 -*-
# Defines the handlers for all of the bond-curve charting pages.

from __future__ import unicode_literals
from charting.models import BondYield
from charting.serializers import BondYieldSerializer
from datetime import datetime
from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


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
  latest = BondYield.objects.latest('date')
  return render(request, 'index.html', {'last_updated': latest.date})
