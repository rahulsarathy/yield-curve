from compound import views
from django.conf.urls import url


urlpatterns = [
  url(r'^compound/$', views.compound_form, name='compound-form'),
  url(r'^api/v1/compound', views.compound_calculator, name='compound-calculator'),
]