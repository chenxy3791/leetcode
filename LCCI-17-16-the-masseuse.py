""" 
程序员面试金典(第6版)
面试题 17.16. 按摩师
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，
因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），
返回总的分钟数。
注意：本题相对原题稍作改动

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
"""
解题思路：
对于每个预约请求，有两种状态，接受 or 拒绝
贪婪算法不一定能得到最优解
这个应该是属于0/1背包问题--但是好像比0/1背包问题简单。
以第一个预约为例
take it: total = nums[0] + f(2)
reject it: total = f(1)
f(0) = max{nums[0] + f(2), f(1)}

"""
class Solution:
    #def massage(self, nums: List[int]) -> int:
    def massage(self, nums) -> int:        
        cache = dict()
        def dp(k):
            if k == len(nums):
                return 0
            if k == len(nums)-1:
                return nums[k]
            
            if k in cache:
                return cache[k]

            tmp = max(nums[k]+dp(k+2), dp(k+1))
            cache[k] = tmp
            return tmp
        
        return dp(0)

if __name__ == '__main__':

    import time
    import numpy as np

    sln   = Solution()        

    print('\nTestcase0 ...')    
    print('sln.massage([])  = {0}'.format(sln.massage([])))
    print('sln.massage([3]) = {0}'.format(sln.massage([3])))

    print('\nTestcase1 ...')
    nums = [1,2,3,1]
    print(sln.massage(nums))

    print('\nTestcase2 ...')
    nums = [2,7,9,3,1]
    print(sln.massage(nums))

    print('\nTestcase3 ...')
    nums = [2,1,4,5,3,1,1,3]
    print(sln.massage(nums))

    print('\nTestcase4 ...')    
    nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    tStart= time.time()
    print(sln.massage(nums))    
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        