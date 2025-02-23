from celery import Celery
import random
import requests
import time
from datetime import datetime

celery = Celery('tasks', broker='redis://redis:6379/0')

CONTROL_SERVICE_URL = 'http://control-service:5001/status'

@celery.task
def validate_service_status():
    # Determinamos si el servicio está activo o no
    is_active = random.choice([True, False])
    
    # Registro de tiempo antes de enviar la solicitud
    print(f"Sending status at {datetime.now()}")

    # Enviar la información al servicio de control
    response = requests.post(CONTROL_SERVICE_URL, json={'active': is_active})

    # Registro de tiempo después de enviar la solicitud
    end_time = datetime.now()
    print(f"Status sent at {end_time}, response status: {response.status_code}")


# Programamos para que se ejecute cada 3 minutos
celery.conf.beat_schedule = {
    'validate-every-3-minutes': {
        'task': 'src.tasks.validate_service_status',
        'schedule': 180.0,
    },
}

celery.conf.timezone = 'UTC'