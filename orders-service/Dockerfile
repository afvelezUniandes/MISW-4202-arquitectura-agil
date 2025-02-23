FROM python:3.9-slim

# Crear un usuario no root para celery
RUN useradd -ms /bin/bash celeryuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Crear un directorio para Celery Beat y darle permisos al usuario no root
RUN mkdir -p /app/celerybeat-schedule && chown -R celeryuser:celeryuser /app/celerybeat-schedule

# Cambiar al usuario no root
USER celeryuser

CMD ["python", "app.py"]