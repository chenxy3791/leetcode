/* 
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

NOTE:
Why the initializaion of vector<char> cannot used the format such as {"","",""}?
But vector<int> can. Refer to singleNumber.cpp.
Below, I used a very troublesome way for vector<char>, is there more compact and efficient way?
    
 */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int i = 0;
        int j = s.size()-1;
        while (i<j){
            cout << i << " " << j << endl;
            swap(s[i], s[j]);
            i++;
            j--;

        }
    }
};

int main() {
    
    Solution sln;

    std::vector<char> charArray;

    // Testcase 0
    printf("Testcase0...\n");
    char test0[] = {};
    std::vector<char> charArray0(test0, test0 + sizeof(test0)/sizeof(*test0));
    //charArray0.pop_back();
    sln.reverseString(charArray0);
    for(int k=0; k<charArray0.size(); k++){
        std::cout << charArray0[k] << ", ";
    }
    std::cout << endl;


    // Testcase 1
    printf("Testcase1...\n");
    char test1[] = "Hannah";    
    std::vector<char> charArray1(test1, test1 + sizeof(test1)/sizeof(*test1));
    charArray1.pop_back(); // Remove the last null character
    sln.reverseString(charArray1);
    for(int k=0; k<charArray1.size(); k++){
        std::cout << charArray1[k] << ", ";
    }
    std::cout << endl;

    // Testcase 2
    printf("Testcase2...\n");
    char test2[] = "hello";    
    std::vector<char> charArray2(test2, test2 + sizeof(test2)/sizeof(*test2));    
    charArray2.pop_back(); // Remove the last null character
    sln.reverseString(charArray2);
    for(int k=0; k<charArray2.size(); k++){
        std::cout << charArray2[k] << ", ";
    }
    std::cout << endl;

}
