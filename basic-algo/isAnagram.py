"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        0. If their lengths are different, then return False         
        1. First convert both string into character list
        2. Check whether each element of s is in t:
        2.1 If yes, then remove it from tList
        2.2 If No, then return False immediately
        3. Return Ture, if passed step2.
        """
        sList = list(s)
        tList = list(t)

        if len(sList) != len(tList):
            return False

        for c in sList:
            if c in tList:
                tList.remove(c)
            else:
                return False
        
        return True

if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = "anagram"
    t = "nagaram"
    print(sln.isAnagram(s,t))

    # Testcase1
    print('Testcase1...')
    s = "rat"
    t = "car"
    print(sln.isAnagram(s,t))