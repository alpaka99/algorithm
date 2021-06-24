import sys
from pandas import DataFrame as df
sys.stdin = open("input.txt", "r")

# 1. 26*26 배열을 만들고 ord로 해당 위치를 찾아서 저장하는 방법
# 266ms 66,100kb
for _ in range(1, int(input())+1):
    # # 기호와 함께 tc 번호
    tc, N = map(str,input().split())

    #first =  ['Z', 'O', 'T', 'T', 'F', 'F', 'S', 'S', 'E', 'N']
    #second = ['R', 'N', 'W', 'H', 'O', 'I', 'I', 'V', 'G', 'I']

    new_rule = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    unsorted = list(map(str,input().split()))

    # 26*26의 2차원 배열 만들자
    matrix = [[0]*26 for _ in range(26)]

    # ord(A) = 65
    # 2번째 글자 까지는 똑같은게 없으니까 2번째 글자까지 ord를 해서 보내자
    for i in range(len(unsorted)):
        matrix[ord(unsorted[i][0]) - 65][ord(unsorted[i][1]) - 65] += 1

    print(df(matrix))
    print(tc)
    # new_rule의 요소 하나하나마다 프린트 하는데
    for i in range(len(new_rule)):
        # 해당요소의 갯수를 저장해놓은 위치로 가서 프린트
        for _ in range(matrix[ord(new_rule[i][0])-65][ord(new_rule[i][1])-65]):
            print(new_rule[i], end = ' ')
    print()