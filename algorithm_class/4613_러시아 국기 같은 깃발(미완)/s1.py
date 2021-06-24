import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

# 해당 라인에 가장 많은 색이 무엇인지를 반환해주는 함수
def count_most(line: list):
    color_dict = {'R': 0, 'B': 0, 'W': 0  }
    for i in range(len(line)):
        color_dict[line[i]] += 1
    color_list = sorted(color_dict.items(), key=lambda x: x[1])
    return color_list[-1][0]

# 가장 파란색이 많은 줄 번호를 반환
def most_blue_line():
    blue_max = 0
    line_idx = 0
    for i in range(N):
        cur_blue = 0
        for j in range(M):
            if matrix[i][j] == 'B':
                cur_blue += 1
        if cur_blue > blue_max:
            blue_max = cur_blue
            line_idx = i
    return line_idx

for tc in range(1, int(input())+1):
    # N행 M열 국기
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    total_change = 0

    # 첫 줄
    for i in range(M):
        if matrix[0][i] != 'W':
            total_change += 1
            matrix[0][i] = 'W'

    # 마지막 줄
    for i in range(M):
        if matrix[N-1][i] != 'R':
            total_change += 1
            matrix[N-1][i] = 'R'

    # 파란색이 가장 많은 줄을 찾고 그 줄을 파란색으로 바꿔줌
    # blue_line = most_blue_line()
    # for j in range(M):
    #     if matrix[blue_line][j] != 'B':
    #         matrix[blue_line][j] = 'B'
    #         total_change += 1
    
    blue_lines = []
    
    # 파란줄로 바뀔 line들을 고름
    for i in range(1,N-1):
        line_color = count_most(matrix[i])
        if line_color == 'B':
            blue_lines.append(i)

    blue_lines.sort()
    # 정렬한 것 중 가장 작은 값의 위는 다 흰색,
    for i in range(1,blue_lines[0]):
        for j in range(M):
            if matrix[i][j] != 'W':
                matrix[i][j] = 'W'
                total_change += 1


    # 가장 큰 값의 아래는 다 붉은색
    for i in range(blue_lines[-1]+1, N):
        for j in range(M):
            if matrix[i][j] != 'R':
                matrix[i][j] = 'R'
                total_change += 1

    # 그 사이는 다 파란색
    for i in range(blue_lines[0], blue_lines[-1]+1):
        for j in range(M):
            if matrix[i][j] != 'B':
                matrix[i][j] = 'B'
                total_change += 1
    print(matrix)
    print(total_change)