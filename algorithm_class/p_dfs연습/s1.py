import sys
sys.stdin = open('input.txt', 'r')


def dfs_adjacent_matrix(V, tmp):
    # 2차원 배열을 만들어서 연결된 방법을 나타내는 방법
    matrix = [[0]*(V+1) for _ in range(V+1)]

    # matrix 준비
    i = 0
    while i < len(tmp):
        matrix[tmp[i]][tmp[i+1]], matrix[tmp[i+1]][tmp[i]] = 1, 1
        i += 2

    # visited 준비
    visited = [0]*(V+1)

    # 시작점을 넣어주고
    stack = []
    stack.append(tmp[0])
    visited[tmp[0]] = 1

    # 기록
    time_line = []

    # dfs를 돌자
    while stack:
        cur_node = stack.pop()
        time_line.append(cur_node)


        # 현재 노드와 연결되어있는 노드를 다 스택에 넣어줌
        for i in range(V+1):
            # 연결되어있는데
            if matrix[cur_node][i] == 1:
                # 방문 안했으면
                if visited[i] == 0:
                    # 넣어줌
                    stack.append(i)
                    visited[i] = 1
    print("2차원 배열로 dfs:", *time_line)

def dfs_adjacent_list(V, tmp):
    # 배열안에 배열이 들어있는 형태로 만듬
    adjacent_list = [[] for _ in range(V+1)]

    i = 0
    while i < len(tmp):
        adjacent_list[tmp[i]].append(tmp[i+1])
        adjacent_list[tmp[i+1]].append(tmp[i])
        i += 2

    stack = []
    visited = [0 for _ in range(V+1)]
    time_line = []

    stack.append(tmp[0])
    visited[tmp[0]] = 1
    time_line.append(tmp[0])
    while len(stack):
        cur_node = stack.pop()
        for i in range(len(adjacent_list[cur_node])):
            if visited[adjacent_list[cur_node][i]] == 0:
                stack.append(adjacent_list[cur_node][i])
                visited[adjacent_list[cur_node][i]] = 1
                time_line.append(adjacent_list[cur_node][i])
    print("인접리스트로 하는 dfs:",*time_line)



    pass

def dfs_dictionary(V, tmp):
    # 연결을 나타내는 딕셔너리를 만들어주고
    connected = {}
    for i in range(1, V+1):
        connected[i] = []
    
    # 입력받은것에 따라 dictionary의 key 값을 찾아가서 value값에 append해줌
    i = 0
    while i < len(tmp):
        connected[tmp[i]].append(tmp[i+1])
        connected[tmp[i+1]].append(tmp[i])
        i += 2

    stack = []
    stack.append(tmp[0])

    visited = [0]*(V+1)
    visited[tmp[0]] = 1

    time_line = []

    # bfs 시작
    while len(stack):
        cur_node = stack.pop()
        time_line.append(cur_node)
        lines = connected[cur_node]
        
        #dictionary의 value의 뒷 값부터 검사 시작
        for i in range(len(lines)):
            # 방문 안했으면
            if not(visited[lines[i]]):
                # visited 체크, stack에 넣기
                visited[lines[i]] = 1
                stack.append(lines[i])
    print("dictionary로 dfs는",*time_line)


V, E = map(int, input().split())

tmp = list(map(int, input().split()))


dfs_adjacent_matrix(V, tmp)

dfs_adjacent_list(V, tmp)

dfs_dictionary(V, tmp)


