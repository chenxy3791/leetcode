# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 21:57:50 2022

@author: Dell
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# fig,ax = plt.subplots(3,1)
# # Generate uniform distributed random samples of real number within the range of [0,1]
# rand0 = np.random.random(10000)
# ax[0].hist(rand0)

# # Generate uniform distributed random integer samples within the specified range
# rand1 = np.random.randint(0,1000,10000)
# ax[1].hist(rand1)

# rand2 = np.random.randn(10000)
# ax[2].hist(rand2,bins=100)

# # coin-tossing
# num_tosses  = [1000,10000,100000]
# np.random.seed(42)
# for num_toss in num_tosses:
#     coin_toss = np.random.random(num_toss)
#     head = coin_toss >= 0.5
#     tail = coin_toss <  0.5
#     head_count = np.sum(head)
#     tail_count = np.sum(tail)
#     head_prob  = head_count/num_toss
#     tail_prob  = tail_count/num_toss
#     print('num_toss = {0}, head_prob={1}, tail_prob={2}'.format(num_toss,head_prob,tail_prob))
    
# # die-rolling
# num_rolling  = [1000,10000,100000]    
# for num_roll in num_rolling:
#     die_roll = np.random.random(num_roll)
#     one   = die_roll <   1/6
#     two   = np.logical_and(die_roll >=  1/6, die_roll < 2/6)
#     three = np.logical_and(die_roll >=  2/6, die_roll < 3/6)
#     four  = np.logical_and(die_roll >=  3/6, die_roll < 4/6)
#     five  = np.logical_and(die_roll >=  4/6, die_roll < 5/6)
#     six   = die_roll >=  5/6

#     prob_one   = np.sum(one)  /num_roll
#     prob_two   = np.sum(two)  /num_roll
#     prob_three = np.sum(three)/num_roll
#     prob_four  = np.sum(four) /num_roll
#     prob_five  = np.sum(five) /num_roll
#     prob_six   = np.sum(six)  /num_roll
#     print('num_roll = {0}, prob_one={1}, prob_two={2}, prob_three={3}, prob_four={4}, prob_five={5}, prob_6={6}'\
#           .format(num_roll,prob_one,prob_two,prob_three,prob_four,prob_five,prob_six))
        
# Find the approximation of pie using monte-carlo simulation
num_trials  = [1000,10000,100000,int(1e6),int(1e7)]    
for num_trial in num_trials:
    x     = np.random.random(num_trial) * 2 - 1
    y     = np.random.random(num_trial) * 2 - 1
        
    d     = np.sqrt(x**2 + y**2)
    in_circle = (d <= 1)
    
    pi_esti = 4 * np.mean(in_circle)
    
    print('num_trial = {0}, pi_esti={1}, err = {2}'.format(num_trial,pi_esti,np.abs(pi_esti-np.pi)))
         