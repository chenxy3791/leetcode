MyQueue: MyQueue.cpp
	g++ -pipe -O2 -std=c++14 MyQueue.cpp -lm
	./a.out

QueueExample: QueueExample.cpp
	g++ -pipe -O2 -std=c++1y QueueExample.cpp -lm
	./a.out

No622_circularQueue: No622_circularQueue.cpp
	g++ -pipe -O2 -std=c++14 No622_circularQueue.cpp -lm
	./a.out

No622_circularQueue_cs: No622_circularQueue.cs
	mcs No622_circularQueue.cs
	./No622_circularQueue.exe

run: a.out
	./a.out

.PHONY:clean
clean: 
	rm a.out
