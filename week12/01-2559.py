#2559 수열 - 누적합

# n, k = map(int, input().split())
# list = list(map(int, input().split()))
# max_value = [0] * n

# for i in range(len(list)-k + 1):
#     sum = 0
#     for j in range(k):
#         sum += list[i+j]
#     max_value[i] = sum
    
# print(max(max_value))

#시간 초과 - 시간복잡도 O(n^2)
#반복문을 한번만 돌면서 합을 저장하기
#첫번째 연속합 구하고, 다음부터는 맨앞에 원소 빼고 맨뒤의 원소 더하기

n, k = map(int, input().split())
number = list(map(int, input().split()))
max_value = []
max_value.append(sum(number[:k]))

for i in range(n - k):
    max_value.append(max_value[i] - number[i] + number[k+i])
    
print(max(max_value))