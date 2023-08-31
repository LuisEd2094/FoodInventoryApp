from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from .forms import HouseForm
from .models import House
from users.models import User
from django.urls import reverse
from django.contrib import messages

# Create your views here.
@login_required
def house_form(request):
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
        return render(request, 'house/house_form.html', {'form': form})
    
@login_required
def view(request, pk):
    house = get_object_or_404(House, pk=pk)
    users_list = get_list_or_404(User, house_id= house)
    users = [user for user in users_list if user.id != request.user.id]
    usernames =[user.username for user in users]
    print(usernames)
    context = {
        'house' : house,
        'users' : users,
    }
    return render(request, 'house/view.html', context)
    
@login_required
def edit(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        form = HouseForm(request.POST, instance=house)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edit house')
            return redirect(reverse('users:index'))
    else:
        form = HouseForm(instance=house)
        return render(request, 'house/house_form.html', {'form': form})
    
@login_required
def delete(request, pk):
    house = get_object_or_404(House, pk=pk)
    if request.method == 'POST':
        house.delete()
        messages.success(request, f'Successfully deleted your House')
        return redirect('users:index')
    return render(request, 'house/confirm_delete.html', {'house': house})