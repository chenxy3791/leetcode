/* 
chenxy, 2021-03-7.

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindorme(string s){
        slen = strlen(s);
        printf("isPalindrome(): slen = %d\n",slen);
        for(int k=0; k<(slen>>1); k++){
            if(s[k] != s[slen-k-1]){
                return false;
            }
        }
        return true;
    }
    vector<vector<string>> partition(string s) { // vector is used to emulate list in python
        vector<vector<string>> par_list;
        slen = strlen(s);
        if(slen == 0){
            return par_list;
        }

        for(int l=1; l<slen+1; l++){ //loop for 0-start palindrome
            string sstr = s.substr(0,l-1));
            if(isPalindrome(sstr) // Inclusive. Different from python
            {
                vector<string> curPartition;                
                curPartition.push_back(sstr);
                if(l == slen){
                    par_list.push_back(curPartition);
                }else{
                    string sstr2 = s.substr(l,end);
                    vector<vector<string>> sub_parlist = partition(sstr2);
                    while(!sub_parlist.empty()){
                        vector<string> subPar = sub_parlist.pop_front();
                        // Concatenate sstr and subPar to form a whole partition to the original input string
                        subPar.push_back(sstr);
                        par_lsit.push_back(subPar);
                    }
                    // Append the new partition to par_list.
                }
            }
        }
        return par_list;
    }
};

int main() {

    Solution sln;

    // Testcase 1
    cout << "Testcase 1 start ..." << endl;    
    string s1 = 'a';
    vector<vector<string>> parList = sln.partition(s1);
    // How to print parList?
    
    // Testcase 2
    cout << "Testcase 2 start ..." << endl;        
    string s2 = 'aab';
    vector<vector<string>> parList = sln.partition(s2);
    // How to print parList?

    // Testcase 3
    cout << "Testcase 3 start ..." << endl;            
    string s3 = 'cdd';
    vector<vector<string>> parList = sln.partition(s3);
    // How to print parList?
}