import sys
sys.stdin = open('input.txt', 'r')

def djikstra(N:int):
    # 사전 설정(거리, 첫 시작점 거리, 방문처리)
    dist = [987654321 for _ in range(N + 1)]
    dist[0] = 0
    visited = [0 for _ in range(N + 1)]

    for _ in range(N):
        # 모든 node를 돌며 방문 안한것 중 가장 작은 거리를 찾음
        min_dist = 987654321
        min_idx = -1
        for i in range(N+1):
            if not(visited[i]) and min_dist > dist[i]:
                min_idx = i
                min_dist = dist[i]

        visited[min_idx] = 1

        # 방문 안한 노드들을 돌면서 거리 전부 초기화
        for j in range(N+1):
            if not(visited[j]) and dist[j] > dist[min_idx] + G[min_idx][j]:
                dist[j] = dist[min_idx] + G[min_idx][j]

    return dist


for tc in range(1, int(input())+1):
    # 끝점 N, 간선의 갯수E
    N, E = map(int, input().split())

    # 인접행렬
    G = [[987654321 for _ in range(E)] for _ in range(E)]



    for _ in range(E):
        # 시작 s, 끝 e, 가중치 w
        s, e, w = map(int, input().split())
        G[s][e] = w

    # print(G)
    dist = djikstra(N)
    print("#{} {}".format(tc,dist[N]))



