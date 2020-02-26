from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import VkUsers


def login(request, **kwargs):
    return render(request, 'login.html', {'redirect_authenticated_user': True})


@login_required
def home(request):
    return render(request, 'home.html',
                  {'vk_user': VkUsers.objects.get(pk=request.user.pk)})


def search(request):
    name = request.GET.get("name")
    friends_by_name = VkUsers.objects.get(pk=request.user.pk).friends.filter(first_name=name.capitalize())
    return render(request, 'home.html', {'friends_by_name': friends_by_name})

