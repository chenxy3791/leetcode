""" 
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""

import time

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        n_len = len(needle)
        h_len = len(haystack)

#        print(h_len, n_len, haystack, needle)

        h_ptr = 0
        while (h_len - h_ptr) >= n_len:
#            print('h_ptr = ', h_ptr)
            unmatch = 0
            for k in range(n_len):
                if haystack[h_ptr+k] != needle[k]:
                    unmatch = 1                    
#                    print('Unmatch found: ', h_ptr, k, haystack[h_ptr+k], needle[k] )
                    break
            
            if unmatch == 0:
                return h_ptr
            else:
                h_ptr = h_ptr + 1
        
        return -1 # Coming to here means failing to match

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    haystack = ''
    needle  = ''
    print(sln.strStr(haystack, needle))

    # Testcase1
    print('Testcase1...')
    haystack = ' '
    needle   = ''
    print(sln.strStr(haystack, needle))

    # Testcase2
    print('Testcase2...')
    haystack = 'Hello'
    needle   = 'lo'
    print(sln.strStr(haystack, needle))

    # Testcase3
    print('Testcase3...')
    haystack = "What's wrong with you?"
    needle   = 'you?'
    print(sln.strStr(haystack, needle))

    # Testcase4
    print('Testcase4...')
    haystack = "What's wrong with you?"
    needle   = 'ou? '
    print(sln.strStr(haystack, needle))