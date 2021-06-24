import sys
sys.stdin = open('input.txt', 'r')

def insert(heap:list, n:int):
    length = len(heap)
    heap.append(n)

    while length:
        if heap[length] < heap[length//2]:
            heap[length], heap[length//2] = heap[length//2], heap[length]
            length //= 2
        else:
            break




for tc in range(1, int(input())+1):
    # N
    N = int(input())
    not_heap = list(map(int, input().split()))

    # 0을 넣어줘야 처음에 2에서 1로갈때 내가 원하는대로 동작하게 됨
    heap = [0]

    for i in range(len(not_heap)):
        insert(heap, not_heap[i])

    length = len(heap)-1
    ans = 0
    while length > 0:
        length //= 2
        ans += heap[length]

    print("#{} {}".format(tc,ans))