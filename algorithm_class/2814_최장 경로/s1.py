"""
1. 각 노드마다 연결되어있는 노드가 다르기 때문에
노드 방문 순서도 상관이 있다.
따라서 재귀로 들어가기전 visited 체크를 한것을
재귀를 나오면 visited 체크를 해제해줘야한다!
​
2. dfs에서 가장 처음에 방문하는 노드의 방문체크를 잊지말자
"""

import sys
sys.stdin = open('input.txt', 'r')

# 재귀가 편할것 같아
def dfs(n:int, cnt:int):
    cnt += 1
    vertex = ad_list[n]
    for v in vertex:
        if not(visited[v]):
            visited[v] = 1
            dfs(v,cnt)
            visited[v] = 0

    # 갈 수 있는 vertex가 없을때
    global max_val
    max_val = max(max_val, cnt)

for tc in range(1, int(input())+1):
    # N개의 정점, M개의 간선, 가중치 없는 무방향 그래프
    N, M = map(int, input().split())

    ad_list = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        ad_list[a].append(b)
        ad_list[b].append(a)

    max_val = 0

    for i in range(N+1):
        visited = [0 for _ in range(N+1)]
        visited[i] = 1
        dfs(i,0)

    print("#{} {}".format(tc,max_val))
