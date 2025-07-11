# 완전탐색 brute force
n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

#하루=86,400초 / 전체 개수도 86,400 < 100,000 이므로 단순히 1씩 증가해 3을 찾아도 제한시간 안에 풀이 가능