""" 
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

import time

class Solution:
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target: int):
        nums_copy = nums.copy()
        nums_copy.sort()

        fPtr = 0
        bPtr = len(nums) - 1
        while fPtr < bPtr:
            if nums_copy[fPtr] + nums_copy[bPtr] == target:
                if nums_copy[fPtr] != nums_copy[bPtr]:
                    idx1 = nums.index(nums_copy[fPtr])
                    idx2 = nums.index(nums_copy[bPtr])
                else:
                    idx1 = nums.index(nums_copy[fPtr])
                    nums.remove(nums_copy[fPtr])
                    idx2 = nums.index(nums_copy[bPtr]) + 1

                return [idx1, idx2]
            elif nums_copy[fPtr] + nums_copy[bPtr] > target:
                bPtr = bPtr - 1
            else:
                fPtr = fPtr + 1       

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = [2, 7, 11, 15]
    target = 9
    print(sln.twoSum(nums, target))

    # Testcase1
    print('Testcase1...')
    nums = [3, 2, 4]
    target = 6
    print(sln.twoSum(nums, target))

    # Testcase2
    print('Testcase2...')
    nums = [3, 3]
    target = 6
    print(sln.twoSum(nums, target))