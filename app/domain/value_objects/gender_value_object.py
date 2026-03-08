from dataclasses import dataclass
from enum import Enum


class GenderType(Enum):
    """Gender type enum."""

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


@dataclass(frozen=True)
class GenderVO:
    """Gender value object."""

    value: GenderType

    @classmethod
    def from_str(cls, gender_str: str) -> "GenderVO":
        """Create a GenderVO from a string representation of the gender."""
        try:
            return cls(value=GenderType(gender_str.lower()))
        except ValueError:
            error_message = f"'{gender_str}' no es un género válido."
            raise ValueError(error_message) from None

    def __str__(self) -> str:
        """Return the gender value as a string."""
        return self.value.value
