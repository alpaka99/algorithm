import sys
sys.stdin = open('input2.txt', 'r')

def dfs(r, c):

    stack = []
    stack.append([r,c])

    visited = [[0]*100 for _ in range(100)]
    visited[r][c] = 1

    # delta 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while stack:
        cur_pos = stack.pop()
        for i in range(4):
            nr = cur_pos[0] + dr[i]
            nc = cur_pos[1] + dc[i]

            if maze[nr][nc] == 3:
                return 1

            if not(visited[nr][nc]) and maze[nr][nc] == 0:
                stack.append([nr, nc])
                visited[nr][nc] = 1
    return 0

for _ in range(1, 11):
    tc = int(input())

    # 16 by 16 maze
    maze = [list(map(int, input())) for _ in range(100)]

    for j in range(100):
        if maze[1][j] == 2:
            ans = dfs(1,j)


    print("#{} {}".format(tc, ans))