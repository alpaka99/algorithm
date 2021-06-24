import sys
sys.stdin = open('input.txt', 'r', encoding='utf8')

global matrix
global dx
global dy

def find_o():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                ans = find_direction(i, j)
                if ans == 1:
                    return 'YES'
    return 'NO'

def find_direction(x, y):
    # 8방향을 봐야함
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 내에서
        if 0 <= nx < N and 0 <= ny < N:
            # 8방향중 o가 있으면
            if matrix[nx][ny] == 'o':
                # 해당 방향에 대한 검사가 오목이 맞으면
                ans = is_it_omok(x, y, i)
                if ans == 1:
                    return 1
            # 못찾으면 다시 8방향 중 남은 방향을 돈다
    return 0

def is_it_omok(x, y, i):
    # 처음 x,y랑 nx, ny가 다 o이므로 일단은 2
    count = 1
    N = len(matrix)

    # count 가 5면 오목이므로 자동 탈출
    while count <= 5:
        x += dx[i]
        y += dy[i]

        # 범위 내에서
        if 0 <= x < N and 0 <= y < N:
            if matrix[x][y] == 'o':
                count += 1
            ####### 아 여기서 틀렸었네 ##########
            # 6 by 6에서 oo.ooo이런 경우에 이 else가 없으면 True반환
            else:
                break
        else:
            break
    if count == 5:
        return 1
    else:
        return 0

for tc in range(1, int(input())+1):
    N = int(input())
    # i는 돌이 있는 칸, . 는 돌이 없는 칸
    matrix = [list(input()) for _ in range(N)]

    # 북, 북동, 동, 남동, 
    # 이 4 방향만 봐도 전체 오목 탐색이 되며
    # 이게 더 빠를듯
    dx = [-1, -1, 0, 1,]
    dy = [0, 1, 1, 1, ]

    print("#{} {}".format(tc, find_o()))
