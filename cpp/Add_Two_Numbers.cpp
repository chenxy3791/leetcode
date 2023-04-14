#define _CRT_SECURE_NO_WARNINGS // Must be placed in the very beginning?
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

#include <Afxwin.h>  //--GetPrivateProfileXXX function family needs it. But seems not limited to them! 2016-09-21
//#include <float.h>   //Definition of Limits on floating point constants.
//#include <fpieee.h>
//#include <excpt.h>
//#include <assert.h>
//#include <math.h>
//#include <malloc.h>

/**
 * 2016-09-22
 * 基本验证通过。
 * 但是当前这种验证方式只能验证两个常规数之和。对于超出整型数表示范围的的数的验证需要另外想办法。
 */


/**
 * Definition for singly-linked list.
 * 注意：链表是从高位指向低位的.
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}   //结构体的构造函数。但是为什么不用class呢？
 };
 
class Solution {
public:
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
		ListNode* result = new ListNode(-1);
		ListNode* pre = result;
		ListNode *pa = l1, *pb = l2;
		int carry = 0;
		while (pa != NULL || pb != NULL)
		{
			int av = pa == NULL ? 0 : pa->val;
			int bv = pb == NULL ? 0 : pb->val;
			ListNode* node = new ListNode((av + bv + carry) % 10);
			carry = (av + bv + carry) / 10;
			pre->next = node;
			pre = pre->next;
			pa = pa == NULL ? NULL : pa->next;
			pb = pb == NULL ? NULL : pb->next;
		}
		if (carry > 0)
			pre->next = new ListNode(1);
		pre = result->next;
		delete result;
		return pre;
	}
};

void delay(int t_delay);
ListNode *NumListGen(int number);

void main()
{
	Solution sln;
    for(int i=0; i<10; i++)
    {       
		//生成两个由链表表示的数字
		int num1 = rand();
		int num2 = rand();
		int sum_ref = num1 + num2;

		ListNode* num1_list;
		ListNode* num2_list;
		ListNode* sum_list;
		ListNode* p_cur;

		num1_list = NumListGen(num1);
		num2_list = NumListGen(num2);

		sum_list  = sln.addTwoNumbers(num1_list,num2_list);
		
		//display the operation result.
		cout<<num1<<" + "<<num2<<" = "<<sum_ref<<endl;

		p_cur = sum_list;
		while(p_cur!=NULL)
		{
			cout<<p_cur->val;
			p_cur = p_cur->next;
		}
		cout<<endl;
		
        delay(1);
		//cout<< "one second elapsed!" <<endl;

		delete num1_list;
		delete num2_list;
		delete sum_list;
		delete p_cur;
    }
    
    exit(0);
}

// Delay 't_delay' seconds.
void delay(int t_delay)
{
    time_t start_time, cur_time; // 变量声明 
    time(&start_time); 
    do { 
        time(&cur_time); 
    } while((cur_time - start_time) < t_delay);

    return;
}

ListNode *NumListGen(int number)
{
	//先要将number分解为个位数字串，存储在一个vector中。
	vector<int> digit_array;
	int tmp1;    // 0~9.每次分离出来的个位数
	int tmp2;    // 原输入数右移一位所剩下的数

	tmp2 = number;
	do{
		tmp1 = tmp2%10;
		tmp2 = tmp2/10;
		digit_array.push_back(tmp1); // push_back: Appends a copy of the input to the end
	}while(tmp2>0);

	//构造链表
	//链表要求从低位链接高位（逆序存储），所以对digit_array从头到尾进行搜索就可以了。
	ListNode* lst_head = new ListNode(-1); //结果链表的起始节点，并将作为返回结果指针
	ListNode* p_cur    = lst_head;
	ListNode* p_next;

	int len = digit_array.size();
	p_cur->val = digit_array[0];        //vector可以像普通数组一样寻址
	for(int i = 1; i<len; i++)
	{
		p_next     = new ListNode(-1);  //先生成一个链表节点
		p_cur->next= p_next;            //链接到链表上去
		p_cur      = p_next;            //更新p_cur
		p_cur->val = digit_array[i];    //更新新追加节点的val
	}

	return(lst_head);
}