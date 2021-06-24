import sys
sys.stdin = open('input.txt', 'r')

# 돌때 전부 해당국가면 True 반환 아니면 False반환
def victory(N:int, country:int):
    for i in range(N):
        for j in range(N):
            if land[i][j] != country:
                if land[i][j] == 0:
                    continue
                else:
                    return False
    return True

def is_alive(N:int, country:int):
    for i in range(N):
        for j in range(N):
            if land[i][j] == country:
                return True
    return False

def attack(N:int, country:int):

    # 공격해야할 칸을 찾고
    target = find_attacked(N, country)

    # 한번에 모든 공격이 이뤄져야하므로 공격내역을 기록할 matrix 필요
    tmp_matrix = [[0 for _ in range(N)] for _ in range(N)]

    while target:
        cur_x, cur_y = target.pop()

        army = 0
        for i in range(4):
            nr = cur_x + dr[i]
            nc = cur_y + dc[i]

            # 범위 초과
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            # 공격하는 국가가 주위에 있으면
            # 공격하는 병력을 모으고
            if land[nr][nc] == country:
                army += force[nr][nc]//5
                # 임시 매트릭스에 저장
                tmp_matrix[nr][nc] -= army
                tmp_matrix[cur_x][cur_y] -= army

    for i in range(N):
        for j in range(N):
            force[i][j] += tmp_matrix[i][j]
            # 땅 점령했음
            if force[i][j] < 0:
                force[i][j] *= -1
                # 점령했으니까 땅주인도 바꿔줌
                land[i][j] = country


def find_attacked(N:int, country:int):
    # 각 칸 주위에 공격 turn의 국가인지
    attacked = []
    for i in range(N):
        for j in range(N):
            # 당하는 국가 입장에서 확인
            if land[i][j] != country and land[i][j] != 0:
                surround = 0 # 공격하는 나라가 둘러싼 병력

                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]

                    # 범위 초과
                    if not(0 <= nr < N and 0 <= nc < N):
                        continue

                    # 각 칸의 주위 둘러싼 병력을 확인
                    if land[nr][nc] == country:
                        surround += force[nr][nc]

                if surround >= force[i][j]*5:
                    attacked.append([i,j])
    return attacked

def reinforce(N:int, country:int):
    tmp_matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if land[i][j] == country:
                # 주위에 전부 아군인지 확인하는 flag
                safe_flag = True
                reinforce_flag = 0
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]

                    # 범위 초과
                    if not (0 <= nr < N and 0 <= nc < N):
                        continue

                    # delta 이동한 칸이 아군일때
                    if land[nr][nc] == country:
                        safe_flag += 1
                        if force[i][j] >= force[nr][nc]*5:
                            reinforce_flag += 1
                            tmp_matrix[nr][nc] += force[i][j]//5
                    else:
                        safe_flag = False
                # 4방이 아군
                if safe_flag == True:
                    for k in range(4):
                        nr = i + dr[k]
                        nc = j + dc[k]

                        # 범위 초과
                        if not (0 <= nr < N and 0 <= nc < N):
                            continue

                        # 여기서 = 으로 초기화를 해줘버림
                        tmp_matrix[nr][nc] = force[i][j]//5

                    force[i][j] //= 5
                # 4방이 아군이 아님
                else:
                    for _ in range(reinforce_flag):
                        tmp_matrix[i][j] -= force[i][j]//5
    for i in range(N):
        for j in range(N):
            force[i][j] += tmp_matrix[i][j]
                
def supply(N:int):
    for i in range(N):
        for j in range(N):
            force[i][j] += supplies[i][j]

for tc in range(1, int(input())+1):
    # 공격&지원(각 나라), 보충(전체)
    N = int(input())

    # 소유정보
    land = [list(map(int, input().split())) for _ in range(N)]

    # 병력
    force = [list(map(int, input().split())) for _ in range(N)]

    # 보충
    supplies = [list(map(int, input().split())) for _ in range(N)]

    # flag를 모아둠
    flags = [False for _ in range(N+1)]

    alive_flag = [True for _ in range(N+1)]

    # 공격, 지원할떄 사용할 delta
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    turn = 1

    # attack(N, 1)
    # print(force)
    # print(land)
    # reinforce(N, 1)
    # print(force)
    # supply(N)
    # print(supplies)
    # print(force)
    # print(victory(N,1))
    while not(flags[1]) and not(flags[2]) and not(flags[3]):
        if turn != 0 and alive_flag[turn]:
            # 공격
            attack(N, turn)
            # 지원
            reinforce(N, turn)
            # 보충
            supply(N)
            # 이겼나 졌나
            print(turn)
            print(force)
            flags[turn] = victory(N, turn)
            alive_flag[turn] = is_alive(N,turn)
        turn = (turn+1) % 4

    print(land)
    print(force)
    total = 0
    for i in range(N):
        for j in range(N):
            total += force[i][j]
    print(total)