import sys
sys.stdin = open("input.txt", "r")

# T: 테스트 케이스
# N: Ai, Bi의 input을 얼마나 받을지 알려주는 수
# Ai, Bi: 각 노선은 Ai에서 시작해서 Bi에서 끝남
# P: 다음 P개의 줄에는 C가 주어짐
# C: 정류장 번호( 나중에 해당 정류장에 버스가 몇번 지나는지 출력)


T = int(input())

for tc in range(1, T+1):
    # 버스 정류장에 대한 counting list를 먼저 만들자
    # 여기서 포인트는 앞에 0번 정류장을 임의로 만들어서
    # 계산할때 복잡하지 않게 하는것!
    bus_stop = [0]*5001
    n = int(input())

    # Ai, Bi를 n번 받고
    # counting list에 a,b사이의 index를 1씩 다 늘리자
    for i in range(n):
        a, b = map(int,input().split())
        for j in range(a, b+1):
            bus_stop[j] += 1
    #p를 받고
    p = int(input())
    #출력할 버스 정류장들의 번호를 받으면서 출력하자
    # 한줄에 다 출력해야하니까 print(,end=' ')를 사용해야함
    print("#{}".format(tc), end=' ')
    for i in range(p):
        c = int(input())
        print(bus_stop[c],end=' ')
    print()

