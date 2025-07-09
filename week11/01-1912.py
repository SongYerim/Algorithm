#1912-연속합 / 동적계획법

# n = int(input())
# list = list(map(int, input().split())) 

# max_value = -1e9 #
# for i in range(0, len(list)):
#     sum = list[i]
#     max_value = max(sum, max_value)
#     for j in range(i+1, len(list)):
#         sum += list[j]
#         max_value = max(sum, max_value)
        
# print(max_value)
        
# 연속된 몇개의 수를 선택해 구할 수 있는 합 중 가장 큰 합 구하기
# 처음부터 더해가며 저장했다가 max만나면 바꾸기 -> 시간 초과 = 완전 탐색색
# 시간 초과를 어떻게 해결해야 할까? + dp를 사용해야함 -> 어떤 값을 저장하면 좋을까??
# 내가 짠 코드의 시간 복잡도 = O(n^2)이다.


# 그러면 시간 복잡도를 O(n)으로 줄여보자
# 리스트를 한번만 거쳐가는데, 본인만 들어갈 수도 있으니 연속합과, 본인값 중에 max값을 고른다.
# 본인 위치 기준 최대 연속합 = 이전 연속합과 더하거나 / 더하지 않거나(본인) 2중 하나
# dp[i] = i번째 위치에서의 최대 연속합

n = int(input())
list = list(map(int, input().split())) 

for i in range(1, n):
    list[i] = max(list[i] + list[i-1], list[i])
    
print(max(list))
    
       

