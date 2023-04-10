# -*- coding: utf-8 -*-
"""
Created on Sun May 29 08:25:05 2022

@author: Dell
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isValidIPv4Field(s):
            if len(s)>1 and s.find('0')==0:
                return False
            if s.isdigit():
                return 0 <= int(s) <= 255
            return False
        
        def isValidIPv6Field(s):
            if 0<len(s)<=4:
                for k in range(len(s)):
                    if not (48<=ord(s[k])<=57 or 97<=ord(s[k])<=102 or 65<=ord(s[k])<=70):
                        return False
                return True
            return False
            
        if queryIP.count('.') == 3:
            # Possibly IPv4
            a = queryIP.split('.')
            for k in range(4):
                if not isValidIPv4Field(a[k]):
                    return "Neither"
            return "IPv4"
        elif queryIP.count(':') == 7:
            # Possibly IPv6
            a = queryIP.split(':')
            for k in range(8):
                if not isValidIPv6Field(a[k]):
                    return "Neither"
            return "IPv6"
        return "Neither"
    
if __name__ == "__main__":
    
    sln = Solution()    
    
    queryIP = "172.16.254.1"
    print(sln.validIPAddress(queryIP))    
            
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    print(sln.validIPAddress(queryIP))

    queryIP = "256.256.256.256"     
    print(sln.validIPAddress(queryIP))
    
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
    print(sln.validIPAddress(queryIP))
    
    queryIP = "1e1.4.5.6"
    print(sln.validIPAddress(queryIP))
    
    queryIP = "20EE:FGb8:85a3:0:0:8A2E:0370:7334"
    print(sln.validIPAddress(queryIP))