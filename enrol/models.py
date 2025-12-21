from django.db import models


from accounts.models import User 
from classes.models import Class,Section  

class Enrollment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    class_section=models.ForeignKey(Section,on_delete=models.CASCADE)
    enrollment_date=models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=(('active','Active'),('inactive','Inactive')))
# Create your models here.
