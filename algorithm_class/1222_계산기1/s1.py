import sys
sys.stdin = open('input.txt', 'r')

# 후위 표현으로 바꿔주는 함수
def post_fix(N, infix):
    stack = []
    ans = ''
    for i in range(N):
        try:
            # 숫자인지 보고
            int(infix[i])
            # 숫자면 ans에 더해줌
            ans += infix[i]
        # 숫자가 아니다? -> 연산자다
        except:
            if stack:
                ans += stack.pop()
                stack.append(infix[i])
            else:
                stack.append(infix[i])
    # stack이 빌때까지 후위에 연산자 씀
    while stack:
        ans += stack.pop()
    return ans

# 후위 표현된것을 계산해주는 함수
def calculation(N,postfix):
    stack = []
    for i in range(N):
        try:
            # 이번에는 숫자면 스택에 넣고
            int(postfix[i])
            stack.append(postfix[i])
        except:
            # 스택이 아닌 연산자면 stack에서 두개를 뺴서 연산 후 결과값을 다시 스택에 넣음
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num1)+int(num2))
    # 마지막에는 스택에 하나의 최종 결과값만 남으므로 이것을 반환해줌
    return stack[-1]

for tc in range(1, 11):
    # 문자열 계산식의 길이
    N = int(input())
    infix = input()
    stack = []

    postfix = post_fix(N, infix)
    print("#{} {}".format(tc, calculation(N, postfix)))