import sys
sys.stdin = open('input1.txt', 'r')
#test case input
for tc in range(1, int(input())+1):
    # 행의 갯수 N, 열의 갯수 M
    N, M = map(int, input().split())
    
    # 열의 갯수로 한줄 씩 받아서 matrix 만들기
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 심은 나무의 수, 심는 총 비용, 가장 비싼 나무의 가격, 가장 비싼 나무가 심어진 열
    total_tree, total_price, max_tree, max_col = 0, 0, 0, 0
    # 이전 열에서 나무를 심었는지 아닌지를 판별해주는 flag 변수
    tree_flag = False
    # 열 우선 탐색
    for j in range(M):
        # 만약 이전 열에 나무를 심었으면, flag를 False로 바꿔준 후 이번 탐색은 skip
        if tree_flag == True:
            tree_flag = False
            continue
        # 만약 skip에서 안결렸으면 나무를 심는다
        for i in range(N):
            # 하나 심을때마다 total_tree += 1
            total_tree += 1
            # 심은 나무의 가격을 더해줌
            total_price += matrix[i][j]
            # 심은 나무가 가장 비싼나무인지 아닌지 판별
            if max_tree <= matrix[i][j]:
                max_tree = matrix[i][j]
                max_col = j
        # 한 줄을 다 심었으면 flag를 True로 바꿔줘서 다음줄은 skip하게 함
        tree_flag = True

    print("#{} {} {} {} {}".format(tc, total_price, total_tree, max_tree, max_col+1))

