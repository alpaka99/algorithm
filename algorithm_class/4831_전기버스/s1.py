import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def elctro_bus(tc):
    k, n, m = map(int, input().split())
    # k는 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # n 은 종점 정류장의 점프 횟수
    # m 은 충전소가 설치된 정류장

    # m은 충전소가 설치된 정류장
    m_list = list(map(int, input().split()))

    stops = []
    # 정류장들 만들기
    for i in range(n):
        if i in m_list:
            stops.append(1)
        else:
            stops.append(0)
    stops.append(0)

    # 주유 횟수
    count = 0

    # 현 위치
    pos = 0

    # 가능 불가능
    for i in range(len(m_list) - 1, 1, -1):
        if m_list[i] - m_list[i - 1] > k:
            print("#{} {}".format(tc,0))
            return

    while pos <= n:
        # 일단 달리고
        pos += k
        if pos >= n:
            break
        # 만약 도착지가 정류소다?
        # 충전하고 또 출발
        if stops[pos]:
            count += 1
        # 도착지가 정류장이 아님
        # 정류장인 곳까지 뒤로 이동
        else:
            while stops[pos] == 0:
                pos -= 1

            # 정류장 도착
            count += 1

    print("#{} {}".format(tc,count))

for tc in range(1,T+1):
    elctro_bus(tc)


