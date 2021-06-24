import sys
sys.stdin = open('input.txt', 'r')

# 지정된 도착지점(2)에 도달하는 시작점의 x좌표를 구하라
for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]


    # 거꾸로 도착지점부터 올라가 봅시다
    for col in range(100):
        if matrix[99][col] == 2:
            # 도착점인 2가 들어있는곳의 좌표를 시작점으로 저장
            cur_x ,cur_y = 99, col

    # 좌 우 상
    # 이래야 좌우 가지를 우선적으로 봄
    dx = [0, 0, -1]
    dy = [-1, 1, 0]


    # 가장 윗부분에 도달하기 전까지 반복
    while cur_x > 0:
        # delta를 사용하여 주위를 둘러봄
        # 그 중에 왼쪽이나 오른쪽으로 갈 길이 있으면 그걸 먼저 감
        for i in range(3):
            # 길이 있나 좌 우 상의 순서로 봄
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            # matrix 범위 내에서 살펴봐야함
            if 0 <= nx < 100 and 0 <= ny < 100:
                # 만약 길이 있으면
                # 왼쪽 오른쪽으로 나있는 길을 우선적으로 살핌
                if matrix[nx][ny]:
                    # 왔던 길을 다 0으로 만들어서 탐색할때 제외하도록 하자
                    matrix[cur_x][cur_y] = 0
                    # 가야할 곳으로 이동
                    cur_x += dx[i]
                    cur_y += dy[i]
    print("#{} {}".format(tc, cur_y))