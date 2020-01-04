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