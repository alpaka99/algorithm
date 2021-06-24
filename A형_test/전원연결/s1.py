import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

global shortest

# 아직 연결 안된것들 중 선택지가 가장 적은것 부터 해버려야할것 같은데?
# 이걸 매 반복마다 검색해야겠다
# def route_num(pm:int):
#     # 아직 연결 안된 core1, core2, core3, core4... 이런 순서대로 cores에 저장되어있음
#     core_dict = {}
#     for i in range(len(cores)):
#         core_dict[i] = []
#
#     # 각 코어마다 방향 찾기
#     for i in range(len(cores)):
#         cur_r, cur_c = cores[i]
#         direction_cnt = 0
#         way = []
#         # 4방으로 봄
#         for j in range(4):
#             # 해당 방향이 뚫려있는지 확인
#             length = 1
#             while length < N+2:
#                 nr = cur_r + dr[j]*length
#                 nc = cur_c + dc[j]*length
#                 # 만약 다른 코어를 만남
#                 if matrix[nr][nc] == 1:
#                     break
#                 # 연결 가능
#                 if matrix[nr][nc] == 2:
#                     way.append(j)
#                     direction_cnt += 1
#                     break
#                 # 아직 모름
#                 if matrix[nr][nc] == 0:
#                     length += 1
#         # 몇가지로 연결 가능한지랑 어디로 가야하는지도 넣자
#         # 연결 가능성이 0이면 안넣음
#         if direction_cnt == 0:
#             continue
#         core_dict[i].append([direction_cnt,way])
#     return core_dict



# 그냥 순열조합으로 하자
def connect_cores(cores:list):
    total = 0
    while cores:
        cur_core = cores.pop()
        cur_shortest = N+2
        for i in range(4):
            ans = shortest_connected(cur_core[0], cur_core[1],i)
            if ans:
                if ans < cur_shortest:
                    cur_shortest = ans

        total += cur_shortest
    return total


def shortest_connected(r, c, i):
    length = 1
    trail = []
    while length < N+2:
        nr = r + dr[i] * length
        nc = r + dc[i] * length

        # 전선 안겹침
        if matrix[nr][nc] == 0:
            matrix[nr][nc] = 1
            trail.append([nr,nc])
            length += 1
            # 길에 다른 코어 존재
        elif matrix[nr][nc] == 1:
            # 왔던 길을 다시 0으로 칠해줘야함
            while trail:
                fix_r, fix_c = trail.pop()
                matrix[fix_r][fix_c] = 0
            return 0
        elif matrix[nr][nc] == 2:
                return length



# 순열 조합중에 가장 연결 많이 되는것 구하고 그것의 최소 거리를 구하면 되는거 아님?
    
for tc in range(1, int(input())+1):
    N = int(input())
    matrix = []
    matrix.append([2 for _ in range(N+2)])
    for _ in range(N):
        matrix.append([2]+list(map(int, input().split()))+[2])
    matrix.append([2 for _ in range(N+2)])
    shortest = N*N
    
    #print(matrix)

    # 최대한 많은 core를 전원에 연결하였을 경우
    # 전원이 연결되지 않는 core가 있을 수 있다.
    # 전선은 직선만 가능
    # 전선 길이의 최소
    # N-queens?

    # visited = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

    #  전체 코어 찾기 + 이미 연결된 코어는 표시-> 아직 연결 안된 코어들만 찾기
    cores = []
    for i in range(N+2):
        for j in range(N+2):
            if matrix[i][j]==1:
                if j == 1 or j == N: # 가장 왼쪽 혹은 오른쪽의 코어들
                    # visited[i][j] = 1
                    continue
                if i == 1 or i == N: # 가장 윗줄에 있는 코어들
                    # visited[i][j] = 1
                    continue

                # 가장자리가 아닌 코어들
                cores.append([i,j])

    # delta 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 순열
    pm = list(permutations(cores, len(cores)))

    for i in range(len(pm)):
        ans = connect_cores(list(pm[i]))
        if ans < shortest:
            shortest = ans

    print(shortest)



