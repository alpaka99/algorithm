import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(T):
    n = int(input())

    #counting 정렬처럼 카드를 세는 list를 만듬
    cards = [0]*10

    # 빈칸없는 숫자들을 input으로 받고
    no_blank = input()

    # 각 string인 숫자들을 int로 바꾼 후 해당칸 1 증가
    for i in range(n):
        cards[int(no_blank[i])] += 1

    # 가장 많은 숫자와 해당 숫자의 idx를 저장할 변수들
    max_idx = 0
    max_value = cards[max_idx]

    # for문을 돌면서 가장 많은 카드와 해당 카드의 번호를 반환
    for idx in range(10):
        if cards[idx] >= max_value:
            max_value = cards[idx]
            max_idx = idx

    print("#{} {} {}".format(tc+1, max_idx, max_value))
