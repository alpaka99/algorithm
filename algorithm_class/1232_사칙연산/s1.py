"""
# 각 연산 함수 딕셔너리
    op_dict = {'+': lambda x, y: x + y,
               '-': lambda x, y: x - y,
               '/': lambda x, y: x / y,
               '*': lambda x, y: x * y,
               }
               - by 짱짱현승님
"""
import sys
sys.stdin = open('input.txt', 'r')

def add(a,b):
    return a + b

def sub(a:int,b:int):
    return a - b

def mul(a:int,b:int):
    return a * b

def div(a:int,b:int):
    return a / b

# 재귀적으로 연산해주는 함수
def calc(s:int):
    op_dict = {'+':add, '-':sub, '*':mul, '/':div}
    node = tree[s]
    if node[3].isnumeric():
            return int(node[3])
    else:
        # node의 내용물이 연산자면
        left_child = node[1]
        right_child = node[2]
        return op_dict[node[3]](calc(left_child), calc(right_child))


for tc in range(1, 11):
    # 정점의 총수 N
    N = int(input())

    # 연산 트리
    # 부모, 왼자, 오자, 내용물
    tree = [[0,0,0,''] for _ in range(N+1)]

    # 트리 내용물 넣기
    for _ in range(N):
        data = input().split()
    
        parent = int(data[0])

        if len(data) > 2:
            left = int(data[2])
            right = int(data[3])

            # 자식관계 설정
            # 왼쪽 자식
            tree[parent][1] = left
            tree[left][0] = parent
            # 오른쪽 자식
            tree[parent][2] = right
            tree[right][0] = parent

        # 연산기호 넣기
        tree[parent][3] = data[1]



    ans = calc(1)

    print("#{} {}".format(tc, int(ans)))