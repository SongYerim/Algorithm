#11053-가장 긴 증가하는 부분 / 동적계획법
#최장 증가 부분 수열(LIS: Longest Increasing Subsequence)

# n = int(input())
# list = list(map(int, input().split()))

# x = list[0]
# cnt = 1
# for i in range(n):
#     if list[i] > x:
#         cnt += 1
#         x = list[i]
        
# print(cnt)

#시간복잡도 = O(n)

# 틀렸다고 뜸 -> 내가 푼거는 무조건 첫번째 숫자를 기준을 증가 부분 수열을 구함
# 근데 꼭 첫번째 숫자가 기준이 아니라 중간에 작은 숫자중에도 기준이 돼서 증가하는 부분 수열을 이룰 수  있음
# 완전 탐색으로 풀경우 시간 복잡도 O(n^2)이 나옴
# 2번째부터 본인보다 앞에 작은 숫자가 몇개인지 카운트 -> max값 구하기

# 다른 테스트케이스 확인

n = int(input())
arr = list(map(int, input().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
