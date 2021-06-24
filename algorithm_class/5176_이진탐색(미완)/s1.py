"""
이진탐색과 그 후에 중위순회로 숫자를 넣어주는 방식
"""

import sys
sys.stdin = open('input.txt', 'r')


def make_binary(tree:list, data:list, count:int)->int:
    if len(data) == 1:
        cur_node = data.pop()
        tree[cur_node][3] = count
        return cur_node

    mid = len(data)//2

    middle = data[mid]
    left = data[:mid]
    right = data[mid+1:]

    # 왼쪽 자식
    left_child = make_binary(tree,left, count*2)
    tree[middle][1] = left_child
    tree[left_child][0] = middle

    # 오른쪽 자식
    right_child = make_binary(tree, right, count*2+1)
    tree[middle][2] = right_child
    tree[right_child][0] = middle

    tree[middle][3] = count
    return middle

for tc in range(1, int(input())+1):
    # 현재 노드의 갯수
    N = int(input())

    # 왼쪽 서브트리 루트 < 현재 노드 < 오른쪽 서브트리 루트

    i = 1
    while i <= N:
        i *= 2

    data = []
    for j in range(1, i):
        data.append(j)

    # 완전 이진 트리를 만들어야함
    # 노드의 부모, 왼자, 오른자
    tree = [[0 for _ in range(4)] for _ in range(i)]

    root = make_binary(tree,data,1)
    root = N//2+1
    n = N//2
    ans = 0
    for i in range(len(tree)):
        if tree[i][3] == n:
            ans = i
            break
    # for i in range(len(tree)):
    #     print(i, tree[i])
    print("#{} {} {}".format(tc, root, ans))
