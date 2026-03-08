from app.application.users.dtos import CreateUserDto, UserDto
from app.domain.entities.user_entity import UserEntity
from app.domain.value_objects.gender_value_object import GenderVO


class UserMapper:
    """Mapper for converting CreateUserDto to User model and vice versa."""

    @staticmethod
    def dto_to_entity(dto: CreateUserDto, hashed_password: str) -> UserEntity:
        """Convert a CreateUserDto to a User entity."""
        return UserEntity(
            id=None,
            password=hashed_password,
            first_name=dto.first_name,
            second_name=dto.second_name,
            first_surname=dto.first_surname,
            second_surname=dto.second_surname,
            gender=GenderVO.from_str(dto.gender),
        )

    @staticmethod
    def entity_to_dto(entity: UserEntity) -> UserDto:
        """Convert a User entity to a CreateUserDto."""
        if entity.id is None:
            message = "No se puede crear un UserDto desde una entidad sin ID"
            raise ValueError(message)
        return UserDto(
            id=entity.id,
            first_name=entity.first_name,
            second_name=entity.second_name,
            first_surname=entity.first_surname,
            second_surname=entity.second_surname,
            gender=entity.gender.value.value,
        )
