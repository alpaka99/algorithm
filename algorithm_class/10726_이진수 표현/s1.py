import sys
sys.stdin = open('input.txt', 'r')

def tf(N, M):
    for i in range(N):
        if M & (1<<i):
            continue
        else:
            return 0
    return 1
for tc in range(1, int(input())+1):
    # M의 이진수 표현의 마지막 N비트가 모두 1로 켜져있는지 아닌지를 판별
    N, M = map(int,input().split())

    ans = tf(N, M)

    if ans:
        print("#{} {}".format(tc, 'ON'))
    else:
        print("#{} {}".format(tc, 'OFF'))