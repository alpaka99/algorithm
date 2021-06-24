"""
stack 없는 dfs
"""
import sys
sys.stdin = open('input.txt', 'r')

global visited
global time_line

def dfs(matrix, cur_node):
    global time_line
    for i in range(len(matrix)):
        if matrix[cur_node][i] == 1:
            if visited[i] == 0:
                visited[i] = 1
                time_line.append(i)
                dfs(matrix, i)
    return



V, E = map(int, input().split())
tmp = list(map(int, input().split()))

matrix = [[0]*(V+1) for _ in range(V+1)]

i = 0

# init matrix
while i < len(tmp):
    matrix[tmp[i]][tmp[i+1]] = 1
    matrix[tmp[i+1]][tmp[i]] = 1
    i += 2

visited = [0]*(V+1)
visited[tmp[0]] = 1
time_line = []
time_line.append(tmp[0])
dfs(matrix, tmp[0])
print("재귀 dfs로는 ",*time_line)
