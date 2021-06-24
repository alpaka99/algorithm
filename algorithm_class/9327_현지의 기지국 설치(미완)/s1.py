import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    # 기지국 설치 비용
    # index로 쓸려고 dummy data 0 맨앞에 넣음
    cost = [0]
    cost += list(map(int,input().split()))

    # 각 도시 기지국 설치 여부 표시
    built = [0 for _ in range(n+1)]

    # 기지국 통신쌍의 정보 시작기지국, 끝기지국, 이득 순
    info = [list(map(int, input().split())) for _ in range(m)]

    # 2차원 리스트로 만들어서 weight을 표현해야겠다.
    matrix = [[0]*(n+1) for _ in range(n+1)]
    for i in range(len(info)):
        # 일단은 이득만 넣고 나중에 설치되어있는걸 따로 표시하자
        matrix[info[i][0]][info[i][1]] = info[i][2] - cost[info[i][0]] - cost[info[i][1]]
    print(matrix)

    stack = []

    max_value = 0

    # 기지국 하나씩 다 넣어봐야 할듯
    for i in range(n):
        # 각각 기지국마다 시작함
        stack.append(i)
        # 내일 다시... 오늘은 일찍 자자
        #while stack: