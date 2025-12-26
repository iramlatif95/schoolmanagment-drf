from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Enrollment

@receiver(post_save, sender=Enrollment)
def send_enrollment_email(sender, instance, created, **kwargs):
    if created:
        student_email = instance.student.email  # Get email from related User
        send_mail(
            subject="Enrollment Successful",
            message=f"Hello {instance.student.username}, you have been enrolled in {instance.class_section}.",
            from_email='School Admin <iramlatif32@gmail.com>',  # Your Gmail
            recipient_list=[student_email],
            fail_silently=False,
        )
