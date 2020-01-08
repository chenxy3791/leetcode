""" 
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

NOTE1(chenxy): 
    Note the difference among the following three method.
    The third one requirs a zig-zag type traverse, and is the most difficult.
NOTE2(chenxy): 
    Not limited to square matrix. That is to say, n may not equal to m.
"""

import time

class Solution:
    #def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    def findDiagonalOrder1(self, matrix):
        ndim1 = len(matrix)
        if ndim1 == 0:
            return []
        ndim2 = len(matrix[0])
        if ndim2 == 0:
            return []

        output = []
        for k in range(ndim1+ndim2-1): # 0...(ndim1+ndim2-2)
            for i in range(min(ndim1-1,k),max(0,k-ndim2+1)-1,-1):                
                #print('k={0}, i={1}'.format(k,i))
                output.append(matrix[i][k-i])

        return output

    def findDiagonalOrder2(self, matrix):
        ndim1 = len(matrix)
        if ndim1 == 0:
            return []
        ndim2 = len(matrix[0])
        if ndim2 == 0:
            return []

        output = []
        for k in range(ndim1+ndim2-1): # 0...(ndim1+ndim2-2)
            for j in range(min(ndim2-1,k),max(0,k-ndim1+1)-1,-1):                
                #print('k={0}, j={1}'.format(k,j))
                output.append(matrix[k-j][j])

        return output

    def findDiagonalOrder3(self, matrix):
        ndim1 = len(matrix)
        if ndim1 == 0:
            return []
        ndim2 = len(matrix[0])
        if ndim2 == 0:
            return []
        
        output = []
        for k in range(ndim1+ndim2-1): # 0...(ndim1+ndim2-2)
            if k % 2 == 0: # i in descending order
                for i in range(min(ndim1-1,k),max(0,k-ndim2+1)-1,-1):                
                    #print('k={0}, i={1}'.format(k,i))
                    output.append(matrix[i][k-i])
            else:          # j in descending order
                for j in range(min(ndim2-1,k),max(0,k-ndim1+1)-1,-1):                
                    #print('k={0}, j={1}'.format(k,j))
                    output.append(matrix[k-j][j])

        return output

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    print(sln.findDiagonalOrder1(matrix))
    print(sln.findDiagonalOrder2(matrix))
    print(sln.findDiagonalOrder3(matrix))

    # Testcase1
    print('Testcase1...')
    matrix = [[1]]
    print(sln.findDiagonalOrder3(matrix))

    # Testcase2
    print('Testcase2...')
    matrix = [[]]
    print(sln.findDiagonalOrder3(matrix))

    # Testcase3
    print('Testcase3...')
    matrix = []
    print(sln.findDiagonalOrder3(matrix))

    # Testcase4
    print('Testcase4...')
    matrix = [[1,2,3]]
    print(sln.findDiagonalOrder3(matrix))

    # Testcase5
    print('Testcase4...')
    matrix = [[1,2,3],[4,5,6]]
    print(sln.findDiagonalOrder1(matrix))
    print(sln.findDiagonalOrder2(matrix))    
    print(sln.findDiagonalOrder3(matrix))

    # Testcase6
    print('Testcase6...')
    matrix = [[1],[2],[3],[4],[5],[6]]
    print(sln.findDiagonalOrder1(matrix))
    print(sln.findDiagonalOrder2(matrix))    
    print(sln.findDiagonalOrder3(matrix))


    # # Testcase3
    # print('Testcase3...')
    # matrix = [9, 9, 9, 9, 9]
    # print(sln.findDiagonalOrder(matrix))

    # # Testcase4
    # print('Testcase4...')
    # matrix = [9, 9, 8, 9, 9]
    # print(sln.findDiagonalOrder(matrix))
