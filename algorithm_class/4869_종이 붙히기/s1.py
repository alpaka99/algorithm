"""
재귀함수
전형적인 dp문제
"""

import sys
sys.stdin = open('input.txt', 'r')

# 재귀함수 구현
def paper_plz(N, memo):
    if N <= 1:
        return memo[N]
    
    # 만약 이미 memo에 값이 있으면
    if memo[N] != 0:
        return memo[N]
    
    # 만약 memo에 값이 없으면
    # memo에 N에 대한 값을 계산해서 넣어줌
    memo[N] = paper_plz(N-1,memo) + paper_plz(N-2,memo)*2
    
    # 자신의 memo값을 return
    return memo[N]

for tc in range(1, int(input())+1):
    N = int(input())
    # 계산하기 편하게 N을 10으로 나눠줌
    N //=10
    # 10 x 20, 20 x 20
    # memoization?
    # memoization list를 N의 크기만큼 만듬
    memo = [0]*(N+1)
    
    # 가장 첫 값을 넣어줌
    memo[0] = 1
    memo[1] = 1

    print("#{} {}".format(tc,paper_plz(N,memo)))
