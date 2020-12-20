#!/bin/python3

import math
import os
import random
import re
import sys

'''
Problem Description
There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
The player must avoid the thunderheads.
 Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.
It is always possible to win the game.

For each game, you will get an array of clouds numbered 0
if they are safe or 1 if they must be avoided. 
'''


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    length = len(c) - 1
    moves = 0
    current_cloud = 0
    while True:
        #if current cloud is not end or the second to last step
        if current_cloud < length-1:
            #only 1 short hop available
            if c[current_cloud+1] == 0 and c[current_cloud+2] != 0:
                moves += 1
                current_cloud = current_cloud+1
            #if they can do a long hop
            elif c[current_cloud+2] == 0:
                moves += 1
                current_cloud = current_cloud+2
                if current_cloud == length:
                    return moves
        #only 1 short hop to the end
        else:
            moves += 1
            return moves

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
