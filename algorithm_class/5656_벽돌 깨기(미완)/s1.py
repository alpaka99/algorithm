# 구슬이 명중한 벽돌은 상하좌우로 '벽돌에 적힌 숫자'만큼 제거됨
# 제거되는 범위 내에 있는 벽돌은 동시에 제거됨
# -> 연쇄작용이 일어난다
# 최대한 많이 벽돌을 부수고 남은 벽돌의 갯수를 구하라


import sys
import copy
from collections import deque
sys.stdin = open('input.txt', 'r')


global min_leftover


# 재귀 bfs
def dfs(matrix:list, level:int):
    #print(level)
    # 재귀 탈출
    if level == N:
        total = 0
        for i in range(H):
            for j in range(W):
                if matrix[i][j]:
                    total += 1
            global min_leftover
            if total < min_leftover:
                min_leftover = total
        return


    # for문으로 모든 곳을 돌면서 하나씩 다 깨보고 내려갈거
    for j in range(W):
        # 일단은 matrix copy
        visited = [[0 for _ in range(H)] for _ in range(W)]
        # 폭발할곳 색칠하기
        color(j, matrix, visited)
        print(visited)
        # 색칠된곳 지우기
        new_matrix = blow(matrix, visited)

        dfs(new_matrix, level+1)


# 칠하는건 bfs
def color(c, matrix, visited):
    # 해당 줄에서 제일 높은 부분 찾음
    for top in range(H):
        if matrix[top][c]:
            break

    dq = deque()
    dq.append([top, c])

    while dq:
        size = len(dq)
        for _ in range(size):
            cur_r, cur_c = dq.popleft()

            # 폭발 반경
            expansion = matrix[cur_r][cur_c]

            for _ in range(expansion):
                for i in range(4):
                    nr = cur_r + dr[i]*(expansion-1)
                    nc = cur_c + dc[i]*(expansion-1)

                    if not(0 <= nr < H and 0 <= nc < W):
                        continue

                    if not(visited[nr][nc]):
                        if matrix[nr][nc]:
                            visited[nr][nc] = 1
                            dq.append([nr, nc])

# 날려버리기
def blow(matrix:list, visited:list):
    new_matrix = []
    for i in range(H):
        stack = []
        blow_cnt = 0 # 폭발시킨 갯수
        for j in range(W):
            if visited[i][j]:
                blow_cnt +=1
            else:
                stack.append(matrix[i][j])
        for _ in range(blow_cnt):
            stack.append(0)
        new_matrix.append(stack)

    return new_matrix






for tc in range(1, int(input())+1):
    # N개의 구슬, W by H의 배열
    N, W, H = map(int, input().split())

    # 근데 stack 여러개에서 pop하는 방법으로 하는게 좋을듯
    matrix = [list(map(int, input().split())) for _ in range(H)]
    new_matrix = []

    for j in range(W):
        stack = []
        for i in range(H - 1, -1, -1):
            stack.append(matrix[i][j])
        new_matrix.append(stack)

    min_leftover = 12*15
    
    # delta 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dfs(matrix,0)

    print(min_leftover)
