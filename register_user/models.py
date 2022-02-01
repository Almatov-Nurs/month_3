from typing import IO
from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN, "ADMIN"),
    (VIPClient, "VIP-Client"),
    (CLIENT, "CLIENT")
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, "MALE"),
    (FEMALE, "FEMALE"),
)

LAPTOP = 1
PC = 2
ANDROID = 3
IOS = 4
DEVICE_TYPE = (
    (LAPTOP,"LAPTOP"),
    (PC,"PC"),
    (ANDROID,"ANDROID"),
    (IOS,"IOS"),
)

class CustomUser(User):
    surname = models.CharField(max_length=100,help_text='Фамилия', null=True)
    name = models.CharField(max_length=100,help_text='Имя',null=True)
    patronymic = models.CharField(max_length=100,help_text='Отчество',null=True)
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name="тип пользователя", default=CLIENT)
    phone_number = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE)
    local = models.CharField(max_length=255, null=True, help_text='Your adress!')
    device = models.IntegerField(choices=DEVICE_TYPE, verbose_name='Your device',null=True)
    reserve_number = models.CharField(max_length=100, null=True)

