# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 17:37:48 2021

@author: chenxy

179. 最大数
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

 

示例 1：

输入：nums = [10,2]
输出："210"
示例 2：

输入：nums = [3,30,34,5,9]
输出："9534330"
示例 3：

输入：nums = [1]
输出："1"
示例 4：

输入：nums = [10]
输出："10"
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 109

"""
import math

class Solution:
    def merge2num(self, numstr1, numstr2):
        a = numstr1 + numstr2
        b = numstr2 + numstr1
        if int(a) >= int(b):
            return a
        else:
            return b                 
    
    # def largestNumber(self, nums: List[int]) -> str:
    def largestNumber(self, nums) -> str:
# =============================================================================
# 执行用时：40 ms, 在所有 Python3 提交中击败了89.04%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了91.16%的用户        
# 什么原理？
# =============================================================================
        def fun(x):
            if x==0:return 0
            L=int(math.log10(x))+1
            return x/(10**L-1)
        nums.sort(key=fun,reverse=True)
        nums=list(map(str,nums))
        return str(int("".join(nums)))
        
    def largestNumberRunError(self, nums) -> str:
        # 没看懂，cmp_to_key什么鬼？运行过不了
        def cmp(x,y):
            return 1 if x+y<y+x else -1
        nums=list(map(str,nums))
        nums.sort(key=cmp_to_key(cmp))
        res= str(int("".join(nums)))
        return res
        
    def largestNumberTwoSlow(self, nums) -> str:
        n=len(nums)
        nums=list(map(str,nums))
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        
        return str(int("".join(nums)))
        
    def largestNumber1(self, nums) -> str:
        # 有问题。。。需要进一步琢磨如何解决
        if len(nums) == 1:
            return str(nums[0])
        
        numstr = [str(num) for num in nums]
        numstr.sort(reverse = True)
        print(numstr)
        
        # a = numstr[0]
        # for k in range(1,len(numstr)):
        #     a = self.merge2num(a,numstr[k])

        ret = ''
        a   = numstr[0]
        curcapital = a[0]
        for k in range(1,len(numstr)):
            b = numstr[k]
            if b[0] == curcapital:
                a = self.merge2num(a,b)
            else:
                ret = ret + a
                a   = b
                curcapital = a[0]
        ret = ret + a
                        
        return ret
                
if __name__ == '__main__':        
    import time
    import random
    
    sln = Solution()        
    
    nums = [10,2]
    print(sln.largestNumber(nums))
    
    nums = [3,30,34,5,9]
    print(sln.largestNumber(nums))    
    
    nums = [1]
    print(sln.largestNumber(nums))        
    
    nums = [3,906,90,5,9]
    print(sln.largestNumber(nums))            

    nums = [3,20,206,5,9]
    print(sln.largestNumber(nums))        
    
    nums = [128,12,320,32]
    print(sln.largestNumber(nums))        
    