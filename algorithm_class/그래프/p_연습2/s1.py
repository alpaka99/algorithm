"""
연습 문제2. dfs 구현
 - dfs 방식으로 그래프를 탐색하시오.
 - 알고리즘 구현은 반복과 재귀를 사용하시오.
"""

#1. 반복문
def dfs_iteration(s:int):
    stack = [s]

    while stack:
        vertex = stack.pop()
        print(vertex, end=' ')
        for v in ad_list[vertex]:
            if visited[v]:
                continue
            stack.append(v)
            visited[v] = 1



#2. 재귀 함수
def dfs_recursion(s:int):
    print(s, end=' ')
    for v in ad_list[s]:
        if visited[v]:
            continue
        visited[v] = 1
        dfs_recursion(v)


import sys
sys.stdin = open('input.txt')

# 정점, 간선 정보 초기화
V, E = map(int, input().split())
data = list(map(int, input().split()))

# 그래프, 방문 정보 초기화
ad_list = [[] for _ in range(V+1)]
for i in range(0,len(data),2):
    ad_list[data[i]].append(data[i+1])
    ad_list[data[i+1]].append(data[i])

# 방문 정보
visited = [0 for _ in range(V+1)]

# 그래프 그리기

# 탐색 시작
print('___iteration___')
dfs_iteration(1)
print()
visited = [0 for _ in range(V+1)]
print('___recursion___')
dfs_recursion(1)