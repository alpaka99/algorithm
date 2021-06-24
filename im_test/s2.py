import sys

sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):

    # N 총 블록의 갯수, M1 타워1의 블록갯수, M2 타워2의 블록갯수
    N, M1, M2 = map(int, input().split())

    # 블록 무게를 저장해놓음
    blocks = list(map(int, input().split()))

    # 탑의 비용은 높이 * 무게의 합
    # 최소비용은?

    # 어짜피 무거운게 아래로 가야 최소비용
    # sort한 다음에 타워 높이까지 뒤에서부터 하나씩 분배
    blocks.sort()

    # m1, m2 탑의 block이 어떤것인지 저장할 리스트들
    m1_list = []
    m2_list = []

    # 2칸씩 뛰면서 블록을 넣음
    m1_height = 0
    m2_height = 0
    
    # M1 + M2 = N 이므로 block에 들어있는 모든 블록을 분배할때까지
    while blocks:
        # m1의 높이가 기준에 닿을때까지 m1_list에 블록을 넣어줌
        if m1_height < M1:
            m1_list.append(blocks.pop())
            m1_height += 1
        # m2의 높이가 기준에 닿을때까지 m2_list에 블록을 넣어줌
        if m2_height < M2:
            m2_list.append(blocks.pop())
            m2_height += 1

    cost = 0

    # 탑 가격 더하기
    # M1탑 가격
    for i in range(len(m1_list)):
        # 1층은 1층블럭 x1, 2층은 2층블럭 x2, 3층은 3층블럭 x3...
        cost += m1_list[i] * (i + 1)
    
    # M2탑 가격
    for i in range(len(m2_list)):
        cost += m2_list[i] * (i + 1)

    print("#{} {}".format(tc,cost))