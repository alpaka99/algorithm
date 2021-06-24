import sys
sys.stdin = open('input.txt', 'r')

def quick_sort(arr:list, left:int, right:int):
    pivot = arr[left]

    while left <= right:
        while arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]




for tc in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    quick_sort(numbers,0,N-1)
    print(numbers)