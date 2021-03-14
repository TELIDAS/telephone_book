from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

ADMIN = 1
DIRECTOR = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (DIRECTOR, 'DIRECTOR'),
    (CLIENT, 'CLIENT'),
)

class Users(AbstractBaseUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя', default=CLIENT)
    username = models.CharField('username', unique=True, max_length=100)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']
