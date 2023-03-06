""" 
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6].
"""

import time

class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1 = 0
        ptr2 = 0
        while ptr2 < n and ptr1 <(m + ptr2):
            print('ptr1 = {0}, ptr2 = {1}'.format(ptr1,ptr2))
            if nums1[ptr1] > nums2[ptr2]:
                nums1.pop()
                nums1.insert(ptr1,nums2[ptr2])
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1

        for k in range(ptr2,n):
            nums1.pop()
            nums1.insert(ptr1,nums2[k])
            ptr1 += 1
                
if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    print('Testcase1...')
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3        
    sln.merge(nums1,m,nums2,n)
    print(nums1)

    # Testcase2 
    print('Testcase2...')
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [4,5,6]
    n = 3        
    sln.merge(nums1,m,nums2,n)
    print(nums1)

    # Testcase3 
    print('Testcase3...')
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3        
    sln.merge(nums1,m,nums2,n)
    print(nums1)
