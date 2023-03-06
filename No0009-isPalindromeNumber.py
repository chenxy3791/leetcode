"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >=0 and x < 10:
            return True

        xStr = str(x)
        for k in range(int(len(xStr)/2)):
            if xStr[k] != xStr[-k-1]:
                return False

        return True
                        
if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    x = 121
    print(sln.isPalindrome(x))

    print('Testcase2...')
    x = -10
    print(sln.isPalindrome(x))

    print('Testcase3...')
    x = 10
    print(sln.isPalindrome(x))

    print('Testcase4...')
    x = 1
    print(sln.isPalindrome(x))

    print('Testcase5...')
    x = 12345654321712345654321
    print(sln.isPalindrome(x))
