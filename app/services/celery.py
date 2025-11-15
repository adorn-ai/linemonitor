from app.core.config import settings
from celery import Celery

celery = Celery(
    'monitorline',
    backend=settings.REDIS_URL,
    broker=settings.REDIS_URL
)
# auto detect tasks in tasks.py
celery.autodiscover_tasks(["app.services"])

# set beat to poll airflow every 1 minute
celery.conf.beat_schedule = {
    "poll-airflow-every-1-minute" : {
        "task": "app.services.tasks.poll_airflow",
        "schedule": 60.0 
    }
}

celery.conf.timezone = "UTC"