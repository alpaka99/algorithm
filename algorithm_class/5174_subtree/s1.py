import sys
sys.stdin = open('input.txt', 'r')
global num

def count(tree:list, s:int):
    global num
    num += 1
    if tree[s][1]:
        count(tree, tree[s][1])
    if tree[s][2]:
        count(tree, tree[s][2])

    return

for tc in range(1, int(input())+1):
    # 간선의 갯수 E, 서브트리의 루트 N
    E, N = map(int, input().split())
    
    # P, L, R 순
    tree = [[0 for _ in range(3)] for _ in range(E+2)]
    edge_data = list(map(int, input().split()))

    i = 0
    while i < len(edge_data):
        parent = edge_data[i]
        child = edge_data[i+1]

        if not(tree[parent][1]):
            tree[parent][1] = child

        else:
            tree[parent][2] = child
        tree[child][0] = parent
        i += 2
    # print(tree)
    num = 0
    count(tree,N)
    print("#{} {}".format(tc,num))