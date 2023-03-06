""" 
300. Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
"""
解题思路：
最终的最长子序列的起始数一定是到该数为止的最小数。但是这并不意味着最长序列起始于数组中的最小元素。
难点在于子序列并不要求是连续的。
前向遍历搜索，如果nums[k]为新的最小值，则记录更新到目前为止的最长子序列长度，并重启新的升序子序列的搜索。
"""
class Solution:
    #def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        res = [nums[0]]
        for k in range(1,len(nums)):
            if nums[k] > res[-1]:
                res.append(nums[k])
            else:    
                kk = len(res)-2
                while kk >= 0:
                    if nums[k] > res[kk]:
                        res[kk+1] = nums[k]
                        break
                    kk -= 1
                if kk == -1:
                    res[0] = nums[k]
        return len(res)


#class Solution:
#    def lengthOfLIS(self, nums: List[int]) -> int:
#        if len(nums) <= 1:
#            return len(nums)

#        dp = [1 for i in range(len(nums))]

#        for k in range(1,len(nums)):
#            maxV = 1
#            for kk in range(0,k):
#                if nums[k] > nums[kk]:
#                    tmpV = dp[kk] + 1
#                    if tmpV > maxV:
#                        maxV = tmpV
#            dp[k] = maxV
#
#        return max(dp)


        
if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase1 ...')
    nums = [10,9,2,5,3,7,101,18]
    print(sln.lengthOfLIS(nums))

    print('\nTestcase2 ...')
    nums = [2,2,1,1,1,2,2]
    print(sln.majorityElement(nums))

    print('\nTestcase3 ...')
    nums = [3,2]
    print(sln.majorityElement(nums))
