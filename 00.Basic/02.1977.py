# 1977 완전제곱수 - 브루트포스

m = int(input())
n = int(input())
# m <= x <= n (1~100)

sum=0
for i in range(100,0,-1):
    print(i)
    if ((i*i) <= n) and ((i*i) >= m):
        min_v = (i*i)
        sum += min_v
                
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min_v)
    
#범위 확인 잘하기