from django.conf.urls import url
from charting import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
]