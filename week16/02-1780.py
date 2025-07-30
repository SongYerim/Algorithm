# 1780 종이의 개수 - 분할정복, 재귀

import sys

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

result = {-1:0, 0:0, 1:0}
#n을 3으로 나눠서 사용해야함
def cut(row, col, n):
    curr = paper[row][col]
    
    for i in range(row, row + n):
        for j in range(col, col + n):
            if paper[i][j] != curr:
                n = n//3
                cut(row, col, n)
                cut(row, col + n, n)
                cut(row, col + (2*n), n)
                cut(row + n, col, n)
                cut(row + n, col + n, n)
                cut(row + n, col + (2*n), n)
                cut(row + (2*n), col, n)
                cut(row + (2*n), col + n, n)
                cut(row + (2*n), col + (2*n), n)    
                return
    result[curr] += 1
    return

cut(0,0,n)

for i in result.values():
    print(i)