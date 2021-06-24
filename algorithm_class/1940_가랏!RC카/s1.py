# 아.... 문제 제발 잘 읽자... 싹 다 지우고 처음부터 다시 시작하게 됐넹
# 근데 쓰레기 문제네... 딱히 신경 안써도 될듯
import sys
sys.stdin = open('input.txt', 'r')

# test case
for tc in range(1, int(input())+1):
    # 0: 현재 속도 유지, 1: 가속, 2: 감속

    # N = 초
    N = int(input())

    # 총 이동거리 & 현재 속도
    distance = 0
    cur_speed = 0

    for _ in range(N):
        command = input()
        # 1 일때 = 가속
        if command[0] == '1':
            #pre_speed = cur_speed
            cur_speed = cur_speed + int(command[2])
            distance += cur_speed
            #distance += (pre_speed + cur_speed)/2
        # 2 일때 = 감속
        elif command[0] == '2':
            #pre_speed = cur_speed
            cur_speed = cur_speed - int(command[2])
            if cur_speed < 0:
                cur_speed = 0
            #distance += (pre_speed + cur_speed)/2
            distance += cur_speed
        # 0 일때 = 현속 유지
        else:
            distance += cur_speed
    print("#{} {}".format(tc,distance))

