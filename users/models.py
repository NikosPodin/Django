from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
# Create your models here.
NULL_INSTALL = {'null':True, 'blank':True}

class User(AbstractUser):
    image = models.ImageField(upload_to='user_image', blank=True)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(unique=True, error_messages={
        'unique': "An email is already used.",
    }, )
    activation_key= models.CharField(max_length=128, **NULL_INSTALL)

    # activasion_key_created = models.DateTimeField(default=(now()+timedelta(hours=48)))
    activation_key_created = models.DateTimeField(auto_now_add=True,**NULL_INSTALL)

    def is_activation_key_expired(self):
        if now() <= self.activation_key_created + timedelta(hours=48):
            return False
        return True