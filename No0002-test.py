# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 17:19:27 2018

@author: chenxy
"""

import random
import unittest

from No2_add_two_numbers import ListNode
from No2_add_two_numbers import Solution

class TestAddTwoNumbers(unittest.TestCase):

    def setUp(self):
         pass

    def addTwoNumbersWrapper(self,in1,in2):
         sln = Solution()
              
         list1 = sln.int2list(in1)
         list2 = sln.int2list(in2)
         #sln.dispList(list1)
         #sln.dispList(list2)
                
         sum_list = sln.addTwoNumbers(list1,list2)
         sum_num  = sln.list2int(sum_list)
         #sln.dispList(sum_list)
                                     
         return(sum_num)

    def test_case1_int_list_conversion(self):
        sln = Solution()
        a = 10
        a_lst = sln.int2list(a)
        #sln.dispList(a_lst)
        b = sln.list2int(a_lst)
        
        self.assertEqual(a, b)
        
        return
                 
    def test_case2_10_22(self):   
        in1 = 10
        in2 = 22            
        sum12 = self.addTwoNumbersWrapper(in1,in2)                                     
        self.assertEqual(in1+in2, sum12)

    def test_case3_0_0(self):   
        in1 = 0
        in2 = 0            
        sum12 = self.addTwoNumbersWrapper(in1,in2)                                     
        self.assertEqual(in1+in2, sum12)

    def test_case4_0_123(self):   
        in1 = 0
        in2 = 123            
        sum12 = self.addTwoNumbersWrapper(in1,in2)                                     
        self.assertEqual(in1+in2, sum12)

    def test_case5_1357_0(self):   
        in1 = 1357
        in2 = 0           
        sum12 = self.addTwoNumbersWrapper(in1,in2)                                     
        self.assertEqual(in1+in2, sum12)

    def test_case6_967557_89747545(self):   
        in1 = 967557
        in2 = 89747545           
        sum12 = self.addTwoNumbersWrapper(in1,in2)                                     
        self.assertEqual(in1+in2, sum12)
              
if __name__ == '__main__':
   unittest.main()
   #testcase = TestAddTwoNumbers()
   #testcase.test_case4_0_123()
   
