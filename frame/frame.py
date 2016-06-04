#!/usr/bin/env python
"""
    ===
    frame.py
    ===

    Write a function that takes a list of strings an prints them, one per line,
    in a rectangular frame. For example the list
    ["Hello", "World", "in", "a", "frame"] gets printed as:
    *********
    * Hello *
    * World *
    * in    *
    * a     *
    * frame *
    *********
"""

def frame(list):
    # get longest string in list to determine size of top/bottom of frame
    longest_string_len = len(max(list, key=len))

    longest_star_len = longest_string_len + 4
    longest_star_string = '*' * (longest_string_len + 4) + '\n';

    # initialize return string with top of the frame
    retstr = longest_star_string

    # build out each row of the string
    for string in list:
        # calculate number of special characters need for a row not including
        # the length of the current word in the loop
        row_spec_len = longest_star_len - len(string)

        rowstr = '* ' + string + ((row_spec_len - 3) * ' ') + '*\n'

        # concatenate row to frame
        retstr = retstr + rowstr

    # close out return string with bottom of frame
    retstr = retstr + longest_star_string
    
    return retstr

print (frame(["Hello", "World", "in", "a", "frame"]))