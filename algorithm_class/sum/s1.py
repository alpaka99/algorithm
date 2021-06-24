import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    # test case 번호
    tc = int(input())
    
    # 100 x 100 크기의 2차원 배열 입력받음
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 가로 100개 세로 100개 대각선 2개
    cero = [0]*100
    garo = [0]*100
    diagonal_1 = 0
    diagonal_2 = 0
    
    # 처음부터 끝까지 한번만 훑으면 전체 matrix의 요소를 적절한곳에 싹 넣는 방법으로 해보자
    # 그냥 전체 matrix를 4번 훑는건 재미없잖아
    for i in range(100):
        for j in range(100):
            if i == j:
                diagonal_1 += matrix[i][j]
            if 99 - i == j:
                diagonal_2 += matrix[i][j]
            garo[i] += matrix[i][j]
            cero[j] += matrix[i][j]

    # garo와 cero사이에서 최고값 구하기
    max_value = 0
    for k in range(100):
        if garo[k] > max_value:
            max_value = garo[k]
        if cero[k] > max_value:
            max_value = cero[k]

    # 구한 최고값과 대각선값들을 비교해서 최종 최고값 도출하기
    if diagonal_1 > max_value:
        max_value = diagonal_1
    if diagonal_2 > max_value:
        max_value = diagonal_2
    print("#{} {}".format(tc, max_value))