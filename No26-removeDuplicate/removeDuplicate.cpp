#include <iostream>
#include <vector>

class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        int foundDuplicate;

        if(nums.size()==0) return(0);

        int wrPtr = 1;
        
        for(int rdPtr = 1; rdPtr<nums.size(); rdPtr++){
            //printf("rdPtr=%d, nums[rdPtr]=%d wrPtr=%d\n",rdPtr, nums[rdPtr],wrPtr);
            foundDuplicate = 0;
            for(int k=0;k<wrPtr;k++){
                if(nums[k] == nums[rdPtr]){
                    //printf("Found duplicate\n");
                    foundDuplicate = 1;
                    break;
                }
            }
            if((0==foundDuplicate)){
                //printf("Not found duplicate\n");
                nums[wrPtr] = nums[rdPtr];
                wrPtr++;
            }
        }
        return(wrPtr);
    }
};

int main() {
    
    Solution sln;
    
    std::vector<int> nums = {1,1,2};
    for(int k=0; k<nums.size(); k++){
        std::cout << nums[k] << '\n';
    }
    
    int newLen = sln.removeDuplicates(nums);
        
    std::cout << "newLen = " << newLen << '\n';
}
