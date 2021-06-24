import sys
sys.stdin = open('input.txt', 'r')

# 노드 객체
# 우선은 default로 다 None이 들어갈 수 있고
class node():
    def __init__(self,p=None, l=None, r=None, val=None):
        self.p = p
        self.l = l
        self.r = r
        self.val = val


# 노드의 갯수
N = int(input())
print(N)

# 노드들에 따른 리스트형 트리 생성
# 인덱스에 접근하기 위해서 가장 위에 더미 루트를 만들어줌
# 근데 0 이 parent. 1이 left, 2가 right
tree = [[0 for _ in range(3)] for _ in range(N+1)]

# 간선 정보
info = list(map(int, input().split()))

i = 0
start_node = node()
while i < len(info):
    # parent = info[i]
    # child = info[i+1]
    # # 왼쪽이 차 있으면
    # if tree[parent][1]:
    #     # 오른쪽에 자식을 넣어줌
    #     tree[parent][2] = child
    # else:
    #     tree[parent][1] = child
    #
    # # 자식을 부모랑 연결해줌
    # tree[child][0] = parent

    i += 2


