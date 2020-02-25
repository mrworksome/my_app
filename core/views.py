from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'home.html')


@login_required
def home(request):
    return render(request, 'home.html')