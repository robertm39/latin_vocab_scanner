# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:48:55 2018

@author: rober
"""

from html.parser import HTMLParser

class TreeParser(HTMLParser):
    def __init__(self):
        super.__init__()
        
        