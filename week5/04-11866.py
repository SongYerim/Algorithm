# 11866-요세푸스 문제 - 자료구조 queue
import sys
from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1,n+1)])
# list = list(range(1,n+1))
ans = []

while len(queue) != 0:
    for _ in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())
    
print("<", ", ".join(map(str,ans)), ">", sep="")
    
#정답 띄어쓰기 주의