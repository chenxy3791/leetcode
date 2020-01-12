""" 
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.

Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""

import time

class Solution:
    def reverseWords(self, s: str) -> str:
        wordStart = -1        
        wordLst = []

        # Convert to list of word, removing the extra spaces
        for k in range(len(s)):
            if s[k] != ' ' and wordStart == -1: # Find the start of one word 
                wordStart = k
            if s[k] == ' ' and wordStart >= 0:  # Find the end of one word
                wordLst.append(s[wordStart:k])
                wordStart = -1
        if wordStart >= 0:
            wordLst.append(s[wordStart:])

        #print(wordLst)

        # Reverse the list of word
        wordLst.reverse()
        #print(wordLst)

        # Convert back to string
        return " ".join(wordLst)
                        
    # Misunderstanding the question. Just reverse the order of word, not character within one word
    def reverseWords_1(self, s: str) -> str:
        # step1: transfer string to list, because string is immutable
        sList = list(s)

        # step2: remove heading and tailing spaces and also extra spaces between words
        wPtr = 0
        rPtr = 0
        for rPtr in range(len(sList)):
            if sList[rPtr] == ' ' and ( wPtr == 0 or ((wPtr > 0) and (s[wPtr-1] == ' ')) ):
                rPtr    = rPtr + 1
            else:
                sList[wPtr] = sList[rPtr]
                wPtr    = wPtr + 1
                rPtr    = rPtr + 1
        print(sList)

        # step3: reverse
        fPtr = 0
        bPtr = wPtr-1
        while fPtr < bPtr:
            tmp     = sList[fPtr]
            sList[fPtr] = sList[bPtr]
            sList[bPtr] = tmp
            fPtr    = fPtr + 1
            bPtr    = bPtr - 1
    
        # step4: convert list back to string
        sNew = ''.join(sList[0:wPtr])

        return sNew

if __name__ == '__main__':

    sln   = Solution()

    #Testcase0
    print('\nTestcase0...')
    s = []
    print(s, '--> ', sln.reverseWords(s))

    # Testcase1
    print('\nTestcase1...')
    s = "the sky is blue"
    print(s, '--> ', sln.reverseWords(s))

    # Testcase2
    print('\nTestcase2...')
    s = "  hello world!  "
    print(s, '--> ', sln.reverseWords(s))

    # Testcase3
    print('\nTestcase3...')
    s = "a good   example"
    print(s, '--> ', sln.reverseWords(s))

