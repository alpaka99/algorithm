import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
ans = []
def check(r_start:int, c_start:int, length:int):
    for i in range(r_start, r_start+length):
        for j in range(c_start, c_start+length):
            if matrix[i][j]:
                ans.append('(')
                check(r_start)
