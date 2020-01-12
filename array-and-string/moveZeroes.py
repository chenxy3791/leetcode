""" 
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input:  [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

import time

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        NOTE: This solution is inefficient, in the sense that the move for the trailing zeros should be skipped.

        """
        moveCnt = 0
        k = len(nums) - 1
        while k >= 0:
            if nums[k] == 0:
                #nZeros = nZeros + 1
                nums.pop(k)
                nums.append(0)
                moveCnt = moveCnt + 1
            k = k - 1

        print('Totally, {0} moves'.format(moveCnt))
        # print(nums)
        # print(nZeros)
        # nums = nums + [0]*nZeros
        # print(nums)

    def moveZeroesRefined(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        moveEnable = False
        moveCnt = 0
        k = len(nums) - 1
        while k >= 0:
            if nums[k] != 0:
                moveEnable = True
            if nums[k] == 0 and moveEnable == True:
                nums.pop(k)
                nums.append(0)
                moveCnt = moveCnt + 1
            k = k - 1

        print('Totally, {0} moves'.format(moveCnt))

if __name__ == '__main__':

    sln   = Solution()

    print('\nTestcase0...')
    nums = []
    sln.moveZeroes(nums)
    print(nums)

    print('\nTestcase1...')
    nums = [0,1,0,3,12]
    sln.moveZeroes(nums)
    print(nums)


    print('\nTestcase2...')
    nums = [0,0,0,0,0]
    sln.moveZeroes(nums)
    print(nums)


    print('\nTestcase3...')
    nums = [1,2,3,0,0,0,0,0]
    sln.moveZeroes(nums)
    print(nums)

    print('\nTestcase4...')
    nums = [1,0,2,0,3,0,0,0,0,0]
    sln.moveZeroes(nums)
    print(nums)

