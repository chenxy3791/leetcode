""" 
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 """
"""  
执行结果：
通过 显示详情
执行用时 : 36 ms , 在所有 Python3 提交中击败了 98.22% 的用户
内存消耗 : 13.6 MB, 在所有 Python3 提交中击败了 100.00% 的用户
 """
class Solution:
    #def findContinuousSequence(self, target: int) -> List[List[int]]:
    def findContinuousSequence(self, target: int):
        if target <= 1: # even number has no solution
            return []

        rslt = []
        k = 2
        while 1:            
            m = (2*target - k**2 + k)/(2*k)
            # print('k = {0}, m = {1}'.format(k, m))
            if m == int(m):
                rslt.append([x for x in range(int(m),k+int(m))])
            if m <= 1:
                break
            k = k+1
        rslt.reverse()
        return rslt

if __name__ == '__main__':    

    import time
    sln   = Solution()

    print('Testcase1...')    
    target = 9
    print('target = {0}: result = {1}'.format(target, sln.findContinuousSequence(target)))

    print('Testcase2...')    
    target = 15
    print('target = {0}: result = {1}'.format(target, sln.findContinuousSequence(target)))

    print('Testcase3...')    
    target = 1
    print('target = {0}: result = {1}'.format(target, sln.findContinuousSequence(target)))    

    print('Testcase4...')    
    target = 10
    print('target = {0}: result = {1}'.format(target, sln.findContinuousSequence(target)))    

    tStart = time.time()       
    print('Testcase5...')    
    target = 10**5
    print('target = {0}: result = {1}'.format(target, sln.findContinuousSequence(target)))        
    tElapsed = time.time() - tStart        
    print('tElapsed = {0}(sec)'.format(tElapsed))