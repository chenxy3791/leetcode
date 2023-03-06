# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 07:13:34 2021

@author: chenxy

31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100

"""
class Solution:
    
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def isMaxPermutation(l,u) -> bool:
            for k in range(l,u):
                if nums[k] < nums[k+1]:
                    return False
            return True

        def reverse(l,u):
            #print('reverse() start: ', nums)
            left = l
            right = u

            while(left < right):
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left  = left + 1
                right = right - 1
            #print('reverse() end: ', nums)
            return
    
        n = len(nums)
        if n == 1:
            return

        if isMaxPermutation(0,n-1):
            reverse(0,n-1)            
            return
        
        # Start from end, find the first one non-max-permutation sub-sequence.
        for k in range(n-1,-1,-1):
            #print('k= ', k, nums[k:])
            if not isMaxPermutation(k,n-1):
                #print(k, ': is not a max permutation')
                #Find the first one in nums[k+1,n-1] from right to left, which is greater than nums[k]
                for j in range(n-1,k,-1):
                    if nums[j] > nums[k]:
                        tmp     = nums[k]
                        nums[k] = nums[j]
                        nums[j] = tmp
                        break
                #Swap nums[j] and nums[k]
                reverse(k+1,n-1)            
                return            
        return

if __name__ == '__main__':        
    #import time
    sln = Solution()

    nums = [1,2,3]
    #print(nums, end='')
    sln.nextPermutation(nums)
    print(' --> ',nums)

    nums = [3,2,1]
    #print(nums, end='')
    sln.nextPermutation(nums)
    print(' --> ',nums)

    nums = [1]
    #print(nums, end='')
    sln.nextPermutation(nums)
    print(' --> ',nums)    

    nums = [1,3,7,6,2,9,4]
    #print(nums, end='')
    sln.nextPermutation(nums)
    print(' --> ',nums)    
    
    nums = [1,3,7,9,8,6,4,2]
    #print(nums, end='')
    sln.nextPermutation(nums)
    print(' --> ',nums)        