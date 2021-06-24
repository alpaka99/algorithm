"""
왜 merge_sort에서 len(arr) == 1이면 통과하는데 그렇지않고
len(arr) <= 1이면 runtime error가 뜨지??
이것때문에 6번 넘게 틀렸는데;
한번 더 깊게 들어가지는 않을텐데..?
"""


import sys
sys.stdin = open('input.txt', 'r')

global cnt

def merge_sort(arr:list):
    if len(arr) == 1:
        return arr

    N = len(arr)
    # 분할
    left = arr[:N//2]
    right = arr[N//2:]
    
    # 정복
    return merge(merge_sort(left), merge_sort(right))

# 정복
def merge(left:list, right:list):
    global cnt
    # 문제 조건
    if left[-1] > right[-1]:
        cnt += 1

    # 병합하여 반환할 리스트
    arr = []

    # left와 right의 현재 idx를 가리키는 포인터
    left_idx, right_idx = 0, 0

    l, r = len(left), len(right)

    while left_idx<l and right_idx<r:
        if left[left_idx] <= right[right_idx]:
            arr.append(left[left_idx])
            left_idx += 1
        else:
            arr.append(right[right_idx])
            right_idx += 1

    # 남은 숫자들 넣기
    if left_idx == l:
        arr += right[right_idx:]
    else:
        arr += left[left_idx:]
    
    # 하나가 다 없어질때까지 while문 돌리고
    # while left and right:
    #     if left[0] <= right[0]:
    #         arr.append(left.pop(0))
    #     else:
    #         arr.append(right.pop(0))
    #
    # # 남은거 다 넣기
    # arr += left
    # arr += right
    return arr




for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 병합 과정에서 왼쪽 마지막 왼소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
    cnt = 0

    ans = merge_sort(numbers)

    print("#{} {} {}".format(tc, ans[N//2],cnt))
    # print(ans)