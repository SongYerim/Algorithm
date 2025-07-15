# 9461 파도반 수열 - 동적계획법

n = int(input())

for i in range(n):
    p = int(input())
    dp = [0] * p
    for j in range(p):
        if j <= 2:
            dp[j] = 1
        elif j == 3 or j == 4:
            dp[j] = 2
        else:
            dp[j] = dp[j-2] + dp[j-3]
    print(dp[j])

# 1 1 1
# 2 2
# 3 =2+1
# 4 =2+2
# 5 =3+2
# 7 =4+3
# 9 =5+4
# 5번까지는 예외 나머지는 2개앞+3개앞