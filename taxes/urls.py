from django.conf.urls import url
from taxes import views


urlpatterns = [
  url(r'^taxes/$', views.tax_calculator, name='tax-calculator'),
]