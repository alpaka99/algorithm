"""
5. bfs - 재귀로 구현한 bfs
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    # 탈출조건
    if len(v) == 0:
        return
    
    # 다음번에 넘겨줘야할 vertex list
    nxt_list = []
    
    # v list의 길이만큼 반복
    for i in range(len(v)):
        cur_vertex = v.pop(0) # 현재 보고있는 vertex
        nxt_candidates = ad_list[cur_vertex] #vertex에 연결된 vertex들
        for j in range(len(nxt_candidates)):
            # 방문 했었으면 바로 지나감
            if visited[nxt_candidates[j]] != 0:
                continue
                
            # 방문 안했으면 기존 bfs처럼 해줌
            nxt_list.append(nxt_candidates[j])
            visited[nxt_candidates[j]] = 1
            trail.append(nxt_candidates[j])

    # 다음에 방문할 vertex들을 넘겨줌
    return bfs(nxt_list)

    



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

for i in range(0, len(edge_list), 2):
    ad_list[edge_list[i]].append(edge_list[i+1])
    ad_list[edge_list[i+1]].append(edge_list[i])


# 방문 표시 초기화
visited = [0 for _ in range(V+1)]


# 흔적
trail = []

# bfs 탐색 시작
visited[1] = 1
trail.append(1)
bfs([1])

# 출력
print(*trail)
