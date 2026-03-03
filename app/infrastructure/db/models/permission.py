# pylint: disable=unsubscriptable-object
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.models.base_model import Base, role_permissions

if TYPE_CHECKING:
    from app.infrastructure.db.models.role import Role


class Permission(Base):
    """Model representing a permission."""

    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(255))

    roles: Mapped[list["Role"]] = relationship("Role", secondary=role_permissions, back_populates="permissions")
