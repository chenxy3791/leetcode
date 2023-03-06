"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical 
             digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.

Question: How about the case that the first digit is zero? Should return 0?
Answer:   According the feedback from leetcode grader, the leading zero should be ignored, instead of returning 0
Solution:
1. Trivial case handling
2. Search the first non-whitespace character a:
    if a is either '+' or '-':
        record the sign
    else:
        record as the highest significance numeric value
    Continue to extract the complete numeric sequence
3. Convert the numeric sequence into double number
4. Judge whether the {sign,number} is within the representation range of integer
    
"""

class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str) == 0:
            return 0
        if str.isspace():
            return 0

        k = 0
        while k < len(str):
            #print(k, str[k])
            if not str[k].isspace():
                break
            k = k + 1
                
        sign = 1        
        if str[k] is "+":
            sign = 1
            validStart = k+1
        elif str[k] is "-":
            sign = -1
            validStart = k+1
        else:
            validStart = k

        k = validStart
        numList = []
        while k < len(str):
            if str[k].isdigit():
                numList.append(int(str[k]))
                k = k + 1
            else:
                break

        print(numList)
        if len(numList) == 0:
            return 0
        #elif numList[0] == 0: # According the feedback from leetcode grader, the leading zero should be ignored, instead of returning 0
        #    return 0

        num = 0
        weight = 1
        # for j in range(len(numList)):
        #     num += (10**(len(numList)-j-1))*numList[j]
        for j in range(len(numList)):
            # num += (10**(len(numList)-j-1))*numList[j]
            num += weight * numList[len(numList)-j-1]
            weight *= 10
        
        if sign == 1 and num > (2**31-1):
            return (2**31-1)
        elif sign == -1 and num > (2**31):
            return -(2**31)
        else:
            return sign*num
    
if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    print(sln.myAtoi(""), sln.myAtoi("   "), )

    # Testcase1
    print('Testcase1...')
    s = "42"
    print(sln.myAtoi(s))

    # Testcase2
    print('Testcase2...')
    s = "-42"
    print(sln.myAtoi(s))

    # Testcase3
    print('Testcase3...')
    s = "4193 with words"
    print(sln.myAtoi(s))

    # Testcase4
    print('Testcase4...')
    s = "words and 987"
    print(sln.myAtoi(s))

    # Testcase5
    print('Testcase5...')
    s = "-91283472332"
    print(sln.myAtoi(s))

    # Testcase6
    print('Testcase6...')
    s = "  +9877654321"
    print(sln.myAtoi(s))

    # Testcase7
    print('Testcase7...')
    s = "  +abc"
    print(sln.myAtoi(s))

    # Testcase8
    print('Testcase8...')
    s = "  +00987"
    print(sln.myAtoi(s))    