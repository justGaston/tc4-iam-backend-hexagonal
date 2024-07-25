# infrastructure/database/postgres.py

import psycopg2
from psycopg2.extensions import connection as Connection

def get_postgres_connection() -> Connection:
    # Lógica para obtener una conexión a PostgreSQL
    return psycopg2.connect(
        host='localhost',
        user='user',
        password='password',
        database='database'
    )
