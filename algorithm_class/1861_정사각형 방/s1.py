import sys
sys.stdin = open('input.txt', 'r')
global max_val,dr,dc, max_r, max_c

def find_route(r:int, c:int):
    global dr,dc,max_val, max_r, max_c

    nr = r
    nc = c
    length = 1
    flag = True
    while flag:
        for i in range(4):
            nxt_r = nr + dr[i]
            nxt_c = nc + dc[i]
            # 범위 밖이면
            if not(0 <= nxt_r < N and 0 <= nxt_c < N):
                continue

            # 범위 안에 조건을 만족하는곳이면
            if matrix[nxt_r][nxt_c] == matrix[nr][nc] + 1:
                nr = nxt_r
                nc = nxt_c
                length += 1
        flag = False

    if max_val < length:
        max_val = length
        max_r = nr
        max_c = nc


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 상 하 좌 우 이동가능
    # 이동하려는 방 숫자  = 현재 방 숫자 + 1
    max_val = 0

    # delta 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            find_route(i,j)


    print("#{} {} {}".format(tc, matrix[max_r][max_c],max_val))