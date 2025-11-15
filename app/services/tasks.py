import logging
from app.services.celery import celery

logger = logging.getLogger(__name__)

@celery.task(name="app.services.tasks.poll_airflow")
def poll_airflow():
    logger.info("Polling Airflow...")

    # TODO (Day 3): fetch DAG runs here
    # For now we just confirm Celery is working:
    return "Polling complete"
