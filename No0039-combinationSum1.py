"""
Given a set of candidate numbers (candidates) (without duplicates) 
and a target number (target), find all unique combinations in 
candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import random
import time

class Solution:
    #def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSumRecursive(self, candidates, target: int):
        #print(candidates, target)
        if len(candidates) == 0 or target < 0:
            return []
        if target == 0:
            return [[]] # Note the critical difference between "[]" and "[[]]"! Related to appending subAns to ans below.            
        if len(candidates) == 1:
            if (target % candidates[0]) == 0:
                return [int(target/candidates[0]) * candidates]
            else:
                return []
        
        M = int(target / candidates[0])
        ans = []
        for k in range(M+1):
            subAns = self.combinationSumRecursive(candidates[1:], target-k*candidates[0])
            #print('subAns =', subAns)        
            for subList in subAns:
                #print(subList)
                ans.append(k*[candidates[0]] + subList)        
        return ans

    def combinationSum(self, candidates, target: int):
""" 
执行结果：通过
执行用时 :96 ms, 在所有 Python3 提交中击败了40.66%的用户
内存消耗 :14.8 MB, 在所有 Python3 提交中击败了5.14%的用户         
"""
        memo = dict() # can be accessed from dp() directly.
        def dp(i,target):            
            if (i,target) in memo:
                return memo[(i,target)]
            if target < 0 or len(candidates) == 0:
                return []
            if target == 0:
                return [[]] # Note the critical difference between "[]" and "[[]]"! Related to appending subAns to ans below.
            if (i+1) == len(candidates):
                if (target % candidates[i]) == 0:
                    return [int(target/candidates[i]) * [candidates[i]]]
                else:
                    return []
            
            M = int(target / candidates[i])
            ans = []
            for k in range(M+1):
                subAns = dp(i+1, target-k*candidates[i])
                #print('subAns({0},{1}) = {2}'.format(i+1, target-k*candidates[i], subAns))
                for subList in subAns:
                    #print(subList)
                    ans.append(k*[candidates[i]] + subList)
            memo[(i,target)] = ans
            #print('dp({0}, {1}) --> {2}'.format(i,target, ans))
            return ans

        return dp(0,target)

if __name__ == '__main__':    

    sln   = Solution()

    print('\nTestcase1...')
    candidates = [2,3,6,7]
    target = 7
    print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))
    print('result = {0}'.format(sln.combinationSum(candidates, target)))

    candidates = [2]
    target = 2
    print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))    
    print('result = {0}'.format(sln.combinationSum(candidates, target)))

    print('\nTestcase2...')
    candidates = [2,3,5]
    target = 8
    print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))    
    print('result = {0}'.format(sln.combinationSum(candidates, target)))

    print('\nTestcase3...')
    candidates = []
    target = 7
    print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))    
    print('result = {0}'.format(sln.combinationSum(candidates, target)))

    print('\nTestcase4...')
    candidates = [2]
    target = 12
    print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))    
    print('result = {0}'.format(sln.combinationSum(candidates, target)))

    print('\nTestcase5...')
    # Generate 'n' unique random numbers within a range        
    # tmp = []
    # for i in range(10):
    #     tmp.append(random.randint(1,10))
    # candidates = list(set(tmp))
    # random.shuffle(candidates)
    # The random.sample() function returns a k length list of unique elements 
    # chosen from the list, sequence or set, used for random sampling without 
    # replacement.
    N = 30
    candidates = random.sample(range(1,2*N), N)

    target = random.randint(N,2*N)
    print(candidates, target)       
    tStart = time.time()        
    #print('result = {0}'.format(sln.combinationSum(candidates, target)))
    print('number of combinations = {0}'.format(len(sln.combinationSum(candidates, target))))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')

    tStart = time.time()        
    #print('result = {0}'.format(sln.combinationSumRecursive(candidates, target)))    
    print('number of combinations = {0}'.format(len(sln.combinationSumRecursive(candidates, target))))
    tElapsed = time.time() - tStart        
    print('tElapsed = ', tElapsed, ' (sec)')    