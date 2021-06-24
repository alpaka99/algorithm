import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 1번부터 N번까지 N개의 상자
    # Q회 동안 일정 범위의 연속한 상자를 동일한숫자로 변경
    N, Q = map(int, input().split())

    boxes = [0 for i in range(N)]
    
    # Q번 반복
    for i in range(1, Q+1):
        # L부터 R까지의 수를 i로 바꿈
        L, R = map(int, input().split())
        for j in range(L-1, R):
            boxes[j] = i

    print("#{}".format(tc), *boxes)