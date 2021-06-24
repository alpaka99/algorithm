"""
quick-정렬의 포인트: pivot을 기준으로 작은것은 왼쪽, 큰것은 오른쪽으로 나눠서
또 그 둘을 quick 정렬을 돌려준다.
"""
import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(unsorted):
    # 재귀로 짤거니까 탈출조건
    if len(unsorted) <= 1:
        return unsorted

    # 우선 피봇을 정하고
    # pivot을 리스트로 만든 이유는 pivot이랑 같은값이 여러개 나올 수 있으니까
    pivot = []
    pivot.append(unsorted[0])


    # 피봇보다 작은것은 left, 큰것은 right에 저장
    left = []
    right = []
    # 0번쨰 인덱스는 pivot으로 설정해 줬으니까 건너뜀
    for i in range(1, len(unsorted)):
        # pivot보다 작으면 왼쪽리스트에 저장
        if unsorted[i] < pivot[0]:
            left.append(unsorted[i])
        # pivot보다 크면 오른쪽 리스트에 저장
        elif unsorted[i] > pivot[0]:
            right.append(unsorted[i])
        # pivot이랑 같으면 pivot리스트에 저장
        else:
            pivot.append(unsorted[i])

    # 각각의 left와 right에 대해서 또 quick 정렬을 실행해주는게 point
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    # 정렬된것 병합하면서 return
    # pivot리스트로 만드니까 굉장히 직관적이고 left나 rigth이 빈 리스트여도 일괄적용 가능
    return sorted_left +pivot + sorted_right

for tc in range(1, int(input())+1):
    N = int(input())

    unsorted = list(map(int, input().split()))

    print("#{}".format(tc),*quick_sort(unsorted))