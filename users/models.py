from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.

class User(AbstractUser):
    pass

#Creation d'un groupe; s'applique une fois
# admin_group = Group.objects.create(name='Admins')

# users_group = Group.objects.create(name='Users')
