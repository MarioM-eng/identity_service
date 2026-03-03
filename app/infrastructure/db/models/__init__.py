"""Models package - imports all models for Alembic auto-detection."""
from app.infrastructure.db.models.base_model import Base
from app.infrastructure.db.models.permission import Permission
from app.infrastructure.db.models.role import Role
from app.infrastructure.db.models.user import User

__all__ = ["Base", "Permission", "Role", "User"]
