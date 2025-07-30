# 10798 세로읽기 - 문자열
import sys

arr = []
for _ in range(5):
    a = sys.stdin.readline().rstrip() #오른쪽 끝 공백 제거
    arr.append(a)

for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')