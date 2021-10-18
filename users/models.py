from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    image = models.ImageField(verbose_name='Ава', upload_to='user_image', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=False, default=18)
