"""
115. 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)
rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)
babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
 
提示：
0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distinct-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def numDistinct_wo_memoization(self, s: str, t: str) -> int:
        #2021-03-17
        """
            Time-limit violation with the following input:
            "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
            "bddabdcae"
        """
        #print('s = ',s,'\t', 't = ',t)

        # Base case, or special case
        if len(s) == 0 or len(t) == 0:
            return 0
        if len(s) == 1 and len(t) == 1:
            if s == t:
                return 1
            else:
                return 0
        if len(s) < len(t):
            return 0

        if len(s) > 0 and len(s) == len(t) and s == t:
            return 1

        # Normal case
        if s[0] == t[0]:
            if len(t) == 1:
                return self.numDistinct_wo_memoization(s[1:],t) + 1
            else:
                return self.numDistinct_wo_memoization(s[1:],t) + self.numDistinct_wo_memoization(s[1:],t[1:])
        else:
            return self.numDistinct_wo_memoization(s[1:],t)

    def numDistinct(self, s: str, t: str) -> int:
        #2021-03-17
        """
        执行结果：        通过
        显示详情
        执行用时：        68 ms        , 在所有 Python3 提交中击败了       10.90%        的用户
        内存消耗：        20.4 MB      , 在所有 Python3 提交中击败了        5.16%        的用户        
        """
        #print('s = ',s,'\t', 't = ',t)

        cache = dict()

        def dp_memoization(i,j):
            if (i,j) in cache:
                return cache[(i,j)]

            s0 = s[i:]
            t0 = t[j:]
            # Base case, or special case
            if len(s0) == 0 or len(t0) == 0:
                return 0
            if len(s0) == 1 and len(t0) == 1:
                if s0 == t0:
                    return 1
                else:
                    return 0
            if len(s0) < len(t0):
                cache[(i,j)] = 0
                return 0

            if len(s) > 0 and len(s0) == len(t0) and s0 == t0:
                cache[(i,j)] = 1
                return 1

            # Normal case
            if s0[0] == t0[0]:
                if len(t0) == 1:
                    ans = dp_memoization(i+1,j) + 1
                else:
                    ans =  dp_memoization(i+1,j) + dp_memoization(i+1,j+1)
            else:
                ans =  dp_memoization(i+1,j)
            cache[(i,j)] = ans
            return ans

        return dp_memoization(0,0)

if __name__ == '__main__':        
    import time
    sln = Solution()

    s = "r"
    t = "r"
    print(sln.numDistinct(s,t))

    s = "t"
    t = "r"
    print(sln.numDistinct(s,t))

    s = "the"
    t = ""
    print(sln.numDistinct(s,t))

    s = ""
    t = "the"
    print(sln.numDistinct(s,t))


    s = "rabbbit"
    t = "rabbit"
    print(sln.numDistinct(s,t))

    s = "babgbag"
    t = "bag"
    print(sln.numDistinct(s,t))

    # tStart = time.time()        
    # print('Testcase...')    
    # s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    # t = "bddabdcae"
    # print(s, t)
    # print('ans = ', sln.numDistinct_wo_memoization(s,t))
    # tElapsed = time.time() - tStart        
    # print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    print('Testcase...')    
    s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    t = "bddabdcae"
    print(s, t)
    print('ans = ', sln.numDistinct(s,t))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')