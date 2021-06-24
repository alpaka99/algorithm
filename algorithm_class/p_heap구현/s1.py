#1. 최소힙 직접 구현

# 삽입
"""
1) heap 가장 마지막에 원소 삽입
2) 부모 & 자식 비교하며 swap
"""
def heap_push(value):
    # value -> node의 값 / heap_count -> node의 index
    global heap_count
    heap_count += 1
    # child & parent (parent = child // 2)
    # 삽입

    heap[heap_count] = value


    # 부모랑 비교
    # 오른쪽 자식이면 계속 비교
    idx = heap_count
    while idx > 0:
        # 부모가 자식보다 작아야함
        if heap[idx//2] > heap[idx]:
            heap[idx // 2], heap[idx] = heap[idx], heap[idx // 2]
            idx //= 2
        else:
            break


# 삭제
"""
1) 루트 노드의 원소 삭제
2) 마지막 노드 삭제 후 루트 노드에 삽입 (heap의 모양 유지)
3) (자리가 확정될 때까지) 부모 & 자식 비교하며 swap 
"""
def heap_pop():
    global heap_count
    # 1)
    idx = heap_count
    ans = heap[1]

    # 2)
    tmp = heap[idx]
    heap[1] = tmp
    heap[idx] = 0


    # 3)
    # 자식 노드 2개 중 더 작은걸 끌어올리자
    i = 1
    while i< heap_count//2:
        if heap[i*2] < heap[i*2+1]:
            change_idx = i*2
        else:
            change_idx=i*2+1

        if heap[i] > heap[change_idx]:
            heap[i], heap[change_idx] = heap[change_idx], heap[i]
            i = change_idx
        else:
            break

    heap_count -= 1
    # print(heap)

    return ans

heap_count = 0
temp = [7, 2, 5, 3, 4, 6]
# temp = [7, 2, 5, 3, 4, 6, 0]
N = len(temp)
heap = [0] * (N+1)
# heap = []
##########################################################

# 삽입 연산
for i in range(N):
    heap_push(temp[i])

print(*heap) # 0 2 3 5 7 4 6

# 삭제 연산
for i in range(N):
    print(heap_pop(), end=' ') # 2 3 4 5 6 7