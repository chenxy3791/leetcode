# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 07:15:54 2021

@author: chenxy

39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

提示：

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
candidate 中的每个元素都是独一无二的。
1 <= target <= 500
"""
class Solution:
    #def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    # def combinationSum(self, candidates, target):
    #     print('combinationSum():', candidates, target)
    #     if len(candidates) == 0:
    #         return []
    #     if target < min(candidates):
    #         return []

    #     if len(candidates) == 1 and target%candidates[0] == 0:
    #         return (target // candidates[0]) * [candidates[0]]
        
    #     rslt = []
    #     while len(candidates) > 0:
    #         # print(candidates)
    #         c = candidates.pop()
    #         M = target // c
    #         print(c,M,candidates)
    #         for k in range(M+1):
    #             l1 = k * [c]
    #             print('k= ', k, 'l1= ', l1)                
    #             a  = self.combinationSum(candidates, target-k*c)

    #             for i in range(len(a)):
    #                 newItem = l1 + a[i]
    #                 if newItem:
    #                     rslt.append(newItem)
                    
    #     return rslt

    def combinationSum(self, candidates, target):        
        if len(candidates) == 0:
            return []
        if target < min(candidates):
            # print(target, candidates, min(candidates))
            # print('A')
            return []

        if len(candidates) == 1 and target%candidates[0] == 0:
            return [(target // candidates[0]) * [candidates[0]]]
        
        rslt = []
        # while len(candidates) > 0:
            # print(candidates)
        c = candidates[0]
        M = target // c
        # print(c,M,candidates)
        for k in range(M+1):
            l1 = k * [c]
            # print('k= ', k, 'l1= ', l1)                
            a  = self.combinationSum(candidates[1:], target-k*c)

            if len(a)==0 and sum(l1)==target:
                rslt.append(l1)
            for i in range(len(a)):
                newItem = l1 + a[i]
                if newItem:
                    rslt.append(newItem)

        # print('combinationSum():', candidates, target, ' -> ',rslt)                    
        return rslt
    
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()
    
    candidates = []
    target = 7
    print(sln.combinationSum(candidates, target))  

    candidates = [6]
    target = 7
    print(sln.combinationSum(candidates, target))  
    
    candidates = [7]
    target = 7
    print(sln.combinationSum(candidates, target))  
    
    candidates = [2,1]
    target = 5
    print(sln.combinationSum(candidates, target))  

    candidates = [3,6,7]
    target = 3
    print(sln.combinationSum(candidates, target))  

    candidates = [2,3,6,7]
    target = 7
    print(sln.combinationSum(candidates, target))  

    candidates = [2,3,5]
    target = 8
    print(sln.combinationSum(candidates, target))  