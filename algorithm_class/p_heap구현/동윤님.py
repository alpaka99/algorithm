def heap_push(value):
    # value -> node의 값 / heap_count -> node의 index
    global heap_count
    heap_count += 1
    heap[heap_count] = value
    parent = heap_count//2
    child = heap_count
    while parent > 0 and heap[child] < heap[parent]:
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent //= 2
    # child & parent (parent = child // 2)

# 삭제
"""
1) 루트 노드의 원소 삭제
2) 마지막 노드 삭제 후 루트 노드에 삽입 (heap의 모양 유지)
3) (자리가 확정될 때까지) 부모 & 자식 비교하며 swap 
"""
def heap_pop():
    global heap_count
    val = heap[1]
    heap[1] = heap[heap_count]
    parent = 1
    if heap[2] < heap[3]:
        child = 2
    else:
        child = 3

    while child < heap_count:
        if heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            parent = child
            child *= 2
        else:
            break

    heap_count -= 1
    return val


heap_count = 0
temp = [7, 2, 5, 3, 4, 6, 9]
# temp = [ 10, 9, 8, 7, 2, 5, 3, 4, 6,]
# temp = [10, 9, 8, 7, 6, 5, 4, 3, 2]
N = len(temp)
heap = [0] * (N+1)

##########################################################

# 삽입 연산
for i in range(N):
    heap_push(temp[i])

print(*heap) # 0 2 3 5 7 4 6

# 삭제 연산
for i in range(N):
    print(heap_pop(), end=' ') # 2 3 4 5 6 7