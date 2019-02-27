#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from pytextgear.utils import *


textgear = TextGear()
raw_json = textgear.grammar_check("I in am engeer")
print(raw_json)

return_json_file(raw_json, "grammar_check.json")
