#인접 행렬 방식: 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식
INF = 999999999
graph1 = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph1)

#인접 리스트 방식: 모든 노드에 연결된 노드에 대한 정볼르 차례대로 연결하며 저장
graph2 = [[] for _ in range(3)]
graph2[0].append((1,7))
graph2[0].append((2,5))
graph2[1].append((0,7))
graph2[2].append((0,5))
print(graph2)

def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
dfs(graph, 1, visited)