# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 10:27:07 2023

@author: chenxy
1041. Robot Bounded In Circle
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.

Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt
from collections import deque
import itertools as it
import bisect

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        Assuming the {0,1,2,3} represents {East, North, West, South}
        '''
        def move(start_state, cmd):
            x,y,orient = start_state
            if cmd == 'G':
                if orient == 0:     # East
                    x = x + 1
                elif orient == 1:   # North
                    y = y + 1
                elif orient == 2:   # West 
                    x = x - 1
                else:               # South
                    y = y - 1                    
            elif cmd == 'L':
                orient = (orient + 1)%4
            else:
                orient = (orient - 1)%4
                        
            return (x,y,orient)
        
        start0 = (0,0,1)
        start  = start0
        round_cnt = 0
        while round_cnt < 4:
            for cmd in instructions:
                end = move(start,cmd)
                # print(cmd, start, end)
                start = end
            if end == start0:
                return True
            round_cnt += 1
            
        return False
            
if __name__ == '__main__':

    sln  = Solution()                
    
    instructions = "GGLLGG"
    print(sln.isRobotBounded(instructions))        
    
    instructions = "GG"
    print(sln.isRobotBounded(instructions))        
    
    instructions = "GL"
    print(sln.isRobotBounded(instructions))        