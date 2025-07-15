# 1927 최소 힙 - 우선순위 큐, 힙
import sys
import heapq

n = int(sys.stdin.readline())
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    
    if num > 0:
        heapq.heappush(min_heap, num)
    else:
        if not min_heap:
            print(0)
        else:
            print(heapq.heappop(min_heap))