"""
input과 stack을 계속해서 비교하는 문제
"""
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    # 어짜피 비교할떄는 숫자, 문자 상관없는 로직이라 그냥 둘 다 str로 받음
    N ,pwd= map(str, input().split())


    stack = []
    # 우선 처음 하나를 넣어줌

    # 우리가 보는 비밀번호의 부분을 가리키는 포인터 i
    i = 0
    
    # i가 비밀번호의 범위 내에 있는동안
    while i < int(N):
        # 축약 검사
        if stack:
            # top과 현재 포인터가 가리키는것이 같다? -> 축약가능
            if stack[-1] == pwd[i]:
                # stack에 있는 축약된 비밀번호 pop
                stack.pop()
            else:
                # 축약 불가능하면 append
                stack.append(pwd[i])
        else:
            # stack에 아무것도 없으면 append
            stack.append(pwd[i])
        # 포인터가 다음 숫자를 가리킴
        i += 1

    # stack에는 축약된 번호들만 남음
    print("#{} {}".format(tc, ''.join(stack)))
