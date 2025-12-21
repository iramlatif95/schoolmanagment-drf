from django.db import models
#from django.db import models

from accounts.models import User 
from classes .models import Section
from subj .models import Subject 

class Exam(models.Model):
    name=models.CharField(max_length=50)
    section=models.ForeignKey(Section,on_delete=models.CASCADE)
    date=models.DateField()

class Result(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks_obtain=models.FloatField()
    total_marks=models.FloatField()

    class Meta:
        unique_together=('student','exam','subject')


# Create your models here.
# Create your models here.
