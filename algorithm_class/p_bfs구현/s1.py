"""
1. bfs - 인접 행렬 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = []
    queue.append(v)


    while queue:
        cur_vertex = queue.pop(0)
        for i in range(V+1):
            if matrix[cur_vertex][i] == 1 and visited[i] == 0:
                queue.append(i)
                trail.append(i)
                visited[i] = 1
    


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())



# 간선 정보 초기화
edge_list = list(map(int, input().split()))

# Graph 초기화
matrix = [[0]*(V+1) for _ in range(V+1)]

i = 0
while i < len(edge_list):
    matrix[edge_list[i]][edge_list[i + 1]] = 1
    matrix[edge_list[i + 1]][edge_list[i]] = 1
    i += 2

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# 흔적
trail = []

# bfs 탐색 시작
visited[1] = 1
trail.append(1)
bfs(1)

# BFS 경로 출력
print(*trail)