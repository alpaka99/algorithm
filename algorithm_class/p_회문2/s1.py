import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

# 100 by 100 matrix
# 가장 긴것을 우선으로 찾는 방식으로 하자
# 그래야 연산을 많이 줄일듯
############### 가로 부분 ###############
def palindrome_garo(matrix):
    # 한변의 길이
    N = len(matrix)

    # 제일 큰값부터 시작해야 큰 회문부터 찾음
    M = 100
    while M > 0:
        # list slicing으로 해보자
        # 각 row들에 대하여
        for i in range(N-M+1):
            for j in range(N-M+1):
                    # 끝 부분이 같으면 잘라내서 실제 회문 테스트
                if matrix[i][j] == matrix[i][j+M-1]:
                # 리스트 슬라이싱은 인덱싱과는 다르게 하나앞에서 끊기는거 꼭 기억하자 이눔아
                    test = matrix[i][j:j+M]
                    ans = is_it_palindrome(test, M)
                    if ans:
                        return ans
        M -= 1

def palindrome_cero(matrix):
    ############### 세로 부분 ###############
    # 한변의 길이
    N = len(matrix)
    # 제일 큰값부터 시작해야 큰 회문부터 찾음
    M = 100
    while M > 0:
        for j in range(N-M+1):
            for i in range(N-M+1):
                if matrix[i][j] == matrix[i+M-1][j]:
                    test = []
                    tmp = M
                    # 리스트 슬라이싱의 위험성... 2차원 배열이어도 그 다음 배열까지 가서 가져옴...
                    while tmp > 0:
                        test.append(matrix[i+tmp-1][j])
                        tmp -= 1
                    ans = is_it_palindrome(test, M)
                    if ans:
                        return ans
        M -= 1

def is_it_palindrome(test,M):
    pos = 0
    # print(M,len(test))
    while pos < M // 2:
    # 지금 보고있는 두 글자가 다르면 탈출
        if test[pos] != test[-pos-1]:
            return None
    # 아니면 다음 글자 검색
        pos += 1
    # print(test)
    return len(test)



for _ in range(1, 11):
    tc = int(input())

    matrix = [list(input()) for _ in range(100)]

    garo = palindrome_garo(matrix)
    cero = palindrome_cero(matrix)

    if garo > cero:
        print("#{}".format(tc),garo)
    else:
        print("#{}".format(tc), cero)