""" 
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 """
class Solution:
    """ 
    执行结果：通过 显示详情
    执行用时 :40 ms, 在所有 Python3 提交中击败了98.01%的用户
    内存消耗 :13.9 MB, 在所有 Python3 提交中击败了20.99%的用户     
    """
    #def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return        
        n = len(matrix[0])
        if n == 0:
            return        
        
        rc_flg = []        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    rc_flg.append((r,c))
        
        r_rem = []
        c_rem = []
        for rc in rc_flg:
            r = rc[0]
            c = rc[1]
            if r not in r_rem:
                # set row#r to 0            
                matrix[r] = [0 for i in range(n)]                        
                r_rem.append(r)

            if c not in c_rem:
                # set col#c to 0
                for x in range(m):
                    matrix[x][c] = 0
        return                

class Solution1:
    """ 
    执行结果：通过 显示详情
    执行用时 :52 ms, 在所有 Python3 提交中击败了92.01%的用户
    内存消耗 :13.8 MB, 在所有 Python3 提交中击败了20.99%的用户     
    """
    #def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return        
        n = len(matrix[0])
        if n == 0:
            return        
        
        r_flg = []
        c_flg = []        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    c_flg.append(c)
                    r_flg.append(r)
        
        for r in r_flg:
            # set row#r to 0            
            matrix[r] = [0 for i in range(n)]                    
        for c in c_flg:
            # set col#c to 0
            for x in range(m):
                matrix[x][c] = 0
        return                

class SolutionNG:
    # Fail to handle confusion between the original 0 and the updated 0 properly.

    #def setZeroes(self, matrix: List[List[int]]) -> None:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        if m == 0:
            return        
        n = len(matrix[0])
        if n == 0:
            return        
        
        col = [x for x in range(n)]
        for r in range(m):
            c_rem = []
            for c in col:                
                if matrix[r][c] == 0:
                    c_rem.append(c)
                    
            # print('c_rem = {0}'.format(c_rem))

            if len(c_rem) > 0:
                # set row#r to 0
                matrix[r] = [0 for i in range(n)]                    
            while len(c_rem) > 0:
                k = c_rem.pop()
                # print(k,col)
                col.remove(k)
                # set col#c to 0
                for x in range(m):
                    matrix[x][k] = 0
        return                

if __name__ == '__main__':    

    import time
    import numpy as np

    sln   = Solution()

    print('Testcase1...')    
    matrix = [ [1,1,1], [1,0,1], [1,1,1] ]
    sln.setZeroes(matrix)
    print(matrix)

    print('Testcase2...')    
    tStart = time.time()        
    matrix = [ [0,1,2,0], [3,4,5,2], [1,3,1,5]]
    sln.setZeroes(matrix)
    print(matrix)
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))

    print('Testcase3...')    
    tStart = time.time()        
    nRow = 100
    nCol = 100
    a    = np.random.randint(0,100,[nRow, nCol])    
    matrix = a.tolist()       
    # print('The original matrix is {0}'.format(matrix))
    sln.setZeroes(matrix)
    # print('The updated matrix is {0}'.format(matrix))
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))

    print('Testcase4...')    
    tStart = time.time()        
    nRow = 200
    nCol = 200
    a    = np.random.randint(0,1000,[nRow, nCol])    
    matrix = a.tolist()       
    # print('The original matrix is {0}'.format(matrix))
    sln.setZeroes(matrix)
    # print('The updated matrix is {0}'.format(matrix))
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))

    print('Testcase5...')    
    tStart = time.time()        
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    sln.setZeroes(matrix)
    print(matrix)
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))
