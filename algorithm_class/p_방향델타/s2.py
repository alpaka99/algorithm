import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())

# # 1. 가장자리 제외
# for tc in range(1, T+1):
#     N = int(input())
#     
        # input matrix
#     matrix = [list(map(int,input().split())) for _ in range(N)]

        # 답안을 저장하는 ans
#     ans = 0

#     # 시계방향으로 델타를 설정
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]

        # 가장자리를 제외하는 상황이기때문에 for문의 범위를 제한해줬음
#     for i in range(1,N-1):
#         for j in range(1, N-1):
#             for k in range(4):
                    # 델타를 이용해 우리가 원하는 칸을 선택함
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 ans += abs(matrix[i][j] - matrix[nx][ny])
#     print(ans_matrix)


# 2. 가장자리 포함

for tc in range(1, T+1):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    #시계방향
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(N):
        for j in range(N):
            cur_abs = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    ans += abs(matrix[i][j] - matrix[nx][ny])

    print(ans)