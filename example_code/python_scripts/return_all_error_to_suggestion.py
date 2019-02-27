#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from pytextgears.utils import *
from pytextgears.json_parser import *

textgear = TextGear("")
raw_json = textgear.grammar_checker("I is an engeneer")
result = return_all_error_to_suggestion(raw_json)
print(result)

return_json_file(raw_json, "../sample_json_output/return_all_error_to_suggestion.json")
