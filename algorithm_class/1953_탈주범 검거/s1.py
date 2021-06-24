import sys
sys.stdin = open('input.txt', 'r')


def bfs(r, c, L):
    if L == 1:
        return 1
    queue = [[r, c]]
    level = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[r][c] = 1

    while queue:
        size = len(queue)

        for _ in range(size):
            cur_r, cur_c = queue.pop(0)

            key = matrix[cur_r][cur_c]
            dr = dict_dr.get(key)
            dc = dict_dc.get(key)

            for i in range(len(dr)):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]

                if not(0 <= nr < N and 0 <= nc < M):
                    continue

                if matrix[nr][nc]:
                    if not(visited[nr][nc]):
                        if connected(cur_r, cur_c, nr, nc):
                            visited[nr][nc] = 1
                            queue.append([nr, nc])
        level += 1
        if level == L:
            break
    answer = 0
    for i in range(N):
        answer += sum(visited[i])

    return answer


# matrix의 r,c와 nr,nc가 연결되어있는지 확인하는 함수
def connected(cur_r, cur_c, nr, nc):
    new_key = matrix[nr][nc]

    new_dr = dict_dr.get(new_key)
    new_dc = dict_dc.get(new_key)

    for i in range(len(new_dr)):
        new_r = nr + new_dr[i]
        new_c = nc + new_dc[i]

        if (new_r == cur_r and new_c == cur_c):
            return 1

    return 0

for tc in range(1, int(input())+1):
    # 세로크기, 가로크기, 시작 세로위치, 시작 가로위치, 탈출 후 소요시간
    N, M, R, C, L = map(int, input().split())


    matrix = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0 for _ in range(M)] for _ in range(N)]

    # 총 7개 모양의 파이프
                # 상 하 좌 우    # 상 하      # 좌 우   # 상 우    #하 우    # 하 좌     # 상 좌
    dict_dr = {1:[-1, 1, 0, 0], 2:[-1, 1], 3:[0, 0], 4:[-1, 0], 5:[1, 0], 6:[1, 0], 7:[-1, 0]}
    dict_dc = {1:[0, 0, -1, 1], 2:[0, 0], 3:[-1, 1], 4:[0, 1], 5:[0, 1], 6:[0, -1], 7:[0, -1]}


    # bfs로 해보자
    print("#{} {}".format(tc,bfs(R,C,L)))