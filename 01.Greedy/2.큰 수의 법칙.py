#다양한 수로 이루어진 배열이 있을대 주어진 수들을 M번 더해 가장 큰 수 만드는 법칙
#단, 배열의 특정 인텍스에 해당하는 수가 연속해서 K번 초과해 더해질 수 X

# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# #data에서 가장 큰 2개 뽑기 -> sort로 정렬
# data.sort(reverse=True)
# k1 = data[0]
# k2 = data[1]

# #숫자 더해지는 횟수M
# #가장 큰거 k번 더하고, 2번째거 한번 더하고, 가장 큰거 더하고...
# #8번더하는데 최대3개까지 -> 1,1,1,2,1,1,1,2 ->1번 6개, 2번 2개 ->8/3 = 2, 8%3 = 2, 8-2 = 6
# sum = 0
# sum += k2 * (m%k)
# sum += k1 * (m - (m%k))
# print(sum)


#solution
#반복되는 수열 = k+1
#가장 큰 수가 등장하는 횟수 = int (m / (k+1)) * k + m % (k+1)
n, k, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
k1 = data[0]
k2 = data[1]

#가장 큰 수가 더해지는 횟수
cnt = int(m / (k+1)) * k
cnt += m % (k+1)

result = 0
result += (cnt) * k1
result += (m-cnt) * k2
print(result)