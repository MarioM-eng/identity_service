from dataclasses import dataclass


@dataclass(frozen=True)
class UserDto:
    """Data transfer object for creating a user."""

    id: int
    first_name: str
    second_name: str | None
    first_surname: str
    second_surname: str | None
    gender: str


@dataclass(frozen=True)
class CreateUserDto:
    """Data transfer object for creating a user."""

    password: str
    first_name: str
    second_name: str | None
    first_surname: str
    second_surname: str | None
    gender: str
