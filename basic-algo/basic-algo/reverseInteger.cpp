/* 
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
 */

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

class Solution {
public:
    int reverseInteger(int x) {
        if ((x ^ 0x7FFFFFFF) == -1){
            return(0);
        }
        vector<int> digitVec;
        int x_abs = abs(x);
        int rem;

        // Separate into digit array
        while(x_abs > 0){
            //cout << "x_abs = " << x_abs << endl;
            rem   = x_abs%10;
            x_abs = floor(x_abs / 10);
            digitVec.push_back(rem);
        }

        // Reverse and merge into new integer
        int numDigit = digitVec.size();
        int revInt   = 0;
        int cnt      = 0;
        while(digitVec.size() > 0){
            int digit = digitVec.back();
            digitVec.pop_back();
            double curSignificance = pow(10,cnt) * digit; // 'int' is not enough!
            if((0x7FFFFFFF - revInt)>=curSignificance){
                revInt += curSignificance; // Automatically cast back into integer? Should be that
            }else{
                return(0);
            }
            
            //cout << "digit/cnt/revInt = " << digit << ", " << cnt << ", " << revInt << endl; 
            cnt++;
        }        
        return(revInt*((signbit(x)==1)?(-1):(1)));                
    }
};

int main() {
    
    Solution sln;
    int x, y;

    std::vector<char> charArray;

    // Testcase 0
    printf("Testcase0...\n");
    x = 123;
    y = sln.reverseInteger(x);
    std::cout << "x = "<< x << " y = "<< y << endl;

    // Testcase 1
    printf("Testcase1...\n");
    x = 0x80000000;
    y = sln.reverseInteger(x);
    std::cout << "x = "<< x << " y = "<< y << endl;

    // Testcase 2
    printf("Testcase2...\n");
    x = -123;
    y = sln.reverseInteger(x);
    std::cout << "x = "<< x << " y = "<< y << endl;

    // Testcase 3
    printf("Testcase3...\n");
    x = 120;
    y = sln.reverseInteger(x);
    std::cout << "x = "<< x << " y = "<< y << endl;

    // Testcase 4
    printf("Testcase4...\n");
    x = 1534236469;
    y = sln.reverseInteger(x);
    std::cout << "x = "<< x << " y = "<< y << endl;

}