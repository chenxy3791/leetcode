/* 
Design your implementation of the circular queue. The circular queue is a 
linear data structure in which the operations are performed based on FIFO 
(First In First Out) principle and the last position is connected back to 
the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the 
spaces in front of the queue. In a normal queue, once the queue becomes full, 
we cannot insert the next element even if there is a space in front of the 
queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
 

Example:

MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4
 
Note:

All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
*/
using System;
using System.Collections.Generic;

public class MyCircularQueue {
    // store elements
    private int[] data;       
    // pointers to indicate the head and tail position
    private int size;
    private int head;                
    private int tail;
    private int dCnt;

    /** Initialize your data structure here. Set the size of the queue to be k. */
    public MyCircularQueue(int k) {
        data = new int[k];
        size = k;
        head = 0;
        tail = 0;
        dCnt = 0;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    public bool EnQueue(int value) {
        //cout << "enQueue()..."<<endl;
        if (IsFull()) {
            return false;
        }
        if (IsEmpty()){
            tail = 0;
            head = 0;
            data[tail] = value;
        }else{
            tail = (tail+1)%size;                
            data[tail] = value;                
        }
        dCnt++; 
        //cout << "tail = "<< tail << " head = "<< head << " dCnt = "<< dCnt << endl;
        return true;        
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    public bool DeQueue() {
        //cout << "deQueue()..."<<endl;
        if (IsEmpty()) {
            return false;
        }            
        head = (head+1)%size;
        dCnt--; 
        return true;            
    }
    
    /** Get the front item from the queue. */
    public int Front() {
        if (IsEmpty()){
            return -1;
        } 
        return data[head];
    }
    
    /** Get the last item from the queue. */
    public int Rear() {
        if (IsEmpty()){
            return -1;
        } 
        return data[tail];
    }
    
    /** Checks whether the circular queue is empty or not. */
    public bool IsEmpty() {
        return (dCnt == 0);
    }
    
    /** Checks whether the circular queue is full or not. */
    public bool IsFull() {
        return (dCnt == size);            
    }
};

namespace MyVirginProgram {
    class HelloWorld {
        static void Main(string[] args) {
            /* my first program in C# */
            // Console.WriteLine("Hello World");
            // Console.ReadKey();

            Console.WriteLine("Testcase 1 ... ... start");
            MyCircularQueue obj = new MyCircularQueue(3);        
            bool param_1 = obj.EnQueue(10);
            Console.WriteLine("param_1 = {0}", param_1);
            bool param_2 = obj.DeQueue();
            Console.WriteLine("param_2 = {0}", param_2);
            int  param_3 = obj.Front();
            Console.WriteLine("param_3 = {0}", param_3);
            int  param_4 = obj.Rear();
            Console.WriteLine("param_4 = {0}", param_4);
            bool param_5 = obj.IsEmpty();
            Console.WriteLine("param_5 = {0}", param_5);
            bool param_6 = obj.IsFull();
            Console.WriteLine("param_6 = {0}", param_6);
            Console.WriteLine("Testcase 1 ... ... end");
            Console.ReadKey();
      }
   }
}
