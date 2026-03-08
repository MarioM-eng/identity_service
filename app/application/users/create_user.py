from app.application.users.dtos import CreateUserDto, UserDto
from app.application.users.mapper import UserMapper
from app.domain.repositories.user_repository import UserRepository
from app.domain.services.password_hasher import PasswordHasher


class CreateUserUseCase:
    """Use case for creating a new user."""

    def __init__(self, user_repo: UserRepository, password_hasher: PasswordHasher):
        """Initialize the use case with a user repository."""
        self.user_repo = user_repo
        self.password_hasher = password_hasher

    async def execute(self, data: CreateUserDto) -> UserDto:
        """Execute the use case to create a new user."""
        hashed_password = self.password_hasher.hash(data.password)
        new_user = UserMapper.dto_to_entity(data, hashed_password)
        saved_user = await self.user_repo.save(new_user)
        return UserMapper.entity_to_dto(saved_user)
