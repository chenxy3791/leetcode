#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
2021-03-16
执行结果：通过显示详情
执行用时：72 ms, 在所有 C++ 提交中击败了37.57%的用户
内存消耗：22.4 MB, 在所有 C++ 提交中击败了78.67%的用户
*/
class Solution {
public:
    int findRepeatNumber(vector<int>& nums) {
        int len = nums.size();
        if(len <= 1) {
            return INT_MAX; // Represent invalid output, no repeat number found
        }

        sort(nums.begin(),nums.end());

        for(int k = 0; k < len - 1 ; k ++){
            if(nums[k] == nums[k+1]) {
                return nums[k];
            }
        }
        return INT_MAX;
    }
};

int main(){
    Solution sln;

    vector<int> a{2, 3, 1, 0, 2, 5, 3};
    int b = sln.findRepeatNumber(a);
    //cout << "Input = " << a << endl;
    cout << "Ans = " << b << endl;
}