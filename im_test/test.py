# 사각형 행렬 만든다음에 반만 그리는게 더 쉬울듯
def solution(n):
    answer = []
    matrix = [[0] * n for _ in range(n)]

    # 총 숫자의 갯수
    total = (n + 1) * n / 2

    # 아래로: r+1, 오른쪽으로: c+1, 대각선 위로: r-1, c-1
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    dir_vector = 0  # 한쪽 끝에 도달하거나 숫자를 만날때마다 이걸로 방향조정

    # 시작점은 항성 꼭대기
    r = 0
    c = 0

    i = 1
    while i <= total:
        if 0 <= r < n and 0 <= c < n and matrix[r][c] == 0:
            matrix[r][c] = i
            r += dr[dir_vector]
            c += dc[dir_vector]
            i += 1
        else:  # 다시 돌아와서 다음방향으로 가야함
            r -= dr[dir_vector]
            c -= dc[dir_vector]
            dir_vector = (dir_vector + 1) % 3  # 방향 전환
            r += dr[dir_vector]
            c += dc[dir_vector]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                answer.append(matrix[i][j])

    return answer


print(solution(4))