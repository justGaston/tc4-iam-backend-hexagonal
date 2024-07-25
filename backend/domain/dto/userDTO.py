# src/domain/model/user_model.py

from dataclasses import dataclass

@dataclass
class UserJustNamesDTO:
    id: str
    first_name: str
    last_name: str
