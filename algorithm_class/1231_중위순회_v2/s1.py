"""
내가 tree안에 있는 노드인지 확인
----
왼쪽 자식 inorder 재귀
본인 저장
오른쪽 자식 inorder 재귀
----
이 순서로 로직을 작성해서 만약 내가 안에 없는 노드면 일단 함수로 내려와서
나를 저장 안하는 방법으로 로직을 구현 - by 지수님
천재이신가..?
"""
import sys
sys.stdin = open('input.txt', 'r')



def inorder(tree:list, s:int, trail:list):
    if s < len(tree):
        inorder(tree,s*2,trail)
        trail.append(s)
        inorder(tree,s*2+1,trail)
        

for tc in range(1, 11):
    V = int(input())
    tree = [0 for _ in range(V+1)]

    for i in range(V):
        data = input().split()
        data = data[:2]
        tree[int(data[0])] = data[1]

    trail = []
    inorder(tree,1,trail)
    print("#{} ".format(tc),end = '')
    for i in range(len(trail)):
        print(tree[trail[i]], end='')
    print()