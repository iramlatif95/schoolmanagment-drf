# fee/tasks.py
from celery import shared_task
from django.core.mail import send_mail
from .models import Payment
from datetime import date

@shared_task
def send_fee_reminders():
    unpaid_payments = Payment.objects.filter(status='unpaid')
    for payment in unpaid_payments:
        student_email = payment.student.email
        send_mail(
            'Fee Reminder',
            f'Hello {payment.student.first_name}, your fee "{payment.fee.title}" is pending.',
            'iramlatif32@.com',
            [student_email],
        )
