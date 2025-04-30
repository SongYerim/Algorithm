# 28279 - 덱2
import sys
from collections import deque

n = int(input())

deque = deque()
for i in range(n):
    x = list(map(int, sys.stdin.readline().strip().split()))
    if x[0] == 1:
        deque.appendleft(x[1]) #맨앞
    elif x[0] == 2:
        deque.append(x[1])
    elif x[0] == 3:
        print(deque.popleft() if len(deque) else -1) #맨앞 제외 출력
    elif x[0] == 4:
        print(deque.pop() if len(deque) else -1)
    elif x[0] == 5:
        print(len(deque))
    elif x[0] == 6:
        print(0 if len(deque) else 1)
    elif x[0] == 7:
        print(deque[0] if len(deque) else -1)
    else:
        print(deque[-1] if len(deque) else -1)
    