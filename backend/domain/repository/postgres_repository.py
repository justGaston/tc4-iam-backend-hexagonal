# domain/repository/postgres_repository.py

from typing import List
from application.ports.output.repository import Repository
from domain.model.user_model import User
from infrastructure.database.postgress import get_postgres_connection

class PostgresRepository(Repository):
    def get_all_items(self) -> List[User]:
        connection = get_postgres_connection()
        pass

    def get_item_by_id(self, item_id: int) -> User:
        connection = get_postgres_connection()
        pass

    def add_item(self, item: User) -> None:
        connection = get_postgres_connection()
        pass

    def delete_item(self, item_id: int) -> None:
        connection = get_postgres_connection()
        pass
