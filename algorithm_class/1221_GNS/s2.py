import sys
sys.stdin = open("input.txt", "r")

# 2. enumerate와 count list를 이용한 방법 -> 근데 더 느림
# 295ms 66,640 kb
for _ in range(1, int(input()) + 1):
    # # 기호와 함께 tc 번호
    tc, N = map(str, input().split())

    # first =  ['Z', 'O', 'T', 'T', 'F', 'F', 'S', 'S', 'E', 'N']
    # second = ['R', 'N', 'W', 'H', 'O', 'I', 'I', 'V', 'G', 'I']

    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    unsorted = list(map(str, input().split()))

    # key를 가지고 해석할 수 있게 해주는 decoder
    decoder = list(enumerate(new_rule))
    # 갯수를 저장해주는 counting list
    count = [0]*10

    # decode 하여 count의 해당 위치에 차곡차곡 쌓음
    for i in range(len(unsorted)):
        for j in range(len(decoder)):
            if unsorted[i] == decoder[j][1]:
                count[j] += 1

    # 다 저장한 후에 출력
    print(tc)
    for i in range(len(count)):
        for _ in range(count[i]):
            print(new_rule[i], end = " ")
    print()