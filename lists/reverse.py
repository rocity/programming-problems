#!/usr/bin/env python
"""
    ===
    reverse.py
    ===

    Problem No. 2 in `Lists, Strings`
    Write a function that reverses a list
"""

def reverse_list(list):
    a = list
    a.reverse()
    return a

print (reverse_list(['one', 'two', 'foo']))