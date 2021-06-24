import sys
from pandas import DataFrame as df
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    color_boxes = [list(map(int, input().split())) for _ in range(N)]

    matrix = [[0]*10 for i in range(10)]

    for color_box in color_boxes:
        # 구역 칠하기
        # 겹쳐도 가능하게끔 짜보자
        for i in range(color_box[0], color_box[2]+1):
            for j in range(color_box[1], color_box[3]+1):
                matrix[i][j] |= color_box[4]
    print(df(matrix))
    # 얼마만큼 보라색인지 판단            
    purple = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                purple += 1
    print("#{} {}".format(tc, purple))