from django.db import models
from accounts.models import User
from classes.models import Class
from schol.models import Branch 

class Subject(models.Model):
    name=models.CharField(max_length=50)
    teacher=models.ForeignKey('accounts.User',on_delete=models.SET_NULL,blank=True,null=True,limit_choices_to={'role':'teacher'})
    created_at=models.DateTimeField(auto_now_add=True)
    class_obj=models.ForeignKey('classes.Class',on_delete=models.CASCADE,related_name='subjects')
    branch=models.ForeignKey('schol.Branch',on_delete=models.CASCADE,related_name='subjects')

# Create your models here.
