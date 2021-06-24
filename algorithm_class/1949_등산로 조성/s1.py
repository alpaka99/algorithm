'''
N by N matrix
height = int
start = heights peak
high -> low
can cut down the height "once"
up down right left
'''

import sys
sys.stdin = open('input.txt', 'r')

global longest


# 백트랙킹 할려면 재귀함수로 만들어야할것 같은데?? ... 다시 다 만들어야하나..
def dfs(start_point: list, cut_flag:bool, road_length:int, trail:list ):
    r, c = start_point
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위밖이면 이번 loop 건너뜀
        if not(0 <= nr < N and 0 <= nc < N):
            continue


        if not(visited[nr][nc]):
            # 그냥 낮을때
            if matrix[nr][nc] < matrix[r][c]:
                visited[nr][nc] = 1
                trail.append([nr,nc])
                dfs([nr, nc], cut_flag, road_length+1, trail)
                trail.pop()
                visited[nr][nc] = 0
            # 깍아서 낮을때
            elif matrix[nr][nc] - K < matrix[r][c] and cut_flag == False:
                cut_flag = True
                # 최대만큼 깍는게 아니라 최대한 높은 높이로 깍아야함
                tmp = matrix[nr][nc]
                matrix[nr][nc] = matrix[r][c]-1
                trail.append([nr,nc])
                dfs([nr,nc], cut_flag, road_length+1, trail)
                # 다시 복구
                matrix[nr][nc] = tmp
                cut_flag = False
                trail.pop()
    # 사방이 다 막혔으면 탐색 끝
    global longest
    if road_length >= longest:
        longest = road_length
        #print(trail)
    visited[r][c] = 0
    return


for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 시작지점들 찾기
    highest = 0
    for i in range(N):
        for j in range(N):
            if highest < matrix[i][j]:
                highest = matrix[i][j]
                start_points = []
                start_points.append([i,j])
            elif highest == matrix[i][j]:
                start_points.append([i,j])

    # delta 위 오른쪽 아래 왼쪽
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    longest = 0

    while start_points:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        cut_flag = False # 깎았는지 아닌지를 나타내는 변수
        start = start_points.pop()
        dfs(start, cut_flag, 1, [])
    print("#{} {}".format(tc,longest))