import sys
sys.stdin = open('input.txt', 'r')

def drop(N:int,c:int):
    # 맨 윗칸에 있을때 블록 하강 시작
    if matrix[0][c]:
        pos = 0 # 맨 끝블록의 위치가 기준
        block_size = 1
        while pos < N: # while문을 빠져나오면 하강 중지
            if not(pos+1 < N):
                break

                # 다른 블록이랑 맞닿음
            if matrix[pos+1][c]:
                size = check_block_size(pos+1,c)
                # 다음에 또 움직일 수 있음
                force = check_drop_force(pos,c,block_size)
                if force > size:
                    pos += size # 포인터를 제일 아래블록으로 만듬
                    block_size += size
                    # 만난 블록이 더 커서 못움직임
                else:
                    break
                # 다른 블록을 안맞남
            else:
                drop_block(pos,c,block_size)
                pos += 1

def check_block_size(i:int,j:int):
    size = 0
    while i < N:
        if matrix[i][j]:
            size += 1
            i+=1
        else:
            break
    return size

def check_drop_force(pos:int,j:int,size:int):
    force = 0
    for i in range(size):
        force = force + matrix[pos-i][j]
    return force

def drop_block(pos:int, j:int, size:int):
    for i in range(size):
        matrix[pos-i+1][j] = matrix[pos-i][j]*1.9
        matrix[pos-i][j] = 0



for tc in range(1,11):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 떨구고
    # print(matrix)
    for c in range(N):
        drop(N,c)
    new_matrix = [[0 for _ in range(N)] for _ in range(N)]
    # print(matrix)

    # 전치하고
    for i in range(N):
        for j in range(N):
            if matrix[j][i]:
                new_matrix[i][j] = 1
    matrix = new_matrix

    # 다시 떨구고
    for c in range(N):
        drop(N,c)

    total_down, total_right = 0, 0
    for i in range(N):
        if matrix[N-1][i]:
            total_down += 1
    for i in range(N):
        if matrix[i][N-1]:
            total_right += 1

    print("#{} {} {}".format(tc, total_right, total_down))