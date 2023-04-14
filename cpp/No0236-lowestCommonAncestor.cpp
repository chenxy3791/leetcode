/* """ 
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
""" */
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    std::vector<TreeNode> dfs(TreeNode* root, TreeNode* target){
        cout << root.val << ";\t" << target.val << endl;
        std::vector<TreeNode> tNodeArray;
        if(root.val == target.val){
            tNodeArray.push_back(target);
        }
        else if(root.left != NULL){
            std::vector<TreeNode>* tmp = dfs(root.left, target);
            if(tmp.size() > 0){
                tNodeArray.push_back(root);
                tNodeArray.insert( tNodeArray.end(), tmp.begin(), tmp.end() );
            }
        }
        else if(root.right != NULL){
            std::vector<TreeNode>* tmp = dfs(root.right, target);
            if(tmp.size() > 0){
                tNodeArray.push_back(root);
                tNodeArray.insert( tNodeArray.end(), tmp.begin(), tmp.end() );
                return tNodeArray;
            }
        }        
        return tNodeArray;
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q){
        if((root == NULL) || (p == NULL) || (q == NULL)){
            return NULL;
        }

        pTmp = dfs(root,p);
        qTmp = dfs(root,q);

        int　k = 0;
        while((k < pTmp.size()) && k < qTmp.size()){
            // Assuming the node value are all unique
            if (pTmp[k].val == qTmp[k].val){
                k += 1;
            }else{
                break;
            }
        }

        if (k == 0){
            return NULL;
        }else{
            return qTmp[k-1];
        }
    }
};

int main() {
    
    Solution sln;

    std::vector<char> charArray;

    // Testcase 0
    printf("Testcase0...\n");
    // char test0[] = {};
    // std::vector<char> charArray0(test0, test0 + sizeof(test0)/sizeof(*test0));
    // //charArray0.pop_back();
    // sln.reverseString(charArray0);
    // for(int k=0; k<charArray0.size(); k++){
    //     std::cout << charArray0[k] << ", ";
    // }
    // std::cout << endl;

}
