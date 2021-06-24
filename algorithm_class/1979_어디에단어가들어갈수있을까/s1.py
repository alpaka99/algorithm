"""
전치 행렬을 이용하여 풀어봤습니다.
"""
import sys
sys.stdin = open('input.txt', 'r')

# 딱 맞는 칸을 찾는 알고리즘
def fit(matrix,N, K):
    ans = 0
    for i in range(N):
        for j in range(N):
            # 일단 시작칸이 칠해져 있어야함
            if matrix[i][j]:
                count = 1
                # 범위를 벗어나지 않는 1로 칠해진 칸에 대하여
                while j + count < N and matrix[i][j+count]:
                    # 칸들을 지우면서 가야지 나중에 또 검사를 안함
                        matrix[i][j+count] = 0
                        count += 1
                if count == K:
                    ans += 1
    return ans

for tc in range(1, int(input())+1):
    # N by N  퍼즐, 길이 K의 단어
    N, K = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    cpy_matrix = [[0]*N for _ in range(N)]
    
    # 전치행렬 제작
    for i in range(N):
        for j in range(N):
            cpy_matrix[i][j] = matrix[j][i]



    garo = fit(matrix,N,K)
    cero = fit(cpy_matrix,N,K)
    print("#{} {}".format(tc,garo + cero))