import sys
sys.stdin = open('input.txt', 'r', encoding = 'utf8')

for tc in range(1, int(input())+1):
    ans = ''
    # 각 테스트 케이스는 5줄
    matrix = []
    for _ in range(5):
        matrix.append(input())


    # 각 줄마다의 col의 위치를 저장하는
    count = [len(i)-1 for i in matrix]

    max_len = 0
    for i in range(len(count)):
        if count[i] > max_len:
            max_len = count[i]

    for j in range(max_len, -1, -1):
        for i in range(len(count)-1,-1,-1):
            if count[i] == j:
                ans = matrix[i][j] + ans
                count[i] -= 1

    print("#{} {}".format(tc, ans))