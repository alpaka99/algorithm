import sys
sys.stdin = open("input.txt", "r")

# 4. 그 자리에서 하나씩 비교하면서 정렬 후 바로 출력
# 이건 tc 1 출력하는데에 1분 15초걸림 개에바
for _ in range(1, int(input()) + 1):
    # # 기호와 함께 tc 번호
    tc, N = map(str, input().split())

    # first =  ['Z', 'O', 'T', 'T', 'F', 'F', 'S', 'S', 'E', 'N']
    # second = ['R', 'N', 'W', 'H', 'O', 'I', 'I', 'V', 'G', 'I']

    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    unsorted = list(map(str, input().split()))

    for i in range(len(unsorted)-1):
        for j in range(i, len(unsorted)):
            for x in range(len(new_rule)):
                if unsorted[i] == new_rule[x]:
                    a = x
                if unsorted[j] == new_rule[x]:
                    b = x
            if a > b:
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
    print(tc)
    print(*unsorted)