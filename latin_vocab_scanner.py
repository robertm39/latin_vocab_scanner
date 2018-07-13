# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:14:20 2018

@author: rober
"""

import ast
import requests as rq

import html_tree_parser as hp

_CACHE = {}

def load_cache():
    global _CACHE
    
    with open('cache.txt') as c_file:
        text = c_file.read()
        try:
            _CACHE = ast.literal_eval(text)
        except SyntaxError:
            _CACHE = {}

load_cache()

def save_cache():
    global _CACHE
    
    with open('cache.txt', 'w') as c_file:
        c_file.write(repr(_CACHE))

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def requests_retry_session(retries=10, backoff_factor=0.01, status_forcelist=(500, 502, 504), session=None):
    session = session or rq.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def get_response(word):
    parser = hp.TreeParser()
#    data = rq.get('http://archives.nd.edu/cgi-bin/wordz.pl?keyword=' + word.lower())
    data = requests_retry_session().get('http://archives.nd.edu/cgi-bin/wordz.pl?keyword=' + word.lower(),
                                        timeout=10)
    html = data.text
    parser.feed(html)
    return parser.stack[0].children[0].children[1].children[1].children

def is_entry(line):
    if 'UNKNOWN' in line:
        return True
    if '[' in line and ']' in line:
        ind1 = line.index('[')
        ind2 = line.index(']')
        if ind2 - ind1 == 6 and ind1 != 0:
            return True

def get_possible_entries(word, verbose=False):
    word = word.lower()
    if not word in _CACHE:
        response = get_response(word)
        if verbose:
            print(word)
        result = []
        prev = ''
        for line in response:
            line = line.strip()
            if is_entry(line):
                result.append(line)
            elif line[0] == '[':
                result.append(prev + ' ' + line)
            prev = line
            
        _CACHE[word] = result
        save_cache()
        return result
    else:
        if verbose:
            print('CACHED ' + word)
        return _CACHE[word]

clean_dict = {'Ā':'A',
              'ā':'a',
              'Ē':'E',
              'ē':'e',
              'Ī':'I',
              'ī':'i',
              'Ō':'O',
              'ō':'o',
              'Ū':'U',
              'ū':'u',
              'Æ':'Ae',
              'Ǣ':'Ae',
              'æ':'ae',
              'ǣ':'ae',
              'Œ':'Oe',
              'œ':'oe',}

remove = ',.<>;\':\"/?[{]}\\|`~!@#$%^&*()-–—_=+0123456789'

def clean_text(text):
    result = []
    for char in text:
        while char in clean_dict:
            char = clean_dict[char]
        if not char in remove:
            result.append(char)
    return ''.join(result)

def get_all_entry_possibilities(text, verbose=False):
    text = clean_text(text)
    words = text.split()
    possibilities = [get_possible_entries(word, verbose=verbose) for word in words]
    save_cache()
    return possibilities

def all_possible_entries(entry_possibilities):
    result = []
    for poss in entry_possibilities:
        result.extend(poss)
    result = list(set(result))
    result.sort(key=lambda s:s.lower())
    return result

















