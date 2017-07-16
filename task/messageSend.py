from twilio.rest import Client
from celery import shared_task
import arrow
from task.models import Task

account_sid = "acxxxxxxxxxx"
auth_token = "xxxxxxxxxxxx"

client = Client(account_sid, auth_token)


@shared_task
def SendReminder(task_pk):
    try:
        task = Task.objects.get(pk=task_pk)
    except Task.DoesNotExist:
        return
    pno = str(task.phoneno)
    msg = str(task.title) + str(task.message)
    message = client.messages.create(
        body=msg,
        to=pno,
        from_="YOUR TWILIO NUMBER",
    )
