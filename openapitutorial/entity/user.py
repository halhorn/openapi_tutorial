from typing import List, Dict, Optional
from .serializable import SerializableType
from .gendar import Gendar
from .interest import Interest


class User:
    user_id: str
    name: str
    mail_address: str
    age: int
    gendar: Gendar
    interests: Optional[List[Interest]]

    def __init__(
            self,
            user_id: str,
            name: str,
            mail_address: str,
            age: int,
            gendar: Gendar,
            interests: Optional[List[Interest]] = None,
    ):
        self.user_id = user_id
        self.name = name
        self.mail_address = mail_address
        self.age = age
        self.gendar = gendar
        self.interests = interests

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            return False
        return (self.user_id == other.user_id and
                self.name == other.name and
                self.mail_address == other.mail_address and
                self.age == other.age and
                self.gendar == other.gendar and
                self.interests == other.interests)

    def to_serializable(self) -> SerializableType:
        serializable = {
            'user_id': self.user_id,
            'name': self.name,
            'mail_address': self.mail_address,
            'age': self.age,
            'gendar': self.gendar.to_serializable(),
        }
        if self.interests is not None:
            serializable['interests'] = [interest.to_serializable()
                                         for interest in self.interests]
        return serializable

    @classmethod
    def from_serializable(cls, value: Dict) -> 'User':
        args: Dict = {
            **value,
            'gendar': Gendar.from_serializable(value['gendar']),
        }
        if 'interests' in args:
            args['interests'] = [Interest(interest_str)
                                 for interest_str in args['interests']]
        return cls(**args)
