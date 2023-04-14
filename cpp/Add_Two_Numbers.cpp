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
 * ������֤ͨ����
 * ���ǵ�ǰ������֤��ʽֻ����֤����������֮�͡����ڳ�����������ʾ��Χ�ĵ�������֤��Ҫ������취��
 */


/**
 * Definition for singly-linked list.
 * ע�⣺�����ǴӸ�λָ���λ��.
 */
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}   //�ṹ��Ĺ��캯��������Ϊʲô����class�أ�
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
		//���������������ʾ������
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
    time_t start_time, cur_time; // �������� 
    time(&start_time); 
    do { 
        time(&cur_time); 
    } while((cur_time - start_time) < t_delay);

    return;
}

ListNode *NumListGen(int number)
{
	//��Ҫ��number�ֽ�Ϊ��λ���ִ����洢��һ��vector�С�
	vector<int> digit_array;
	int tmp1;    // 0~9.ÿ�η�������ĸ�λ��
	int tmp2;    // ԭ����������һλ��ʣ�µ���

	tmp2 = number;
	do{
		tmp1 = tmp2%10;
		tmp2 = tmp2/10;
		digit_array.push_back(tmp1); // push_back: Appends a copy of the input to the end
	}while(tmp2>0);

	//��������
	//����Ҫ��ӵ�λ���Ӹ�λ������洢�������Զ�digit_array��ͷ��β���������Ϳ����ˡ�
	ListNode* lst_head = new ListNode(-1); //����������ʼ�ڵ㣬������Ϊ���ؽ��ָ��
	ListNode* p_cur    = lst_head;
	ListNode* p_next;

	int len = digit_array.size();
	p_cur->val = digit_array[0];        //vector��������ͨ����һ��Ѱַ
	for(int i = 1; i<len; i++)
	{
		p_next     = new ListNode(-1);  //������һ������ڵ�
		p_cur->next= p_next;            //���ӵ�������ȥ
		p_cur      = p_next;            //����p_cur
		p_cur->val = digit_array[i];    //������׷�ӽڵ��val
	}

	return(lst_head);
}