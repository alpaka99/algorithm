import sys
sys.stdin = open("input.txt", 'r')

# 재귀함수
# 인자로 시작과 끝, 그리고 목표지점을 받습니다
def binary_recursion(start, end, goal):
    # 인자로 받아온 시작과 끝으로 중간지점을 알아봅니다.
    mid = int((start+end)/2)
    # 재귀함수의 가장 큰 포인트인 종료조건
    if mid == goal:
        return 1
    # 만약 중간값이 목표보다 위에 있으면
    # 끝을 중간으로 떙겨와서 다시 탐색
    elif mid > goal:
        return binary_recursion(start, mid, goal) + 1
    # 만약 중간값이 목표보다 아래에 있으며 있으면
    # 시작을 중간으로 땡겨와서 다시 탐색
    else:
        return binary_recursion(mid, end, goal) + 1




for tc in range(1, int(input())+1):
    P, A, B = map(int, input().split())
    count_a = binary_recursion(1, P, A)
    count_b = binary_recursion(1, P, B)

    if count_a < count_b:
        ans = 'A'
    elif count_a > count_b:
        ans = 'B'
    else:
        ans = 0
    print("#{} {}".format(tc, ans))