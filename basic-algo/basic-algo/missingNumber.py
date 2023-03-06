""" 
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

import time
import math

class Solution:
    #def missingNumber(self, nums: List[int]) -> int:
    def missingNumber(self, nums) -> int:
        nums.sort()
        for k in range(len(nums)):
            if k != nums[k]:
                return k
        return k+1


if __name__ == '__main__':

    sln   = Solution()

    print('Testcase1...')
    tStart = time.time()        
    nums = [3,0,1]
    print('expected = 2, actual = {0}'.format(sln.missingNumber(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase2...')
    tStart = time.time()        
    nums = [9,6,4,2,3,5,7,0,1]
    print('expected = 8, actual = {0}'.format(sln.missingNumber(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    print('Testcase3...')
    tStart = time.time()        
    nums = [0]
    print('expected = 1, actual = {0}'.format(sln.missingNumber(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')