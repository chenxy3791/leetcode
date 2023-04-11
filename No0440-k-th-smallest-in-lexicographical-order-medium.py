# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 08:03:33 2022

@author: Dell

给定整数 n 和 k，返回 [1, n] 中字典序第 k 小的数字。

示例 1:

输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
示例 2:

输入: n = 1, k = 1
输出: 1

提示:

1 <= k <= n <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
import time
import random

class Solution:
    def findKthNumber1(self, n: int, k: int) -> int:
        numstr = [str(k+1) for k in range(n)]
        numstr.sort()
        # print(numstr)
        nums = [int(numstr[k]) for k in range(n)]
        return nums[k-1]
    
    def findKthNumber2(self, n: int, k: int) -> int:        
        
        nums = [j+1 for j in range(n)]
        round = 0
        while len(nums)>1:            
            # print(round,nums)
            # if max(nums) < 10:
            #     return nums[k-1]
            
            # Create the hash table
            d = dict()
            for j in range(10):
                d[j] = []
            for m in range(len(nums)):
                mStr = str(nums[m])
                if len(mStr) > round:
                    d[int(mStr[round])].append(nums[m])
                else:
                    # d[0].append(m)
                    k -= 1
                    if k<=0:
                        return nums[m]
            # print(round,k,nums,d)
            # Serach for the period in which the target can be found
            cnt = 0
            for j in range(10):
                cnt_prev = cnt
                cnt += len(d[j])
                if cnt >= k:
                    nums = d[j]
                    k   -= cnt_prev
                    break
            round += 1
            # if round > 10: # temporarily for debug
            #     break
        return nums[0]

    def findKthNumber3(self, n: int, k: int) -> int:

        def subTreeSize(i):
            # print('subTreeSize(): ',i)
            if i>n:
                return 0
            cnt  = 1
            for node in range(10*i,10*i+10):
                cnt   = cnt + subTreeSize(node)
            return cnt
        
        def dp(i, k):
            # print('dp:',i,k)
            # baseline case
            if k==1:
                return i
            k = k-1
            for m in range(10):
                x = 10*i + m
                if x==0:
                    continue
                size_x = subTreeSize(x)
                # print('subTreeSize: ',x,size_x)
                if size_x >= k:
                    return dp(x,k)
                else:
                    k = k - size_x

        return dp(0,k+1)

    def findKthNumber4(self, n: int, k: int) -> int:

        def getSteps(cur: int, n: int) -> int:
            steps, first, last = 0, cur, cur
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps
        
        cur = 1
        k -= 1
        while k:
            steps = getSteps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

# =============================================================================
# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/zi-dian-xu-de-di-kxiao-shu-zi-by-leetcod-bfy0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# =============================================================================
    
if __name__ == '__main__':
    
    sln = Solution()

    print('case1...')
    print(sln.findKthNumber1(9, 5))
    print(sln.findKthNumber3(9, 5))

    print('case2...')
    print(sln.findKthNumber1(13, 2))
    print(sln.findKthNumber3(13, 2))

    print('case3...')
    n,k = 102, 17
    print(sln.findKthNumber1(n, k))
    print(sln.findKthNumber3(n, k))

    print('case4...')
    n,k = 1052, 16
    print(sln.findKthNumber1(n, k))
    print(sln.findKthNumber3(n, k))
    
    print('case5...')
    # n,k = 1027532, 6
    n,k = 1427590, 116
    tstart = time.time()    
    ans = sln.findKthNumber1(n, k)
    tcost  = time.time() - tstart
    print('n={0}, k={1}, ans={2}, tcost={3:5.2f}'.format(n,k,ans,tcost))
    
    tstart = time.time()    
    ans = sln.findKthNumber3(n, k)
    tcost  = time.time() - tstart
    print('n={0}, k={1}, ans={2}, tcost={3:5.2f}'.format(n,k,ans,tcost))    

    tstart = time.time()    
    ans = sln.findKthNumber4(n, k)
    tcost  = time.time() - tstart
    print('n={0}, k={1}, ans={2}, tcost={3:5.2f}'.format(n,k,ans,tcost))  
    
    # print('case6...')
    # # n,k = 1027532, 6
    # n,k = 142759000, 5665
    # tstart = time.time()    
    # ans = sln.findKthNumber1(n, k)
    # tcost  = time.time() - tstart
    # print('n={0}, k={1}, ans={2}, tcost={3:5.2f}'.format(n,k,ans,tcost))
    
    # tstart = time.time()    
    # ans = sln.findKthNumber2(n, k)
    # tcost  = time.time() - tstart
    # print('n={0}, k={1}, ans={2}, tcost={3:5.2f}'.format(n,k,ans,tcost))  
    
    # random test
    print('case6: random test...')
    for j in range(100):
        n = random.randint(1,10**5)
        k = random.randint(1,n)
        ans1 = sln.findKthNumber1(n, k)
        ans2 = sln.findKthNumber3(n, k)
        ans3 = sln.findKthNumber4(n, k)
        if ans1!=ans3 or ans1!=ans2:
            print('n={0},k={1}, ans1={2}, ans2={3}'.format(n,k,ans1,ans2))