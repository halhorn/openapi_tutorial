from typing import Dict, Optional
from werkzeug.exceptions import Forbidden, NotFound
from openapitutorial.entity.serializable import SerializableType
from openapitutorial.entity.gendar import Gendar
from openapitutorial.entity.interest import Interest
from openapitutorial.entity.user import User


def call(
        user_id: str,  # URL パラメータの user_id の値
        user: str,  # auth.call で api_key から引っ張ってきたユーザー ID (sub の中身)
        token_info: Dict,  # auth.call の返り値の dict
) -> SerializableType:
    if user_id != user or 'user:read' not in token_info['scope']:
        raise Forbidden()
    got_user = _get_user_from_db(user_id)
    if got_user is None:
        raise NotFound()
    return got_user.to_serializable()


def _get_user_from_db(user_id: str) -> Optional[User]:
    data = {
        'halhorn': User(
            user_id='halhorn',
            name='信田春満',
            mail_address='halhorn@exmaple.com',
            age=32,
            gendar=Gendar.MALE,
            interests=[Interest.BOULDERING, Interest.PHOTO],
        ),
        'nisehorn': User(
            user_id='nisehorn',
            name='偽田偽満',
            mail_address='nisehorn@exmaple.com',
            age=3,
            gendar=Gendar.OTHER,
        ),
    }
    return data.get(user_id)
