import requests
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from social_django.models import UserSocialAuthManager
from django.contrib.auth import logout as auth_logout

from django.contrib.auth import logout


def login(request, **kwargs):
    return render(request, 'login.html', {'redirect_authenticated_user': True})


@login_required
def home(request):
    social_user = UserSocialAuth.objects.filter(user=request.user).first()
    access_token = social_user.extra_data.get('access_token')

    params = {"fields": 'photo_max, counters', "access_token": access_token, "v": "5.103"}
    user_data = requests.get('https://api.vk.com/method/users.get', params=params)
    user_data = user_data.json()
    user = user_data.get("response")[0]

    return render(request, 'home.html',
                  {'vk_user': user})


def search(request):
    social_user = UserSocialAuth.objects.filter(user=request.user).first()
    access_token = social_user.extra_data.get('access_token')
    search_name = request.GET.get("name")

    params = {"fields": 'photo_max, counters', "access_token": access_token, "v": "5.103"}
    user_data = requests.get('https://api.vk.com/method/users.get', params=params)
    user_data = user_data.json()
    user = user_data.get("response")[0]

    friends_with_search_name = []
    params = {"fields": 'name', "access_token": access_token, "v": "5.103"}
    response = requests.get('https://api.vk.com/method/friends.get', params=params)
    if response.status_code == 200:
        response = response.json()
        for item in response.get("response").get("items"):
            if search_name == item.get("first_name").lowercase():
                friends_with_search_name.append(item)

    return render(request, 'home.html', {'friends_by_name': friends_with_search_name,
                                         'vk_user': user})
