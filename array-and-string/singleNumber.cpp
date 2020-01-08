#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        if(nums.size()%2 == 0){
            printf("Warning: the input array must be odd size!\n");
            return(-1);
        }
        if(nums.size() == 1){
            return(nums[0]);
        }

        // Sort the input array first
        sort(nums.begin(), nums.end());

        int k = 0;
        while(k < nums.size()-2){
            if(nums[k] != nums[k+1]){
                return(nums[k]);
            }else{
                k = k + 2;
            }
        }
        return(nums.back());
    }
};

int main() {
    
    Solution sln;
    
    //std::vector<int> nums = {1,1,2};
    std::vector<int> nums = {2,1,2};
    for(int k=0; k<nums.size(); k++){
        std::cout << nums[k] << ", ";
    }
    std::cout << endl;
    
    int single = sln.singleNumber(nums);
        
    std::cout << "single = " << single << endl;
}
