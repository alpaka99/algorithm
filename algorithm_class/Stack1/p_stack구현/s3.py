"""
stack을 클래스로 구현해보자
"""

class stack:
    def __init__(self):
        # 비어있는 리스트를 인스턴스 변수로 생성
        self.s = []

    def push(self, item):
        # __init__매직메서드는 객체가 생성될때 자동으로 생성됨으로
        # 아무생각없이 stack에 아이템을 넣어줘도 됨
        self.s.append(item)
    
    def is_empty(self):
        # 만약 스택이 비어있지 않으면 0
        if len(self.s):
            return 0
        # 비어있으면 1을 리턴(추후에 not(is_empty())로 사용하고 싶어서
        return 1
        
    def pop(self):
        # 우선 스택이 비어있는지 아닌지 검사
        # 비어있지 않으면
        if not(self.is_empty()):
            return self.s.pop()
        # 비어있으면 None을 리턴
        return


    def peek(self):
        # 스택이 비어있지 않으면
        if not(self.is_empty()):
            # 가장 끝 부분의 값을 리턴해서 보여줌
            return self.s[-1]
        return

    def current_status(self):
        print(*self.s)

new_stack = stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.current_status()

print('------')

# 가장 뒤(위)부터 pop
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
new_stack.pop()
print(new_stack.peek())
new_stack.pop()
new_stack.current_status()
