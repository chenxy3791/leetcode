"""
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.


Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 
Constraints: 1 <= num <= 3999
"""
import sys
# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, '../utilfunc')

# import time
# from TreeNode import TreeNode 
# from TreeNode import BinaryTree
# from TreeNode import binTree2Lst

class Solution:
    def intToRoman(self, num: int) -> str:
        ge  = num % 10
        shi = int(num/10) % 10
        bai = int(num/100) % 10
        qian= int(num/1000)

        #print(ge, shi, bai, qian)

        outStr = []
        for k in range(1,qian+1):
            outStr.append('M')

        if bai == 9:
            outStr.append('CM')
        elif bai >= 5:
            outStr.append('D')
            for k in range(1,bai-5+1):
                outStr.append('C')
        elif bai == 4:
            outStr.append('CD')
        else:
            for k in range(1,bai+1):
                outStr.append('C')
        
        if shi == 9:
            outStr.append('XC')
        elif shi >= 5:
            outStr.append('L')
            for k in range(1,shi-5+1):
                outStr.append('X')
        elif shi == 4:
            outStr.append('XL')
        else:
            for k in range(1,shi+1):
                outStr.append('X')

        if ge == 9:
            outStr.append('IX')
        elif ge >= 5:
            outStr.append('V')
            for k in range(1,ge-5+1):
                outStr.append('I')
        elif ge == 4:
            outStr.append('IV')
        else:
            for k in range(1,ge+1):
                outStr.append('I')
        
        return ''.join(outStr)

if __name__ == '__main__':    

    sln   = Solution()

    print('Testcase1...')
    for num in range(1,20):
        print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))

    print('Testcase2...')
    num = 58
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))

    print('Testcase3...')
    num = 1994
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))

    print('Testcase4...')
    num = 3999
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))    

    print('Testcase5...')
    num = 100
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))

    num = 10
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))

    num = 1000
    print('num = {0}, result = {1}'.format(num,sln.intToRoman(num)))
