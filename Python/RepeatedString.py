#!/bin/python3

import math
import os
import random
import re
import sys

'''
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer,n, 
find and print the number of letter a's in the first n
letters of the infinite string.

Example
s = 'abcac'
n = 10

The substring we consider is abcacabcac, 
the first characters of the infinite string. There are 4
occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

Returns

    int: the frequency of a in the substring

Input Format

The first line contains a single string, s
.
The second line contains an integer, n.
'''



# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    # get the amount of character a in the string
    first_string_chars = s.count('a')
    if first_string_chars == 0:
        return 0
    elif first_string_chars == 1 and length == 1:
        return n
    else:
        # get the amount with full strings
        total = first_string_chars * int((n / length))
        # check the rest of the characters
        remainder = int(n % length)
        return total + s[:remainder].count('a')

if __name__ == '__main__':


    s = input()

    n = int(input())

    result = repeatedString(s, n)
