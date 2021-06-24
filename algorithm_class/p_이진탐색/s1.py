import sys
sys.stdin = open("input.txt", 'r')


def binary_search(p, num):
    start = 1
    end = p

    count = 0
    mid = 0

    while mid != num :

         mid = int((start+end)/2)
         count += 1
         if num < mid:
            end = mid
            # 우리가 찾는 값이 중간보다 위에 있음
         elif num > mid:
            start = mid
            # 우리가 찾던 값
         else:
            return count



for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    count_a = binary_search(P, A)
    count_b = binary_search(P, B)

    if count_a < count_b:
        ans = 'A'
    elif count_a > count_b:
        ans = 'B'
    else:
        ans = 0
    print("#{} {}".format(tc, ans))