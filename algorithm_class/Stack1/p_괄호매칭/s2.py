"""
한정된 크기의 스택으로 괄호 매칭해보기
"""
import sys
sys.stdin = open('input.txt', 'r')

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
global top, stack_size
global stack
# stack끝에 item을 넣어줌
def push(item):
    # top을 1 증가시키고 해당 칸에 item을
    global top
    top += 1
    stack[top] = item


def pop():
    # is_empty를 통해 스택이 비어있지 않은지 확인함
    if not(is_empty()):
        global top
        # top에 저장되어있는 아이템을 tmp에 저장시키고
        # 스택의 top을 비운 뒤
        # top을 한칸 낮춤
        tmp = stack[top]
        stack[top] = ''
        top -= 1
        return tmp
    # 비어있으면 그냥 return
    else:
        return

def is_empty():
    # 만약 스택에 뭐라도 있으면 0을 return -> not(isEmpty()) 이렇게 사용하기 위해서
    if top > -1:
        return 0
    # 만약 스택이 비어있으면 stack is Empty를 출력하고 1을 리턴
    else:
        print("Stack is Empty")
        return 1

# stack을 초기화해주는 함수
def init_stack(data):
    # global 변수들을 불러와서 하나씩 초기화해줌
    global top,stack_size,stack
    top = -1
    stack_size = len(data)//2
    stack = ['']*stack_size

def check_matching(data):
    # 우선 스택 초기화
    init_stack(data)
    # data를 돌면서 괄호 확인
    for i in range(len(data)):
        if data[i] == '(':
            push('(')
        elif data[i] == ')':
            # 오른쪽 괄호가 왼쪽괄호보다 먼저 나오면
            if is_empty():
                return "Parenthesis order wrong"
            else:
                pop()
    # 다 돌고 나서 만약 스택에 남은 왼쪽 괄호가 있으면
    if not(is_empty()):
        return "Parenthesis matching failed"
    # 다 돌고 나서 스택도 다 비어있으면
    else:
        return "All Clear"

# 첫 번째 괄호쌍
data = input()

# 두 번째 괄호쌍
data2 = input()



print(check_matching(data))


print(check_matching(data2))