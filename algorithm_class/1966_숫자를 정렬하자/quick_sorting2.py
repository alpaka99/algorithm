"""
quick-정렬의 포인트: pivot을 기준으로 작은것은 왼쪽, 큰것은 오른쪽으로 나눠서
또 그 둘을 quick 정렬을 돌려준다.
"""
import sys
sys.stdin = open('input.txt', 'r')

# 왼쪽, 오른쪽 인덱스로 파티션을 나눠서 quick정렬을 돌리는 방법
def quick_sort(unsorted, start, end):
    # 이것도 재귀니까 탈출조건
    N = len(unsorted)
    if N <= 1:
        return
    
    # 우선은 pivot 설정
    pivot = unsorted[0]

    # 시작점과 끝점이 만날때까지
    while start <= end:
        pass
    
    # 이제 왼쪽, 오른쪽의 혼란스러운 값들에 대해 또 quick정렬


    return



    # 왼쪽 오른쪽 포인터로 구하자
for tc in range(1, int(input())+1):
    N = int(input())

    unsorted = list(map(int, input().split()))

    start = 1
    end = len(unsorted)-1

    quick_sort(unsorted, start, end)
    print(unsorted)