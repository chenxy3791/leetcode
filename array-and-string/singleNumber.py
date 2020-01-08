""" 
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""

import time

class Solution:
    #def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums) -> int:
        if len(nums)%2 == 0:
            print("Warning: don't accept empty array of even length array as input!")
            return -1
        if len(nums) == 1:
            return nums[0]
        
        # sort it first
        nums.sort()        
        k = 0
        while (k < len(nums)-2):
        #for k in range(len(nums)-1):
            if nums[k] != nums[k+1]:
                return nums[k]
            else:
                k = k+2

        return nums[-1]

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = []
    print(sln.singleNumber(nums))

    # Testcase1
    print('Testcase1...')
    nums = [2,2,1]
    print(sln.singleNumber(nums))

    # Testcase2
    print('Testcase2...')
    nums = [4,1,2,1,2]
    print(sln.singleNumber(nums))

    # Testcase3
    print('Testcase3...')
    nums = []
    N = 100000
    for k in range(N):
        nums.append(k)
        nums.append(k)
    nums.append(N)
 
    print(nums[0:10])
 
    tStart = time.time()    
    print(sln.singleNumber(nums))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
