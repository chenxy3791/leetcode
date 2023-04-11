# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:21:29 2022

@author: Dell
"""
import random
class Solution:
    def minimumBuckets(self, street: str) -> int:
        B_cnt = 0
        # The first round
        if street[0]=='H':
            if len(street)==1:
                return -1
            elif street[1]=='H':
                return -1
            else:
                street = 'HB'+street[2:]
                B_cnt += 1
        if street[-1]=='H':
            if street[-2]=='H':
                return -1
            elif street[-2]=='.': # it may already set to 'B'
                street = street[:-2]+'BH'
                B_cnt += 1
        
        for k in range(1,len(street)-1):
            if street[k-1]=='H' and street[k]=='H' and street[k+1]=='H':
                return -1
            elif street[k-1]=='.' and street[k]=='H' and street[k+1]=='H': # it may already set to 'B'
                street = street[:k-1] + 'B' + street[k:]
                B_cnt += 1
            elif street[k-1]=='H' and street[k]=='H' and street[k+1]=='.': # it may already set to 'B'
                # street[k+1] = 'B'
                street = street[:k+1] + 'B' + street[k+2:]
                B_cnt += 1
        # print(street,B_cnt)    
        # The second round
        memo = dict()   
        def dp(k) -> int:
            # print('dp: ',k)
            if k in memo:
                return memo[k]            
            # baseline case
            if k >= len(street)-2:
                return 0
            j = k+1  # instead of k!             
            # search for the first H with '.' in both side
            while j<=len(street)-2:
                if street[j]=='H' and street[j-1]=='.' and street[j+1]=='.':
                    ret1 = 1+dp(j+1)
                    if j==len(street)-2:
                        ret2 = 1
                    else:
                        if street[j+2]=='.' or street[j+2]=='B':                        
                            ret2 = 1+dp(j+2)
                        elif street[j+2]=='H':
                            ret2 = 1+dp(j+3)
                    return min(ret1,ret2)
                j += 1
            return 0    
            
        return B_cnt + dp(0)
    
if __name__ == '__main__':
    
    sln = Solution()
    
    street = "H..H"
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))
    
    street = ".H.H."
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))
    
    street = ".HHH."
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))
    
    street = "H"
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))
    
    street = "."
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))

    street = ".."
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))  
    
    street = "H."
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))    
    
    street = "H.H"
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))   
    
    street = ".HH.HH.HH.HH..H"
    print('street={0}, ans={1}'.format(street,sln.minimumBuckets(street)))
    
    # Random Test
    for i in range(1000):
        n = random.randint(1,50)
        street = ''
        for l in range(n):
            m = random.randint(0,3)
            street = street + ('H' if m==0 else '.')
        print('n={0}, street={1}, '.format(n,street), end='')
        ans = sln.minimumBuckets(street)
        print('ans={0}'.format(ans))
    
    