from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    school = models.ForeignKey(School,on_delete=models.CASCADE,related_name='branches')
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school.name} - {self.name}"


# Create your models here.
