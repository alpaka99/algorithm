"""
태어나서 처음으로 N-queens 방법으로 풀긴 했는데
내가 풀어놓고도 완벽히 이해 못함. 다시 생각하자
"""

import sys
sys.stdin = open('input.txt', 'r')

# 최솟값을 저장하는 변수
global min_val

# 각 행을 레벨로 생각해서 재귀를 돌려봤음
def level_min(visited, cur_sum, level):
    if level == N: # 마지막 단계까지 끝
        global min_val 
        if cur_sum < min_val: # 마지막까지 갔을때 다 더한 값이 현재 최솟값보다 작으면
            min_val = cur_sum
            return

    if cur_sum > min_val: # 중간합이 최소보다 커짐 -> 바로 탈출
        return
    
    # 아직 가능성이 있음
    for i in range(N): # 그 행의 0번부터 쭉 검사 시작
        if visited[i] == 0: # 같은 열에서 숫자를 고른적이 없으면
            cur_sum += matrix[level][i] 
            level += 1
            visited[i] = 1
            level_min(visited, cur_sum, level) # 아랫 단계로 이동
            visited[i] = 0 # 다시 이번 단계로 돌아와서 방문 흔적 지우기
            level -= 1
            cur_sum -= matrix[level][i]

    # for문을 다 돌았음
    return

for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int,input().split())) for _ in range(N)]

    # 순열 조합을 stack으로 푸는 재주가 없으니
    # n-queens 백트랙킹으로 풀어보자
    min_val = 100
    for i in range(N):
        visited = [0 for _ in range(N)]
        level = 0
        cur_sum = 0
        level_min(visited, cur_sum, level)

    print("#{} {}".format(tc,min_val))

