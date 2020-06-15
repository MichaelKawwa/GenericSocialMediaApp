from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, UserProfileModel

# Create your views here.
def signUp(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
    else:
        form = UserCreationForm()
        print('well shit mate ')
    return render(request, 'users/signup.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('/')

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in {username}")
                return redirect('/')
            else:
                message.error(request, "There was trouble logging in.")
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def UpdateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.Post, instance=request.user)
        p_form = UserProfileModel(request.Post, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileModel(instance=request.user.profile)

    context = {
    'u_form':u_form,
    'p-form':p_form
    }

    return render(request, 'users/profile.html', context)
