# src/infrastructure/config/settings.py

from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    database_url: str
    database_type: str  # 'mysql' o 'postgres'

    class Config:
        env_file = '.env'

settings = Settings()
