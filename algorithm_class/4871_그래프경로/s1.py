"""
1.문희님, 근일님, 두호님 감사합니다
[[0]*N] -> 이렇게 하는것은 [0]을 얕은 복사를 조지는것!! 그래서 하나를 바꾸면 다 바뀜
따라서 [[0] for _ in range(N)] 이렇게 해줘야만 한다!

2. 그리고 이 문제는 방향이 존재한다!!
"""

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 반환할 값
    ans = 0
    
    V, E = map(int, input().split())
    
    # 인접리스트 구현
    ad_list = [[] for _ in range(51)]

    
    # 인접리스트에 연결된 vertex 채워넣기
    for _ in range(E):
        start, end = map(int, input().split())
        ad_list[start].append(end)

    # start, goal
    S, G = map(int, input().split())

    # stack의 초기값에 S를 넣어줌
    stack = [S]
    # visited
    visited = [0]*51
    visited[S] = 1
    
    # dfs 시작
    while len(stack):
        cur_node = stack.pop()
        # 현재 vertex의 연결된곳들에 대한 정보
        connected = ad_list[cur_node]
        
        # for문으로 돌아줌
        for i in range(len(connected)):
            # 만약 연결된 곳 중에 goal이 있으면
            if connected[i] == G:
                ans = 1
                stack = []
                break
            # 만약 연결된 곳이 없으면 다른 vertex들로 탐색 계속 진행
            if visited[connected[i]] != 1:
                stack.append(connected[i])
                visited[connected[i]] = 1

    print("#{} {}".format(tc,ans))