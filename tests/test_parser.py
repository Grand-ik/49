from Lexicon.parser import *
from unittest import TestCase


class ParserTests(TestCase):
    def test_peek(self):
        self.assertEqual(peek([("error", "1234kghj")]),
                         'error')

    def test_match(self):
        self.assertEqual(mtch([("error", "1k")], "error"),
                         ("error", "1k"))
        self.assertEqual(mtch([("error", "1234kghj")], "noun"),
                         None)