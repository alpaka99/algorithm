"""
괄호는 stack 안과 밖에서 우선순위가 다르다는 규칙을 찾기가 어려웠습니다.
dict의 value로 함수를 지정해주는것은 역시 좋았습니다.
"""
import sys
sys.stdin = open('input.txt', 'r')


def hoo_whee(string):
    ans = ''
    stack = []

    # 괄호가 stack 밖에 있을떄랑 안에 있을때랑 우선순위가 다름 ㅠㅠ...
    op_priority_out = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': 0}  # 밖에서의 우선순위
    op_priority_in = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 3}  # 안에 들어가서의 우선순위

    for i in range(len(string)):
        if string[i].isdigit():
            ans += string[i]
        else:
            if string[i] == ')':
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
                continue
            else:
                while stack:
                    if op_priority_in[stack[-1]] >= op_priority_out[string[i]]:
                        ans += stack.pop()
                    else:
                        break
            stack.append(string[i])

    while stack:
        ans += stack.pop()
    return ans


def calculate(string):
    stack = []

    op_dict = {'+': add, '-': sub, '*': mul, '/': div}
    for i in range(len(string)):
        if string[i].isdigit():
            stack.append(int(string[i]))
        else:
            num2 = stack.pop()
            num1 = stack.pop()

            stack.append(op_dict[string[i]](num1, num2))

    return stack[0]


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


for tc in range(1, 11):
    N = int(input())

    string = input()

    new_string = hoo_whee(string)
    ans = calculate(new_string)
    print("#{} {}".format(tc, ans))