import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(start:list):
    global shark_size, exp, time

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = 1

    matrix[start[0]][start[1]] = 0
    dq = deque([start])

    # 먹을 수 있는 물고기있나 파악
    eat_flag = False
    for i in range(0, len(fish_cnt)-1):
        if fish_cnt[i]:
            if fish_cnt[i] <= shark_size:
                eat_flag = True
                break
            else:
                continue

    if not(eat_flag):
        return False

    nxt_location = []

    time_cnt = 0
    while dq:
        time_cnt += 1
        size = len(dq)
        for _ in range(size):
            cur = dq.popleft()
            r, c = cur

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위 밖 처리
                if not(0<=nr<N and 0<=nc<N):
                    continue

                # 먹을 수 있는 물고기 발견
                if not(visited[nr][nc]):
                    if matrix[nr][nc]:
                        if matrix[nr][nc] <= shark_size:
                            # # 이동
                            # matrix[r][c] = 0
                            # matrix[nr][nc] = 9
                            # time += time_cnt
                            # # 상어 크기 성장
                            # exp += matrix[nr][nc]
                            # if exp >= shark_size:
                            #     exp -= shark_size
                            #     shark_size += 1
                            # return [nr, nc]
                            nxt_location.append([nr,nc])
                    else:
                        visited[nr][nc] = 1
                        dq.append([nr, nc])
        if nxt_location:
            break

    # 다음 위치 중 가장 위쪽 왼쪽 찾기
    if nxt_location:
        nxt_location.sort(key = lambda x: x[0])
        row = nxt_location[0][0]

        nxt = []
        for i in range(len(nxt_location)):
            if nxt_location[i][0] == row:
                nxt.append(nxt_location[i])
            else:
                break

        nxt.sort(key = lambda x: x[1])
        # # 이동
        nxt_n, nxt_r = nxt[0]
        matrix[nxt_n][nxt_r] = 9
        time += time_cnt
        # 상어 크기 성장
        exp += matrix[nxt_n][nxt_r]
        if exp >= shark_size:
            exp = 0
            shark_size += 1
        return [nxt_n, nxt_r]
    else:
        return False



N = int(input())

shark_size = 2
exp = 0
time = 0

matrix = [list(map(int, input().split())) for _ in range(N)]

# 총 몇마리 남은지 확인
fish_cnt = [0 for _ in range(7)]

# 시작 위치
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            start = [i,j]
        elif matrix[i][j]:
            fish_cnt[matrix[i][j]] += 1


# 가장 가까운 물고기를 먹으러 감
# 가장 위에 있는 물고기 + 가장 왼쪽에 있는 물고기
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


not_completed = True

while not_completed:
    not_completed = bfs(start)
    start = not_completed

print(time)






    