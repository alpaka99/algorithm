import sys
sys.stdin = open('input.txt', 'r')

trash_count = 0
matrix = []


def garo():
    for i in range(4):
        cur_line = matrix[i]
        if cur_line[0] == '.':
            continue
        elif cur_line[0] == 'X':
            count = 0
            for j in range(4):
                if matrix[i][j] == 'X' or matrix[i][j] == 'T':
                    count += 1
            if count == 4:
                return 'X'
        elif cur_line[0] == 'O':
            count = 0
            for j in range(4):
                if matrix[i][j] == 'O' or matrix[i][j] == 'T':
                    count += 1
            if count == 4:
                return 'O'
def cero():
    for i in range(4):
        cur_line = matrix[i]
        if cur_line[0] == '.':
            continue
        elif cur_line[0] == 'X':
            count = 0
            for j in range(4):
                if matrix[j][i] == 'X' or matrix[j][i] == 'T':
                    count += 1
            if count == 4:
                return 'X'
        elif cur_line[0] == 'O':
            count = 0
            for j in range(4):
                if matrix[j][i] == 'O' or matrix[j][i] == 'T':
                    count += 1
            if count == 4:
                return 'O'

def diagonal():
    # 왼-오 대각
    i = 0
    j = 0
    tmp = []
    while i < 4:
        tmp.append(matrix[i][j])
        i += 1
        j += 1

    if tmp[0] == '.':
        return

    count = 0
    for k in range(4):
        if tmp[0] == tmp[k] or tmp[k] == 'T':
            count += 1
    if count == 4:
        return tmp[0]
    # 오-왼 대각
    i = 0
    j = 3
    tmp = []
    while i < 4:
        tmp.append(matrix[i][j])
        i += 1
        j -= 1

    if tmp[0] == '.':
        return

    count = 0
    for k in range(4):
        if tmp[0] == tmp[k] or tmp[k] == 'T':
            count += 1
    if count == 4:
        return tmp[0]


def is_full():
    count = 0
    for i in range(4):
        for j in range(4):
            if not(matrix[i][j] == '.'):
                count += 1
    if count == 16:
        return True
    return False


def tic_tac_tom():
    # 가로 검사
    ans = garo()
    if ans == 'X' or ans == 'O':
        return ans

    # 세로 검사
    ans = cero()
    if ans == 'X' or ans == 'O':
        return ans

    # 대각검사
    ans = diagonal()
    if ans == 'X' or ans == 'O':
        return ans

T = int(input())

for tc in range(1, T+1):
    # 항상 4 x 4
    matrix = [list(input()) for _ in range(4)]

    # trash
    if trash_count < T-1:
        trash_input = input()
        trash_count += 1


    real_ans = tic_tac_tom()

    if real_ans:
        if real_ans == 'X':
            print("#{} X Won".format(tc))
        elif real_ans == 'O':
            print("#{} O won".format(tc))
    else:
        if is_full():
            print("#{} Draw".format(tc))
        else:
            print("#{} Game has not completed".format(tc))

