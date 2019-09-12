from enum import Enum
from .serializable import SerializableType


class Interest(Enum):
    PHOTO = 'photo'
    BOULDERING = 'bouldering'
    TRIP = 'trip'
    CYCLING = 'cycling'
    BIRDWATCHING = 'birdwatching'

    def to_serializable(self) -> SerializableType:
        return self.value

    @classmethod
    def from_serializable(self, value: SerializableType) -> 'Interest':
        return Interest(value)
