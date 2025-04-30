# 24511-queuestack

import sys
from collections import deque

n = int(sys.stdin.readline()) #자료구조 개수
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queue = deque([])
for i in range(n):
    if A[i] == 0:
        queue.append(B[i])

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(m):
    queue.appendleft(C[i])
    print(queue.pop(), end= ' ')