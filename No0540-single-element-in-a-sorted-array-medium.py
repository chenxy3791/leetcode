# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 11:19:42 2022

@author: chenxy

540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。

示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums = [3,3,7,7,10,11,11]
输出: 10

提示:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5
 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-element-in-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N     = len(nums)        
        if N==1:
            return nums[0]
        if N%2 == 0:
            return None
        left  = 0
        right = N - 1
        
        # Boundary check
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]        
        cnt = 0                
        while left <= right:
            if left == right:
                return nums[left]

            mid   = (left+right) // 2
            # print(left,right,mid)
            if mid%2 == 1:
                mid = mid - 1            

            if (nums[mid] != nums[mid-1]) and (nums[mid] != nums[mid+1]):
                return nums[mid]
            
            if nums[mid] == nums[mid-1]:
                right = mid
            else:
                left  = mid

if __name__ == '__main__':        
    
    sln = Solution()

    nums = [1,1,2,3,3,4,4,8,8]
    print(sln.singleNonDuplicate(nums))            
    
    nums = [3,3,7,7,10,11,11]
    print(sln.singleNonDuplicate(nums))            
    
    nums = [3,3,7,7,9,9,10]
    print(sln.singleNonDuplicate(nums))            
    
    nums = [2,3,3,4,4,8,8]
    print(sln.singleNonDuplicate(nums))            
        
    nums = [2]
    print(sln.singleNonDuplicate(nums))            
    
    nums = [2,2,3,3]
    print(sln.singleNonDuplicate(nums))            
                
                