#!/usr/bin/env python
"""
    ===
    rtotal.py
    ===

    Problem No. 5 in `Lists, Strings`
    Write three functions that compute the sum of the numbers in a list: using
    a for-loop, a while-loop and recursion.
"""

def sum_for(list):
    ret = 0
    for number in list:
        ret += number
    return ret

def sum_while(list):
    counter = 0
    ret = 0
    while (counter < len(list)):
        ret += list[counter]
        counter += 1
    return ret

print (sum_for([1,2,3]))
print (sum_while([1,2,3]))