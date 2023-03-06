""" 
999. 车的可用捕获量
在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。
它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选
择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进
入同一个方格。
返回车能够在一次移动中捕获到的卒的数量。--严格地来说，应该说是在車的一次移动的攻击覆盖范围内的卒的个数

示例 1：

输入：[[".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".","R",".",".",".","p"],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
输出：3
解释：
在本例中，车能够捕获所有的卒。

示例 2：
输入：[[".",".",".",".",".",".",".","."],
      [".","p","p","p","p","p",".","."],
      [".","p","p","B","p","p",".","."],
      [".","p","B","R","B","p",".","."],
      [".","p","p","B","p","p",".","."],
      [".","p","p","p","p","p",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
输出：0
解释：
象阻止了车捕获任何卒。

示例 3：
输入：[[".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      ["p","p",".","R",".","p","B","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".","B",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
输出：3
解释： 
车可以捕获位置 b5，d6 和 f5 的卒。

提示：
board.length == board[i].length == 8
board[i][j] 可以是 'R'，'.'，'B' 或 'p'
只有一个格子上存在 board[i][j] == 'R'

解题思路：
1. 先定位R
2. 从R的位置向4个方向出发搜索，直到碰到p, b or wall
    如果碰到的是p, 则结果加1

"""
import math
import time
import numpy as np

class Solution:
    #def numRookCaptures(self, board: List[List[str]]) -> int:
    def numRookCaptures(self, board) -> int:
        #1. Find R
        nrow = len(board)
        ncol = len(board)
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 'R':
                    rNum = r
                    cNum = c
                    break
        rslt = 0
        #2. left search
        for c in range(cNum,-1,-1):
            if board[rNum][c] == 'p':
                rslt += 1
                break
            if board[rNum][c] == 'B':
                break
        #3. right search
        for c in range(cNum,ncol):
            if board[rNum][c] == 'p':
                rslt += 1
                break
            if board[rNum][c] == 'B':
                break
        #4. up search
        for r in range(rNum,-1,-1):
            if board[r][cNum] == 'p':
                rslt += 1
                break
            if board[r][cNum] == 'B':
                break        
        #5. down search
        for r in range(rNum,nrow):
            if board[r][cNum] == 'p':
                rslt += 1
                break
            if board[r][cNum] == 'B':
                break        
        return rslt
                           
if __name__ == '__main__':

    sln   = Solution()

    print('\ntestcase1 ...')
    board =  [[".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".","R",".",".",".","p"],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
    tStart= time.time()
    print(sln.numRookCaptures(board))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    
    print('\ntestcase2 ...')
    board =  [[".",".",".",".",".",".",".","."],
      [".","p","p","p","p","p",".","."],
      [".","p","p","B","p","p",".","."],
      [".","p","B","R","B","p",".","."],
      [".","p","p","B","p","p",".","."],
      [".","p","p","p","p","p",".","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
    tStart= time.time()
    print(sln.numRookCaptures(board))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    

    print('\ntestcase2 ...')
    board =  [[".",".",".",".",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      ["p","p",".","R",".","p","B","."],
      [".",".",".",".",".",".",".","."],
      [".",".",".","B",".",".",".","."],
      [".",".",".","p",".",".",".","."],
      [".",".",".",".",".",".",".","."]]
    tStart= time.time()
    print(sln.numRookCaptures(board))
    tStop = time.time()
    print('tStart={0}, tStop={1}, tElapsed={2}(sec)'.format(tStart, tStop, tStop-tStart))    
