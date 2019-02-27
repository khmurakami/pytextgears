#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from pytextgear.utils import *

import unittest
import os

# Insert your own key as a string here
API_KEY = os.environ['PYTEXTGEARS_KEY']

class TestTextGearMethods(unittest.TestCase):


    def test_grammar_check(self):

        textgear = TextGear(API_KEY)
        raw_json = textgear.grammar_check("I is an engeneer")

        error_json = raw_json['errors']

        self.self.assertEqual(2, len(error_json))

if __name__ == '__main__':
    unittest.main()
