from celery import Celery
import random
import requests
import time

# Initialize Celery
celery = Celery('tasks', broker='redis://localhost:6379/0')

# Control service URL
CONTROL_SERVICE_URL = 'http://control-service:5000/status'

@celery.task
def validate_service_status():
    # Randomly determine if the service is active
    is_active = random.choice([True, False])
    
    # Send the status to the control service
    requests.post(CONTROL_SERVICE_URL, json={'active': is_active})

# Schedule the task to run every 3 minutes
celery.conf.beat_schedule = {
    'validate-every-3-minutes': {
        'task': 'tasks.validate_service_status',
        'schedule': 180.0,
    },
}