# main.py

import os
from fastapi import FastAPI
from interface.rest.user_controller import router

# Crear la aplicación FastAPI
app = FastAPI()

# Incluir el router
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    
    # Cargar las variables de entorno desde un archivo .env si es necesario
    from dotenv import load_dotenv
    load_dotenv()

    # Configurar y ejecutar Uvicorn directamente
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
