# src/domain/repository/mysql_repository.py

from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from application.ports.output.repository import Repository
from domain.model.user_model import User
from infrastructure.database.mysql import get_mysql_connection
from domain.model.user_model import User

class MySQLRepository(Repository):
    def get_all_items(self) -> List[User]:
        with get_mysql_connection() as session:
            users_db = session.query(User).all()
            return [User(first_name=user.first_name, last_name=user.last_name, company=user.company) for user in users_db]

    def get_item_by_id(self, item_id: int) -> User:
        with get_mysql_connection() as session:
            try:
                user_db = session.query(User).filter(User.id == item_id).one()
                return User(first_name=user_db.first_name, last_name=user_db.last_name, company=user_db.company)
            except NoResultFound:
                return None

    def add_item(self, item: User) -> None:
        with get_mysql_connection() as session:
            user_db = User(
                first_name=item.first_name,
                last_name=item.last_name,
                company=item.company
            )
            session.add(user_db)
            session.commit()

    def delete_item(self, item_id: int) -> None:
        with get_mysql_connection() as session:
            user_db = session.query(User).filter(User.id == item_id).first()
            if user_db:
                session.delete(user_db)
                session.commit()
