""" 
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
