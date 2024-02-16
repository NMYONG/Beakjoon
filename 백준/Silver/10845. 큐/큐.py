# 10845 : 큐
from collections import deque
import sys

class Queue:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.items.popleft()
        
    def size(self):
        return len(self.items)

    def empty(self):
        if self.is_empty():
            return 1
        else:
            return 0
    
    def front(self):
        if  self.is_empty():
            return -1
        else:
            return self.items[0]
    
    def back(self):
        if self.is_empty():
            return -1
        else:
            return self.items[-1]
        
    def is_empty(self):
        return len(self.items) == 0
    

queue = Queue()

N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        queue.push(int(command[-1]))
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'empty':
        print(queue.empty())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'back':
        print(queue.back())