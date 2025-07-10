n, k = map(int, input().split())

cnt = 0
# while(True):
#     if n % k == 0:
#         n = (n//k)
#         cnt += 1
#         # print('1)n:' + str(n))
#     elif n != 1:
#         n -= 1
#         cnt += 1
#         # print('2)n:' + str(n))
#     elif n == 1:
#         break
# print(cnt)
# # 나머지는 n으로 나누어떨어질때만 가능

while n >= k:
    while n %k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1

while n >1:
    n -= 1
    cnt += 1
print(cnt)
