"""
쇠막대를 stack으로 풀어봅시다.
"""

import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):

    # 우선 쇠막대를 받아오자
    steel_rode = input()

    # 반환할 값
    ans = 0
    # 빈 스택
    stack = []

    # 이전에 나온게 left parenthesis인지 right parenthesis인지 체크
    left_flag = False
    
    for i in range(len(steel_rode)):
        # 만약 왼쪽 괄호면
        if steel_rode[i] == '(':
            stack.append(steel_rode[i])
            left_flag = True
        # 만약 오른쪽 괄호면
        else:
            stack.pop()
            # 바로 이전이 left였다
            # laser라는 뜻
            if left_flag == True:
                ans += len(stack)
                left_flag = False
            # 이전에 right parenthesis가 나왔다.
            # 쇠막대가 끝났다는 뜻
            else:
                ans += 1
    print("#{} {}".format(tc, ans))