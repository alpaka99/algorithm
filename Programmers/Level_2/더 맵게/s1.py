"""
왜 만든 heap으로는 안됨?
"""
global heap_count

def heap_push(heap:list, n:int):
    # heap에 마지막에
    global heap_count
    heap_count += 1

    # 마지막에 삽입
    pos = heap_count
    heap[pos] = n

    # 부모 자식 비교
    while pos > 0:
        parent = pos//2
        if heap[pos] < heap[parent]:
            heap[pos], heap[parent] = heap[parent], heap[pos]
            pos = parent
        else:
            break



def heap_pop(heap:list):
    # 가장 작은 값 ans에 저장
    ans = heap[1]

    # 가장 마지막값을 힙의 루트에 저장 후 끝에서 삭제
    global heap_count
    heap[1] = heap[heap_count]
    heap[heap_count] = 0

    # 힙카운트 1 감소
    heap_count -= 1


    i = 1
    # 자식이 있는 범위까지만 자식과 나를 비교
    # 힙은 완전이진이니까 왼쪽자식의 idx가 범위 안인지 밖인지로 판단
    while i*2 < heap_count:
        # 두 자식 중 작은 값 찾기
        left = i * 2
        right = i * 2 + 1

        child = left if heap[left] < heap[right] else right

        if heap[i] > heap[child]:
            heap[i], heap[child] = heap[child], heap[i]
            i = child
        else:
            break
    return ans


def solution(scoville, K):
    answer = 0

    
    # 1) 최소 힙 만들기
    heap = [0]+sorted(scoville)

    global heap_count
    heap_count = 0

    for i in range(len(scoville)):
        heap_push(heap,scoville[i])
    
    # 한번도 안돌아도 최소값이 K 이상
    # if heap[1] >= K:
    #     return answer

    while heap_count >= 1:
        # 2) 종료조건 만족하는지 확인
        if heap[1] >= K:
            return answer

        # 3) 최소힙에서 2개를 뽑아서 두번쨰에 뽑은거 *2
        new = heap_pop(heap) + heap_pop(heap)*2

        # 4) 최소힙에 삽입
        heap_push(heap, new)

        answer += 1



    if heap[1] >= K:
        return answer
    else:
        return -1



print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([1, 1, 1], 4), 2)
print(solution([10, 10, 10, 10, 10], 100), 4)
print(solution([1, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 2, 3, 9, 10, 12], 7), 2)
print(solution([0, 0, 3, 9, 10, 12], 7), 3)
print(solution([0, 0, 0, 0], 7), -1)
print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
print(solution([0, 0, 3, 9, 10, 12], 0), 0)
print(solution([0, 0, 3, 9, 10, 12], 1), 2)
print(solution([0, 0], 0), 0)
print(solution([0, 0], 1), -1)
print(solution([1, 0], 1), 1)
print(solution([1, 2], 3), 1)
print(solution([0, 0, 0, 0, 3], 4),4)
print(solution([1, 1, 2], 3), 2)