# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:47:28 2021

@author: chenxy

90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]

提示：
1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""

class Solution:
    #def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def subsetsWithDup(self, nums):
        nums.sort()
        
        repeatNum = dict()
        sublist = []
        
        cnt = 0
        for k in range(1,len(nums)):
            if nums[k] != nums[k-1]:
                if cnt == 0:
                    sublist.append(nums[k-1])
                else:
                    repeatNum[nums[k-1]] = cnt + 1
                    cnt = 0
            else:
                cnt = cnt + 1
        # The final element
        if cnt == 0:
            sublist.append(nums[-1])
        else:
            repeatNum[nums[-1]] = cnt + 1
        
        print(sublist)
        for key,value in repeatNum.items():
            print('{key}:{value}'.format(key = key, value = value))
        
        rslt = []
        # power set of sublist
        for k in range(2**len(sublist)):
            k_bin = bin(k)[2:]
            k_bin = (len(sublist) - len(k_bin))*'0' + k_bin
            subset = []
            for j in range(len(sublist)):
                if k_bin[j] == '1':
                    subset.append(sublist[j])
            rslt.append(subset)
        
        # cartesian product between the power set of sublist and the remaining subsets from repeated elements
        # Should pay attention to avoid repetition due to []
        for k in repeatNum:
            # Every loop, rslt will grow larger due to cartesian product
            N = len(rslt)
            M = repeatNum[k]
            for n in range(N):
                ss = rslt[n]
                for m in range(1,M+1): # [] should be excluded to avoid trival repetition
                    rslt.append(ss + m*[k])
        
        return rslt
    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()
    
    nums = [1,2,2]
    print(sln.subsetsWithDup(nums))  
    
    nums = [0]
    print(sln.subsetsWithDup(nums))  
    
    nums = [1,2,3,4]
    print(sln.subsetsWithDup(nums))  
            
            
            
            
                
                
            