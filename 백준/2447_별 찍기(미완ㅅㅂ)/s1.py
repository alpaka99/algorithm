import sys
sys.stdin = open('input.txt', 'r')
N = int(input())

matrix = [['*' for _ in range(N)] for _ in range(N)]

def draw(r_start:int,c_start:int,length:int):
    if length == 0:
        return

    for i in range(r_start//3,r_start//3+length):
        for j in range(c_start//3,c_start//3+length):
            matrix[i][j] = ' '

    n_length = length//3

    tmp_r = r_start//3
    for i in range(3):
        tmp_c = c_start//3
        for j in range(3):
            draw(tmp_r+(n_length)*i, tmp_c+(n_length)*j, n_length)

draw(N,N,N//3)
for i in range(N):
    print(*matrix[i])