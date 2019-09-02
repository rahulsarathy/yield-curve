from django.shortcuts import render


def credit_cards_view(request):
  return render(request, 'credit_cards.html')
