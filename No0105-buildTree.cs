using System;
using System.Collections.Generic;
using System.Text;

// * Definition for a binary tree node.
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

public class Solution {
    public TreeNode BuildTree(int[] preorder, int[] inorder) {
        // Baseline case handling
        if (inorder.Length == 0){
            return(null);
        }            
        if (inorder.Length == 0){
            TreeNode t = new TreeNode(inorder[0]);
            return(t) ;
        }            

        // Find the index of 'rootval' in inorder.
        int rootVal = preorder[0];        
        int k = Array.IndexOf(inorder,rootVal);
        // sublist generation
        int [] leftInorder  = inorder.SubArray(0,k);
        int [] rightInorder = inorder.SubArray(k+1,end);
        int [] leftPreorder = preorder.SubArray(1,k+1);
        int [] rightPreorder= preorder.SubArray(k+1,end);
        TreeNode root = new TreeNode(rootVal);
        root.left = self.BuildTree(leftPreorder,leftInorder);
        root.right = self.BuildTree(rightPreorder,rightInorder);

        return root;
    }
}