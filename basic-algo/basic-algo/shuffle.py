""" 
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle(); 
"""

import time
import math
import random

class Solution:
    #def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.origArray = nums.copy()
        self.curArray = self.origArray.copy()
        
    #def reset(self) -> List[int]:
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.curArray = self.origArray.copy()
        return self.curArray

    #def shuffle(self) -> List[int]:
    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.curArray)
        return self.curArray
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':

    nums = [1,2,3,4,5,6,7,8]
    sln   = Solution(nums)

    # Testcase1 
    tStart = time.time()        
    print('Testcase1...')
    
    print(sln.shuffle())
    print(sln.reset())
    print(sln.shuffle())
    print(sln.shuffle())
    print(sln.shuffle())
    print(sln.shuffle())
    print(sln.reset())
    print(sln.shuffle())
    print(sln.shuffle())
    print(sln.shuffle())
    print(sln.shuffle())

    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')
