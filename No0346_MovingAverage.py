""" 
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3.

"""

import time

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size   = size
        self.data   = []
        self.dLen   = 0

    def next(self, val: int) -> float:
        self.data.append(val)
        self.dLen += 1
        if self.dLen < self.size:
            cumLen = self.dLen
        else:
            cumLen = self.size

        sum = 0
        for k in range(cumLen):
            sum = sum + self.data[-1-k]
        return sum/cumLen
        
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':

    print('Testcase#1 ...... start!')
    mAver   = MovingAverage(3)

    print(mAver.next(1))
    print(mAver.next(10))
    print(mAver.next(3))
    print(mAver.next(5))


