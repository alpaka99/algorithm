import sys
sys.stdin = open('input.txt','r')

N = int(input())

for tc in range(N):
    list1=[]
    total = 0
    list1 = list(map(int,input().split()))

    for num in list1:
        total += num
    result = round(total/len(list1))
    print("#{} {}".format(tc+1, result))