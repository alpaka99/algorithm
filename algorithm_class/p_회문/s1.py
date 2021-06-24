import sys
from pandas import DataFrame as df
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

def palindrome(matrix, N, M):
    for i in range(N):
        for j in range(N-M+1):
            # 만약 M만큼 떨어진곳에서 같은 글자 발견
            if matrix[i][j] == matrix[i][j+M-1]:
                # 이 부분을 떼어내서
                test = matrix[i][j:j+M]
                # 회문 검사 시작
                pos = 0
                # 회문인지 아닌지 확인을 이걸로 함
                p_flag = True
                # 양 끝단부터 좁혀오며 검사 시작
                while pos < M//2 :
                    if test[pos] != test[-pos-1]:
                        #print(test[pos], test[-pos-1])
                        p_flag = False
                        break
                    else:
                        pos += 1
                # while 빠져나올때까지 True로 살아남음
                if p_flag == True:
                    return test

for tc in range(1,int(input())+1):
    # N by N 에서 길이가 M인 회문
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    ans1 = palindrome(matrix, N, M)

    if ans1:
        print("#{}".format(tc), ''.join(ans1))
        continue

    # 행렬 전치
    for i in range(N):
        for j in range(N):
            if i< j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    ans2 = palindrome(matrix,N,M)
    print("#{}".format(tc), ''.join(ans2))
