import sys
sys.stdin = open('input.txt', 'r')


def max_percent(total:float, level:int, N:int):
    global max_val
    if level == N:
        max_val = max(total, max_val)
        return

    if total <= max_val:
        return

    for i in range(N):
        if not(visited[i]):
            visited[i] = 1
            max_percent(total*percent[level][i]*0.01, level+1, N)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    # i번 사람이 j번 일을 성공할 확률을 퍼센트 단위로 나타냄
    percent = [list(map(int, input().split())) for _ in range(N)]

    # 직원이 일을 했나 안했나
    visited = [0 for _ in range(N)]

    max_val = 0

    # 모든 일이 성공할 확률이 최대화 될 떄의 확률
    max_percent(1,0,N)

    # 소수점 자리수 출력하는게 제일 어려웠음
    print("#{} {}".format(tc,format(max_val*100,".6f")))