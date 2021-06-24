"""
level을 나눠서 풀어봤음
"""
# 이거 못풀면 오늘 안잔다
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    harvest = 0

    # 상 좌 우 하
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    start_point = [[N//2, N//2]]
    # 첫 시작 포인트는 더해지지 않아서 처음에는 더해줌
    harvest += matrix[N//2][N//2]
    visited[N//2][N//2] = 1

    ########## 이 부분이 point#############
    # harvest가 끝난 마름모의 크기를 level로 나타냄
    harvest_level = 0
    #################################
    
    # 수확 마름모가 농장 끝에 닿을때 까지만
    while harvest_level < N//2:
        # start_point를 다 비우면 그때 harvest_level을 1 증가시키는 로직이므로
        new_start_point = []
    # start point에 뭐가 있는 동안은 계속 진행
        while start_point:
            # 시작점 하나를 뽑아냄
            x = start_point[0][0]
            y = start_point[0][1]
            start_point.pop(0)

            # delta를 돌면서 상 좌 하 우 를 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 수확하지 않은 곳이면 수확하고 시작점으로 저장
                if not(visited[nx][ny]):
                    harvest += matrix[nx][ny]
                    visited[nx][ny] =1
                    new_start_point.append([nx, ny])
        # start_point 리스트가 비었으면 한 레벨이 끝났으므로
        harvest_level += 1
        start_point = new_start_point

    print("#{} {}".format(tc,harvest))