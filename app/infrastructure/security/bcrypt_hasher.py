import bcrypt

from app.domain.services.password_hasher import PasswordHasher


class BcryptHasher(PasswordHasher):
    """Concrete implementation of PasswordHasher using bcrypt."""

    def hash(self, password: str) -> str:
        """Hash the given password."""
        return str(bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8"))

    def verify(self, password: str, hashed_password: str) -> bool:
        """Verify the given password against the hashed password."""
        return bool(bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8")))
