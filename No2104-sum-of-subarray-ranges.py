# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:38:11 2022

@author: chenxy

2104. 子数组范围和
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。
返回 nums 中 所有 子数组范围的 和 。
子数组是数组中一个连续 非空 的元素序列。

示例 1：
输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
示例 2：

输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4
示例 3：

输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59
 
提示：
1 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-subarray-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

方法一：遍历子数组
为了方便计算子数组的最大值与最小值，我们首先枚举子数组的左边界 i，然后枚举子数组的右边界 j，
且 i≤j。在枚举 j 的过程中我们可以迭代地计算子数组 [i,j] 的最小值 minVal 与最大值 maxVal，
然后将范围值 maxVal−minVal 加到总范围和。

复杂度分析
时间复杂度：O(n^2)，其中 n 为数组的大小。两层循环需要 O(n^2)。
空间复杂度：O(1)。


方法二：单调栈
思路与算法

为了使子数组的最小值或最大值唯一，我们定义如果 \textit{nums}[i] = \textit{nums}[j]nums[i]=nums[j]，那么 \textit{nums}[i]nums[i] 与 \textit{nums}[j]nums[j] 的逻辑大小由下标 ii 与下标 jj 的逻辑大小决定，即如果 i < ji<j，那么 \textit{nums}[i]nums[i] 逻辑上小于 \textit{nums}[j]nums[j]。

根据范围和的定义，可以推出范围和 \textit{sum}sum 等于所有子数组的最大值之和 \textit{sumMax}sumMax 减去所有子数组的最小值之和 \textit{sumMin}sumMin。

假设 \textit{nums}[i]nums[i] 左侧最近的比它小的数为 \textit{nums}[j]nums[j]，右侧最近的比它小的数为 \textit{nums}[k]nums[k]，那么所有以 \textit{nums}[i]nums[i] 为最小值的子数组数目为 (k - i) \times (i - j)(k−i)×(i−j)。为了能获得 \textit{nums}[i]nums[i] 左侧和右侧最近的比它小的数的下标，我们可以使用单调递增栈分别预处理出数组 \textit{minLeft}minLeft 和 \textit{minRight}minRight，其中 \textit{minLeft}[i]minLeft[i] 表示 \textit{nums}[i]nums[i] 左侧最近的比它小的数的下标，\textit{minRight}[i]minRight[i] 表示 \textit{nums}[i]nums[i] 右侧最近的比它小的数的下标。

以求解 \textit{minLeft}minLeft 为例，我们从左到右遍历整个数组 \textit{nums}nums。处理到 \textit{nums}[i]nums[i] 时，我们执行出栈操作直到栈为空或者 \textit{nums}nums 中以栈顶元素为下标的数逻辑上小于 \textit{nums}[i]nums[i]。如果栈为空，那么 \textit{minLeft}[i] = -1minLeft[i]=−1，否则 \textit{minLeft}[i]minLeft[i] 等于栈顶元素，然后将下标 ii 入栈。

那么所有子数组的最小值之和 \textit{sumMin} = \sum_{i=0}^{n-1} (\textit{minRight}[i] - i) \times (i - \textit{minLeft}[i]) \times \textit{nums}[i]sumMin=∑ 
i=0
n−1
​
 (minRight[i]−i)×(i−minLeft[i])×nums[i]。同理我们也可以求得所有子数组的最大值之和 \textit{sumMax}sumMax。

复杂度分析

时间复杂度：O(n)O(n)，其中 nn 为数组的大小。使用单调栈预处理出四个数组需要 O(n)O(n)，计算最大值之和与最小值之和需要 O(n)O(n)。

空间复杂度：O(n)O(n)。保存四个数组需要 O(n)O(n)；单调栈最多保存 nn 个元素，需要 O(n)O(n)。

"""
import time
import random
from typing import List

class Solution:
    def subArrayRanges1(self, nums: List[int]) -> int:
        # 超出时间限制
        maxsum = 0
        for k in range(2,len(nums)+1):
            for m in range(len(nums)-k+1):
                # print(k,m)
                maxsum += max(nums[m:m+k]) - min(nums[m:m+k])
        return maxsum

    def subArrayRanges2(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            minVal, maxVal = float('inf'), -float('inf')
            for j in range(i, n):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                ans += maxVal - minVal
        return ans

    def subArrayRanges3(self, nums: List[int]) -> int:
        # A minor refinement upon subArrayRanges2
        ans, n = 0, len(nums)
        for i in range(n):
            minVal, maxVal = nums[i], nums[i]
            for j in range(i+1, n):
                minVal = min(minVal, nums[j])
                maxVal = max(maxVal, nums[j])
                ans += maxVal - minVal
        return ans                

if __name__ == '__main__':        
    
    sln = Solution()  

    # nums = [1,2,3]
    # tStart = time.time()        
    # ans = sln.subArrayRanges1(nums)
    # tElapsed = time.time() - tStart            
    # print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums,ans,tElapsed))        

    # nums = [1,3,3]
    # tStart = time.time()        
    # ans = sln.subArrayRanges1(nums)
    # tElapsed = time.time() - tStart            
    # print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums,ans,tElapsed))        
    
    # nums = [4,-2,-3,4,1]
    # tStart = time.time()        
    # ans = sln.subArrayRanges1(nums)
    # tElapsed = time.time() - tStart            
    # print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums,ans,tElapsed))            
    
    nums = [random.randint(-10**9, 10**9) for k in range(1000)]
    tStart = time.time()        
    ans = sln.subArrayRanges1(nums)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums[0],ans,tElapsed))                
    
    tStart = time.time()        
    ans = sln.subArrayRanges2(nums)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums[0],ans,tElapsed))        

    tStart = time.time()        
    ans = sln.subArrayRanges3(nums)
    tElapsed = time.time() - tStart            
    print('input={0}, ans={1}, tCost={2:3.2f}(sec)'.format(nums[0],ans,tElapsed))        