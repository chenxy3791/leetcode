/*
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int sLen = s.length(); // s.size() is also OK
        int ptr = 0;
        int maxSubStringLen = 0;
        list<char> charset; 
        for(int k=0; k<sLen; k++){
            char newChar = s[k];            
            
            std::list<char>::iterator it = std::find(charset.begin(), charset.end(), newChar);
            if (it == charset.end()){
                std::cout << "Element not found in charset: " <<'\n';
                charset.push_back(newChar);
            }else{
                if(charset.size() > maxSubStringLen){
                    maxSubStringLen = charset.size();
                }
                //erase elements from the begin to the found duplicated element.                
                charset.erase(charset.begin(),++it);
                charset.push_back(newChar);
            }                                
            /*   
            for (auto itr = charset.begin(); 
                itr != charset.end(); itr++) { 
                cout << *itr << " "; 
            }      
            cout << "\n "; 
            */// For debug
        }
        if(charset.size() > maxSubStringLen){
            maxSubStringLen = charset.size();
        }        
        return(maxSubStringLen);
    }
};

/* Testcase
"pweakwbcd"
"abcabcbb"
"bbbbb"
"pwwkew"
/*
// Can we use set class for this problem?
// The key seems to be the use of the return result of set.find(). To be investigated.
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int sLen = s.length(); // s.size() is also OK
        int ptr = 0;
        set<char> charset;
        for(int k=0; k<sLen; k++){
            char newChar = s[k];
            if(charset.find(newChar) >= 0){                
            }else{
                charset.insert(newChar);
            }            
        }
        return(charset.size());
    }
};*/