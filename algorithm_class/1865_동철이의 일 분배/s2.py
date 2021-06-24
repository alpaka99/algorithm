import sys
sys.stdin = open('input.txt', 'r')
# 항상 1보다 작은 소수이므로 중간에 최소보다 작은값이 나오면 가지치기 할 수 있다
def dfs(row, total, N):
    global answer
    if row == N:
        if answer < total:
            answer = total
        return

    if total <= answer:
        return

    for col in range(N):
        if not check[col]:
            check[col] = True
            dfs(row+1, total*0.01*arr[row][col], N)
            check[col] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    check = [False for _ in range(N)]
    dfs(0, 1, N)
    answer *= 100
    print('#{} {}'.format(tc, format(answer, ".6f")))