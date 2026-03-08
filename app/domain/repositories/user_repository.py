from abc import ABC, abstractmethod

from app.domain.entities.user_entity import UserEntity


class UserRepository(ABC):
    """User repository interface."""

    @abstractmethod
    async def save(self, user: UserEntity) -> UserEntity:
        """Save a user."""
