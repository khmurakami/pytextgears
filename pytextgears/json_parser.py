#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
from .utils import *

import os

#API_KEY = os.environ['PYTEXTGEARS_KEY']

def return_error_list(raw_json):

    '''Return all json in the error list individually

    Args: raw_json (dict): Raw JSON output from grammar checker

    Return error_list (list): List of JSON dicts

    '''

    error_list = raw_json['errors']
    return error_list

def return_first_error(raw_json):

    '''Return the first error json

    Args: raw_json (dict): Raw JSON output from grammar checker

    Return first_error (dict): Raw JSON dict

    '''
    error_list = raw_json['errors']
    first_error = error_list[0]
    return first_error

def return_all_bad_error_text(raw_json):

    '''Return all error words in the json

    Args: raw_json (dict): Raw JSON output from grammar checker

    Return bad_error_text_list (list): List of JSON dicts

    '''

    error_list = raw_json['errors']
    bad_error_text_list = []
    for error in error_list:
        bad_error_text_list.append(error['bad'])
    return bad_error_text_list

def return_all_suggestions(raw_json):

    '''Return all the suggestions to the error words

    Args: raw_json (dict): Raw JSON output from grammar checker

    Return: suggestions_text_list (list): List of JSON dicts

    '''

    error_list = raw_json['errors']
    suggestions_text_list = []

    for suggestions in error_list:
        suggestions_text_list.append(suggestions['better'])

    return suggestions_text_list

def return_all_error_to_suggestion(raw_json):

    '''Return a list of dicts pairs of error to suggestions

    Args: raw_json (dict): Raw JSON output from grammar checker

    Return result (list): List of JSON dicts
    '''

    bad_error_text_list = return_all_bad_error_text(raw_json)
    sugesstions_text_list = return_all_suggestions(raw_json)

    # Pair the bar error list as keys to sugesstions
    result = {bad_error_text_list[i]: suggestions_text_list[i] for i in range(len(bad_error_text_list))}

    return result
