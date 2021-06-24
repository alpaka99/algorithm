"""
미래를 본다는 문제의 글에서 힌트를 얻어서 풀었습니다.
"""

import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    # 원두의 날짜별 가격 list
    price = list(map(int, input().split()))
    # 원두로 얻은 이득
    profit = 0


    # stack에 쌓았다가 하나씩 뽑으면서 연산할까
    cur_price = price.pop()
    stack = []

    # price list가 비었는지 아닌지를 판별하는 flag
    if len(price) != 0:
        price_empty_flag = False
    else:
        price_empty_flag = True

    # price가 빌때까지(1일차를 살펴볼때까지) 진행
    while price:
        # 미래의 가격보다 낮은것을 다 넣고
        while cur_price > price[-1]:
            stack.append(price.pop())
            if len(price) == 0:
                price_empty_flag = True
                break

        # 이제 stack에서 뽑아내면서 연산
        while stack:
            profit += (cur_price-stack.pop())

        # 다 뽑아냈으면 price의 가장 끝을 다시 cur_price로 지정
        if price_empty_flag:
            break
        else:
            cur_price = price.pop()

    print("#{} {}".format(tc, profit))