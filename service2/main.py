from fastapi import FastAPI
import logging
import os

# Asegúrate de que el directorio exista
log_path = '/var/log/fastapi'
os.makedirs(log_path, exist_ok=True)

# Configuración de logging
logging.basicConfig(filename=f'{log_path}/service.log', level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Hola desde el servicio 2 - root endpoint")
    return {"message": "Servicio 2"}

@app.get("/service2")
def read_service2():
    logger.info("Hola desde el servicio 2 - /service2 endpoint")
    return {"message": "Servicio 2"}