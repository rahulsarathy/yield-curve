# -*- coding: utf-8 -*-
# Defines the handlers for all of the bond-curve charting pages.

from __future__ import unicode_literals
from django.shortcuts import render


def index(request):
  return render(request, 'index.html')
