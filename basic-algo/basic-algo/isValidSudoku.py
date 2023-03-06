""" 
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

NOTE: The naive solution is validate each row, each column, and each 3*3 block.
For each one of them: 
(1) Whether does each element belongs to either '.' or '1'~'9' --> The input assure this.
(2) Whether each element except '.' occurs only once

"""

import time

class Solution:
	def isValid(self, group):
		for k in range(len(group)):
			if group[k] != '.':
				for j in range(k+1,len(group)):
					if group[k] == group[j]:
						#print('group check fail at [{0}, {1}]'.format(k,j))		
						return False
		return True

	def isValidSudoku(self, board):      
		# Check each row:
		for k in range(9):
			#print(board[k])
			valid = self.isValid(board[k])
			#if ~valid: Doesn't work.
			if valid == False:
				#print('Row#{0} check fails'.format(k))
				return False

		# Check each col:
		for k in range(9):
			group = [row[k] for row in board]
			valid = self.isValid(group)
			if valid == False:
				#print('Col#{0} check fails'.format(k))
				return False

		# Check each sub-block:
		for k in range(9):
			k1 = int(k/3)
			k2 = k%3			
			group = [board[l][m] for l in [0+k1*3,1+k1*3,2+k1*3] for m in [0+k2*3,1+k2*3,2+k2*3] ]
			valid = self.isValid(group)
			if valid == False:
				#print('subblock#{0} check fails'.format(k))
				return False

		return True

if __name__ == '__main__':

	sln   = Solution()

	# Testcase0
	print('Testcase0...')
	board = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]
	print(sln.isValidSudoku(board))

	# Testcase1
	print('Testcase1...')
	board = [
		["8","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]
	print(sln.isValidSudoku(board))

	# Testcase2
	print('Testcase2...')
	board = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","9","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]
	]
	print(sln.isValidSudoku(board))

	# Testcase3
	print('Testcase3...')
	board = [
		[".",".","4",".",".",".","6","3","."],
		[".",".",".",".",".",".",".",".","."],
		["5",".",".",".",".",".",".","9","."],
		[".",".",".","5","6",".",".",".","."],
		["4",".","3",".",".",".",".",".","1"],
		[".",".",".","7",".",".",".",".","."],
		[".",".",".","5",".",".",".",".","."],
		[".",".",".",".",".",".",".",".","."],
		[".",".",".",".",".",".",".",".","."]]
	print(sln.isValidSudoku(board))		