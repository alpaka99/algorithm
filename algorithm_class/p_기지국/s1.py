import sys
sys.stdin = open('input.txt', 'r', encoding='utf8')

for tc in range(1, int(input())+1):
    # 배열크기
    n = int(input())
    matrix = [list(input()) for _ in range(n)]

    covered = [[0]*n for _ in range(n)]

    # H = 집, A, B, C = 기지국 1, 2, 3 , X 는 아무것도 없다
    station = [[] for i in range(4)]


    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'X' or matrix[i][j] == 'H':
                continue
            else:
                # 현재 기지국의 좌표를 넣어줌
                station[ord(matrix[i][j])-ord('A')+1].append([i,j])

    # 상 우 하 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    # 이제 각 station 별로 주변의 집을 더해줌
    # dummy, A, B, C 마다
    for i in range(4):
        # A, B, C의 각 스테이션 마다
        for j in range(len(station[i])):
            cur_station = station[i][j]
            x = cur_station[0]
            y = cur_station[1]
            # 4방향을 둘러보면서 더함
            for k in range(4):
                length = 1
                while length <= i:
                    nx = x + dx[k]*length
                    ny = y + dy[k]*length
                    if 0 <= nx < n and 0 <= ny < n:
                        covered[nx][ny] = 1
                    length += 1

    # 이제 matrix를 돌면서 coverd와 비교하면서 matrix 에서는 'H'인데 cover되지 않은곳 검사
    ans = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'H':
                if not(covered[i][j]):
                    ans += 1
    #print(covered)
    print("#{} {}".format(tc, ans))