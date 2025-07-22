# 11286 절댓값 힙 - 우선순위 큐, 힙

# heappush heappop
# heapq.heapify(lst)	            리스트를 힙 구조로 변환
# heapq.heappush(heap, item)	    힙에 원소 추가
# heapq.heappop(heap)	            힙에서 가장 작은 원소 제거 후 반환
# heapq.heappushpop(heap, item)	원소 추가 후 가장 작은 원소 제거
# heapq.heapreplace(heap, item)	가장 작은 원소 제거 후 새 원소 추가
# heapq.nlargest(n, iterable)	    가장 큰 n개 원소 반환 (힙 아님)
# heapq.nsmallest(n, iterable)	가장 작은 n개 원소 반환 (힙 아님)

import heapq

n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    if x == 0 :
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)     
    else:
        heapq.heappush(heap, (abs(x),x))
        
#(abs(x), x)형태의 튜플: 절댓값 기준으로 정렬되면서, 절댓값이 같을 경우 원래 값의 크기로 정렬
# ->  (3, -3)형태로 출력 -> 출력 시에는 두 번째 값인 x만 출력

