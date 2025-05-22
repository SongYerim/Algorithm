# 구간 합 구하기 - 누적합
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
sum = [0] #리스트 앞에 0을 채워 인덱스 맞춰줌
total = 0

for i in range(n):
    total += num[i]
    sum.append(total)
    
for _ in range(m):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])

#n:수의 개수 / m:합 구해야 하는 횟수 / n개의 수
#구간합: 누적합 - 누적합
#누적합

#python3로 하니 시간초과떠서 pypy3로 돌림