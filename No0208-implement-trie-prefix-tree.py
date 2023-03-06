# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 07:36:14 2021

@author: chenxy

208. 实现 Trie (前缀树)
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
"""

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        k0 = 0
        matchFlg = True
        for k in range(len(word)):
            if word[k] in p:
                p = p[word[k]]
            else:
                matchFlg = False
                k0 = k
                break
        if matchFlg is False:
            for k in range(k0,len(word)):
                p[word[k]] = dict()
                p = p[word[k]]
            p[''] = None # Add termination
        else:
            if '' in p:
                # Nothing to do
                return
            else:
                # Add termination
                p[''] = None
                return
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        matchFlg = True
        for k in range(len(word)):
            if word[k] in p:
                p = p[word[k]]
            else:
                matchFlg = False
                break
        if matchFlg is False:
            return False
        else:
            if '' in p:
                return True
            else:
                return False            

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        matchFlg = True
        for k in range(len(prefix)):
            if prefix[k] in p:
                p = p[prefix[k]]
            else:
                matchFlg = False
                break
        return matchFlg

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':        
    import time
    import random
    
    obj = Trie()
    obj.insert('apple')
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    obj.insert('app')
    print(obj.search('app'))
    print(obj.startsWith('app'))    