#1912-연속합-동적계획법

n = int(input())
x =  list(map(int, input().split()))

for i in range(1, n):
    x[i] = max(x[i], x[i] + x[i-1])
    
print(max(x))