def solution(places):
    answer = []

    # # 파티션 주위를 다 x처리하고 남은 자리중에 곂치는 사람이 있나 확인?

    for place in places:
        # 행렬 만들어 주고
        matrix = [[0 for _ in range(5)] for _ in range(5)]

        for i in range(5):
            for j in range(5):
                matrix[i][j] = place[i][j]

    # # delta : 상하좌우
    dr1 = [-1, 1, 0, 0]
    dc1 = [0, 0, -1, 1]

    def check_level_1(r:int, c:int):
        N = len(matrix)
        for k in range(4):
            nr = r + dr1[k]
            nc = c + dc1[k]

            if not(0<=nr<N and 0<=nc<N):
                continue

            if matrix[nr][nc] == 'P':
                return False
        return True

    # 맨 위부터 시계방향
    dr2 = [-2, -1, 0, 1, 2, 1, 0, -1]
    dc2 = [0, 1, 2, 1, 0, -1, -2, -1]

    check_r = [[-1], [-1,0], [0], [0, 1], [1], [0, 1], [0], [-1, 0]]
    check_c = [[0], [0, 1], [1], [0 ,1], [0], [-1, 0], [-1], [-1,0]]
    def check_level_2(r:int, c:int):
        N = len(matrix)

        for k in range(8):
            nr = r + dr2[k]
            nc = c + dc2[k]

            if not(0<=nr<N and 0<=nc<N):
                continue

            if matrix[nr][nc] == 'P':
                for l in range(len(check_r[k])):
                    nnr = r + check_r[k][l]
                    nnc = c + check_c[k][l]
                    if matrix[nnr][nnc] != 'X':
                        return False
        return True

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 'P':
                ans = check_level_1(i,j)
                if ans == True:
                    ans = check_level_2(i,j)
                    if ans:
                        print(1)
                    else:
                        print(0)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
