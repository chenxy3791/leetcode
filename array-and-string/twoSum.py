""" 
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""
import time

class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, numbers, target):
        nNums = len(numbers)

        # Ignore the validity check, because it is assured that there would be a unique solution.

        fPtr = 0
        bPtr = nNums - 1        

        while fPtr < bPtr:
            #print(fPtr, bPtr)
            sum = numbers[fPtr] + numbers[bPtr]
            if sum == target:
                #print('Successful: ', fPtr, bPtr)
                return fPtr+1, bPtr+1
            elif sum < target:
                fPtr = fPtr + 1
            else:
                bPtr = bPtr - 1            

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    nums = [2,7,11,15]
    target = 9
    idx1, idx2 = sln.twoSum(nums, target)
    print(idx1, idx2)

    # Testcase1
    print('Testcase1...')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 17
    [idx1, idx2] = sln.twoSum(nums, target)
    print(idx1, idx2)
    
    # Testcase2
    print('Testcase2...')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 3
    [idx1, idx2] = sln.twoSum(nums, target)
    print(idx1, idx2)
