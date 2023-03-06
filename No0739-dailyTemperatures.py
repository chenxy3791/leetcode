""" 
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 """
class Solution:
    """ 
    执行结果：通过 显示详情
    执行用时 :556 ms, 在所有 Python3 提交中击败了56.94%的用户
    内存消耗 :17.7 MB, 在所有 Python3 提交中击败了5.37%的用户
     """
    #def dailyTemperatures(self, T: List[int]) -> List[int]:                
    def dailyTemperatures(self, T):                
        if len(T) == 0:
            return []
        if len(T) == 1:
            return [0]

        stack = []
        b     = len(T) * [0]
        
        for k in range(len(T)):
            while len(stack) > 0 and T[k] > stack[-1][1]:
                x = stack.pop()
                b[x[0]] = k - x[0]
            stack.append((k,T[k]))    
        return b

if __name__ == '__main__':    

    import time
    import numpy as np

    sln   = Solution()

    print('Testcase1...')    
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sln.dailyTemperatures(T))

    print('Testcase2...')    
    tStart = time.time()        
    a = np.random.randint(0,1000,[1000000,])    
    T = a.tolist()    
    rslt = sln.dailyTemperatures(T)
    #print(sln.dailyTemperatures(T))
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))
