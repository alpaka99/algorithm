import sys
sys.stdin = open('문제3_input.txt', 'r')

def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        find_set(p[x])
    return x

def union(x, y):
    x, y = find_set(x), find_set(y)
    p[find_set(x)] = find_set(p[y])



def dijkstra(s):
    dist = [987654321 for _ in range(V+1)]
    dist[s] = 0
    visited = [0 for _ in range(V)]
    visited[0] = 1

    for _ in range(V):
        min_idx = -1
        min_dist = 987654321

        # 가장 작은 노드 찾고
        for i in range(V):
            if not(visited[i]):
                if dist[i] < min_dist:
                    min_idx = i
                    min_dist = dist[i]

        visited[min_idx] = 1

        # 이어진 노드들 초기화
        for j in range(V):
            if not(visited[j]) and dist[j] > G[min_idx][j] + dist[min_idx]:
                dist[j] = G[min_idx][j] + dist[min_idx]

    return dist

for tc in range(1, int(input())+1):
    V, E, M = map(int, input().split())

    G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]
    data = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = G[e][s] = w
        data.append((s,e,w))

    # 1. 최소신장트리 찾기(크루스칼)
    p = [ 0 for _ in range(V+1) ]

    for x in range(V+1):
        make_set(x)

    total = 0

    # 쫙 정리해놓고
    data.sort(key=lambda x:x[2])
    cnt = 0
    for d in data:
        start, end, weight = d
        if find_set(start) != find_set(end):
            print(p)
            union(start, end)
            total += weight
            cnt += 1

        if cnt == V:
            break

    if total <= M:
        print(M-total)
        continue

    # 2. djikstra
    dist = dijkstra(1)
    print(dist)
    if M >= dist[V]:
        print(M-dist[V])
    else:
        print(-1)

