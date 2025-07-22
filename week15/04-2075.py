# 2075 N번째 큰 수 - 우선순위 큐
# import sys, heapq

# n = int(input())
# arr = [[0 for col in range(n)] for row in range(n)]

# for i in range(n):
#     arr[i] = list(map(int, sys.stdin.readline().split()))

# heap = []
# for i in range(n):
#     for j in range(n):
#         heapq.heappush(heap, arr[i][j])

# print(heapq.nlargest(n, heap)[n-1])
# 메모리 초과

import sys, heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    for num in arr: #힙의 크기를 n으로 유지
        if len(heap) < n:
            heapq.heappush(heap, num)
        else:
            if num > heap[0]:
                heapq.heappushpop(heap, num)

print(heap[0])