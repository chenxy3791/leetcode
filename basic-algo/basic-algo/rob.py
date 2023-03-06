""" 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12. 
"""

import time
import math

class Solution:
    #def rob(self, nums: List[int]) -> int:
    def robWoMemoization(self, nums) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        total1 = nums[0] + self.robWoMemoization(nums[2:])
        total2 = nums[1] + self.robWoMemoization(nums[3:])

        return max([total1,total2])

    def robWithMemoization(self, nums:list, totalDict:dict):
        #print('len(nums) = {0}, totalDict = {1}'.format(len(nums), totalDict))

        if len(nums) == 0:
            totalDict[len(nums)] = 0
            return 0,totalDict
        elif len(nums) == 1:
            totalDict[len(nums)] = nums[0]
            return nums[0],totalDict
        elif len(nums) == 2:
            totalDict[len(nums)] = max(nums)
            return max(nums),totalDict

        total = totalDict.get(len(nums))
        if  total == None:
            tmp1,totalDict = self.robWithMemoization(nums[2:], totalDict)
            tmp2,totalDict = self.robWithMemoization(nums[3:], totalDict)
            total1 = nums[0] + tmp1
            total2 = nums[1] + tmp2
            total  = max([total1,total2])
            totalDict[len(nums)] = total

        return total, totalDict

    def rob(self, nums) -> int:
        totalDict = {}
        total, totalDict = self.robWithMemoization(nums, totalDict)
        return total

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    tStart = time.time()        
    print('Testcase1...')
    nums = [1,2,3,1]
    print('expected = 4, actual = {0}'.format(sln.rob(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # Testcase2 
    tStart = time.time()        
    print('Testcase2...')
    nums = [2,7,9,3,1]
    print('expected = 12, actual = {0}'.format(sln.rob(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    # Testcase2 
    tStart = time.time()        
    print('Testcase2: robWoMemoization()...')
    nums = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
    print('expected = ???, actual = {0}'.format(sln.robWoMemoization(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    print('Testcase2: rob()...')
    nums = [155,44,52,58,250,225,109,118,211,73,137,96,137,89,174,66,134,26,25,205,239,85,146,73,55,6,122,196,128,50,61,230,94,208,46,243,105,81,157,89,205,78,249,203,238,239,217,212,241,242,157,79,133,66,36,165]
    print('expected = ???, actual = {0}'.format(sln.rob(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')