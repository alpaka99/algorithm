def dice_game(first_roller, dice_A, dice_B):
    # first_roller에 맞춰서 swtich를 통해 A인지 B인지를 구분
    if first_roller == 'A':
        cur_roller = 'B'
        switch = 1
    else:
        cur_roller = 'A'
        switch = -1
    
    # 말들이 움직일 보드
    board = ['']*20
    # 현재 A와 B의 위치
    cur_A, cur_B = 0, 0
    
    # 10번 굴릴때까지
    for i in range(10):
        # A,B마다 한번씩
        for _ in range(2):
            # 굴리는 사람을 바꿔줌
            switch *= -1
            cur_roller = chr(ord(cur_roller) + switch)
            # 현재 굴리는 사람이 B일떄
            if ord(cur_roller) - ord('A'):
                prev_B = cur_B
                cur_B += dice_B[i]
                # 현재 굴린 주사위까지의 합이 마지막칸을 넘어가면
                if cur_B >= 19:
                    return 'B'
                else:
                    # 아니면 이동했다는것을 구현하기위해 B를 지우고 다시 새로운 자리에 넣어줌
                    board[prev_B] = ''
                # 만약 이동하려는 자리에 A가 있으면
                if board[cur_B] == 'A':
                    cur_A = 0
                    board[cur_B] = 'B'
                # 없으면
                else:
                    board[cur_B] = 'B'
            # A일떄
            else:
                prev_A = cur_A
                cur_A += dice_A[i]
                # 현재 굴린 주사위의 합까지가 마지막 칸을 넘어가면
                if cur_A >= 19:
                    return 'A'
                # 아니면 이동했다는것을 구현하기 위해 원래 있던 A를 지워줌
                else:
                    board[prev_A] = ''
                # 만약 이동하려는 자리에 B가 있으면
                if board[cur_A] == 'B':
                    cur_B = 0
                    board[cur_A] = 'A'
                # 없으면
                else:
                    board[cur_A] = 'A'
    #10번을 다 굴렸는데도 도착점에 도달하지 못했으면 AB를 리턴
    return 'AB'

for tc in range(1, int(input())+1):
    # 먼저 주사위를 굴리는 사람, a의 주사위 번호들, b의 주사위 번호들
    first_roller = input()
    dice_a = list(map(int, input().split()))
    dice_b = list(map(int, input().split()))
    
    # dice_game의 결과를 ans에 저장해줌
    ans = dice_game(first_roller, dice_a, dice_b)
    print("#{} {}".format(tc, ans))
