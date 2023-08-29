from django.urls import path
from . import views

app_name = 'house'

urlpatterns = [
                path('create_house/', views.create_house, name ='create_house'),
               ]