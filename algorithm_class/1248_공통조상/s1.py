"""
1부터 찾아가는게 아니라 각 노드에 부모노드의 번호가 적혀있으니까
그냥 그거 따라서 거슬러 올라가면 되잖아 이눔아...
"""
import sys
sys.stdin = open('input.txt', 'r')

def find_route(tree:list, s:int, g:int, trail:list):
    # 만약 현재 노드의 정보가 우리가 찾던 노드면 return
    if s == g:
        return 1

    # 최단 거리를 찾아야함
    if tree[s][1]:
        trail.append(tree[s][1])
        ans = find_route(tree, tree[s][1], g, trail)
        # 만약 맞는 길이면 pass하고
        if ans:
            return 1
        # 틀린길이면 방금의 길에 대한 정보를 지워줌
        else:
            trail.pop()

    if tree[s][2]:
        trail.append(tree[s][2])
        ans = find_route(tree, tree[s][2], g, trail)
        # 만약 맞는 길이면 pass하고
        if ans:
            return 1
        # 틀린길이면 방금의 길에 대한 정보를 지워줌
        else:
            trail.pop()
    # 두 자식 다 틀린길이면 틀린 길이니까 0을 리턴
    return 0

def count(tree:list, s:int):
    if s == 0:
        return 1
    tmp = 0
    tmp += count(tree, tree[s][1])
    tmp += count(tree, tree[s][2])
    return tmp

for tc in range(1, int(input())+1):
    # 정점 수 V, 간선 수 E, 공통 조상을 찾는 a, b
    V, E, a, b = map(int, input().split())

    # 부모, 왼자, 오자 순
    tree = [[0 for _ in range(3)] for _ in range(V+1)]

    # edge 정보
    edge = list(map(int, input().split()))
    # 가장 정점의 노드 번호는 항상 1
    tree[0][1] = 1
    i = 0
    while i < len(edge):
        parent = edge[i]
        child = edge[i+1]
        
        # 부모 자식 관계 설정
        if not(tree[parent][1]):
            tree[parent][1] = child
        else:
            tree[parent][2] = child
        tree[child][0] = parent
        i += 2

    # for i in range(len(tree)):
    #     print(i, tree[i])
    # 공통 조상을 어떻게 찾지?
    # -> 해당 노드를 찾아 내려가는 경로를 다 저장하면서 해보자
    trail_1 = []
    tmp = find_route(tree, 0, a, trail_1)

    trail_2 = []
    tmp = find_route(tree, 0, b, trail_2)

    if len(trail_1) > len(trail_2):
        short = trail_1
        long = trail_2
    else:
        short = trail_2
        long = trail_1
    
    # 두 list에서 공통 부모 찾음
    for i in range(len(short)):
        if short[i] != long[i]:
            break

    lca = short[i-1]
    num = count(tree, lca)-1
    print("#{} {} {}".format(tc, lca, num))