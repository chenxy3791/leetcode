""" 
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

import time
from bisect import bisect_left 
  
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1)==0 or len(nums2)==0:
            return []

        len1 = len(nums1)
        len2 = len(nums2)
        nums = []
        if len1 <= len2:
            for item1 in nums1:
                #print(item1)
                if item1 in nums2:
                    nums2.remove(item1)
                    nums.append(item1)
        else:
            for item2 in nums2:
                #print(item2)
                if item2 in nums1:
                    nums1.remove(item2)
                    nums.append(item2)                    
        return nums
    
if __name__ == '__main__':

    sln   = Solution()

    # Testcase1
    print('Testcase1...')
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(sln.intersect(nums1,nums2))

    # Testcase2
    print('Testcase2...')
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(sln.intersect(nums1,nums2))

    # Testcase3
    print('Testcase3...')
    nums1 = [3,1,2]
    nums2 = [1,1]
    print(sln.intersect(nums1,nums2))
