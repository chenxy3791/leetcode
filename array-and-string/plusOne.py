""" 
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321..

"""

import time

class Solution:
    #def plusOne(self, digits: List[int]) -> List[int]:
    def plusOne(self, digits):
        if len(digits) == 0:
            print('Error: the input should be non-empty array!')
            return -1
        carry = 1 # Taken 1 as the initial carry, to simplify the code
        for k in range(len(digits)-1,-1,-1): # In descending order case, the final valid is (stop+1)!
            #print(k)
            tmp = digits[k] + carry

            if tmp < 10:
                digits[k] = tmp
                carry   = 0
            else:
                digits[k] = tmp - 10
                carry   = 1

        if carry == 1:
            digits.insert(0,carry)

        return digits

if __name__ == '__main__':

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    digits = []
    print(sln.plusOne(digits))

    # Testcase1
    print('Testcase1...')
    digits = [1,2,3]
    print(sln.plusOne(digits))

    # Testcase2
    print('Testcase2...')
    digits = [9]
    print(sln.plusOne(digits))

    # Testcase3
    print('Testcase3...')
    digits = [9, 9, 9, 9, 9]
    print(sln.plusOne(digits))

    # Testcase4
    print('Testcase4...')
    digits = [9, 9, 8, 9, 9]
    print(sln.plusOne(digits))


    # # Testcase4
    # print('Testcase3...')
    # digits = []
    # N = 100000
    # for k in range(N):
    #     digits.append(k)
    #     digits.append(k)
    # digits.append(N)
 
    # print(digits[0:10])
 
    # tStart = time.time()    
    # print(sln.singleNumber(digits))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')
