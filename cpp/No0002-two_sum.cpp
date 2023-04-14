/**
2019-12-20. chenxy
    
题目描述：    
    给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。    
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。    
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    
    示例：
    
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
    
    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/add-two-numbers
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。        
*/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *sum = new ListNode(0);                
        ListNode *curPtr = sum;

        // Assuming neither l1 nor l2 is empty list.
        int carry = 0;
        int add1 = l1->val;
        int add2 = l2->val;
        bool l1_end = 0;
        bool l2_end = 0;

        while(1){
            
            int sum_tmp  = add1 + add2 + carry;
            printf("sum_tmp = %d\n", sum_tmp);
            if(sum_tmp < 10){
                curPtr->val = sum_tmp;
                carry = 0;
            }else{
                curPtr->val = sum_tmp - 10;
                carry = 1;                
            }         

            if(NULL != l1->next){
                l1   = l1->next;
                add1 = l1->val;
            }else{
                add1 = 0;
                l1_end = 1;
            }

            if(NULL != l2->next){
                l2   = l2->next;
                add2 = l2->val;
            }else{
                add2 = 0;
                l2_end = 1;
            }

            if(l1_end && l2_end && (0==carry)){
                break;
            }else{
                curPtr->next = new ListNode(0);   
                curPtr = curPtr->next;
            }
        }
        return(sum);
    }
};