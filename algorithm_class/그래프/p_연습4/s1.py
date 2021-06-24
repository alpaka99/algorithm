"""
연습 문제4. bfs 구현
 - bfs 방식으로 그래프를 탐색하시오.
"""
from collections import deque

def bfs(n:int):
    dq = deque()
    dq.append(n)
    visited[n] = 1

    while dq:
        vertex = dq.popleft()
        print(vertex, end = ' ')
        for v in ad_list[vertex]:
            if not(visited[v]):
                visited[v] = 1
                dq.append(v)



import sys
sys.stdin = open('input.txt')

# 정점, 간선 정보 초기화
V, E = map(int, input().split())
data = list(map(int, input().split()))

ad_list = [[] for _ in range(V+1)]

for i in range(0, len(data), 2):
    ad_list[data[i]].append(data[i+1])
    ad_list[data[i+1]].append(data[i])

# 그래프, 방문 정보 초기화
visited = [0 for _ in range(V+1)]

# 그래프 그리기

# 탐색 시작
bfs(1)

# 시작 정점으로부터의 거리(visited 활용)