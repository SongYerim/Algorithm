# 7785 회사에 있는 사람 - 집합
# import sys

# n = int(input())
# arr = []

# for i in range(n):
#     name, state = map(str, sys.stdin.readline().split())
#     if state == 'enter':
#         arr.append(name) #이름만 출력할거니까 이름만 저장하기
#     else:
#         if name in arr:
#          arr.remove(name)
         
# arr.sort(reverse=True)
# for name in arr:
#     print(name)   

# -> 시간초과
# 원인: list.remove(name) 의 시간복잡도는 O(n)
# arr.remove(name)은 리스트 전체를 순회하면서 name을 찾은 뒤 제거합니다.
# 입력이 최대 1,000,000행(n ≤ 10⁶) 이므로, 매번 O(n)으로 삭제하면 최악의 경우 **O(n²)**의 시간복잡도가 됩니다.


import sys

n = int(input())
arr = set()

for i in range(n):
    name, state = sys.stdin.readline().split()
    if state == 'enter':
        arr.add(name)
    else:
        if name in arr:
            arr.remove(name)
         
for name in sorted(arr, reverse=True):
    print(name)
    
# 시간복잡도
# 각 줄 입력 처리: O(1)
# set.add, set.remove: 평균 O(1)
# 정렬: O(k log k), 여기서 k는 현재 회사에 남아 있는 사람 수 (최대 n)


#딕셔너리를 활용한 풀이도 시간초과를 막을 수 있음