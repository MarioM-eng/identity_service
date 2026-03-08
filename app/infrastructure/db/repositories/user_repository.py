from sqlalchemy.orm import Session

from app.domain.entities.user_entity import UserEntity
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.db.models.user import User


class SQLAlchemyUserRepository(UserRepository):
    """User repository implementation."""

    def __init__(self, db: Session):
        """Initialize the SQLAlchemy user repository.

        Args:
            db (Session): The database session.

        """
        self.db = db

    async def save(self, user: UserEntity) -> UserEntity:
        """Save a user entity to the database.

        Args:
            user (UserEntity): The user entity to save.

        Returns:
            UserEntity: The saved user entity.

        """
        user_model = User.from_entity(user)
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return user_model.to_entity()
