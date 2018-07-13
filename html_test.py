# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:16:41 2018

@author: rober
"""

import requests as rq

import html_tree_parser as htp

parser = htp.TreeParser()
data = rq.get('http://archives.nd.edu/cgi-bin/wordz.pl?keyword=sic')
html = data.text
print(html)
print('')
parser.feed(html)
print(parser.stack[0])