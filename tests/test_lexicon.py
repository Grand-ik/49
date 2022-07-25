from unittest import TestCase
from Lexicon.lexicon import *


class LexiTest(TestCase):
    def test_directions(self):
        self.assertEqual(scan("north"), [('direction', 'north')])

    def test_verbs(self):
        self.assertEqual(scan("go"), [('verb', 'go')])

    def test_stops(self):
        self.assertEqual(scan("the"), [('stop', 'the')])

    def test_nouns(self):
        self.assertEqual(scan("bear", [('noun', 'bear')]))

    def test_numbers(self):
        self.assertEqual(scan("1234"), [('numb', 1234)])

    def test_error(self):
        self.assertEqual(scan("ASDF"), [('error', 'ASDF')])