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
    def isMatch(self, s: str, p: str) -> bool:
        if s=="":
            if p == "":
                return True
            elif len(p) == 2 and p[1] == '*':
                return True
            else:
                return False
        if p=="":
            if s == "":
                return True
            else:
                return False
        if p =='.*':
            return True

        kp = 0
        ks = 0
        while kp < len(p) and ks < len(s):
            #print('kp = {0}, ks = {1}'.format(kp,ks))
            if p[kp].isalpha() == True:
                if (kp < len(p) - 1) and (p[kp+1] == '*'):
                    while ks < len(s):
                        if s[ks] != p[kp]:
                            break
                        ks += 1                
                    kp += 2
                else:
                    if (s[ks] == p[kp]):
                        ks += 1
                        kp += 1                        
            elif p[kp] == '.':
                if (kp < len(p) - 1) and (p[kp+1] == '*'):
                    tmp = s[ks]
                    ks  += 1
                    while ks < len(s):
                        if s[ks] != tmp:
                            break
                        ks += 1                
                    kp += 2
                else:                    
                    ks += 1
                    kp += 1                                            
            elif p[kp] == '*':
                print('isMatch: Unexpected, p[kp] == '*'. Please check the input string, and the program logic!')
                return False
            else:
                print('isMatch: Unexpected, p[kp] == {0}. Please check the input string, and the program logic!'.format(p[kp]))
                return False
        if ks == len(s) and kp == len(p):
            return True
        else:
            return False

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    s = "aa"
    p = "a"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase2...')
    s = "aa"
    p = "a*"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase3...')
    s = "ab"
    p = ".*"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase4...')
    s = "aab"
    p = "c*a*b"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase5...')
    s = "mississippi"
    p = "mis*is*p*."
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase6...')
    s = ""
    p = "."
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))  

    print('Testcase7...')
    s = ""
    p = "c*"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))  

    print('Testcase8...')
    s = ""
    p = ".*"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))      

    print('Testcase9...')
    s = "a"
    p = ""
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase10...')
    s = "aaaaa"
    p = ".*"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))              

    print('Testcase11...')
    s = "aaa"
    p = "a*a"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))

    print('Testcase12...')
    s = "aa"
    p = "a**"
    print('s = {0}, p = {1}, result = {2}'.format(s, p, sln.isMatch(s,p)))
