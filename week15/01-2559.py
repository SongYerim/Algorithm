#2559 수열 - 누적합
import sys
n, m = map(int, input().split())

arr = list(map(int, sys.stdin.readline().split()))

max_v = []
sum = 0
for i in range(m):
    sum += arr[i]
max_v.append(sum)
# max_value.append(sum(number[:k]))

for i in range(1, n - m + 1): 
    sum = sum - arr[i-1] + arr[i + m -1]
    max_v.append(sum)

print(max(max_v))   
