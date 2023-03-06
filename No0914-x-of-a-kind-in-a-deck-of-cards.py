""" 
914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。
此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

示例 3：
输入：[1]
输出：false
解释：没有满足要求的分组。

示例 4：
输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

示例 5：
输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：
1 <= deck.length <= 10000
0 <= deck[i] < 10000

解题思路：
(1) 数组长度要能被X整除，所以X的候选为数组长度的因数（除1以外）
    进一步，因为相同的数才能分成一组，所以X应该是每种元素的个数的公因子
(2) 列表问题第一步总是考虑排序是不是有帮助

step1: Sorting
step2: Count each unique element
step3: Calculate the common divisor of the count of each unique element

How to calculate the common divisor of multiple numbers?
NOTE: No need of greatest common divisor. Any common divisor greater than 1 is enough.

"""
import math
import time
import numpy as np

class Solution:
    #def hasGroupsSizeX(self, deck: List[int]) -> bool:
    def prime_factors(self,n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors    

    def hasGroupsSizeX(self, deck) -> bool:
        if len(deck) <= 1:
            return False
        deck.sort()
        print('deck after sorting = {0}'.format(deck))
        count = []

        countCur = 0
        for k in range(len(deck)):
            if countCur == 0:
                countCur += 1
            elif deck[k] == deck[k-1]:
                countCur += 1
            else:
                count.append(countCur)
                countCur = 1 # instead of '0'!!!
        count.append(countCur) 
        
        if len(count) == 1:
            return True
        print('count = {0}'.format(count))

        # Does non-trival common divisor of all elements of count exist?
        mincount = min(count)
        minfactors = self.prime_factors(mincount)
        for f in minfactors:
            isCommonDivisor = True
            for c in count:
                if c % f :
                    isCommonDivisor = False
                    break
            if isCommonDivisor:
                return True
        return False
                           
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    deck = [1,2,3,4,4,3,2,1]
    tStart= time.time()
    print(sln.hasGroupsSizeX(deck))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    deck = [1,1,1,2,2,2,3,3]
    tStart= time.time()
    print(sln.hasGroupsSizeX(deck))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))      

    print('\ntestcase3 ...')
    deck = [1]
    tStart= time.time()
    print(sln.hasGroupsSizeX(deck))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))          

    print('\ntestcase4 ...')
    deck = [1,1]
    tStart= time.time()
    print(sln.hasGroupsSizeX(deck))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))          

    print('\ntestcase5 ...')
    deck = [1,1,2,2,2,2]
    tStart= time.time()
    print(sln.hasGroupsSizeX(deck))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))          
