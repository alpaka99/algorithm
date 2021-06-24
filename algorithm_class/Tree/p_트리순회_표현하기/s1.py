import sys
sys.stdin = open('input.txt', 'r')

# def VLR(tree:list, s:int)->list:
#     trail = []
#     stack = [s]
#     while stack:
#         cur_node = stack.pop()
#         trail.append(cur_node)
#         # 오른쪽 부터 넣어줘야 LR순서대로 가능
#         if tree[cur_node][2]:
#             stack.append(tree[cur_node][2])
#         if tree[cur_node][1]:
#             stack.append(tree[cur_node][1])
#     return trail

# 재귀로 다시 만듬...
def VLR(tree: list, s: int, trail: list):
    # 탈출 조건
    if s == 0:
        return

    # 자기자신 저장
    trail.append(s)
    # 왼쪽
    VLR(tree, tree[s][1], trail)
    # 오른쪽
    VLR(tree, tree[s][2], trail)
    return

# 재귀로 짜는 방법밖에 생각이 안나네
def LVR(tree:list, s:int, trail:list):
    # 종료 조건
    if s == 0:
        return

    # 왼쪽
    LVR(tree, tree[s][1], trail)
    # 자기자신 저장
    trail.append(s)
    # 오른쪽
    LVR(tree, tree[s][2], trail)
    return


# 이것도 재귀로...
def LRV(tree:list, s:int, trail:list):
    # 탈출 조건
    if s == 0:
        return
    
    # 왼쪽
    LRV(tree, tree[s][1], trail)
    # 오른쪽
    LRV(tree, tree[s][2], trail)
    # 자기자신 저장
    trail.append(s)
    return

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
while i < len(info):
    parent = info[i]
    child = info[i+1]
    # 왼쪽이 차 있으면
    if tree[parent][1]:
        # 오른쪽에 자식을 넣어줌
        tree[parent][2] = child
    else:
        tree[parent][1] = child

    # 자식을 부모랑 연결해줌
    tree[child][0] = parent
    i += 2
#
# for i in range(len(tree)):
#     print(i, tree[i])

# 전위 탐진
VLR_trail = []
VLR(tree, 1, VLR_trail)

# 중위 탐진
LVR_trail = []
LVR(tree, 1, LVR_trail)

# 후위 탐진
LRV_trail = []
LRV(tree, 1, LRV_trail)


print('전위 순회', *VLR_trail)
print('중위 순회', *LVR_trail)
print('후위 순회', *LRV_trail)
