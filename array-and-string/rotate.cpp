/* 
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space? 

NOTE:
Don't forget the case that k may be larger than the length of the input array.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    // Judge by leetcode as 'surpassing the time limit'
    void rotate(vector<int>& nums, int k) {
        std::vector<int>::iterator it;
        int lastVal;
        for(int j=0; j<k; j++){
            it = nums.begin();
            lastVal = nums.back();
            nums.pop_back();
            nums.insert(it,lastVal);
        }
        return;
    }

    void rotate1(vector<int>& nums, int k) {
        std::vector<int>::iterator it;
        int nLen = nums.size();
        k = k % nLen;
        if(k <= nLen/2){ // right shift
            cout << "normal right shift" << endl;
            int lastVal;
            for(int j=0; j<k; j++){
                it = nums.begin();
                lastVal = nums.back();
                nums.pop_back();
                nums.insert(it,lastVal);
            }
        }else{  // left shift
            cout << "equivalent left shift" << endl;
            k = nLen - k;
            int firstVal;
            for(int j=0; j<k; j++){                                
                firstVal = nums[0];
                cout << "j = " << j << ", firstVal = " << firstVal <<endl;
                nums.erase(nums.begin());
                nums.push_back(firstVal);
            }
        }

        return;
    }

};

int main() {
    
    printf("Start...\n");

    Solution sln;
    int k;
    
    std::vector<int> nums = {1,2,3,4,5,6,7};
    
    printf("Calling sln.rotate()...Start\n");
    sln.rotate(nums,4);
    printf("Calling sln.rotate()...End\n");

    for(int l=0;l<nums.size();l++){
        std::cout << "nums[*] = " << nums[l] << '\n';        
    }

    // Testcase1
    printf("Testcase1...Start\n");
    std::vector<int> nums1 = {1,2,3,4,5,6,7};    
    sln.rotate1(nums1,4);

    for(int l=0;l<nums1.size();l++){
        std::cout << "nums1[*] = " << nums1[l] << '\n';        
    }
    printf("Testcase1...End\n");

    // Testcase2
    printf("Testcase2...Start\n");
    std::vector<int> nums2 = {1,2,3};    
    k = 15;
    sln.rotate1(nums2,k);

    for(int l=0;l<nums2.size();l++){
        std::cout << "nums2[*] = " << nums2[l] << '\n';        
    }
    printf("Testcase2...End\n");

}