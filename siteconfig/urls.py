# Central URL configuration for the Division web application.

from django.conf.urls import include, url


urlpatterns = [
  url(r'^', include('charting.urls')),
  url(r'^', include('compound.urls')),
  url(r'^', include('credit_cards.urls')),
  url(r'^', include('investing.urls')),
  url(r'^', include('taxes.urls')),
]
