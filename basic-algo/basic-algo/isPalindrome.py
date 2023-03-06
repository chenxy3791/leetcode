"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 
        Using double pointer technique.
        Search from two direction, skip the non-alphanumeric characters and match each pair.
        """
        if len(s) == 0 or len(s) == 1:
            return True

        fPtr = 0
        bPtr = len(s) - 1

        while fPtr < bPtr:
            #print('fPtr = {0}, bPtr = {1}, s[fPtr] = {2}, s[bPtr] = {3}'.format(fPtr,bPtr,s[fPtr],s[bPtr]))
            if s[fPtr].lower() == s[bPtr].lower():
                fPtr += 1
                bPtr -= 1
                continue
            
            # Two characters unmatch
            if not s[fPtr].isalnum():
                fPtr += 1
            elif not s[bPtr].isalnum():
                bPtr -= 1 
            else:
                return False        
        return True
                        
if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = ""    
    print(sln.isPalindrome(s))

    s = "a"
    print(sln.isPalindrome(s))


    # Testcase1
    print('Testcase1...')
    s = "A man, a plan, a canal: Panama"    
    print(sln.isPalindrome(s))

    # Testcase2
    print('Testcase2...')
    s = "race a car"    
    print(sln.isPalindrome(s))