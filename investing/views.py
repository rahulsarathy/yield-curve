from django.shortcuts import render


def scott_adams(request):
  return render(request, 'scott_adams.html')
