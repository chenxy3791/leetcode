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
#include <iostream>
#include <vector>
using namespace std;

class MyCircularQueue {
    private:
        // store elements
        int* data;       
        // pointers to indicate the head and tail position
        int size;
        int head;                
        int tail;
        int dCnt;
    public:
        /** Initialize your data structure here. Set the size of the queue to be k. */
        MyCircularQueue(int k) {            
            data = new int[k];
            size = k;
            head = 0;
            tail = 0;
            dCnt = 0;
        }
        
        /** Insert an element into the circular queue. Return true if the operation is successful. */
        bool enQueue(int value) {
            //cout << "enQueue()..."<<endl;
            if (isFull()) {
                return false;
            }
            if (isEmpty()){
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
        bool deQueue() {
            //cout << "deQueue()..."<<endl;
            if (isEmpty()) {
                return false;
            }            
            head = (head+1)%size;
            dCnt--; 
            return true;            
        }
        
        /** Get the front item from the queue. */
        int Front() {
            if (isEmpty()) return -1;
            return data[head];
        }
        
        /** Get the last item from the queue. */
        int Rear() {
            //cout << "Rear()..." << endl;
            //cout << "tail = "<< tail<< " data[tail] = " << data[tail] << endl;
            if (isEmpty()) return -1;
            return data[tail];
        }
        
        /** Checks whether the circular queue is empty or not. */
        bool isEmpty() {
            return (dCnt == 0);
        }
        
        /** Checks whether the circular queue is full or not. */
        bool isFull() {
            return (dCnt == size);            
        }
};

class MyCircularQueue_Ref {
private:
    vector<int> data;
    int head;
    int tail;
    int size;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        data.resize(k);
        head = -1;
        tail = -1;
        size = k;
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if (isFull()) {
            return false;
        }
        if (isEmpty()) {
            head = 0;
        }
        tail = (tail + 1) % size;
        data[tail] = value;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if (isEmpty()) {
            return false;
        }
        if (head == tail) {
            head = -1;
            tail = -1;
            return true;
        }
        head = (head + 1) % size;
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if (isEmpty()) {
            return -1;
        }
        return data[head];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if (isEmpty()) {
            return -1;
        }
        return data[tail];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return head == -1;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return ((tail + 1) % size) == head;
    }
};

int main() {
    
    // Testcase 1
    cout << "Testcase 1 start ..." << endl;
    int k = 3;
    int value = 10;
    MyCircularQueue* obj = new MyCircularQueue(3);
    bool param_1 = obj->enQueue(value);
    bool param_2 = obj->deQueue();
    int  param_3 = obj->Front();
    cout << "param_3 == " << param_3 << endl;
    int  param_4 = obj->Rear();
    cout << "param_4 == " << param_4 << endl;
    bool param_5 = obj->isEmpty();
    cout << "param_5 == " << param_5 << endl;
    bool param_6 = obj->isFull();
    cout << "param_6 == " << param_6 << endl;
    cout << "Testcase 1 end ..." << endl;

    // Testcase 2
    cout << endl;
    cout << "Testcase 2 start ..." << endl;
    MyCircularQueue* obj1 = new MyCircularQueue(3);
    cout << "obj1->enQueue(1): " << obj1->enQueue(1) << endl;
    cout << "obj1->enQueue(2): " << obj1->enQueue(2) << endl;
    cout << "obj1->enQueue(3): " << obj1->enQueue(3) << endl;
    cout << "obj1->enQueue(4): " << obj1->enQueue(4) << endl;
    cout << "obj1->Rear()    : " << obj1->Rear()     << endl;
    cout << "obj1->isFull()  : " << obj1->isFull()   << endl;
    cout << "obj1->deQueue() : " << obj1->deQueue()  << endl;
    cout << "obj1->enQueue(4): " << obj1->enQueue(4) << endl;
    cout << "obj1->Rear()    : " << obj1->Rear()     << endl;    
    
    // vector<int> *pQueue = new vector[4];
    // cout << "Initial Size: " << pQueue->size() << std::endl;
    // cout << "Initial Capacity: " << pQueue->capacity() << std::endl;

}