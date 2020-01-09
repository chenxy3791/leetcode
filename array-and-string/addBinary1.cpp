/* Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101" 

Fail for two long input string: The lower bits don't match with the expected output. To be investigated.
    a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
    b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
    // Expected: 
    //  "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"
*/

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    // The return-value is in fact an integer, but we use double to extend the representation range
    double str2int(string x){        
        int nbits = x.length();
        cout << "nbits = "<< nbits <<endl;
        double x_int = 0;
        for(int k=0; k < nbits; k++){
            x_int += pow(2,(nbits-k-1))*(x[k]-48);
        }
        return(x_int);
    }

    // The input 'x' is in fact an integer, but we use double to extend the representation range
    string int2str(double x){
        int nbits;
        if(x == 0){
            nbits = 1;
        }else{
            nbits = floor(log2(x)) + 1; // Not exactly equal to ceil()!
        }
        
        cout << "nbits = "<< nbits <<endl;

        string x_str;
        int y;
        for(int k=0; k<nbits; k++){
            double x_half = floor(x/2);
            y = x - 2*x_half;
            x_str.insert(0,(y==0)?"0":"1");
            x = x_half;
        }
        return(x_str);
    }

    string addBinary(string a, string b) {
        double a_int = str2int(a);
        double b_int = str2int(b);
        double c_int = a_int + b_int;
        cout << "a_int = "<< a_int <<endl;
        cout << "b_int = "<< b_int <<endl;
        cout << "c_int = "<< c_int <<endl;

        string c_str = int2str(c_int);
        return c_str;
    }
};

int main() {
    Solution sln;

/*     // Test str2int();
    string a = "11";
    double a_int = sln.str2int(a);
    cout << "a = "<< a <<endl;
    cout << "a_int = "<< a_int <<endl;

    a = "11001110";
    a_int = sln.str2int(a);
    cout << "a = "<< a <<endl;
    cout << "a_int = "<< a_int <<endl;

    a = "10000000000";
    a_int = sln.str2int(a);
    cout << "a = "<< a <<endl;
    cout << "a_int = "<< a_int <<endl;

    // Test int2str();
    int x = 1024;
    string x_str = sln.int2str(x);
    cout << "x = "<< x <<endl;
    cout << "x_str = "<< x_str <<endl;    

    x = 102;
    x_str = sln.int2str(x);
    cout << "x = "<< x <<endl;
    cout << "x_str = "<< x_str <<endl;     */

    string a, b, c;
    // cout << "Testcase 1:" << endl;
    // a = "11";
    // b = "1";
    // c = sln.addBinary(a,b);
    // cout << a << "+" << b << "=" << c <<endl;

    // cout << "Testcase 2:" << endl;
    // a = "110001";
    // b = "00011";
    // c = sln.addBinary(a,b);
    // cout << a << "+" << b << "=" << c <<endl;

    // cout << "Testcase 3:" << endl;
    // a = "0";
    // b = "0";
    // c = sln.addBinary(a,b);
    // cout << a << "+" << b << "=" << c <<endl;

    cout << "Testcase 3:" << endl;
    a = "10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101";
    b = "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011";
    // Expected: 
    //  "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"
    c = sln.addBinary(a,b);
    cout << a << endl << "+" << endl << b << endl << "=" << endl << c <<endl;

}