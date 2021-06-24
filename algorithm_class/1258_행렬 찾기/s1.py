import sys

sys.stdin = open('input.txt', 'r')


def check_size(r, c):
    one_box = []
    # 아래 먼저 재고 그 다음에 가로를 잼
    for i in range(2):
        nr = r
        nc = c
        length = 0
        # 범위 내에서
        while 0 <= nr < N and 0 <= nc < N:
            if matrix[nr][nc] == 0:  # 화학물질통이 아니면
                break
            else:  # 화학물질통이면
                # visited[nr][nc] = 1
                length += 1
                nr = r + dr[i] * length
                nc = c + dc[i] * length
        one_box.append(length)
    # 가로 세로 한줄만 visited 처리가 된 것을 여기서 다 visited처리해줌
    for i in range(one_box[0]):
        for j in range(one_box[1]):
            visited[r + i][c + j] = 1
    return one_box


for tc in range(1, int(input()) + 1):
    # N by N
    N = int(input())

    # 창고
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 방문 기록
    visited = [[0] * N for _ in range(N)]

    # 아래, 오른쪽
    dr = [1, 0]
    dc = [0, 1]
    # 크기를 저장하는 배열
    boxes = []
    box_cnt = 0

    # 탐색을 한 부분은 visited로 표시해서 안가게끔 함
    for i in range(N):
        for j in range(N):
            if not (visited[i][j]):
                # 왼쪽 위 모서리 발견
                if matrix[i][j]:
                    box = check_size(i, j)
                    boxes.append(box)

    # 크기가 같을 경우 행이 작은 순으로 정렬
    sorted_boxes = sorted(boxes, key = lambda x: x[0])
    sorted_boxes = sorted(sorted_boxes, key=lambda x: x[0] * x[1])

    print("#{} {}".format(tc, len(boxes)), end=' ')
    for i in range(len(sorted_boxes)):
        print("{} {}".format(sorted_boxes[i][0], sorted_boxes[i][1]), end=' ')
    print()
