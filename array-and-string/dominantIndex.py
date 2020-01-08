""" 
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].

chenxy:
It seems that the point is how to find the max and the second to max in one iteration.
When the Max is updated, the old Max can always be transferred to the Max2.

How to initialize max1 and max2?
We can initializa both of them to nums[0], but if there is no update, i.e, nums[0] is
the maximum, then it will cause mis-judge.
Of course, we can use the knowledgr that "Every nums[i] will be an integer in the range [0, 99].".
But if we don't have this prior knowledge, how to handle this problem?

"""
import time

class Solution:
    #def dominantIndex(self, nums: List[int]) -> int:
    def dominantIndex(self, nums):
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        
        max1  = 0 # Because it is known that the nums[i] will be in the range [0,99]
        max2  = 0 # Because it is known that the nums[i] will be in the range [0,99]
        kMax1 = 0
        #kMax2 = 0

        for k in range(len(nums)):
            if max1 < nums[k]:
                # First update max2
                #kMax2 = kMax1
                max2  = max1
                # First update max1
                max1  = nums[k]
                kMax1 = k
            else:
                if max2 < nums[k]:
                    max2  = nums[k]
                    #kMax2 = k
        if max1 >= 2*max2:
            return kMax1
        else:
            return -1                                

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = []
    print(sln.dominantIndex(nums))

    nums = [1]
    print(sln.dominantIndex(nums))

    # Testcase1
    print('Testcase1...')
    nums = [3, 6, 1, 0]
    print(sln.dominantIndex(nums))

    # Testcase2
    print('Testcase2...')
    nums = [1, 2, 3, 4]
    print(sln.dominantIndex(nums))

    # Testcase3
    print('Testcase1...')
    nums = [1, 0]
    print(sln.dominantIndex(nums))
