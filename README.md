# pytextgears

[![Build Status](https://travis-ci.com/khmurakami/pytextgears.svg?token=GdqQUUu1xsypr1oorMoh&branch=master)](https://travis-ci.com/khmurakami/pytextgears)

Python Wrapper for TextGears

## Requirements

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
$ python3 -m virutalenv env
$ source env/bin/activate
$ python3 setup.py install
```

## Using the Python Wrapper

##### Checking your Grammar

```python
from pytextgears import TextGear
from pytextgears.utils import *

textgear = TextGear(API_KEY)
raw_json = textgear.grammar_checker("I is an engeneer")
print(raw_json)

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

```python

from pytextgears import TextGear
from pytextgears.utils import *
from pytextgears.json_parser import *

textgear = TextGear(API_KEY)
raw_json = textgear.grammar_checker("I is an engeneer")

# Get all error words to TextGears suggested fixes
result = return_all_error_to_suggestion(raw_json)
print(result)

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

Code samples can be found in example_code.python_scripts

Run
```shell
$ python example_code/python_scripts/grammar_checker.py
```

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python unit_test/pytextgears_tests.py
```

## TODO

- Sample code and output for all functions.
- Comment JSON parsing
- Add more error handlers
- add better test cases
