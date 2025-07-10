#가장 높은 숫자 카드 한장 뽑기
n, m = map(int, input().split())
result = 0

#이중배열
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)