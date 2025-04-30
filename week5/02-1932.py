# 1932 - 정수 삼각형 DP

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))
    
#2줄부터 내려가며 확인
for i in range(1,n):
    for j in range(i+1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        #위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(up_left, up)
print(max(dp[n-1]))

# 왼쪽 위 / 바로 위 중 max 선택해 더함
#dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j])
