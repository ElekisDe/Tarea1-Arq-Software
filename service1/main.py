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
    logger.info("Hola desde el servicio 1 - root endpoint")
    return {"message": "Servicio 1"}

@app.get("/service1")
def read_service1():
    logger.info("Hola desde el servicio 1 - /service1 endpoint")
    return {"message": "Servicio 1"}