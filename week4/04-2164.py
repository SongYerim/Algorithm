# 2164-카드2

from collections import deque

N = int(input())
queue = deque(range(1, N+1))

while len(queue) > 1:
    queue.popleft() 
    queue.append(queue.popleft()) 

print(queue[0])
#print(queue)출력했더니 deque([4])