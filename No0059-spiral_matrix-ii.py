"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]

提示：

1 <= n <= 20

2021-03-16
执行结果：通过
显示详情
执行用时：44 ms, 在所有 Python3 提交中击败了34.77%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了33.20%的用户

"""

class Solution:
    def generateMatrix(self, n: int) :

        matrix = []
        for k in range(n):
            matrix.append(n*[0])
        
        nxtMove = 'right'
        i,j     = 0,0 # matrix index
        lBound, uBound, rBound, dBound = 0,0,n-1,n-1        
        curElement = 1
        n2      = n*n
        while (curElement <= n2):
            matrix[i][j] = curElement
            curElement   = curElement + 1

            curMove = nxtMove
            if curMove == 'right':
                j = j + 1
                if j < rBound:
                    nxtMove = 'right'
                else:
                    nxtMove = 'down'
                    uBound  = uBound + 1
            elif curMove == 'down':
                i = i + 1
                if i < dBound:
                    nxtMove = 'down'
                else:
                    nxtMove = 'left'
                    rBound  = rBound - 1        
            elif curMove == 'left':
                j = j - 1
                if j > lBound:
                    nxtMove = 'left'
                else:
                    nxtMove = 'up'
                    dBound  = dBound - 1        
            else:
                i = i - 1
                if i > uBound:
                    nxtMove = 'up'
                else:
                    nxtMove = 'right'
                    lBound  = lBound + 1        
            
        return matrix
                
if __name__ == '__main__':        
    #import time
    sln = Solution()

    print(sln.generateMatrix(1))
    
    print(sln.generateMatrix(2))

    print(sln.generateMatrix(3))

    print(sln.generateMatrix(4))