"""
재현님의 "this is backtracking bbb"이라는 문장을 보고 백트랙킹으로 풀어보고싶어짐
"""

import sys
sys.stdin = open('input.txt', 'r')

def back_tracking(new_info: list, L: int):
    # new_info를 스택으로 생각하고 계속 pop해보자
    total_calories = 0
    total_point = 0

    while new_info:
        cur_ingredient = new_info.pop(-1)
        if total_calories + cur_ingredient[1] <= L:
            total_point += cur_ingredient[0]
            total_calories += cur_ingredient[1]

    return total_point

for tc in range(1, int(input())+1):
    N, L = map(int, input().split())
    ingredient_info = [list(map(int, input().split())) for _ in range(N)]

    # 맛을 기준으로 sorting
    new_info = sorted(ingredient_info, key = lambda x: x[0])
    print(new_info)
    print(back_tracking(new_info, L))