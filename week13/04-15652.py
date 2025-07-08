# 15652 - 백트래킹

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

# 중복순열 - product
import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())

for x in combinations_with_replacement(map(str, range(1,n+1)), m):
    print(' '.join(x))
    
#dfs로 푸는 방법
# 시작 값이 1,2,3 인 경우에 따라 m의 개수까지 될때까지 현재 값보다 큰 값 넣기
# n, m = map(int, input().split())
 
# s = []
# def dfs(start):
#     if len(s)==m:
#         print(' '.join(map(str,s)))
#         return
    
#     for i in range(start, n+1): 
#         s.append(i)
#         dfs(i)
#         s.pop()
    
# dfs(1)

s = []
def dfs(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()


# #1.순열 Permutation: 순서를 고려해 뽑는 경우
# from itertools import permutations
# n, m= map(int, input().split())
# for x in permutations(map(str, range(1, n+1)), m):
#     print(' '.join(x))
# # 2.조합 combination: 순서를 고려X 뽑는 경우
# from itertools import combinations
# for x in combinations(map(str, range(1, n+1)), m):
#     print(' '.join(x))
# # 3.중복순열 Permutation with Repetition -> Product: 순서를 고려해 뽑는 경우(중복 가능)
# from itertools import product
# for x in product(map(str, range(1, n+1)), repeat=m):
#     print(' '.join(x))
# # 4.중복조합 Combination with Repetition: 순서 고려X 뽑는 경우의 수 (중복가능)
# from itertools import combinations_with_replacement
# for x in combinations_with_replacement(map(str,range(1,n+1)), m):
#     print(' '.join(x))
    