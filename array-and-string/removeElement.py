""" 
让我们从另一个经典问题开始：

给定一个数组和一个值，原地删除该值的所有实例并返回新的长度。

如果我们没有空间复杂度上的限制，那就更容易了。我们可以初始化一个新的数组来存储答案。如果元素不等于给定的目标值，则迭代原始数组并将元素添加到新的数组中。

实际上，它相当于使用了两个指针，一个用于原始数组的迭代，另一个总是指向新数组的最后一个位置。


重新考虑空间限制
现在让我们重新考虑空间受到限制的情况。 

我们可以采用类似的策略，我们继续使用两个指针：一个仍然用于迭代，而第二个指针总是指向下一次添加的位置。 

总结二
这是你需要使用双指针技巧的一种非常常见的情况：同时有一个慢指针和一个快指针。
解决这类问题的关键是:确定两个指针的移动策略。
与前一个场景类似，你有时可能需要在使用双指针技巧之前对数组进行排序，也可能需要运用贪心想法来决定你的运动策略。

总结一
总之，使用双指针技巧的典型场景之一是你想要从两端向中间迭代数组。
这时你可以使用双指针技巧：一个指针从始端开始，而另一个指针从末端开始。
值得注意的是，这种技巧经常在排序数组中使用。

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,
Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
Note that the order of those five elements can be arbitrary.
It doesn't matter what values are set beyond the returned length.
Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.
Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""
import time

class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def removeElement(self, numbers, target):
        nNums = len(numbers)

        # Ignore the validity check, assuming the valid input data.

        rPtr = 0
        wPtr = 0

        while rPtr < nNums:
            print(rPtr, wPtr)            
            if numbers[rPtr] != target:
                #print('Successful: ', fPtr, bPtr)
                numbers[wPtr] = numbers[rPtr]
                wPtr = wPtr + 1            
            rPtr = rPtr + 1
        
        #print(numbers[0:wPtr])
        return wPtr

if __name__ == '__main__':

    sln   = Solution()

    # Testcase1
    print('Testcase1...')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 2
    print(sln.removeElement(nums, target))    

    # Testcase1
    print('Testcase1...')
    nums = [0,1,2,2,3,0,4,2]
    target = 2
    print(sln.removeElement(nums, target))    
