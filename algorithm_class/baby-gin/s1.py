import sys
sys.stdin = open("input.txt", "r")


T = int(input())

def baby_gin(t):
    # 우선 카운팅 해주는 10칸짜리 array 만듬
    count = [0] * 10
    # 카드들을 받고
    numbers = input()
    # 카드에 해당하는 칸을 각 카드마다 +1 씩 증가시켜줌
    for num in numbers:
        count[int(num)] += 1

    # triplet을 지워줌
    for i in range(10):
        count[i] %= 3

    # run 제거
    # 3칸 연속 차있는거는 다 1씩 뺴줌
    for i in range(0, 8):
        while count[i] > 0:
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1

    # run triplet 다 지웠는데 아직 남은 카드가 있다?
    # => babygin이 아님
    for card in count:
        if card:
            print("#{} {}".format(t + 1, 0))
            return

    print("#{} {}".format(t + 1, 1))
    return

for t in range(T):
    baby_gin(t)



