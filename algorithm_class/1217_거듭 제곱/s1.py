import sys
sys.stdin = open('input.txt', 'r')

# 재귀함수
def solution(level: int) -> int:
    # 탈출조건
    if level == M:
        return N
    # 한단계 더 들어가자
    return solution(level+1)*N

for _ in range(1, 11):
    tc = int(input())

    N, M = map(int, input().split())

    print("#{} {}".format(tc, solution(1)))