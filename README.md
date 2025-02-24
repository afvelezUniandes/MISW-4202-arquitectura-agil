# Mis Microservicios en Python

Este proyecto es una colección de microservicios construidos usando Python, Flesk, Docker, PostgreSQL y SQLAlchemy. Consiste en tres servicios principales: un gatewaye, un servicio de órdenes y un servicio de control.

## Resumen de los Servicios

### Gateway de Cliente

- **Descripción**: Este servicio actúa como el punto de entrada para las solicitudes entrantes. Maneja tanto solicitudes POST como GET y las reenvía al microservicio correspondiente.
- **Tecnologías**: Flask

### Servicio de Órdenes

- **Descripción**: Este microservicio procesa órdenes. Recibe mensajes del gateway de cliente, interactúa con una base de datos PostgreSQL y ejecuta tareas periódicas para validar su estado.
- **Tecnologías**: Flask, SQLAlchemy, PostgreSQL, Celery, Redis

### Servicio de Control

- **Descripción**: Este servicio monitorea el estado del servicio de órdenes. Recibe mensajes de estado y los registra en la consola.
- **Tecnologías**: Flask

## Instrucciones de Configuración

1. **Clonar el Repositorio**

   ```
   git clone https://github.com/afvelezUniandes/MISW-4202-arquitectura-agil
   cd my-python-microservices
   ```

2. **Construir y Ejecutar los Servicios**
   Usa Docker Compose para construir y ejecutar los servicios:

   ```
   docker-compose up --build
   ```

3. **Acceder al Gateway de Cliente**
   El gateway de cliente estará accesible en `http://localhost:<puerto>` (reemplaza `<puerto>` con el puerto especificado en el `docker-compose.yml`).

## Uso

- Envía solicitudes POST al gateway de cliente para crear órdenes.
- Usa solicitudes GET para recuperar el estado de las órdenes u otra información según sea necesario.

## Dependencias

Cada servicio tiene su propio archivo `requirements.txt` que lista las dependencias necesarias. Asegúrate de instalarlas según sea necesario.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
