#!/usr/bin/env python
"""
    ===
    occurs.py
    ===

    Problem No. 3 in `Lists, Strings`
    Write a function that checks if an element exists a list
"""

def occurs(list, element):
    try:
        list.index(element)
        return True
    except:
        return False

print (occurs(['foo', 'bar', 'baz'], 'foo'))
print (occurs(['foo', 'bar', 'baz'], 'fubar'))