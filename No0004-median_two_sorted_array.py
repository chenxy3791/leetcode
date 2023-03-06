'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


需要考虑的情况:
1. 其中一个为空 vs 两者都不为空
2. m + n is odd vs even
3. 两个或者多个数相等的情况呢
    比如说，考虑合并后的数组的情况
    [1,2,3,3,4,5] --> 3
    [1,2,3,3,3,4,5] --> 3
    [1,2,3,4,4,5] --> 3.5
    所以，归根结底就是
        总个数为偶数时，排序后的位置排在中间两个的平均数
        总个数为奇数时，排序后的位置排在正中间的那个数
        不管它（它们）两侧有多少个相等的数
        
[解题思路1]
step1: Merge two arrays, just like the second part of mergesort.
step2: Then find the median of the merged array.
但是这个单merge就是O((m+n))的复杂度了吧。

[解题思路2]
因为两者都是已经排好序的，所以各自的中位数立即就可以得到了。
但是融合中位数与各自的中位数是什么关系呢？
    nums1 = [1,2,3,4,5]
    nums2 = [6,7,8,9,10]
    median = 5.5

case1: 两者覆盖的区间没有交集，即比如说nums1的最小数大于或等于nums1的最大数
    这种情况最简单
case2: 其中一个的覆盖区间包含另外一个
    
case3: 两者的覆盖区间有交集，比如说，nums1的最大值大于nums2的最小值
'''
class Solution:
    #def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # Merge the two sorted arrays first
        idx1 = 0
        idx2 = 0
        merged = []
        len1 = len(nums1)
        len2 = len(nums2)
        while idx1 < len1 and idx2 < len2 :
            if nums1[idx1] <= nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 = idx1 + 1
            else:
                merged.append(nums2[idx2])
                idx2 = idx2 + 1
        if idx1 == len1:
            print('A: ' + 'idx2 = ', idx2, ' merged = ', merged)            
            #merged.append(nums2[idx2:])
            merged = merged + nums2[idx2:]
        if idx2 == len2:    
            print('B: ' + 'idx1 = ', idx1, ' merged = ', merged)
            #merged.append(nums1[idx1:])
            merged = merged + nums1[idx1:]
        print(merged)

        # Find the median of the merged array
        merged_len = len1 + len2
        assert(merged_len == len(merged))
        if merged_len%2 == 1: # Odd number of elements
            median = merged[merged_len//2]
        else:                 # Even number of elements    
            median = (merged[int(merged_len/2)-1] + merged[int(merged_len/2)])/2

        return median

if __name__ == '__main__':

    sln   = Solution()

    # # testcase1
    # nums1 = [1,2,3]
    # nums2 = [4,5,6]
    # print(sln.findMedianSortedArrays(nums1, nums2))

    # # testcase2
    # nums1 = []
    # nums2 = [4,5,6,6,6,7,8]    
    # print(sln.findMedianSortedArrays(nums1, nums2))    

    # # testcase3
    # nums1 = [1,2,3,4]
    # nums2 = [4,5,6]    
    # print(sln.findMedianSortedArrays(nums1, nums2))    

    # # testcase4
    # nums1 = [1,2,3,3]
    # nums2 = [4,5,6]    
    # print(sln.findMedianSortedArrays(nums1, nums2))    

    # # testcase5
    # nums1 = [1,2,3,4,4,5,6,7]
    # nums2 = [3,4,4,6]    
    # print(sln.findMedianSortedArrays(nums1, nums2))        

    # testcase5
    nums1 = [1,2]
    nums2 = [3,4]    
    print(sln.findMedianSortedArrays(nums1, nums2))        