# 동전0 - 그리디
import sys

n, k = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True) #큰수부터 해결

sum = 0
for i in coin:
    sum += k//i
    k %= i

print(sum)
    
#동전이 k보다 작을때부터 카운트 -> 크면 몫이 0으로 나오니 상관없음
#빼주기 / 나누기 / 정수 나누기
#k값에서 나눈만큼 빼주기