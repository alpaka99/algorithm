import sys
#from pandas import DataFrame
sys.stdin = open('input.txt', 'r')

N = int(input())

# 1 입력받기
# 1.1 첫번째 방법
# matrix = []
# for i in range(N):
#     matrix.append(list(map(int, input().split())))
# print(matrix)

# 1.2 두번쨰 방법
# matrix = []
# for i in range(N):
#     matrix[i] = (list(map(int, input().split())))

# 1.3 세번째 방법
matrix = [list(map(int, input().split())) for _ in range(N)]
print(matrix)