# 14888 연산자 끼워넣기 - 백트랙킹
import sys
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_v = 1e9
max_v = -1e9    

def back(i, now):
    global min_v, max_v, add, sub, mul, div
    if i == n:
        min_v = min(min_v, now)         
        max_v = max(max_v, now)
    else:
        if add > 0:
            add -= 1
            back(i+1, now + data[i])
            add += 1
        if sub > 0 :
            sub -= 1
            back(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            back(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            back(i+1, int(now/data[i]))
            div += 1
back(1, data[0])

print(max_v)
print(min_v)