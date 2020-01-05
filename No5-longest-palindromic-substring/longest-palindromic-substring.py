class Solution:
    #def longestPalindrome(self, s: str) -> str:
    def longestPalindrome(self, s):
        max_len  = -1 # Initialized to a invalid value
        max_pos  = 0  
        max_type = 0  # -1: left-center; 0: center; 1: right-center
        
        sLen = len(s)
        if sLen == 0 or sLen == 1:
            return s
        
        for k in range(sLen):
            max_type_k = -2 # Initialized to a invalid value
            max_len_k  = -1 # Initialized to a invalid value
                        
            # search as left-center
            max_left_k = 0
            for l in range(min(k+1, sLen-k-1)):
                if s[k-l] == s[k+1+l]:
                    max_left_k = max_left_k + 2
                else:
                    break

            # In fact, the right-center is equivalent to left-center, hence, can be removed.
            ## # search as right-center
            ## max_right_k = 0
            ## for l in range(min(k, sLen-k)):
            ##     if s[k-l-1] == s[k+l]:
            ##         max_right_k = max_right_k + 2
            ##     else:
            ##         break       
                
            # search as center
            max_center_k = -1 # For center-type is 1, there will be at least one time hit.
            for l in range(min(k+1, sLen-k)):
                if s[k-l] == s[k+l]:
                    max_center_k = max_center_k + 2
                else:
                    break       

            # Find max among left/center/right
            if max_center_k >= max_left_k :
                max_len_k  = max_center_k
                max_type_k = 0
            else:
                max_len_k  = max_left_k
                max_type_k = -1                
                
            ## if max_len_k < max_right_k:
            ##     max_len_k  = max_right_k
            ##     max_type_k = 1                

            # Update the total 
            if max_len_k > max_len:
                max_type = max_type_k
                max_len  = max_len_k
                max_pos  = k
            
            # print(k, max_pos, max_len, max_type)
            
        # Judge the validity of the result
        if max_len <= 0 or max_pos < 0 or max_type < -1:
            print('Invalid output: something wrong in the program')
            return 'Wrong result! Please check the program'
        
        # Recovery the longest palindromic substring        
        # print(max_pos, max_len, max_type)
        if max_type == 0:
            substring = s[max_pos-int((max_len-1)/2) : max_pos+int((max_len-1)/2)+1]
        elif  max_type == -1:    
            substring = s[max_pos-int(max_len/2)+1 : max_pos+int(max_len/2)+1]
        else:
            substring = s[max_pos-int(max_len/2) : max_pos+int(max_len/2)]
        
        return substring

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    s = ""
    print(s + ':  '+sln.longestPalindrome(s))

    # Testcase1
    print('Testcase1...')
    s = "babad"
    print(s + ':  '+sln.longestPalindrome(s))
    
    # Testcase2
    print('Testcase2...')    
    s = "cbbd"
    print(s + ':  '+sln.longestPalindrome(s))
    
    # Testcase3
    print('Testcase3...')    
    s = "dcqcbababd"
    print(s + ':  '+sln.longestPalindrome(s))
    
    # Testcase4
    print('Testcase4...')    
    s = "dcd08qcbababcq80"
    print(s + ':  '+sln.longestPalindrome(s))    

    # Testcase5
    print('Testcase5...')    
    s = "abcdbbd"
    print(s + ':  '+sln.longestPalindrome(s))
    
    # Testcase6
    print('Testcase5...')    
    s = "cdbbdcasq"
    print(s + ':  '+sln.longestPalindrome(s))