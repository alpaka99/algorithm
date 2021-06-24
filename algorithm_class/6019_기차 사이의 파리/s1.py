import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # D 두 기차 전면부 사이의 거리, A 의 속력, B의 속력, F 파리의 속력
    D, A, B, F = map(int, input().split())

    # 두 기차가 충돌하기까지 걸린 시간
    time = D/(A+B)

    # 그 시간동안 파리는 계속 F의 속도로 이동
    # 따라서 파리의 이동 거리는 그냥 시간*속도
    distance = F*time
    
    print("#{} {}".format(tc,distance))
