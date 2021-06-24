import sys
sys.stdin = open('input.txt', 'r')

trash_count = 0
matrix = []

def garo_tic():
    # 회문처럼 양 끝에서 접어들어오면 더 빠르게 볼 수 있을듯
    for i in range(4):
        same_flag = True
        # 4칸 중 1개라도 . 이 있으면 안됨
        if '.' in matrix[i]:
            continue

        if matrix[i].count('X') == 4 or matrix[i].count('O') == 4:
            return matrix[i][0]
        if matrix[i].count('X') == 3 or matrix[i].count('O') == 3:
            if 'T' in matrix[i]:
                if matrix[i][0] == 'T':
                    return matrix[i][1]
                else:
                    return matrix[i][0]


def diagonal_tic():
    # 대각 윗왼-아래오
    list_1 = []
    i = 0
    j = 0
    while i < 4:
        list_1.append(matrix[i][j])
        i += 1
        j += 1

    # 대각 윗오-아래왼
    i = 0
    j = 3
    list_2 = []
    while i < 4:
        list_2.append(matrix[i][j])
        i += 1
        j -= 1

    if '.' in list_1:
        list_1 = []
    if list_1:
        if list_1.count('X') == 4 or list_1.count('O') == 4:
            return list_1[0]
        if list_1.count('X') == 3 or list_1.count('O') == 3:
            if 'T' in list_1:
                if list_1[0] == 'T':
                    return list_1[1]
                else:
                    return list_1[0]

    if '.' in list_2:
        list_2 = []
    if list_2:
        if list_2.count('X') == 4 or list_2.count('O') == 4:
            return list_2[0]
        if list_2.count('X') == 3 or list_2.count('O') == 3:
            if 'T' in list_2:
                if list_2[0] == 'T':
                    return list_2[1]
                else:
                    return list_2[0]



T = int(input())

for tc in range(1, T+1):
    # 항상 4 x 4
    matrix = [list(input()) for _ in range(4)]

    # trash
    if trash_count < T-1:
        trash_input = input()
        trash_count += 1

    # 가로검사
    ans = garo_tic()
    if ans:
        print("#{} {} won".format(tc,ans))
        continue

    # 세로로 바꿈
    for i in range(4):
        test = list(zip(*matrix))
    matrix = test
    # 세로검사
    ans = garo_tic()
    if ans:
        print("#{} {} won".format(tc, ans))
        continue

    # 대각 검사
    ans = diagonal_tic()
    if ans:
        print("#{} {} won".format(tc, ans))
        continue

    # 가로세로대각이 없으면
    if ans == None:
        dot_flag = False
        for i in range(4):
            if '.' in matrix[i]:
                dot_flag = True
                break
        if dot_flag == True:
            print('#{} Game has not completed'.format(tc))
        else:
            print('#{} Draw'.format(tc))