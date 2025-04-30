# 18258-큐2

import sys
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    x = sys.stdin.readline().split()

    if x[0] == 'push':
        queue.append(int(x[1]))

    if x[0] == 'pop': #가장 앞에 있는 정수 빼고, 출력
        if queue:  #값O
            print(queue.popleft())
        else:
            print(-1)

    if x[0] == 'size':  #정수 개수 출력
        print(len(queue))

    if x[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')

    if x[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if x[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
            
#dequeue: 양방향에서 데이터 처리 가능