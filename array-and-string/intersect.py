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
        
        nums1.sort()
        nums2.sort()

        nums = []

        if len(nums1) <= len(nums2):
            #for k in range(len(nums1)):
            while len(nums1)>0:
                # Find nums1[k] in nums2
                numTmp = nums1.pop()
                i = bisect_left(nums2, numTmp) 
                if i != len(nums2) and nums2[i] == numTmp: # Successful
                    nums.append(numTmp)
                    nums2.remove(numTmp) #del(nums2[i])        
        else:
            #for k in range(len(nums2)):
            while len(nums2)>0:
                # Find nums2[k] in nums1
                numTmp = nums2.pop()
                i = bisect_left(nums1, numTmp) 
                if i != len(nums1) and nums1[i] == numTmp: # Successful
                    nums.append(numTmp)
                    nums1.remove(numTmp) #del(nums1[i])        
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

#    # Testcase2
#    print('Testcase2...')
#    nums = [4,1,2,1,2]
#    print(sln.singleNumber(nums))
#
#    # Testcase3
#    print('Testcase3...')
#    nums = []
#    N = 100000
#    for k in range(N):
#        nums.append(k)
#        nums.append(k)
#    nums.append(N)
# 
#    print(nums[0:10])
# 
#    tStart = time.time()    
#    print(sln.singleNumber(nums))
#    tElapsed = time.time() - tStart        
#    print('tElapsed = ', tElapsed, ' (sec)')
