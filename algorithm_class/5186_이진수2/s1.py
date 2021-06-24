import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N = float(input())
    answer = ''
    tmp = 0
    flag = True
    # 소수점 아래 12자리
    for i in range(1, 13):
        if tmp + 2**(-i) <= N:
            tmp += 2**(-i)
            answer += '1'
        else:
            answer += '0'

        if tmp == N:
            print("#{} {}".format(tc, answer))
            flag = False
            break
    if flag:
        print("#{} {}".format(tc,'overflow'))