
from django.shortcuts import render, redirect
from .models import Invite  # Import your models
from house.models import House
from .forms import InvitationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse
# Create your views here.
User = get_user_model()

@login_required
def send_invitation(request):
    if request.method == "POST":
        form = InvitationForm(request.POST)
        if form.is_valid():
            sending_user = request.user
            receiving_username = form.cleaned_data['receiving_user']
            message = form.cleaned_data['message']
            house = sending_user.house
            try:
                receiving_user = User.objects.get(username = receiving_username)
                invite = Invite.objects.create(
                    inviting_user = sending_user,
                    receiving_user = receiving_user,
                    house = house,
                    message = message,
                )
                invite.save()
                messages.success(request, f'Invite send to {receiving_username}')
                redirect(reverse('users:index'))
            except User.DoesNotExist:
                messages.error(request, f'Couldn\'t send message to {receiving_username}, check username again')
                return render(request, 'invite/send_invitation.html', {'form' : form})


    else:
        form = InvitationForm()
        return render(request, 'invite/send_invitation.html', {'form' : form})
