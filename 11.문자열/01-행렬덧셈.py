# 2738 행렬 덧셈 - 문자열
import sys

n, m = map(int, input().split())

a = []
b = []
for _ in range(n):
    aa = sys.stdin.readline().split()
    a.append(aa)
for _ in range(n):
    bb = sys.stdin.readline().split()
    b.append(bb)
    
c = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        result = int(a[i][j]) + int(b[i][j])
        print(result, end =' ')
    print()