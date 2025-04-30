#2839-설탕배달-브루트포스
# 5/3, 정확하게X -1  5로 최대한 나누고, 3나누고

n = int(input())
cnt = 0

while n>=0:
    if n%5 == 0: 
        cnt += n//5
        print(cnt) 
        break
    n -= 3
    cnt += 1
else:
    print(-1)
    