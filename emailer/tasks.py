from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_welcome_email(to_email):
    print('Sending to: ', to_email)
    send_mail(
        subject="Welcome!",
        message="Thanks for signing up.",
        from_email=None,
        recipient_list=[to_email],
    )
    return f"Sent to {to_email}"


@shared_task
def send_daily_summary_email():
    print("Sending daily summary email")
    send_mail(
        subject="Daily summary",
        message="Here is your daily summary",
        from_email=None,
        recipient_list=["developer.rathan@gmail.com"]
    )
    return "Daily summary sent"

