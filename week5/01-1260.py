# DFS(Depth-First Search): 깊이 우선 탐색 그래프에서 깊은 부분 우선 탐색
# n:정점 개수 / m:간선 개수 / v:정점 번호
from collections import deque

def dfs(v):
    #현재 노드 방문 처리
    v1[v] = 1 
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[v]:
        if not v1[i]:
            dfs(i)    

def bfs(v):
    v2[v] = 1
    queue = deque([v])
    
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        #해당 원소와 연결된, 아직 방문X 원소들 큐에 삽입
        for i in graph[q]:
            if not v2[i]:
                queue.append(i)
                v2[i] = 1
                
n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(n+1):
    graph[i].sort()
    
v1 = [0]*(n+1)
v2 = [0]*(n+1)

dfs(v)
print()
bfs(v)
    
