""" 
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7].

[chenxy]
At any time, there are at most two candiates for next move.
(1) If there is only one, then the choice is trivial
(2) If there qre two, there would be the following two alternatives:
    (a) right, down
    (b) down,  left
    (c) left,  up
    (d) up,    right
    In each of the above case, the first one should be chosen

Implementation problems:
(1) Memorize the already-passed point
(2) Identify the possible choices for the current point.
    {Neighbour points} - {already-passed points}
(3) Choose the next point for moving to
(4) Termination condition: count the moves to the number of the total points

For List[List] type input, except for regular 2-D array, special types of input such as 
[], [[]], [1,2,3],[[1,2,3]], [[1],[2],[3]], should be taken into consideration.
"""

import time

class Solution:
    #def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        ndim1 = len(matrix)        
        #print(ndim1)
        # Special cases need special handling, start.
        if ndim1 == 0:
            return []
        else:
           if not isinstance(matrix[0],list): # 1-D array 
               #print('1-D arrary')
               return matrix
           else: # 2-D array : List of List
               ndim2 = len(matrix[0])
               if ndim2 == 0:
                   return []
        # Special cases need special handling, end.
        
        # For regular 2-D array handle        
        passed   = []

        # Initialization with the first point.
        cur = [0,0]
        passed.append(cur)
        #print('ndim1 = ', ndim1, 'ndim2 = ',ndim2)
        while (len(passed) < ndim1*ndim2):
            candidate = []
            # Candidate point for next move according to geometrical constraint
            if cur[0]-1 >= 0:
                candidate.append([cur[0]-1,cur[1]])
            if cur[0]+1 < ndim1:
                candidate.append([cur[0]+1,cur[1]])

            if cur[1]-1 >= 0:
                candidate.append([cur[0],cur[1]-1])
            if cur[1]+1 < ndim2:
                candidate.append([cur[0],cur[1]+1])
            #print('candidate = ',candidate)

            # Remove the already-passed point from candidate set
            candidate1 = []
            for k in range(len(candidate)):
                #print(k,candidate[k],passed)
                if candidate[k] not in passed:
                    candidate1.append(candidate[k])
            #print('candidate1 = ',candidate1)

            # Choose the next point for moving to with horizontal-priority criterion
            # At most there will be two candidate points left, one horizontally, and one vertically.
            # When there are two left,...
            if len(candidate1) == 1:
                next = candidate1[0]
            else:    
                nextMoveCand = []
                for k in range(2):
                    if candidate1[k][0]-cur[0] == 0 and candidate1[k][1]-cur[1] == -1:
                        nextMoveCand.append('left')
                    elif candidate1[k][0]-cur[0] == 0 and candidate1[k][1]-cur[1] == 1:
                        nextMoveCand.append('right')
                    elif candidate1[k][0]-cur[0] == -1 and candidate1[k][1]-cur[1] == 0:
                        nextMoveCand.append('up')
                    else:
                        nextMoveCand.append('down')
                #print(nextMoveCand)

                next = cur.copy()
                if (nextMoveCand[0] == 'left' and nextMoveCand[1] == 'down') or (nextMoveCand[1] == 'left' and nextMoveCand[0] == 'down'):
                    # left, down --> down
                    # print('move down')
                    next[0] = next[0] + 1
                elif (nextMoveCand[0] == 'left' and nextMoveCand[1] == 'up') or (nextMoveCand[1] == 'left' and nextMoveCand[0] == 'up'):
                    # left, up --> left
                    # print('move left')
                    next[1] = next[1] - 1
                elif (nextMoveCand[0] == 'right' and nextMoveCand[1] == 'up') or (nextMoveCand[1] == 'right' and nextMoveCand[0] == 'up'):
                    # right, up --> up
                    # print('move up')
                    next[0] = next[0] - 1
                elif (nextMoveCand[0] == 'right' and nextMoveCand[1] == 'down') or (nextMoveCand[1] == 'right' and nextMoveCand[0] == 'down'):
                    # right, down --> right
                    # print('move right')
                    next[1] = next[1] + 1

            #print(cur, '-->', next)

            # Update passed and cur
            cur = next
            passed.append(cur)

        # Generate the output list according to passed and matrix
        rsltList = []
        for k in range(ndim1*ndim2):
            coord = passed[k]
            #print(k,coord)
            rsltList.append(matrix[coord[0]][coord[1]])

        return rsltList

if __name__ == '__main__':

    sln   = Solution()

    #Testcase0
    print('\nTestcase0...')
    nums = []
    print(nums, '--> ', sln.spiralOrder(nums))

    nums = [[]]
    print(nums, '--> ', sln.spiralOrder(nums))

    # Testcase1
    print('\nTestcase1...')
    nums = [1, 2, 3 ]
    print(nums, '--> ', sln.spiralOrder(nums))

    # Testcase2
    print('\nTestcase2...')
    nums = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(nums, '--> ', sln.spiralOrder(nums))

    # Testcase3
    print('\nTestcase3...')
    nums = [[1, 2, 3, 4], [5, 6, 7 , 8], [9, 10, 11, 12]]
    print(nums, '--> ', sln.spiralOrder(nums))

    # # Testcase4
    print('Testcase4...')
    nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(nums, '--> ', sln.spiralOrder(nums))

    # Testcase5
    print('\nTestcase5...')
    nums = [[1, 2],[3, 4]]
    print(nums, '--> ', sln.spiralOrder(nums))
