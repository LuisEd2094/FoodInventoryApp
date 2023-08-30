from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HouseForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
@login_required
def create_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save()
            user = request.user
            user.house = house
            user.save()
            messages.success(request, "House created")
            return redirect(reverse('users:index'))
    else:
        form = HouseForm()
        return render(request, 'house/create_house.html', {'form': form})
        