from django.urls import path
from . import views

app_name = 'invite'

urlpatterns = [
    path("send_invitation/", views.send_invitation, name = "send_invitation"),
    path('accept/<int:invitation_id>/', views.accept_invitation, name='accept_invitation'),
    path('decline/<int:invitation_id>/', views.decline_invitation, name='decline_invitation'),
]