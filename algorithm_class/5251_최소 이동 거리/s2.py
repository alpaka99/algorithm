"""
Dijkstra by 현승님
using heapq
"""

import sys
import heapq
sys.stdin = open('input.txt', 'r')

INF = 987654321

def dijkstra(v):
    # 출발지를 우선순위큐에 넣어주면서 시작
    pq = []
    heapq.heappush(pq, (0, v))
    d[v] = 0
    while pq:
        # 우선순위 큐를 통해 현재 와본 정점중에 가장 비용(가중치)이 적게드는 최소비용정점을 골라낸다
        # w : 출발지에서 현재 정점으로가는 가중치, v : 현재 정점
        # w, v = heapq.heappop(pq)
        # # nw : 현재정점에서 인접정점으로가는 가중치  nv :현재 정점에 대한 인접 정점
        # for nw, nv in graph[v]:
        #     # 인접정점의 원래 최소비용 > 현재정점 거쳐서 인접정점가는 최소비용 이면 갱신&우선순위큐에 넣어주기
        #     if d[nv] > w + nw:
        #         d[nv] = w + nw
        #         heapq.heappush(pq, (d[nv], nv))

        w, v = heapq.heappop(pq)

        for nw, nv in graph[v]:
            if d[nv] > nw + d[v]:
                d[nv] = nw + d[v]
                heapq.heappush(pq, (d[nv], nv))

    return d[N]

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
    # 출발지에서 각 정점으로의 최소비용
    d = [INF for _ in range(N+1)]
    print('#{} {}'.format(tc, dijkstra(0)))


