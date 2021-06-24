"""
동윤님 방법대로 dfs로 풀어보자
"""
import sys
sys.stdin = open('input.txt', 'r')

global min_value

# 거리를 재는 dfs를 만들어보자
def dfs(r, c, step):
    step += 1

    if maze[r][c] == 3:
        global min_value
        if step < min_value:
            min_value = step
        return # 시작할때 1로 시작해서 -1을 해줘야함

    if step > min_value:
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if maze[nr][nc] != 1 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(nr, nc, step)
            visited[nr][nc] = 0
    return


for tc in range(1, int(input())+1):
    N = int(input())

    # 쿠션 만드는거 깔끔하게 하는 방법 익히자
    maze = []
    maze.append([1]*(N+2))
    matrix = [[1]+ list(map(int, input())) +[1] for _ in range(N)]
    maze += matrix
    maze.append([1]*(N+2))


    # 방문 기록
    visited = [[0]*(N+2) for _ in range(N+2)]
    
    # 상 우 하 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    for i in range(N+2):
        for j in range(N+2):
            if maze[i][j] == 2:
                # 이 부분을 안해줘서 시작지점에서 다시 돌아오는 현상 발생
                visited[i][j] = 1
                min_value = 10000
                dfs(i, j, -1)

    if min_value == 10000:
        print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, min_value-1))
