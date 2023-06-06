#!/usr/bin/env python3
import unittest
from Reverse_String import reverse_Operation

class ReverseString(unittest.TestCase):
    def test_basic(self):
        testcase = "Ankylosaurus"
        expected = "suruasolyknA"
        self.assertEqual(reverse_Operation(testcase), expected)
    def test_empty(self):
        testcase = ""
        expected = "You have entered an empty string or a string without content."
        self.assertEqual(reverse_Operation(testcase), expected)
    def test_empty1(self):
        testcase = " "
        expected = "You have entered an empty string or a string without content."
        self.assertEqual(reverse_Operation(testcase), expected)
unittest.main()