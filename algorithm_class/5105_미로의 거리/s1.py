import sys
sys.stdin = open('input.txt', 'r')

# 거리를 재면서 bfs
def bfs(r, c):
    level = 1 # 거리를 level로 표현
    visited = [[0]*N for _ in range(N)]

    # delta 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    
    # queue에 시작점 넣어주기
    queue = []
    queue.append([r,c])
    visited[r][c] = 1


    while queue:
        size = len(queue) 
        for _ in range(size): # 현재 level의 길이 만큼만 반복을 돌림
            cur_pos = queue.pop(0)
            for i in range(4): # 4방 탐색
                nr = cur_pos[0] + dr[i]
                nc = cur_pos[1] + dc[i]

                if not(0 <= nr < N and 0 <= nc < N): # 범위 밖
                    continue
                if maze[nr][nc] == 3: # 도착
                    return level
                if visited[nr][nc] == 0 and maze[nr][nc] == 0: # 가는 길
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
        level += 1

    return 0




for tc in range(1, int(input())+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    
    # 시작 점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                ans = bfs(i,j)

    print("#{} {}".format(tc, ans))