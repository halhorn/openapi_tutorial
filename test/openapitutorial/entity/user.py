from unittest import TestCase
from openapitutorial.entity.gendar import Gendar
from openapitutorial.entity.interest import Interest
from openapitutorial.entity.user import User


class TestUser(TestCase):
    def test_serializable(self):
        args = dict(
            user_id='halhorn',
            name='信田春満',
            mail_address='halhorn@exmaple.com',
            age=32,
            gendar=Gendar.MALE,
            interests=[Interest.BOULDERING, Interest.PHOTO],
        )
        value = User(**args).to_serializable()
        self.assertEqual(User.from_serializable(value), User(**args))
