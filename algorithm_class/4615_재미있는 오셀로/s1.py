"""
1. -1(백돌) 일떄는 잘 뒤집히는데 1(흑돌) 일때 잘 안뒤집힘 -> 와... delta쓸때 y하나 잘못 써서 x라고 써놔서 y축 검사가 아예 안됐네
2. 0일때도 내가 놓은 돌과 달라서 검사했던 부분 수정 -> 이젠 곱해서 -1일떄만 돌뒤집기 검사
"""
import sys
sys.stdin = open('input.txt', 'r')

# python은 const가 없구나...

def look_around(x, y):
    # 현재 놓은 돌의 색
    color = matrix[x][y]

    # 주위를 둘러봄
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # matrix 범위 안을 탐색
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
            # 체크하는 방향의 돌이 지금 돌 색이랑 다르면
            if matrix[nx][ny]*color == -1:
                # 해당 방향을 쭉 탐색하며 색을 돌림
                turn_colors(x, y, i)


# 색을 뒤집는 함수
def turn_colors(x,y,i):
    # 지금까지의 경로를 백트랙킹 할 stack
    stack = []
    
    # 지금 놓은 돌의 색
    color = matrix[x][y]
    
    nx = x + dx[i]
    ny = y + dy[i]

    # 같은색 돌을 찾기전에 while을 나간건지 찾아서 나간건지 구분해주는 flag
    same_flag = False

    while 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
        # 사이에 끼어있는지 아닌지 모르니까 우선 다 쌓자
        # 다른색 돌을 만남
        if color * matrix[nx][ny] == -1:
            stack.append([nx, ny])
        # 0이 나왔다는 뜻은 stack에 있는 돌들은 사이에 끼인 돌이 아니라는 뜻
        elif color*matrix[nx][ny] == 0:
            return
        # 같은색 돌을 찾음
        elif color*matrix[nx][ny] == 1:
            # 같은색 돌을 찾았다는 신호
            same_flag = True
            break
        # 계속 그 방향으로 전진
        nx += dx[i]
        ny += dy[i]

    # stack에 쌓인게 있고 same_flag가 True면 가운데에 다른색이 끼어있다
    if same_flag == True:
        while stack:
            prev_node = stack.pop()
            matrix[prev_node[0]][prev_node[1]] *= -1



for tc in range(1, int(input())+1):
    # 보드 한변의 길이
    N, M = map(int, input().split())

    # 판 만들기
    matrix = [[0]*N for _ in range(N)]
    matrix[(N//2)-1][(N//2)-1], matrix[N//2][N//2] = -1, -1
    matrix[(N // 2)][(N // 2) - 1], matrix[(N // 2)-1][N // 2] = 1, 1

    # delta
    # 북, 북동, 동, 남동, 남, 남서, 서, 북서
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    # 이제 수를 두기 시작함
    for _ in range(M):
        # 1은 흑, 2는 백
        x, y, color = map(int, input().split())
    
        # index로 편하게 접근하고 싶어서
        x -= 1
        y -= 1

        # -1 곱하는걸로 뒤집고 싶어서
        # 이러면 1은 흑, -1은 백
        if color == 2:
            color = -1

        # 수를 놓고
        matrix[x][y] = color

        # 주위를 확인
        look_around(x, y)

    # 수를 다 놓고 for문 탈출 후 백돌 흑돌 색 구하기
    black_count = 0
    white_count = 0
    for i in range(N):
        for j in range(N):
            # 흑돌 숫자 세기
            if matrix[i][j] == 1:
                black_count += 1
            # 백돌 숫자 세기
            elif matrix[i][j] == -1:
                white_count += 1

    print("#{} {} {}".format(tc,black_count, white_count ))