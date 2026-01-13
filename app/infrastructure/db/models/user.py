"""Model representing a user."""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import Enum, Uuid

from app.infrastructure.db.models.base_model import Base


class User(Base):
    """Model representing a user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="Primer nombre del usuario")
    second_name: Mapped[str | None] = mapped_column(String(100), comment="Segundo nombre del usuario")
    first_surname: Mapped[str] = mapped_column(String(100), nullable=False, comment="Primer apellido del usuario")
    second_surname: Mapped[str | None] = mapped_column(String(100), comment="Segundo apellido del usuario")
    gender: Mapped[Enum] = mapped_column(Enum("male", "female", "other"), nullable=False)
    uuid: Mapped[Uuid[str]] = mapped_column(Uuid(as_uuid=True), server_default=func.uuid())

    def __repr__(self) -> str:
        """Return a string representation of the user."""
        return f"User(id={self.id!r}, name={self.first_name!r})"
