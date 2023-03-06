"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""
import math

class Solution:
    def rotate2D(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        Assuming matrix is a list of list, representing 2-D array
        """
        N = len(matrix)

        # In case of N is odd, the innermost square belt is just one cell, no need of rotating.
        for i in range(0,int(N/2)): # outer loop for each square belt			
            for j in range(i,N-i-1):  # N-i group in the i-th square belt
                #print(i,j)
                tmp = matrix[i][j]
                matrix[i][j]         = matrix[N-j-1][i]
                matrix[N-j-1][i]     = matrix[N-i-1][N-j-1]
                matrix[N-i-1][N-j-1] = matrix[j][N-i-1]
                matrix[j][N-i-1]     = tmp
                #print(matrix)
            
if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]]
    sln.rotate2D(matrix)
    print(matrix)

    # Testcase1
    print('Testcase1...')
    matrix = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]]
    sln.rotate2D(matrix)
    print(matrix)