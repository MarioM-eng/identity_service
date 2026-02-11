"""Base model for SQLAlchemy ORM."""

from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import Uuid
from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class  # pylint: disable=E0401

SOFT_DELETE_MIXIN_CLASS: type = generate_soft_delete_mixin_class()


class UUIDModel:
    """Base UUID class for SQLAlchemy models."""

    uuid: Mapped[Uuid[str]] = mapped_column(Uuid(as_uuid=True), default=func.uuid())


class Base(DeclarativeBase, UUIDModel):
    """Base class for SQLAlchemy models."""


class AuditableModel:
    """Base Auditable class for SQLAlchemy models."""

    created_at: Mapped[datetime] = mapped_column(default=func.now, comment="Fecha de creación")
    updated_at: Mapped[datetime] = mapped_column(onupdate=func.now, comment="Fecha de actualización")
    created_by: Mapped[int | None] = mapped_column(comment="ID del usuario que creó el registro")
    updated_by: Mapped[int | None] = mapped_column(comment="ID del usuario que actualizó el registro")


class SoftDeleteMixin(SOFT_DELETE_MIXIN_CLASS):  # type: ignore[misc]
    """Mixin for soft delete functionality."""

    deleted_at: datetime
