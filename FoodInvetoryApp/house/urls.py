from django.urls import path
from . import views

app_name = 'house'

urlpatterns = [
                path('house_form/', views.create_house, name ='create_house'),
                path('edit/<int:pk>/', views.edit, name="edit"),
                path('view/<int:pk>', views.view, name='view'),
                
               ]