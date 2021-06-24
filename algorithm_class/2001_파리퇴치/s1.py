import sys
sys.stdin = open("input.txt", "r")

    
for tc in range(1, int(input())+1):
    # 배열 크기 N, 파리채 크기 M
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 좀 재밌게 푸는 방법 없을까...
    # 진짜 최악의 문제인데 이건...


    value_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            cur_value = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    cur_value += matrix[x][y]
            if cur_value > value_max:
                value_max = cur_value


    print("#{} {}".format(tc, value_max))