from django.urls import path
from . import views 
from django.conf import settings

urlpatterns = [
    path('' , views.Ppadre, name="Ppadre" ),
    path('index/', views.index, name='index')
]