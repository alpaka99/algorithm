"""
재현님 말대로 재귀적으로도 풀어보자
stack을 사용한 방법이랑 다른점:

이동할때:
stack 사용 - 한 위치에서 갈림길을 다 stack에 저장해놓고 그 중에서 하나를 골라서 길을 감
recursion - 갈림길이 보이자마자 그곳으로 감

돌아올때:
stack사용 - top에 저장된 현 위치에서 가장 최근의 갈림길로 순간이동함
recursion - 한발짝 뒤로 돌아오면서 이제는 한걸음 뒤에 갈림길이 있나 확인함, 이걸 계속 반복
"""

import sys

sys.stdin = open('input.txt', 'r')

global maze
global visited


# 한걸음 걸어갈때마다 dfs_recursion 함수를 반복하며 길을 찾아감
def dfs_recursion(x, y):
    # 탈출 조건
    if maze[x][y] == 3:
        return 1
    
    # delta, 상, 좌, 하 우
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if maze[nx][ny] != 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if dfs_recursion(nx, ny) == 1:
                    return 1
    return 0




for tc in range(1, int(input()) + 1):
    # N by N
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]

    # 방문 했는지 안했는지 체크-> 막다른 길일떄를 위해서
    visited = [[0] * N for _ in range(N)]


    # 가장 아래쪽의 2부터 가장 위쪽의 3까지 갈 수 있으면 1 없으면 0

    # 시작점을 찾아서 dfs함수에 넣어줌
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                visited[i][j] = 1
                ans = dfs_recursion(i, j)

    print("#{} {}".format(tc, ans))
