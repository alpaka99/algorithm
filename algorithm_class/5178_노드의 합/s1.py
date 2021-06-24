import sys
sys.stdin = open('input.txt', 'r')

# tree의 가장 끝 leaf부터 부모 node에 자신의 값을 더함
def leaf_sum(tree:list):
    idx = len(tree)-1

    while idx > 0:
        tree[idx//2] += tree[idx]
        idx -= 1

    return



for tc in range(1, int(input())+1):
    # 노드의 갯수 N, 리프 노드의 갯수 M, 출력할 노드 번호 L
    N, M, L = map(int,input().split())

    # 위의 idx//2 계산 편하게 하기 위해서 N+2
    tree = [0 for _ in range(N+1)]

    # leaf node들 입력
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    leaf_sum(tree)

    print("#{} {}".format(tc, tree[L]))