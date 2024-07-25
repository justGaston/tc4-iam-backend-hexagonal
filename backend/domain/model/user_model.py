# src/domain/model/user_model.py

from dataclasses import dataclass

@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    company: str
