from django.shortcuts import render


def tax_calculator(request):
  return render(request, 'taxes.html')
