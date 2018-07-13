# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 10:48:55 2018

@author: rober
"""

from html.parser import HTMLParser

class Node:
    def __init__(self, tag, attributes, children=None):
        self.tag = tag
        self.attributes = attributes
        self.children = [] if children == None else children
    
    def __str__(self):
        return self.in_str()
    
    def in_str(self, level=0):
        if self in self.children:
            print('CIRCLE')
            print('\t'*level + self.tag + ' ' + str(self.attributes))
            assert False
        result = '\t'*level + self.tag + ' ' + str(self.attributes)
        for child in self.children:
            if type(child) is type(self):
                result += '\n' + child.in_str(level=level+1)
            else:
                result += '\n' + '\t'*(level+1) + str(child)
        return result

class TreeParser(HTMLParser):
    def __init__(self):
        super(TreeParser, self).__init__()
        
        self.stack = [Node('root', [])]
    
    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        self.stack.append(node)
    
    def handle_endtag(self, tag):
        if tag != self.stack[-1].tag:
            raise AssertionError('tag:', tag, 'current tag:', self.stack[-1].tag)
        
        self.stack = self.stack[:-1] #pop top
    
    def handle_data(self, data):
        if type(data) is str:
            if len(data) > 0:
                for line in data.splitlines():
                    if len(line) > 0:
                        self.stack[-1].children.append(line)
        else:
            self.stack[-1].children.append(data)