"""
You have a lock in front of you with 4 circular wheels. 
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to 
be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 
4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any 
of these codes, the wheels of the lock will stop turning and you will be unable 
to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if 
it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1

Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
"""

class Solution:
    #def openLock(self, deadends: List[str], target: str) -> int:
    def openLock(self, deadends, target: str) -> int:
        def neighbours(a):
            neighbs = []
            for k in range(len(a)):
                b = a[:k] + str((int(a[k]) + 1)%10) + a[k+1:]
                neighbs.append(b)
                b = a[:k] + str((int(a[k]) - 1)%10) + a[k+1:]
                neighbs.append(b)
            #print(a, neighbs)
            return neighbs
                
        if "0000" in deadends:
            return -1

        q       = ['0000']
        turnCnt = -1
        visited = deadends.copy()
        visited.append('0000')
        while len(q) > 0:
            qSize = len(q)
            turnCnt = turnCnt + 1
            # print('turnCnt = {0}, qSize = {1}'.format(turnCnt,qSize))
            #print(q, visited)
            for k in range(qSize):
                a = q.pop(0)
                #visited.append(a)
                if a == target:
                    return turnCnt
                else: # Add a's neighbours into q, without duplicate.                    
                    neighbs = neighbours(a)
                    for node in neighbs:
                        #if node not in visited:
                        if not(node in visited):
                            q.append(node)
                            visited.append(node)
        
        return -1

class Solution1:
    #def openLock(self, deadends: List[str], target: str) -> int:
    def openLock(self, deadends, target: str) -> int:
        def neighbours(a):
            neighbs = []
            for k in range(len(a)):
                b = a.copy()
                b[k] = int(a[k] + 1) % 10
                neighbs.append(b)
                b = a.copy()
                b[k] = int(a[k] - 1) % 10
                neighbs.append(b)
            #print(a, neighbs)
            return neighbs
                
        if "0000" in deadends:
            return -1

        #grids = 10*[10*[10*[10*[0]]]]
        grids = 10000*[0]
        # Initialize all grids corresponding to deadends to 1
        for node in deadends:            
            k0 = int(node[0])
            k1 = int(node[1])
            k2 = int(node[2])
            k3 = int(node[3])
            grids[k0+10*k1+100*k2+1000*k3] = 1

        targetLst = [int(target[0]), int(target[1]), int(target[2]), int(target[3])]
        start = [0,0,0,0] # Corresponding to "0000"
        q = []
        q.append(start)
        turnCnt = -1

        while len(q) > 0:
            qSize = len(q)
            turnCnt = turnCnt + 1
            # print('turnCnt = {0}, qSize = {1}, q = {2}'.format(turnCnt, qSize, q))
            for k in range(qSize):
                a = q.pop(0)
                # print('a = {0}, targetLst = {1}'.format(a, targetLst))
                if a == targetLst:
                    return turnCnt
                else: # Add a's neighbours into q, without duplicate.                    
                    neighbs = neighbours(a)
                    # print('a = {0}'.format(a))
                    for node in neighbs:                        
                        #print('node = {0}, grids[node] = {1}'.format(node,grids[node[0]][node[1]][node[2]][node[3]]))
                        idx = node[0]+10*node[1]+100*node[2]+1000*node[3]
                        if grids[idx] == 0:
                            q.append(node)
                            grids[idx] = 1
        
        return -1

if __name__ == '__main__':    

    import time
    sln    = Solution()
    sln1   = Solution1()

    # print('Testcase1...')
    # deadends = ["0201","0101","0102","1212","2002"]
    # target = "0202"
    # tStart = time.time()  
    # print('expected = 6, actual = {0}, tElapsed = {1}'.format(sln.openLock(deadends, target), (time.time() - tStart)))

    deadends = ["0201","0101","0102","1212","2002"]
    print('Before, deadends length = {0}'.format(len(deadends)))
    target = "0202"
    tStart = time.time() 
    print('expected = 6, actual = {0}, tElapsed = {1}'.format(sln1.openLock(deadends, target), (time.time() - tStart)))
    print('After, deadends length = {0}'.format(len(deadends)))

    # print('Testcase2...')
    # deadends = ["8888"]
    # target = "0009"    
    # tStart = time.time() 
    # print('expected = 1, actual = {0}, tElapsed = {1}'.format(sln.openLock(deadends, target), (time.time() - tStart)))

    # print('Testcase3...')
    # deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    # target = "8888"
    # tStart = time.time() 
    # print('expected = -1, actual = {0}, tElapsed = {1}'.format(sln.openLock(deadends, target), (time.time() - tStart)))

    # print('Testcase4...')
    # deadends = ["0000"]
    # target = "8888"
    # tStart = time.time() 
    # print('expected = -1, actual = {0}, tElapsed = {1}'.format(sln.openLock(deadends, target), (time.time() - tStart)))

    print('\nTestcase5...')
    deadends = ["6586","6557","0399","3436","1106","4255","1161","7546","2375","5535","7623","0805","7045","8244","1804","1777","5152","7241","4488","3653","7485","9103","2726","4624","8654","1404","9321","5145","4237","5423","9350","3383","8658","2601","2446","1605","6804","1521","0832","5555","6710","3851","6370","0069","7369","6352","4165","4327","9727","1363","9906","9463","8628","5239","0009","2743","0419","4722","7251","5645","5159","4040","1406","5836","0623","9851","2970","0479","1707","5248","0135","8840","9395","1068","9653","4461","6830","7851","7798","3745","1608","2061","5404","3536","3875","3552","8430","0846","5575","2835","1777","5848","5181","8129","2408","3257","9168","3279","4705","9799","1592","7849","4934","1210","0384","3946","5200","3702","4792","1363","0340","4623","9837","0798","2400","0859","3002","1819","2925","8966","7065","3310","1415","9986","7612","1233","9681","6869","5324","4271","1632","2947","8829","9102","9502","4896","2556","4998","7642","8477","4439","8391","7171","2081","5401","0369","4498","1269","2535","7805","6611","1605","1432","6237","5565","9618","2123","5178","3649","8657","6236","6737","1561","1802","1349","9738","6245","7202","8442","7183","5105","7963","0259","5622","3098","0664","7366","1556","5711","9981","4607","2063","7540","1818","7320","8505","1028","6127","1816","8961","7126","4739","4050","7729","5887","4836","1244","2697","3937","9817","2759","9536","0154","7214","5688","1284","5434","7103","2704","6790","3244","8797","3860","1988","1458","4268","1901","4787","7599","6672","3579","3726","6670","1603","3332","7249","0984","6783","4456","0023","2678","0167","8626","6080","5716","5083","6135","8700","7890","8683","2089","0264","2123","0787","3056","2647","4645","8748","6936","6899","0031","4934","0221","9481","9959","1386","7695","2034","0466","0809","9166","6381","6937","0744","8059","8498","5772","8379","4448","5794","7423","2568","4671","6408","4335","1655","3662","1250","5262","7197","6831","8004","0575","8784","2920","0869","7157","0153","7255","1541","1247","5498","0566","6632","7640","1733","2546","5110","2852","8042","8175","0284","8589","8918","5755","2289","0812","4850","4650","9018","6649","5099","6532","9891","8675","1718","5442","6786","8915","3710","3833","2659","7040","3959","2505","7574","1199","3465","4557","7230","9161","5177","7815","4564","1470","8051","6287","2504","4025","8911","6158","6857","8948","7991","3670","3413","0423","7184","7921","1351","8908","1921","1685","5579","4641","0286","6410","2800","7018","1402","7410","3471","1312","9530","4581","5364","4820","8192","3088","4714","2255","2342","5042","8673","9788","2203","0879","2345","9712","2008","0652","0939","0720","2954","4482","2390","0807","4634","6266","5222","6898","7491","0294","1811","0667","8282","5754","1841","9518","9093","7904","4902","0068","5157","7823","8073","8801","8179","1402","9977","2332","9448","2251","8455","6157","1878","4183","3331","8047","1254","9639","2156","5780","7359","0260","9683","6842","1098","6495","2057","6583","0932","2577","1818","6042","8358","1833","5512","4529","0583","9955","9205","6055","3322","2232","5372","5835","2202","9696","1596","3424","3696","5695","1365","6432","0327","1565","8509","6936","3363","3007","3107","0410","6258","2492","0300","1255","1664","8666","6826","9961","5782","0140","5567","9596","1680","1892","5016","8804","4962","9318","4540","5044","0979","2004","4265","7689","0289","3434","6090","1375","3135","3935","5140","9255","3997","3482","8150","8164","0787"]
    # print('Before, deadends length = {0}'.format(len(deadends)))
    target = "8828"
    tStart = time.time() 
    print('expected = ?, actual = {0}, tElapsed = {1}'.format(sln.openLock(deadends, target), (time.time() - tStart)))
    # print('After, deadends length = {0}'.format(len(deadends)))

    deadends = ["6586","6557","0399","3436","1106","4255","1161","7546","2375","5535","7623","0805","7045","8244","1804","1777","5152","7241","4488","3653","7485","9103","2726","4624","8654","1404","9321","5145","4237","5423","9350","3383","8658","2601","2446","1605","6804","1521","0832","5555","6710","3851","6370","0069","7369","6352","4165","4327","9727","1363","9906","9463","8628","5239","0009","2743","0419","4722","7251","5645","5159","4040","1406","5836","0623","9851","2970","0479","1707","5248","0135","8840","9395","1068","9653","4461","6830","7851","7798","3745","1608","2061","5404","3536","3875","3552","8430","0846","5575","2835","1777","5848","5181","8129","2408","3257","9168","3279","4705","9799","1592","7849","4934","1210","0384","3946","5200","3702","4792","1363","0340","4623","9837","0798","2400","0859","3002","1819","2925","8966","7065","3310","1415","9986","7612","1233","9681","6869","5324","4271","1632","2947","8829","9102","9502","4896","2556","4998","7642","8477","4439","8391","7171","2081","5401","0369","4498","1269","2535","7805","6611","1605","1432","6237","5565","9618","2123","5178","3649","8657","6236","6737","1561","1802","1349","9738","6245","7202","8442","7183","5105","7963","0259","5622","3098","0664","7366","1556","5711","9981","4607","2063","7540","1818","7320","8505","1028","6127","1816","8961","7126","4739","4050","7729","5887","4836","1244","2697","3937","9817","2759","9536","0154","7214","5688","1284","5434","7103","2704","6790","3244","8797","3860","1988","1458","4268","1901","4787","7599","6672","3579","3726","6670","1603","3332","7249","0984","6783","4456","0023","2678","0167","8626","6080","5716","5083","6135","8700","7890","8683","2089","0264","2123","0787","3056","2647","4645","8748","6936","6899","0031","4934","0221","9481","9959","1386","7695","2034","0466","0809","9166","6381","6937","0744","8059","8498","5772","8379","4448","5794","7423","2568","4671","6408","4335","1655","3662","1250","5262","7197","6831","8004","0575","8784","2920","0869","7157","0153","7255","1541","1247","5498","0566","6632","7640","1733","2546","5110","2852","8042","8175","0284","8589","8918","5755","2289","0812","4850","4650","9018","6649","5099","6532","9891","8675","1718","5442","6786","8915","3710","3833","2659","7040","3959","2505","7574","1199","3465","4557","7230","9161","5177","7815","4564","1470","8051","6287","2504","4025","8911","6158","6857","8948","7991","3670","3413","0423","7184","7921","1351","8908","1921","1685","5579","4641","0286","6410","2800","7018","1402","7410","3471","1312","9530","4581","5364","4820","8192","3088","4714","2255","2342","5042","8673","9788","2203","0879","2345","9712","2008","0652","0939","0720","2954","4482","2390","0807","4634","6266","5222","6898","7491","0294","1811","0667","8282","5754","1841","9518","9093","7904","4902","0068","5157","7823","8073","8801","8179","1402","9977","2332","9448","2251","8455","6157","1878","4183","3331","8047","1254","9639","2156","5780","7359","0260","9683","6842","1098","6495","2057","6583","0932","2577","1818","6042","8358","1833","5512","4529","0583","9955","9205","6055","3322","2232","5372","5835","2202","9696","1596","3424","3696","5695","1365","6432","0327","1565","8509","6936","3363","3007","3107","0410","6258","2492","0300","1255","1664","8666","6826","9961","5782","0140","5567","9596","1680","1892","5016","8804","4962","9318","4540","5044","0979","2004","4265","7689","0289","3434","6090","1375","3135","3935","5140","9255","3997","3482","8150","8164","0787"]
    # print('Before, deadends length = {0}'.format(len(deadends)))
    target = "8828"
    tStart = time.time() 
    print('expected = ?, actual = {0}, tElapsed = {1}'.format(sln1.openLock(deadends, target), (time.time() - tStart)))
    # print('After, deadends length = {0}'.format(len(deadends)))