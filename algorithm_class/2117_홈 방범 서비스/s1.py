import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(r, c):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    dq = deque()
    dq.append([r,c])
    visited[r][c] = 1
    
    # 현재 범위 안에 있는 집들의 갯수
    num_house = matrix[r][c]

    level = 1
    max_profit = 0
    max_house = num_house


    # bfs 시작
    # 모든 집을 커버하는 마름모를 그릴때까지 해봄
    while dq:
        # 현재 레벨에서의 손해를 보지 않고 가장 많은 집을 커버하면
        profit = num_house * M - (level**2 + (level-1)**2)
        if profit >= 0:
            if max_house < num_house:
                max_house = num_house
        
        # 탈출 조건

        
        size = len(dq)
        for _ in range(size):
            cur_r, cur_c = dq.popleft()
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]

                if not(0<=nr<N and 0<=nc<N):
                    continue

                if not(visited[nr][nc]):
                    visited[nr][nc] = 1
                    dq.append([nr,nc])
                    if matrix[nr][nc] == 1:
                        num_house += 1
        level += 1
    return max_house


for tc in range(1, int(input())+1):
    # Matrix크기 N, 하나의 집이 지불하는 비용 M
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 손해보지 않는 선에서 서비스 가능한 최대값은?
    ans_matrix = [[0 for _ in range(N)] for _ in range(N)]


    # 커버되는 집의 수는 각 칸에 기재

    # delta
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]


    for i in range(N):
        for j in range(N):
            ans_matrix[i][j] = bfs(i, j)


    # ans_matrix에서 최댓값 찾기
    max_value = 0
    for i in range(N):
        for j in range(N):
            if ans_matrix[i][j] > max_value:
                max_value = ans_matrix[i][j]

    print("#{} {}".format(tc,max_value))