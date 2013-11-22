# Create your views here.

from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse
from .forms import RegistrationForm
from .forms import LoginForm


def registrate(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return HttpResponse('User was registered')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def log_in(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                auth.login(request, form.get_user())
                return HttpResponse('User login successfully!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
