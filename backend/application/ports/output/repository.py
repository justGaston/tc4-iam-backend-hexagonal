# src/application/ports/output/repository.py

from abc import ABC, abstractmethod
from typing import List
from domain.model.user_model import User

class Repository(ABC):
    @abstractmethod
    def get_all_items(self) -> List[User]:
        pass

    @abstractmethod
    def get_item_by_id(self, item_id: int) -> User:
        pass

    @abstractmethod
    def add_item(self, item: User) -> None:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        pass
