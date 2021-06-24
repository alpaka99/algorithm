"""
3. bfs - 인접 딕셔너리 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = []
    queue.append(1)

    while queue:
        cur_vertex = queue.pop(0)
        nxt_candidates = vertex_dict[cur_vertex]
        for i in range(len(nxt_candidates)):
            if visited[nxt_candidates[i]] == 0:
                queue.append(nxt_candidates[i])
                visited[nxt_candidates[i]] = 1
                trail.append(nxt_candidates[i])




import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
edge_list = list(map(int, input().split()))

# Dict 초기화
vertex_dict = {}
for i in range(V+1):
    vertex_dict[i] = []

for i in range(0, len(edge_list), 2):
    vertex_dict[edge_list[i]].append(edge_list[i+1])
    vertex_dict[edge_list[i+1]].append(edge_list[i])


# 방문 표시 초기화
visited = [0 for _ in range(V+1)]


# 흔적
trail = []

# bfs 탐색 시작
visited[1] = 1
trail.append(1)
bfs(1)

# 출력
print(*trail)