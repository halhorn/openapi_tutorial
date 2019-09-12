from typing import Union, Dict, List
from typing_extensions import Protocol

SerializableType = Union[Dict, List, str, int, float, bool]


class Serializable(Protocol):
    def to_serializable(self) -> SerializableType:
        ...

    @classmethod
    def from_serializable(cls, value: SerializableType) -> 'Serializable':
        ...
