from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('population', views.pop_loss, name='pop_loss'),
    path('clusters', views.clusters, name='clusters'),
    path('request_pop_data', views.request_pop_data, name='request_pop_data')
]
