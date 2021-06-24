"""
2. bfs - 인접 리스트 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = []
    queue.append(1)

    while queue:
        cur_vertex = queue.pop(0)

        for i in range(len(ad_list[cur_vertex])):
            nxt_vertex = ad_list[cur_vertex][i]
            if visited[nxt_vertex] == 0:
                queue.append(nxt_vertex)
                visited[nxt_vertex] = 1
                trail.append(nxt_vertex)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())


# 간선 정보 초기화
edge_list = list(map(int, input().split()))

# Adjacecy list 초기화
ad_list = [[] for _ in range(V+1)]

for i in range(0, len(edge_list), 2):
    ad_list[edge_list[i]].append(edge_list[i + 1])
    ad_list[edge_list[i + 1]].append(edge_list[i])


# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# 경로 저장
trail = []

# bfs 탐색 시작
visited[1] = 1
trail.append(1)
bfs(1)

# 경로 프린트
print(*trail)