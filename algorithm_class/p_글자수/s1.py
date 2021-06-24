import sys
sys.stdin = open('input.txt', 'r', encoding='utf8')

for tc in range(1, int(input())+1):
    N = input()
    M = input()

    alphabet_N = [False]*26
    alphabet_M = [0]*26


    for i in range(len(N)):
        alphabet_N[ord(N[i])-65] = True

    for i in range(len(M)):
        alphabet_M[ord(M[i])-65] += 1

    max_value = 0

    for i in range(len(alphabet_N)):
        if alphabet_N[i] == True:
            if max_value < alphabet_M[i]:
                max_value = alphabet_M[i]

    print("#{} {}".format(tc, max_value))