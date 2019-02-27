#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script uses the pytextgears.json_parser library to return all error to suggestion as a dict

from pytextgears import TextGear
from pytextgears.utils import *
from pytextgears.json_parser import *

# Create a TextGear object
textgear = TextGear("")

# Use sample sentence from TextGear API documentation
raw_json = textgear.grammar_checker("I is an engeneer")

# Use the json_parser library
result = return_all_error_to_suggestion(raw_json)
print(result)

# Use the utils library to download beautified .json file to
return_json_file(result, "../sample_json_output/return_all_error_to_suggestion.json")
