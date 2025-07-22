# 13550 주유소 - 그리디알고리즘
import sys

n = int(input())
load = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

#마지막 도시 제외 앞에 n-1개 중에서 작은 가격이 더 많은 리터 배정
#처음은 무조건 1번 이용해 다음으로 이동
# sum = load[0] * price[0]
# load = load[1:n]
# price = price[1:-1]
# for i in range(n-1):
#     if price[i] == min(price):#처음부터 끝까지 다 곱해기
#         for j in range(i, n-2):
#             sum += load[j] * price[i]
#         break
#     else:
#         sum += load[i] * price[i]
# print(sum)

min_v = price[0]
sum = 0
for i in range(n-1):
    if price[i] < min_v:
        min_v = price[i]
    
    sum += (min_v * load[i])
print(sum)