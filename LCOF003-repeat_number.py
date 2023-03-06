"""
剑指 Offer 03. 数组中重复的数字
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
 
限制：

2 <= n <= 100000

2021-03-16
执行结果：通过
显示详情
执行用时：48 ms, 在所有 Python3 提交中击败了80.64%的用户
内存消耗：23.4 MB, 在所有 Python3 提交中击败了49.38%的用户

"""

class Solution:
    def findRepeatNumber(self, nums) -> int:
        if len(nums) <= 1:
            return []

        nums.sort()
        for k in range(len(nums)-1):
            if nums[k] == nums[k+1]:
                return nums[k]

                
if __name__ == '__main__':        
    #import time
    sln = Solution()

    a = [2, 3, 1, 0, 2, 5, 3]
    print(sln.findRepeatNumber(a))

    a = [2]
    print(sln.findRepeatNumber(a))
