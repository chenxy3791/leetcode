# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 07:45:53 2022

@author: Dell
"""
import time
import random

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        has_lower = has_upper = has_digit = False
        for ch in password:
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
        
        categories = has_lower + has_upper + has_digit

        if n < 6:
            return max(6 - n, 3 - categories)
        elif n <= 20:
            replace = cnt = 0
            cur = "#"

            for ch in password:
                if ch == cur:
                    cnt += 1
                else:
                    replace += cnt // 3
                    cnt = 1
                    cur = ch
            
            replace += cnt // 3
            return max(replace, 3 - categories)
        else:
            # 替换次数和删除次数
            replace, remove = 0, n - 20
            # k mod 3 = 1 的组数，即删除 2 个字符可以减少 1 次替换操作
            rm2 = cnt = 0
            cur = "#"

            for ch in password:
                if ch == cur:
                    cnt += 1
                else:
                    if remove > 0 and cnt >= 3:
                        if cnt % 3 == 0:
                            # 如果是 k % 3 = 0 的组，那么优先删除 1 个字符，减少 1 次替换操作
                            remove -= 1
                            replace -= 1
                        elif cnt % 3 == 1:
                            # 如果是 k % 3 = 1 的组，那么存下来备用
                            rm2 += 1
                        # k % 3 = 2 的组无需显式考虑
                    replace += cnt // 3
                    cnt = 1
                    cur = ch
            
            if remove > 0 and cnt >= 3:
                if cnt % 3 == 0:
                    remove -= 1
                    replace -= 1
                elif cnt % 3 == 1:
                    rm2 += 1
            
            replace += cnt // 3

            # 使用 k % 3 = 1 的组的数量，由剩余的替换次数、组数和剩余的删除次数共同决定
            use2 = min(replace, rm2, remove // 2)
            replace -= use2
            remove -= use2 * 2
            # 由于每有一次替换次数就一定有 3 个连续相同的字符（k / 3 决定），因此这里可以直接计算出使用 k % 3 = 2 的组的数量
            use3 = min(replace, remove // 3)
            replace -= use3
            remove -= use3 * 3
            return (n - 20) + max(replace, 3 - categories)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/strong-password-checker/solution/qiang-mi-ma-jian-yan-qi-by-leetcode-solu-4fqx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# class Solution:
#     def strongPasswordChecker1(self, password: str) -> int:   
#         def legalCheck(c):
#             return (c.isdigit() or c.islower() or c.isupper() or c in ['.','!'])
        
#         mdfyCnt = 0
#         hasLower = False
#         hasUpper = False
#         hasDigit = False
#         for k in range(len(password)):
#             if password[k].isdigit():
#                 hasDigit = True
#             elif password[k].islower():
#                 hasLower = True
#             elif password[k].isupper():
#                 hasUpper = True            
#             elif not password[k] not in ['.','!']:
#                 # Invalid character
#                 mdfyCnt += 1
#         if len(password) < 6:
#             return 6-len(password) + mdfyCnt
        
#         sameCnt  = 0
#         prevChar = None
#         for k in range(len(password)):
#             if legalCheck(password[k]):
#                 # Only check the legal characters.
#                 if password[k] == prevChar:
#                     sameCnt += 1
#                 else:
#                     mdfyCnt += sameCnt // 3
#                     sameCnt  = 1
#             else:
#                 # But when illegal char, should reset sameCnt
#                 sameCnt = 0
#             prevChar = password[k]
#         mdfyCnt += sameCnt // 3
#         if not hasLower: mdfyCnt+=1
#         if not hasUpper: mdfyCnt+=1
#         if not hasDigit: mdfyCnt+=1
#         return mdfyCnt

#     def strongPasswordChecker(self, password: str) -> int:   
#         def legalCheck(c):
#             return (c.isdigit() or c.islower() or c.isupper() or c in ['.','!'])
#         pwLen    = len(password)
#         mdfyCnt  = 0
#         hasLower = False
#         hasUpper = False
#         hasDigit = False
#         sameCnt  = 0
#         prevChar = None        
#         for k in range(len(password)):
#             if password[k].isdigit():
#                 hasDigit = True
#             elif password[k].islower():
#                 hasLower = True
#             elif password[k].isupper():
#                 hasUpper = True    
            
#         for k in range(len(password)):
#             if legalCheck(password[k]):                                    
#                 if password[k] == prevChar:
#                     sameCnt += 1
#                 else:
#                     if sameCnt // 3 > 0:
#                         if pwLen < 6:
#                             # Insert to break the continuous identical sequence
#                             tmp = sameCnt // 3
#                             while tmp > 0:
#                                 if not hasLower: 
#                                     hasLower = True
#                                 elif not hasUpper: 
#                                     hasUpper = True
#                                 elif not hasDigit: 
#                                     hasDigit = True
#                                 pwLen += 1
#                                 mdfyCnt += 1
#                                 tmp -= 1 
#                         elif pwLen > 20:
#                             print(pwLen, sameCnt)
#                             if sameCnt <= pwLen-20:
#                                 # Remove    
#                                 pwLen  -= sameCnt
#                                 mdfyCnt+= sameCnt
#                                 sameCnt = 0
#                             else:
#                                 # Remove
#                                 sameCnt-= pwLen-20
#                                 mdfyCnt+= pwLen-20
#                                 pwLen   = 20
#                                 tmp = sameCnt // 3
#                                 while tmp > 0:
#                                     # Replace
#                                     if not hasLower: 
#                                         hasLower = True
#                                     elif not hasUpper: 
#                                         hasUpper = True
#                                     elif not hasDigit: 
#                                         hasDigit = True
#                                     mdfyCnt += 1
#                                     tmp -= 1                                                             
#                         else:
#                             # print(k)
#                             tmp = sameCnt // 3
#                             while tmp > 0:
#                                 # Replace
#                                 if not hasLower: 
#                                     hasLower = True
#                                 elif not hasUpper: 
#                                     hasUpper = True
#                                 elif not hasDigit: 
#                                     hasDigit = True
#                                 mdfyCnt += 1
#                                 tmp -= 1  
#                     sameCnt  = 1                    
#             else:
#                 # illegal character, remove or replace
#                 # mdfyCnt += 1
#                 if pwLen < 6:
#                     # Replace
#                     mdfyCnt += 1                    
#                     if not hasLower: 
#                         hasLower = True
#                     elif not hasUpper: 
#                         hasUpper = True
#                     elif not hasDigit: 
#                         hasDigit = True                    
#                 elif pwLen > 20:                        
#                     if (k>0) and (k<len(password)) and (password[k-1]==password[k+1]):
#                         # Replace
#                         mdfyCnt += 1
#                         if not hasLower: 
#                             hasLower = True
#                         elif not hasUpper: 
#                             hasUpper = True
#                         elif not hasDigit: 
#                             hasDigit = True                        
#                     else:
#                         # Remove
#                         pwLen -= 1
#                 # when illegal char, should reset sameCnt
#                 sameCnt = 0
#             prevChar = password[k]
#         # For the last continuous identical legal char sequence.
#         tmp = sameCnt // 3
#         while tmp > 0:
#             # Replace
#             if not hasLower: 
#                 hasLower = True
#             elif not hasUpper: 
#                 hasUpper = True
#             elif not hasDigit: 
#                 hasDigit = True
#             mdfyCnt += 1
#             tmp -= 1  
            
#         # print(pwLen,mdfyCnt,hasLower,hasUpper,hasDigit)        
#         if pwLen < 6:
#             while pwLen<6:
#                 mdfyCnt += 1
#                 pwLen   += 1
#                 if not hasLower: 
#                     hasLower = True
#                 elif not hasUpper: 
#                     hasUpper = True
#                 elif not hasDigit: 
#                     hasDigit = True                  
#         elif pwLen > 20:
#             mdfyCnt += pwLen-20

#         if not hasLower: mdfyCnt+=1
#         if not hasUpper: mdfyCnt+=1
#         if not hasDigit: mdfyCnt+=1

#         return mdfyCnt
            
if __name__ == "__main__":

    # # Verify validityChecker()
    # print(validityChecker("a"))
    # print(validityChecker("aA1"))    
    # print(validityChecker("1337C0d3"))    
    
    validCharSet = '0123456789'
    validCharSet = validCharSet + 'abcdefghijklmnopqrstuvwxyz'
    validCharSet = validCharSet + 'abcdefghijklmnopqrstuvwxyz'.upper()
    validCharSet = validCharSet + '.!'
    
    # for k in range(10):
    #     pwlen = random.randint(1,20)
    #     password = ''
    #     for l in range(pwlen):
    #         password = password + random.choice(validCharSet)
    #     print('password={0}, valid={1}'.format(password,validityChecker(password)))    
        
    sln = Solution()
    print(sln.strongPasswordChecker("a"))
    print(sln.strongPasswordChecker("aA1"))    
    print(sln.strongPasswordChecker("1337C0d3"))    
    print(sln.strongPasswordChecker("aaa123"))
    print(sln.strongPasswordChecker("aaa111"))    
    print(sln.strongPasswordChecker("aaaB1"))
    print(sln.strongPasswordChecker("ABABABABABABABABABAB1"))
    print(sln.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
    for k in range(10):
        pwlen = random.randint(1,50)
        password = ''
        for l in range(pwlen):
            password = password + random.choice(validCharSet)
        print('password={0}, ans={1}'.format(password,sln.strongPasswordChecker(password)))   
