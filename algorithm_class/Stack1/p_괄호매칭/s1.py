import sys
sys.stdin = open('input.txt')

"""
괄호 매칭
1. 괄호의 종류 - [], {}, ()
2. 괄호 매칭의 조건 
- 왼쪽 괄호의 개수와 오른쪽 괄호의 '개수'가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 '먼저' 나와야 한다.
 - 괄호 사이에는 포함 관계만 존재한다.
3. 잘못된 사용의 예시
(a(b) -> 괄호 개수
a(b)c) -> 괄호 개수
a{b(c[d]e}) -> 괄호가 올바르게 매칭되지 않음
"""

# 소괄호만

# stack끝에 item을 넣어줌
def push(item):
    stack.append(item)


def pop():
    # is_empty를 통해 스택이 비어있지 않은지 확인함
    if not(is_empty()):
        stack.pop()
    # 비어있으면 그냥 return
    else:
        return

def is_empty():
    # 만약 스택에 뭐라도 있으면 0을 return -> not(isEmpty()) 이렇게 사용하기 위해서
    if stack:
        return 0
    # 만약 스택이 비어있으면 stack is Empty를 출력하고 1을 리턴
    else:
        print("Stack is Empty")
        return 1

def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            push('(')
        elif data[i] == ')':
            if is_empty():
                return "Parenthesis order wrong"

            else:
                pop()
    if not(is_empty()):
        return "Parenthesis matching failed"
    else:
        return "All Clear"

# 첫 번째 괄호쌍
data = input()

# 두 번째 괄호쌍
data2 = input()

stack = []
print(check_matching(data))
print(check_matching(data2))