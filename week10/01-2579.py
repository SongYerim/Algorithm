#계단오르기 - 동적계획법
import sys

n = int(input())
stair = [0] + [int(sys.stdin.readline()) for _ in range(1, n+1)]
dp = [0] * (n+1)

if n<2:
    print(stair[n])
else:
    dp[1] = stair[1]
    dp[2] = stair[2]
    for i in range(3,n+1):
        dp[i] = max(stair[i] + stair[i-1]+dp[i-3], stair[i]+dp[i-2])
    print(dp[n])