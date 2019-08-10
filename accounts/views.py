from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# from main.forms import PasswordChangeForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'User account created for: {username}')
            email = form.cleaned_data.get('email')
            send_mail('Welcome to 360academia', 'Weclcome, we are glad you could make it. We appreciate your taking the time to register.',
                      'no-reply@360academia.com', [email], fail_silently=False)
            login(request, user)
            messages.info(request, 'You are now logged in as {username}')
            return redirect("main:index")
        else:
            for msg in form.error_messages:
                messages.error(request, '{msg}: {form.error_messages[msg]}')

    form = NewUserForm
    return render(request, "accounts/register.html", context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Logged out successfully!')
    return redirect("main:index")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, '{username} Logged-in Successfully!')
                return redirect("main:index")
            else:
                messages.error(
                    request, 'Invalid Login credentials. Please try again.')
        else:
            messages.error(
                request, 'Invalid Login credentials. Please try again.')

    form = AuthenticationForm
    return render(request, "accounts/login.html", {"form": form})


@login_required
def account(request):
    return render(request, "accounts/account.html")
