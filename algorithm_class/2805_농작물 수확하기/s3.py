"""
소영님 방법으로 풀어보자
회문을 데칼코마니처럼 푸는 방법 -> 굉장히 좋은듯. stack으로 하는것보다 더 빠를것 같다.
"""

import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N = int(input())

    matrix = [list(map(int,input())) for _ in range(N)]

    # 데칼코마니를 어떻게 구현하셨더라...
    harvest = 0
    i = 1
    while i <= N//2:
        area_1 = matrix[(N//2)-i][i:N-i]
        area_2 = matrix[(N//2)+i][i:N-i]

        i += 1

        for j in range(len(area_1)):
            harvest += area_1[j]
            harvest += area_2[j]

    # 마지막으로 가운데 줄 더해줌

    for i in range(len(matrix[N//2])):
        harvest += matrix[N//2][i]


    print("#{} {}".format(tc,harvest))