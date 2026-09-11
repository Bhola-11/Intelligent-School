"""Accounts Authentication and Profile Views."""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import View
from .forms import EduFlowLoginForm, UserProfileForm

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/portals/dashboard/')
        form = EduFlowLoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = EduFlowLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.get_full_name() or user.username}!")
            return redirect('/portals/dashboard/')
        return render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid credentials.'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have been successfully logged out.")
        return redirect('/accounts/login/')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
