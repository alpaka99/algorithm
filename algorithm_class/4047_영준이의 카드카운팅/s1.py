import sys
sys.stdin = open('input.txt', 'r')

def card_counting(tc, cards):
    # S01 = spade 1, D02 = diamond 2...
    # card: 1~13
    # 카드 덱
    deck = {}
    symbols = ['S', 'D', 'H', 'C']

    # key랑 카운팅 리스트 넣어줌
    for i in range(len(symbols)):
        deck[symbols[i]] = [0 for _ in range(14)]

    # 3개씩 잘라서 넣어주자
    for i in range(0, len(cards), 3):
        # 글자 3개씩 자르기
        card = cards[i:i + 3]
        # 카드의 종류
        card_key = card[0]
        # 카드의 숫자
        card_num = int(card[1]) * 10 + int(card[2])
        # 만약 같은게 이미 있으면 return
        if deck[card_key][card_num] == 1:
            print("#{} ERROR".format(tc))
            return
        # 해당하는 카드의 숫자 1증가
        deck[card_key][card_num] += 1

    missing_cards = [0 for _ in range(len(symbols))]
    # 4개의 symbol을 돌면서
    for i in range(4):
        for j in range(len(deck[symbols[i]])):
            if deck[symbols[i]][j] == 0:
                missing_cards[i] += 1
        # 맨앞에 0 값은 count 안함
        missing_cards[i] -= 1
    print("#{}".format(tc),*missing_cards)
    return
for tc in range(1, int(input())+1):
    # A = 1, J, Q, K = 11, 12, 13
    cards = input()
    card_counting(tc, cards)