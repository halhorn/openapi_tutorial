from unittest import TestCase
from openapitutorial.entity.interest import Interest


class TestInterest(TestCase):
    def test_serializable(self):
        value = Interest.PHOTO.to_serializable()
        self.assertEqual(Interest.from_serializable(value), Interest.PHOTO)
