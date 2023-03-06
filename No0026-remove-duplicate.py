# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 08:19:45 2021

@author: chenxy
26. 删除有序数组中的重复项
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 
示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 

提示：

0 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums 已按升序排列
 
"""
from typing import List
import time
import random
import sys

class Solution:
    def removeDuplicates0(self, nums: List[int]) -> int:
# =============================================================================
# 执行用时：76 ms, 在所有 Python3 提交中击败了13.33%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了29.97%的用户        
# =============================================================================
        N = len(nums)
        if N==0:
            return 0
        
        cur = nums[0]
        p   = 1
        rmcnt = 0
        for cnt in range(1,N):
            if nums[p] == cur:
                del nums[p]
                rmcnt += 1
            else:
                cur = nums[p]
                p += 1
                
        return N - rmcnt

    def removeDuplicates(self, nums: List[int]) -> int:
# =============================================================================
# 执行用时：44 ms, 在所有 Python3 提交中击败了79.81%的用户
# 内存消耗：15.8 MB, 在所有 Python3 提交中击败了24.69%的用户
# =============================================================================
        N = len(nums)
        if N==0:
            return 0
        
        sptr = 0        
        rmcnt = 0
        for fptr in range(1,N):
            if nums[fptr] == nums[sptr]:
                fptr  += 1
                rmcnt += 1
            else:
                sptr  += 1
                nums[sptr] = nums[fptr]                
                
        return N - rmcnt
                
if __name__ == '__main__':    
        
    sln = Solution()        

    nums = []    
    print(sln.removeDuplicates(nums), nums)        

    nums = [1]    
    print(sln.removeDuplicates(nums), nums)        
    
    nums = [1,1,2]    
    print(sln.removeDuplicates(nums), nums)        
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sln.removeDuplicates(nums), nums)            