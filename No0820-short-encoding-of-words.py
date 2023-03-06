""" 
820. 单词的压缩编码
给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

示例：

输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。

提示：
1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母

解题思路：
只有一个单词恰好是它的前一个单词的尾子字符串，才能实现overlap encoding

补充：
不仅限于上面所说的情况。例子：["me", "time"]
前面的单词是后面的单词的子字符串，这样难度就立即上去了

另外，又不能改变原有单词的顺序。
所以基本上还是必须按照原有顺序遍历所有单词。
但是对于每个新的单词，不是只看它是不是前一个单词的子串，而是要看它是不是到当前为止构成的S的子串。
与上述例子类似的情况有(不仅仅出现在最前面两个)：
["dog", "me", "time",  "mytime"] --> "dog#mytime#", [0, 8, 6, 4]
    --> "dog#" --> "dog#me#" --> "dog#time#" --> "dog#mytime#"
这意味着每个新的单词要跟当前的S的每一节进行比较，看相互是否是对方的子串。
如果是S中某一节是新的单词的子串的话，需要更新S的该字符串节，并且更新所有与它相关联的原单词的index

一种可能的方案：
先确认原单词串中的所有的独立单词，即不是任何其它单词的子串的单词。
先处理这些独立单词，然后再处理非独立单词
如何跟踪记录这些信息呢？
遍历每一个单词看它是不是任何其它单词的子串，是的话，就推后处理。。。

实际上原题只要求返回总长，而不需要给出A和S，所以只要遍历并统计长度即可。
1. 对words基于单词长度排序
2. 按words中单词长度从大到小遍历 -- 因为长的单词不可能是短的单词的子串，这样不必进行单词间是否包含的检测
2.1 如果words[k]+"#"不是S的子串，加入到S
    这里用'words[k]+"#"'而不是用‘words[k]’是因为只有当一个单词是另一个的尾子串才能进行缩短编码
2.2 否则就不加入
单词再加入S后中间加了“#”进行分割，所以从大到小处理时，只需要判断是不是S的子串即可，如果是的话则表明当前单词
必定是原words中某个更长单词的子串

"""
import math
import time
import numpy as np

class Solution:
    #def minimumLengthEncoding(self, words: List[str]) -> int:
    def minimumLengthEncoding(self, words) -> int:
        total = 0
        words.sort(key = len)
        S = ""
        for k in range(len(words)-1,-1,-1):
            if k > len(words)-10:
                print('k = {0}, words[k] = {1}'.format(k,words[k]))
            if S.find(words[k]+"#") < 0:
                S = S + words[k] + "#"
        return len(S)

class Solution1:
    # Calculate A and S explicitly, but not necessarily needed.
    # Failed in some cases.

    #def minimumLengthEncoding(self, words: List[str]) -> int:
    def minimumLengthEncoding(self, words) -> int:
        if len(words) == 0:
            return []

        A = [0]        
        S = words[0] + "#"
        k = 1
        while k < len(words):
            idx = words[k-1].find(words[k])
            if (idx + len(words[k])) == len(words[k-1]) and idx >= 0:
                A.append(len(S)-len(words[k])-1)
            else:
                A.append(len(S))
                S = S + words[k] + "#"
            k += 1
            print('S = {0}, A = {1}'.format(S, A))
        return len(S)

if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    words = ["time", "me", "bell"]
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    words = ["time", "abell", "bell"]
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))         
    
    print('\ntestcase3 ...')
    words = ["hello","hello", "i", "am", "chenxy"]
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))       

    print('\ntestcase4 ...')
    words = ["i","", "am", "chenxy"]
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        

    print('\ntestcase5 ...')
    words = ["me", "time"]
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        

    filename = 'No820-testdata.py'
    exec(compile(open(filename).read(),'dummy','exec'))   
    print('\ntestcase6 ...')    
    tStart= time.time()
    print(sln.minimumLengthEncoding(words))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))        
