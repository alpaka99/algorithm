"""
순열 조합으로도 풀 수 있고 ( 대진님)
DP로도 풀 수 있다.(다은님)
"""


import sys
sys.stdin = open('input.txt', 'r')


# 재귀적인 dp
def dp(r:int, c:int, N:int):
    # 재귀함수 탈출 조건
    if r == N-1 and c == N-1:
        return matrix[r][c]
    
    # 아래 오른쪽 다 갈 수 있을떄
    if r+1 < N and c+1 < N:
        down = dp(r+1, c, N)
        right = dp(r, c+1, N)
        return matrix[r][c] + min(down, right)

    # 아래만 갈 수 있을떄
    elif r+1 < N and N <= c+1:
        down = dp(r + 1, c, N)
        return matrix[r][c] + down

    # 오른쪽만 갈 수 있을떄
    elif N <= r+1 and c+1 < N:
        right = dp(r, c + 1, N)
        return matrix[r][c] + right


    

for tc in range(1, int(input())+1):
    # 맨 왼쪽 위에서 맨 오른쪽 아래까지 이동
    # 지나는 칸에 써진 숫자의 합계가 최소
    # 시간 초과를 줄이는 부분으로 생각해야 스텝업 할 수 있다

    # 가로 세로 칸 수
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]


    print("#{} {}".format(tc,dp(0,0,N)))

