""" 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle. 
"""

import time
import math

class Solution:
    #def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArrayNG(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxSumTmp = self.maxSubArray(nums[0:-1])        
        if maxSumTmp <= 0 and nums[-1] >= 0:
            maxSum = nums[-1]
        elif maxSumTmp <= 0 and nums[-1] < 0:
            maxSum = max(maxSumTmp, nums[-1])
        elif maxSumTmp > 0 and nums[-1] > 0:
            maxSum = maxSumTmp + nums[-1]
        else:
            maxSum = maxSumTmp        
        
        print('nums = {0}, maxSum = {1}'.format(nums, maxSum))

        return maxSum

    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        end   = 0
        maxSum= nums[end]
        curSum= nums[end]
        while end < len(nums) - 1:
            end = end + 1
            if curSum <= 0:
                start = end
                curSum = nums[end]                
            else:
                curSum += nums[end]

            maxSum = max(maxSum, curSum)

        return maxSum

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    tStart = time.time()        
    print('Testcase1...')
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sln.maxSubArray(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # Testcase2 
    tStart = time.time()        
    print('Testcase2...')
    nums = [-2,1,-1,1,-1,2,1,-5,4,3,4,-1,-2,1,2,-3,5]
    print(sln.maxSubArray(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
