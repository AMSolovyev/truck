from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.trucks_table, name='trucks_table'),
]
