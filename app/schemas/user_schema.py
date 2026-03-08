from pydantic import BaseModel, ConfigDict, Field

from app.schemas.helper_schema import Gender


class UserSchema(BaseModel):
    """Data transfer object for a user."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    second_name: str | None = None
    first_surname: str
    second_surname: str | None = None
    gender: Gender


class UserCreateSchema(BaseModel):
    """Data transfer object for creating a user."""

    password: str = Field(..., min_length=8)
    first_name: str = Field(..., min_length=3, max_length=50)
    second_name: str | None = None
    first_surname: str = Field(..., min_length=3, max_length=50)
    second_surname: str | None = None
    gender: Gender
