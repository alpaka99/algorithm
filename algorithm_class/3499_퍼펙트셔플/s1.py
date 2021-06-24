import sys
sys.stdin = open('input.txt', 'r',encoding='utf8')

for tc in range(1, int(input())+1):
    N = int(input())
    cards = list(input().split())
    
    # 1인경우 예외처리
    if len(cards) == 1:
        print("#{} {}".format(tc, *cards))
        continue

    ans = ''


    # 이렇게 하면 <5-1 = 4 // 2 = 2>, <6 -1 = 5 // 2> 둘 다 인덱싱으로 가능
    N -= 1
    half = N//2

    # 시작부터 반까지
    cards_front = cards[:half + 1]
    # 반부터 끝까지
    cards_back = cards[half+1:]

    while len(cards_back) != 0:
        ans = ans + cards_front[0] + ' '
        ans = ans + cards_back[0] + ' '

        cards_front.pop(0)
        cards_back.pop(0)
    if len(cards_front) != 0:
        ans = ans + cards_front[0]
    print("#{} {}".format(tc, ans))
