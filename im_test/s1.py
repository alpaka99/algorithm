import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    
    # N 총 블록의 갯수, M1 타워1의 블록갯수, M2 타워2의 블록갯수
    N, M1, M2 = map(int, input().split())

    # 블록 무게를 저장해놓음
    blocks = list(map(int, input().split()))

    # 탑의 비용은 높이 * 무게의 합
    # 최소비용은?

    # 걍 sort한 다음에 하나씩 분배하면 되지않냐
    # 이게 맞는데 높이가 다를 수 있어서 하나씩 돌아가면서 분배
    blocks.sort()
    
    m1_list = []
    m2_list = []

    m1_height = 0
    m2_height = 0

    # 둘에 하나씩 뒤부터 넣다가 둘 중 하나가 다 차면 비어있는거에 몰아넣음
    while m1_height < M1 and m2_height < M2:
        m1_list.append(blocks.pop())
        m2_list.append(blocks.pop())
        m1_height += 1
        m2_height += 1

    # 남아있으면
    if blocks:
        # 비어있는곳 확인
        # m1이 비어있다
        if 0 in m1_list:
            while blocks:
                m1_list.append(blocks.pop())
        # m2가 비어있다
        else:
            while blocks:
                m2_list.append(blocks.pop())

    #print(m1_list, m2_list)
    cost = 0
    # 가격 더하기
    for i in range(len(m1_list)):
        cost += m1_list[i]*(i+1)

    for i in range(len(m2_list)):
        cost += m2_list[i]*(i+1)

    print(cost)