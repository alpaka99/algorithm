""" 부분집합으로 풀어보자 """
import sys
sys.stdin = open('input.txt', 'r')


# 부분집합으로 나눠주는 재귀함수
def powerset(num_list: list, visited: list, tmp_1: list):
    if sum(visited) == N:
        return

    for i in range(K):
        if visited[i] == 0:
            tmp_1.append(num_list[i])
            visited[i] = 1
            powerset(num_list, visited, tmp_1)
            visited[i] = 0


for tc in range(1, int(input())+1):
    K, N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 각 숫자의 자리값으로 방문 체크
    visited = [0 for _ in range(K)]

