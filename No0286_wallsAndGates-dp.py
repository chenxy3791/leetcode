""" 
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 
to represent INF as you may assume that the distance to a gate is less than 
2147483647.
Fill each empty room with the distance to its nearest gate. If it is 
impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""

import time

class Solution:
    #def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms) -> None:
        #Dynamical programming, but NG, need further investigation
        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 

        memo = dict()
        visited = []
        nRow = len(rooms)
        nCol = len(rooms[0])

        def neighbours(a):
            neighb = []
            if a[0] > 0: # up
                neighb.append((a[0]-1,a[1]))
            if a[0] < nRow - 1: # down
                neighb.append((a[0]+1,a[1]))            
            if a[1] > 0: # left
                neighb.append((a[0],a[1]-1))            
            if a[1] < nCol - 1: # right
                neighb.append((a[0],a[1]+1))            
            return neighb

        def dp(coordi):            
            if coordi in memo:
                print('dp({0},{1}) == {2}'.format(coordi[0],coordi[1],memo[coordi]))
                return memo[coordi]
            if rooms[coordi[0]][coordi[1]] == 0:
                # This is a gate;
                memo[coordi] = 0;
                print('dp({0},{1}) == {2}'.format(coordi[0],coordi[1],memo[coordi]))
                return 0
            
            visited.append(coordi)
            neighb = neighbours(coordi)            
            dMax = -2;
            for room in neighb:                
                print('room = {0}'.format(room))
                if (rooms[room[0]][room[1]] == -2) or (rooms[room[0]][room[1]] == -1):
                    print('Wall or unreachable, pass')
                    continue # Wall or already flagged as unreachable, don't search for it again.
                if room in visited:
                    print('Visited, pass')
                    continue
                dTmp = dp(room)
                visited.pop()
                
                if dMax < dTmp:
                    dMax = dTmp
            
            if dMax >= 0:
                dist = 1 + dMax
            else:
                dist = dMax

            memo[coordi] = dist
            rooms[coordi[0]][coordi[1]] = dist
            print('dp({0},{1}) == {2}'.format(coordi[0],coordi[1],dist))
            return dist
        
        for i in range(nRow):
            for j in range(nCol):
                dist = dp((i,j))
        # Finally, convert '-2'--unreachable to INF as required by the problem statement
        for i in range(nRow):
            for j in range(nCol):
                if rooms[i][j] == -2:
                    rooms[i][j] = 2**31 - 1        

        return

if __name__ == '__main__':

    sln = Solution()
    print('\nTestcase#1 ...... start!')
    INF = 2**31-1
    rooms = [[INF,  -1,   0, INF],    
             [INF, INF, INF,  -1],    
             [INF,  -1, INF,  -1],    
             [0  ,  -1, INF, INF]]
    print('The original rooms : ')
    for k in range(len(rooms)):
        print(rooms[k])
    sln.wallsAndGates(rooms)
    print('After conversion : ')
    for k in range(len(rooms)):
        print(rooms[k])    

    print('\nTestcase#2 ...... start!')
    rooms = []
    print('The original rooms : ')
    for k in range(len(rooms)):
        print(rooms[k])
    sln.wallsAndGates(rooms)
    print('After conversion : ')
    for k in range(len(rooms)):
        print(rooms[k])        

    # print('\nTestcase#3 ...stress test... start!')
    # import numpy as np    
    # for nRow in range(20,80,20):
    #     for nCol in range(20,80,20):            
    #         rArray = np.random.randn(nRow,nCol)
    #         rArray[rArray>=0] = 2**31-1
    #         rArray[rArray<0]  = -1
    #         rArray[nRow-1,nCol-1] = 0
    #         rooms = rArray.tolist()
    #         # print('nRow = {0}, nCol = {1}'.format(len(rooms),len(rooms[0])))
    #         # print('The original rooms : ')
    #         # for k in range(5):
    #         #     print(rooms[k][:5])    
    #         tStart = time.time()                
    #         sln.wallsAndGates(rooms)
    #         tElapsed = time.time() - tStart        
    #         print('nRow = {0}, nCol = {1}, tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    #         # print('After conversion : ')
    #         # for k in range(len(rooms)):
    #         #     print(rooms[k])    

    # # print('\nTestcase#4 ...stress test... start!')
    # # rooms = 
    # # print('nRow = {0}, nCol = {1}'.format(len(rooms),len(rooms[0])))
    # # tStart = time.time()                
    # # sln.wallsAndGates(rooms)
    # # tElapsed = time.time() - tStart        
    # # print('nRow = {0}, nCol = {1}, tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    # # print('After conversion : ')
    # # for k in range(5):
    # #     print(rooms[k][:5])    