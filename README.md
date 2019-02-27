# pytextgears

[![Build Status](https://travis-ci.com/khmurakami/pytextgears.svg?token=GdqQUUu1xsypr1oorMoh&branch=master)](https://travis-ci.com/khmurakami/pytextgears)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CodeFactor](https://www.codefactor.io/repository/github/khmurakami/pytextgears/badge)](https://www.codefactor.io/repository/github/khmurakami/pytextgears)

pytextgears is a Python 2 and 3 library to access the TextGears API. This library allows you to access their one API call which is to check your grammar. This library also parses the JSON result.

## Requirements

This has been tested with Python 2.7, 3.3, 3.4, 3.5, 3.6 and 3.6-dev

Also listed in requirements.txt:

- requests==2.21.0

## Install

#### Install Locally

```shell
$ python setup.py install
```

#### Install inside a Virtualenv

```shell
$ pip3 install virtualenv
$ python -m virutalenv env
$ source env/bin/activate
$ python setup.py install
```

## Getting an API Key

The process is very simple to get an API Key. To sign up, go to this site right here: https://textgears.com/signup.php

You are only allowed to make 2500 requests a month with in the free tier.

## Using the Python Library

The Python Library for the request was based off this documentation site:
https://textgears.com/api/

##### Checking your Grammar

This code segment shows how to check your grammar. This uses the sample sentence from the API documentation from TextGear.

```python

from pytextgears import TextGear
from pytextgears.utils import *

# Create a textgear object
textgear = TextGear(API_KEY)

# Use grammar_checker to check your sentence
raw_json = textgear.grammar_checker("I is an engeneer")
print(raw_json)

# Use the utils library to download a beautified json
return_json_file(raw_json, "grammar_checker.json")
```

##### Result

```json
{
    "errors": [
        {
            "bad": "is",
            "better": [
                "am"
            ],
            "id": "e2071310856",
            "length": 2,
            "offset": 2,
            "type": "grammar"
        },
        {
            "bad": "engeneer",
            "better": [
                "engineer",
                "engender"
            ],
            "id": "e1196874737",
            "length": 8,
            "offset": 8,
            "type": "spelling"
        }
    ],
    "result": true
}
```

##### Parsing JSON using helper functions

All the parsing functions are in pytextgears/json_parser.py. They all take in the raw_json output from grammar_checker. This is an example of one of the json parsers that gives you a dictionary of words that are incorrect to the suggestions that TextGears output.

```python

from pytextgears import TextGear
from pytextgears.utils import *
from pytextgears.json_parser import *

# Create a textgear object
textgear = TextGear(API_KEY)
raw_json = textgear.grammar_checker("I is an engeneer")

# Get all error words to TextGears suggested fixes using the json_parser library
result = return_all_error_to_suggestion(raw_json)
print(result)

# Use the utils library to download a beautified json
return_json_file(result, "return_all_error_to_suggestion.json")
```

##### Result

```json

{
    "engeneer": [
        "engineer",
        "engender"
    ],
    "is": [
        "am"
    ]
}

```

## Samples

### Sample Python Scripts

Code samples can be found in example_code/python_scripts

Run:

```shell
$ python example_code/python_scripts/grammar_checker.py
```

### Sample JSON Output

Sample JSON output from the Python Scripts can be found in example_code/sample_json_output


## Testing using Unit Tests

Run test script to test if it works properly

```shell
# The test looks for this specific environmental variable
$ export PYTEXTGEARS_KEY='insert api key here'
$ python unit_test/pytextgears_tests.py
```

## TODO

- Sample code and output for all functions.
- Comment JSON parsing
- Add more error handlers
- add better test cases
