import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    # 숫자의 갯수
    N = int(input())
    # 정렬하지 않은 리스트
    unsorted = list(map(int, input().split()))

    for i in range(len(unsorted),0,-1):
        for j in range(i-1, -1, -1):
            if unsorted[j] < unsorted[j-1]:
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
            print(*unsorted)
