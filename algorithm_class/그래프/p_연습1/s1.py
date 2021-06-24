"""
연습 문제1. Stack 구현
 - 사이즈가 5인 고정 배열 Stack을 구현하시오.
"""

SIZE = 5
stack = [0]*5
top = -1

def is_full():
    if top == SIZE:
        print('stack is full')
        return True
    else:
        return False
def is_empty():
    if top == -1:
        print('stack is empty')
        return True
    else:
        return False

def push(n:int):
    if is_full():
        return
    global top
    top += 1
    stack[top] = n



def pop():
    global top
    if is_empty():
        return
    else:
        top -= 1
        return stack[top+1]


push(1)
push(2)
push(3)
push(4)
push(5)

item = pop() # 5
print('Pop item {}'.format(item))
item = pop() # 4
print('Pop item {}'.format(item))
item = pop() # 3
print('Pop item {}'.format(item))
item = pop() # 2
print('Pop item {}'.format(item))
item = pop() # 1
print('Pop item {}'.format(item))

item = pop() # None
print('Pop item {}'.format(item))