# pylint: disable=unsubscriptable-object
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.db.models.base_model import Base, role_permissions, user_roles

if TYPE_CHECKING:
    from app.infrastructure.db.models.permission import Permission
    from app.infrastructure.db.models.user import User


class Role(Base):
    """Model representing a role."""

    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(255))

    users: Mapped[list["User"]] = relationship("User", secondary=user_roles, back_populates="roles")
    permissions: Mapped[list["Permission"]] = relationship(
        "Permission", secondary=role_permissions, back_populates="roles"
    )
