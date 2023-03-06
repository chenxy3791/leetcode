# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 08:43:18 2021

@author: chenxy

27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
 
说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
 
提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def removeElementSlow(self, nums: List[int], val: int) -> int:
        left  = 0
        right = len(nums) - 1
        cnt   = 0
        while left <=right:
            while right >= left and nums[right] == val:
                right = right - 1
                cnt   = cnt + 1
            # print(right, cnt)
            if right < left:
                return len(nums) - cnt
            
            while left <= right and nums[left] != val:
                left = left + 1
            if left > right:
                return len(nums) - cnt
            # print(left, cnt)
            
            nums[left] = nums[right]
            left  = left + 1            
            right = right - 1
            cnt   = cnt + 1
            # print('left={0}, right={1}, cnt={2}'.format(left,right,cnt))
        return len(nums) - cnt

    def removeElement1(self, nums: List[int], val: int) -> int:
# =============================================================================
# 执行用时：40 ms, 在所有 Python3 提交中击败了60.40%的用户
# 内存消耗：14.8 MB, 在所有 Python3 提交中击败了77.03%的用户        
# =============================================================================
# =============================================================================
#2022-03-05
# 执行用时：40 ms, 在所有 Python3 提交中击败了24.25%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了52.44%的用户
# =============================================================================
        if len(nums) == 0:
            return 0

        wptr  = 0
        for k in range(wptr, len(nums)):
            # print(k,nums[k])
            if nums[k] != val:
                nums[wptr] = nums[k]
                wptr += 1
            
        return wptr

    def removeElement(self, nums: List[int], val: int) -> int:
# =============================================================================
# 2022-03-05
# 执行用时：36 ms, 在所有 Python3 提交中击败了53.15%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了55.62%的用户
# =============================================================================
        
        if len(nums) == 0:
            return 0

        lptr,rptr  = 0,len(nums)-1
        ans = len(nums)
        while lptr <= rptr:
            # print(lptr, rptr, ans)
            if nums[lptr] == val:
                ans -= 1
                while rptr > lptr:
                    if nums[rptr] != val:
                        nums[lptr] = nums[rptr]
                        rptr -= 1
                        break
                    else:
                        ans -= 1
                        rptr -= 1
            lptr += 1
                        
        return ans
                                    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()

    # nums = [2,2,2,2,2,2,2,2]
    # val  = 2
    # print(nums,val, ' -> ', sln.removeElement(nums,val))
    # print(nums,val, ' -> ', sln.removeElementSlow(nums,val))

    # nums = [2,2,2,2,2,2,2,2]
    # val  = 3
    # print(nums,val, ' -> ', sln.removeElement(nums,val))
    # print(nums,val, ' -> ', sln.removeElementSlow(nums,val))
    
    nums = [0,1,2,2,3,0,4,2]
    nums1 = nums.copy()
    nums2 = nums.copy()
    val  = 2
    print(nums,val, ' -> ', sln.removeElement(nums1,val))
    print(nums,val, ' -> ', sln.removeElementSlow(nums2,val))
                    
    nums = [random.randint(0,10) for x in range(100)]        
    nums1 = nums.copy()
    nums2 = nums.copy()    
    val  = random.randint(0,10)
    print(nums,val, ' -> ', sln.removeElement(nums1,val))
    print(nums,val, ' -> ', sln.removeElementSlow(nums2,val))

    tStart = time.time()        
    nums = [random.randint(0,10) for x in range(100)]        
    nums1 = nums.copy()
    nums2 = nums.copy()    
    val  = 11
    print(nums,val, ' -> ', sln.removeElement(nums1,val))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    

    tStart = time.time()        
    print(nums,val, ' -> ', sln.removeElementSlow(nums2,val))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    