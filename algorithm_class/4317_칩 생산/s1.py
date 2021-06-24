import sys
sys.stdin = open('input.txt','r')

for tc in range(1, int(input())+1):
    H, W = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(H)]

    global_max = 0

    for _ in range(4):
        # 회전 0
        local_max = 0
        visited = [[0 for _ in range(W)]for _ in range(H)]

        for i in range(H):
            for j in range(W):
                visited[i][j] = matrix[i][j]

        for i in range(H-1):
            for j in range(W-1):
                if visited[i][j] == 0 and visited[i+1][j] == 0 and visited[i][j+1] == 0 and visited[i+1][j+1] == 0:
                    visited[i][j], visited[i+1][j], visited[i][j+1], visited[i+1][j+1] = 1, 1, 1, 1
                    local_max += 1
        global_max = max(global_max, local_max)


        # 90도 회전
        local_max = 0
        visited = [[0 for _ in range(H)] for _ in range(W)]

        # 회전 로직
        visited = [list(each) for each in zip(*matrix)]

        for i in range(W - 1):
            for j in range(H - 1):
                if visited[i][j] == 0 and visited[i + 1][j] == 0 and visited[i][j + 1] == 0 and visited[i + 1][j + 1] == 0:
                    visited[i][j], visited[i + 1][j], visited[i][j + 1], visited[i + 1][j + 1] = 1, 1, 1, 1
                    local_max += 1

        global_max = max(global_max, local_max)

        # 180도 회전
        local_max = 0

        a = [list(each) for each in zip(*matrix)]
        visited = [list(each) for each in zip(*a)]
        for i in range(H - 1):
            for j in range(W - 1):
                if visited[i][j] == 0 and visited[i + 1][j] == 0 and visited[i][j + 1] == 0 and visited[i + 1][j + 1] == 0:
                    visited[i][j], visited[i + 1][j], visited[i][j + 1], visited[i + 1][j + 1] = 1, 1, 1, 1
                    local_max += 1

        global_max = max(global_max, local_max)
    print("#{} {}".format(tc,global_max))

