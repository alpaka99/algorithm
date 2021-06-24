import sys
from pandas import DataFrame
sys.stdin = open('input.txt', 'r')

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]

# 현재 위치 -> (1, 1)
x = 1
y = 1


# 이동을 시키고 싶다...
# 상하 좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# print(DataFrame(matrix))
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N:
        continue