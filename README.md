# Reminder
Backend of the event reminder application by sending sms 30 min before the scheduled event
# Requirement
Install these libraries to run this project-<br/>
django-pip install django<br/>
djangorest framework-pip install djangorestframework<br/>
PhoneNumberField-pip install django-phonenumber-field,for more information look https://github.com/stefanfoulis/django-phonenumber-field<br/>
TimeZoneField-pip install django-timezone-field<br/>
Install redis and celery-http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/<br/>
The above mentioned link is the best for setting up celery redis<br/>
Setup your twilio account details in task/messageSend.py file<br/>
To start celery redis -
Go to the foder where celery is installed and run-<br/>
celery --app=Reminder.celery worker --loglevel=info<br/>
Run the DRF project as normal any django web application and you are good to go.<br/>
# Future Work
Well,someday I will create the frontend for this application
# Contribution
Feel free to branch out and make pull request.Reporting bugs or code breaks and contributing a frontend for this project is highly appreciated,till then Happy coding!!
