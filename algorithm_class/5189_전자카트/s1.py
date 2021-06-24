import sys
sys.stdin = open('input.txt', 'r')
global min_val

def find_route(cur_row:int, num_sum:int):
    # 탈출 조건
    if sum(visited) == N:
        global min_val
        tmp = matrix[cur_row][0]
        num_sum += tmp
        min_val = min(min_val, num_sum)


    for i in range(1, N):
        if not(visited[i]):
            visited[i] = 1
            num_sum += matrix[cur_row][i]
            # print(num_sum)
            find_route(i, num_sum)
            visited[i] = 0
            num_sum -= matrix[cur_row][i]


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # 방문처리
    visited = [0 for _ in range(N)]

    # 1은 맨 마지막에 돌아가야하니까 미리 1로 처리
    visited[0] = 1

    min_val = N*100

    find_route(0,0)
    print("#{} {}".format(tc,min_val))

    