#!/usr/bin/env python
"""
    ===
    rtotal.py
    ===

    Problem No. 5 in `Lists, Strings`
    Write a function that computes the running total of a list
"""

def rtotal(list):
    ret = []
    holder = 0
    for number in list:
        running = holder + number
        ret.append(running)
        holder = running
    return ret

print (rtotal([1, 2, 3]))