from django.conf.urls import url
from taxes import views


urlpatterns = [
  url(r'^taxes/$', views.tax_form, name='taxes-form'),
  url(r'^api/v1/taxes/', views.tax_calculator, name='tax-calculator'),
]