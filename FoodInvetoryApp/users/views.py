from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from house.models import House, Ingredients
from invite.models import Invite


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        try:
            house = House.objects.get(pk=request.user.house_id)
        except House.DoesNotExist:
            house = []
        try:
            pending_invites = Invite.objects.filter(receiving_user=request.user, status='pending')
        except Invite.DoesNotExist:
            pending_invites = []
        if house:
            ingredients = house.ingredients_set.all()
        else:
            ingredients = []
        context = {
            'house': house,
            'pending_invites' : pending_invites,
            'ingredients' : ingredients,
        }
        return render(request, 'users/index.html', context)
    else:
        house = []
        pending_invites = []
        context = {
            'house': house,
            'pending_invites' : pending_invites,
        }
        return render(request, 'users/index.html', context)

    

def sign_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse("users:index"))
        form = LoginForm()
        return render(request, "users/login.html", {'form' : form})

    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back')
                return redirect(reverse('users:index'))
        messages.error(request, f'Invalid username or password')
        return render (request, 'users/login.html', {'form': form})
            
    
def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect(reverse("users:index"))

def sign_up(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse("users:index"))
        form = RegisterForm()
        return render(request, 'users/register.html', {'form' : form})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up.')
            login(request, user)
            return redirect(reverse('users:index'))
        else:
            return render(request, 'users/register.html', {'form': form})