# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 09:17:15 2021

@author: chenxy
"""

import itertools as it

# accumulate
print('accumulate example 1...')
print(list(it.accumulate([1,2,3,4,5])))

# count(start, step)
print('count example 1 ...')
k = 0
for item in it.count(10.7,1.1):
    k += 1
    if k == 10 : break    
    print('k={0}, item={1})'.format(k,item))  

print('count example 2 ...')
for k in it.count(0):
    item = 10.7 + 1.1 * k
    if k == 10 : 
        break    
    print('k={0}, item={1})'.format(k,item))  

# cycle(iterable)
print('\ncycle example 1 ...')
k = 0
for item in it.cycle('ABCDE'):
    print('k={0}, item={1}'.format(k,item))      
    k += 1
    if k == 10 : break    

# repeat(object, times)
print('\nrepeat example 1 ...')
print('Important things are worth of three times of repeat!')
for item in it.repeat('Do not answer!',3):
    print('{0}'.format(item))      
print('\nrepeat example 2 ...')
print(list(map(pow, range(10), it.repeat(2))))

# product(*iterables, repeat=1)
print('\nproduct example 1 ...')
for item in it.product('AB','CD'):
    print(item)

print('\nproduct example 2 ...')
for item in it.product('AB', repeat=4):
    print(item)

# permutations
print('\npermutations example1:')
# for p in it.permutations(['a','b','c'],3):
for p in it.permutations(['a','b','c']): 
    # Has the same behaviour as the above statement    
    print(p, end=', ')
print('\n')

print('permutations example2:')
for p in it.permutations(['a','b','c'],2 ): 
    # Return any permutations of length 2
    print(p, end=', ')
print('\n')

# combinations
print('\ncombinations example1:')
for item in it.combinations(['A', 'B', 'C', 'D'], 2):
    print(item)

# combinations_with_replacement
print('\combinations_with_replacement example1:')
k = 0
for item in it.combinations_with_replacement(['A', 'B', 'C', 'D'], 3):
    print(item)
    k += 1
print('Totally there are {0} combinations'.format(k))    

# islice
print('\nislice example1:')
A = [k for k in range(10)]
for item in it.islice(A, 3):
    print(item)    

print('\nislice example2:')
A = [k for k in range(10)]
for item in it.islice(A, 2,8,2):
    print(item)  

# chain example
print(list(it.chain('ABCD','EFG','HIJ')))

# def get_three_data(data_list,amount):
#     for data in list(itertools.combinations(data_list, 3)):
#         if sum(data) == amount:
#             print(data)
# #(7, 13, 15)
# #(9, 11, 15)

# max= 100
# ll = [x for x in range(2,max +1)]
# print(ll)
# for i in range(max):
#     if i > len(ll) -1:
#         break
#     else:
#         item = ll[i]
#         ll = [x for x in ll if item == x or x%item != 0]
# print(len(ll))
 
# import itertools
 
# for item in itertools.combinations(ll,3):
#     if sum(item) == 35:
#         print(item)