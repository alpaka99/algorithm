import sys
sys.stdin = open('input.txt', 'r')

# 재귀함수로 짤거임
# maximum depth 넘는거는 내가 잘못짠거 아님?
def harvest(matrix, visited, start_point):

    # 상 좌 하 우
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    product = 0
    new_start_point = []


    while start_point:
        print(start_point)
        # 탈출 조건
        if not (0 <= start_point[0][0] < N and 0 <= start_point[0][1] < N):
            return 0

        # 시작점 잡고 리스트에서는 뺴줌
        x = start_point[0][0]
        y = start_point[0][1]
        start_point.pop(0)

        # 델타로 주위를 돌며 밭을 봄
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 방문하지 않았으면 수확
            if 0 <= nx < N and 0 <= ny < N:
                if not(visited[nx][ny]):
                    product += matrix[nx][ny]
                    visited[nx][ny] = 1
                    new_start_point.append([nx, ny])

    return harvest(matrix, visited, new_start_point) + product

        

for tc in range(1, int(input())+1):
    # n by n 농장, n 은 홀수
    # 농장에 딱 맞는 마름모로만 수확
    N = int(input())

    # delta로 계속 재귀하면 될 것 같은데?



    # matrix input 과 visited matrix
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # 출발점을 넣은 list, 여기다가 계속 시작점을 추가해나갈 예정
    start_point = [[N//2 + 1, N//2 + 1]]

    ans = harvest(matrix, visited, start_point) + matrix[start_point[0][0],start_point[0][1]]
    print(ans)
