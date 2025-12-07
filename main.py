from fastapi import FastAPI
from typing import Union

# Crea la instancia de la aplicación FastAPI
app = FastAPI(title="Mi API de Prueba en Vercel")

# 1. Endpoint de Raíz (Health Check)
@app.get("/")
def read_root():
    """Endpoint básico para verificar que la API está viva."""
    return {"message": "¡La API de FastAPI está funcionando en Vercel!"}

# 2. Endpoint de Suma
@app.get("/sumar/{num1}/{num2}")
def sumar_numeros(num1: Union[int, float], num2: Union[int, float]):
    """Suma dos números."""
    resultado = num1 + num2
    return {"numero_1": num1, "numero_2": num2, "resultado": resultado}

# Nota: No necesitamos el código de Uvicorn aquí. Vercel se encarga de iniciarlo.
