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