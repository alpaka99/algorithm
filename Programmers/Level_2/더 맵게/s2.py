import heapq

def solution(scoville, K):
    answer = 0

    # 1) 최소힙을 만듬
    
    # heapq 공식문서에서 이미 있는 list를 heapify를 이용해 
    # heap으로 만드는게 비교를 많이 줄여서 더 좋다고 함
    heapq.heapify(scoville)
    heap = scoville

    while len(heap) > 1:
        if heap[0] >= K:
            return answer

        answer += 1
        # 2) 최소힙에서 2개를 뽑아서 두번쨰에 뽑은거 *2
        new = heapq.heappop(heap) + heapq.heappop(heap)*2

        # 3) 최소힙에 삽입
        heapq.heappush(heap, new)

        # 4) 종료조건 만족하는지 확인


    if heap[0] >= K:
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