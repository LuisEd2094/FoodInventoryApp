from django.urls import path
from . import views

app_name = 'house'

urlpatterns = [
                path('house_form/', views.house_form, name ='house_form'),
                path('edit/<int:pk>/', views.edit, name='edit'),
                path('view/<int:pk>', views.view, name='view'),
                path('delete/<int:pk>', views.delete, name = 'delete'),
               ]