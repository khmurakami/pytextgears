#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from pytextgear.utils import *

textgear = TextGear("")
raw_json = textgear.grammar_checker("I is an engeneer")
result = return_all_error_to_sugesstion(raw_json)
print(result)

return_json_file(raw_json, "return_all_error_to_suggestion.json")
