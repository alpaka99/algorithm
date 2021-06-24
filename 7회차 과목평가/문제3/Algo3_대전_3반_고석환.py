global robot_loc

def bfs(robot):
    queue = [robot]

    cnt = 0

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[robot[0]][robot[1]] = 1

    while queue:
        cnt += 1
        size = len(queue)
        for _ in range(size):
            # 아 이거 pop(0)을 안해서 틀렸던거였네
            r, c = queue.pop(0)
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                # 범위 벗어나는값 처리
                if not(0 <= nr < N and 0 <= nc < N):
                    continue

                if matrix[nr][nc] != 1:
                    if not(visited[nr][nc]):
                        # 여기서 그냥 칸인지 zone인지 체크
                        if matrix[nr][nc] != 0:
                            flags[matrix[nr][nc]] = [nr, nc]
                        else:
                            queue.append([nr, nc])
                            visited[nr][nc] = 1
        # 현재 간 칸중에 zone이 있을 경우
        for i in range(6):
            if flags[i]:
                # r,g,b 순으로 리스트를 보면서 zone을 벽으로 바꿔주고
                matrix[flags[i][0]][flags[i][1]] = 1
                # 로봇을 해당 위치로 이동시켜줌
                global robot_loc
                robot_loc = [flags[i][0], flags[i][1]]
                # 해당 색의 flag를 True로 만듬
                flag_collect[i-3] = True
                return cnt

    
for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 빈칸 0, 벽1, 로봇2, 레드3, 그린4, 블루5
    flags = [[] for _ in range(6)]

    red_flag = False
    green_flag = False
    blue_flag = False

    flag_collect = [red_flag, green_flag, blue_flag]

    # 통과한 zone은 이동중에 다시 못들어감 => 통과하면 벽으로 만들어버리자
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                robot_loc = [i, j]
                matrix[i][j] = 0
                break

    # delta
    # 위, 오, 아, 왼
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    answer = 0
    key = False
    while not(key):
        ans = bfs(robot_loc)
        flags = [[] for _ in range(6)]
        # print(ans, robot_loc)
        answer += ans
        key = flag_collect[0] and flag_collect[1] and flag_collect[2]
    print("#{} {}".format(tc,answer))



