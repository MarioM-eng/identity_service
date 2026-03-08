"""Base model for SQLAlchemy ORM."""

import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import Uuid
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class  # pylint: disable=E0401

SOFT_DELETE_MIXIN_CLASS: type = generate_soft_delete_mixin_class()


class UUIDModel:
    """Base UUID class for SQLAlchemy models."""

    uuid: Mapped[uuid_pkg.UUID] = mapped_column(Uuid(as_uuid=True), default=uuid_pkg.uuid4)


class Base(DeclarativeBase, UUIDModel):
    """Base class for SQLAlchemy models."""


class AuditableModel:
    """Base Auditable class for SQLAlchemy models."""

    created_at: Mapped[datetime] = mapped_column(
        default=func.now(), comment="Fecha de creación"  # pylint: disable=not-callable
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        onupdate=func.now(), comment="Fecha de actualización"  # pylint: disable=not-callable
    )
    created_by: Mapped[int | None] = mapped_column(comment="ID del usuario que creó el registro")
    updated_by: Mapped[int | None] = mapped_column(comment="ID del usuario que actualizó el registro")


class SoftDeleteMixin(SOFT_DELETE_MIXIN_CLASS):  # type: ignore[misc]
    """Mixin for soft delete functionality."""

    deleted_at: datetime


user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)


role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
    Column("permission_id", ForeignKey("permissions.id"), primary_key=True),
)
