import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def left(matrix:list):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 블록 더하기
    for i in range(N):
        for j in range(N):
            # 바운더리 설정
            if j+1 >= N:
                continue

            if matrix[i][j] == matrix[i][j+1] and not(visited[i][j]):
                matrix[i][j] *= 2
                matrix[i][j+1] = 0
                visited[i][j] = 1
    # 왼쪽으로 블록 몰기
    for i in range(N):
        for j in range(N):
            if j+1<N:
                if matrix[i][j] == 0:
                    n = 1
                    while matrix[i][j] == 0:
                        if j+n >= N-1:
                            break
                        matrix[i][j], matrix[i][j+n] = matrix[i][j+n], matrix[i][j]
                        n += 1

    return matrix



def right(matrix:list):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-1, -1, -1):
            # 바운더리 설정
            if j-1 < 0:
                continue

            if matrix[i][j] == matrix[i][j-1] and not(visited[i][j]):
                matrix[i][j] *= 2
                matrix[i][j-1] = 0
                visited[i][j] = 1

    # 오른쪽으로 블록 몰기
    for i in range(N):
        for j in range(N-1, -1, -1):
            if j+1<N:
                if matrix[i][j] == 0:
                    n = 1
                    while matrix[i][j] == 0:
                        if j-n < 0:
                            break
                        matrix[i][j], matrix[i][j-n] = matrix[i][j-n], matrix[i][j]
                        n += 1

    return matrix

def up(matrix:list):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N):
            # 바운더리 설정
            if i+1 >= N:
                continue

            if matrix[i][j] == matrix[i+1][j] and not (visited[i][j]):
                matrix[i][j] *= 2
                matrix[i+1][j] = 0
                visited[i][j] = 1

    # 위쪽으로 블록 몰기
    for j in range(N):
        for i in range(N):
            if i < N-1:
                if matrix[i][j] == 0 and matrix[i+1][j]:
                    matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]

    return matrix

def down(matrix:list):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for i in range(N - 1, -1, -1):
            # 바운더리 설정
            if i-1 < 0:
                continue

            if matrix[i][j] == matrix[i-1][j] and not (visited[i][j]):
                matrix[i][j] *= 2
                matrix[i-1][j] = 0
                visited[i][j] = 1

    # 아래쪽으로 블록 몰기
    for j in range(N):
        for i in range(N-1, -1, -1):
            if i>= 1:
                if matrix[i][j] == 0 and matrix[i-1][j]:
                    matrix[i][j], matrix[i-1][j] = matrix[i-1][j], matrix[i][j]

    return matrix

def move(board:list, level:int):
    if level == 6:
        local_max = max(max(board))
        global global_max
        global_max = max(global_max, local_max)
        return

    # move(left(board), level + 1)
    move(right(board), level + 1)
    # move(up(board), level + 1)
    # move(down(board), level + 1)

global_max = 0
move(board, 1)
print(global_max)



