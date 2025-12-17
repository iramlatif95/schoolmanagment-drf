from django.db import models

class School(models.Model):
    name=models.CharField(max_length=50)
    phone_number=models.CharField(default=True,max_length=80)
    email=models.EmailField(max_length=60)
    address=models.TextField(max_length=100)

    def __str__(self):
        return self.name 
    
class Branch(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='schoolbranch')
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    email=models.EmailField(max_length=50)

    


# Create your models here.
