"""
판 위에 코어들
판 둘레로 전원공급
전선은 직선으로만
가장 많은 코어가 전원이 연결되는 상황에서
가장 최소 길이의 전선은?
12
10
24
31
25
"""

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    
    # 주위에 둘러져있는 전원은 2로 표현
    matrix = [[2 for _ in range(N+2)]]
    for _ in range(N):
        matrix.append([2] + list(map(int,input().split()))+[2])
    matrix.append([2 for _ in range(N+2)])

    # 전원이 공급되지 않은 코어들을 저장해놓은 배열
    cores = []
    for i in range(2, N):
        for j in range(2, N):
            if matrix[i][j]:
              cores.append([i,j])



    




