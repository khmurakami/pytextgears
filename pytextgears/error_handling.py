#!/usr/bin/env python
# -*- coding: utf-8 -*-


def grammar_error_checker(raw_json):

    '''Checks to the see the key pair in the raw json 'result' is true

    Args:
        raw_json (dict): Raw JSON output from grammar checker

    Return boolean: True if the result is true. False if result is false

    '''

    status = raw_json['result']
    if status is "true":
        return True
    else:
        return False

def http_error_handler(http_status_code):

    '''Displays reason for http status code

    Args:
        http_status_code (int): The status code output by the request
    '''

    if http_status_code == 600:
        raise Exception("600: Invalid license key. Go to https://textgears.com/signup.php to get a key")
    elif http_status_code == 601:
        raise Exception("601: Too many requests per second. By default the number of requests per second is limited to 8.")
    elif http_status_code == 602:
        raise Exception("602: Month request limit exceeded. Each plan has its month request limit. You can buy some extra requests or renew your plan.")
    elif http_status_code == 603:
        raise Exception("603: Too many requests per day. Too many requests was sent by your application during the last 24 hours. You should buy some extra requests or renew you license to the next plan.")
    elif http_status_code == 605:
        raise Exception("605: 	License key cannot be empty. Add key parameter to the request.")
    elif http_status_code == 500:
        raise Exception("500: General API error.")
    elif http_status_code == 501:
        raise Exception("501: Text input is too long. Max text length is 32768 chars.")
    elif http_status_code == 605:
        raise Exception("502: Too many errors. Not English?")
    else:
        return None
