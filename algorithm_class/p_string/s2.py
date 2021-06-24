import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf-8')

# 2. 보이어-무어로 한번 풀어보자 나중에
for _ in range(1, 11):
    tc = int(input())
    M = input()
    N = input()

    ans = 0
    pos = 0

    print("#{} {}".format(tc, ans))