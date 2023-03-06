"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    #def firstMissingPositive(self, nums: List[int]) -> int:
    def firstMissingPositive(self, nums) -> int:
        if len(nums) == 0:
            return 1
        nums.sort()
        k = 0
        posFlag = False
        posCnt  = 0
        while k < len(nums):
            if posFlag == False:
                if nums[k] > 0:
                    posCnt += 1
                    if nums[k] != 1:
                        return 1
                    else:
                        posFlag = True
                        k += 1
                else:
                    k += 1
            else:
                if nums[k] == posCnt:
                    k += 1
                elif nums[k] == posCnt + 1:   
                    posCnt += 1
                    k += 1
                else:
                    return posCnt+1
        return posCnt + 1
            
if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    nums = [1,2,0] 
    print('Expected = 3; result = {0}'.format(sln.firstMissingPositive(nums)))

    nums = [] 
    print('Expected = 1; result = {0}'.format(sln.firstMissingPositive(nums)))

    nums = [1] 
    print('Expected = 2; result = {0}'.format(sln.firstMissingPositive(nums)))

    nums = [0,2,2,1,1]
    print('Expected = 3; result = {0}'.format(sln.firstMissingPositive(nums)))
    
    print('Testcase2...')
    nums = [3,4,-1,1]
    print('Expected = 2; result = {0}'.format(sln.firstMissingPositive(nums)))

    print('Testcase3...')
    nums = [7,8,9,11,12]
    print('Expected = 1; result = {0}'.format(sln.firstMissingPositive(nums)))

    print('Testcase4...')
    import random
    import time
    nums = []
    # for i in range(5000):
    #     n = random.randint(1,1000)
    #     nums.append(n)
    nums = [n for n in range(10)]
    print(nums)         
    tStart = time.time()        
    print('Expected = ???; result = {0}'.format(sln.firstMissingPositive(nums)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')