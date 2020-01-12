""" 
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""
import time

class Solution:
    #def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    def minSubArrayLen(self, s: int, nums) -> int:
    
        if sum(nums) < s:
            return 0
        
        nNums = len(nums)
        minLen = nNums
                
        for k in range(nNums):
            #print('k = ',k)
            upperLimit = min(nNums, k+minLen) - 1
            curSum     = sum(nums[k:upperLimit+1])
            if curSum < s:
                if upperLimit == (nNums-1):
                    #print('No need of continual search')
                    break # No need to continue the search.
                else:
                    #print('Go to the next k')
                    continue # Go to for the next k

            j = upperLimit
            while j > k:
                curSum = curSum - nums[j]
                if curSum >= s:
                    j = j - 1
                    minLen = minLen - 1
                else:
                    # update minLen
                    #print('  ', minLen, (j-k+1))
                    if minLen > (j-k+1):
                        minLen = (j-k+1)
                    break

        return minLen

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1
    print('\nTestcase1...')
    s = 7
    nums = [2,3,1,2,4,3]
    print(sln.minSubArrayLen(s, nums))    
    
    # Testcase2
    print('\nTestcase2...')
    s = 17
    nums = [2,3,1,2,4,3]
    print(sln.minSubArrayLen(s, nums))    

    # Testcase3
    print('\nTestcase3...')
    s = 14
    nums = [2,3,1,2,4,3]
    print(sln.minSubArrayLen(s, nums))        

    # Testcase4
    print('\nTestcase4...')
    s = 13
    nums = [2,3,1,2,4,3]
    print(sln.minSubArrayLen(s, nums))            

    # Testcase5
    print('\nTestcase5...')
    s = 2
    nums = [2,3,1,2,4,3]
    print(sln.minSubArrayLen(s, nums))            