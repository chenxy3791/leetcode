Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
回文字符串有两种情况，一种是长度为奇数，一种是长度偶数
对每个字符位置，分别假定它是某个奇数长度回文子字符串的的中心和假定它是偶数长度回文子字符串的左中心，搜索所能得到的最大长度的回文子字符串。
注意奇数长度回文子字符串的长度最小为1，偶数的最小长度则为0
然后比较各字符位置所能得到的最大长度，得到最终的最大长度。

中间不存储所得到的回文子字符串，最后根据字符位置，回文子字符串类型（奇数长度还是偶数长度）以及长度，恢复出最终的最大长度回文子字符串