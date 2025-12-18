from django.db import models

from accounts.models import User


from schol.models import Branch

class Class(models.Model):
    name=models.CharField(max_length=50)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='classes')
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='classes',limit_choices_to={'role':'teacher'})
    created_at=models.DateTimeField(auto_now_add=True)
# Create your models here.

class Section(models.Model):
    name=models.CharField(max_length=50)
    class_obj=models.ForeignKey(Class,on_delete=models.CASCADE,related_name='sections')
    created_at=models.DateTimeField(auto_now_add=True)
    students=models.ManyToManyField(User,blank=True,related_name='sections',limit_choices_to={'role':'student'})
    

                                   