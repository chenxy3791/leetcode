# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:39:01 2021

@author: chenxy

88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 

提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[i] <= 10^9

"""

class Solution:
    #def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n) -> None:        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for k in range(n):
                nums1[k] = nums2[k]
            return
        
        ptr0 = m + n - 1
        ptr1 = m - 1
        ptr2 = n - 1        
        
        while ptr1 >= 0 and ptr2 >= 0:
            print(ptr0, ptr1, ptr2)            
            n2 = nums2[ptr2]
            n1 = nums1[ptr1]
            if n2 >= n1:
                nums1[ptr0] = n2
                ptr2 = ptr2 - 1
            else:
                nums1[ptr0] = n1
                ptr1 = ptr1 - 1                
            ptr0 = ptr0 - 1
            print(nums1)            
            
        if ptr2 >= 0:
            for k in range(ptr2+1):
                nums1[k] = nums2[k]
            return            
        return
    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(nums1,m,nums2,n)    
    sln.merge(nums1,m,nums2,n)
    print('\t-> ', nums1)    

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    print(nums1,m,nums2,n)    
    sln.merge(nums1,m,nums2,n)
    print('\t-> ', nums1)    

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(nums1,m,nums2,n)    
    sln.merge(nums1,m,nums2,n)
    print('\t-> ', nums1)       
    
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1
    print(nums1,m,nums2,n)    
    sln.merge(nums1,m,nums2,n)
    print('\t-> ', nums1)  