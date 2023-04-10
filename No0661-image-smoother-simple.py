# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 07:41:42 2022

@author: Dell
"""
from typing import List
import numpy as np

class Solution:
    def imageSmoother1(self, img: List[List[int]]) -> List[List[int]]:
        imgpadded = np.zeros((len(img)+2, len(img[0])+2))
        imgsmoothed = np.zeros((len(img), len(img[0])))
        for r in range(len(img)):
            for c in range(len(img[0])):
                imgpadded[r+1,c+1] = img[r][c]
        # print(imgpadded)
        for r in range(len(img)):
            for c in range(len(img[0])):
                divisor = 9
                if (r,c) in [(0,0),(0,len(img)-1),(len(img)-1,0),(len(img)-1,len(img)-1)]:
                    divisor = 4
                elif r==0 or r==len(img)-1 or c==0 or c==len(img)-1:
                    divisor = 6
                imgsmoothed[r,c] = int(np.sum(imgpadded[r:r+3,c:c+3])/divisor)
        imgsmoothed = imgsmoothed.astype('int')
        return [list(imgsmoothed[k,:]) for k in range(len(img))]

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:    
        imgs = [len(img[0])*[0] for k in range(len(img))]
        for r in range(len(img)):
            for c in range(len(img[0])):
                valid_cnt = 0
                for r1 in range(-1,2):
                    for c1 in range(-1,2):
                        if r+r1>=0 and r+r1<len(img) and c+c1>=0 and c+c1<len(img[0]):
                            # print(r,c,r+r1,c+c1)
                            valid_cnt  += 1
                            imgs[r][c] += img[r+r1][c+c1] 
                imgs[r][c] = imgs[r][c]//valid_cnt
        return imgs
    
if __name__ == '__main__':
    
    sln = Solution()
    
    img = [[1,1,1],[1,0,1],[1,1,1]]
    print(sln.imageSmoother(img))
    
    img = [[100,200,100],[200,50,200],[100,200,100]]
    print(sln.imageSmoother(img))
    
    img = [[100,200,100]]
    print(sln.imageSmoother(img))    
    
    img = [[100],[200],[100]]
    print(sln.imageSmoother(img))        