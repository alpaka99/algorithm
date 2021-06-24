"""
1. 단방향이 내가 틀렸던 포인트! 기계적으로 코딩하지 말자
2. 인접 리스트는 파이썬에서는 굉장히 효율적이고 재밌다
"""

import sys

sys.stdin = open('input.txt', 'r')


def dfs(ad_list):
    # visited, stack 초기화 및 첫 vertex에 대한 입력 처리
    #visited = [0] * 100
    stack = [0]
    #visited[0] = 1

    # stack이 빌 떄 까지
    while len(stack):
        # 현재 vertex와 연결된 edge들 수
        cur_node = stack.pop()
        edge_num = len(ad_list[cur_node])

        for i in range(edge_num):
            # cur_node에 연결된 것들 중 하나를 지정
            tmp_node = ad_list[cur_node][i]
            # 만약 99로 연결되어있으면
            if tmp_node == 99:
                return 1
            # 만약 아직 99로 가는길이 발견되지 않았으면 dfs 속행
            # if not (visited[tmp_node]):
            #     visited[tmp_node] = 1
            #     stack.append(tmp_node)
            else:
                stack.append(tmp_node)
    # 완전탐색을 했는데 99로 가는길이 발견되지 않으면 return 0
    return 0



for _ in range(1, 11):
    tc, N = map(int, input().split())

    # vertex끼리의 연결을 저장한 리스트
    connections = list(map(int, input().split()))

    # 정점의 갯수는 최대 98개(1~98) + 시작(0) + 도착(99) = 100칸의 리스트 필요
    ad_list = [[] for _ in range(100)]

    # adjacent_list 채워넣기
    i = 0
    while i < len(connections):
        # 여기가 point: 방향성이 있기떄문에 양방향을 위한 추가작업 안해도 됨
        ad_list[connections[i]].append(connections[i + 1])
        i += 2

    print("#{} {}".format(tc, dfs(ad_list)))
