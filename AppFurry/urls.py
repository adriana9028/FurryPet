from django.urls import path
from . import views 
from django.conf import settings

urlpatterns = [
    path('' , views.layout, name="layout" ),
    path('index/', views.index, name='index'),
]