# 1149-RGB거리

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = rgb[0] #첫행 넣어주기 - i에서 i-1과 비교하니까

for i in range(1,n): #i-1행의 열들 중 최솟값 + 현재 비용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[n-1]))
