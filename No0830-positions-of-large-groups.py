"""
830. 较大分组的位置
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。

找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

 

示例 1：

输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
示例 2：

输入：s = "abc"
输出：[]
解释："a","b" 和 "c" 均不是符合要求的较大分组。
示例 3：

输入：s = "abcdddeeeeaabbbcd"
输出：[[3,5],[6,9],[12,14]]
解释：较大分组为 "ddd", "eeee" 和 "bbb"
示例 4：

输入：s = "aba"
输出：[]
 
提示：

1 <= s.length <= 1000
s 仅含小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

2021-03-13 
执行用时：36 ms, 在所有 Python3 提交中击败了94.00%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了19.25%的用户

"""

class Solution:

    def positions(self, s: str):
        slen = len(s)
        print('s = ', s)
        if slen < 3:
            return []

        rsltList = []
        curChar  = s[0]
        cnt      = 1
        start    = 0

        for k in range(1, slen - 1): # Leave the final character for extra processing
            print('k = {0}, curChar = {1}, cnt = {2}'.format(k,curChar,cnt))
            if s[k] == curChar:   
                cnt = cnt + 1
            else:                
                if cnt >= 3:
                    end = k - 1
                    rsltList.append([start, end])

                # Initialization for the next group, regardless of whether cnt>=3 or not.
                curChar = s[k]
                start   = k
                cnt     = 1                

        # Extra handling for the final character.
        if s[-1] == curChar:   
            cnt = cnt + 1
            end = slen - 1
        else:
            end = slen - 2

        if cnt >= 3:
            rsltList.append([start, end])

        return rsltList
                    
if __name__ == '__main__':        
    #import time
    sln = Solution()
    
    s = 'abbba'
    print(sln.positions(s))
    
    s = 'aaaabbbbcdddd'
    print(sln.positions(s))

    s = 'aaa'
    print(sln.positions(s))
    
    s = "bababbabaa"
    print(sln.positions(s))

    s = "bababbaaab"
    print(sln.positions(s))    