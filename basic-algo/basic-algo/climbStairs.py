""" 
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step. 
"""

import time
import math

class Solution:
    def climbStairsRecursion(self, n: int) -> int:
        # Compact, but very time-consuming.
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairsRecursion(n-1) + self.climbStairsRecursion(n-2)

    def climbStairsRecursionWithMemoization(self, n: int, nums: dict):
        if n == 0 or n == 1:
            nums[n] = 1
            return 1,nums
        if n == 2:
            nums[n] = 2
            return 2,nums

        nMinus1 = nums.get(n-1) # dictionary.get("Age") is same as writing dictionary["Age"] or None so it implicitly handles KeyError exception 
        if nMinus1 == None:
            nMinus1,nums = self.climbStairsRecursionWithMemoization(n-1,nums)

        nMinus2 = nums.get(n-2) # dictionary.get("Age") is same as writing dictionary["Age"] or None so it implicitly handles KeyError exception 
        if nMinus2 == None:
            nMinus2,nums = self.climbStairsRecursionWithMemoization(n-2,nums)

        tmp = nMinus1 + nMinus2
        nums[n] = tmp
        return tmp, nums

    def climbStairsRecursionWithMemoization1(self, n: int, nums: dict):
        # Check the dict in different postion, making the code more compact
        if n == 0 or n == 1:
            nums[n] = 1
            return 1,nums
        if n == 2:
            nums[n] = 2
            return 2,nums

        tmp = nums.get(n)
        if tmp == None:
            nMinus1,nums = self.climbStairsRecursionWithMemoization(n-1,nums) 
            nMinus2,nums = self.climbStairsRecursionWithMemoization(n-2,nums)
            tmp = nMinus1 + nMinus2
            nums[n] = tmp

        return tmp, nums

    def climbStairsIterWithMemoization(self, n: int):
        if n == 0 or n == 1:
            return 1

        nCnt = []
        nCnt.append(1)
        nCnt.append(1)
        for k in range(2,n+1):
            nCnt.append(nCnt[k-1]+nCnt[k-2])
        
        return nCnt[n]
    """ 
    https://blog.csdn.net/u010712012/article/details/85836732
    2.用递推也就是动态规划的思想，就是找到f[n] = f[n-1] + f[n-2]这种状态的方程，其实和Fibonacci数列很相似，
    我们设定f(0)=f(1) = 1,最终的时间复杂度就是O(N),而且只需要存储前后的数字，所以内存消耗只需要常数级别的O(1).
    [chenxy] 这个也算动态规划的思想？
    """
    def climbStairs(self, n: int):
        # In fact, there is no need of store all the history. Only storing the last two is enough
        if n == 0 or n == 1:
            return 1

        x,y = 1,1
        for _ in range(2,n+1):
            x,y = y, x+y
        
        return y

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1 
    tStart = time.time()        
    print('Testcase1...')
    n = 30    
    print(sln.climbStairsRecursion(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    print('Testcase1...')
    n = 100    
    print(sln.climbStairsIterWithMemoization(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()    
    n = 100
    nums = {}
    nClimbStarts, nums = sln.climbStairsRecursionWithMemoization(n, nums)
    print(nClimbStarts)
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()    
    n = 100
    nums = {}
    nClimbStarts, nums = sln.climbStairsRecursionWithMemoization1(n, nums)
    print(nClimbStarts)
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    n = 100    
    print(sln.climbStairs(n))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed)