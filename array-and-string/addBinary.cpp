/* Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101" 

*/

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        int a_len = a.length();
        int b_len = b.length();

        string strLong;
        string strShort;
        int    lenShort;
        int    lenLong;

        if(a_len >= b_len){
            strLong  = a;
            strShort = b;
            lenLong  = a_len;
            lenShort = b_len;
        }else{
            strLong  = b;
            strShort = a;    
            lenLong  = b_len;
            lenShort = a_len;
        }

        string c;
        int carry = 0;
        int sum   = 0;
        for(int k=0; k<lenShort; k++){
            sum = (strLong[lenLong-k-1] - 48) + (strShort[lenShort-k-1] - 48) + carry;
            if(sum >= 2){
                carry = 1;
                sum  -= 2;
            }else{
                carry = 0;
            }
            c.insert(0,(sum==0)?"0":"1");
        }
        for(int k=lenShort; k<lenLong; k++){
            sum = (strLong[lenLong-k-1] - 48) + carry;
            if(sum >= 2){
                carry = 1;
                sum  -= 2;
            }else{
                carry = 0;
            }
            c.insert(0,(sum==0)?"0":"1");
        }
        // The MSB insert if the final carry is 1.
        if(carry == 1){
            c.insert(0,(carry==0)?"0":"1");
        }

        return c;
    }
};

int main() {
    Solution sln;

    string a, b, c;
    cout << "Testcase 1:" << endl;
    a = "11";
    b = "1";
    c = sln.addBinary(a,b);
    cout << a << "+" << b << "=" << c <<endl;

    cout << "Testcase 2:" << endl;
    a = "110001";
    b = "00011";
    c = sln.addBinary(a,b);
    cout << a << "+" << b << "=" << c <<endl;

    cout << "Testcase 3:" << endl;
    a = "0";
    b = "0";
    c = sln.addBinary(a,b);
    cout << a << "+" << b << "=" << c <<endl;

    cout << "Testcase 3:" << endl;
    a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
    b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
    // Expected: 
    //  "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"
    c = sln.addBinary(a,b);
    cout << a << endl << "+" << endl << b << endl << "=" << endl << c <<endl;

}