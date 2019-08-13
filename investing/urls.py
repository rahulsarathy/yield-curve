from django.conf.urls import url
from investing import views


urlpatterns = [
  url(r'^scott_adams/$', views.scott_adams, name='scott-adams'),
]