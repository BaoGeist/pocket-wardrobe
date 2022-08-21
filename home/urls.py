from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('home', views.home, name='home-home'),
    path('input', views.input, name='home-input'),
    path('generator', views.getFit, name='home-fit'),
]