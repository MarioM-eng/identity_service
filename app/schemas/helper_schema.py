from collections.abc import Sequence
from enum import StrEnum, auto
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class ResponseSchema(BaseModel):
    """Generic response schema."""

    model_config = ConfigDict(from_attributes=True)

    success: bool = True
    message: str = Field(..., description="Message of the response")
    total_rows: int = Field(default=1, description="Total number of rows")


class SequenceResponseSchema(ResponseSchema, Generic[T]):
    """Response schema for sequences."""

    data: Sequence[T] = Field(..., description="Data of the response")


class SingleResponseSchema(ResponseSchema, Generic[T]):
    """Response schema for single items."""

    data: T | None = Field(..., description="Data of the response")


class Gender(StrEnum):
    """Gender enum class."""

    MALE = auto()
    FEMALE = auto()
    OTHER = auto()
