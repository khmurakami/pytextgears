#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from pytextgears.utils import *


textgear = TextGear("insert api key here")
raw_json = textgear.grammar_checker("I is an engeneer")
print(raw_json)

return_json_file(raw_json, "grammar_checker.json")
