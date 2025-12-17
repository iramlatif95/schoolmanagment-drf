from django.db import models
from django.contrib.auth.models import AbstractUser 

class User(AbstractUser):
    USER_ROLES=(
        ('admin','admin'),
        ('teacher','teacher'),
        ('student','student'),
        ('parent','parent'),
    )
    role=models.CharField(max_length=50,choices=USER_ROLES)
    #phone_number=models.IntegerField(max_length=30,default=True)
    def __str__(self):
        return self.username


# Create your models here.
