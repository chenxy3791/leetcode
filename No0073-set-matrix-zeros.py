"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？

示例 1：
输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

示例 2：
输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

提示：

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    #def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix)
        N = len(matrix[0])
        for m in range(M):
            for n in range(N):
                if matrix[m][n] == 0:
                    # set all elements of the same and the same colomn to '-1'
                    for j in range(N):
                        # matrix[m][j] = -1 * matrix[m][j]  # 1 -> -1; 0 kept unchanged. NG. Repeated change occurs
                        if matrix[m][j] != 0:
                            matrix[m][j] = None
                    for l in range(M):
                        # matrix[l][n] = -1 * matrix[l][n]  # 1 -> -1; 0 kept unchanged. NG. Repeated change occurs
                        if matrix[l][n] != 0:
                            matrix[l][n] = None
                            
        # Finally, change all '-1' to 0, and keep '1' unchanged
        for m in range(M):
            for n in range(N):
                if matrix[m][n] == None:
                    matrix[m][n] = 0
        
        return
        
if __name__ == '__main__':        
    #import time
    sln = Solution()
    
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print('before change: ', matrix)
    sln.setZeroes(matrix)
    print('after change: ', matrix)
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print('before change: ', matrix)    
    sln.setZeroes(matrix)
    print('after change: ', matrix)
 
    matrix = [[-1],[2],[3]]
    print('before change: ', matrix)    
    sln.setZeroes(matrix)
    print('after change: ', matrix)
    