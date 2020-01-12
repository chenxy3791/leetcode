""" 
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""
import time

class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def findMaxConsecutiveOnes(self, nums):
        nNums = len(nums)
        # Ignore the validity check, assuming the valid input data.
        if nNums == 0:
            return 0
        
        maxLen = 0
        start  = -1
        oneLen = 0

        for k in range(nNums):
            if start==-1 and nums[k] == 1:
                start = k
                oneLen = oneLen + 1
            elif start>=0 and nums[k] == 1:
                oneLen = oneLen + 1
            elif start>=0 and nums[k] == 0:
                if maxLen < oneLen:
                    maxLen = oneLen
                oneLen = 0
                start  = -1

        # For handle the last part of list is consecutive ones segment
        if maxLen < oneLen:
            maxLen = oneLen

        return maxLen

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1
    print('Testcase1...')
    nums = [1,1,0,1,1,1]
    print(sln.findMaxConsecutiveOnes(nums))    

    # Testcase2
    print('Testcase2...')
    nums = [1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0]
    print(sln.findMaxConsecutiveOnes(nums))    
