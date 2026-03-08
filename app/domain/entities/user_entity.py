from dataclasses import dataclass

from app.domain.entities.auditable_entity import AuditableEntity
from app.domain.value_objects.gender_value_object import GenderVO


@dataclass
class UserEntity(AuditableEntity):
    """User entity."""

    id: int | None
    password: str | None
    first_name: str
    second_name: str | None
    first_surname: str
    second_surname: str | None
    gender: GenderVO
