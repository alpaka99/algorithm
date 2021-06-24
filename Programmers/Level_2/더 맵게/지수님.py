global element_cnt
# 삽입
def heappush(tree, value):
    global element_cnt
    element_cnt += 1

    # 1. 값 추가
    tree[element_cnt] = value

    idx = element_cnt
    while idx > 0 and tree[idx] < tree[idx // 2]:
        tree[idx], tree[idx // 2] = tree[idx // 2], tree[idx]
        idx //= 2

# 삭제
def heappop(tree):
    global element_cnt

    return_value = tree[1]
    tree[1], tree[element_cnt] = tree[element_cnt], 0
    element_cnt -= 1

    parent = 1
    child = parent * 2
    if child + 1 <= element_cnt:
        if tree[child + 1] < tree[child]:
            child += 1

    while child <= element_cnt and tree[parent] > tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        parent = child
        child *= 2

        if child + 1 <= element_cnt:
            if tree[child + 1] < tree[child]:
                child += 1

    return return_value


def solution(scoville, K):
    global element_cnt
    element_cnt = 0
    tree = [0]*(len(scoville)+1)


    # 함수 실행
    for sco in scoville:
        heappush(tree, sco)

    mix = 0
    while tree[2] != 0 and tree[1] < K:
        mix += 1
        new_scovile = heappop(tree) + heappop(tree)*2
        heappush(tree, new_scovile)

    if tree[1] >= K:
        return mix
    else:
        return -1


# print(solution([1, 2, 3, 9, 10, 12], 7), 2)
# print(solution([1, 1, 1], 4), 2)
# print(solution([10, 10, 10, 10, 10], 100), 4)
# print(solution([1, 2, 3, 9, 10, 12], 7), 2)
# print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
# print(solution([0, 0, 0, 0], 7), -1)
# print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
# print(solution([0, 0, 3, 9, 10, 12], 0), 0)
# print(solution([0, 0, 3, 9, 10, 12], 1), 2)
# print(solution([0, 0], 0), 0)
# print(solution([0, 0], 1), -1)
# print(solution([1, 0], 1), 1)
# print(solution([1, 2], 3), 1)
# print(solution([0, 0, 0, 0, 3], 4),4)
# print(solution([1, 1, 2], 3), 2)