"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
You can do so recursively, in other words from the previous member read off the digits, 
counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.
Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can 
be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", 
so the answer is the concatenation of "12" and "11" which is "1211".
    
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        #print("countAndSay({0}) ... ".format(n))
        assert(n > 0)

        if n == 1:
            return "1"
        
        strPrev = self.countAndSay((n-1))
        #print(strPrev)
        strCur = []

        curChar = strPrev[0]
        curCnt  = 1        
        if len(strPrev) == 1:
            strCur.append(str(curCnt))
            strCur.append(curChar)
            return "".join(strCur)

        for k in range(1,len(strPrev)):
            if strPrev[k] == curChar:
                curCnt += 1
            else:
                # Completion of one group
                strCur.append(str(curCnt))
                strCur.append(curChar)
                # Start of a new group
                curChar = strPrev[k]
                curCnt  = 1             

        # Handling of the final group
        strCur.append(str(curCnt))
        strCur.append(curChar)        

        return "".join(strCur)
    
if __name__ == '__main__':    

    sln   = Solution()

    # Testcase0
    print('Testcase0...')
    for k in range(1,10):
        print("sln.countAndSay({0}) is {1}".format(k, sln.countAndSay(k)))

    