from typing import List, Dict, Optional
from werkzeug.exceptions import Unauthorized


def call(api_key: str, required_scopes: None) -> Dict:
    auth = AuthData.get(api_key)
    if auth is None:
        raise Unauthorized()
    return {
        'sub': auth.user_id,
        'scope': auth.scopes,
    }


class AuthData:
    api_key: str
    user_id: str
    scopes: List[str]

    def __init__(self, api_key: str, user_id: str, scopes: List[str]) -> None:
        self.api_key = api_key
        self.user_id = user_id
        self.scopes = scopes

    @classmethod
    def get(cls, api_key: str) -> Optional['AuthData']:
        record = cls._get_data_from_db(api_key)
        return cls(**record) if record else None

    @classmethod
    def _get_data_from_db(cls, api_key: str) -> Optional[Dict]:
        # TODO: implement
        data = {
            'abcd1234-1': {
                'user_id': 'halhorn',
                'scopes': ['user:read', 'user:write'],
                'api_key': 'abcd1234-1',
            },
            'abcd1234-2': {
                'user_id': 'nisehorn',
                'scopes': ['user:read'],
                'api_key': 'abcd1234-2',
            },
        }
        return data.get(api_key)
