# 5635 생일 
import sys
n = int(input())

s = []
for _ in range(n):
    name, d, m, y = map(str, sys.stdin.readline().split())
    d, m, y = map(int, (d,m,y))
    s.append([y,m,d,name])
s.sort(reverse=True)
print(s[0][3])
print(s[-1][3])
    