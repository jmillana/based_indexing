from unittest import TestCase

from based_indexing import range


class TestList(TestCase):

    def test_simple_range(self):
        expected = [
            "first",
            "second",
            "third",
            "fourth",
            "fifth",
            "sixth",
            "seventh",
            "eighth",
            "ninth",
        ]
        result = []
        for i in range("ninth"):
            result.append(i)
        self.assertEqual(result, expected)

    def test_start_and_end(self):
        expected = [
            "one thousand and eight",
            "one thousand and ninth",
        ]
        result = []
        for i in ("one thousand and eight", "one thousand and ninth"):
            result.append(i)

        self.assertEqual(result, expected)

    def test_range_with_steps(self):
        expected = [
            "first",
            "third",
            "fifth",
            "seventh",
            "ninth",
        ]
        result = []
        for i in range("first", "ninth", "second"):
            result.append(i)
        self.assertEqual(result, expected)
