from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.application.users.create_user import CreateUserUseCase
from app.application.users.dtos import CreateUserDto
from app.infrastructure.db.repositories.user_repository import SQLAlchemyUserRepository
from app.infrastructure.db.sesion import get_db
from app.infrastructure.security.bcrypt_hasher import BcryptHasher
from app.schemas.helper_schema import SingleResponseSchema
from app.schemas.user_schema import UserCreateSchema, UserSchema

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.post("")
async def create_user(
    data: UserCreateSchema, db: Annotated[Session, Depends(get_db)]
) -> SingleResponseSchema[UserSchema]:
    """Create a new user."""
    repository = SQLAlchemyUserRepository(db)
    password_hasher = BcryptHasher()
    use_case = CreateUserUseCase(repository, password_hasher)
    create_user_dto = CreateUserDto(**data.model_dump())

    user = await use_case.execute(create_user_dto)
    return SingleResponseSchema[UserSchema](message="user created successfully", data=UserSchema.model_validate(user))
