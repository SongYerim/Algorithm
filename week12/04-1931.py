#1931 회의실 배정 - 그리디 알고리즘
import sys

n = int(input()) #회의의 수
array = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    array.append([start, end])

#2차원 배열에서 2번째 값으로 정렬하고 같으면 1번째 값으로 정렬
array.sort(key = lambda x : (x[1], x[0])) 

cnt = 1
end = array[0][1]
for i in range(1,n):
    if array[i][0] >= end:
        end = array[i][1]
        cnt += 1

print(cnt)