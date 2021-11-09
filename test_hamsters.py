import unittest

from Hamster import Hamster
from main import buy_hamsters


def fill_array():
    hamsters = []
    for i in range(1, 6):
        hamsters.append(Hamster(i, i))

    return hamsters


class TestHamsters(unittest.TestCase):

    def test_by_hamsters(self):
        self.assertEqual(buy_hamsters(fill_array(), 50, 5), 4)
