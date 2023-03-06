# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 07:45:24 2021

@author: chenxy

4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

 

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000
 

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

"""
class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2) -> float:        
        print(nums1, nums2)        
        M = len(nums1) + len(nums2)        
        cnt = 0
        prevNum = 0
        curNum  = 0
        p1 = 0
        p2 = 0
        while cnt <= M//2 and (p1<len(nums1)) and (p2<len(nums2)):
            prevNum = curNum
            if nums1[p1] <= nums2[p2]:
                curNum = nums1[p1]
                p1 = p1 + 1
            else:
                curNum = nums2[p2]
                p2 = p2 + 1
            cnt = cnt + 1
        print(cnt, p1, p2, prevNum, curNum)
        
        if cnt <= M//2:
            if p1<len(nums1):                
                # print('nums2 is used-up first')
                left = nums1[p1:]
                # prevNum= nums1[p1 + M//2 - cnt - 1]
                # curNum = nums1[p1 + M//2 - cnt]
            else:
                # print('nums1 is used-up first')
                left = nums2[p2:]
                # prevNum= nums2[p2 + M//2 - cnt - 1]
                # curNum = nums2[p2 + M//2 - cnt]
            p = 0
            while cnt <= M//2:
                prevNum = curNum
                curNum = left[p]
                p   = p + 1
                cnt = cnt + 1                
            
        if M%2 == 0:
            return (prevNum + curNum)/2
        else:
            return curNum
        
if __name__ == '__main__':        
    #import time
    sln = Solution()

    nums1 = [1,3]
    nums2 = [2]
    print(nums1, nums2, ' --> ', sln.findMedianSortedArrays(nums1,nums2))        
    
    nums1 = [1,2]
    nums2 = [3,4]
    print(nums1, nums2, ' --> ', sln.findMedianSortedArrays(nums1,nums2))            
    
    nums1 = [0,0]
    nums2 = [0,0]
    print(nums1, nums2, ' --> ', sln.findMedianSortedArrays(nums1,nums2))                
    
    nums1 = []
    nums2 = [1]
    print(nums1, nums2, ' --> ', sln.findMedianSortedArrays(nums1,nums2))                    
    
    nums1 = [2]
    nums2 = []
    print(nums1, nums2, ' --> ', sln.findMedianSortedArrays(nums1,nums2))                        
