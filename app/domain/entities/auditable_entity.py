from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True)
class AuditableEntity:
    """Base Auditable class for SQLAlchemy models."""

    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by: int | None = None
    updated_by: int | None = None
