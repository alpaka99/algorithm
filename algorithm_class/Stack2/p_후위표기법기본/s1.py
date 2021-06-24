"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여
수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

예시 입력)
2+3*4/5

예시 출력)
2345/*+
"""

import sys
sys.stdin = open('input.txt')

line = input()

stack = []
ans = ''

for i in range(len(line)):
    try:
        print(int(line[i]), end='')
    except:
        stack.append(line[i])
for i in range(len(stack)):
    print(stack.pop(),end='')