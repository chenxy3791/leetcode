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
        """
        Do not return anything, modify rooms in-place instead.

        Flag the unreachable to '-2'.
        Finally, convert '-2'(unreachable) to INF to avoid the confusion with the initialized INF
        """        
        def isEmpty(a):
            return (rooms[a[0]][a[1]] == (2**31 - 1))

        def isWall(a):
            return (rooms[a[0]][a[1]] == -1) 

        def isUnreachable(a):
            return (rooms[a[0]][a[1]] == -2)

        def isVisited(a):
            return (a in visited)

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

        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 
        nRow = len(rooms)
        nCol = len(rooms[0])
        visitCnt = 0
        for i in range(nRow):
            for j in range(nCol):
                # print('\nSearch from ({0}, {1})...START'.format(i,j))
                start = (i,j)
                if not isEmpty(start):
                    # print('rooms[{0}][{1}] = {2} is not empty, skip it!'.format(i,j, rooms[i][j]))
                    continue

                nxtLayer  = [start] # 
                visited   = []
                gateFound = False
                unReachable = False
                depth = 0
                while len(nxtLayer) > 0:
                    curLayer = nxtLayer
                    nxtLayer = []
                    for cur in curLayer:
                        # print('cur = {0}'.format(cur))
                        visited.append(cur)
                        visitCnt += 1
                        if rooms[cur[0]][cur[1]] == 0:
                            # Find a gate, flagging the start node in this round of search.
                            # print('Found a gate: i = {0}, j = {1}, depth = {2}'.format(i,j,depth))
                            rooms[i][j] = depth
                            gateFound = True
                            break
                        # elif rooms[cur[0]][cur[1]] == -1: # Wall. Impossible in this implementation.
                        #     continue      
                        elif rooms[cur[0]][cur[1]] == -2: # Already flagged as unreachable
                            unReachable = True
                            break
                        else:
                            # Add all neighbours of a to nxtLayer, but need check to avoid duplicate
                            neighb = neighbours(cur)
                            # print('cur = {0}, neighb = {1}'.format(cur, neighb))
                            for k in range(len(neighb)):
                                x = neighb[k]                            
                                if (not isWall(x) and not isVisited(x)) and not(x in nxtLayer):
                                    # print('Append x = {0} to nxtLayer, rooms[x] = {1}'.format(x, rooms[x[0]][x[1]]))
                                    nxtLayer.append(x)
                            # print('nxtLayer = {0}'.format(nxtLayer))
                    if gateFound is True or unReachable is True:
                        break
                    depth = depth + 1

                if gateFound is False or unReachable is True:
                    # Not found a path, flag all node in the path as unreachable (-2)
                    for x in visited:
                        rooms[x[0]][x[1]] = -2
                # print('\nSearch from ({0}, {1})...END'.format(i,j))

        # Finally, convert '-2'--unreachable to INF as required by the problem statement
        for i in range(nRow):
            for j in range(nCol):
                if rooms[i][j] == -2:
                    rooms[i][j] = 2**31 - 1
        print('Solution: total visit count = {0}'.format(visitCnt))

class Solution1:
    #def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Flag the unreachable to '-2'.
        Finally, convert '-2'(unreachable) to INF to avoid the confusion with the initialized INF

        The same algorithm with Solution, except that disable the use of the following functions.
        Only has marginal performance improvement.
        """        
        # def isEmpty(a):
        #     return (rooms[a[0]][a[1]] == (2**31 - 1))

        # def isWall(a):
        #     return (rooms[a[0]][a[1]] == -1) 

        # def isUnreachable(a):
        #     return (rooms[a[0]][a[1]] == -2)

        # def isVisited(a):
        #     return (a in visited)

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

        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 
        nRow = len(rooms)
        nCol = len(rooms[0])
        visitCnt = 0
        for i in range(nRow):
            for j in range(nCol):
                # print('\nSearch from ({0}, {1})...START'.format(i,j))
                start = (i,j)
                if (rooms[i][j] != (2**31 - 1)):
                    # print('rooms[{0}][{1}] = {2} is not empty, skip it!'.format(i,j, rooms[i][j]))
                    continue

                nxtLayer  = [start] # 
                visited   = []
                gateFound = False
                unReachable = False
                depth = 0
                while len(nxtLayer) > 0:
                    curLayer = nxtLayer
                    nxtLayer = []
                    for cur in curLayer:
                        # print('cur = {0}'.format(cur))
                        visited.append(cur)
                        visitCnt += 1
                        if rooms[cur[0]][cur[1]] == 0:
                            # Find a gate, flagging the start node in this round of search.
                            # print('Found a gate: i = {0}, j = {1}, depth = {2}'.format(i,j,depth))
                            rooms[i][j] = depth
                            gateFound = True
                            break
                        # elif rooms[cur[0]][cur[1]] == -1: # Wall. Impossible in this implementation.
                        #     continue      
                        elif rooms[cur[0]][cur[1]] == -2: # Already flagged as unreachable
                            unReachable = True
                            break
                        else:
                            # Add all neighbours of a to nxtLayer, but need check to avoid duplicate
                            neighb = neighbours(cur)
                            # print('cur = {0}, neighb = {1}'.format(cur, neighb))
                            for k in range(len(neighb)):
                                x = neighb[k]                            
                                if (not (rooms[x[0]][x[1]] == -1) and not (x in visited)) and not(x in nxtLayer):
                                    # print('Append x = {0} to nxtLayer, rooms[x] = {1}'.format(x, rooms[x[0]][x[1]]))
                                    nxtLayer.append(x)
                            # print('nxtLayer = {0}'.format(nxtLayer))
                    if gateFound is True or unReachable is True:
                        break
                    depth = depth + 1

                if gateFound is False or unReachable is True:
                    # Not found a path, flag all node in the path as unreachable (-2)
                    for x in visited:
                        rooms[x[0]][x[1]] = -2
                # print('\nSearch from ({0}, {1})...END'.format(i,j))

        # Finally, convert '-2'--unreachable to INF as required by the problem statement
        for i in range(nRow):
            for j in range(nCol):
                if rooms[i][j] == -2:
                    rooms[i][j] = 2**31 - 1

        print('Solution1: total visit count = {0}'.format(visitCnt))

class Solution2:
    #def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Flag the unreachable to '-2'.
        Finally, convert '-2'(unreachable) to INF to avoid the confusion with the initialized INF
        """        
        def isEmpty(a):
            return (rooms[a[0]][a[1]] == (2**31 - 1))

        def isWall(a):
            return (rooms[a[0]][a[1]] == -1) 

        def isUnreachable(a):
            return (rooms[a[0]][a[1]] == -2)

        def isVisited(a):
            return (a in visited)

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

        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 
        nRow = len(rooms)
        nCol = len(rooms[0])
        visitCnt = 0
        for i in range(nRow):
            for j in range(nCol):
                # print('\nSearch from ({0}, {1})...START'.format(i,j))
                start = (i,j)
                if not isEmpty(start):
                    # print('rooms[{0}][{1}] = {2} is not empty, skip it!'.format(i,j, rooms[i][j]))
                    continue
                layers    = []
                nxtLayer  = [start] # 
                visited   = []
                gateFound = False
                unReachable = False
                depth = 0
                while len(nxtLayer) > 0:
                    curLayer = nxtLayer
                    layers.append(curLayer)
                    nxtLayer = []
                    for cur in curLayer:
                        # print('cur = {0}'.format(cur))
                        visited.append(cur)
                        visitCnt += 1
                        if rooms[cur[0]][cur[1]] == 0:
                            # Find a gate, flagging the start node in this round of search.
                            # print('Found a gate: i = {0}, j = {1}, depth = {2}'.format(i,j,depth))
                            rooms[i][j] = depth
                            # Backtracking: start from cur:
                            for layIndex in range(depth-1,0,-1):
                                for r in layers[layIndex]:
                                    if cur in neighbours(r):
                                        rooms[r[0]][r[1]] = depth - layIndex
                                        cur = r
                                        break
                                    
                            gateFound = True
                            break
                        # elif rooms[cur[0]][cur[1]] == -1: # Wall. Impossible in this implementation.
                        #     continue      
                        elif rooms[cur[0]][cur[1]] == -2: # Already flagged as unreachable
                            unReachable = True
                            break
                        else:
                            # Add all neighbours of a to nxtLayer, but need check to avoid duplicate
                            neighb = neighbours(cur)
                            # print('cur = {0}, neighb = {1}'.format(cur, neighb))
                            for k in range(len(neighb)):
                                x = neighb[k]                            
                                if (not isWall(x) and not isVisited(x)) and not(x in nxtLayer):
                                    # print('Append x = {0} to nxtLayer, rooms[x] = {1}'.format(x, rooms[x[0]][x[1]]))
                                    nxtLayer.append(x)
                            # print('nxtLayer = {0}'.format(nxtLayer))
                    if gateFound is True or unReachable is True:
                        break
                    depth = depth + 1

                if gateFound is False or unReachable is True:
                    # Not found a path, flag all node in the path as unreachable (-2)
                    for x in visited:
                        rooms[x[0]][x[1]] = -2
                # print('\nSearch from ({0}, {1})...END'.format(i,j))

        # Finally, convert '-2'--unreachable to INF as required by the problem statement
        for i in range(nRow):
            for j in range(nCol):
                if rooms[i][j] == -2:
                    rooms[i][j] = 2**31 - 1
        print('Solution2: total visit count = {0}'.format(visitCnt))

class Solution3:
    #def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Search from gate...
        """        
        def isEmpty(a):
            return (rooms[a[0]][a[1]] == (2**31 - 1))

        def isWall(a):
            return (rooms[a[0]][a[1]] == -1) 

        def isUnreachable(a):
            return (rooms[a[0]][a[1]] == -2)

        def isVisited(a):
            return (a in visited)

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

        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 
        nRow = len(rooms)
        nCol = len(rooms[0])
        visitCnt = 0
        for i in range(nRow):
            for j in range(nCol):                
                if not (rooms[i][j] == 0):
                    # Not a gate, nothing to do.
                    continue
                #print('\nSearch from ({0}, {1})...START'.format(i,j))
                nxtLayer  = [(i,j)] 
                visited   = []
                depth = 0
                while len(nxtLayer) > 0:
                    curLayer = nxtLayer
                    #layers.append(curLayer)
                    nxtLayer = []
                    for cur in curLayer:
                        # print('cur = {0}'.format(cur))
                        visited.append(cur)
                        visitCnt += 1
                        if rooms[cur[0]][cur[1]] > depth:
                            rooms[cur[0]][cur[1]] = depth

                        # For non-Wall room, add its neighbours to nxtLayer, but need check to avoid duplicate
                        neighb = neighbours(cur)
                        # print('cur = {0}, neighb = {1}'.format(cur, neighb))
                        for k in range(len(neighb)):
                            x = neighb[k]                            
                            if (not isWall(x) and not isVisited(x)) and not(x in nxtLayer):
                                # print('Append x = {0} to nxtLayer, rooms[x] = {1}'.format(x, rooms[x[0]][x[1]]))
                                nxtLayer.append(x)
                            # print('nxtLayer = {0}'.format(nxtLayer))
                    depth = depth + 1

        print('Solution3: total visit count = {0}'.format(visitCnt))

class Solution4:
    #def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        Search from gate...
        """        
        def isEmpty(a):
            return (rooms[a[0]][a[1]] == (2**31 - 1))

        def isWall(a):
            return (rooms[a[0]][a[1]] == -1) 

        def isUnreachable(a):
            return (rooms[a[0]][a[1]] == -2)

        def isVisited(a):
            return (a in visited)

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

        if len(rooms) == 0:
            return 
        if len(rooms[0]) == 0:
            return 
        nRow = len(rooms)
        nCol = len(rooms[0])
        visitCnt = 0
        for i in range(nRow):
            for j in range(nCol):                
                if not (rooms[i][j] == 0):
                    # Not a gate, nothing to do.
                    continue
                #print('\nSearch from ({0}, {1})...START'.format(i,j))
                nxtLayer  = [(i,j)] 
                visited   = []
                depth = 0
                while len(nxtLayer) > 0:
                    curLayer = nxtLayer
                    #layers.append(curLayer)
                    nxtLayer = []
                    for cur in curLayer:
                        #print('cur = {0}'.format(cur))
                        visited.append(cur)
                        visitCnt += 1
                        if rooms[cur[0]][cur[1]] >= depth:
                            rooms[cur[0]][cur[1]] = depth
                            # Only add the neighbours of updated rooms to nxtLayer, but need check to avoid duplicate
                            neighb = neighbours(cur)
                            #print('cur = {0}, neighb = {1}'.format(cur, neighb))
                            for k in range(len(neighb)):
                                x = neighb[k]                            
                                if (not isWall(x) and not isVisited(x)) and not(x in nxtLayer):
                                    # print('Append x = {0} to nxtLayer, rooms[x] = {1}'.format(x, rooms[x[0]][x[1]]))
                                    nxtLayer.append(x)
                                # print('nxtLayer = {0}'.format(nxtLayer))
                    depth = depth + 1

        print('Solution4: total visit count = {0}'.format(visitCnt))

def printListOfList(lol, nRow, nCol):
    for k in range(nRow):
        print(rooms[k][:nCol])

if __name__ == '__main__':

    import numpy as np    
    import os
    import copy

    sln  = Solution()
    sln1 = Solution1()
    sln2 = Solution2()
    sln3 = Solution3()    
    sln4 = Solution4()        
    print('\nTestcase#1 ...... start!')
    INF = 2**31-1
    rooms = [[INF,  -1,   0, INF],    
             [INF, INF, INF,  -1],    
             [INF,  -1, INF,  -1],    
             [0  ,  -1, INF, INF]]
    rooms1 = copy.deepcopy(rooms)             
    rooms2 = copy.deepcopy(rooms)                 
    rooms3 = copy.deepcopy(rooms)                     
    rooms4 = copy.deepcopy(rooms)                             

    print('The original rooms : ')
    for k in range(len(rooms)):
        print(rooms[k])
    sln.wallsAndGates(rooms)
    print('Solution - After conversion : ')
    for k in range(len(rooms)):
        print(rooms[k])    

    # sln1.wallsAndGates(rooms1)
    # print('Solution1 - After conversion : ')
    # for k in range(len(rooms1)):
    #     print(rooms1[k])    

    sln2.wallsAndGates(rooms2)
    print('Solution2 - After conversion : ')
    for k in range(len(rooms2)):
        print(rooms2[k])    

    sln3.wallsAndGates(rooms3)
    print('Solution3 - After conversion : ')
    for k in range(len(rooms3)):
        print(rooms3[k])    
 
    sln4.wallsAndGates(rooms4)
    print('Solution4 - After conversion : ')
    for k in range(len(rooms4)):
        print(rooms4[k])    

    # print('\nTestcase#2 ...... start!')
    # rooms = []
    # print('The original rooms : ')
    # for k in range(len(rooms)):
    #     print(rooms[k])
    # sln.wallsAndGates(rooms)
    # print('After conversion : ')
    # for k in range(len(rooms)):
    #     print(rooms[k])        

    # print('\nTestcase#3 ...... start!')
    # rooms = [[-1.0, 2147483647.0, -1.0, -1.0, 2147483647.0],
    #         [2147483647.0, 2147483647.0, 2147483647.0, 2147483647.0, -1.0],
    #         [2147483647.0, -1.0, -1.0, 2147483647.0, -1.0],
    #         [-1.0, -1.0, -1.0, 2147483647.0, -1.0],
    #         [2147483647.0, 2147483647.0, -1.0, 2147483647.0, 0.0]]
    # nRow = len(rooms)
    # nCol = nRow
    # print('The original rooms : ')
    # printListOfList(rooms, nRow, nCol)
    # tStart = time.time()                
    # sln.wallsAndGates(rooms)
    # tElapsed = time.time() - tStart        
    # print('nRow = {0}, nCol = {1}, tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    # print('After conversion : ')
    # printListOfList(rooms, nRow, nCol)

    # print('\nTestcase#4 ...stress test... start!')
    # nRow = 20
    # nCol = nRow
    # rArray = np.random.randn(nRow,nCol)
    # rArray[rArray>=0] = 2**31-1
    # rArray[rArray<0]  = -1
    # rArray[nRow-1,nCol-1] = 0
    # rooms = rArray.tolist()
    # print('The original rooms : ')
    # printListOfList(rooms, nRow, nCol)    
    # tStart = time.time()                
    # sln.wallsAndGates(rooms)
    # tElapsed = time.time() - tStart        
    # print('nRow = {0}, nCol = {1}, tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    # print('After conversion : ')
    # printListOfList(rooms, nRow, nCol)        


    # print('\nTestcase#5 ...stress test... start!')
    # import numpy as np    
    # for nRow in range(10,20,20):
    #     nCol = nRow            
    #     rArray = np.random.randn(nRow,nCol)
    #     rArray[rArray>=0] = 2**31-1
    #     rArray[rArray<0]  = -1
    #     rArray[nRow-1,nCol-1] = 0
    #     rooms = rArray.tolist()
    #     print('nRow = {0}, nCol = {1}'.format(len(rooms),len(rooms[0])))
    #     print('The original rooms : ')
    #     for k in range(nRow-5,nRow):
    #         print(rooms[k][:])    
    #     tStart = time.time()                
    #     sln.wallsAndGates(rooms)
    #     tElapsed = time.time() - tStart        
    #     print('nRow = {0}, nCol = {1}, tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    #     print('After conversion : ')
    #     for k in range(len(rooms)):
    #         print(rooms[k])    

    print('\nTestcase#6 ...stress test... start!')        
    # Reference: https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files
    filename = 'wallsAndGates_testdata.py'
    exec(compile(open(filename).read(),'dummy','exec'))

    nDel = 70
    a = np.array(rooms)
    # Delete some rows from the center of a
    delStart = int((a.shape[0]-nDel)/2)
    delStop  = delStart + nDel - 1
    a = np.delete(a,list(np.arange(delStart, delStop+1)),0)
    a = np.delete(a,list(np.arange(delStart, delStop+1)),1)
    print(delStart, delStop, a.shape)
    rooms = a.tolist()
    rooms1 = copy.deepcopy(rooms)
    rooms2 = copy.deepcopy(rooms)
    rooms3 = copy.deepcopy(rooms)                     
    rooms4 = copy.deepcopy(rooms)                   

    nRow  = len(rooms)
    nCol  = len(rooms[0])
    print('nRow = {0}, nCol = {1}'.format(nRow,nCol))
    #print('The original rooms : ')
    #printListOfList(rooms, nRow, nCol)

    tStart = time.time()                
    sln.wallsAndGates(rooms)
    tElapsed = time.time() - tStart        
    print('Solution(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))

    # tStart = time.time()                
    # sln1.wallsAndGates(rooms1)
    # tElapsed = time.time() - tStart        
    # print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    # assert( (rooms == rooms1) )

    tStart = time.time()                
    sln2.wallsAndGates(rooms2)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms2) )

    tStart = time.time()                
    sln3.wallsAndGates(rooms3)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms3) )

    tStart = time.time()                
    sln4.wallsAndGates(rooms4)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms4) )

    print('\nTestcase#7 ...stress test... start!')        
    filename = 'wallsAndGates_testdata2.py'
    exec(compile(open(filename).read(),'dummy','exec'))

    nDel = 0
    a = np.array(rooms)
    # Delete some rows from the center of a
    delStart = int((a.shape[0]-nDel)/2)
    delStop  = delStart + nDel - 1
    a = np.delete(a,list(np.arange(delStart, delStop+1)),0)
    a = np.delete(a,list(np.arange(delStart, delStop+1)),1)
    print(delStart, delStop, a.shape)
    rooms = a.tolist()
    rooms1 = copy.deepcopy(rooms)
    rooms2 = copy.deepcopy(rooms)
    rooms3 = copy.deepcopy(rooms)                     
    rooms4 = copy.deepcopy(rooms)      

    nRow  = len(rooms)
    nCol  = len(rooms[0])
    print('nRow = {0}, nCol = {1}'.format(nRow,nCol))
    #print('The original rooms : ')
    #printListOfList(rooms, nRow, nCol)

    tStart = time.time()                
    sln.wallsAndGates(rooms)
    tElapsed = time.time() - tStart        
    print('Solution(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))

    # tStart = time.time()                
    # sln1.wallsAndGates(rooms1)
    # tElapsed = time.time() - tStart        
    # print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    # assert( (rooms == rooms1) )

    tStart = time.time()                
    sln2.wallsAndGates(rooms2)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms2) )

    tStart = time.time()                
    sln3.wallsAndGates(rooms3)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms3) )    

    tStart = time.time()                
    sln4.wallsAndGates(rooms4)
    tElapsed = time.time() - tStart        
    print('Solution1(): tElapsed = {2}(sec)'.format(nRow,nCol,tElapsed))
    assert( (rooms == rooms4) )        