from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.new, name='new'),
    url('charge', views.charge, name='charge')
]
