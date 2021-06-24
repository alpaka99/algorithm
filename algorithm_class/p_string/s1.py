import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf-8')

# 1. 지루한 방법
for _ in range(1, 11):
    tc = int(input())
    M = input()
    N = input()

    ans = 0
    for i in range(len(N)-len(M)+1):
        count = 0
        for j in range(len(M)):
            if N[i+j] == M[j]:
                count += 1
        if count == len(M):
            ans += 1

    print("#{} {}".format(tc, ans))