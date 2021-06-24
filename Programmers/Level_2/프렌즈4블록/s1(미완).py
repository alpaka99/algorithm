global dr, dc

def find_2by2( m:int, n:int, board:list):
    # 삭제할 사각형의 왼쪽 윗 부분을 저장
    delete_pos = []

    for i in range(m-1):
        for j in range(n-1):
            if not(board[i][j].isalpha()):
                continue

            # 4개씩 저장
            tmp = []

            for k in range(4):
                tmp.append(board[i+dr[k]][j+dc[k]])


            # 4개가 다같은지 확인
            result = list(filter(lambda x: x == tmp[0], tmp))

            # 4개가 다 같으면 delete_pos에 왼쪽 위의 위치 저장
            if len(result) == 4:
                delete_pos.append([i, j])

    return delete_pos



def delete_2by2(board:list, delete_pos:list, m:int, n:int):
    visited = [[0 for _ in range(m)] for _ in range(n)]

    delete_cnt = 0

    for i in range(len(delete_pos)):
        r,c = delete_pos[i]
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if nr-1 >= 0:
                if not(visited[nr][nc]):
                    board[nr][nc], board[nr-1][nc] = board[nr-1][nc], ''
                    visited[nr][nc] = 1
                    delete_cnt += 1
            else:
                board[nr][nc] = ''
    return delete_cnt


def fix_board(board:list, i:int, j:int):
    # 2칸위에 요소가 있으면 2칸 위에 있는 요소를 가져와서 넣어줌
    if i-2 >= 0:
        board[i][j], board[i-2][j] = board[i-2][j], board[i][j]
    # 없으면 그냥 빈칸을 넣어줌
    else:
        board[i][j] = ' '

def solution(m, n, old_board):
    answer = 0
    # 파리채 문제처럼 봐야하려나...

    # 왼위, 오위, 왼아, 오아
    global dr, dc
    dr = [0, 0, 1, 1]
    dc = [0, 1, 0, 1]

    global friends
    # friends = ['R', 'M', 'A', 'F', 'N', 'T', 'J', 'C', 'B']
    board = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(old_board[i][j])
        board.append(line)


    while True:
        delete_pos = find_2by2(m, n, board)
        ans = delete_2by2(board, delete_pos, m, n)

        if ans == 0:
            break
        else:
            answer += ans

    # print(board)

    return answer


# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
# print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]))