"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

2021-03-15
执行用时：44 ms, 在所有 Python3 提交中击败了28.71%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了9.57%的用户

"""

class Solution:
    #def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        if matrix == [] or matrix == [[]]:
            return []
        m = len(matrix) # number of rows
        n = len(matrix[0]) # number of cols
        rslt = []
        if m == 1: # Single row matrix
            return matrix[0]
        if n == 1: # Single col matrix
            for k in range(m):
                rslt.append(matrix[k][0])
            return rslt 

        nxtMove = 'right'
        i,j = 0,0 # matrix index
        lBound = 0
        rBound = n - 1
        uBound = 0
        dBound = m - 1

        rslt.append(matrix[i][j])
        while (1):
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
            rslt.append(matrix[i][j])
            if rBound < lBound or uBound > dBound:
                break
        return rslt
                
if __name__ == '__main__':        
    #import time
    sln = Solution()

    matrix = [[]]
    print(sln.spiralOrder(matrix))

    matrix = [[4,5,6]]
    print(sln.spiralOrder(matrix))

    matrix = [[2],[4],[9]]
    print(sln.spiralOrder(matrix))

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sln.spiralOrder(matrix))
    
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(sln.spiralOrder(matrix))