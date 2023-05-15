# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:38:02 2023

@author: chenxy

1072. Flip Columns For Maximum Number of Equal Rows
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.

方法一: 哈希
思路与算法

题目给定 m×n 的矩阵，要求从中选取任意数量的列并翻转其上的每个单元格。单元格仅包含 0 或者 11。
问最多可以得到多少个由相同元素组成的行。如果某一行全部是 1 或者全部是 0，则表示该行由相同元素组成。

如果翻转固定的某些列，可以使得两个不同的行都变成由相同元素组成的行，那么我们称这两行为本质相同的行。例如 
001 和 110 就是本质相同的行。

本质相同的行有什么特点呢？可以发现，本质相同的行只存在两种情况，一种是由 0 开头的行，另一种是由 1 开头的行。
在开头的元素确定以后，由于翻转的列已经固定，所以可以推断出后续所有元素是 0 还是 1。

为了方便统计本质相同的行的数量，我们让由 1 开头的行全部翻转，翻转后行内元素相同的行即为本质相同的行。
之后我们将每一行转成字符串形式存储到哈希表中，遍历哈希表得到最多的本质相同的行的数量即为答案。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/solution/an-lie-fan-zhuan-de-dao-zui-da-zhi-deng-teeig/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

另一个思路：
本质是找出所有行中模式相同的行数最大值，这里关键在于如何描述每一行的pattern，
这里采取的方法是记录每一行从左到右值发生跳变的当前行下标值的一个集合，累加起来成为一个string，
以这个作为hash的key，最后检查一下hash表的value最大值即可

"""
import time
import random
import time
import itertools as it
import numpy as np
from   typing import List, Optional
from   collections import defaultdict, Counter
from   math import sqrt, inf
from   collections import deque
from   bisect import bisect, bisect_left, bisect_right

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        count = Counter()
        for i in range(m):
            value = 0
            for j in range(n):
                # 如果 matrix[i][0] 为 1，则对该行元素进行翻转
                value = value * 10 + (matrix[i][j] ^ matrix[i][0])
            count[value] += 1
        return max(count.values())


if __name__ == '__main__':

    sln  = Solution()                
    
    matrix = [[0,1],[1,1]]
    print(sln.maxEqualRowsAfterFlips(matrix))           
    
    matrix = [[0,1],[1,0]]
    print(sln.maxEqualRowsAfterFlips(matrix))           
    
    matrix = [[0,0,0],[0,0,1],[1,1,0]]
    print(sln.maxEqualRowsAfterFlips(matrix))           