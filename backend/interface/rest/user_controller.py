# interface/rest/item_controller.py

from fastapi import APIRouter, Depends
from typing import List
from domain.model.user_model import User
from application.ports.output.repository import Repository
from domain.repository.mysql_repository import MySQLRepository
from domain.repository.postgres_repository import PostgresRepository
from infrastructure.config.settings import settings

router = APIRouter()

def get_repository() -> Repository:
    if settings.database_type == 'mysql':
        return MySQLRepository()
    elif settings.database_type == 'postgres':
        return PostgresRepository()
    else:
        raise ValueError("Unsupported database type")

@router.get("/users", response_model=List[User])
def read_items(repository: Repository = Depends(get_repository)):
    return repository.get_all_items()

@router.get("/users/{item_id}", response_model=User)
def read_item(item_id: int, repository: Repository = Depends(get_repository)):
    return repository.get_item_by_id(item_id)

@router.post("/users")
def create_item(item: User, repository: Repository = Depends(get_repository)):
    repository.add_item(item)

@router.delete("/users/{item_id}")
def delete_item(item_id: int, repository: Repository = Depends(get_repository)):
    repository.delete_item(item_id)
