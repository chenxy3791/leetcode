# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 05:52:20 2022

@author: Dell
"""
import random
import time
class Solution:
    def reachingPoints1(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        memo = dict()
        def dp(_sx,_sy,_tx,_ty):
            if (_sx,_sy,_tx,_ty) in memo:
                return memo[(_sx,_sy,_tx,_ty)]
            # baseline case
            if _sx > _tx or _sy > _ty:
                return False
            if _sx == _tx and _sy == _ty:
                return True
            
            rslt = dp(_sx+_sy, _sy, _tx, _ty) or dp(_sx, _sx+_sy, _tx, _ty)
            memo[(_sx,_sy,_tx,_ty)] = rslt
            return rslt
        
        return dp(sx, sy, tx, ty)
    
    def reachingPoints2(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # With the approach, no need of memoization
        # memo = dict()
        def dp(_sx,_sy,_tx,_ty):
            # print("dp:", _sx,_sy,_tx,_ty)
            # if (_sx,_sy,_tx,_ty) in memo:
            #     return memo[(_sx,_sy,_tx,_ty)]
            # baseline case
            if _sx > _tx or _sy > _ty or _tx < 0 or _ty < 0:
                return False
            if _sx == _tx and _sy == _ty:
                return True
            if _sx+_sy==_tx and _sy == _ty:
                return True
            if _sx==_tx and _sx+_sy == _ty:
                return True
            
            rslt = dp(_sx+_sy, _sy, _tx-_ty, _ty) or dp(_sx+_sy, _sy, _tx, _ty-_tx) or dp(_sx, _sx+_sy, _tx-_ty, _ty) or dp(_sx, _sx+_sy, _tx, _ty-_tx)
            # memo[(_sx,_sy,_tx,_ty)] = rslt
            return rslt
        
        return dp(sx, sy, tx, ty)

    # def reachingPoints3(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    #     while True:
    #         if sx==tx and sy==ty:
    #             return True
    #         if sx>tx or sy>ty:
    #             return False
    #         if tx==ty:
    #             return False
            
    #         if tx>ty:
    #             tx = tx - ty
    #         else:
    #             ty = ty - tx

    def reachingPoints3(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx>sx and ty>sy and tx!=ty:
            if tx>ty:
                tx = tx % ty
            else:
                ty = ty % tx
        if tx==ty==sx==sy:
            return True
        if tx==sx:
            if ty>sy and (ty-sy)%tx==0:
                return True
            else:
                return False
        if ty==sy:
            if tx>sx and (tx-sx)%ty==0:
                return True
            else:
                return False
        return False
    
if __name__ == "__main__":
    
    sln = Solution()
    
    sx, sy, tx, ty = 1,1,3,5
    print(sln.reachingPoints1(sx, sy, tx, ty))
    print(sln.reachingPoints2(sx, sy, tx, ty))
    print(sln.reachingPoints3(sx, sy, tx, ty))

    sx, sy, tx, ty = 3,3,12,9
    print(sln.reachingPoints1(sx, sy, tx, ty))
    print(sln.reachingPoints2(sx, sy, tx, ty))
    print(sln.reachingPoints3(sx, sy, tx, ty))

    sx, sy, tx, ty = 9,10,9,19
    print(sln.reachingPoints1(sx, sy, tx, ty))
    print(sln.reachingPoints2(sx, sy, tx, ty))
    print(sln.reachingPoints3(sx, sy, tx, ty))

    sx, sy, tx, ty = 2,7,9,16
    print(sln.reachingPoints1(sx, sy, tx, ty))
    print(sln.reachingPoints2(sx, sy, tx, ty))
    print(sln.reachingPoints3(sx, sy, tx, ty))    
    
    # sx, sy, tx, ty = 1,1,2,2 
    # print(sln.reachingPoints1(sx, sy, tx, ty))
    
    # sx, sy, tx, ty = 3,1,200,1037 
    # print(sln.reachingPoints1(sx, sy, tx, ty))
    
    # sx, sy, tx, ty = 3,1,2073,1037 
    # print(sln.reachingPoints1(sx, sy, tx, ty))

    # sx, sy, tx, ty = 3,1,2073,7037 
    # print(sln.reachingPoints1(sx, sy, tx, ty))

    sx, sy, tx, ty = 3,1,2073,10037 
    tstart = time.time()
    ans = sln.reachingPoints1(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))

    tstart = time.time()
    ans = sln.reachingPoints2(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))    

    tstart = time.time()
    ans = sln.reachingPoints3(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart)) 
    
    sx, sy, tx, ty = 3,2,7,10037 
    tstart = time.time()
    ans = sln.reachingPoints3(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))

    tstart = time.time()
    ans = sln.reachingPoints2(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))    

    sx, sy, tx, ty = 35,13,455955547,420098884
    # ans = sln.reachingPoints2(sx, sy, tx, ty)
    # tstop  = time.time()
    # print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))
    tstart = time.time()
    ans = sln.reachingPoints3(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))

    sx, sy, tx, ty = 1,1,1,10**9
    tstart = time.time()
    ans = sln.reachingPoints3(sx, sy, tx, ty)
    tstop  = time.time()
    print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))
    
    # for k in range(10):
    #     sx = random.randint(1,10)
    #     # sy = random.randint(1,10)
    #     sy = 1
    #     # tx = random.randint(10**7,10**9)
    #     # ty = random.randint(10**7,10**9)
    #     tx = random.randint(10**2,10**4)
    #     ty = random.randint(10**2,10**4)
    #     # tstart = time.time()
    #     # ans = sln.reachingPoints1(sx, sy, tx, ty)
    #     # tstop  = time.time()
    #     # print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))
        
    #     tstart = time.time()
    #     ans = sln.reachingPoints2(sx, sy, tx, ty)
    #     tstop  = time.time()
    #     print("sx,sy,tx,ty={0}, ans={1}, tcost={2:5.2f}sec".format((sx,sy,tx,ty),ans,tstop-tstart))
    