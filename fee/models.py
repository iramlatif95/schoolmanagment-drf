from django.db import models

# Create your models here.
from django.db import models
from accounts.models import User
from classes.models import Section

class Fee(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()

   


class Payment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'student'})
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('paid','Paid'),('partial','Partial'),('unpaid','Unpaid')], default='unpaid')

    class Meta:
        unique_together = ('student', 'fee')

   