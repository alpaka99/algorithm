import sys
import math
from pandas import DataFrame as df
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    # 행렬 주위에 벽을 쌓는 방법으로 해보자
    matrix = [[100]*(N+2) for _ in range(N+2)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            matrix[i][j] = 0

    # print(df(matrix))

    # 초기에 돌아가는 방향 설정
    dir = 0

    # dx = 0 1 0 -1
    # dy = 1 0 -1 0
    dx = round(math.sin((math.pi / 2) * dir))
    dy = round(math.cos((math.pi / 2) * dir))

    # 현재 x, y 좌표
    x = 1
    y = 0

    # 넣는 수(시작이 1)
    num = 1

    # 우리가 넣는 수가 이론상 가장 큰 수가 되기 전까지 계속 반복
    while num <= N**2:
        # 현재 넣는 곳이 넣어도 되는곳인지 확인
        if matrix[x+dx][y+dy] == 0:
            x += dx
            y += dy
            matrix[x][y] = num
            num += 1
            #넣으면 안되는 곳이면 방향을 바꿔줌
        else:
            dir = (dir + 1) % 4
            dx = round(math.sin((math.pi / 2) * dir))
            dy = round(math.cos((math.pi / 2) * dir))

    print("#{}".format(tc))
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(matrix[i][j],end=' ')
        print()