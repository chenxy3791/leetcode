# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:37:04 2022

@author: Dell
"""

import random

num_trial = 100000
exchange_win = 0
for k in range(num_trial):
    
    #1. 随机将车子放在3个门后面，分别记为门1,门2,门3
    car = random.randint(1, 3)
    #print(car)
    
    #2. 随机打开其中任何一扇门
    open1 = random.randint(1, 3)
    
    #3. 主持打开其中一扇门
    # 如果open1打开的是有车的门，则主持人在剩下两扇门中任选一扇打开
    # 如果open1打开的是无车的门，则主持人必须打开另一扇无车的门
    while 1:
        open2 = random.randint(1, 3)
        if open2 != open1 and open2 != car:
            break
        
    if open1 != car:
        exchange_win += 1

print('The win prob of exchanging the door is {0}'.format(exchange_win/num_trial))
    