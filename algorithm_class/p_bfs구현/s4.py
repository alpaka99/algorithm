"""
size변수사용과 visited를 거리를 저장하는 용도로 사용
"""

global distance

def bfs(v):
    queue = []
    queue.append(1)

    global distance
    distance = 1

    while queue:

        size = len(queue)

        for i in range(size): # 딱 현재의 queue의 길이만큼만 dequeue 진행
            cur_vertex = queue.pop(0) # deque
            nxt_candidates = ad_list[cur_vertex] # 인접리스트에 저장된 vertex들
            for j in range(len(nxt_candidates)):
                if visited[nxt_candidates[j]] == 0:  #방문하지 않았으면
                    queue.append(nxt_candidates[j])  #enque
                    visited[nxt_candidates[j]] = distance  #visited에 방문과 함꼐 거리까지 표시
                    trail.append(nxt_candidates[j]) # 경로를 남김
        # queue의 모든것들을 다 BFS검사하고 나면 그 다음 범위를 탐색하니까 distance를 1 증가
        distance += 1


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
# 여기서는 visited에 방문하면서 얼마나 떨어져 있는지 distance도 저장하는 용도로 사용할거임
visited = [0 for _ in range(V+1)]

# 경로 저장
trail = []

# bfs 탐색 시작
visited[1] = 1
trail.append(1)
bfs(1)

# 경로 프린트
print(*trail)

# 가장 멀리 떨어진것
max_vertex = 0
for i in range(len(visited)):
    if visited[max_vertex] <= visited[i]:
        max_vertex = i

print("Furtherest veretex is {} with distance of {}".format(max_vertex, visited[max_vertex]))
