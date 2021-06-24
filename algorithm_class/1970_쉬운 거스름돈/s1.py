import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt_list = [0 for _ in range(8)]

    for i in range(8):
        # print(N, money[i])
        if N // money[i] > 0:
            cnt_list[i] = N//money[i]
            N %= money[i]


    print("#{}".format(tc))
    print(*cnt_list)