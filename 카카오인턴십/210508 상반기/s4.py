min_val = 987654321
def solution(n, start, end, roads, traps):
    answer = 0
    start -= 1
    end -= 1
    for road in roads:
        road[0], road[1] = road[0]-1, road[1]-1

    for i in range(len(traps)):
        traps[i] -= 1
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    maze = [[ 0 for _ in range(n)] for _ in range(n)]
    trap_status = [False for _ in range(n)]
    for road in roads:
        maze[road[0]][road[1]] = road[2]
        matrix[road[0]][road[1]] = road[2]

    # min_val = 987654321

    def dfs(s:int, end:int, total:int):
        global min_val
        if s == end:
            min_val = min(min_val, total)
            return

        if total >= min_val:
            return

        if maze[s][end]:
            dfs(end, end, total + maze[s][end])

        for i in range(n):
            # 길이 있는데
            if maze[s][i]:
                # 함정이면
                # 함정과 연결된 모든 방이 반대가 됨
                if i in traps:
                    tmp = maze[s][i]
                    if trap_status[i] == False:
                        trap_activate(i)
                        trap_status[i] = True
                        dfs(i, end, total + tmp)
                        trap_status[i] = False
                        trap_activate(i)
                    else:
                        trap_status[i] = False
                        history = trap_deactivate(i)
                        dfs(i, end, total + tmp)
                        trap_reverse_deactivate(i, history)
                        trap_status[i] = True


                # 함정 아니면
                else:
                    dfs(i, end, total+maze[s][i])

    def trap_activate(c:int):
        N = len(maze)
        # 해당하는 행과 열만 전치시키면  trap 발동하는게 됨
        for k in range(N):
            maze[k][c], maze[c][k] = maze[c][k], maze[k][c]


    def trap_deactivate(c:int):
        N = len(maze)
        tmp = []
        for i in range(N):
            tmp.append([maze[i][c], maze[c][i]])
            maze[i][c] = matrix[i][c]
            maze[c][i] = matrix[c][i]
        return tmp

    def trap_reverse_deactivate(c:int, history:list):
        N = len(maze)
        for i in range(N):
            maze[i][c], maze[c][i] = history.pop(0)


    dfs(start, end, 0)

    answer = min_val
    return answer

print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))