import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

def garo(M, matrix):
    ans = 0
    # 가로중에서 M길이의 양 끝이 같은 리스트를 찾아야함
    # 기계적으로 코딩하지말고 내 로직을 스스로 생각하면서 문제를 풀자
    for i in range(8):
        for j in range(8-M+1):
            if matrix[i][j] == matrix[i][j+M-1]:
                test = matrix[i][j:j+M]
                ans += is_it_palindrome(test, M)
    return ans

def cero(M, matrix):
    ans = 0
    # 세로중에서 M길이의 양 끝이 같은 리스트를 찾아야함
    for j in range(8):
        for i in range(8-M+1):
            if matrix[i][j] == matrix[i+M-1][j]:
                # 세로의 배열을 뽑아내는 알고리즘은 따로 만들어줘야함
                tmp = M
                test = []
                while tmp > 0:
                    test.append(matrix[i+tmp-1][j])
                    tmp -= 1
                ans += is_it_palindrome(test, M)
    return ans


def is_it_palindrome(test,M):
    # 회문이면 1 아니면 0 return
    pos = 0
    # 길이의 절반인 M//2로 양 끝부터 회문검사
    while pos < M//2:
        if test[pos] != test[-(pos+1)]:
            return 0
        pos += 1
    return 1


for tc in range(1, 11):
    # 찾아야하는 회문의 길이
    M = int(input())

    # 8 by 8
    matrix = [list(input()) for _ in range(8)]

    # 나눠서 생각하자
    # 1. garo에서 행의 window screen의 양쪽 끝이 같은 글자인 list를 찾음
    # -> palidrome에 전달해서 회문인지 검사
    # 2. cero에서 열의 "
    # -> palidrome에 전달해서 "
    # 3. palidrome: 전달받은 리스트가 회문인지 검사

    garo_pal = garo(M, matrix)
    cero_pal = cero(M, matrix)

    print("#{} {}".format(tc, garo_pal+cero_pal))