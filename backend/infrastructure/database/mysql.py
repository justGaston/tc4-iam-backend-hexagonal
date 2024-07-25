# src/infrastructure/database/mysql.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from contextlib import contextmanager

# Base de SQLAlchemy para los modelos
Base = declarative_base()

# URL de la base de datos (asegúrate de que está correctamente configurada en tu .env o en el código)
DATABASE_URL = os.getenv("192.168.0.192:3666", "mysql+pymysql://admin:admin@localhost/my_database")

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)

# Crear una sesión configurada
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una nueva sesión de base de datos
def get_mysql_connection():
    db = SessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()
