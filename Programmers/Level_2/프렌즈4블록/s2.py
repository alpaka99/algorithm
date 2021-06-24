global dr, dc

def find_2by2(m:int, n:int,board:list):
    to_be_deleted = []

    global dr, dc

    for i in range(n-1):
        for j in range(m-1):
            standard = board[i][j]
            tmp = []
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if board[nr][nc] == standard:
                    tmp.append([nr, nc])
                else:
                    break
            if len(tmp) == 4:
               to_be_deleted.append(tmp)
    return to_be_deleted


def delete_2by2(board:list, to_be_deleted:list):
    for eles in to_be_deleted:
        for ele in eles:
            r, c = ele
            board[r][c] = ''
    return


def fix_board(board:list, m:int, n:int):
    delete_cnt  = 0
    for i in range(n):
        j = 0
        cur_cnt = 0
        while j < len(board[i]):
            if board[i][j] == '':
                del(board[i][j])
                cur_cnt += 1
            else:
                j += 1
        for k in range(cur_cnt):
            board[i].append('')
        delete_cnt += cur_cnt
    return delete_cnt

def solution(m, n, board):
    answer = 0
    new_board = []

    # 왼위, 오위, 왼아, 오아
    global dr, dc
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]

    # split_board = board

    # list연산을 편하게 하기 위해서 이렇게 옆으로 눕힘
    for j in range(n):
        line = []
        for i in range(m):
            line.append(board[i][j])
        new_board.append(line)

    while True:
        to_be_deleted = find_2by2(m, n, new_board)
        delete_2by2(new_board, to_be_deleted)
        ans = fix_board(new_board, m, n)
        print(new_board)
        break




print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
# print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))