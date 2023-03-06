# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:19:27 2018

@author: chenxy
"""

import random
import unittest

from No1_two_sum import Solution

class TestTwoSum(unittest.TestCase):

   def setUp(self):
       pass

   def test_case1(self):
       nums = [1,2,3,4]
       target = 7
       sln = Solution()
       [idx1,idx2] = sln.twoSum(nums,target)
       self.assertEqual(set([idx1,idx2]), set([2,3]))
       
   def test_case2(self):
       nums = [2*i for i in range(10000)]
       ref_idx1 = 9999
       ref_idx2 = 8888
       target = nums[ref_idx1] + nums[ref_idx2]
    
       [idx1,idx2] = sln.twoSum(nums,target)
       self.assertEqual(set([idx1,idx2]), set([ref_idx1,ref_idx2]))       

   def test_case3(self):
       nums = [3,2,4]
       target = 6
       sln = Solution()
       [idx1,idx2] = sln.twoSum(nums,target)
       self.assertEqual(set([idx1,idx2]), set([1,2]))

   def test_case4(self):
       nums = [3,3]
       target = 6
       sln = Solution()
       [idx1,idx2] = sln.twoSum(nums,target)
       self.assertEqual(set([idx1,idx2]), set([0,1]))

   def test_case5(self):
       nums = [3,2,3]
       target = 6
       sln = Solution()
       [idx1,idx2] = sln.twoSum(nums,target)
       self.assertEqual(set([idx1,idx2]), set([0,2]))
       
if __name__ == '__main__':
   unittest.main()
