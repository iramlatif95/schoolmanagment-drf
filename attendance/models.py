from django.db import models
from accounts.models import User 
from classes.models import Section,Class    


ATTENDANCE_STATUS=(
    ('present','present'),
    ('abscent','abscent'),
    ('leave','leave'),
    ('late','late'),

)
class Attendance(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role':'student'})
    date=models.DateField()
    status=models.CharField(max_length=30,choices=ATTENDANCE_STATUS)
    note = models.TextField(blank=True, null=True)
    class_section=models.ForeignKey(Section,on_delete=models.CASCADE)

    class Meta:
        unique_together=('student','date','class_section')




# Create your models here.
