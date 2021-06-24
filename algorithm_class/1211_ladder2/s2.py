import sys
sys.stdin = open('input.txt', 'r')
global matrix
global visited

def find_route(cur_start):
    x = cur_start[0]
    y = cur_start[1]

    # 좌 우 하
    dx = [0, 0, 1]
    dy = [-1, 1, 0]

    # 시작점도 세줘야하나?
    count = 1


    # 길찾기 시작
    while x < 99:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                if matrix[nx][ny] and not(visited[nx][ny]):
                    #print(nx, ny)
                    # 방문 표시
                    visited[nx][ny] = 1
                    # 이동
                    count += 1
                    x = nx
                    y = ny
                    break

    return count, cur_start


for _ in range(1, 11):
    tc = int(input())

    # 가장 짧은 이동거리라....


    # 100 by 100
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 시작 지점들 저장
    start_points = []
    for i in range(100):
        if matrix[0][i] == 1:
            start_points.append([0,i])

    results = []

    # 시작 지점들에 대해서 검사를 해야함
    while start_points:
        cur_start = start_points.pop()

        # visited 초기화
        visited = [[0]*100 for _ in range(100)]

        # 아랫방향으로 진행하다가 좌우로 가능한 통로가 나오면 좌나 우로 가야함
        # 그리고는 다시 아래로 감
        # 도착점에 복수의 갯수가 들어갈 수 있구나 ㄷㄷ...

        results.append(find_route(cur_start))


    # 이제 최소 거리를 갖는 시작점을 찾아야함
    min_idx = 0
    min_length = results[0][0]


    for i in range(1, len(results)):
        if results[i][0] <= min_length:
            min_idx = i
            min_length = results[i][0]

    print("#{} {}".format(tc, results[min_idx][1][1]))
