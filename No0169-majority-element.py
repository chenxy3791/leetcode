""" 
169. Majority Element
Given an array of size n, find the majority element. The majority element 
is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
"""
解题思路1：
先排序再数。数到不同的计数器就清零。
数到某个满足条件就中止。
数到最后仍没有则返回false
"""
class Solution:
    #def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        cnt = 1
        k = 1
        while k < len(nums):
            if nums[k] == nums[k-1]:
                cnt += 1
                if cnt > int(len(nums)/2):
                    return nums[k]
            else:
                cnt = 1
            k += 1
        return None
        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase1 ...')
    nums = [3,2,3]
    print(sln.majorityElement(nums))

    print('\nTestcase2 ...')
    nums = [2,2,1,1,1,2,2]
    print(sln.majorityElement(nums))

    print('\nTestcase1 ...')
    nums = [3,2]
    print(sln.majorityElement(nums))
