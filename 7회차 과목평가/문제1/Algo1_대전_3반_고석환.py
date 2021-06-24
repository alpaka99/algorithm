for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    bomb = [list(map(int, input().split())) for _ in range(M)]

    # delta
    #위.왼, 위.오, 아.왼, 아.오
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, -1, 1]


    visited = [[0 for _ in range(N)] for _ in range(N)]

    cnt = 0
    while bomb:
        cur_bomb = bomb.pop()
        r, c, area = cur_bomb
        # 0부터 범위까지를 체크해야함
        for i in range(area+1):
            for j in range(4):
                nr = r + dr[j]*i
                nc = c + dc[j]*i

                # 범위 벗어나는것 예외처리
                if not(0 <= nr < N and 0 <= nc < N):
                    continue


                if not(visited[nr][nc]):
                    cnt += matrix[nr][nc]
                    visited[nr][nc] = 1

    print("#{} {}".format(tc,cnt))