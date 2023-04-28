# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:20:20 2023

@author: chenxy

1172. Dinner Plate Stacks
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.
 

Example 1:

Input
["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
[[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
Output
[null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
 

Constraints:

1 <= capacity <= 2 * 10**4
1 <= val <= 2 * 10**4
0 <= index <= 10**5
At most 2 * 10**5 calls will be made to push, pop, and popAtStack.
"""
import time
import random
from typing import List, Optional
from collections import defaultdict
import time
import numpy as np
from math import sqrt, inf
from collections import deque
import itertools as it
from bisect import bisect, bisect_left, bisect_right

# class DinnerPlates:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.stacks = []

#     def push(self, val: int) -> None:
#         if len(self.stacks) == 0:
#             stack = deque([val])
#             self.stacks.append(stack)
#         else:
#             for i in range(len(self.stacks)):                
#                 if len(self.stacks[i]) < self.capacity:
#                     self.stacks[i].append(val)
#                     return
#             stack = deque([val])
#             self.stacks.append(stack)            
#             return
        
#     def pop(self) -> int:
#         # for i in range(len(self.stacks),-1,-1):
#         #     if len(self.stacks[i]) > 0:
#         #         val = self.stacks[i].pop()
#         #         if len(self.stacks[i]) == 0:
#         #             self.stacks.pop(i)
#         #         return 
#         if len(self.stacks) > 0:
#             val = self.stacks[-1].pop()
#             if len(self.stacks[-1]) == 0:
#                 self.stacks.pop(-1)
#             return val
#         else:
#             return -1        

#     def popAtStack(self, index: int) -> int:        
#         if len(self.stacks) < index+1:
#             return -1
#         val = self.stacks[index].pop()
#         if len(self.stacks[index]) == 0:
#             self.stacks.pop(index)
#         return val

from sortedcontainers import *
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.top = []
        self.poppedPos = SortedSet()

    def push(self, val: int) -> None:
        if not self.poppedPos:
            pos = len(self.stacks)
            self.stacks.append(val)
            if pos % self.capacity == 0:
                self.top.append(0)
            else:
                stackPos = len(self.top) - 1
                stackTop = self.top[stackPos]
                self.top[stackPos] = stackTop + 1
        else:
            pos = self.poppedPos.pop(0)
            self.stacks[pos] = val
            index = pos // self.capacity
            stackTop = self.top[index]
            self.top[index] = stackTop + 1

    def pop(self) -> int:
        while self.stacks and self.poppedPos and self.poppedPos[-1] == len(self.stacks) - 1:
            self.stacks.pop()
            pos = self.poppedPos.pop()
            if pos % self.capacity == 0:
                self.top.pop()
        if not self.stacks:
            return -1
        else:
            pos = len(self.stacks) - 1
            val = self.stacks[pos]
            self.stacks.pop()
            if pos % self.capacity == 0 and self.top:
                self.top.pop()
            elif self.top:
                self.top[-1] -= 1
            return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.top):
            return -1
        stackTop = self.top[index]
        if stackTop < 0:
            return -1
        self.top[index] = stackTop - 1
        pos = index * self.capacity + stackTop
        self.poppedPos.add(pos)
        return self.stacks[pos]


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

if __name__ == '__main__':

    # cmds = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
    # vals = [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]

    # cmds = ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
    # vals = [[2],[1],[2],[3],[4],[7],[8],[20],[21],[0],[2],[],[],[],[],[]]

    cmds = ["DinnerPlates","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
    vals = [[2],[373],[86],[395],[306],[370],[94],[41],[17],[387],[403],[66],[82],[27],[335],[252],[6],[269],[231],[35],[346],[4],[6],[2],[5],[2],[2],[7],[9],[8],[1],[474],[216],[256],[196],[332],[43],[75],[22],[273],[101],[11],[403],[33],[365],[338],[331],[134],[1],[250],[19],[],[],[],[],[],[],[],[],[],[]]
    
    output = []
    for k in range(len(cmds)):
        if cmds[k] == "DinnerPlates":
            obj = DinnerPlates(vals[k][0])
            output.append(None)
        elif cmds[k] == "push":
            obj.push(vals[k][0])
            output.append(None)
            print(cmds[k], obj.stacks)
        elif cmds[k] == "pop":
            output.append(obj.pop())
            print(cmds[k], obj.stacks)
        elif cmds[k] == "popAtStack":
            output.append(obj.popAtStack(vals[k][0]))
            print(cmds[k], obj.stacks)
        else:
            ValueError()
                
    print(output)  
    
