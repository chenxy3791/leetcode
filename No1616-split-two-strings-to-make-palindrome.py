# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 08:15:15 2023

@author: chenxy
1616. 分割两个字符串得到回文串
给你两个字符串 a 和 b ，它们长度相同。请你选择一个下标，将两个字符串都在 相同的下标 分割开。
由 a 可以得到两个字符串： aprefix 和 asuffix ，满足 a = aprefix + asuffix ，
同理，由 b 可以得到两个字符串 bprefix 和 bsuffix ，满足 b = bprefix + bsuffix 。
请你判断 aprefix + bsuffix 或者 bprefix + asuffix 能否构成回文串。

当你将一个字符串 s 分割成 sprefix 和 ssuffix 时， ssuffix 或者 sprefix 可以为空。
比方说， s = "abc" 那么 "" + "abc" ， "a" + "bc" ， "ab" + "c" 和 "abc" + "" 都是合法分割。

如果 能构成回文字符串 ，那么请返回 true，否则返回 false 。

注意， x + y 表示连接字符串 x 和 y 。

示例 1：

输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。

示例 2：
输入：a = "abdef", b = "fecab"
输出：true

示例 3：
输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
 
提示：
1 <= a.length, b.length <= 10**5
a.length == b.length
a 和 b 都只包含小写英文字母
"""

class Solution:
    # def checkPalindromeFormation(self, a: str, b: str) -> bool:
    #     '''
    #     Time-Out...
    #     '''
    #     def isPalindrome(s):
    #         return s == s[::-1]
    #     if len(a)==1: return True
    #     # print(len(a))
    #     isOddLen = len(a)%2
    #     if isOddLen:
    #         middle = len(a)//2
    #         for k in range(middle,-1,-1):
    #             # print(k,a[k:2*middle-k+1],b[k:2*middle-k+1])
    #             if not(isPalindrome(a[k:2*middle-k+1]) or isPalindrome(b[k:2*middle-k+1])):
    #                 return False
    #             elif isPalindrome(a[k:2*middle-k+1]):
    #                 if isPalindrome(a[:k]+b[2*middle-k+1:]) or isPalindrome(b[:k]+a[2*middle-k+1:]):
    #                     return True
    #             elif isPalindrome(b[k:2*middle-k+1]):
    #                 if isPalindrome(b[:k]+a[2*middle-k+1:]) or isPalindrome(a[:k]+b[2*middle-k+1:]):
    #                     return True
    #         return False
    #     else:
    #         middle = len(a)//2-1
    #         for k in range(middle+1,-1,-1):
    #             # print(k,a[k:2*middle-k+2],b[k:2*middle-k+2],a[:k]+b[2*middle-k+2:],b[:k]+a[2*middle-k+2:])
    #             if not(isPalindrome(a[k:2*middle-k+2]) or isPalindrome(b[k:2*middle-k+2])):
    #                    return False
    #             elif isPalindrome(a[k:2*middle-k+2]):
    #                 if isPalindrome(a[:k]+b[2*middle-k+2:]) or isPalindrome(b[:k]+a[2*middle-k+2:]):
    #                     return True
    #             elif isPalindrome(b[k:2*middle-k+2]):
    #                 if isPalindrome(b[:k]+a[2*middle-k+2:]) or isPalindrome(a[:k]+b[2*middle-k+2:]):
    #                     return True
    #         return False

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkConcatenation(a, b) or self.checkConcatenation(b, a)
    
    def checkConcatenation(self, a: str, b: str) -> bool:
        n = len(a)
        left, right = 0, n-1
        while left < right and a[left] == b[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return self.checkSelfPalindrome(a, left, right) or self.checkSelfPalindrome(b, left, right)

    def checkSelfPalindrome(self, a: str, left: int, right: int) -> bool:
        while left < right and a[left] == a[right]:
            left += 1
            right -= 1
        return left >= right

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/split-two-strings-to-make-palindrome/solution/fen-ge-liang-ge-zi-fu-chuan-de-dao-hui-w-bjzk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == '__main__':

    sln  = Solution()                
    
    a = "x"
    b = "y"
    print(sln.checkPalindromeFormation(a,b))        
    
    a = "abdef"
    b = "fecab"
    print(sln.checkPalindromeFormation(a,b))        
    
    a = "ulacfd"; b = "jizalu"
    print(sln.checkPalindromeFormation(a,b))        
    
    a = "pvhmupgqeltozftlmfjjde"
    b = "yjgpzbezspnnpszebzmhvp"
    print(sln.checkPalindromeFormation(a,b))        