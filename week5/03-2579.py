# 2579 - 계단 오르기 - DP
import sys

n = int(input())
stair = [0] + [int(sys.stdin.readline()) for _ in range(1, n+1)]
dp = [0]*(n+1)

if n < 2:
    print(stair[n])
else:
    dp[1] = stair[1]
    dp[2] = stair[1]+stair[2]
    for i in range(3, n + 1):
        dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])
    print(dp[n])
    
# dp[1] = stair[1]
# dp[2] = stair[1]+stair[2]
# dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])
# for i in range(4,n+1):
#     dp[i] = max(stair[i]+stair[i-1]+dp[i-3], stair[i]+dp[i-2])

# print(dp[n])
# 런타임 에러 -> pypy3