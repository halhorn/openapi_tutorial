from enum import Enum
from .serializable import SerializableType


class Gendar(Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    def to_serializable(self) -> SerializableType:
        return self.value

    @classmethod
    def from_serializable(self, value: SerializableType) -> 'Gendar':
        return Gendar(value)
