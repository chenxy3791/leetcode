""" 
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

"""
import time

class Solution:
    #def arrayPairSum(self, nums: List[int]) -> int:
    def arrayPairSum(self, nums):
        # The length of nums should be even number
        assert( (len(nums) % 2) == 0)
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return min(nums)

        # Sort the list in ascending order
        nums.sort()

        # Calculate the sum
        sum = 0
        for k in range(int(len(nums)/2)):
            #print(k, nums[2*k:2*k+2])
            sum = sum + min(nums[2*k:2*k+2])

        return sum

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = []
    print(sln.arrayPairSum(nums))

    # nums = [1]
    # print(sln.arrayPairSum(nums))

    nums = [1, 3]
    print(sln.arrayPairSum(nums))

    # Testcase1
    print('Testcase1...')
    nums = [1, 2, 3, 4]
    print(sln.arrayPairSum(nums))

    # Testcase2
    print('Testcase2...')
    nums = [1, 6, 9, 10, 2, 5, 9, 0]
    print(sln.arrayPairSum(nums))
