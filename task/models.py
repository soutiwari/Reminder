from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField
from Reminder import celery_app
import arrow

REMINDER_TIME = 30


class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    message = models.TextField()
    phoneno = PhoneNumberField()
    scheduleTime = models.DateTimeField()
    timezone = TimeZoneField(default='Asia/Kolkata')
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)
    eventId = models.CharField(max_length=50, default='1234')

    class Meta:
        ordering = ('created',)

    def scheduleReminder(self):
        eventTime = arrow.get(self.scheduleTime, self.timezone.zone)
        reminderTime = eventTime.replace(minutes=-REMINDER_TIME)
        print(reminderTime)
        from task.messageSend import SendReminder
        action = SendReminder.apply_async((self.pk,), eta=reminderTime)
        return action.id

    def save(self, *args, **kwargs):
        if self.eventId:
            celery_app.control.revoke(self.eventId)
        super(Task, self).save(*args, **kwargs)
        self.eventId = self.scheduleReminder()
        super(Task, self).save(update_fields=['eventId'])
