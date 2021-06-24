"""
여러번의 오류 이유
1. 손님이 같은 시간에 겹쳐서 올 수 있다는것을 생각하지 못함
2. 0초에도 손님이 올 수 있다.
3. 2에 따라 0초부터 시작하면 0초에 나눗셈이 0이라 붕어빵을 바로 구워내서 불가능한데도 가능하게 됨
"""
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # N 예약한 사람 수, M초의 시간동안 붕어빵 K개
    N, M, K = map(int, input().split())

    # 모든 손님에 대해 기다리는 시간 없이 붕어빵 가능? 불가능?
    customer_arrival = list(map(int, input().split()))

    customer_time = [0 for _ in range(max(customer_arrival)+1)]

    for i in range(len(customer_arrival)):
        customer_time[customer_arrival[i]] += 1

    boong_a_pang = 0

    time = 0
    
    # 정상적으로 끝났는지 break가 걸려서 끝났는지 판단하기 위한 flag
    possible_flag = True

    # customer time이 끝날떄까지 진행
    for i in range(len(customer_time)):
        # 만약 다음 손님이 온 시간이면
        if customer_time[i] != 0:
            # 붕어빵이 있나 확인
            if boong_a_pang >= customer_time[i]:
                boong_a_pang -= customer_time[i]
            # 붕어빵이 없으면 break
            else:
                possible_flag = False
                break

        # 다음 시간으로 넘어감
        time += 1
        # M 시간이 되면 K개의 붕어빵을 만듬
        # 이걸 time += 1 아래로 내려줘야 0초에 붕어빵이 있지 않음
        if time % M == 0:
            boong_a_pang += K
    
    # 종료 조건에 따라 출력을 바꿔줌
    if possible_flag == True:
        print("#{} {}".format(tc,'Possible'))
    else:
        print("#{} {}".format(tc, 'Impossible'))