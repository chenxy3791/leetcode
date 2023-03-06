# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 07:27:54 2022

@author: chenxy

1994. 好子集的数目
给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。

比方说，如果 nums = [1, 2, 3, 4] ：
[2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
[1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。
请你返回 nums 中不同的 好 子集的数目对 109 + 7 取余 的结果。

nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。

示例 1：
输入：nums = [1,2,3,4]
输出：6
解释：好子集为：
- [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。

示例 2：
输入：nums = [4,2,3,15]
输出：5
解释：好子集为：
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
- [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。
 
提示：
1 <= nums.length <= 105
1 <= nums[i] <= 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-number-of-good-subsets
"""
from typing import List
from math import sqrt
# from collections import deque
import itertools as it
import time
class Solution:

    def isPrime(self, x):
        for i in range(2,int(sqrt(x))+1):
            if x%i==0:
                return False
        return True

    def primeFactorization(self, n):
        ans = []
        
        i = 2        
        while n>=2:
            if self.isPrime(i):
                while n%i == 0:
                    n = n // i
                    ans.append(i)
            i = i + 1
        return ans
    
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 1. Repetition removal
        num_set = set(nums)
        # 2. Prime factorization for each element and record the existence of 1
        #    Remove the number with repetitive primes in the factorization
        #    Store the result in a dictionary
        primeFactor = dict()
        one_flag = False
        num_set_reduced = num_set.copy()
        ans = []
        for n in num_set:
            if n != 1:
                tmp = self.primeFactorization(n)
                if len(set(tmp)) == len(tmp):
                    primeFactor[n] = tmp
                else:
                    num_set_reduced.discard(n)
            else:
                num_set_reduced.discard(1)
                one_flag = True
        
        # 3. Traverse the power set                
        for k in range(1, len(num_set_reduced)+1):
            for subset in it.combinations(num_set_reduced,k):                
                primeSet = []
                for e in subset:
                    primeSet = primeSet + primeFactor[e]
                print(subset, primeSet)
                if len(set(primeSet)) == len(primeSet):
                    ans.append(list(subset))                
        # 4. If there is 1 in the original set
        if one_flag: # No need of give the list of the good subset, only the numbers!
            # ans1 = []
            # for each in ans:
            #     print(each)
            #     ans1.append(each + [1])
            # ans = ans + ans1             
            return 2 * len(ans)
        else:
            return len(ans)
        
if __name__ == '__main__':        
    
    sln = Solution()
    # print(sln.isPrime(17))
    # print(sln.primeFactorization(105))
    
    nums = [1,2,3,4]
    print('nums={0}:  {1}'.format(nums,sln.numberOfGoodSubsets(nums)))
    print()
    
    nums = [4,2,3,15]
    print('nums={0}:  {1}'.format(nums,sln.numberOfGoodSubsets(nums)))
    print()
    
    nums = [6,8,1,8,6,5,6,11,17]
    print('nums={0}:  {1}'.format(nums,sln.numberOfGoodSubsets(nums)))
    print()    