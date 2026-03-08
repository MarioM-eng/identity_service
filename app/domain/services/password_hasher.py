from abc import ABC, abstractmethod


class PasswordHasher(ABC):
    """Abstract base class for password hashing."""

    @abstractmethod
    def hash(self, password: str) -> str:
        """Hash the given password."""

    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> bool:
        """Verify the given password against the hashed password."""
