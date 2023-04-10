# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 07:28:12 2022

@author: Dell
"""
import time
from typing import List
from collections import deque

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        input = input +'\n' # Attach one '\n' for the convenience of processing
        maxlen = 0
        q = deque([(0,0)]) # Put root node into stack

        tab_cnt = 0       
        name    = ''
        isFile  = False
        for k,c in enumerate(input):
            if c=='\t':
                tab_cnt += 1
            elif c=='\n':
                # Found a new name, either a dir name or a file name
                if isFile:
                    # A file
                    # print('A file is found: ',name)
                    while True:
                        length, layer = q.pop()
                        if layer < (tab_cnt+1):
                            filePathLen = len(name) + length
                            maxlen = filePathLen if filePathLen>maxlen else maxlen
                            q.append((length, layer)) # Put it back into stack
                            break
                else:
                    # A dir
                    # print('A dir is found: ',name)
                    while True:
                        length, layer = q.pop()
                        if layer < (tab_cnt+1):
                            dirPathLen = len(name) + length + 1
                            q.append((length, layer)) # Put it back into stack
                            q.append((dirPathLen,tab_cnt+1))
                            break
                # Reset 
                tab_cnt = 0
                name    = ''
                isFile  = False
            else:
                name = name + c
                if c=='.':
                    isFile = True
            
        return maxlen
                
if __name__ == "__main__":
    
    sln = Solution()
    input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    print(sln.lengthLongestPath(input))
    
    input = "dir\n\tsubdir1\n\t\tfile.ext\n\tsubdir2\n\t\tfile.ext"
    print(sln.lengthLongestPath(input))
    
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(sln.lengthLongestPath(input))

    input = "dir\n\tsubdir1\n\t\tsubsubdir1\n\t\tfile1.ext\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(sln.lengthLongestPath(input))
    
    input = "a"
    print(sln.lengthLongestPath(input))
    
    input = "file1.txt\nfile2.txt\nlongfile.txt"
    print(sln.lengthLongestPath(input))