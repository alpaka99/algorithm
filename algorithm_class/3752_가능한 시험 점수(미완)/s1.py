"""
상태공간 트리를 만들어서 사용해야한다
"""
import sys
sys.stdin = open('input.txt', 'r')

def tree_comb(num_sum:int, count:int):
    # 여기서 tree의 겹치는 노드는 미리 잘라내서 확인을 안하는게 좋다.
    for i in range(N):
        tmp = ''.join(visited)
        if tmp not in num_set:
            if not(visited[i]):
                visited[i] = '1'
                num_sum += scores[i]
                tree_comb(num_sum)
                visited[i] = '0'
                num_sum -= scores[i]

for tc in range(1, int(input())+1):
    # 문제의 갯수
    N = int(input())
    scores = list(map(int, input().split()))

    num_set = set()

    visited = ['0' for _ in range(N)]