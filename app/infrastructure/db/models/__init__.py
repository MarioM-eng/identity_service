"""Models package - imports all models for Alembic auto-detection."""
from app.infrastructure.db.models.base_model import Base
from app.infrastructure.db.models.user import User

__all__ = ["Base", "User"]
