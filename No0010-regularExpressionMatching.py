"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isMatchNG(self, s: str, p: str) -> bool:    
        """ 
        (1) maximum recursion depth exceeded in comparison
        (2) there is logical hole -- some cases uncovered.
        Should change the way-of-thinking concretely.
        """
        if len(p) == 0:
            return len(s) == 0
        elif len(p) == 1:
            if len(s) == 0:
                return False
            else:
                return ((s[0] == p[0]) or (p[0] == '.')) and (len(s) == 1)
        else: #len(p) >= 2
            if p[1] != '*':
                if len(s) == 0:
                    return False
                else:
                    firstMatch = (s[0] == p[0]) or (p[0] == '.')
                return firstMatch and self.isMatch(s[1:],p[1:])
            else: # p[1] == '*'
                if p[0] == '.':
                    return self.isMatch(s,p[2:]) or self.isMatch(s[1:],p)
                else: # p[0] is normal char
                    if len(s) == 0:
                        return False
                    else:
                        firstMatch = (s[0] == p[0]) or (p[0] == '.')

                    if firstMatch:
                        # Skip the following char same as s[0]
                        sPtr = 1
                        while sPtr < len(s):
                            if s[sPtr] == s[0]:
                                sPtr += 1
                            else:
                                break
                        # Skip the following char same as p[0]
                        pPtr = 2
                        while pPtr < len(p):
                            if p[pPtr] == p[0]:
                                pPtr += 1
                            else:
                                break
                        return self.isMatch(s[sPtr:], p[pPtr:])
                    else:
                        return False

    def isMatch(self, s: str, p: str) -> bool:
        memo = dict()
        def dp(i,j):
            #print(i,j)
            if (i,j) in memo:
                return memo[(i,j)]
            if j == len(p) : 
                return i == len(s)

            first = i < len(s) and p[j] in [s[i],'.']
            if j <= len(p)-2 and p[j+1] == '*':
                ans = dp(i,j+2) or first and dp(i+1,j)
            else:
                ans = first and dp(i+1,j+1)
            memo[(i,j)] = ans
            return ans
        return dp(0,0)

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    s = "aa"
    p = "a"
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase2...')
    s = "aa"
    p = "a*"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase3...')
    s = "ab"
    p = ".*"
    print('s = {0}, p = {1}, Expected: True result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase3-1...')
    s = "abcdefgn"
    p = ".*"
    print('s = {0}, p = {1}, Expected: True result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase3-2...')
    s = "abcdefgn"
    p = ".*gn"
    print('s = {0}, p = {1}, Expected: True result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase3-3...')
    s = "abcdefgn"
    p = ".*g"
    print('s = {0}, p = {1}, Expected: False result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase4...')
    s = "aab"
    p = "c*a*b"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase5...')
    s = "mississippi"
    p = "mis*is*p*."
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase6...')
    s = ""
    p = "."
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))  

    print('Testcase7...')
    s = ""
    p = "c*"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))  

    print('Testcase8...')
    s = ""
    p = ".*"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))      

    print('Testcase9...')
    s = "a"
    p = ""
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase10...')
    s = "aaaaa"
    p = ".*"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))              

    print('Testcase11...')
    s = "aaa"
    p = "a*a"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase11-1...')
    s = "aaaa"
    p = "a*a*a"
    print('s = {0}, p = {1}, Expected: True; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase12...')
    s = "aa"
    p = "a**"
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase13...')
    s = "abcdefg"
    p = "abcdefh"
    print('s = {0}, p = {1}, Expected: False; result = {2}'.format(s, p, sln.isMatch(s,p)))

