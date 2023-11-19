from celery import shared_task 

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from Celeryproject  import settings

@shared_task(bind=True)
def test_fun(self):
    try:
        for i in range(10):
            print(i)
    except Exception as e:
        print(e)
    return "done"



@shared_task(bind=True)
def test_email(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi, celery testing"
        messege = "Sample celery testing"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message = messege,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )

    return "done"    
