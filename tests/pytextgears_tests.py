#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Check if all the libraries import correctly
from pytextgears import TextGear
from pytextgears.utils import *
from pytextgears.error_handling import *
from pytextgears.json_parser import *

# Import unittest
import unittest
import os

# Insert your own key as a string here
# Or export PYTEXTGEARS_KEY in your shell with the API Key
API_KEY = os.environ['PYTEXTGEARS_KEY']

class TestTextGearMethods(unittest.TestCase):

    def test_grammar_checker(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")

        error_json = raw_json['errors']

        self.assertEqual(2, len(error_json))

    def test_return_error_list(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")
        result = return_error_list(raw_json)

        self.assertEqual(2, len(result))

    def test_return_first_error(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")
        result = return_first_error(raw_json)

        self.assertEqual(type({}), type(result))

    def test_return_all_suggestions(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")
        result = return_all_suggestions(raw_json)

        self.assertEqual(type([]), type(result))

    def test_return_all_bad_error_text(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")
        result = return_all_bad_error_text(raw_json)

        self.assertEqual(type([]), type(result))

    def test_return_all_error_to_suggestion(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_checker("I is an engeneer")
        result = return_all_error_to_suggestion(raw_json)

        self.assertEqual(type({}), type(result))

if __name__ == '__main__':
    unittest.main()
