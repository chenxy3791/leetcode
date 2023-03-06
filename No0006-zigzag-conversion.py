""" 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Assuming numRow = 4:
     0  1  2  3 
    -1 -1  4 -1
    -1  5 -1 -1
     6  7  8  9
    -1 -1 10 -1
    -1 11 -1 -1
    ...

2020-1-10 Need further optimization.
执行结果：通过
显示详情
执行用时 : 388 ms, 在所有 Python3 提交中击败了7.56%的用户
内存消耗 :14.9 MB, 在所有 Python3 提交中击败了7.43%的用户    
 """
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sLen = len(s)

        assert(numRows>0)
        if (sLen <= numRows) or (numRows == 1):
            return s

        # flagging
        flagLOL = []
        listCnt = 0
        rPtr    = 0
        lTmp    = [-1]*numRows
        wCnt    = 0 # The write count for the full-write-row
        while rPtr < sLen:            
            if (listCnt % (numRows-1)) == 0:
                lTmp[wCnt] = rPtr
                rPtr    = rPtr + 1
                wCnt    = wCnt + 1
                if (wCnt == numRows) or (rPtr == sLen):
                    flagLOL.append(lTmp)
                    listCnt = listCnt + 1
                    lTmp    = [-1]*numRows                
                    wCnt    = 0
            else:
                lTmp[numRows-(listCnt%(numRows-1))-1] = rPtr
                rPtr    = rPtr + 1
                flagLOL.append(lTmp)
                listCnt = listCnt + 1
                lTmp = [-1]*numRows
        #print('rPtr=', rPtr, ' sLen=', sLen)

        # Read out
        #print(flagLOL)
        sOut = []
        for m in range(numRows):
            for n in range(len(flagLOL)):
                if flagLOL[n][m] != -1:
                    # print('n=', n, ' ', 'm=', m)
                    # print('flagLOL[n][m] =', flagLOL[n][m])
                    sOut.append(s[flagLOL[n][m]])

        return ''.join(sOut)

    def convert1(self, s: str, numRows: int) -> str:
# =============================================================================
#         2021-03-30
#         执行用时：76 ms, 在所有 Python3 提交中击败了33.51%的用户
#         内存消耗：15.1 MB, 在所有 Python3 提交中击败了31.97%的用户
# =============================================================================
        rslt = ''
        if numRows <= 1 or numRows >= len(s):
            return s
        
        for r in range(numRows):        
            k = r        
            if r == 0:                  # The first line
                step = 2 * numRows - 2
                while k < len(s): 
                    rslt = rslt + s[k]
                    k = k + step
            elif r <= numRows-2:        # The middle lines
                step2 = 2 * r
                step1 = 2 * numRows - 2 - step2
    
                cnt = 0
                while k < len(s):
                    rslt = rslt + s[k]
                    if (cnt%2) == 0:
                        step = step1
                    else:
                        step = step2
                    k = k + step                
                    cnt = cnt + 1
            else:                       # The last line
                step = 2 * numRows - 2
                while k < len(s):
                    rslt = rslt + s[k]
                    k = k + step
        #print(s, ' --> ', rslt)
        #print(len(s), len(rslt))    
        assert(len(s) == len(rslt))
        return rslt

    def convert2(self, s: str, numRows: int) -> str:
# =============================================================================
# 改为先将字符串读入列表，最后再变换，稍微快了一丢丢
# =============================================================================
        if numRows <= 1 or numRows >= len(s):
            return s

        rslt = []
        for r in range(numRows):        
            k = r        
            if r == 0:                  # The first line
                step = 2 * numRows - 2
                while k < len(s): 
                    rslt.append(s[k])
                    k = k + step
            elif r <= numRows-2:        # The middle lines
                step2 = 2 * r
                step1 = 2 * numRows - 2 - step2
    
                cnt = 0
                while k < len(s):
                    rslt.append(s[k])
                    if (cnt%2) == 0:
                        step = step1
                    else:
                        step = step2
                    k = k + step                
                    cnt = cnt + 1
            else:                       # The last line
                step = 2 * numRows - 2
                while k < len(s):
                    rslt.append(s[k])
                    k = k + step
        #print(s, ' --> ', rslt)
        #print(len(s), len(rslt))    
        assert(len(s) == len(rslt))
        return ''.join(rslt)

    def convert3(self, s: str, numRows: int) -> str:
# =============================================================================
# 参考官解进行优化
# =============================================================================
        if numRows <= 1 or numRows >= len(s):
            return s

        rslt = []
        for r in range(numRows):        
            k = r        
            if r == 0:                  # The first line
                step = 2 * numRows - 2
                while k < len(s): 
                    rslt.append(s[k])
                    k = k + step
            elif r <= numRows-2:        # The middle lines
                step2 = 2 * r
                step1 = 2 * numRows - 2 - step2
    
                cnt = 0
                while k < len(s):
                    rslt.append(s[k])
                    if (cnt%2) == 0:
                        step = step1
                    else:
                        step = step2
                    k = k + step                
                    cnt = cnt + 1
            else:                       # The last line
                step = 2 * numRows - 2
                while k < len(s):
                    rslt.append(s[k])
                    k = k + step
        #print(s, ' --> ', rslt)
        #print(len(s), len(rslt))    
        assert(len(s) == len(rslt))
        return ''.join(rslt)
# Official Solution
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         n, r = len(s), numRows
#         if r == 1 or r >= n:
#             return s
#         t = r * 2 - 2
#         ans = []
#         for i in range(r):  # 枚举矩阵的行
#             for j in range(0, n - i, t):  # 枚举每个周期的起始下标
#                 ans.append(s[j + i])  # 当前周期的第一个字符
#                 if 0 < i < r - 1 and j + t - i < n:
#                     ans.append(s[j + t - i])  # 当前周期的第二个字符
#         return ''.join(ans)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/zigzag-conversion/solution/z-zi-xing-bian-huan-by-leetcode-solution-4n3u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    
if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = "PAYPALISHIRING"
    numRows = 3
    print(s, ' --> ', sln.convert(s, numRows))

    # Testcase1
    print('Testcase1...')
    s = "PAYPALISHIRING"
    numRows = 4
    print(s, ' --> ', sln.convert(s, numRows))
    
    # Testcase2
    print('Testcase2...')
    s = "HELLO"
    numRows = 1
    print(s, ' --> ', sln.convert(s, numRows))

    # Testcase4
    print('Testcase3...')
    s = "HELLO"
    numRows = 5
    print(s, ' --> ', sln.convert(s, numRows))

    # Testcase4
    print('Testcase4...')
    s = "HELLO"
    numRows = 0
    print(s, ' --> ', sln.convert(s, numRows))
