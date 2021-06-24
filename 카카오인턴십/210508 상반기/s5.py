def solution(k, num, links):
    answer = 0
    
    # 트리 만들기
    # l_child, r_child, parent, data
    tree = [[-1,-1,-1,0] for _ in range(len(num))]

    for i in range(len(num)):
        tree[i][3] = num[i]

    for i in range(len(links)):
        if links[i][0] != -1:
            child = links[i][0]
            tree[i][0] = child
            tree[child][2] = i

        if links[i][1] != -1:
            child = links[i][1]
            tree[i][1] = child
            tree[child][2] = i

    for i in range(len(tree)):
        if tree[i][2] == -1:
            root = i

    def tree_sum(root:int):
        left = 0
        right = 0
        if tree[root][0] != -1:
            left = tree_sum(tree[root][0])
        if tree[root][1] != -1:
            right = tree_sum(tree[root][1])
        return left + tree[root][3] + right

    values = []

    # 트리 쪼개기
    for _ in range(k-1):
        roots = []
        for i in range(len(tree)):
            # 부모가 -1임 -> root다
            if tree[i][2] == -1:
                roots.append(i)

        max_sum = 0
        max_root = -1
        # 가장 큰 sum을 갖는 root를 찾고
        for root in roots:
            tmp_sum = tree_sum(root)
            if  tmp_sum > max_sum:
                max_sum = tmp_sum
                max_root = root
        
        # 해당 root를 쪼갬
        left = 0
        right = 0
        if tree[max_root][0] != -1:
            left = tree_sum(tree[max_root][0])
        if tree[max_root][1] != -1:
            right = tree_sum(tree[max_root][1])
    
        # 두 child 중 큰 sub_child의 root를 root로 끄집어 올림
        if left > right:
            tree[tree[max_root][0]][2] = -1
            tree[max_root][0] = -1
        else:
            tree[tree[max_root][1]][2] = -1
            tree[max_root][1] = -1

    for i in range(len(tree)):
        if tree[i][2] == -1:
            values.append(tree_sum(i))

    answer = max(values)
    # print(values)


    return answer


solution(3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], 	[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]])
# solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]])