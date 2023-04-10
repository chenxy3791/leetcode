# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 07:24:59 2022

@author: Dell
"""
import random
class Solution:
    def trailingZeroes1(self, n: int) -> int:
        if n==0:
            return 0
        prod = 1
        for k in range(2,n+1):
            prod = prod * k
        # print(prod)
        
        trailZeroCnt = 0
        while prod > 0:
            if prod % 10 == 0:
                trailZeroCnt += 1
                prod = prod // 10
            else:
                break
        return trailZeroCnt

    def trailingZeroes2(self, n: int) -> int:
        if n==0:
            return 0    
        prod = 1
        trailZeroCnt = 0
        for k in range(2,n+1):
            if (k%10) in [1,3,4,6,7,8,9]:
                continue
            prod = prod * k
            while True:
                if prod % 10 == 0:
                    trailZeroCnt += 1
                    prod = prod // 10
                else:
                    break
        # print(prod)
        return trailZeroCnt        
        
    def trailingZeroes3(self, n: int) -> int:
        if n==0:
            return 0
        
        trailZeroCnt = 0
        for k in range(2,n+1):
            cur = k
            while True:
                if cur % 5 == 0:
                    trailZeroCnt += 1
                    cur = cur // 5
                else:
                    break
        return trailZeroCnt

    def trailingZeroes4(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans

# =============================================================================
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/jie-cheng-hou-de-ling-by-leetcode-soluti-1egk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# =============================================================================
if __name__ == '__main__':
    
    sln = Solution()
    
    err_cnt = 0
    
    for k in range(100):
        n = random.randint(0,10000)
        print('n = {0}: '.format(n))
        ans1 = sln.trailingZeroes1(n)
        ans2 = sln.trailingZeroes2(n)
        ans3 = sln.trailingZeroes3(n)
        ans4 = sln.trailingZeroes4(n)
        if ans1 != ans2 or ans1 != ans3 or ans1 != ans4:
            err_cnt += 1
            print('Failure: n = {0}, ans1 ={1}, ans2={2}, ans3={3}, ans3={4}'.format(n,ans1,ans2,ans3,ans4))
    print('num_test，err_cnt = ',k+1,err_cnt)
        # print(sln.trailingZeroes1(n)) 
    # print(sln.trailingZeroes2(22))
        