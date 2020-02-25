import requests as requests

from core.models import VkUsers



def load(*args, **kwargs):
    access_token = kwargs.get('response').get("access_token")
    user, created = VkUsers.objects.get_or_create(username=kwargs.get('response').get('user_id'),
                                                  first_name=kwargs.get('response').get('first_name'),
                                                  last_name=kwargs.get('response').get('last_name'),
                                                  user_photo=kwargs.get('response').get('user_photo'),
                                                  django_user=kwargs.get('user'))
    if created:

        params = {"fields": 'name', "access_token": access_token, "v": "5.103"}
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        if response.status_code == 200:
            response = response.json()
            user.count_friends = response.get("response").get("count")
            for item in response.get("response").get("items"):
                username = item.get("id")
                first_name = item.get("first_name")
                last_name = item.get("last_name")
                friend, created_friend = VkUsers.objects.get_or_create(username=username, first_name=first_name, last_name=last_name)
                user.friends.add(friend)
                user.save()
