import sys
sys.stdin = open("input.txt", "r")

# 3. dictionary를 이용
# 288ms 66,096kb
for _ in range(1, int(input()) + 1):
    # # 기호와 함께 tc 번호
    tc, N = map(str, input().split())

    # first =  ['Z', 'O', 'T', 'T', 'F', 'F', 'S', 'S', 'E', 'N']
    # second = ['R', 'N', 'W', 'H', 'O', 'I', 'I', 'V', 'G', 'I']

    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    unsorted = list(map(str, input().split()))

    decode = {}
    for i in range(len(new_rule)):
        decode[new_rule[i]] = 0

    for i in range(len(unsorted)):
        decode[unsorted[i]] += 1

    print(tc)
    for i in range(len(new_rule)):
        for _ in range(decode[new_rule[i]]):
            print(new_rule[i], end = " ")
    print()