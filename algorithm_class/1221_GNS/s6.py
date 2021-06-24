import sys
sys.stdin = open("input.txt", "r")

# 연욱님의 177ms는 도대체 어떻게 한걸까? 궁금하다
for _ in range(1, int(input())+1):
    # # 기호와 함께 tc 번호
    tc, N = map(str,input().split())
    unsorted = list(input().split())
    print(unsorted)
    num = []
    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in range(len(new_rule)):
        test = 0
        for j in range(2):
            test += ord(new_rule[i][j])
        num.append(test-100)
    num.sort()
    print(num)