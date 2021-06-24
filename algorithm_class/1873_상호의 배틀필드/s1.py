import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

def shooting():
    pass

def watch_n_roll():
    pass

for tc in range(1, int(input())+1):
    # 맵의 높이 H, 너비 W
    H, W = map(int, input().split())

    # 문자    의미
    # .         평지(전차 들어갈 수 있음)
    # *         벽돌로 만들어진 벽
    # #         강철로 만들어진 벽
    # -         물(전차 들어갈 수 없음)
    # 위 화살표     위쪽을 바라보는 전차(아래는 평지이다)
    # 아래 화살표    아래를 바라보는 전차(아래는 평지이다)
    # <             왼쪽을 바라보는 전차(아래는 평지이다.)
    # >             오른쪽을 바라보는 전차(아래는 평지이다)
    # 전차는 단 한대
    field = [list(input()) for _ in range(H)]
    # 사용자가 넣을 입력
    # U UP: 전차가 바라보는 방향을 위쪽으로 바꾸고 위쪽이 평지이면 이동
    # D Down: "
    # L Left : "
    # R Right: "
    # S shoot: 전차가 현재 바라보고 있는 방향으로 포탄 발사.
    N = int(input())
    user_input = input()

    command_dict = {'U':[-1, 0], 'D': [1, 0], 'L': [0, -1], 'R':[0, 1],'S':0}
    tank = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R'}
    tank_direction = ''
    cur_x = 0
    cur_y = 0

    # 탱크의 위치를 찾음
    for i in range(H):
        for j in range(W):
            if field[i][j] in tank:
                cur_x = i
                cur_y = j
                tank_direction = tank[field[i][j]]
                break
    print(cur_x, cur_y, tank_direction)

    for i in range(N):
        command = command_dict[user_input[i]]
    
        # 쏘는것
        if command == 'S':
            pass
        # 그 이외에는 다 움직이거나 보는 방향 전환
        else:
            pass
