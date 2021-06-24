import sys
sys.stdin = open('input.txt', 'r')

def LVR(tree:list, s:int, trail:list):
    if s == 0:
        return


    LVR(tree, tree[s][2], trail)
    trail.append(tree[s][1])
    LVR(tree, tree[s][3], trail)
    return

for tc in range(1, 11):
    # 정점의 총 수
    N = int(input())
    
    # tree는 부모, 해당노드의 글자, 왼쪽자식, 오른쪽자식 순서대로 저장
    tree = [[0 for _ in range(4)] for _ in range(N+1)]

    for _ in range(N):
        data = list(input().split())

        cur_node = int(data[0])
        tree[cur_node][1] = data[1]
        
        # 슬라이싱 했을때 뒤에 뭐가 있다
        # -> 자식노드가 있다
        data = data[2:]
        # 자식노드 연결
        i = 2
        while data:
            child = int(data.pop(0))
            tree[cur_node][i] = child
            tree[child][0] = cur_node
            i += 1

    # tree 저장 다 했으니까 이제 중위표현돌리자
    LVR_trail = []
    LVR(tree, 1, LVR_trail)
    answer = ''.join(LVR_trail)
    print("#{} {}".format(tc, answer))