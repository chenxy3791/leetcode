""" 
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true     

IDEA: Usually, for array-related problems, sorting the array first is wise choice.

"""

import time

class Solution:
    # Surpass time limit.
    def containsDuplicate(self, nums) -> bool:
        for k in range(1,len(nums)):
            for j in range(k):
                if nums[j] == nums[k]:
                    return True
        
        return False

    def containsDuplicate2(self, nums) -> bool:
        # sort it first
        nums.sort()        
        for k in range(len(nums)-1):
            if nums[k] == nums[k+1]:
                    return True
        
        return False

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = []
    print(sln.containsDuplicate(nums))

    # Testcase1
    print('Testcase1...')
    nums = [2,2]
    print(sln.containsDuplicate(nums))

    # Testcase2
    print('Testcase2...')
    nums = [2,3,4,2,1,2,3]
    print(sln.containsDuplicate(nums))

    # Testcase3
    print('Testcase3...')
    nums = [x for x in range(10000)]
    nums.append(9999)

    tStart = time.time()    
    print(sln.containsDuplicate(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()    
    nums = [x for x in range(100000)]
    nums.append(99999)
    print(sln.containsDuplicate2(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
