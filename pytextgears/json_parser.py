#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytextgears import TextGear
#from pytextgear.utils import *

#API_KEY = os.environ['PYTEXTGEARS_KEY']

def return_error_list(raw_json):
    '''

    return list of json
    '''

    error_list = raw_json['errors']
    return error_list

def return_first_error(raw_json):
    '''
    return json dict
    '''
    error_list = raw_json['errors']
    first_error = error_list[0]
    return first_error

def return_all_bad_error_text(raw_json):
    '''
    return list of strings
    '''
    error_list = raw_json['errors']
    bad_error_text_list = []
    for error in error_list:
        bad_error_text_list.append(error['bad'])
    return bad_error_text_list

def return_all_suggestions(raw_json):
    '''
    return list of list of strings
    '''
    error_list = raw_json['errors']
    suggestions_text_list = []
    for suggestions in error_list:
        suggestions_text_list.append(suggestions['better'])
    return suggestions_text_list

def return_all_error_to_sugesstion(raw_json):
    '''
    return dict
    '''
    bad_error_text_list = return_all_bad_error_text(raw_json)
    sugesstions_text_list = return_all_suggestions(raw_json)
    result = {bad_error_text_list[i]: sugesstions_text_list[i] for i in range(len(bad_error_text_list))}
    return result


if __name__ == '__main__':
    textgear = TextGear("")
    raw_json = textgear.grammar_checker("I is an engeneer")
    result = return_all_error_to_sugesstion(raw_json)
    print(result)
    print(type(result))
