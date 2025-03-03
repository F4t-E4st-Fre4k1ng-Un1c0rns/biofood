from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Self

from src.backend.domain.models import UserID
from src.backend.domain.value_objects import UserRole


@dataclass
class AccessTokenI(ABC):
    exp: datetime
    user_id: UserID
    user_role: UserRole

    @abstractmethod
    def decode(cls, encoded_token: str) -> Self:
        raise NotImplementedError

    @abstractmethod
    def encode(self) -> str:
        raise NotImplementedError
