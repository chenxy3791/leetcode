# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:42:34 2022

@author: Dell
"""

class Solution:
    def winnerOfGame1(self, colors: str) -> bool:

        memo = dict()
        def dp(player:str, game:str) -> bool:
            # player: 'A'; 'B'
            # print(player, game)
            if game in memo:
                return memo[game]
            # Baseline case
            if len(game) < 3:
                return False if player=='A' else True

            # Search for possible action
            action =[]
            cnt    = 0
            for k,c in enumerate(game):
                if c != player:
                    cnt  = 0
                else:
                    if cnt == 0:
                        cnt += 1
                    elif cnt == 1:
                        cnt += 1
                    else:
                        action.append(k - 1)
            # No action can be taken
            # print(action)
            if len(action) == 0:
                ret = not (player == 'A')
                memo[game] = ret
                return ret                
            # Traverse all possible actions
            for k in range(len(action)):
                nxtplayer = 'A' if player == 'B' else 'B'
                nxtgame   = game[:action[k]-1] + game[action[k]:]
                ret = dp(nxtplayer, nxtgame)
                memo[nxtgame] = ret
                return ret
            # Coming here indicates A lose the current game
            memo[game] = False
            return False

        return dp('A',colors)

    def winnerOfGame2(self, colors: str) -> bool:
        def actionSearch(player):
            # Search for possible action 
            num_action = 0
            cnt    = 0
            for k,c in enumerate(colors):
                if c != player:
                    cnt  = 0
                else:
                    if cnt == 0:
                        cnt += 1
                    elif cnt == 1:
                        cnt += 1
                    else:
                        num_action += 1    
            return num_action
        A_action = actionSearch('A')
        B_action = actionSearch('B')
        
        return A_action > B_action 
    
if __name__ == '__main__':
    
    sln = Solution()
    colors = "ABBBBBBBAAA"
    print(sln.winnerOfGame1(colors))
    print(sln.winnerOfGame2(colors))
    
    colors = "AA"
    print(sln.winnerOfGame1(colors))
    print(sln.winnerOfGame2(colors))    
    
    colors = "AAABABB"
    print(sln.winnerOfGame1(colors))       
    print(sln.winnerOfGame2(colors))
    
    colors = "AAAAAAAAAAAAAAAAAAAAAAAABABBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    print(sln.winnerOfGame1(colors))       
    print(sln.winnerOfGame2(colors))
    
    colors = 1000*'A' + 176*'B'    
    print(sln.winnerOfGame1(colors))
    print(sln.winnerOfGame2(colors))