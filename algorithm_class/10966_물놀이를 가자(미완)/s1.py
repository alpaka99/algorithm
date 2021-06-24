'''
runtime error뭐임... 
맨해튼 거리도 안돼
bfs도 안돼 뭐임
'''


import sys
sys.stdin = open('input.txt', 'r',encoding='utf8')

# def bfs(r,c):
#     queue = []
#     queue.append([r,c])
#     level = 0
#     visited = [[0 for _ in range(M)] for _ in range(N)]
#     visited[r][c] = 1
#
#     # 현재 queue size만큼만 돌리면서 길이를 1씩 늘려가자
#     while queue:
#         level += 1
#         size = len(queue)
#         for _ in range(size):
#             cur_r, cur_c = queue.pop(0)
#             for i in range(4):
#                 nr = cur_r + dr[i]
#                 nc = cur_c + dc[i]
#
#                 # 범위 밖
#                 if not(0 <= nr < N and 0 <= nc < M):
#                     continue
#
#                 # 범위 안
#                 if not(visited[nr][nc]):
#                     # 물을 찾음
#                     if matrix[nr][nc] == 'W':
#                         move[r][c] = level
#                         return
#                     # 물 못찾음
#                     else:
#                         visited[nr][nc] = 1
#                         queue.append([nr, nc])

# 이게 아니라 각 물의 위치를 저장하고 그냥 각 땅까지의 맨해튼 거리를 구하면 되는거 아님?


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # 우선 수영장을 입력받고
    matrix = [list(input()) for _ in range(N)]

    # 그러면 가장 가까운 물을 찾아야하는데 어떻게 찾아야하려나
    # 가장 가까운건 bfs지
    
    # 각 칸마다 얼마만큼 이동했는지 여기에 기록
    move = 0

    # delta, 위 오른쪽, 아래, 왼쪽
    # dr = [-1, 0, 1, 0]
    # dc = [0, 1, 0, -1]

    water = []

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                water.append([i, j])

    # 각 water까지의 맨해튼 거리를 구하고 최솟값을 넣음
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'L':
                shortest = 1000000
                for k in range(len(water)):
                    cur_water = water[k]
                    length = abs(i-cur_water[0]) + abs(j-cur_water[1])
                    if length < shortest:
                        shortest = length
                move += shortest




    print("#{} {}".format(tc, move))