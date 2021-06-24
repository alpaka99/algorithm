import sys
sys.stdin = open('input.txt', 'r')

# BFS
def bfs(start, goal, vertex):
    level = 1 #몇 레벨 만에 도달하는지를 retrun
    
    visited = [0 for _ in range(vertex+1)]

    queue = []
    queue.append(start)

    while queue:
        size = len(queue) # 현재 레벨의 vertex들만큼만 for문 탐색
        for i in range(size):
            cur_vertex = queue.pop(0)
            nxt_vetexes = ad_list[cur_vertex]
            for j in range(len(nxt_vetexes)):
                if nxt_vetexes[j] == goal: # 목표 도착
                    return level
                if visited[nxt_vetexes[j]] == 0: # 추가 탐색
                    visited[nxt_vetexes[j]] = 1
                    queue.append(nxt_vetexes[j])
        level += 1 # 현재 level 끝
    return 0


for tc in range(1, int(input())+1):
    # Vertex and Edge number
    V, E = map(int, input().split())

    edge_list = []
    for i in range(E):
        edge_list.append(list(map(int, input().split())))


    # making adjacency list
    ad_list = [[] for _ in range(V+1)]

    for i in range(len(edge_list)):
        ad_list[edge_list[i][0]].append(edge_list[i][1])
        ad_list[edge_list[i][1]].append(edge_list[i][0])


    # Start, Goal Vertex
    S, G = map(int, input().split())

    print("#{} {}".format(tc,bfs(S, G, V)))