"""
Given n non-negative integers a1, a2, ..., an , where each represents 
a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container 
contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution1:
Area = Max(min(height[i], height[j]) * (j-i)) {0 <= i < j < height,size()}
动态规划.
基本的表达式: area = min(height[i], height[j]) * (j - i) 使用两个指针，
值小的指针向内移动. 
原因是：
面积取决于指针的距离与值小的值乘积，如果值大的值向内移动，距离一定减小，而求高则
一定不会大于值小的值，因此面积一定减小。
反过来，值小的指针向内移动的话，距离也一定在减小，面积有可能增大也有可能减小。
在遍历过程中记录出现过的最大的值即可。
因为始终都是值小的指针向内移动的话，最多移动N次，复杂度即为O(N).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    #def maxArea(self, height: List[int]) -> int:
    def maxAreaNaive(self, height) -> int:
        if len(height) == 2:
            return min(height)
        aMax = 0;
        for k in range(len(height)-1):
            for j in range(k+1,len(height)):
                area = min(height[k],height[j]) * (j-k)
                if area > aMax:
                    aMax = area
        return aMax

    def maxArea(self, height) -> int:
        """ 
        执行结果：通过
        执行用时 :164 ms, 在所有 Python3 提交中击败了32.82%的用户
        内存消耗 :15 MB,  在所有 Python3 提交中击败了50.79%的用户        
         """
        fptr = 0
        bptr = len(height) - 1
        aMax = 0
        while bptr > fptr:
            #print(fptr, bptr)
            if height[bptr] < height[fptr]:
                area = (bptr - fptr) * height[bptr]
                bptr -= 1
            else:
                area = (bptr - fptr) * height[fptr]
                fptr += 1                        
            if area > aMax:
                aMax = area            
        return aMax                

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    height = [1,8,6,2,5,4,8,3,7]    
    print('Expected = 49; result = {0}'.format(sln.maxArea(height)))

    print('Testcase2...')
    import random
    import time
    height = []
    for i in range(5000):
        n = random.randint(1,1000)
        height.append(n)
    print(height[:10])         
    tStart = time.time()        
    print('Expected = ???; result = {0}'.format(sln.maxArea(height)))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')