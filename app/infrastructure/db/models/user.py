"""Model representing a user."""
# pylint: disable=unsubscriptable-object
from typing import TYPE_CHECKING

import bcrypt
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Enum

from app.domain.entities.user_entity import UserEntity
from app.domain.value_objects.gender_value_object import GenderVO
from app.infrastructure.db.models.base_model import AuditableModel, Base, SoftDeleteMixin, user_roles

if TYPE_CHECKING:
    from app.infrastructure.db.models.role import Role


class User(Base, SoftDeleteMixin, AuditableModel):
    """Model representing a user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False, comment="Primer nombre del usuario")
    second_name: Mapped[str | None] = mapped_column(String(100), comment="Segundo nombre del usuario")
    first_surname: Mapped[str] = mapped_column(String(100), nullable=False, comment="Primer apellido del usuario")
    second_surname: Mapped[str | None] = mapped_column(String(100), comment="Segundo apellido del usuario")
    gender: Mapped[str] = mapped_column(Enum("male", "female", "other"), nullable=False)

    roles: Mapped[list["Role"]] = relationship("Role", secondary=user_roles, back_populates="users")

    def __repr__(self) -> str:
        """Return a string representation of the user."""
        return f"User(id={self.id!r}, name={self.first_name!r})"

    def set_password(self, password: str) -> None:
        """Set password to security."""
        self.password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @classmethod
    def from_entity(cls, entity: UserEntity) -> "User":
        """Convert a UserEntity to a User model."""
        return cls(
            id=entity.id,
            password=entity.password,
            first_name=entity.first_name,
            second_name=entity.second_name,
            first_surname=entity.first_surname,
            second_surname=entity.second_surname,
            gender=entity.gender.value.value,
        )

    def to_entity(self) -> UserEntity:
        """Convert this DB model back to a Domain Entity."""
        return UserEntity(
            id=self.id,
            password=self.password,
            first_name=self.first_name,
            second_name=self.second_name,
            first_surname=self.first_surname,
            second_surname=self.second_surname,
            gender=GenderVO.from_str(self.gender),
        )
