"""
사칙연산으로 확장
-,/일때 오류생기는것 수정 -> stack의 아래에 있는 요소가 먼저 들어온것임을 기억!
"""
import sys
sys.stdin = open('input.txt', 'r')

# 문제에서는 +,* 뿐이지만 나는 4칙 연산이 되는 계산기를 만들고 싶다.
def post_fix(N, infix):
    op_stack = []
    op_dict = {'+': 1, '-':1, '*': 2, '/':2}

    ans = ''

    # 다른분들이 쓰신 isDecimal을 써볼까?
    for i in range(N):
        # 만약 숫자면
        if infix[i].isdecimal():
            ans += infix[i]
        else:
            # 스택이 비어있지 않으면
            if op_stack:
                # 비어있지 않고(단축평가), 최상단이 지금의 연산자보다 우선순위가 높거나 같은동안
                while op_stack and op_dict[infix[i]] <= op_dict[op_stack[-1]]:
                    ans += op_stack.pop()
                # stack이 비었거나, 자신보다 우선순위 낮은게 나오면 push
                op_stack.append(infix[i])
            # 스택이 비어있으면 그냥 push
            else:
                op_stack.append(infix[i])
    # 다 돌고나서 연산자가 남았으면
    while op_stack:
        ans += op_stack.pop()
    return ans


def calculation(N, postfix):
    # 후위표기 계산에는 숫자를 넣어야함
    num_stack = []

    # 잠만... 이거 표기를 어캐해야하냐;; 그냥 if elif?
    for i in range(N):
        # 숫자면
        if postfix[i].isdecimal():
            num_stack.append(int(postfix[i]))
        else:
            # 나눗셈이랑 뺄셈 들어오니까 이거 순서 바뀌어서 오류남
            # 항상 stack 아래에 있는 요소가 먼저 들어온것이라는것 기억하자!
            # 나중에 들어옴
            num2 = num_stack.pop()
            # 먼저 들어옴
            num1 = num_stack.pop()

            # 아 이거 좀 지저분한데 어떻게 방법이 없나, 다른분들 코드 참고해야겠다
            if postfix[i] == '+':
                num_stack.append(num1+num2)
            elif postfix[i] == '-':
                num_stack.append(num1-num2)
            elif postfix[i] == '*':
                num_stack.append(num1*num2)
            elif postfix[i] == '/':
                num_stack.append(num1/num2)

    return num_stack[-1]

for tc in range(1, 13):
    N = int(input())
    infix = input()

    print("#{} {}".format(tc, calculation(N,post_fix(N,infix))))
