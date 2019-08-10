from charting import views
from django.conf.urls import url


urlpatterns = [
  url(r'^$', views.index, name='index'),

  # Bond yield chart
  url(r'^yield/$', views.yield_curve, name='yield-curve'),
  url(r'^api/v1/bond_yield/(?P<date>[0-9]{8})$', views.BondYieldData.as_view(), name='bond-yield-retrieve'),

  # Compounding calculator
  url(r'^compound/$', views.compound_form, name='compound-form'),
  url(r'^api/v1/compound', views.compound_calculator, name='compound-calculator'),

  # Resources
  url(r'^resources/$', views.resources, name='resources'),
]
