from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING


class VkUsers(models.Model):
    id = models.IntegerField(auto_created=True, unique=True, primary_key=True, null=False, )
    username = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_photo = models.CharField(max_length=250, null=True, blank=True)
    count_friends = models.CharField(max_length=5000, null=True, blank=True)
    django_user = models.ForeignKey(User, on_delete=DO_NOTHING, null=True)
    friends = models.ManyToManyField('self', symmetrical=True)
