# 24416-알고리즘 수업 피보나치 수1 -동적계획법

#재귀
def fib(n):
    # if n==1 or n==2:
    #     return 1
    # else:
    #     return (fib(n-1) + fib(n-2))
    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[i]

#다이나믹 프로그래밍
def fibonacci(n): #실행횟수
    f = [0] * (n+1)
    f[1] = f[2] = 1
    cnt = 0
    for i in range(3,n+1):
        cnt += 1
        f[i] = f[i-1] + f[i-2]
    return cnt

n = int(input())
print(fib(n), fibonacci(n))