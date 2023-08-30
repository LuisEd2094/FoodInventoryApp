from django.urls import path
from . import views

app_name = 'invite'

urlpatterns = [
    path("send_invitation/", views.send_invitation, name = "send_invitation")
]