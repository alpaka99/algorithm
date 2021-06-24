import sys
sys.stdin = open('input.txt', 'r')

"""
밥 먹고 다시 해보자 ㅠ...
"""
def bfs(water:list):
    while water:
        start_pos = water.pop(0)

        queue = start_pos
        length = 0
        while queue:
            size = len(queue)




for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    water = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                water.append([i, j])

    # 위 오른쪽 아래 왼쪽
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]


    bfs(water)