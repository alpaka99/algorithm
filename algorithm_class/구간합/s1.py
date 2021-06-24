import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    num_list = list(map(int,input().split()))

    max_value = 0
    min_value = 100000 * m
    for i in range(len(num_list)-m+1):
        cur_sum = 0
        for j in range(i, i+m):
            cur_sum += num_list[j]


        if max_value < cur_sum:
            max_value = cur_sum
        if min_value > cur_sum:
            min_value = cur_sum
    print(max_value - min_value)