"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/third-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def thirdMax(self, nums) -> int:        
        nums.sort(reverse = True)
        cnt = 1
        k   = 1
        cur = nums[0]
        while k < len(nums):
            if nums[k] == cur:
                k += 1
            else:
                cur  = nums[k]
                cnt += 1
                k   += 1
            if cnt == 3:
                break
        if cnt == 3:
            return cur
        else:
            return nums[0]

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    nums = [1, 2]
    print(sln.thirdMax(nums))

    print('Testcase2...')
    nums = [3, 2, 1]
    print(sln.thirdMax(nums))

    print('Testcase3...')
    nums = [2, 2, 3, 1]
    print(sln.thirdMax(nums))
