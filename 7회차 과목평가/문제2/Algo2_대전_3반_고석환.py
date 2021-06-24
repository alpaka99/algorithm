global cnt

def node_cnt(node:int):
    if node == 0:
        return

    global cnt
    cnt += 1

    node_cnt(tree[node][1])
    node_cnt(tree[node][2])



for tc in range(1, int(input())+1):
    V, N = map(int, input().split())

    # 이진 트리
    # p, l, r 순으로 저장
    tree = [[0 for _ in range(3)] for _ in range(V+1)]

    info = list(map(int, input().split()))

    i = 0
    while i < len(info):
        parent = info[i]
        child = info[i+1]

        # 왼쪽이 비었으면 왼쪽 먼저 넣어줄래
        if not(tree[parent][1]):
            tree[parent][1] = child
        else:
            tree[parent][2] = child

        tree[child][0] = parent
        i += 2

    global cnt
    cnt = 0

    node_cnt(N)
    # cnt-1을 해주는 이유
    # => N의 자식노드만 세야 하는데 내 함수는 처음 들어갈때 N에 대해서도 cnt+1을 해줘서
    print("#{} {}".format(tc,cnt-1))
