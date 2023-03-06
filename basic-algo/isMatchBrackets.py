""" 
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
 """
class Solution:    
    def isMatch(self, c1:str, c2:str):
        #print(c1,c2)
        if (c1 == '(' and c2 == ')') or (c1 == '[' and c2 == ']') or (c1 == '{' and c2 == '}'):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        charLst = []
        for k in range(len(s)):
            if k == 0:
                charLst.append(s[k])                
            else:
                if len(charLst) > 0:
                    if self.isMatch(charLst[-1], s[k]):
                        charLst.pop()
                    else:
                        charLst.append(s[k])
                else:
                    charLst.append(s[k])
        #print(charLst)
        if len(charLst) == 0:
            return True
        else:
            return False