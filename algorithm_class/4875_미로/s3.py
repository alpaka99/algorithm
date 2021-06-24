"""
가는길을 표시해보자
"""

import sys

sys.stdin = open('input.txt', 'r')

global maze
global trail

# 한걸음 걸어갈때마다 갈림길 있는지 확인하고 갈림길이 있으면 둘 다 stack에 저장
def dfs(x, y):
    stack = []

    # delta, 상, 좌, 하 우
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # 방문 했는지 안했는지 체크-> 막다른 길일떄를 위해서
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1



    # 시작지점 넣어줌
    stack.append([x, y])

    # 갈림길마다 스택에 저장해줄거야
    while stack:
        # 현재 위치
        cur_pos = stack.pop()
        # 길에 넣어줌
        trail.append(cur_pos)
        
        # 사방검사해서 갈림길 저장하고 안가본 곳으로 가자
        for i in range(4):
            nx = cur_pos[0] + dx[i]
            ny = cur_pos[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < N:  # 가려고 하는 방향이 범위 안이고
                if maze[nx][ny] == 3:  # 목적지면 1 리턴
                    trail.append([nx, ny])
                    return 1
                elif maze[nx][ny] == 0 and visited[nx][ny] == 0:  # 목적지는 아니지만 길이 뚫려있음
                    stack.append([nx, ny])  # 길을 다 저장
                    visited[nx][ny] = 1  # 방문 표시
            # 만약 if문을 통과하지 못하면 맞는 길의 방향이 아니므로 trail에서 뺴줌
            trail.pop()
    # stack이 다 빌때까지 완전탐사했는데 목적지에 도달하지 못했으므로
    return 0


for tc in range(1, int(input()) + 1):
    # N by N
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 가장 아래쪽의 2부터 가장 위쪽의 3까지 갈 수 있으면 1 없으면 0

    # 지나온 길을 넣어두는 리스트
    trail = []

    # 시작점을 찾아서 dfs함수에 넣어줌
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                trail.append([i, j])
                ans = dfs(i, j)
    print(trail)
    print("#{} {}".format(tc, ans))
