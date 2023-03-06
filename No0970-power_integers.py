"""
970. 强整数
给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。

返回值小于或等于 bound 的所有强整数组成的列表。

你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。

示例 1：

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释： 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
示例 2：

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]
 

提示：

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
通过次数9,914提交次数24,149

执行用时：
40 ms
, 在所有 Python3 提交中击败了
79.44%
的用户
内存消耗：
15 MB
, 在所有 Python3 提交中击败了
5.24%
的用户
炫耀一下:

"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        #print('x = {0}, y = {1}, bound = {2}'.format(x,y,bound))

        xpowLst = []
        if x == 1:
            xpowLst.append(1)
        else:
            xpow = 1
            while xpow < bound:
                xpowLst.append(xpow)
                xpow = xpow * x

        ypowLst = []
        if y == 1:
            ypowLst.append(1)
        else:
            ypow = 1
            while ypow < bound:
                ypowLst.append(ypow)
                ypow = ypow * y

        #print('xpowLst = {0}, ypowLst = {1}'.format(xpowLst, ypowLst))

        sumLst = []
        for i in range(len(xpowLst)):
            for j in range(len(ypowLst)):
                if xpowLst[i] + ypowLst[j] <= bound:
                    sumLst.append(xpowLst[i] + ypowLst[j])
                else:
                    break
        
        # Remove repetition
        if len(sumLst) == 0:
            return []

        sumLst.sort()

        #print('sumLst = ', sumLst)
        sumLst2 = [sumLst[0]]
        for i in range(1,len(sumLst)):
            if sumLst[i] != sumLst2[-1]:
                sumLst2.append(sumLst[i])

        return sumLst2

if __name__ == '__main__':        
    #import time
    sln = Solution()
    
    x,y,bound = 2,3,10
    print(sln.powerfulIntegers(x,y,bound))
    
    x,y,bound = 3,5,15
    print(sln.powerfulIntegers(x,y,bound))

    x,y,bound = 3,5,1
    print(sln.powerfulIntegers(x,y,bound))

    x,y,bound = 3,5,2
    print(sln.powerfulIntegers(x,y,bound))

    x,y,bound = 1,2,1000000
    print(sln.powerfulIntegers(x,y,bound))

    x,y,bound = 1,1,1000000
    print(sln.powerfulIntegers(x,y,bound))