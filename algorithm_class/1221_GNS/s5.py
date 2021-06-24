import sys
sys.stdin = open("input.txt", "r")

# 5. if- elif
# 320ms 66392kb
for _ in range(1, int(input())+1):
    # # 기호와 함께 tc 번호
    tc, N = map(str,input().split())
    unsorted = list(input().split())

    count = [0]*10
    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(unsorted)):
        if unsorted[i] == 'ZRO':
            count[0] += 1
        elif unsorted[i] == 'ONE' :
            count[1] += 1
        elif unsorted[i] == 'TWO':
            count[2] += 1
        elif unsorted[i] == 'THR':
            count[3] += 1
        elif unsorted[i] == 'FOR':
            count[4] += 1
        elif unsorted[i] == 'FIV':
            count[5] += 1
        elif unsorted[i] == 'SIX':
            count[6] += 1
        elif unsorted[i] == 'SVN':
            count[7] += 1
        elif unsorted[i] == 'EGT':
            count[8] += 1
        elif unsorted[i] == 'NIN':
            count[9] += 1

    # 다 저장한 후에 출력
    print(tc)
    for i in range(len(count)):
        for _ in range(count[i]):
            print(new_rule[i], end = " ")
    print()

