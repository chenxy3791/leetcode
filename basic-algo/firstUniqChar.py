"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

firstUniqChar_NaivelyNG(): Naively NG solution.
    For one character, there maybe no another identical one behind it, but there maybe another identical one before it.
    This mehtod works for the case of searching the first duplicate character, but not for the first unique.
    The non-unique character identified in the search should be marked to avoid the abovementioned mistake.
"""

class Solution:
    def firstUniqChar_NaivelyNG(self, s: str) -> int:
        sLen = len(s)
        # Trival case
        if sLen == 0:
            return -1 
        if sLen == 1:
            return 0
        
        # Mormal case        
        for k in range(len(s)):
            isUnique = True
            for j in range(k+1,len(s)):
                if s[k] == s[j]:
                    isUnique = False
                    break
            
            if isUnique:
                return k
        return -1

    def firstUniqChar(self, s: str) -> int:
        sLen = len(s)
        # Trival case
        if sLen == 0:
            return -1 
        if sLen == 1:
            return 0

        # Mormal case        
        nonunique = [False] * sLen
        for k in range(len(s)):
            # Avoid invalid searched for already-marker non-unique characters
            if nonunique[k] is True:
                continue
            
            for j in range(k+1,len(s)):
                if s[k] == s[j]:
                    nonunique[k] = True
                    nonunique[j] = True         

            if nonunique[k] is False:
                return k
        return -1


if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = "leetcode"
    print(sln.firstUniqChar(s))

    # Testcase1
    print('Testcase1...')
    s = "loveleetcode"
    print(sln.firstUniqChar(s))

    # Testcase2
    print('Testcase2...')
    s = "loveleetcodeloveleetcode"
    print(sln.firstUniqChar(s))

    # Testcase3
    print('Testcase3...')
    s = "o"
    print(sln.firstUniqChar(s))
