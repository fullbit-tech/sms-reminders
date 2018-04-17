from celery.schedules import crontab


CELERY_IMPORTS = ('app.tasks')
CELERYBEAT_SCHEDULE = {
    'scheduled-reminders': {
        'task': 'app.tasks.send_reminders',
        'schedule': crontab(minute="*"),  # Run every minute
    }
}
