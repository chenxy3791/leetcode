""" 
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2. 
"""

#import time
#import math
#import random

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #print('__init__()...')

        self.stack = []       
        self.minV  = None
        self.size  = 0

    def push(self, x: int) -> None:
        #print('push()...')

        self.stack.append(x)
        #if self.minPtr == None:
        if self.size == 0:
            #self.minPtr = 0
            self.minV   = x
            self.size   = 1
        else:
            if self.minV > x:
                self.minV = x
                #self.minPtr = self.size                            
            self.size   += 1

    def pop(self) -> None:
        #print('pop()...')
        if self.size == 1:            
            self.minV  = None
            ##self.minPtr= None
        else:
            if self.minV == self.stack[-1]:                        
                # Search to determine the new minimum
                self.minV   = self.stack[0]
                k = 1
                while k < self.size-1:
                    if self.minV > self.stack[k]:
                        self.minV = self.stack[k]
                    k += 1
        self.stack.pop()
        self.size -= 1

    def top(self) -> int:
        #print('top()...')
        if self.size == 0:
            return None
        else:
            return self.stack[-1]
    
    def getMin(self) -> int:
        #print('getMin()...')
        return self.minV
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())    #--> Returns -3.
    minStack.pop()
    print(minStack.top())       #--> Returns 0.
    print(minStack.getMin())    #--> Returns -2. 
