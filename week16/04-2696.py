# 2696 중앙값 구하기 - 우선순위 큐
# https://dingdingcrong.tistory.com/209


import sys
import heapq

def result():
    n = int(input())
    for _ in range(n):
        heapleft = []
        heapright = []
        mid = []
        m = int(input())
        arr = list(map(int, sys.stdin.readline().split()))
        for i in range(m//10):
            arr += list(map(int, sys.stdin.readline().split()))
            
        # 양쪽 힙의 길이 같으면 왼쪽에,아니면 오른쪽에 push
        for i in range(len(arr)):
            if len(heapleft) == len(heapright):
                heapq.heappush(heapleft, -arr[i])
            else:
                heapq.heappush(heapright, arr[i])
            # 왼쪽 최댓값 > 오른쪽 최솟값  
            if heapright and -heapleft[0] > heapright[0]:
                big = heapq.heappop(heapleft)
                small = heapq.heappop(heapright)
                heapq.heappush(heapleft, -small)
                heapq.heappush(heapright, -big)
                
            if (i+1)%2 == 1:
                mid.append(-heapleft[0])
            
        length = len(mid)
        if length > 10:
            start = 0
            end = 10
            print(length)
            for i in range(length//10):
                print(*mid[start:end])
                start += 10
                end += 10
            else:
                print(*mid[start:])
        else:
            print(length)
            print(*mid)


result()