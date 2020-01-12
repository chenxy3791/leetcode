""" 
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""

import time

class Solution:                           
    def reverseWords(self, s: str) -> str:
        # step1: transfer string to list, because string is immutable
        sList = list(s)

        # Find each word and reverse it.
        wordStart = -1        

        # Convert to list of word, removing the extra spaces
        for k in range(len(sList)):
            if sList[k] != ' ' and wordStart == -1: # Find the start of one word 
                wordStart = k
            if sList[k] == ' ' and wordStart >= 0:  # Find the end of one word
                sList[wordStart:k] = reversed(sList[wordStart:k])
                wordStart = -1
        if wordStart >= 0:
            sList[wordStart:] = reversed(sList[wordStart:])
        #print(sList)

        # step4: convert list back to string
        sNew = ''.join(sList)

        return sNew

if __name__ == '__main__':

    sln   = Solution()

    #Testcase0
    print('\nTestcase0...')
    s = "Let's take LeetCode contest"
    print(s, '--> ', sln.reverseWords(s))
