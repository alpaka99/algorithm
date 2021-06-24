import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    # 주위 벽 없이 해보자
    matrix = [[0]*N for _ in range(N)]

    # dx = 0 1 0 -1
    # dy = 1 0 -1 0

    # 초기 delta
    dx = 0
    dy = 1

    # 초기 좌표
    x = 0
    y = -1

    # 초기 방향
    dir = 0
    
    # num이 N^2을 넘지 않는 순간까지 돌면 됨
    num = 1
    while num <= N**2:
        # delta만큼 이동해서 볼 칸이 matrix 범위 안에 있으면
        if 0 <= x+dx < N and 0 <= y+dy <N:
            # 이동하고
            x += dx
            y += dy
            # 그 칸을 알맞은 수로 채움
            matrix[x][y] = num
            # num에 다음 숫자를 저장해줌
            num += 1

        # 만약 delta만큼 이동할칸이 matrix의 범위를 넘어서면
        # 이동 방향을 바꿔줌
        else:
            dir = (dir + 1) % 4
            # dx는 오늘 배운 비트연산으로 표현해보자
            # 2까지의 범위인 이유는 4방향이니까 4는 이진법 2자리까지
            count = 0
            for i in range(2):
                if(1<<i & dir):
                    count += 1

            # 이진법 각 자리수를 더한것이 짝수면 dx는 -1
            if count % 2 == 0:
                dx += -1
            else:
                dx += 1


            # dy는 간단하게 dir이 2보다 작으면 -1, 2보다 크면 +1
            if dir < 2:
                dy += -1
            else:
                dy += 1
            print(x, dx, y, dy)

        print(matrix)