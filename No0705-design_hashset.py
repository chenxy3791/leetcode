"""
705. Design HashSet
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
 

Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 

Constraints:

0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
 
Follow up: Could you solve the problem without using the built-in HashSet library?

执行用时：160 ms, 在所有 Python3 提交中击败了74.15%的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了55.03%的用户

"""

class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """    
        self.a = set()        

    def add(self, key: int) -> None:
        self.a.add(key)

    def remove(self, key: int) -> None:
        self.a.discard(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.a

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

if __name__ == '__main__':        
            
    myHashSet = MyHashSet()
    myHashSet.add(1)      # set = [1]
    myHashSet.add(2)      # set = [1, 2]
    myHashSet.contains(1) # return True
    myHashSet.contains(3) # return False, (not found)
    myHashSet.add(2)      # set = [1, 2]
    myHashSet.contains(2) # return True
    myHashSet.remove(2)   # set = [1]
    myHashSet.contains(2) # return False, (already removed)

    print(myHashSet.a)

    #["MyHashSet","add","remove","add","contains","add","remove","add","add","add","add"]
    #[[],           [6],     [4], [17],      [14], [14],    [17], [14], [14], [18], [14]]
    #[null,null,null,null,false,null,null,null,null,null,null]
    b = MyHashSet()
    print(b.add(6))      # set = [6]
    print(b.remove(4))   # set = [6]
    print(b.add(17))     # set = [6,17]
    print(b.contains(14))# return False, (not found)
    print(b.add(14))     # set = [6, 17, 14]
    print(b.remove(17))  # set = [6, 14]
    print(b.add(14))     # set = [6, 14]
    print(b.add(14))     # set = [6, 14]
    print(b.add(18))     # set = [6, 14，18]
    print(b.add(14))     # set = [6, 14，18]
