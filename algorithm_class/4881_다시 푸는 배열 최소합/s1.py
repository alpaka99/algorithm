import sys
sys.stdin = open('input.txt', 'r')

global min_val

def add_matrix(visited:list, level:int, total:int):
    if level == N:
        global min_val
        min_val = min(total, min_val)
        return
    
    # 재현님식 회심의 백트랙킹
    if total >= min_val:
        return

    for i in range(len(visited)):
        if not(visited[i]):
            visited[i] = 1
            add_matrix(visited, level+1, total+matrix[level][i])
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited = [0 for _ in range(N)]

    min_val = 10*N

    add_matrix(visited, 0, 0)

    print("#{} {}".format(tc,min_val))