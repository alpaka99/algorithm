

def binary_search(target:int, l:int, r:int, cnt:int):
    m = (l+r)//2

    tmp = numbers[m]

    if target == tmp:
        return cnt

    if target < tmp:
        r = m-1
    else:
        l = m+1
    return binary_search(target, l, r, cnt+1)





for tc in range(1, int(input())+1):
    # 숫자 목록 길이 N, 탐색 횟수 M
    N, M = map(int, input().split())
    targets = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_val = 987654321
    min_num = -1

    for target in targets:
        if target not in numbers:
            continue
        nums = numbers[:]
        ans = binary_search(target, 0, N-1, 1)
        if ans < min_val:
            min_val = ans
            min_num = target
    print("#{} {} {}".format(tc,min_num, min_val))