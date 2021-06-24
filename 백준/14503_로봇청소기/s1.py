import sys
sys.stdin = open('input.txt', 'r')
N, M = map(int, input().split())

# 로봇 청소기의 초기 정보 저장
info = list(map(int, input().split()))
r, c, dir = info[0], info[1], info[2]

matrix = [list(map(int, input().split())) for _ in range(N)]

# 청소한 칸
cleaned = 1

# delta -> 현재 방향으로부터 다음 방향의 칸을 봄
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 후진할때 사용하는 델타
back_r = [-1, 0, 1, 0]
back_c = [0, -1, 0, 1]

visited = [[0 for _ in range(M)] for _ in range(N)]
matrix[r][c] = -1
direction_check_flag = 1
while True:
    # 조건 2
    clean_flag = 1

    while direction_check_flag != 4:
        nr = r + dr[dir]
        nc = c + dc[dir]

        # 범위를 벗어나거나
        if not(0<=nr<N and 0<=nc<M):
            dir = (dir - 1) % 4
            direction_check_flag += 1
            clean_flag = 0
            continue

        # 벽이거나 청소한칸 -> 건너뜀
        if matrix[nr][nc] == 1 or visited[nr][nc] == 1:
            dir = (dir - 1) % 4
            direction_check_flag += 1
            clean_flag = 0
        # 청소해야하는 칸을 발견
        else:
            r = nr
            c = nc
            dir = (dir - 1) % 4
            visited[nr][nc] = 1
            cleaned += 1
            matrix[nr][nc] = -1
            clean_flag = 1
            direction_check_flag = 1
            break

    # 4방향 다 봤는데 답 없음
    if direction_check_flag == 4 and clean_flag == 1:
        # 후진 시도
        nr = r + back_r[dir]
        nc = c + back_c[dir]

        # 후진도 안되면
        if not(0<=nr<N and 0<=nc<M) or matrix[nr][nc]:
            print(cleaned)
            break
        # 후진 가능
        else:
            r = nr
            c = nc




