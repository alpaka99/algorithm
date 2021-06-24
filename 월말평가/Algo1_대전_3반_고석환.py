
def baby_gin():
    triplet_flag = False
    run_flag = False

    # triplet 검사
    for i in range(10):
        if cards[i] > 0:
            cards[i] %= 3
            triplet_flag = True

    # run 검사
    for i in range(7):
        if cards[i] >= 1:
            while cards[i]:
                cards[i] -= 1
                cards[i+1] -= 1
                cards[i+2] -= 1
            run_flag = True


    # 전체 검사
    if triplet_flag or run_flag:
        for i in range(10):
            if cards[i] != 0:
                return 0
        return 1
    else:
        return 0

for tc in range(1, int(input())+1):
    infos = list(input())

    cards = [0 for _ in range(10)]

    for info in infos:
        cards[int(info)] += 1

    ans = baby_gin()

    print("#{} {}".format(tc,ans))
