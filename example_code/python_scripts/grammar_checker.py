#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script uses grammar_checker to check the grammar of the sentence

from pytextgears import TextGear
from pytextgears.utils import *

# Create a TextGear object
textgear = TextGear("insert api key here")

# Use sample sentence from TextGear API documentation
raw_json = textgear.grammar_checker("I is an engeneer")
print(raw_json)

# Use the utils library to download beautified .json file to
return_json_file(raw_json, "../sample_json_output/grammar_checker.json")
