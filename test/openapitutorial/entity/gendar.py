from unittest import TestCase
from openapitutorial.entity.gendar import Gendar


class TestGendar(TestCase):
    def test_serializable(self):
        value = Gendar.FEMALE.to_serializable()
        self.assertEqual(Gendar.from_serializable(value), Gendar.FEMALE)
