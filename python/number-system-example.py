# -*- coding: utf-8 -*-
"""

"""

a = 0o762
b = 0b101
c = 0x1d8

print('a={0}, b={1}, c={2}'.format(a,b,c))

print(bin(c))
print(oct(a))
print(hex(b))
print(type(a), type(bin(a)))

print(eval(bin(1276)))
print(eval(oct(1276)))
print(eval(hex(1276)))

print(int(bin(1276)[2:],2))
print(int(oct(1276)[2:],8))
print(int(hex(1276)[2:],16))

print(int(bin(1276),0))
print(int(oct(1276),0))
print(int(hex(1276),0))



print(int('J', 21))
print(int('G', 17))
print(int('GF', 17))