"""
On the first row, we write a 0. Now in every subsequent row, we look at 
the previous row and replace each occurrence of 0 with 01, and each 
occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. 
(The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1: return 0

        return bin(K - 1).count('1') % 2

        """     
        kBin = bin(K-1) # Because the input K is 1-indexed
        # Count the 1's in kBin        
        l = 0
        countOne = 0
        while l < len(kBin):
            if kBin[l] == '1':
                countOne += 1
            l += 1
        if countOne % 2 == 1:
            return 1
        else:
            return 0 
        """
            
if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    N = 1
    K = 1 
    print('Expected = 0; result = {0}'.format(sln.kthGrammar(N,K)))        

    print('Testcase2...')
    N = 2
    K = 1 
    print('Expected = 0; result = {0}'.format(sln.kthGrammar(N,K)))            

    print('Testcase3...')
    N = 2
    K = 2 
    print('Expected = 1; result = {0}'.format(sln.kthGrammar(N,K)))                

    print('Testcase4...')
    N = 4
    K = 5 
    print('Expected = 1; result = {0}'.format(sln.kthGrammar(N,K)))                    