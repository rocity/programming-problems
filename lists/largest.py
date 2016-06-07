#!/usr/bin/env python
"""
    ===
    largest.py
    ===

    Problem No. 1 in `Lists, Strings`
    Write a function that returns the largest element in a list.
"""

def largest(list):
    return max(list, key=len)

print (largest(['foo', 'bar', 'spam', 'fubar']))