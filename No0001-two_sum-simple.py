"""
1. 两数之和
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
 
提示：
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import time
class Solution_naive:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i+1,nums_len):
                if nums[i] + nums[j] == target:
                    return (i,j)                
        return -1

class Solution_dual_pointer:    
    def twoSum(self, nums, target):
        if len(nums) < 2:
            raise ValueError(nums)

        h = dict()
        for k in range(len(nums)):
            if nums[k] in h:
                h[nums[k]].append(k)
            else:
                h[nums[k]] = [k]

        nums.sort()
        
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l]+nums[r] == target:
                if nums[l] == nums[r]:
                    return tuple(h[nums[l]])                    
                else:
                    return (h[nums[l]][0],h[nums[r]][0])
                
            if nums[l]+nums[r] > target:
                r -= 1
            else:
                l += 1
        
        raise ValueError(nums)

class Solution_hash:    
    def twoSum(self, nums, target):
        if len(nums) < 2:
            ValueError(nums, target)
        
        h = dict()
        for k in range(len(nums)):
            if nums[k] in h:
                h[nums[k]].append(k)
            else:
                h[nums[k]] = [k]
        # print(h)
        for k in range(len(nums)):
            # print(nums[k])
            diff = target-nums[k]
            if diff == nums[k]:
                if len(h[nums[k]])==2:
                    return tuple(h[nums[k]])
            elif diff in h :
                return k, h[diff][0]
        
        raise ValueError(nums, target)

class Solution_hash2:    
    def twoSum(self, nums, target):
        if len(nums) < 2:
            ValueError(nums, target)
        
        h = dict()
        for k in range(len(nums)):
            if (target-nums[k]) in h:
                return k, h[target-nums[k]]
            else:
                h[nums[k]] = k
        
        raise ValueError(nums, target)
            
if __name__ == '__main__':        
        
    sln_naive = Solution_naive()
    sln_dual_pointer = Solution_dual_pointer()
    sln_hash = Solution_hash()
    sln_hash2 = Solution_hash2()
        
    nums = [3,2,4]
    target = 6
    print('sln_naive.twoSum(nums,target) = ', sln_naive.twoSum(nums,target))
    print('sln_hash.twoSum(nums,target) = ', sln_hash.twoSum(nums,target))    
    print('sln_hash2.twoSum(nums,target) = ', sln_hash2.twoSum(nums,target))    
    print('sln_dual_pointer.twoSum(nums,target) = ', sln_dual_pointer.twoSum(nums,target))    
    print()
    
    nums = [3,3]
    target = 6
    print('sln_naive.twoSum(nums,target) = ', sln_naive.twoSum(nums,target))
    print('sln_hash.twoSum(nums,target) = ', sln_hash.twoSum(nums,target))    
    print('sln_hash2.twoSum(nums,target) = ', sln_hash2.twoSum(nums,target))        
    print('sln_dual_pointer.twoSum(nums,target) = ', sln_dual_pointer.twoSum(nums,target))    
    print()
    
    # Note, this example has multiple solutions.
    nums = [2*i for i in range(10000)]
    index1 = 9999
    index2 = 8888
    target = nums[index1] + nums[index2]    
    print()
    
    tStart = time.time()        
    print('sln_naive.twoSum(nums,target) = ', sln_naive.twoSum(nums,target))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')   
    
    tStart = time.time()        
    print('sln_hash.twoSum(nums,target) = ', sln_hash.twoSum(nums,target))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')       

    tStart = time.time()        
    print('sln_hash2.twoSum(nums,target) = ', sln_hash2.twoSum(nums,target))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')       

    tStart = time.time()        
    print('sln_dual_pointer.twoSum(nums,target) = ', sln_dual_pointer.twoSum(nums,target))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')       