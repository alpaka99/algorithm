import sys
sys.stdin = open('input.txt', 'r')
def solution(A:int, B:int, time:int):
    time += 1
    # A를 B로 바꾸는데
    # 1. 2를 곱한다
    # 2. 1을 수의 가장 오른쪽에 추가한다.
    # DP로 해야하나?
    if B == A:
        return time
    if B < A:
        return -1

    times_2 = solution(A*2, B, time)
    append_1 = solution((A*10)+1, B, time)
    if times_2 != (-1) and append_1 != (-1):
        return min(append_1, times_2)
    else:
        if times_2 == -1:
            return append_1
        else:
            return times_2


for _ in range(int(input())):
    A, B = map(int, input().split())
    # print(A, B)

    print(solution(A, B, 0))