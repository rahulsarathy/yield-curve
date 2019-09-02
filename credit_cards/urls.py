from credit_cards import views
from django.conf.urls import url


urlpatterns = [
  url(r'^credit_cards/$', views.credit_cards_view, name='credit-cards'),
]
